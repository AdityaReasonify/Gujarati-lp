#!/bin/bash
# Wait for ch12's A10 output (the expensive stage) before we restart its stalled shard.
F=/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch12/10_exercise_solutions.json
END=$(( $(date +%s) + ${1:-720} ))
while [ "$(date +%s)" -lt "$END" ]; do
  if [ -f "$F" ]; then echo "LANDED $(wc -c < $F | tr -d ' ') bytes"; exit 0; fi
  sleep 20
done
echo "TIMEOUT ch12 A10 never landed"
