#!/bin/bash
# Auto-resume the gujarati-lp pipeline when quota refills.
#
# Runs on a schedule (launchd, every 20 min). Each tick it decides whether to act:
#   1. Is there unfinished work?            (reads chapter output files, never a journal)
#   2. Is a workflow already running?       (any run journal touched in the last 25 min)
#   3. Has quota actually refilled?         (one tiny Opus probe — the pipeline needs Opus,
#                                            and limits are per-model, so probing Haiku lies)
# Only if work remains AND nothing is running AND the probe succeeds does it launch a
# background Claude session that reads RESUME.md and continues. A lock file prevents two
# ticks racing. Standards are finished in order: 6, then 7, 8, 9, 10.

# --loop makes this self-scheduling. It must be started from a normal user session:
# macOS privacy protection blocks launchd-spawned processes from reading ~/Downloads
# ("Operation not permitted"), so a LaunchAgent cannot drive this script from here.
if [ "$1" = "--loop" ]; then
  INTERVAL=${2:-1200}
  while true; do "$0"; sleep "$INTERVAL"; done
fi

ROOT=/Users/aditya/Downloads/Gujarati-lp
S=$ROOT/scratch
LOG=$ROOT/gujarati-lp/auto-resume.log
LOCK=$S/.auto-resume.lock
MARK=$S/.auto-resume.launched
CLAUDE=/Users/aditya/.local/bin/claude

# acceptEdits alone is NOT enough: it permits edits but still prompts for Bash, and a
# --bg session has nobody to answer the prompt. Confirmed 2026-08-23 — the first
# autonomous resume launched correctly then sat forever on "This command requires
# approval" for ./scratch/resume.sh. Scope an allowlist to exactly what it needs.
# --allowedTools is VARIADIC: space-separated values keep consuming argv, so passing the
# prompt as a following positional made it get eaten as another tool name and the session
# started with NO prompt ("idle — send a prompt to start"). Confirmed twice, 2026-08-24
# 09:14 and 09:34. Pass the allowlist as ONE comma-separated argument.
# A spawned session explores with whatever shell command it needs — find, grep, ls, sed.
# A narrow per-command allowlist means every unlisted one raises a prompt nobody can answer,
# and the session parks in state=blocked looking like a successful launch. Observed
# 2026-08-24: several sessions accumulated as "waiting". Allow Bash broadly so the
# automation can actually run, but deliberately NOT --dangerously-skip-permissions: writes
# still go through acceptEdits, and the prompt keeps the session on a narrow task.
ALLOW='Bash,Workflow,Read,Glob,Grep,Write,Edit,TodoWrite'
say(){ echo "$(date '+%F %T') | $*" >> "$LOG"; }

# --- single instance -------------------------------------------------------
if ! mkdir "$LOCK" 2>/dev/null; then say "another tick holds the lock — skipping"; exit 0; fi
trap 'rmdir "$LOCK" 2>/dev/null' EXIT

# --- 1. is there work left? ------------------------------------------------
NEXT=""
for std in 6 7 8 9 10; do
  [ -d "$ROOT/gujarati-lp/output$std" ] || { NEXT=$std; break; }
  n=$(python3 "$S/args_for.py" "$std" 6 2>/dev/null | python3 -c "import json,sys;print(len(json.load(sys.stdin)['chapters']))" 2>/dev/null || echo 0)
  if [ "${n:-0}" -gt 0 ]; then NEXT=$std; break; fi
done
if [ -z "$NEXT" ]; then say "ALL STANDARDS COMPLETE — nothing to resume"; exit 0; fi

# --- 2. is a workflow already running? -------------------------------------
ACTIVE=$(python3 - <<'PY'
import glob,os,time
base="/Users/aditya/.claude/projects/-Users-aditya-Downloads-Gujarati-lp"
now=time.time(); n=0
for wf in glob.glob(os.path.join(base,"*","subagents","workflows","wf_*")):
    jp=os.path.join(wf,"journal.jsonl")
    if not os.path.exists(jp): continue
    # The journal only advances when an agent COMPLETES. With every agent inside a long
    # A12/A10 generation it can sit stale for an hour while the run is perfectly alive.
    # Judging on the journal alone made this check report 0 active while an agent had
    # written 30 seconds earlier — one tick from launching a DUPLICATE workflow over a
    # live one, with two agents writing the same chapter files. (2026-08-24)
    fresh = now-os.path.getmtime(jp) < 25*60
    if not fresh:
        for f in glob.glob(os.path.join(wf,"agent-*.jsonl")):
            try:
                if now-os.path.getmtime(f) < 15*60: fresh=True; break
            except OSError: pass
    if fresh: n+=1
print(n)
PY
)
if [ "${ACTIVE:-0}" -gt 0 ]; then
  rm -f "$MARK"                      # a workflow is running: the last launch worked
  # A workflow can be "active" and still be going nowhere: every live agent past its
  # measured bar with no artifact landing. Until now that fell in a blind spot — this
  # loop only ever handled "no workflow running". Conditions are deliberately strict,
  # because killing a healthy long generation is how work got destroyed before.
  WEDGED=$(python3 - "$NEXT" <<'PY'
import glob,os,time,json,re,sys
std=sys.argv[1]
BARS={"01":25,"02":20,"04":12,"05":18,"07":32,"08":8,"09":12,"10":52,"11":5,"12":58,"13":10,"14":5,"15":5,"16":18}  # gap-based, matches health.py/supervisor.sh
base="/Users/aditya/.claude/projects/-Users-aditya-Downloads-Gujarati-lp"
out=f"/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output{std}"
now=time.time()
newest=0.0
for f in glob.glob(os.path.join(out,"ch*","*")):
    try: newest=max(newest,os.path.getmtime(f))
    except OSError: pass
quiet=(now-newest)/60 if newest else 0
live=0; past=0
for wf in glob.glob(os.path.join(base,"*","subagents","workflows","wf_*")):
    jp=os.path.join(wf,"journal.jsonl")
    if not os.path.exists(jp) or now-os.path.getmtime(jp)>3*3600: continue
    done=set(); started=[]
    for line in open(jp,encoding="utf-8",errors="replace"):
        try: x=json.loads(line)
        except: continue
        a=x.get("label") or x.get("agentId")
        if x.get("type")=="started": started.append(a)
        elif x.get("type")=="result": done.add(a)
    for a in [x for x in started if x not in done]:
        f=os.path.join(wf,f"agent-{a}.jsonl")
        if not os.path.exists(f): continue
        try: st=os.stat(f)
        except OSError: continue
        idle=(now-st.st_mtime)/60
        if idle>180: continue
        try:
            with open(f,'rb') as fh:
                head=fh.read(120_000); fh.seek(max(0,st.st_size-4000)); tail=fh.read()
        except OSError: continue
        if b"[Request interrupted" in tail: continue
        live+=1
        m=re.search(rb"agents/(\d\d)_",head)
        if idle >= BARS.get(m.group(1).decode() if m else "--",10): past+=1
# wedged only if EVERY live agent is past its bar AND nothing has landed for 20 min
print("WEDGED" if (live>0 and past==live and quiet>=20) else "OK")
PY
)
  if [ "$WEDGED" = "WEDGED" ]; then
    say "WEDGED: std-$NEXT workflow active but every agent past its bar and no output for 20m — asking a session to stop and relaunch it"
    "$CLAUDE" --bg "The running gujarati-lp workflow is WEDGED: every live agent is past its measured stage bar and no artifact has landed in 20 minutes. Use TaskList to find the running local_workflow task, stop it with TaskStop, then run python3 scratch/args_for.py $NEXT 3 and relaunch scratch/chapter-runner-optimized.js with those args via the Workflow tool. Read $ROOT/RESUME.md first. Do not hand-write args." \
      --permission-mode acceptEdits --allowedTools "$ALLOW" >> "$LOG" 2>&1
    date +%s > "$MARK"
    exit 0
  fi
  say "std-$NEXT pending but $ACTIVE workflow(s) still active — no action"; exit 0
fi

# A previous tick launched a session but no workflow ever appeared. That is the failure
# mode seen 2026-08-23 22:17: the session started, then sat on a permission prompt with
# nobody to answer it. Surface it and let this tick launch again rather than waiting mute.
if [ -f "$MARK" ]; then
  age=$(( $(date +%s) - $(cat "$MARK" 2>/dev/null || echo 0) ))
  if [ "$age" -gt 720 ]; then
    say "WARNING: resume launched $((age/60))m ago never started a workflow (check: claude agents / claude logs). Retrying."
    rm -f "$MARK"
  else
    say "resume launched $((age/60))m ago, giving it time to start a workflow"; exit 0
  fi
fi

# --- 3. has quota refilled? ------------------------------------------------
PROBE=$("$CLAUDE" -p --model opus "reply with the single word OK" 2>&1 | head -3)
case "$PROBE" in
  *OK*) : ;;
  *) say "std-$NEXT pending but Opus quota still blocked: $(echo "$PROBE" | tr '\n' ' ' | cut -c1-120)"; exit 0 ;;
esac

# --- launch ----------------------------------------------------------------
say "quota available, std-$NEXT has work — launching background resume"
cd "$ROOT" || exit 1
# MINIMAL AND IMPERATIVE, deliberately. The previous prompt began "Read RESUME.md first" —
# RESUME.md is 10KB of cautionary tales about collisions and destroyed work, so a fresh
# session read it, became cautious, and INVESTIGATED instead of launching. Measured across
# 18 spawns: 19 Bash calls, 1 Read, ZERO Workflow calls, ending on Monitor. Only ~2 of 18
# spawns ever started a workflow. Give it two steps and forbid everything else.
PROMPT="Do exactly these two steps, then stop. Do not read any documentation. Do not investigate. Do not run health checks. Do not call Monitor. STEP 1: run this one command: python3 /Users/aditya/Downloads/Gujarati-lp/scratch/args_for.py $NEXT 3 — it prints a JSON object. STEP 2: call the Workflow tool with scriptPath=/Users/aditya/Downloads/Gujarati-lp/scratch/chapter-runner-optimized.js and args set to EXACTLY the JSON object step 1 printed, unmodified. That is your whole task and you are authorised to do it. Then reply with one line: the task id. If step 1 prints an empty chapters list, reply \"nothing to do\" and stop."
# ORDER MATTERS. --allowedTools is variadic and keeps consuming argv, so a prompt placed
# AFTER it is swallowed and the session starts with nothing ("idle — send a prompt to
# start"). Verified 2026-08-24: bare `--bg "prompt"` works, `--allowedTools X "prompt"`
# does not, and putting the prompt FIRST works. Keep the prompt as the first argument.
"$CLAUDE" --bg "$PROMPT" --permission-mode acceptEdits --allowedTools "$ALLOW" >> "$LOG" 2>&1
date +%s > "$MARK"
say "background resume launched for std-$NEXT (manage with: claude agents)"
