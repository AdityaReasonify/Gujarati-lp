#!/usr/bin/env python3
"""Disk-derived progress tracker + stall watchdog for the gujarati-lp pipeline.

State is derived ONLY from output files on disk, so it survives session death.
Emits:
  output<STD>/PROGRESS.md    human-readable stage matrix
  output<STD>/progress.json  machine-readable + ready-to-use resume args
"""
import json, os, sys, time, glob, re

ROOT = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp"
SESSIONS = "/Users/aditya/.claude/projects/-Users-aditya-Downloads-Gujarati-lp"
STD = int(sys.argv[1]) if len(sys.argv) > 1 else 6

def chapter_count(std):
    """Numbered chapters for this standard, from its manifest (front matter,
    revision and purak-vachan entries have non-numeric 'no' and are excluded)."""
    try:
        m = json.load(open(f"/Users/aditya/Downloads/Gujarati-lp/Textbooks-pdf/std-{std}/manifest.json"))
        items = m if isinstance(m, list) else m.get("chapters", m.get("items", []))
        nums = [int(x["no"]) for x in items if isinstance(x, dict) and str(x.get("no", "")).isdigit()]
        return max(nums) if nums else 15
    except Exception:
        return 15

NCH = chapter_count(STD)

# stage -> the declared output file that proves it ran
STAGES = [
    ("A1",  "01_meta.json",                 "ingestion+genre"),
    ("A2",  "02_structure.json",            "structure"),
    ("A4",  "04_converged.json",            "mapping convergence"),
    ("A11", "11_pages.json",                "pagination"),
    ("A5",  "05_with_content.json",         "verbatim"),
    ("A7",  "07_pitfalls.json",             "genre pitfalls"),
    ("A8",  "08_sensitivity.json",          "sensitivity"),
    ("A9",  "09_media.json",                "media planning"),
    ("A10", "10_exercise_solutions.json",   "exercise solutions"),
    ("A12", "12_authoring.json",            "runtime authoring"),
    ("A16", "16_publication.json",          "publication authoring"),
    ("A13", "13_merged.json",               "assembly QC"),
    ("A14", "learning_plan_logical.json",   "logical plan"),
]
IDLE_WEDGE_MIN = 15.0   # calibrated: 5-10 min silences are NORMAL (A1/A12 end in one big generation)


def chapter_state(std, ch):
    d = os.path.join(ROOT, f"output{std}", f"ch{ch:02d}")
    if not os.path.isdir(d):
        return {"ch": ch, "done": [], "exists": False, "lp2": False, "bytes": 0, "last_write": None}
    done, newest = [], 0.0
    for s, f, _ in STAGES:
        p = os.path.join(d, f)
        if os.path.exists(p) and os.path.getsize(p) > 0:
            done.append(s)
            newest = max(newest, os.path.getmtime(p))
    lp2 = False
    vr = os.path.join(d, "validation_report.md")
    if os.path.exists(vr):
        try:
            lp2 = "## LP2 validator" in open(vr, encoding="utf-8", errors="replace").read()
        except Exception:
            pass
    total = sum(os.path.getsize(p) for p in glob.glob(os.path.join(d, "*")) if os.path.isfile(p))
    return {"ch": ch, "done": done, "exists": True, "lp2": lp2, "bytes": total,
            "last_write": newest or None}


import os, glob

def _workflows_root():
    """Locate the current session's workflow directory.

    The session id changes on every restart and on an account switch, so it must
    never be hardcoded. Prefer $GLP_SESSION; otherwise take the session directory
    whose workflows folder was touched most recently.
    """
    base = "/Users/aditya/.claude/projects/-Users-aditya-Downloads-Gujarati-lp"
    env = os.environ.get("GLP_SESSION")
    if env:
        return os.path.join(base, env, "subagents", "workflows")
    cands = glob.glob(os.path.join(base, "*", "subagents", "workflows"))
    return max(cands, key=os.path.getmtime) if cands else ""

MY_SESSION = os.environ.get("GLP_SESSION") or os.path.basename(os.path.dirname(os.path.dirname(_workflows_root() or "x/y/z")))


def live_agents():
    """Agents of workflow runs OWNED BY THIS SESSION that are still being written.

    Scoped to this session's own runs on purpose: PID-liveness is unreliable (pids get
    recycled), and every other session's agents are corpses we must not count.
    A run is considered active only if its journal was touched in the last 30 min.
    """
    out, now = [], time.time()
    root = os.path.join(SESSIONS, MY_SESSION, "subagents", "workflows")
    for wf in glob.glob(os.path.join(root, "wf_*")):
        jp = os.path.join(wf, "journal.jsonl")
        if not os.path.exists(jp) or (now - os.path.getmtime(jp)) > 30 * 60:
            continue
        done, started = set(), []
        for line in open(jp, encoding="utf-8", errors="replace"):
            try:
                r = json.loads(line)
            except Exception:
                continue
            a = r.get("label") or r.get("agentId")
            if r.get("type") == "started":
                started.append(a)
            elif r.get("type") == "result":
                done.add(a)
        # A run that has been stopped keeps its agent transcripts on disk forever. Without
        # these two gates every stopped run's agents accumulate into the wedge count
        # permanently — on 2026-08-25 this reported 9 wedged agents across 3 DEAD runs
        # while all 4 live runs were healthy. Same class as the supervisor.sh fix.
        run_fresh = any(
            (now - os.path.getmtime(x)) < 15 * 60
            for x in glob.glob(os.path.join(wf, "agent-*.jsonl"))
        )
        if not run_fresh:
            continue
        for a in [x for x in started if x not in done]:
            f = os.path.join(wf, f"agent-{a}.jsonl")
            if not os.path.exists(f):
                continue
            try:
                with open(f, "rb") as fh:
                    fh.seek(max(0, os.path.getsize(f) - 4000))
                    if b"[Request interrupted by user]" in fh.read():
                        continue          # killed, not slow
            except OSError:
                continue
            st = os.stat(f)
            out.append({"run": os.path.basename(wf), "agent": a,
                        "idle_min": round((now - st.st_mtime) / 60.0, 1),
                        "mb": round(st.st_size / 1e6, 1)})
    return sorted(out, key=lambda x: -x["idle_min"])


def rate_limited(wf_dir, minutes=10):
    """Recent 429s across a run's agent logs — the signal to LOWER concurrency, not restart."""
    now, hits = time.time(), 0
    for f in glob.glob(os.path.join(wf_dir, "agent-*.jsonl")):
        if now - os.path.getmtime(f) > minutes * 60:
            continue
        try:
            with open(f, "rb") as fh:
                fh.seek(max(0, os.path.getsize(f) - 200_000))
                hits += len(re.findall(rb"429|rate.?limit", fh.read(), re.I))
        except Exception:
            pass
    return hits


def main():
    now = time.time()
    chapters = [chapter_state(STD, c) for c in range(1, NCH + 1)]
    agents = live_agents()
    pack_writes = [0.0]
    for sub in ("reference", "agents", "profiles"):
        for f in glob.glob(os.path.join(ROOT, sub, "**", "*.md"), recursive=True):
            try:
                pack_writes.append(os.path.getmtime(f))
            except OSError:
                pass
    newest_output = max([c["last_write"] or 0 for c in chapters] + [max(pack_writes)])
    quiet_min = (now - newest_output) / 60.0 if newest_output else None

    # NO WEDGE VERDICT HERE, deliberately. Stall detection lives in health.py and
    # supervisor.sh, which scope to a known run id. progress.py sees every run on disk, so
    # any wedge count it produces mixes live agents with corpses from stopped runs — it
    # reported 9 wedged agents across 3 DEAD runs on 2026-08-25 while all 4 live runs were
    # healthy. Three thresholds for one question is two too many; this file reports
    # PROGRESS, and progress is what the chapter files say.
    verdict = f"{len(agents)} agent(s) writing recently" if agents else "no agents writing"

    done_all = [c for c in chapters if len(c["done"]) == len(STAGES)]
    resume_args = {"std": STD, "concurrency": 3,
                   "chapters": [{"ch": c["ch"], "done": c["done"]} for c in chapters]}
    blob = {"generated_at": time.strftime("%Y-%m-%d %H:%M:%S"), "std": STD,
            "verdict": verdict, "complete_chapters": [c["ch"] for c in done_all],
            "chapters": chapters, "live_agents": agents, "stage_count": len(STAGES), "resume_args": resume_args}

    outdir = os.path.join(ROOT, f"output{STD}")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "progress.json"), "w") as f:
        json.dump(blob, f, indent=2, ensure_ascii=False)

    keys = [s for s, _, _ in STAGES]
    L = ["# gujarati-lp std-%d progress" % STD, "",
         "_%s_ — **%s**" % (blob["generated_at"], verdict), "",
         "| ch | " + " | ".join(keys) + " | LP2 | done |",
         "|---|" + "---|" * (len(keys) + 2)]
    for c in chapters:
        cells = ["✅" if s in c["done"] else "·" for s in keys]
        L.append("| %02d | %s | %s | %d/%d |" % (c["ch"], " | ".join(cells),
                 "✅" if c["lp2"] else "·", len(c["done"]), len(keys)))
    L += ["", "## Live agents", ""]
    L += ["- none" ] if not agents else [
        "- `%s` idle %.1fm (%.1f MB) in %s" % (a["agent"][:17], a["idle_min"], a["mb"], a["run"]) for a in agents]
    L += ["", "## Resume", "",
          "```", "Workflow({scriptPath: \"/Users/aditya/Downloads/Gujarati-lp/scratch/chapter-runner-resume.js\",",
          "          args: <the resume_args object in progress.json>})", "```",
          "", "Stage legend: " + ", ".join("%s=%s" % (s, d) for s, _, d in STAGES)]
    with open(os.path.join(outdir, "PROGRESS.md"), "w") as f:
        f.write("\n".join(L) + "\n")

    print(f"[{blob['generated_at']}] {verdict}")
    for c in chapters:
        if c["done"]:
            print(f"  ch{c['ch']:02d}: {len(c['done'])}/{len(STAGES)}  {'+'.join(c['done'])}"
                  + ("  LP2✓" if c["lp2"] else ""))
    if wedged:
        print("  WEDGE CANDIDATES: " + ", ".join(f"{a['agent'][:17]}({a['idle_min']}m)" for a in wedged))


if __name__ == "__main__":
    main()
