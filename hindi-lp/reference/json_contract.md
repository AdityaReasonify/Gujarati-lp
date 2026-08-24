# JSON Contract — what Agent 13 asserts before anything ships

Shape authority is `reference/phase2_contract.md` and `schema/hindi_learning_plan_skeleton.json`.
These are the invariants Agent 13 checks; each is a **hard fail**.

1. **`phase` is `2`**, `plan_id` is `{chapter_id}_v{version}`, `chapter_id` is
   `cbse_eng_hindi{grade}_ch{unit_number}`.
2. **Every topic has a non-empty Devanagari `original_chunk`** with no Roman characters outside
   bracketed technical terms.
3. **Every topic has ≥1 concept**, each with a valid `concept_id`, an `objective_id` that exists
   in the root registry, and non-empty `content[]`.
4. **Root `objectives[]` is complete and consistent**: every `objective_id` unique; every
   `home_topic_id` and every id in `anchor[]` resolves to a real node; `strand_to_objective_map`
   covers every `legacy_id`; every topic's `objective_ids` resolve.
5. **Inline mirrors match the registry.** `learning_objectives[]` on a topic carries the same
   `objective_text` as the root entry, character for character.
6. **Id grammar holds** — media match `MEDIA_ID_RE` (concept-scoped), topic recalls are `RQ{n}`
   with `legacy_id` `TR{n}`, segment recalls are `SR{n}`.
7. **No अभ्यास block is a topic**, and every block inventoried in `01_meta.json` is answered in
   `exercise_solutions.json`.
8. **Three-tier summaries strictly increase** at topic, segment and module level.
9. **No numbers in display text** — no `छंद 2` / `प्रश्न 4` in any name, explanation, example,
   summary, bullet or prompt.
10. **Media (soft, but reported)** — one image per reading scene; at most one `2d_tool` in the
    whole chapter; a reused `image_url` names its source frame in `teaching_notes`; a scene
    without a match carries `image_url: ""` **and** a non-empty `generation_prompt`.
11. **`figures_of_speech` entries quote words that actually appear** in that topic's
    `original_chunk`. A device whose `lines` are not found in the chunk is a fail, not a warning.
12. **Every reference survives renumbering** — after Agent 14 no `anchor`, `home_topic_id`,
    `objective_ids`, `depends_on`, `source_topic_ids`, media id or recall id points at a node that
    no longer exists.

## Whitelist

Agent 14 emits only the keys named in `phase2_contract.md` (plus the काव्य extras
`figures_of_speech`, `rhyme_scheme`, `difficult_words`, `overall_rhyme_scheme`). Working fields
from intermediate agents — pitfall notes, media match scores, validation flags — are dropped.

## The final gate

`POST /api/lp2/learning-plans/validate` must return **zero** `validation_errors`
(`phase2_contract.md` §Upload). The server is the authority on shape; when it disagrees with this
file, the server is right and this file gets fixed.
