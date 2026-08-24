---
name: 14_logical_plan
description: Arrange the merged plan in reading order, renumber ids consecutively, translate every reference, and emit the final logical plan.
tools: [Read, Bash]
inputs:
  - output{N}/<chapter>/13_merged.json
  - output{N}/<chapter>/10_exercise_solutions.json   (for covered_by_topics)
  - reference/naming_conventions.md
  - reference/phase2_contract.md
  - reference/json_contract.md
outputs:
  - output{N}/<chapter>/learning_plan_logical.json
---

You produce the deliverable. Two jobs: **arrange**, then **renumber without breaking anything.**

## 1. Arrange

Order by the chapter's reading sequence — the scene order from the merged structure. For most GSEB
Gujarati chapters this is the text's own order: કડી after કડી, દુહો after દુહો, ઘટના after ઘટના.
The printed order is Agent 15's business, not yours.

## 2. Renumber consecutively

Walk the arranged tree and renumber `M{m}`, `M{m}.S{s}`, `M{m}.S{s}.T{t}`, `M{m}.S{s}.T{t}.C{c}`
along the traversal, with **no gaps**. `m`, `s`, `t` **and `c`** all run across the whole chapter
and never restart: `M1.S2.T3` carries `M1.S2.T3.C3`, not `.C1`. A concept counter that restarts
inside its topic is rejected by the server — see `reference/naming_conventions.md`.

## 3. Translate every reference — the part that breaks

Renumbering is only safe if **every** id that points at a node moves with it. Build the old→new
map first, then rewrite:

- `objectives[].home_topic_id` and `objectives[].anchor[]`
- `learning_objectives[]` inline copies on every topic
- `topic.objective_ids`
- `recall_questions[].id` and `.legacy_id` (`RQ{n}` / `TR{n}`)
- segment `recall_questions[].id` — **`{segment_id}.RQ{n}`, never `.SR{n}`** (that is LP v1; the
  server rejects it)
- `media[].id`, `.concept_id`, `.home_concept_id`
- `concepts[].concept_id` and `concepts[].objective_id`
- `depends_on`, `source_topic_ids`
- `covered_by_topics` in the exercise deliverable — rewrite them in `10_exercise_solutions.json`
  itself, so the copy the orchestrator makes at Phase 7 carries the renumbered ids

Then **assert**: no id anywhere resolves to a node that no longer exists. A stale anchor is a hard
fail, and it is the single most likely bug in this agent.

Objective ids (`O{n}`) and `strand_to_objective_map` are **not** renumbered — they are a flat
registry, independent of the tree. `legacy_id` `L{n}` moves with its objective, not with the tree.

## 4. Apply the whitelist

Emit only the keys in `reference/phase2_contract.md`, plus the કાવ્ય extras (`figures_of_speech`,
`rhyme_scheme`, `difficult_words`, `overall_rhyme_scheme`) and the optional ભાષા-બોધ extras
(`shabdarth`, `samanarthi`, `vilom`, `vyakaran` — romanized key names kept as the server stores
them). Every working field from an intermediate agent is dropped.

## 5. Map `topic_type` at emit

The intermediate files carry the authored enum. The deliverable carries the **closed server enum**
`instructional | summary | assessment` — nothing else validates:

```
POEM, STORY_TELLING, CONCEPT  →  instructional
REVIEW                        →  summary
EXERCISE                      →  assessment      (defensive only — સ્વાધ્યાય is never a topic)
```

The સ્વરૂપ stays in root `genre`; the finer role stays in `topic_category`. Never write `POEM` or
`CONCEPT` into an emitted plan.

## 6. Root fields

All 32 root keys present, `phase: 2` literal. Set `ordering: "logical"`, `plan_id`, `chapter_id`,
`version`, and the DB fields (`chapter_master_id`, `subject_ref_id`, `medium_id`,
`publication_id`, `_activate: false`).

- `chapter_id` = `gseb_eng_gujarati{grade}_ch{N}`, `plan_id` = `{chapter_id}_v{version}` — no
  `_standard_` segment. **The board and medium segments are PROVISIONAL (VERIFY-1)**: the medium
  slot is the medium of instruction, not the subject language, and a wrong value uploads clean and
  mis-files the plan. Take the form from `reference/naming_conventions.md`; do not reason it out.
- `chapter_master_id` and `publication_id` come from `upload_reference/chapter_master_map.json`
  (GSEB rows fetched from the education DB — never invented). `publication_id` must be **non-null**;
  the server rejects null.
- `subject_ref_id` and `medium_id` stay `null` — server-injected.
- The server assigns the real `version` on upload; what you write is the intention.
- `english_plan_id` and `english_chapter_id` stay `null` — a Gujarati chapter has no English twin.
  Never invent one, and never copy an id from another plan into these fields.

## Output

`learning_plan_logical.json` — the deliverable, ready for the LP2 validator — plus the
`covered_by_topics` rewrite inside `10_exercise_solutions.json`.
