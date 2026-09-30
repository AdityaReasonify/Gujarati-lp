# Validation Report — std9/ch13 (ઘડવૈયા)

સ્વરૂપ: પ્રસંગકથા (રેખાચિત્ર) (confidence: high)   explanation unit: એક જીવન-પ્રસંગ
Topics: 3   Objectives: 3   Images: 0/1   Exercises: 9/9 items answered (8 inventoried + 1 flagged addition — see Gaps)

## A–D (blocking)   **PASS**

This is the re-QC pass after the owner re-ran the two missing agents named in this file's prior
verdict. `12_authoring.json` (513 lines) and `16_publication.json` (45 lines) now exist alongside
every other input; `13_merged.json` is emitted for the first time this run.

- **A — Diagnosis and lens: PASS** (unchanged from the prior pass). `04_validation.json.checks.genre_fidelity.pass = true`.
  Genre પ્રસંગકથા (રેખાચિત્ર), confidence high, cross-checked against `profiles/genres/charitra_prasang.md`'s
  own named worked example — this exact chapter. Single active profile, no mixed chapter.
  `guiding_question`/`teaching_lens` are chapter-derived, not copied from the profile.
- **B — Verbatim and structure: PASS** (re-verified). Re-diffed all three `original_chunk` values
  in `05_with_content.json` against `00_chapter_normalized.md` programmatically: `M1.S1.T1`
  matches the `[[લેખક-પરિચય]]` block character-for-character, `M1.S1.T2` matches
  `[[કૃતિ-પરિચય]]` character-for-character, and `M2.S2.T3` matches the concatenation of all five
  `[[ઘટના: …]]` blocks (markers stripped) character-for-character — 4,005 characters, zero diffs.
  A script scan of all three chunks found zero Roman characters outside bracketed technical terms,
  zero Devanagari characters, and zero `।`. All 7 reading-scene markers map onto the 3 topics
  (2 parichay 1:1, 5 ઘટના merged into one, per the profile's own instruction for this chapter); no
  `[[સ્વાધ્યાય: …]]` block became a topic; ids consecutive (T1–T3, C1–C3, chapter-continuous).
- **C — The teaching block: PASS.** Every topic now carries non-empty `explanation` and
  `real_life_example`. Word counts (script-verified): M1.S1.T1 78/74 words, M1.S1.T2 83/68 words,
  M2.S2.T3 87/69 words — all inside the 55–90 band; all three `objective_text` values (20/23/28
  words) are inside the 12–30 band. Voice is second-person, spoken શિષ્ટ ગુજરાતી, glosses hard
  words at point of use (`તળપદું`, `આલેખક`, `કુસંસ્કાર`, `ભવાયા`, `ભાનબારો`, `બખડજંતર` and others),
  and craft is named only within the std-9 ceiling (see D below). Each `real_life_example` is one
  concrete Gujarat anchor and closes on a question to the child; the three anchors rotate domain
  (a village elder's storytelling → a younger sibling's bad habit at home → a night-time DJ-garba
  silenced before exams) with no repeat and no adult/abstract example.
- **D — સ્વરૂપ essence: PASS.** All 14 `severity:"hard"` `avoid_checks` in `07_pitfalls.json`
  verified against the authored text: M1.S1.T1/T2 add no book title, place, award or honorific
  beyond what each topic's own `original_chunk` prints, and use only the chunk's own word
  `વિખ્યાત`. M2.S2.T3's `explanation` names the quality (ત્યાગ) only in its final sentence, after
  the concrete act (paying the twelve rupees); every quotation-marked span attributed to
  master/wife/nayak is copied character-for-character from `original_chunk` (`'ગામમાં ભવાયા રમવા
  આવ્યા છે, તેથી મને ચેન નથી'`, `'ખોદ્યો ડુંગર અને કાઢ્યો ઉંદર'`, `'ના, મારા ગામ વતી આજની રાતનો
  ફાળો આપું છું.'`); no interior state is attributed beyond the two licensed phrases (`નિર્ણય
  કરીને આંખ મીંચે છે`, `વાતનો ઘૂંટડો ગળે ઊતરી ગયો`); the writer's era-line dates are never
  attached to કરુણાશંકર માસ્તર anywhere; the salary stays `બાર રૂપિયા` in words throughout, never a
  digit; and neither `explanation` nor `real_life_example` closes on an unquoted "આપણે પણ … જોઈએ"
  ઉપદેશ line. The one soft item (glossing the કહેવત and એક રૂઢિપ્રયોગ at point of use) is honoured
  via `vyakaran`. `figures_of_speech` names exactly one device (વ્યતિરેક, the std-9-canon one of
  the three the book's own ભાષા-અભિવ્યક્તિ box tags) and its `lines` string is byte-verified
  present in `M2.S2.T3.original_chunk`; `M1.S1.T1`/`M1.S1.T2` correctly carry `[]`;
  `rhyme_scheme` is `null` on all three (prose genre). Both `08_sensitivity.json` items (one hard
  on `M2.S2.T3`, one soft on `M1.S1.T2`, both સમુદાય) are honoured: `explanation`/
  `real_life_example` scope the master's worry to his own students, use only the chapter's printed
  craft-words (ભવાયા, નાયક, ડાગલો), never generalise a judgment onto the community, and let the
  નાયકનું પોતાનું ગૌરવભર્યું, સાદું પ્રસ્થાન (`'નાયકો પણ સંસ્કારપૂજક હતા'`) stand as the text's own
  balance, unembellished.
- **Contract / Publication: PASS.** Every topic has `publication_text`; `publication_chunk` is
  byte-identical to `original_chunk` on all three topics (script-verified); `concept_publication`
  supplies one entry per `paragraph`-type content block, in order, matched by `content_index`
  (list-type blocks correctly carry no `publication_text`, per `agents/16_publication_authoring.md`'s
  own "one entry per paragraph block" rule) — M1.S1.T1 and M1.S1.T2 each 1/1 paragraph covered,
  M2.S2.T3 2/2 paragraphs covered. No vocative or classroom instruction survived into any
  `publication_text` (the three occurrences of the word "બાળકો" are the ordinary noun "children"
  inside reported narrative content — `...શબ્દોનું બાળકો અનુકરણ ન કરે...` — never the vocative
  address "બાળકો, જુઓ —"). No meaning is added beyond the teaching block.

### 12-invariant contract check (`reference/json_contract.md`)

Ran a full mechanical check against the merged file: all 31 root keys present and no extras
(the 32nd, `ordering`, is correctly withheld — Agent 14/15's to set); `phase:2`; `chapter_id`/
`plan_id` grammar holds; `publication_id:1` (non-null placeholder, provisional until VERIFY-2, the
same value every other output9/output10 chapter in this pack carries); `english_plan_id`/
`english_chapter_id` both `null`; objective registry internally consistent (3 unique
`objective_id`s, every `home_topic_id`/`anchor[]` resolves, `strand_to_objective_map` covers
L1–L3 one-to-one); `learning_objectives[]` mirrors match the root `objective_text` character for
character on every topic, each carrying `image_examples: []`; concept ids chapter-continuous and
equal to their topic's own number under the one-concept-per-topic rule (C1/C2/C3); recall ids are
all `{topic_id}.RQ{n}` with `legacy_id` `{topic_id}.TR{n}` — no `.SR{n}` anywhere; the one media id
(`M2.S2.T3.C3.IMG1`) matches `MEDIA_ID_RE` and its `concept_id` field agrees with the id's own
segment; three-tier summaries strictly increase in length on every topic; zero digits found in any
authored display field (`topic_name`, `explanation`, `real_life_example`, summaries, bullets,
recall prompts/answers) — script-checked, not just read. Zero contract violations found.

## E–G (reported)

- **E — Exercises: functionally complete**, unchanged from the prior pass. `10_exercise_solutions.json.coverage_report`:
  all 3 blocks inventoried in `01_meta.json` (MCQ ×4, બે-ત્રણ વાક્યમાં ×2, સવિસ્તાર ×2 = 8 items,
  EX1–EX8) are answered in printed order; `unanswered: []`, `unmapped: []`. The file additionally
  answers `વિદ્યાર્થી-પ્રવૃત્તિ` (EX9, marked `is_model_answer: true`) — see Gaps for the standing,
  non-blocking inventory-count note carried forward from the prior pass (still unresolved by
  Agent 1 as of this run).
- **E — Sensitivity: now actioned**, closing the item this file's prior pass left open pending
  Agent 12. Both `08_sensitivity.json` items are honoured in the authored text — see D above.
- **F — Shape: PASS.** Root fields well-formed (`chapter_id: gseb_eng_gujarati9_ch13`,
  `plan_id: gseb_eng_gujarati9_ch13_v1`); `04_validation.json.checks.objectives.pass = true`;
  `09_media.json` (untouched this run, already clean): the one media node carries `image_url:""`
  and a non-empty, self-contained `generation_prompt`; `negative_prompt` names "Devanagari script
  labels"; `2d_tool: null`. `estimated_time: 1.5` and `publication_id: 1` follow the exact
  convention every other merged chapter in `output9`/`output10` uses.
- **G — usual failure modes: none observed.** Genre kept as પ્રસંગકથા throughout, taught through
  situation → act → outcome → named quality rather than flattened into સાર+બોધ; the five ઘટના
  beats correctly stay merged into one topic per the profile's own instruction for this exact
  chapter; no book title/date invented beyond what each topic's own chunk prints; no biographical
  fact invented for કરુણાશંકર માસ્તર; the writer's era-line dates never conflated with the
  character's; no craft named above the std-9 ceiling (સજીવારોપણ and સહજોદ્‌ગાર, both tagged by
  the book's own ભાષા-અભિવ્યક્તિ box, are correctly withheld as off std-9's seven-અલંકાર canon);
  no real-life anchor pitched outside std-9's reach or outside India; સ્વાધ્યાય not cut as a
  teaching topic anywhere.

## Media

`09_media.json.reuse_report` (unchanged, re-verified this pass): `scenes: 1`, `authored: 1`,
`reused: 0`, `rejected: []` — matches the one topic (`M2.S2.T3`) whose `available_content_types`
carries `"image"`; the two `CONCEPT` પરિચય topics correctly carry none. `image_url:""` with a real,
self-contained `generation_prompt` on the one node; the depicted moment (money changing hands at
the troupe's morning camp) is the one sentence the chunk actually prints, with an invented,
non-portrait face for both men per the profile's truth-claim-ladder likeness rule. Structurally
clean; folded into `13_merged.json` without alteration.

## Gaps

- **Exercise-inventory discrepancy (Agent 1, not blocking — carried forward unresolved from the
  prior pass):** `01_meta.json.exercise_inventory` still lists 3 blocks / 8 items and still
  classifies `વિદ્યાર્થી-પ્રવૃત્તિ` as apparatus, not an exercise, while
  `reference/exercise_alignment.md`'s std-9 ladder table and `agents/01_ingestion_genre_diagnosis.md`'s
  own "Not exercises" list both keep `વિદ્યાર્થી-પ્રવૃત્તિ` out of that exclusion — it names only
  `ભાષા-અભિવ્યક્તિ` and `શિક્ષકની ભૂમિકા`. `10_exercise_solutions.json` answers the block anyway
  (EX9, flagged transparently in its own `coverage_report._note`), so no exercise content is
  missing or unanswered — the only open item is that `01_meta.json`'s own count undercounts by
  one block. Recommend Agent 1 add `વિદ્યાર્થી-પ્રવૃત્તિ` to `exercise_inventory` on its next pass;
  not routed as a run-blocking failure, unchanged from the prior verdict.
- `11_pages.json`: `textbook_pages: "69–72"`, confidence **medium** — both end folios were read
  directly off renders and agree with `manifest.json` and the board profile, but the std-9 cover
  page itself has not been separately read/confirmed. `textbook_url` is a local PDF path; no
  hosted URL exists. Fail-soft per spec, not blocking.
  `chapter_master_id`/`subject_ref_id` stay `null` pending VERIFY-2 (server-side lookups);
  `publication_id` carries the pack-wide provisional placeholder `1` pending the same; the
  `chapter_id`/`plan_id` medium segment is provisional pending VERIFY-1. All four are pipeline-wide,
  standing gaps, not specific to this chapter.
- `07_pitfalls.json`/`08_sensitivity.json` (working files) are correctly **not** carried into
  `13_merged.json` — checked and dropped, per this agent's own "do not carry a working field, a
  score or a note into `13_merged.json`" rule.

## LP2 validator

Not run — that is Phase 8's step (`POST /api/lp2/learning-plans/validate`), out of this agent's
scope. `13_merged.json` is emitted this run for the first time; a subsequent Phase-8 pass should
record the validator's `validation_errors[]` here.

## LP2 validator

Result: Valid

```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati9_ch13_v1",
  "version": null,
  "phase": null,
  "is_active": null,
  "is_draft": null,
  "counts": null,
  "diff": null,
  "publication_id": null,
  "publication_name": null,
  "validation_errors": [],
  "message": "Valid"
}
```
