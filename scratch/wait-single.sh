#!/bin/bash
# Wait until at most ONE workflow is genuinely writing, then report.
END=$(( $(date +%s) + 420 ))
while [ "$(date +%s)" -lt "$END" ]; do
  R=$(python3 - <<'PY'
import glob,os,time
base='/Users/aditya/.claude/projects/-Users-aditya-Downloads-Gujarati-lp'
now=time.time(); alive=[]
for wf in glob.glob(os.path.join(base,'*','subagents','workflows','wf_*')):
    ages=[(now-os.path.getmtime(f))/60 for f in glob.glob(os.path.join(wf,'agent-*.jsonl'))]
    if ages and sum(1 for a in ages if a<1.5): alive.append(os.path.basename(wf))
print(len(alive), " ".join(alive))
PY
)
  n=${R%% *}
  if [ "${n:-9}" -le 1 ]; then echo "SETTLED $R"; exit 0; fi
  sleep 20
done
echo "STILL_MULTIPLE $R"
