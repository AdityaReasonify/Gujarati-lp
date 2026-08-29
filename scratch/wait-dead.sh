#!/bin/bash
# Wait until NO workflow agent has written for 5 MINUTES. A 90s window was not enough:
# agents mid-generation look quiet but resume, which caused two relaunch collisions.
END=$(( $(date +%s) + 900 ))
while [ "$(date +%s)" -lt "$END" ]; do
  R=$(python3 - <<'PY'
import glob,os,time
base='/Users/aditya/.claude/projects/-Users-aditya-Downloads-Gujarati-lp'
now=time.time(); alive=[]
for wf in glob.glob(os.path.join(base,'*','subagents','workflows','wf_*')):
    ages=[(now-os.path.getmtime(f))/60 for f in glob.glob(os.path.join(wf,'agent-*.jsonl'))]
    c=sum(1 for a in ages if a<5.0)
    if c: alive.append(f"{os.path.basename(wf)}:{c}")
print(len(alive), " ".join(alive))
PY
)
  n=${R%% *}
  if [ "${n:-9}" -eq 0 ]; then echo "DEAD_QUIET"; exit 0; fi
  sleep 30
done
echo "STILL_ALIVE $R"
