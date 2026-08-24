#!/bin/bash
# Fast-reacting wedge / starvation detector.
# Splits "idle" by WHAT the agent is waiting on, so thresholds can be low without false kills:
#   last event = tool_use     -> a TOOL is executing. Should be seconds. 4m = hung.
#   last event = tool_result  -> the MODEL is generating. Legitimately slow (A1/A12
#                               end in one huge generation), so needs a higher bar
#                               AND corroboration that no output landed anywhere.
S=/Users/aditya/Downloads/Gujarati-lp/scratch
OUT=/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6
LOG=$OUT/wedge-monitor.log
TOOL_MIN=${1:-4}      # tool executing this long = hung
GEN_MIN=${2:-8}       # model generating this long AND no output = wedged
STARVE=${3:-5}        # 429s in the last 5 minutes
POLL=${4:-30}
MAXH=${5:-12}
RUNID=${6:-}
END=$(( $(date +%s) + MAXH*3600 ))
echo "=== monitor start $(date '+%F %T') tool>=${TOOL_MIN}m gen>=${GEN_MIN}m starve>=${STARVE}/5m poll=${POLL}s ===" >> "$LOG"
while [ "$(date +%s)" -lt "$END" ]; do
  R=$(python3 - "$TOOL_MIN" "$GEN_MIN" "$STARVE" "$RUNID" <<'PY'
import json,os,sys,time,glob,re
TOOL=float(sys.argv[1]); GEN=float(sys.argv[2]); STARVE=int(sys.argv[3])

def _workflows_root():
    """Locate the current session's workflow directory.

    The session id changes on every restart and on an account switch, so it must
    never be hardcoded. Prefer $GLP_SESSION; otherwise take the session directory
    whose workflows folder was touched most recently.
    """
    base = "/Users/aditya/.claude/projects/-Users-aditya-Downloads-Gujarati-lp"
    env = os.environ.get("GLP_SESSION")
    if env:
        return os.path.join(base, env, "subagents", "workflows")
    cands = glob.glob(os.path.join(base, "*", "subagents", "workflows"))
    return max(cands, key=os.path.getmtime) if cands else ""
RUNID=sys.argv[4] if len(sys.argv)>4 else ""
SES=_workflows_root()
OUT="/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6"
now=time.time()
live=0; n429=0; runs=0; hung=[]; genstuck=[]; run_start=now
pattern = RUNID if RUNID else "wf_*"
for wf in glob.glob(os.path.join(SES,pattern)):
    # A stopped run keeps its agent transcripts on disk; those are corpses, never
    # incidents. Scoping to one run id is the only reliable way to exclude them.
    jp=os.path.join(wf,"journal.jsonl")
    if not os.path.exists(jp) or now-os.path.getmtime(jp)>30*60: continue
    runs+=1
    done=set(); started=[]
    for line in open(jp,encoding="utf-8",errors="replace"):
        try: r=json.loads(line)
        except: continue
        a=r.get("label") or r.get("agentId")
        if r.get("type")=="started": started.append(a)
        elif r.get("type")=="result": done.add(a)
    for a in [x for x in started if x not in done]:
        f=os.path.join(wf,f"agent-{a}.jsonl")
        if not os.path.exists(f): continue
        live+=1
        st=os.stat(f)
        run_start=min(run_start, getattr(st,"st_birthtime",st.st_ctime))
        idle=(now-st.st_mtime)/60
        with open(f,'rb') as fh:
            fh.seek(max(0,os.path.getsize(f)-300_000)); blob=fh.read()
        if now-os.path.getmtime(f)<300:
            n429+=len(re.findall(rb"429|rate.?limit",blob,re.I))
        # classify what the agent is waiting on
        # Which pipeline stage is this? The heavy generators (A1 transcription,
        # A5 verbatim, A10 solutions, A12 authoring at xhigh) legitimately run
        # 20-40 min and end in ONE huge write. A flat bar kills them mid-output.
        stage=""
        # blob is the TAIL of the transcript; the spec path lives in the PROMPT at
        # the head, so read the head separately or stage detection silently fails.
        try:
            with open(f,'rb') as hf: head=hf.read(120_000)
            m=re.search(rb"agents/(\d\d)_",head) or re.search(rb"agents/(\d\d)_",blob)
            if m: stage=m.group(1).decode()
        except OSError:
            pass
        gen_bar = 30.0 if stage in ("01","05","10","12") else GEN
        kind=None
        for line in blob.decode("utf-8","replace").split("\n"):
            line=line.strip()
            if not line: continue
            try: r=json.loads(line)
            except: continue
            c=(r.get("message") or {}).get("content")
            if isinstance(c,list):
                for b in c:
                    if isinstance(b,dict):
                        if b.get("type")=="tool_use": kind="tool"
                        elif b.get("type")=="tool_result": kind="gen"
                        elif b.get("type")=="text": kind="gen"
        if kind=="tool" and idle>=TOOL: hung.append(f"{a[:9]}:{idle:.0f}m")
        elif kind=="gen" and idle>=gen_bar: genstuck.append(f"{a[:9]}/A{stage}:{idle:.0f}m")
newest=0.0
for f in glob.glob(os.path.join(OUT,"ch*","*")):
    try: newest=max(newest,os.path.getmtime(f))
    except OSError: pass
quiet=(now-newest)/60 if newest else 999
# a run cannot be "quiet" for longer than it has been alive — otherwise the gap
# before launch is charged against it and every fresh run looks instantly wedged
quiet=min(quiet,(now-run_start)/60)
verdict="OK"; detail=""
if runs==0 and live==0: verdict="NO_RUN"
elif hung: verdict="TOOL_HUNG"; detail=",".join(hung)
elif genstuck and quiet>=GEN: verdict="WEDGED"; detail=",".join(genstuck)  # per-agent bar already applied
# Rate limiting only matters if it is actually stopping progress. Retries that
# still land output are noise, not an incident — firing on them costs in-flight work.
elif n429>=STARVE and quiet>=5: verdict="STARVED"; detail=f"{n429} in 5m, no output {quiet:.0f}m"
print(f"{verdict}|live={live}|quiet={quiet:.1f}m|429={n429}|{detail}")
PY
)
  echo "$(date '+%F %T') | $R" >> "$LOG"
  V="${R%%|*}"
  case "$V" in
    OK) ;;
    *) echo "$(date '+%F %T') | TRIGGER $V" >> "$LOG"; echo "$V $R"; exit 0 ;;
  esac
  sleep "$POLL"
done
echo "=== monitor timed out $(date '+%F %T') ===" >> "$LOG"
