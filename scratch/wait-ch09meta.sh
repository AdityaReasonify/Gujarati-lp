#!/bin/bash
F=/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output8/ch09/01_meta.json
END=$(( $(date +%s) + 600 ))
while [ "$(date +%s)" -lt "$END" ]; do
  [ -f "$F" ] && { echo "LANDED $(wc -c < $F | tr -d ' ') bytes — ch09 A1 complete"; exit 0; }
  sleep 20
done
echo "TIMEOUT — sharding anyway, ch09 A1 will re-run"
