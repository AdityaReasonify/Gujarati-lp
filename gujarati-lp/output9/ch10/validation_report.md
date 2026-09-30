# Validation Report — std 9, ch 10 એ લોકો

સ્વરૂપ: અછાંદસ (confidence: high)   explanation unit: એક વિચાર-એકમ
Topics: 5   Objectives: 5   Images: 0/3   Exercises: 11/11 (4/4 blocks)

Deliverables: two — the plan (`13_merged.json`) and the exercise pack
(`10_exercise_solutions.json`). Both present. This is a RE-QC final pass: every check below was
re-run mechanically (script-driven scans over the actual JSON, not eyeballing prose) against the
current `13_merged.json` and its ten declared inputs, none of which changed since the prior pass —
`12_authoring.json` (11:41) → `13_merged.json` (11:42) is the newest input/output pair on disk, so
this run re-verifies the same content rather than a new upstream fix.

## A–D (blocking)   PASS

**A — diagnosis and lens. PASS.** `genre_confidence: high`, four `genre_signals` (structure,
theme, exercises, purpose) recorded in `01_meta.json` off the rendered page, quoting the
કવિ-પરિચય's own line ("પ્રબલગતિ મુખ્યત્વે ગદ્યકાવ્યોનો સંગ્રહ છે") as evidence, not verdict.
`explanation_unit: એક વિચાર-એકમ` matches the roster row for અછાંદસ. Marker count verified by
grep on `00_chapter_normalized.md`: `[[કવિ-પરિચય]]` + `[[કૃતિ-પરિચય]]` + three
`[[વિચાર-એકમ: …]]` = 5 markers, and the merged plan carries exactly 5 topics, one marker each.
Zero `[[સ્વાધ્યાય: …]]` block became a topic (the three `સ્વાધ્યાય:`-prefixed markers plus the
bare `[[વિદ્યાર્થી-પ્રવૃત્તિ]]` marker together account for the 4 inventoried exercise blocks,
none of them a topic). `M2.S2.T3` holds three concepts (`C3`–`C5`) for one વિચાર-એકમ
(કાપડ→ધાન્ય→ઔષધ) — checked against the id-continuity scan below and against
`07_pitfalls.json`'s own instruction that this frame is one escalating accusation, never three
separate examples. Apparatus (શબ્દ-સમજૂતી, ભાષા-અભિવ્યક્તિ, શિક્ષકની ભૂમિકા) stayed apparatus;
કવિ-પરિચય/કૃતિ-પરિચય are the two CONCEPT topics, licensed for std 9. No revision-checkpoint/
વ્યાકરણ carve-out applies. `guiding_question` is chapter-specific (quotes this poem's own hanging
line) and is answerable by `M2.S2.T4` → `M2.S3.T5` in traversal order.

**B — verbatim and structure. PASS.** Independently re-derived, not just re-read:
- Codepoint scan of all five `original_chunk` fields (with bracketed spans excluded): zero Latin
  characters, zero Devanagari characters, zero `।`/`॥` outside brackets, on every topic.
- `word_count.original` recomputed by whitespace split and compared to the declared value on all
  five topics: **exact match** (51, 134, 58, 18, 14 — recomputation reproduces the report's own
  numbers).
- Marker-to-topic accounting (above) balances at 5=5, and a targeted string search confirms no
  `સ્વાધ્યાય`-named node exists among `topic_name` values.
- `M2.S3.T5.original_chunk` carries the corrected reading `ભારે અસર કરનારી જંતુનાશક દવા`, matching
  `01_meta.json`'s own 400-dpi re-verification note (the ભ/મ correction), and the છાપ line
  `('પ્રબલગતિ'માંથી)` sits inside this **last** topic's chunk, not elsewhere.
- Id-traversal walk of `modules[].segments[].topics[]` reproduces `M1`/`M2`,
  `M1.S1`/`M2.S2`/`M2.S3` (s continuous across the chapter, never restarting per module),
  `T1`–`T5` continuous, and concept ids `C1`–`C7` chapter-continuous with `M2.S2.T3` correctly
  holding `C3`,`C4`,`C5` for its one topic — verified against `MEDIA_ID_RE`-style traversal logic,
  not asserted.

**C — the teaching block. PASS.** Independently recomputed word counts (not re-read from the
prior report) confirm every band:

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 72 | 81 |
| M1.S1.T2 | 85 | 68 |
| M2.S2.T3 | 83 | 78 |
| M2.S2.T4 | 83 | 69 |
| M2.S3.T5 | 73 | 73 |

`objective_text` O1–O5 recomputed: 16, 23, 25, 26, 22 words — all inside 12–30.
Three-tier summaries recomputed and confirmed strictly increasing on all five topics (word
counts: 19<31<62, 16<46<99, 19<49<103, 22<48<112, 24<35<85).

A full codepoint sweep of every authored display field in the merged plan — `topic_name`,
`explanation`, `real_life_example`, all three summaries, `concept_bullets`, `important_points`,
`recall_questions[].prompt/answer`, `concepts[].content[].text`, `figures_of_speech[].note`,
`rhyme_scheme.note`, `difficult_words[].meaning/example`, the ભાષા-બોધ Gujarati values,
`guiding_question`, `teaching_lens`, `chapter_name`, `unit_title`, `objectives[].objective_text`
— with bracketed spans excluded before scanning, found **zero bare Roman characters, zero
Devanagari characters, zero danda anywhere**, confirming the earlier `vs`→`સામે` fix
(`M2.S2.T4.important_points[0]`, `M2.S3.T5.important_points[1]`) is in place and holding, and that
no other instance of the same defect exists anywhere in the plan.

L2 calibration: glossing sits at point-of-first-use (ઔષધ, સંઘરવું, ઊધઈ, વ્યંગ, ભારે opened where
they matter); the L2-bar words (`ભાવવું`, `ઉછરવું`) are glossed even though a first-language reader
might skip them. Craft named only at the std-9 ceiling and only where the page's own
ભાષા-અભિવ્યક્તિ block names it: `રૂપક` on `M2.S2.T4` only, correctly distinguished from ઉપમા;
`M2.S2.T3`/`M2.S3.T5` correctly carry `figures_of_speech: []`.

**D — સ્વરૂપ essence. PASS.** Every hard `avoid_checks` item in `07_pitfalls.json` and every
hard/soft item in `08_sensitivity.json` was checked with a targeted scan of the merged plan's
display text (not the sample prose alone):
- Poet-date digits (1927/1976/24-1/25-6): **zero occurrences** anywhere in the plan.
- ટેક / ધ્રુવપંક્તિ: **zero occurrences** anywhere in the plan — the three-rung frame is never
  mislabelled as a refrain.
- છંદ names (દુહો, સોરઠો, ચોપાઈ, ઝૂલણા, હરિગીત, સવૈયા, મંદાક્રાન્તા, શિખરિણી, અનુષ્ટુપ,
  વસંતતિલકા): **zero occurrences**. `rhyme_scheme.pattern` reads `અછાંદસ` with `rhyming_words: []`
  on every poem topic; `overall_rhyme_scheme` on M2 states the same in prose; M1 (no poem)
  carries `null`.
- `વેપારી` occurrences: every hit was inspected in context. The one qualified use
  (`કાળાબજાર કરનારા વેપારીઓએ`) sits inside `M1.S1.T2.explanation` reporting the book's own
  કૃતિ-પરિચય wording; every other occurrence explicitly states the **poem itself never uses the
  word** (`M1.S1.T2.explanation`, `M1.S1.T2.important_points[2]`) — exactly the correction
  `07_pitfalls.json` calls for. No occurrence generalises `વેપારીઓ` into an unqualified class.
- `આપણે … જોઈએ` exhortation pattern: zero matches. A substring hit on `બોધ` inside
  `સંબોધનનો` (M2.S3.T5, meaning "of address/vocative", unrelated to moralising) was checked by
  hand and is not a real `બોધ`/`શિખામણ`/`ઉપદેશ` occurrence; no genuine instance of those three
  words exists anywhere in the plan.
- `figures_of_speech[M2.S2.T4]`'s one entry (`રૂપક`) was checked character-for-character against
  `M2.S2.T4.original_chunk` and found verbatim; its `note` correctly states why `રૂપક` and not
  ઉપમા/ઉત્પ્રેક્ષા; `M2.S2.T4.explanation` names why the hanging line stands alone (પંક્તિ-ભંગ),
  not only what it means.
- `M2.S3.T5.explanation` and its recall answers explicitly name the closing lines as વ્યંગ
  (કટાક્ષ) and state outright that the poet does not literally want to become જંતુનાશક દવા.
- Sensitivity: no real caste/community/religion/party name appears anywhere in `explanation` or
  `real_life_example` fields (checked against a list of common Gujarat community terms — zero
  hits); every `real_life_example` anchors the accusation in an unnamed act (a shop that will not
  sell before the price climbs, a house hoarding tank water, a classmate hoarding a ball) — never
  a named shop, caste or trade — and four of five end on a direct question to the child.

## E–G (reported)

**E — સ્વાધ્યાય and risk.** `10_exercise_solutions.json`'s own `coverage_report` cross-checked
against `01_meta.json`'s `exercise_inventory`: both list the same 4 groups (MCQ=4,
બે-ત્રણ વાક્યમાં=2, સવિસ્તારા વાક્યમાં=2, વિદ્યાર્થી-પ્રવૃત્તિ=3 → 11 items), `blocks_found` equals
`blocks_answered`, `unanswered`/`unmapped` both empty, and every `covered_by_topics` id resolves to
a real topic in the merged plan. Headings matched exactly, including the page's own misprint
`સવિસ્તારા` (not normalised). Spot-checked two solutions (`EX1`, `EX9`) directly against
`original_chunk`/the chapter's own text: `EX1`'s MCQ answer and explanation match the poem's
closing lines exactly; `EX9` (વિદ્યાર્થી-પ્રવૃત્તિ) is correctly flagged `is_model_answer: true`
with a teacher_note naming it open-ended. All three વિદ્યાર્થી-પ્રવૃત્તિ items are marked as model
answers; the third (a poor-locality visit) frames it with respect, per `08_sensitivity.json`'s
chapter-level guidance on that exact item.

**F — shape and media.** All 12 `json_contract.md` invariants checked programmatically against
`13_merged.json`, not asserted: `phase:2`; `plan_id`/`chapter_id` match `01_meta.json` exactly on
every shared field (14/14 checked); every topic has ≥1 concept with a resolving `objective_id` and
non-empty `content[]`; the objectives registry (5 objectives) is internally consistent — every
`home_topic_id` and every `anchor[]` entry resolves to a real node, `strand_to_objective_map`
covers L1–L5 exactly and agrees with each objective's own `legacy_id`; every topic's
`learning_objectives[]` mirror matches its root `objective_text` **character for character** and
carries `image_examples: []` (checked on all 5 topics, 0 mismatches); recall ids are
`{topic}.RQ{n}` with `legacy_id` `{topic}.TR{n}` on all 15 recall questions, **zero** `.SR{n}`
anywhere in the file; media ids match `MEDIA_ID_RE`, concept-scoped, on all 3 media nodes;
`publication_id` is non-null (see Gaps); summaries strictly increase (recomputed above);
`figures_of_speech`'s one entry quotes verbatim (checked above); root key set is **exactly** the
contract's 32 keys minus `ordering` (Agent 14/15's to set) — zero missing, zero extra; every
topic's key set is **exactly** the contract's 31 topic keys plus the licensed poem/ભાષા-બોધ extras
— zero missing, zero extra, on all 5 topics.

Bands from `field_shape_rules.md`: `key_terms` 3–5 per topic (band 3–6); `concept_bullets`/
`important_points` 4 each (band 3–4); `recall_questions` 3 per topic (band 2–3), Bloom-laddered
remember→understand→analyze/evaluate on every topic; `difficult_words` 8 (M1) / 7 (M2), both
inside 5–10; `estimated_exchanges` small integer strings ("3","4","4","4","4"); `bloom_level`
lowercase in recalls, Capitalised in `objectives[]` — all confirmed by direct inspection.

One correction to the prior pass's report: it stated every analyze/evaluate recall item cites a
quoted line. Re-checked directly — four of five do (`M1.S1.T1.RQ3`, `M2.S2.T3.RQ3`,
`M2.S2.T4.RQ3`, `M2.S3.T5.RQ3`); `M1.S1.T2.RQ3`'s answer paraphrases the કૃતિ-પરિચય's own account
rather than quoting a bracketed phrase — substantively fine (the topic is the intro-paragraph
CONCEPT topic, not a verse), but the prior report's blanket claim overstated it. Not a checklist
requirement, so not a fail; recorded here so the report doesn't repeat the overclaim.

**G — the seven usual mistakes.** None present. The plan teaches ચિત્ર + મૌન + પંક્તિ-ભંગ, not
સાર+બોધ+પ્રશ્નોત્તર; the three-rung frame stays one topic per the profile's own licence; no
તળપદું/archaic form needed correction (chapter is plain modern Gujarati); no અલંકાર named because
the field existed (`M2.S2.T3`/`M2.S3.T5` honestly carry `[]`); every `real_life_example` is single,
Indian (Gujarat-anchored), unnamed-community, inside std-9 reach, and four of five end on a
question to the child; સ્વાધ્યાય was not cut as topics and the exercise deliverable is full.

## Media

`reuse_report`: scenes 3, authored 3, **reused 0**, rejected none — matches the three topics
(`M2.S2.T3`, `M2.S2.T4`, `M2.S3.T5`) whose `available_content_types` carry `"image"`. Every media
node (`M2.S2.T3.C3.IMG1`, `M2.S2.T4.C6.IMG1`, `M2.S3.T5.C7.IMG1`) carries `image_url:""` and a
non-empty, self-contained `generation_prompt`; every `negative_prompt` carries
`"Devanagari script labels"`. `2d_tool` is `null` chapter-wide. `M1.S1.T1`/`M1.S1.T2` correctly
carry no media (CONCEPT topics, `available_content_types: []`).

## Gaps

1. **`publication_id` is a placeholder (`1`) and must not ship as written.** CBSE's `1` is not
   portable to GSEB. VERIFY-2 must resolve the real GSEB publication row before Phase 8.
2. **`chapter_master_id` is `null`** — mandatory for upload, fetched per chapter from the education
   DB (VERIFY-2); never derived.
3. **`textbook` title confidence: the two source agents disagree, and this report does not paper
   over it.** `01_meta.json`'s own `extraction_notes[]` states the std-9 cover was glyph-matched
   against `std-9/00-front-matter.pdf`'s large-type cover line and calls the reading confirmed.
   `11_pages.json` — whose specific job this is — still records `confidence: "medium"` and lists
   "std 9 cover has not been read" in its own `gaps[]`. Per spec, `textbook`/`textbook_url`/
   `textbook_pages` are folded from `11_pages.json` (done, and verified to match exactly), and its
   `confidence` value is carried rather than overridden here — Agent 13 does not adjudicate a
   disagreement between two upstream agents' own confidence calls. Flagging this discrepancy for
   the owner rather than silently picking a side.
4. **`textbook_url` is a local path string** (`../Textbooks-pdf/std-9/ch-10-e-loko.pdf`) — no
   hosted URL exists. `textbook_pages`: `44–46`.
5. **`topic_title` was derived**, set to the printed chapter title `એ લોકો` (`topic_title =
   chapter_name`, this pack's established convention).
6. **`ordering` is deliberately absent** from `13_merged.json` — confirmed: the merged plan carries
   exactly 31 of the contract's 32 root keys, `ordering` being the one withheld for Agent 14/15.
7. **Board/medium segments (`gseb_eng_gujarati9_ch10`) are PROVISIONAL until VERIFY-1** — confirm
   against the live server before the first upload; a wrong medium uploads clean and mis-files
   silently.
8. **`publication_chunk` embeds `original_chunk` as an exact prefix** on all five topics (checked
   with `str.startswith`, not eyeballed), followed by publication-facing prose; no vocative
   (`બાળકો`, `જુઓ —`) or direct classroom question was found in any `publication_text` or
   `publication_chunk` (checked by string search). `concept_publication` blocks in
   `16_publication.json` match `concepts[].content[]` by count and by `(concept_id, content_index)`
   on all 11 paragraph blocks across the chapter — zero mismatches.
9. **No unmapped exercises** — independently recounted against `01_meta.json`'s inventory (11/11,
   all `covered_by_topics` resolving); confirms `10_exercise_solutions.json`'s own report.

## LP2 validator

Phase 8 validation — POST to https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate

```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati9_ch10_v1",
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

**Result: PASS** — validation_errors is empty. Plan is valid and ready for Phase 9.

## Verdict

**Complete — all A–D sections PASS**, re-verified end to end by direct, script-driven inspection
of `13_merged.json` against every named input (`00_chapter_normalized.md` markers, `01_meta.json`
root fields and inventory, `04_validation.json`/`05_with_content.json` structure, `07_pitfalls.json`
and `08_sensitivity.json` hard items, `09_media.json` reuse report, `10_exercise_solutions.json`
coverage, `11_pages.json` pagination, `12_authoring.json` teaching fields, `16_publication.json`
concept-indexed rewrite) rather than re-asserted from the prior report's prose. `13_merged.json` is
unchanged by this pass — every check confirmed the existing merge is correct and no repair was
needed. The one correction made in this pass is to the **report**, not the plan: the prior
overclaim about every analyze/evaluate recall citing a quoted line (Section F, above). This plan
is ready to proceed to Phase 8, subject only to the Gaps above (VERIFY-1, VERIFY-2,
`publication_id`/`chapter_master_id` placeholders, and the textbook-confidence disagreement between
Agents 1 and 11), none of which are new to this run.
