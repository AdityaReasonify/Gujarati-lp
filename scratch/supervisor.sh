#!/bin/bash
# Overnight supervisor across standards. Polls every POLL sec and logs EVERY agent
# individually: standard, chapter, stage, idle, what it is waiting on.
#
# Trigger rules — 2 minutes is applied where a 2-minute pause is genuinely abnormal:
#   DEAD_WORKFLOW : a run has chapters left but ZERO live agents, or its journal has
#                   not moved in DEAD_MIN. This is the failure that costs hours.
#   TOOL_HUNG     : an agent has been waiting on a TOOL for >TOOL_MIN (default 2m).
#                   Tools return in seconds; 2 minutes means hung. (Bash gets 6m —
#                   pdftoppm rasterising a whole chapter legitimately takes minutes.)
#   NO_PROGRESS   : a standard has written no artifact for STALL_MIN while agents run.
# Model generation is NOT trigger-worthy on a short clock: A10 ~36m and A5 ~22m
# medians end in one huge write, so they get stage-aware bars instead.
S=/Users/aditya/Downloads/Gujarati-lp/scratch
G=/Users/aditya/Downloads/Gujarati-lp/gujarati-lp
LOG=$G/supervisor.log
DETAIL=$G/supervisor-agents.log
STDS="${1:-6 7 8}"
STALL_MIN=${2:-25}
POLL=${3:-60}
MAXH=${4:-12}
TOOL_MIN=${5:-2}
DEAD_MIN=${6:-3}
RUNS="${7:-}"   # space-separated run ids; empty = every recent run
ACT="${8:-act}" # "act" = recover automatically; anything else = alert only
CONFIRM=0       # an alert must hold for 2 consecutive polls before we spend tokens on it
CLAUDE=/Users/aditya/.local/bin/claude
ALLOW='Bash,Workflow,Read,Glob,Grep,Write,Edit,TodoWrite'
ROOT=/Users/aditya/Downloads/Gujarati-lp
END=$(( $(date +%s) + MAXH*3600 ))
echo "=== supervisor start $(date '+%F %T') stds=[$STDS] poll=${POLL}s tool_hung>${TOOL_MIN}m dead>${DEAD_MIN}m no_progress>${STALL_MIN}m ===" >> "$LOG"
while [ "$(date +%s)" -lt "$END" ]; do
  R=$(python3 - "$STDS" "$STALL_MIN" "$TOOL_MIN" "$DEAD_MIN" "$DETAIL" "$RUNS" <<'PY'
import json,os,sys,time,glob,re,subprocess
STDS=[int(x) for x in sys.argv[1].split()]

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
STALL=float(sys.argv[2]); TOOLM=float(sys.argv[3]); DEADM=float(sys.argv[4]); DETAIL=sys.argv[5]
RUNS=[r for r in (sys.argv[6].split() if len(sys.argv)>6 else []) if r]
S="/Users/aditya/Downloads/Gujarati-lp/scratch"
SES=_workflows_root()
# Generation bars derived from MEASURED maxima across every completed agent, with
# ~25% headroom. Guessed bars produce false kills; these come from real durations:
# A10 max 47.5m, A12 max 60.6m, A7 max 32m, A5 max 25.5m, A9 max 24.1m.
# Bars = 1.5x the longest SILENT GAP ever observed inside a SUCCESSFULLY COMPLETED agent
# of that stage, measured across 611 finished agents (2026-08-24). This is stricter and
# better-grounded than duration-based bars: A12 drops 130m->58m, A10 85m->52m, A13
# 30m->10m, A11 15m->5m. A healthy agent has never exceeded these; anything past one is
# doing something no successful run of that stage has done.
HEAVY={'01': 25, '02': 20, '04': 12, '05': 18, '07': 32, '08': 8, '09': 12, '10': 52, '11': 5, '12': 58, '13': 10, '14': 5, '15': 5, '16': 18}
NAMES={"01":"ingestion","02":"structure","04":"convergence","05":"verbatim","07":"pitfalls","08":"sensitivity",
       "09":"media","10":"solutions","11":"pagination","12":"authoring","13":"QC","14":"logical","15":"textbook","16":"publication"}
now=time.time(); ts=time.strftime("%F %T")
lines=[]; alerts=[]; alldone=True; tot_done=0; tot_ch=0; n429=0; detail=[]

# ---- per-standard chapter progress ----
prog={}
for std in STDS:
    subprocess.run(["python3",f"{S}/progress.py",str(std)],capture_output=True)
    try: d=json.load(open(f"/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output{std}/progress.json"))
    except Exception: continue
    chs=d["chapters"]; N=d.get("stage_count",14)
    done=[c for c in chs if len(c["done"])==N]
    tot_done+=len(done); tot_ch+=len(chs)
    newest=0.0
    for f in glob.glob(f"/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output{std}/ch*/*"):
        try: newest=max(newest,os.path.getmtime(f))
        except OSError: pass
    started=newest>0; quiet=(now-newest)/60 if started else 0.0
    prog[std]={"done":len(done),"tot":len(chs),"quiet":quiet,"started":started,"live":0}
    if len(done)<len(chs): alldone=False

# ---- per-workflow, per-agent detail ----
# Scope to the runs we actually launched. A stopped run leaves its agent transcripts
# on disk looking idle for hours; counting those manufactures alerts for dead work.
targets=[os.path.join(SES,r) for r in RUNS] if RUNS else sorted(glob.glob(os.path.join(SES,"wf_*")))
for wf in targets:
    jp=os.path.join(wf,"journal.jsonl")
    if not os.path.exists(jp): continue
    jage=(now-os.path.getmtime(jp))/60
    # A journal only advances when an agent COMPLETES, so a run with one long A12 has a
    # stale journal while being perfectly alive. Skipping on jage alone dropped a LIVE run
    # on 2026-08-26 (journal 62m stale, agent writing 11m ago), reported live=0, and fired
    # NO_PROGRESS against a healthy agent at 141% of typical. Keep the run if EITHER the
    # journal or any agent transcript is recent.
    if jage>60:
        _fresh=False
        for _af in glob.glob(os.path.join(wf,"agent-*.jsonl")):
            try:
                if (now-os.path.getmtime(_af))/60 <= 60: _fresh=True; break
            except OSError: pass
        if not _fresh: continue               # genuinely long-finished run
    done=set(); started=[]
    for line in open(jp,encoding="utf-8",errors="replace"):
        try: r=json.loads(line)
        except: continue
        a=r.get("label") or r.get("agentId")
        if r.get("type")=="started": started.append(a)
        elif r.get("type")=="result": done.add(a)
    live=[a for a in started if a not in done]
    wfstd=None; nlive=0; min_agent_idle=1e9; n_past_bar=0
    for a in live:
        f=os.path.join(wf,f"agent-{a}.jsonl")
        if not os.path.exists(f): continue
        try:
            st=os.stat(f); idle=(now-st.st_mtime)/60
        except OSError:
            continue   # agent file rotated or removed mid-tick
        if idle>90: continue                  # corpse from a stopped run
        nlive+=1
        min_agent_idle=min(min_agent_idle,idle)
        try:
            with open(f,'rb') as fh:
                head=fh.read(120_000); fh.seek(max(0,st.st_size-200_000)); tail=fh.read()
        except OSError:
            continue
        # An agent whose transcript ends in an interrupt is dead, not slow. The runtime
        # retries it under a new id, so the old one lingers "started with no result" and
        # would be reported as a stalled agent forever (std-7 ch04, 2026-08-24).
        if b"[Request interrupted by user]" in tail[-4000:]:
            continue
        m=re.search(rb"agents/(\d\d)_",head); stage=m.group(1).decode() if m else "--"
        cm=re.search(rb"chapter (\d+)",head); ch=cm.group(1).decode() if cm else "?"
        sm=re.search(rb"std (\d+)",head)
        if sm:
            try: wfstd=int(sm.group(1))
            except ValueError: pass
        if now-st.st_mtime<300: n429+=len(re.findall(rb"429|rate.?limit",tail,re.I))
        kind="gen"; tool=None
        for line in tail.decode("utf-8","replace").split("\n"):
            line=line.strip()
            if not line: continue
            try: r=json.loads(line)
            except: continue
            c=(r.get("message") or {}).get("content")
            if isinstance(c,list):
                for b in c:
                    if isinstance(b,dict):
                        if b.get("type")=="tool_use": kind="tool"; tool=str(b.get("name"))
                        elif b.get("type") in ("tool_result","text"): kind="gen"; tool=None
        bar = (TOOLM if tool!="Bash" else 6.0) if kind=="tool" else HEAVY.get(stage,10)
        label=f"std{wfstd or '?'} ch{ch} A{stage} {NAMES.get(stage,'setup')}"
        detail.append(f"{ts} | {label:34} idle {idle:5.1f}m bar {bar:4.0f}m {'tool:'+tool if tool else 'generating'}")
        if idle>=bar: n_past_bar+=1
        if kind=="tool" and idle>=bar:
            alerts.append(f"TOOL_HUNG {label} on {tool} {idle:.1f}m")
        elif kind=="gen" and idle>=bar:
            alerts.append(f"GEN_OVERRUN {label} {idle:.1f}m>{bar:.0f}m")
    if wfstd in prog: prog[wfstd]["live"]+=nlive
    # a run whose journal has gone quiet AND has no live agents is dead
    if nlive==0 and jage>=DEADM and wfstd in prog and prog[wfstd]["done"]<prog[wfstd]["tot"]:
        alerts.append(f"DEAD_WORKFLOW {os.path.basename(wf)} std{wfstd} journal quiet {jage:.1f}m, 0 live agents")
    # PER-WORKFLOW stall. The journal advances every time ANY agent of this run finishes,
    # so a run with live agents whose journal has not moved in 20 min is stalled — even
    # while a sibling shard is happily writing. A global quiet clock hides exactly this:
    # on 2026-08-23 shards 1 and 2 sat at 29m journal-idle while shard 3 reset the clock
    # every minute, and three wedged A12 agents went unreported for half an hour.
    # ...but the journal only advances when an agent COMPLETES. At the end of a batch
    # every remaining agent can sit in a long A12/A10 generation at once, so the journal
    # legitimately freezes for an hour while agents write steadily. Require that NO agent
    # has written recently before calling it stalled. (2026-08-23: fired on three healthy
    # A12s, one of which had written 6 seconds earlier.)
    # A flat "quietest agent" threshold contradicts the per-stage bars: 83% of SUCCESSFUL
    # A12 runs are silent >10m, so a flat 10m guard fires on healthy endgames. Require that
    # EVERY live agent has exceeded its own stage's bar — the level no successful agent of
    # that stage has ever reached.
    if nlive>0 and jage>=20 and n_past_bar==nlive:
        alerts.append(f"SHARD_STALLED {os.path.basename(wf)} journal idle {jage:.1f}m, all {nlive} agent(s) past their stage bars")

for std in STDS:
    p=prog.get(std)
    if not p: continue
    lines.append(f"std{std}:{p['done']}/{p['tot']} live={p['live']} "+(f"q{p['quiet']:.0f}m" if p['started'] else "starting"))
    if p['done']<p['tot'] and p['started'] and p['quiet']>=STALL and p['live']==0:
        alerts.append(f"NO_PROGRESS std{std} no artifact {p['quiet']:.0f}m, 0 live agents")

if detail:
    with open(DETAIL,"a") as fh: fh.write("\n".join(detail)+"\n")
v="ALL_DONE" if alldone else ("ALERT" if alerts else "OK")
print(f"{v}|{tot_done}/{tot_ch} chapters|429={n429}|"+" ".join(lines)+("|"+" ; ".join(alerts[:4]) if alerts else ""))
PY
)
  echo "$(date '+%F %T') | $R" >> "$LOG"
  V="${R%%|*}"
  # An EMPTY verdict means the probe itself failed — a file vanishing mid-read while agents
  # write is enough to abort it. That is not an incident; treating it as one killed the
  # supervisor at 16:41 on 2026-08-24 while the pipeline was perfectly healthy.
  if [ -z "$R" ] || [ -z "$V" ]; then
    echo "$(date '+%F %T') | (probe returned nothing — transient, continuing)" >> "$LOG"
    sleep "$POLL"; continue
  fi
  if [ "$V" != "OK" ]; then
    # Require the SAME alert twice in a row. A single tick can catch a file mid-rotation or
    # an agent a second before it writes; acting on one sample wastes a recovery session.
    CONFIRM=$((CONFIRM+1))
    if [ "$CONFIRM" -lt 2 ]; then
      echo "$(date '+%F %T') | $V seen once — confirming next poll before acting" >> "$LOG"
      sleep "$POLL"; continue
    fi
    echo "$(date '+%F %T') | TRIGGER $V (confirmed x$CONFIRM)" >> "$LOG"
    # Only recover when the WHOLE run is stuck. Stopping a workflow kills every sibling
    # agent, so acting on ONE overrunning agent destroys healthy work — on 2026-08-25 a
    # single A05 at 19.6m vs an 18m bar would have thrown away a sibling A05 holding
    # 11.5MB, another at 4.9MB, plus an A12 and an A10 mid-run. A lone GEN_OVERRUN now
    # alerts and keeps watching; only SHARD_STALLED, DEAD_WORKFLOW or TOOL_HUNG recover.
    case "$R" in
      *SHARD_STALLED*|*DEAD_WORKFLOW*|*TOOL_HUNG*|*NO_PROGRESS*) RECOVERABLE=yes ;;
      *) RECOVERABLE=no ;;
    esac
    if [ "$RECOVERABLE" = "no" ]; then
      echo "$(date '+%F %T') | $V is a single-agent overrun — alerting only, siblings are healthy" >> "$LOG"
      CONFIRM=0; sleep "$POLL"; continue
    fi
    if [ "$ACT" = "act" ]; then
      # Bars are 1.5x the longest silence any SUCCESSFUL agent of that stage has shown, so
      # crossing one means doing something no healthy run has ever done. Recover immediately
      # rather than waiting: a wedged agent blocks its whole chapter, because wave 3 awaits
      # every branch. One small session per incident — rare by construction.
      echo "$(date '+%F %T') | ACTING: spawning recovery session" >> "$LOG"
      "$CLAUDE" --bg "A gujarati-lp workflow has a wedged agent. Detector: $R. Do these steps IN ORDER and stop if any fails. STEP 1: TaskList to find every running local_workflow task. STEP 2: TaskStop EVERY one of them. STEP 3: VERIFY nothing is still running — re-run TaskList and also check that no agent transcript under ~/.claude/projects/*/subagents/workflows/wf_*/ has been modified in the last 2 minutes. If ANY workflow is still alive, STOP HERE, append 'recovery aborted: old run still alive' to $LOG, and do nothing else. Launching a second workflow over a live one makes two sets of agents write the same chapter files. STEP 4 (only if step 3 is clean): run python3 scratch/args_for.py $STDS 3 and relaunch scratch/chapter-runner-optimized.js with exactly those args via the Workflow tool. Do not hand-write args. Do not read RESUME.md. Keep output under 20 lines." \
        --permission-mode acceptEdits --allowedTools "$ALLOW" >> "$LOG" 2>&1
      echo "$(date '+%F %T') | recovery session dispatched — supervisor exiting" >> "$LOG"
    fi
    echo "$V $R"; exit 0
  fi
  CONFIRM=0
  sleep "$POLL"
done
echo "=== supervisor timed out $(date '+%F %T') ===" >> "$LOG"
