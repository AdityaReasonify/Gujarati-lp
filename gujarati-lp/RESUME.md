# RESUME — where std-6 stands and how to continue

**Blocked until:** weekly usage limit resets **Aug 29, 5:30am IST**. No agent work is possible before then.
State below is derived from files on disk (the authority), not from workflow journals.

## Std-6 status (15 chapters)

| Chapters | State |
|---|---|
| ch01, ch02, ch03, ch04, ch05, ch06, ch07, ch08, ch09, ch10 | **COMPLETE** — all four deliverables, LP2 validator returned zero `validation_errors` |
| ch11 | partial — has 01,02,04,05,07,08,09,10,11,12,16; needs 13, 14, 15, Phase 8 |
| ch12 | partial — has 01,02,04,05,07,08,09,10,11,12; needs 16, 13, 14, 15, Phase 8 |
| ch13, ch14 | partial — have 01,02,04,05,07,08,09,10,11; need 12, 16, 13, 14, 15, Phase 8 |
| ch15 | partial — has 01,02,04,05,07,08,11; needs 09, 10, 12, 16, 13, 14, 15, Phase 8 |

Std-7 to std-10: not started. Corpus inventories for all five standards ARE complete.

## To resume (after Aug 29)

Recompute the done-map from disk (never trust the journal), then run:

```
python3 - <<'PY'
import os, json
G='/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6'
M={'01_meta.json':'01','02_structure.json':'02','04_converged.json':'04','05_with_content.json':'05',
   '07_pitfalls.json':'07','08_sensitivity.json':'08','09_media.json':'09','10_exercise_solutions.json':'10',
   '11_pages.json':'11','12_authoring.json':'12','16_publication.json':'16','13_merged.json':'13',
   'learning_plan_logical.json':'14','learning_plan_textbook.json':'15'}
done={}
for ch in range(1,16):
    d=os.path.join(G,'ch%02d'%ch)
    if os.path.isdir(d):
        c=sorted({M[f] for f in os.listdir(d) if f in M})
        if c: done[str(ch)]=c
print(json.dumps(done))
PY
```

Then launch the runner (script: `scratchpad/chapter-runner.js`, or copy it into the pack):
`Workflow({scriptPath: <chapter-runner.js>, args: {std: 6, chapters: [11,12,13,14,15], concurrency: 3, done: <map above>}})`

Agents whose output already exists are skipped, so nothing is redone.

## Known issues to fix before any upload

1. **`publication_id` = 1 in every std-6 plan.** That is the CBSE/Hindi publication row, carried over as a
   default; it is NOT verified for GSEB. The server only checks non-null, so validation passing is not proof
   of correctness. **VERIFY-2 must resolve the real GSEB publication row and every plan must be updated.**
   Also observed: A14 left it null on ch02 while setting 1 elsewhere — the agent spec should state one rule.
2. **`chapter_master_id` is null in all plans.** Required for upload; must be fetched from the education DB.
3. **`chapter_id` medium segment (`gseb_eng_...`) is provisional** — VERIFY-1. A wrong medium uploads cleanly
   and mis-files the plan.

Validation-only runs are unaffected by 1-3. Upload is blocked until they are resolved.

## Cost note

~9 chapters consumed ~15M subagent tokens (~1.7M/chapter). Std-7 to std-10 (72 chapters) would be on the
order of 120M tokens. Levers if that is too much: single tier only, trim the mandatory per-agent reading
list, or process selected chapters rather than whole standards.
