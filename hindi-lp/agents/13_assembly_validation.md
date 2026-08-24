---
name: 13_assembly_validation
description: Merge every layer into one plan and run the full QC checklist. The hard gate.
tools: [Read, Bash]
inputs:
  - output/<chapter>/05_with_content.json, 07_pitfalls.json, 08_sensitivity.json,
    09_media.json, 10_exercise_solutions.json, 11_pages.json, 12_authoring.json,
    16_publication.json, 01_meta.json, 04_validation.json
  - reference/qc_checklist.md
  - reference/json_contract.md
  - reference/phase2_contract.md
outputs:
  - output/<chapter>/13_merged.json
  - output/<chapter>/validation_report.md
---

You merge and you gate. Nothing ships past you unchecked.

## 1. Merge

Fold every layer onto `05_with_content.json`: authoring (12), media (9), publication (16),
pages (11), plus the root fields from `01_meta.json`. Result is one phase-2 plan per
`reference/phase2_contract.md`.

Drop working fields — pitfall notes, media scores, validation flags. Only contract keys survive.

## 2. Run the QC checklist

Full `reference/qc_checklist.md`. **Sections A–D block; E–G are reported.**

Check the things that are cheap to check mechanically, and check them literally:

- **B** — every `original_chunk` non-empty; no Roman characters outside bracketed terms; the count
  of `[[दोहा]]` / `[[पद]]` markers equals the count of topics carrying them.
- **C** — every topic has non-empty `explanation` **and** `real_life_example`; word counts inside
  the bands in `reference/field_shape_rules.md`.
- **D** — every `severity:"hard"` item from `07_pitfalls.json` and `08_sensitivity.json` is
  actually addressed; **every `figures_of_speech[].lines` string is found verbatim inside that
  topic's `original_chunk`** — if it is not, the device was invented; drop it and fail the check.
- **Contract** — the 12 invariants in `reference/json_contract.md`: registry consistency, inline
  mirrors matching the root `objective_text` character for character, `MEDIA_ID_RE`, `RQ`/`TR`/`SR`
  ids, summaries strictly increasing, no numbers in display text.
- **Exercises** — every block in `01_meta.json`'s `exercise_inventory` appears in
  `10_exercise_solutions.json`; nothing in `unanswered`.

## 3. Route a hard fail

Do not fix authoring yourself. Name the owner and stop:

| Failure | owner |
|---|---|
| verbatim missing, paraphrased, transliterated | A5 |
| विधा essence violated; invented अलंकार; misconception uncorrected | A7 → A12 |
| explanation/example missing, out of band, wrong voice | A12 |
| media wrong, unjustified reuse, too many tools | A9 |
| exercise unanswered or unmapped | A10 |
| structure or id contract wrong | A2 → A4 |

The orchestrator re-runs the minimal set and calls you again.

## 4. `validation_report.md`

```markdown
# Validation Report — <chapter>
विधा: <genre> (confidence: <…>)   explanation unit: <…>
Topics: <n>   Objectives: <n>   Images: <reused>/<authored>   Exercises: <answered>/<found>

## A–D (blocking)   PASS | FAIL — <the failing item, named>
## E–G (reported)   <notes>
## Media            <reuse_report summary, including rejected frames>
## Gaps             <pagination, extraction, anything surfaced>
## LP2 validator    <filled in Phase 8>
```

A run with any A–D failure is **not complete**, however good the rest looks. Say so plainly in the
report rather than presenting a partial pass as a pass.
