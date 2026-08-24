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
for jp in glob.glob(os.path.join(base,"*","subagents","workflows","wf_*","journal.jsonl")):
    if now-os.path.getmtime(jp) < 25*60: n+=1
print(n)
PY
)
if [ "${ACTIVE:-0}" -gt 0 ]; then
  rm -f "$MARK"                      # a workflow is running: the last launch worked
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
# acceptEdits alone is NOT enough: it permits edits but still prompts for Bash, and a
# --bg session has nobody to answer the prompt. Confirmed 2026-08-23 — the first
# autonomous resume launched correctly then sat forever on "This command requires
# approval" for ./scratch/resume.sh. Scope an allowlist to exactly what it needs.
# --allowedTools is VARIADIC: space-separated values keep consuming argv, so passing the
# prompt as a following positional made it get eaten as another tool name and the session
# started with NO prompt ("idle — send a prompt to start"). Confirmed twice, 2026-08-24
# 09:14 and 09:34. Pass the allowlist as ONE comma-separated argument.
ALLOW='Bash(python3 *),Bash(./scratch/*),Bash(cat *),Bash(ls *),Bash(tail *),Bash(date),Workflow,Read,Glob,Grep'
PROMPT="Resume the gujarati-lp pipeline. Read $ROOT/RESUME.md first. Then run exactly: python3 scratch/args_for.py $NEXT 3 — it prints the args, already skipping finished chapters. Launch scratch/chapter-runner-optimized.js with those args using the Workflow tool. Run ONE workflow at a time; parallel workflows cause 429 storms. Finish std-$NEXT before any other standard. Judge stalls with python3 scratch/health.py, never by raw idle time. Do not hand-write args. If a tool needs permission you cannot grant, stop and append the reason to $LOG."
# ORDER MATTERS. --allowedTools is variadic and keeps consuming argv, so a prompt placed
# AFTER it is swallowed and the session starts with nothing ("idle — send a prompt to
# start"). Verified 2026-08-24: bare `--bg "prompt"` works, `--allowedTools X "prompt"`
# does not, and putting the prompt FIRST works. Keep the prompt as the first argument.
"$CLAUDE" --bg "$PROMPT" --permission-mode acceptEdits --allowedTools "$ALLOW" >> "$LOG" 2>&1
date +%s > "$MARK"
say "background resume launched for std-$NEXT (manage with: claude agents)"
