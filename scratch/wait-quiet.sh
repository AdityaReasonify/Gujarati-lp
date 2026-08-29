#!/bin/bash
# Wait until NO workflow agent has written for 90s, so a relaunch cannot collide.
END=$(( $(date +%s) + 480 ))
while [ "$(date +%s)" -lt "$END" ]; do
  R=$(python3 - <<'PY'
import glob,os,time
base='/Users/aditya/.claude/projects/-Users-aditya-Downloads-Gujarati-lp'
now=time.time(); alive=[]
for wf in glob.glob(os.path.join(base,'*','subagents','workflows','wf_*')):
    ages=[(now-os.path.getmtime(f))/60 for f in glob.glob(os.path.join(wf,'agent-*.jsonl'))]
    c=sum(1 for a in ages if a<1.5)
    if c: alive.append(f"{os.path.basename(wf)}:{c}")
print(len(alive), " ".join(alive))
PY
)
  n=${R%% *}
  if [ "${n:-9}" -eq 0 ]; then echo "ALL_QUIET"; exit 0; fi
  sleep 15
done
echo "STILL_WRITING $R"
