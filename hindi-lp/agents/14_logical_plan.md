---
name: 14_logical_plan
description: Arrange the merged plan in reading order, renumber ids consecutively, translate every reference, and emit the final logical plan.
tools: [Read, Bash]
inputs:
  - output/<chapter>/13_merged.json
  - reference/naming_conventions.md
  - reference/phase2_contract.md
  - reference/json_contract.md
outputs:
  - output/<chapter>/learning_plan_logical.json
---

You produce the deliverable. Two jobs: **arrange**, then **renumber without breaking anything.**

## 1. Arrange

Order by the chapter's reading sequence — the scene order from the merged structure. For most
Hindi chapters this is the text's own order.

## 2. Renumber consecutively

Walk the arranged tree and renumber `M{m}`, `M{m}.S{s}`, `M{m}.S{s}.T{t}`, `M{m}.S{s}.T{t}.C{c}`
along the traversal, with **no gaps**. Segment and topic counters run across the whole chapter and
never restart; concept counters restart within their topic.

## 3. Translate every reference — the part that breaks

Renumbering is only safe if **every** id that points at a node moves with it. Build the old→new
map first, then rewrite:

- `objectives[].home_topic_id` and `objectives[].anchor[]`
- `learning_objectives[]` inline copies on every topic
- `topic.objective_ids`
- `recall_questions[].id` and `.legacy_id` (`RQ{n}` / `TR{n}`)
- segment `recall_questions[].id` (`SR{n}`)
- `media[].id`, `.concept_id`, `.home_concept_id`
- `concepts[].concept_id` and `concepts[].objective_id`
- `depends_on`, `source_topic_ids`
- `covered_by_topics` in the exercise deliverable

Then **assert**: no id anywhere resolves to a node that no longer exists. A stale anchor is a hard
fail, and it is the single most likely bug in this agent.

Objective ids (`O{n}`) and `strand_to_objective_map` are **not** renumbered — they are a flat
registry, independent of the tree.

## 4. Apply the whitelist

Emit only the keys in `reference/phase2_contract.md`, plus the काव्य extras (`figures_of_speech`,
`rhyme_scheme`, `difficult_words`, `overall_rhyme_scheme`). Every working field from an
intermediate agent is dropped.

## 5. Root fields

Set `ordering: "logical"`, `phase: 2`, `plan_id`, `chapter_id`, `version`, and the DB fields
(`chapter_master_id`, `subject_ref_id`, `medium_id`, `publication_id`, `_activate: false`).
`english_plan_id` and `english_chapter_id` stay `null` — a Hindi chapter has no English twin.

## Output

`learning_plan_logical.json` — the deliverable, ready for the LP2 validator.
