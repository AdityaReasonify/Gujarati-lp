#!/bin/bash
# Wait until the named artifacts land (or timeout), then exit so the orchestrator wakes.
G=/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6
TIMEOUT=${1:-900}
END=$(( $(date +%s) + TIMEOUT ))
TARGETS="$G/ch11/10_exercise_solutions.json $G/ch12/10_exercise_solutions.json $G/ch13/00_chapter_normalized.md"
while [ "$(date +%s)" -lt "$END" ]; do
  missing=""
  for t in $TARGETS; do [ -f "$t" ] || missing="$missing $(basename $(dirname $t))/$(basename $t)"; done
  if [ -z "$missing" ]; then echo "ALL_LANDED"; exit 0; fi
  sleep 20
done
echo "TIMEOUT still missing:$missing"
