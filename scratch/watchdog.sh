#!/bin/bash
# Periodic disk-derived progress tracker for gujarati-lp.
# Snapshots every INTERVAL sec; exits when all chapters complete or MAXHOURS elapse.
STD=${1:-6}
INTERVAL=${2:-180}
MAXHOURS=${3:-12}
S=/Users/aditya/Downloads/Gujarati-lp/scratch
OUT=/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output${STD}
LOG=$OUT/watchdog.log
mkdir -p "$OUT"
END=$(( $(date +%s) + MAXHOURS*3600 ))
echo "=== watchdog start $(date '+%F %T') std=$STD interval=${INTERVAL}s max=${MAXHOURS}h ===" >> "$LOG"
while [ "$(date +%s)" -lt "$END" ]; do
  LINE=$(python3 "$S/progress.py" "$STD" 2>&1 | head -1)
  DONE=$(python3 -c "
import json
d=json.load(open('$OUT/progress.json'))
tot=sum(len(c['done']) for c in d['chapters'])
full=sum(1 for c in d['chapters'] if len(c['done'])==14)
print(f'{tot}/210 stages, {full}/15 chapters complete')
" 2>/dev/null)
  echo "$(date '+%F %T') | $LINE | $DONE" >> "$LOG"
  # stop early once every chapter is finished
  if [ "$(python3 -c "
import json
d=json.load(open('$OUT/progress.json'))
print(sum(1 for c in d['chapters'] if len(c['done'])==14))
" 2>/dev/null)" = "15" ]; then
    echo "$(date '+%F %T') | ALL 15 CHAPTERS COMPLETE — watchdog exiting" >> "$LOG"
    break
  fi
  sleep "$INTERVAL"
done
echo "=== watchdog end $(date '+%F %T') ===" >> "$LOG"
