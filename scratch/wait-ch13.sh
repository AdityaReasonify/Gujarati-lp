#!/bin/bash
# Wait for ch13's two in-flight outputs, then hand ownership back to the main session.
G=/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output7/ch13
END=$(( $(date +%s) + 1800 ))
while [ "$(date +%s)" -lt "$END" ]; do
  if [ -f "$G/12_authoring.json" ] && [ -f "$G/10_exercise_solutions.json" ]; then
    echo "LANDED authoring=$(wc -c < $G/12_authoring.json | tr -d ' ')B solutions=$(wc -c < $G/10_exercise_solutions.json | tr -d ' ')B"; exit 0
  fi
  sleep 30
done
echo "TIMEOUT"
