#!/bin/bash
F=/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output8/ch09/00_chapter_normalized.md
END=$(( $(date +%s) + 1500 ))
while [ "$(date +%s)" -lt "$END" ]; do
  [ -f "$F" ] && { echo "LANDED $(wc -c < $F | tr -d ' ') bytes"; exit 0; }
  sleep 20
done
echo "TIMEOUT"
