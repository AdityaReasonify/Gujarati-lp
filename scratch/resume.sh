#!/bin/bash
# Print everything needed to resume the gujarati-lp pipeline after a restart
# or an account switch. Reads ONLY from disk — no session state required.
S=/Users/aditya/Downloads/Gujarati-lp/scratch
G=/Users/aditya/Downloads/Gujarati-lp/gujarati-lp
echo "=================================================================="
echo " gujarati-lp — RESUME SNAPSHOT   $(date '+%F %T %Z')"
echo "=================================================================="
TOTD=0; TOTC=0
for s in 6 7 8 9 10; do
  [ -d "$G/output$s" ] || continue
  python3 "$S/progress.py" "$s" >/dev/null 2>&1
  python3 - "$s" <<'PY'
import json,sys,os
s=sys.argv[1]
p=f"/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output{s}/progress.json"
if not os.path.exists(p):
    print(f"  std-{s}: not started"); raise SystemExit
d=json.load(open(p)); chs=d["chapters"]
N=d.get("stage_count",14)
done=[c["ch"] for c in chs if len(c["done"])==N]
part=[(c["ch"],len(c["done"])) for c in chs if 0<len(c["done"])<N]
print(f"  std-{s}: {len(done)}/{len(chs)} complete  done={done}")
if part: print(f"           partial={part}")
PY
done
echo
echo "------------------------------------------------------------------"
echo " SCOPE: std-6, 7, 8 ONLY — std-9 and std-10 are OUT OF SCOPE (user directive"
echo "        2026-08-29). Status for 9/10 is shown above for information only."
echo " TO RESUME A STANDARD (run these two steps):"
echo "------------------------------------------------------------------"
echo "  1. python3 $S/args_for.py <STD> 6      # prints args, skips finished chapters"
echo "  2. Ask Claude: launch chapter-runner-optimized.js with those args"
echo "     script: $S/chapter-runner-optimized.js"
echo
echo "  Run ONE workflow at a time. Sharding into parallel workflows triggers"
echo "  429 storms (measured: 62 -> 0 when consolidated back to one)."
echo
echo "------------------------------------------------------------------"
echo " MONITORING"
echo "------------------------------------------------------------------"
echo "  python3 $S/health.py            # per-agent verdict, newest run"
echo "  python3 $S/progress.py <STD>    # stage matrix + PROGRESS.md + progress.json"
echo "  $S/supervisor.sh \"<STDS>\" 25 60 12 2 3 \"<run_ids>\"   # background watchdog"
echo
echo "------------------------------------------------------------------"
echo " READ FIRST: $S/RESUME.md   (state, open decisions, hard-won lessons)"
echo "=================================================================="
