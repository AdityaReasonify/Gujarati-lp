# Validation Report — ધોરણ 10, એકમ 6 — સામગ્રી તો સમાજની છે ને !

સ્વરૂપ: આત્મકથાખંડ (અનુભવકથા) (`nibandh_atmaparak.md`, confidence: **high**)
explanation unit: એક પ્રસંગ

Topics: 7 (M1.S1 = 2 · M2.S2 = 2 · M2.S3 = 2 · M3.S4 = 1)
Objectives: 7   Images: 0/6   Exercises: 7/7 items across 4/4 blocks

**This is the RE-QC pass.** The prior gate (previous `validation_report.md`) failed A–D on one
narrow, fully-named item: a bare Roman `vs` sitting in `M2.S2.T3.concept_bullets[1]`, routed to
A12 for a targeted fix. Since that report, only `12_authoring.json` changed on disk (confirmed by
a field-by-field diff of every topic against the prior `13_merged.json`: `explanation`,
`real_life_example`, all three summary tiers, `important_points`, every `concepts[].content[]`
block, `figures_of_speech`, `rhyme_scheme` and `estimated_exchanges` are byte-identical on all 7
topics; `concept_bullets` on `M2.S2.T3` is the **only** field that differs anywhere in the file).
`05_with_content.json`, `07_pitfalls.json`, `08_sensitivity.json`, `09_media.json`,
`10_exercise_solutions.json`, `11_pages.json`, `16_publication.json` and `01_meta.json` all
pre-date the prior report and were not touched — none needed re-running, matching that report's own
routing ("Everything upstream of A12 … is sound and does not need re-running"). This agent applied
the one-field fix to `13_merged.json` and re-ran the full QC checklist programmatically against the
merged file — nothing below is repeated on trust from the prior pass.

---

## A–D (blocking)   **PASS**

### A — Diagnosis and lens.   PASS
Unchanged from the prior pass — `01_meta.json` did not change. `genre_signals`/`genre_confidence:
"high"` stand, routing correctly to `nibandh_atmaparak.md`; `explanation_unit` (`એક પ્રસંગ`)
matches the cut; 1 `[[લેખક-પરિચય]]` + 6 `[[ઘટના: …]]` markers map one-to-one to the 7 topics
carrying them; no `[[સ્વાધ્યાય: …]]` block became a topic; apparatus (શબ્દ-સમજૂતી,
વિદ્યાર્થી-પ્રવૃત્તિ, ભાષા-અભિવ્યક્તિ, શિક્ષકની ભૂમિકા) produced zero topics; `guiding_question` is
chapter-specific and the seven topics in order answer it.

### B — Verbatim and structure.   PASS
Re-ran the full script scan against the **current** `13_merged.json` programmatically: every
`topic_name`, `explanation`, `real_life_example`, all three summary tiers, `objective_text`,
`guiding_question`, `teaching_lens`, `chapter_name`, `unit_title`, `topic_title`, every
`concept_bullets`/`important_points`/`key_terms` entry, every `recall_questions[].prompt/answer`,
every concept `paragraph`/`list` block and `publication_text` field — **zero** Devanagari
codepoints, **zero** stray Roman characters outside the bracketed technical-term shape, **zero**
`।` anywhere. This re-scan is the direct re-check of the item that failed last time: `M2.S2.T3.
concept_bullets[1]` now reads `'લાગે છે' સામે 'છે' — લેખકનો પોતાનો વિચાર, પુરવાર થયેલી હકીકત નહીં`
— the bare `vs` is gone, replaced with `સામે`, no bracket needed since nothing here is a technical
term. All 7 `original_chunk`s remain non-empty Gujarati-script with no Roman intrusion (re-checked
directly, not assumed). Ids remain consecutive and chapter-continuous exactly as before — the fix
touched no id, no structural field.

### C — The teaching block.   PASS
Re-verified word counts on the current file (unchanged from the prior pass, since no teaching field
besides the one bullet line changed): `explanation`/`real_life_example` all inside 55–90 words on
all 7 topics; `objective_text` all inside 12–30 words on all 7 objectives (checked
programmatically this pass, band-by-band, not re-quoted from the old table). `concept_bullets`
itself has no word-count band (it is a `કીવર્ડ — gloss` list per `field_shape_rules.md`), so the
fix could not and did not push any band out of range. Glossing, voice and craft-naming ceiling are
unchanged from the prior PASS.

### D — સ્વરૂપ essence.   PASS
The exact item that failed — the bare Roman `vs` — is fixed and confirmed absent by direct search
across the whole merged file (0 occurrences of a bare `vs`/`Vs`/`VS` token anywhere). Every other D
check from the prior pass (કંજૂસ hedged everywhere, no forced બોધ, no national judgment about
Germany/India, the unresolved source-credit line left untouched in `M3.S4.T7.original_chunk`,
`figures_of_speech: []` vacuously correct for prose) re-verified clean against the current file —
none of those fields changed. One check specific to this pass: `M2.S2.T3`'s `detailed_summary` and
`important_points` (unchanged from the prior pass, but re-read against `08_sensitivity.json`'s soft
caution for this exact topic) attribute `આપણે ત્યાં તો… આંજી નાખે` explicitly as `એવો વિચાર પણ
લેખકને આવ્યો` (a thought that occurred to the writer) rather than asserting it as fact — matching
the caution's own instruction to keep the line "as the narrator's momentary (and mildly
self-mocking) first impression" rather than "a stated contrast between 'stingy Germans' and
'showy Indians'." This is a soft (§E) item, not a hard §D one, and it holds.

### Contract — the 12 invariants.   **12/12 hold**
Re-ran every invariant programmatically against the current `13_merged.json`:
1. `phase: 2`; `chapter_id` = `gseb_eng_gujarati10_ch6`; `plan_id` = `gseb_eng_gujarati10_ch6_v1`. ✓
2. **Now passes.** Zero Roman/Devanagari/`।` hits anywhere in the file (the re-scan above) — the
   one item that failed the prior pass is fixed.
3. Every topic has ≥1 concept (9 concepts across 7 topics), each with a resolving `concept_id`
   (`M{m}.S{s}.T{t}.C{c}`, matching its topic), a resolving `objective_id`, and non-empty
   `content[]` — checked programmatically. ✓
4. Registry: 7 unique `objective_id`s; every `home_topic_id` and every `anchor[]` entry resolves to
   a real topic/concept; `strand_to_objective_map` keys equal the 7 `legacy_id`s one-to-one; every
   topic's `objective_ids` resolve. ✓
5. Inline `learning_objectives[].objective_text` matches the root registry character for character
   on all 7 topics — checked programmatically. ✓
6. Id grammar: all 6 media ids match `MEDIA_ID_RE` (concept-scoped); every recall id is
   `{topic_id}.RQ{n}` with `legacy_id` `{topic_id}.TR{n}`; zero `.SR{n}` anywhere — checked
   programmatically. ✓
7. No સ્વાધ્યાય block is a topic; `10_exercise_solutions.json`'s `coverage_report` reads
   `blocks_found` = `blocks_answered` = the 4-item inventory, `unanswered: []`, `unmapped: []`. ✓
8. Three-tier summaries strictly increase (by character count) on all 7 topics — checked
   programmatically; the fix did not touch any summary field. ✓
9. **No digit** — Latin or Gujarati — in any authored display field, re-scanned across every field
   listed under B above (including the fixed bullet line itself: `સામે` introduces no digit). ✓
10. Media: 6 reading scenes, 6 media nodes, `reuse_report` reads `scenes:6 / authored:6 / reused:0
    / rejected:[]`; every node carries `image_url:""` and a non-empty `generation_prompt`;
    `2d_tool: null` chapter-wide. Unchanged from the prior pass. ✓
11. `figures_of_speech` is `[]` on all 7 topics — vacuously true for this prose chapter. ✓
12. Renumbering (Agent 14) has not run yet — nothing to check here yet; ids remain internally
    consistent going in.

### Publication.   PASS
Re-checked programmatically against the current file: all 7 `publication_text` fields non-empty;
every `original_chunk` found as an exact substring of its topic's `publication_chunk` (byte-level
check, all 7); every `paragraph`-type concept content block carries a `publication_text` (9/9
concepts); zero `બાળકો`/`જુઓ —`/`બોલો` hits across all 16 publication-text fields. The fix did not
touch `concepts[].content[]` or any publication field (`concept_bullets` sits outside
`concepts[].content[]`, so it feeds nothing downstream) — confirmed by direct diff, not assumed —
so `agents/16_publication_authoring.md` correctly did not need to re-run, and publication remains
exactly as it passed last time.

---

## E–G (reported)

- **E — સ્વાધ્યાય and risk.** Unchanged and still clean: all 4 inventoried blocks (7 items)
  answered as EX1–EX7, `covered_by_topics` non-empty on every item, none unmapped.
  `08_sensitivity.json`'s three soft items (M1.S1.T2, M2.S2.T3, M3.S4.T7 — all area સમુદાય) remain
  honoured; the M2.S2.T3 one is re-verified above under D since it sits directly beside this pass's
  fix.
- **F — Shape and media.** 12/12 contract invariants now hold (up from 11/12). `chapter_id`/
  `plan_id` shape correct and provisional per VERIFY-1. 6 scenes, 6 media nodes, `2d_tool: null`.
  Every `negative_prompt` carries `Devanagari script labels` (re-checked, unchanged).
- **G — the seven usual mistakes.** All seven checked clean, as before. Mistake (5)'s bare-Roman
  cousin — the one this whole re-pass exists to close — is now fixed and re-verified absent
  file-wide, not just at the one reported location.

## Media

`reuse_report`: **scenes 6 · authored 6 · reused 0 · rejected []**. Unchanged from the prior pass
— `09_media.json` was not re-run and did not need to be.

## Gaps

Unchanged from the prior pass (no source file besides `12_authoring.json` moved, and that file's
only change was the one bullet line):

- `textbook_url` is a local path — no hosted URL exists for this reader.
- `textbook_pages: "29–31"` at confidence **high**. No pagination gap.
- `chapter_master_id: null`, `subject_ref_id: null`, `publication_id: 1` — the pack-wide
  placeholder shared with every other std-10 chapter in this output set until VERIFY-2 resolves
  the real GSEB rows from the education DB.
- `chapter_id`/`plan_id`'s board/medium segments (`gseb`/`eng`) remain provisional until VERIFY-1.
- `medium_id`, `subject_ref_id` null by contract (server-injected); `english_plan_id`/
  `english_chapter_id` null — no English twin for a Gujarati chapter.
- `ordering: null` — left for Agent 14/15.
- `05b_textbook_order.json`'s printed order is identical to the merged plan's logical traversal
  order: `{"human_confirmation_required": true, "reason": "textbook order is identical to logical
  order", "checked": "05b_textbook_order.json matches the logical traversal exactly"}`.
- Module/segment-level three-tier summaries, `important_points` and segment `recall_questions[]`
  are not produced anywhere in this pack — a pack-wide convention matching every already-passed
  sibling chapter (`ch01`–`ch04`), not a chapter-specific gap.
- `10_exercise_solutions.json`'s `exercise_group` annotation (e.g. `(પ્રશ્ન 1, ઉપ-પ્રશ્ન 1)`) is
  Agent 10's own indexing on a separate, non-merged deliverable — not authored display text inside
  `13_merged.json`, so it does not trip the digits check.
- Working fields dropped at merge, as required: `genre_signals`, `genre_confidence`,
  `active_genre_profiles`, `explanation_unit`, `structure_inventory`, `exercise_inventory`,
  `extraction_notes` (from `01_meta.json`); `notes` (from `05_with_content.json`,
  `12_authoring.json`); `avoid_checks`/`misconception`/`correction` (from `07_pitfalls.json`);
  `caution`/`guidance`/`severity`/`none_found` (from `08_sensitivity.json`); `topic_id` on each
  media node; `04_validation.json`'s checklist scaffolding; `09_media.json`'s `reuse_report`.
  `13_merged.json` carries the 32 root contract keys and, on every topic, the 31 topic keys plus
  the ભાષા-બોધ extras (`shabdarth`, `samanarthi`, `vilom`, `vyakaran`) and the (vacuously empty,
  correctly so) poem extras (`figures_of_speech`, `rhyme_scheme`) — nothing else.

## LP2 validator

**PASS** — Validated at Phase 8 against `learning_plan_logical.json` on staging.singularity-learn.com:

```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati10_ch6_v1",
  "validation_errors": [],
  "message": "Valid"
}
```

Zero validation errors returned.

---

## Verdict

**PASS.** The one narrow item from the prior gate — a bare Roman `vs` in
`M2.S2.T3.concept_bullets[1]` — is fixed (now `સામે`) and re-verified absent across the entire
merged file, not just at that one location. All of A–D pass; all 12 contract invariants hold;
publication, media and the exercise deliverable are complete and clean. `13_merged.json` is
written in the full 32-root-key / 7-topic / 9-concept / 6-media-node shape with the fix applied and
nothing else disturbed — no id was renumbered, no `original_chunk` was touched, no band was
widened, no working field survived the merge. This chapter is ready to hand to Agent 14 for
renumbering and enum-mapping.
