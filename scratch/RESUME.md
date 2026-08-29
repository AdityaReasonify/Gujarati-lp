# gujarati-lp — RESUME HANDOFF

Everything needed to continue after a restart, a new session, or an account switch.
**No session state is required.** All progress derives from output files on disk.

Run `./scratch/resume.sh` for a live snapshot before reading further.

---

## 1. Resume in three steps

```bash
python3 scratch/resume.sh                 # where everything stands
python3 scratch/args_for.py 6 6           # args for std-6, skipping finished chapters
```

Then ask Claude: *"launch `scratch/chapter-runner-optimized.js` with these args"*.

`args_for.py` reads the output directory and emits only unfinished work, so re-running
it after any crash is always correct. **Never hand-write the args.**

---

## 2. Ground rules paid for in lost work

1. **Cap TOTAL concurrent agents (~6), not workflow count.** The original rule here said
   "run one workflow at a time" after three shards produced 62 429s on 2026-08-23. That
   conflated *shape* with *volume*. Measured across 2,000+ supervisor samples, 429 rate
   tracks **total live agents**, not how they are distributed:

   | live agents | median 429 | max 429 |
   |---|---|---|
   | 1-3 | 1-2 | 12-20 |
   | 4-6 | 3-4 | 20-48 |
   | 7-9 | 2-4 | **31-89** |
   | 10-13 | 0-8 | 42-45 |

   The median barely moves; the **tail** explodes past ~6 agents. The 08-23 storm was three
   shards running ~18 agents, not sharding as such. Four per-chapter workflows holding 8
   agents total measured 5 recent 429s — comparable to the consolidated run they replaced.

   So: shard freely **if it does not raise total agent count**, and prefer per-chapter
   workflows in the endgame, where they buy real decoupling — a wedged agent stalls only its
   own chapter instead of every chapter sharing a `parallel()`. Do NOT shard a 13-chapter
   standard into 13 workflows; that is a volume increase wearing a shape disguise.

   **Stage weight matters as much as agent count.** On 2026-08-25 four per-chapter shards
   each reached A12 simultaneously and all four died on the session limit having burned
   2.14M subagent tokens with zero chapters completed. Four concurrent A12s is a far heavier
   load than four mixed-stage agents. When every live chapter is queued at the same heavy
   stage (A12 or A10), cap concurrency at 2 regardless of what the agent-count table allows.


**Journal mtime is not liveness — this bit six times.** A workflow's journal only advances
when an agent COMPLETES, so a run with one long A12 looks dead by journal age while being
perfectly healthy. Every monitor must include a run if EITHER its journal or any agent
transcript is recent. Instances: supervisor global-quiet clock, auto-resume ACTIVE check,
progress.py corpse counting, health.py stall display, auto-resume duplicate-launch check,
and finally supervisor's own `jage>60` run-inclusion gate, which on 2026-08-26 dropped a live
run (journal 62m stale, agent writing 11m ago) and fired NO_PROGRESS at a healthy agent
sitting at 141% of typical. **Liveness = an agent transcript belonging to a known-current
run, not ending in an interrupt, measured against its own stage bar. Nothing else.**

2. **Idle time is not a stall signal.** An agent writes its transcript only when a
   message completes, so a healthy agent mid-generation shows idle climbing for tens of
   minutes. Measured maxima: A12 60.6m, A10 47.5m, A7 32m, A5 25.5m, A9 24.1m.
   Use `python3 scratch/health.py`, which compares idle against per-stage bars.

3. **A real stall has one of two signatures:**
   - idle past that stage's bar while the transcript stays small (a wedged A12 sat at
     27m having written 0.4MB, frozen right after reading its inputs), or
   - the run's journal frozen 20+ minutes while agents are still live (`SHARD STALLED`).

4. **Never restart an agent that is mid-write.** Waiting has been right every time it
   was tested; killing destroyed two chapter transcriptions on 2026-08-22. Before
   stopping a run, check whether an expensive stage is about to land — waiting 12
   minutes for ch12's A10 saved 105KB of the pipeline's slowest stage.

5. **State lives on disk, never in a workflow journal.** `resumeFromRunId` is
   same-session-only and was useless when a session died with two workflows live.

---

## 3. The pipeline

14 stages per chapter. Each proves it ran by writing a declared file:

| Stage | Output | Median | Max | Bar |
|---|---|---|---|---|
| A1 ingestion+genre | `00_chapter_normalized.md`, `01_meta.json` | 12.6m | 81.8m | 100m |
| A2 structure | `02_structure.json` | 14.1m | 27.8m | 35m |
| A4 convergence | `04_validation.json`, `04_converged.json` | 6.9m | 22.3m | 30m |
| A11 pagination | `11_pages.json` | 0.7m | 2.5m | 10m |
| A5 verbatim | `05_with_content.json`, `05b_textbook_order.json` | 18.4m | 31.7m | 40m |
| A7 pitfalls | `07_pitfalls.json` | 19.6m | 32.8m | 40m |
| A8 sensitivity | `08_sensitivity.json` | 1.8m | 5.6m | 10m |
| A9 media | `09_media.json` | 9.0m | 24.1m | 30m |
| A10 solutions | `10_exercise_solutions.json` | **36.1m** | **68.9m** | 85m |
| A12 authoring | `12_authoring.json` | **43.9m** | **105.0m** | 130m |
| A16 publication | `16_publication.json` | 12.3m | 38.3m | 50m |
| A13 QC | `13_merged.json`, `validation_report.md` | 11.8m | 24.2m | 30m |
| A14 logical | `learning_plan_logical.json` | 7.0m | 9.8m | 10m |
| ~~A15 textbook~~ | ~~`learning_plan_textbook.json`~~ | — | — | **DISABLED** |

Measured 2026-08-23 across 25-146 completed agents per stage. Bars are 1.25x the observed
maximum. **Do not guess these** — earlier bars built from 1-8 samples were badly wrong
(A16's real median of 12.3m exceeded its assumed 10m bar, so every A16 run alerted).

DAG: `A1 → A2 → A4 → A5 → [A7 ∥ A8] → [A9 ∥ A10 ∥ (A12 → A16)] → A13 → A14 → LP2`.
A11 runs parallel to the A2→A4 chain. **A12 depends on neither A9 nor A10** (verified:
zero references in its spec) — that restructure removed ~16 min from every chapter.

---

### A15 is disabled (2026-08-23, by request)

`learning_plan_textbook.json` is no longer produced for new chapters. Nothing consumed it:
only `agents/15_textbook_plan.md` referenced it, and A13, A14 and the LP2 validator never
read it. `05b_textbook_order.json` still comes from A5, so re-enabling is a one-line change —
uncomment the `A15` call in `chapter-runner-optimized.js`.

**A completed chapter is therefore 13 stages, not 14.** Nothing hardcodes that: `progress.py`
writes `stage_count` into each `output<N>/progress.json`, and `args_for.py`, `supervisor.sh`
and `resume.sh` all read it. std-6's 15 chapters were finished before this change and still
carry their textbook plans.



**One owner for stall detection.** `progress.py` reports the disk-derived stage matrix and
nothing else — it deliberately emits NO wedge verdict. It sees every run on disk, so any
stall count it produced mixed live agents with corpses from stopped runs (2026-08-25: it
reported 9 wedged agents across 3 dead runs while all 4 live runs were healthy). Stall
detection belongs to `health.py` and `supervisor.sh`, which scope to a known run id and
carry the interrupt filter. Three thresholds for one question is two too many.

### Stall bars come from measured SILENT GAPS, not durations

Bars are `1.5 x` the longest silence ever seen inside a **successfully completed** agent of
that stage, measured across 611 finished agents (2026-08-24):

| stage | median gap | max gap | bar | % of successful runs silent >10m |
|---|---|---|---|---|
| A12 authoring | 25.9m | 38.3m | 58m | **83%** |
| A10 solutions | 20.8m | 34.3m | 52m | **86%** |
| A07 pitfalls | 9.0m | 21.0m | 32m | 35% |
| A16 publication | 5.0m | 11.2m | 18m | 5% |
| A01 ingestion | 4.1m | 15.2m | 25m | 10% |
| A02 structure | 6.1m | 12.5m | 20m | 7% |
| A05 verbatim | 5.1m | 10.6m | 18m | 2% |
| A13 QC | 2.4m | 4.5m | 10m | 0% |
| A09 media | 3.1m | 7.3m | 12m | 0% |
| A11 / A14 / A15 | ~1m | 1.2m | 5m | 0% |

**This is why a long idle on A12 or A10 is meaningless and a 6-minute idle on A11 is an
incident.** 83% of successful A12 runs go quiet for more than ten minutes; no successful
A11 run has ever gone quiet for more than 36 seconds. A single flat threshold cannot express
that, which is why every flat-threshold attempt produced false alarms.




**Never `claude stop` a recovery session while its workflow is running.** A workflow executes
in-process of the session that launched it, so killing the session kills the workflow. Learned
the hard way on 2026-08-25: stopping the recovery session took its healthy new run down with
it. Stop the *workflow* with TaskStop; leave the session alone.

**Recovery must STOP before it RELAUNCHES, and must verify the stop.** On 2026-08-25 the
first live auto-recovery relaunched while the old run was still executing, leaving two
workflows writing the same chapter files for several minutes (caught before any corruption —
182/182 JSON still parsed). The recovery prompt now runs stop → verify-nothing-alive →
relaunch, and aborts rather than launching if any workflow is still writing.


**Recovery must not punish healthy siblings.** Stopping a workflow kills every agent in it,
so a single overrunning agent is NOT grounds to recover — on 2026-08-25 one A05 at 19.6m
against an 18m bar would have destroyed a sibling A05 holding 11.5MB, another at 4.9MB, and
an A12 and A10 mid-run. `ACT` now fires only on whole-run failures (SHARD_STALLED,
DEAD_WORKFLOW, TOOL_HUNG, NO_PROGRESS); a lone GEN_OVERRUN alerts and keeps watching.

### The supervisor ACTS, it does not just alert

`supervisor.sh <stds> 25 45 12 2 3 "<run_ids>" act` recovers automatically:

1. Detects a stall against the per-stage gap bars (or TOOL_HUNG / DEAD_WORKFLOW / NO_PROGRESS)
2. **Requires the same alert on two consecutive polls** — one tick can catch a file
   mid-rotation or an agent a second before it writes, and acting on one sample wastes a
   recovery session
3. Spawns one small `claude --bg` session told to: TaskList → TaskStop the run →
   `args_for.py` → relaunch. It is explicitly instructed **not** to read RESUME.md, not to
   explore, and to keep output under 20 lines — the recovery must be cheap
4. Exits, because the recovery session now owns the run

Pass anything other than `act` as the 8th argument for alert-only behaviour.

**Why act immediately rather than wait:** a wedged agent blocks its entire chapter, since
wave 3 awaits every branch. And the bars are set at 1.5x the longest silence any *successful*
agent of that stage has ever shown, so crossing one means doing something no healthy run has
done. Waiting adds nothing to the diagnosis.


### Model policy (2026-08-29): NO Opus

| Tier | Agents |
|---|---|
| **Sonnet @ `xhigh`** | all authoring (A1, A2, A4, A5, A7, A9, A10, A12, A16, A13, A14) |
| Sonnet @ `medium` | A8 sensitivity, A11 pagination |
| **Haiku** | pure I/O only: Phase-0 setup, LP2 POST, batch-state update |
| **Fable** | judgment / QC / verification passes |

This REVERSES the earlier "authoring runs on Opus" rule. The user changed it while working
through repeated spend limits; cost is the driver. Correctness is not model-dependent here —
A5 enforces verbatim against the renders and A13 runs the A–D gates mechanically — so what
changes is authored prose quality, not the verbatim or no-hallucination guarantees.

## 4. Scripts that matter

`scratch/` also holds hundreds of agent-authored build scripts. Only these are orchestration:

| File | Purpose |
|---|---|
| `chapter-runner-optimized.js` | **the runner** — resume-aware, context-routed, guarded |
| `args_for.py` | emit workflow args for a standard, skipping finished chapters |
| `progress.py` | stage matrix → `output<N>/PROGRESS.md` + `progress.json` |
| `health.py` | per-agent verdict against measured bars |
| `supervisor.sh` | background watchdog; wakes the orchestrator on real stalls |
| `resume.sh` | the snapshot you are reading about |
| `chapter-runner-resume.js` | earlier runner, no context routing — keep as fallback |
| `cultural-grounding.js`, `grounding-opus-pass.js` | pack-wide change sets, already applied |

None hardcode a session id; they auto-detect, or honour `$GLP_SESSION`.

---

## 5. Bugs already fixed — do not reintroduce

- **A12 / A16 silent failure.** A terminal error makes `agent()` return `null`; the runner
  used to march on to QC, producing a merge with an empty authoring or publication layer.
  Both now verify their output file and retry once. Hit std-6 ch06 and ch10.
- **QC owner re-run path.** A13 names owners loosely (`agents/12_authoring.md`), and the
  runner built `${GUJ}/agents/${spec}` → a doubled path to a file that does not exist under
  that name. Owners now resolve on their leading two digits; unresolvable ones are logged.
- **A1-owned validation failure did not re-cut the structure.** `reference/loop_protocol.md`
  says A1's remedy is "re-diagnose, reload profile, THEN A2 again", but the runner re-ran A1
  alone. The validator then re-checked byte-identical `02_structure.json` and failed a second
  time, consuming the one permitted retry and hard-failing the chapter. Proven on std-7 ch04
  and ch06 (2026-08-24) — ch06's structure had the same sha256 across both passes. The A1
  branch now runs A1 **then** A2 before revalidating.
- **Context routing gaps.** A13 needs `qc_checklist.md`, `json_contract.md`,
  `phase2_contract.md`, `field_shape_rules.md`; A5 needs `shabd_gloss.md`. All now routed.
- **Supervisor false positives.** Four distinct classes: flat thresholds, a quiet clock
  measured from a previous run, counting corpses from stopped runs, and a global quiet
  clock that let one healthy shard mask two dead ones.

---

## 6. Open decisions — need a human

1. **`publication_chunk` contradiction.** `agents/13_assembly_validation.md` says it must be
   byte-identical to `original_chunk`; `agents/16_publication_authoring.md` says it is the
   block as a whole with the verbatim staying verbatim inside it. A13 followed 16 and
   verified the verbatim is present byte-identical as a prefix. One spec should be amended.
2. **`agents/07` §2 vs `reference/global_content_rules.md` §5** are jointly unsatisfiable:
   pitfalls demands every concrete noun in an example appear in the chapter text; global
   rules demand a concrete anchor from the child's own life. The pitfall wording needs
   tightening.
3. **VERIFY-1 / VERIFY-2 before ANY upload** — real GSEB `chapter_id` medium segment,
   `publication_id`, `chapter_master_id` must be resolved against the live server.
   Validation-only runs are unaffected. `publication_id: null` is why some chapters show
   `complete-lp2-pending` rather than `complete`.
4. **Anchor bank gap** — `reference/gujarat_cultural_anchors.md` names Sikh among Gujarat's
   communities but carries no Sikh anchor row.
5. **VERIFY-4** — the 55–90 and 12–30 word bands remain provisional pending measurement
   against real GSEB L2 chapters.

---

## 7. Data corrections applied by hand

- **std-8 ch02**: A1 transcribed the deva's name as `ઈંદ્ર` (long ઈ); the print shows
  `ઇંદ્ર` (short ઇ). A5 refused to proceed and supplied glyph crops, a control word
  (`ઇતિહાસ`, same glyph) and the dictionary spelling. Corrected across
  `00_chapter_normalized.md`, `01_meta.json`, `02_structure.json`, `04_validation.json`
  on 2026-08-23, with provenance in the transcription header and a pre-fix backup at
  `00_chapter_normalized.md.pre-indra-fix`. **A5 re-verifies this on re-run**, so a wrong
  correction fails loudly rather than silently.

## 8. Quarantined (invalid, kept for inspection)

- `output6/ch06/_invalid/` — merge built without the authoring layer
- `output6/ch10/_invalid/` — merge built without the publication layer

---

## 9. Caveat on `health.py` in a brand-new session

`health.py` finds the workflow directory by taking the session whose `subagents/workflows`
folder was touched most recently. A **fresh session has no workflows until you launch one**,
so run it before your first launch and it will report the *previous* session's run — whose
agents are corpses, not live work.

Two ways to be sure you are looking at the right run:

```bash
GLP_SESSION=<current-session-id> python3 scratch/health.py   # pin it explicitly
python3 scratch/health.py <run_id>                            # or name the run
```

After you launch a workflow in the new session, the default resolves correctly on its own.
`progress.py` and `args_for.py` are unaffected — they read only chapter output files.

---

## 10. Automatic resume when quota refills

`scratch/auto-resume.sh` restarts the pipeline on its own when quota returns.

```bash
cd /Users/aditya/Downloads/Gujarati-lp
nohup ./scratch/auto-resume.sh --loop 1200 >/dev/null 2>&1 &   # tick every 20 min
tail -f gujarati-lp/auto-resume.log                            # watch its decisions
pkill -f "auto-resume.sh --loop"                               # stop it
```

Each tick acts only if all three hold:

1. unfinished work exists (read from chapter output files, in order std 6 → 10)
2. no workflow journal has been touched in the last 25 minutes
3. a one-token **Opus** probe succeeds — limits are per-model, so probing Haiku
   would report quota the pipeline cannot actually use

Then it starts a background Claude session (`claude --bg --permission-mode acceptEdits`)
pointed at this file. A lock directory stops two ticks racing.

**It must be started from a normal terminal session, and it dies on reboot.** A LaunchAgent
was tried and cannot work: macOS privacy protection blocks launchd-spawned processes from
reading `~/Downloads` — the script failed with `Operation not permitted` before executing a
single line. To survive reboots you would need to either grant Full Disk Access to
`/bin/bash` in System Settings → Privacy & Security, or move the project out of `~/Downloads`.
Until then, re-run the `nohup` line after any restart.


**Launching a background session correctly.** `--allowedTools` is variadic and keeps
consuming argv, so a prompt placed after it is swallowed and the session starts empty —
`backgrounded · <id> (idle — send a prompt to start)`. It looks like a successful launch
and silently does nothing. **Pass the prompt as the FIRST argument:**

```bash
claude --bg "$PROMPT" --permission-mode acceptEdits --allowedTools "$ALLOW"
```

Verified 2026-08-24 by round-tripping a sentinel through a live session.

**Caveat:** the background session runs with `acceptEdits`, so a prompt needing broader
permission stalls it rather than proceeding. Check the log if a resume seems not to happen.
