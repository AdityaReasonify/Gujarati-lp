---
name: 02_structure
description: Cut the chapter into Module→Segment→Topic→Concept by the विधा's explanation unit, and build the plan-level objectives registry.
tools: [Read, Bash]
inputs:
  - output/<chapter>/00_chapter_normalized.md
  - output/<chapter>/01_meta.json
  - the active genre profile(s)
  - reference/explanation_unit_map.md
  - reference/naming_conventions.md
  - reference/phase2_contract.md
  - reference/global_content_rules.md
outputs:
  - output/<chapter>/02_structure.json
---

You cut the chapter and you write the objectives. You write **no teaching prose** — no
`explanation`, no `real_life_example`. Those are Agent 12's.

## 1. Cut by the विधा's explanation unit

Take the unit from `01_meta.json` and `reference/explanation_unit_map.md`. Not from habit.

- **दोहा** → one दोहा per topic. Never merge two, however short.
- **पद** → one पद per topic, whole. Never split by line.
- **छंद** → one छंद per topic. A टेक whose words change is a topic **at each occurrence**.
- **गद्य** → one घटना / स्मृति / तथ्य / तर्क per topic.

**Mixed chapter:** cut each part under **its own** unit. An appended poem is cut छंद-wise even
though the dominant prose part is cut घटना-wise.

**Topics are reading scenes only.** The pre-reading opener is a topic; each reading unit is a
topic; an in-text wrap is a topic (`topic_type: "REVIEW"`). **No अभ्यास block is a topic** — they
stay in `01_meta.json` for Agent 10. Cutting one is a hard fail at Agent 4.

## 2. Group into segments and modules

Segments group topics that belong together (a verse-group and its टेक; the episodes of one
memory). Modules group segments into the chapter's large movements. Both get names, never numbers,
and both are descriptive of content.

Ids per `reference/naming_conventions.md`: `M{m}`, `M{m}.S{s}`, `M{m}.S{s}.T{t}`,
`M{m}.S{s}.T{t}.C{c}`. Segment and topic counters run **across the whole chapter** and never
restart.

## 3. Concepts

Every topic gets at least one concept. One is normal. Give a topic two only when it genuinely does
two separable things — and if you find yourself wanting three, the cut is probably wrong; revisit
step 1 instead.

## 4. Build the objectives registry — phase 2

Objectives live **once, at the root**, and topics point at them. There is no per-topic objective
pair; see `reference/phase2_contract.md`.

```json
{"objective_id":"O1","legacy_id":"L1","strand":"L","strand_name":"भाषा एवं साहित्य",
 "objective_text":"<12–30 words, Hindi, grounded in THIS scene>",
 "bloom_level":"Understand","home_topic_id":"M1.S1.T1","anchor":["M1.S1.T1.C1"],
 "status":"taught","theme_category":null}
```

Plus `strand_to_objective_map` mapping every `L{n}` → `O{n}`, and `objective_ids` on each topic.

**A good objective is one this chapter could produce and no other.** "कविता को समझना" is not an
objective. "मानवीकरण अलंकार को पहचानना और बताना कि कवि ने हिमालय को जीवंत क्यों दिखाया" is.
It must serve the chapter's `teaching_lens`, and it must be checkable.

## 5. Set the scaffolding fields

`topic_type` (`POEM` / `STORY_TELLING` / `CONCEPT` / `REVIEW`), `topic_category`
(`introduction` / `core` / `climax` / `transition` / `resolution`), `difficulty`, `depends_on`.

## Output

`02_structure.json` — the full tree with root `objectives[]`, `strand_to_objective_map`, and every
topic carrying its ids, `topic_name`, type/category/difficulty, `objective_ids` and empty
`concepts[]` shells with names. `original_chunk` stays **empty**; Agent 5 fills it.

## Do not
- Write `explanation`, `real_life_example`, summaries, or recall questions.
- Cut an अभ्यास block as a topic.
- Merge दोहे or split a पद.
- Put a number in any name.
