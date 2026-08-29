#!/usr/bin/env python3
"""Health check for the gujarati-lp pipeline.  Usage: python3 scratch/health.py [run_id]

Compares each live agent's IDLE time against a bar derived from that stage's MEASURED
maximum duration. Raw idle is not a stall signal here: an agent writes its transcript
only when a message completes, so a healthy agent mid-generation shows idle climbing
for tens of minutes (A12 runs up to 60m, A10 up to 47m).
"""
import json, os, sys, time, re, glob

BASE = "/Users/aditya/.claude/projects/-Users-aditya-Downloads-Gujarati-lp"

def workflows_root():
    """Session id changes on restart / account switch, so never hardcode it."""
    env = os.environ.get("GLP_SESSION")
    if env:
        return os.path.join(BASE, env, "subagents", "workflows")
    cands = glob.glob(os.path.join(BASE, "*", "subagents", "workflows"))
    return max(cands, key=os.path.getmtime) if cands else ""

# Bars = 1.25x the MEASURED maximum per stage, from 25-146 completed agents each
# (re-measured 2026-08-23). Earlier bars came from 1-8 samples and were badly wrong:
# A16's real median 12.3m exceeded its old 10m bar, so every A16 was doomed to alert.
# Bars = 1.5x the longest SILENT GAP ever observed inside a SUCCESSFULLY COMPLETED agent
# of that stage, measured across 611 finished agents (2026-08-24). This is stricter and
# better-grounded than duration-based bars: A12 drops 130m->58m, A10 85m->52m, A13
# 30m->10m, A11 15m->5m. A healthy agent has never exceeded these; anything past one is
# doing something no successful run of that stage has done.
BARS = {'01': 25, '02': 20, '04': 12, '05': 18, '07': 32, '08': 8, '09': 12, '10': 52, '11': 5, '12': 58, '13': 10, '14': 5, '15': 5, '16': 18}
# Median TOTAL duration per stage, measured across completed agents. Shown so progress
# reads as "23m into a 44m job" instead of an idle counter that means nothing on its own.
MEDIAN = {"01":12.6,"02":14.1,"04":6.9,"05":18.4,"07":19.6,"08":1.8,"09":9.0,
          "10":36.1,"11":0.7,"12":43.9,"13":11.8,"14":7.0,"15":1.4,"16":12.3}

NAMES = {"01":"ingestion","02":"structure","04":"convergence","05":"verbatim","07":"pitfalls",
         "08":"sensitivity","09":"media","10":"solutions","11":"pagination","12":"authoring",
         "13":"QC","14":"logical","15":"textbook","16":"publication"}

def main():
    B = workflows_root()
    if not B:
        print("no workflow directory found"); return
    if len(sys.argv) > 1:
        runs = [sys.argv[1]]
    else:
        # newest run only — a stopped workflow leaves transcripts that look merely idle
        cands = [(os.path.getmtime(os.path.join(p, "journal.jsonl")), os.path.basename(p))
                 for p in glob.glob(os.path.join(B, "wf_*"))
                 if os.path.exists(os.path.join(p, "journal.jsonl"))]
        runs = [max(cands)[1]] if cands else []
    now = time.time(); total = bad = 0
    for r in runs:
        D = os.path.join(B, r); jp = os.path.join(D, "journal.jsonl")
        if not os.path.exists(jp):
            print(f"{r}: no journal"); continue
        jage = (now - os.path.getmtime(jp)) / 60
        done, started = set(), []
        for line in open(jp, encoding="utf-8", errors="replace"):
            try: x = json.loads(line)
            except Exception: continue
            a = x.get("label") or x.get("agentId")
            if x.get("type") == "started": started.append(a)
            elif x.get("type") == "result": done.add(a)
        rows = []
        for a in [x for x in started if x not in done]:
            f = os.path.join(D, f"agent-{a}.jsonl")
            if not os.path.exists(f): continue
            st = os.stat(f); idle = (now - st.st_mtime) / 60
            if idle > 90: continue                      # corpse from a stopped run
            born = getattr(st, "st_birthtime", st.st_ctime)
            with open(f, "rb") as fh:
                head = fh.read(120_000)
                fh.seek(max(0, st.st_size - 60_000)); tail = fh.read()
            # An agent whose transcript ends in an interrupt is dead, not slow. The runtime
            # retries it under a new id, so the old one lingers "started with no result" and
            # would be reported as a stalled agent forever (std-7 ch04, 2026-08-24).
            if b"[Request interrupted by user]" in tail[-4000:]:
                continue
            m = re.search(rb"agents/(\d\d)_", head)
            stage = m.group(1).decode() if m else "--"
            cm = re.search(rb"chapter (\d+)", head); ch = cm.group(1).decode() if cm else "?"
            sm = re.search(rb"std (\d+)", head); std = sm.group(1).decode() if sm else "?"
            n429 = len(re.findall(rb"429|rate.?limit", tail, re.I))
            rows.append((std, ch, stage, (now-born)/60, idle, BARS.get(stage,10), n429, st.st_size/1e6))
        # The journal only moves when an agent COMPLETES, so it goes stale whenever every
        # remaining agent is inside a long generation. Only call the run stalled if NOTHING
        # has written recently either — otherwise it cries wolf on a healthy endgame.
        # every live agent past ITS OWN bar — a flat threshold fires on healthy A12/A10
        all_past = bool(rows) and all(r[4] >= r[5] for r in rows)
        stalled = "   *** SHARD STALLED ***" if (rows and jage >= 20 and all_past) else ""
        print(f"\n{r}   journal idle {jage:.1f}m{stalled}")
        for std, ch, stage, el, idle, bar, n429, mb in sorted(rows, key=lambda x: -x[4]):
            total += 1
            ok = idle < bar
            if not ok: bad += 1
            med = MEDIAN.get(stage)
            if not ok:
                note = "*** PAST ITS BAR — investigate ***"
            elif med and el < med * 0.75:
                note = f"working ({el/med*100:.0f}% of typical {med:.0f}m)"
            elif med and el < med * 1.5:
                note = f"due soon ({el/med*100:.0f}% of typical {med:.0f}m)"
            else:
                note = f"long but OK ({el/med*100:.0f}% of typical {med:.0f}m)" if med else "healthy"
            print(f"  std{std} ch{ch:<3} A{stage} {NAMES.get(stage,'setup'):<13}"
                  f"ran {el:6.1f}m  quiet {idle:5.1f}m/{bar:3.0f}m  {mb:5.1f}MB  {note}"
                  + (f"  429={n429}" if n429 else ""))
        if not rows:
            print("  (no live agents)")
    print(f"\n{total-bad}/{total} agents healthy" + ("" if bad == 0 else f"  —  {bad} past bar, investigate"))

if __name__ == "__main__":
    main()
