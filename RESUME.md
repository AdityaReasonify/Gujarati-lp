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

1. **Run ONE workflow at a time.** Sharding into parallel workflows looks faster and
   is not. Measured on 2026-08-23: three shards produced **62 recent 429s**, three
   wedged A12 agents and one corrupted merge; consolidating to a single workflow took
   429s to **0** with the same six chapters. The rate limiter — not the CPU-derived
   agent cap of `min(16, cores-2)` — is the binding constraint.

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
