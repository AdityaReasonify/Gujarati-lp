# Validation Report — std 8, ch 6 · પીડ પરાઈ જાણે રે !

સ્વરૂપ: ચરિત્રલેખ — profile `charitra_prasang.md` (confidence: high)   explanation unit: એક જીવન-પ્રસંગ

Topics: 8   Objectives: 8   Images: 0/8   Exercises: 14/14 blocks · 61/61 items

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` → `13_merged.json` (31 of the 32 root keys; `ordering` is
Agent 14/15's and was deliberately not written).

**This is a RE-QC pass.** The prior run of this agent failed on one D-section item
(`M4.S4.T8.modified_chunk` naming `ઝૂલણા છંદ` as a craft label). The owner, `agents/05_verbatim_attachment.md`,
re-ran and rewrote `05_with_content.json`'s `M4.S4.T8.modified_chunk` (timestamped after the prior
merge and prior report). Every other input file (`07_pitfalls.json`, `08_sensitivity.json`,
`09_media.json`, `10_exercise_solutions.json`, `11_pages.json`, `12_authoring.json`,
`16_publication.json`) is unchanged since the prior merge — confirmed by a full field-by-field diff
of every topic's `05_with_content.json`-sourced fields (`original_chunk`, `modified_chunk`,
`key_terms`, `word_count`, the three content-type fields) against the previous `13_merged.json`:
the only difference anywhere is the one corrected sentence. `13_merged.json` has been rebuilt from
the corrected base and every section below was re-checked against the corrected plan, not assumed
to still hold.

---

## A–D (blocking)   **PASS**

All four sections now hold. The single prior failure is fixed and re-verified below.

### A — diagnosis and lens.   Holds.

સ્વરૂપ ચરિત્રલેખ, confidence high, diagnosed off the rendered page from the four signals recorded in
`01_meta.json` and cross-agreed by `02_structure.json`/`04_validation.json`. The explanation unit
`એક જીવન-પ્રસંગ` matches the roster row for ચરિત્ર/રેખાચિત્ર/પ્રસંગકથા (one પ્રસંગ or one printed
person-section), and this chapter has no printed person-section head, so only the ઘટના half of the
rule applies — correctly, all eight cut topics are ઘટના, not person-sections. Apparatus stayed
apparatus: the blue પ્રવેશપેટી (teacher-addressed, unlike std-10's student-facing કવિ-પરિચય), the
yellow શબ્દાર્થ box and the closing ચર્ચા-વિચારણા box are outside the topic tree and carry no topic.
No pre-reading CONCEPT topic exists, which is measured (std-8 prints no student-facing પરિચય
paragraph here), not omitted. `guiding_question` is derived from this chapter's own event chain
(જન્મ → સાધના → ખ્યાતિ → હૂંડી → મામેરું-કેદ → સમદર્શિતા → પદ-વારસો) and reading T1→T8 answers it.

### B — verbatim and structure.   Holds.

All 8 `original_chunk` non-empty. Programmatic scan of the full merged plan: **0 Devanagari
codepoints, 0 Roman letters outside brackets, 0 `।` (daṇḍa)** in any `original_chunk`.
`publication_chunk` is byte-identical to `original_chunk` on 8/8 (checked programmatically, re-run
against the rebuilt merge). Marker parity is exact: eight `[[ઘટના: …]]` markers in
`00_chapter_normalized.md` (lines 11, 15, 19, 27, 35, 39, 43, 50) against eight topics, one per
marker, in printed order. **No સ્વાધ્યાય block became a topic** — all fourteen `[[સ્વાધ્યાય: …]]`
markers match `01_meta.json`'s `exercise_inventory` exactly by count and by `verbatim_heading`, with
zero overlap against any topic name or chunk. Poetic licence preserved, not corrected: `નરસૈયો`/
`નરસૈયાના`, `છોડાવિયો`, `તુજ`, `જાદવા` all kept exactly. The printed unmatched closing quote in
M2.S2.T4 (`…વૈષ્ણવજન તો તેને રે કહીએ જે પીડ પરાઈ જાણે રે"માં કરે છે !`) is kept as printed, not
repaired.

### C — the teaching block.   Holds.

All 8 topics carry non-empty `explanation` **and** `real_life_example`. Measured word counts, all
inside `field_shape_rules.md` bands with no band widened (checked programmatically against the
rebuilt merge): `explanation` and `real_life_example` both within 55–90, `objective_text` within
12–30. No numerals — Arabic or Gujarati — in any authored display text (explanations, examples,
three summaries, `concept_bullets`, `important_points`, concept `content[]`, recall prompts/answers,
names, objective texts): checked programmatically, zero hits. Glossing sits at point of use, in
Gujarati, calibrated to L2.

### D — સ્વરૂપ essence.   **PASS — the prior failure is fixed.**

`figures_of_speech` is `[]` and `rhyme_scheme` is `null` on all eight topics (the correct answer for
a ગદ્ય ચરિત્રલેખ). All 18 `severity:"hard"` items in `07_pitfalls.json` and both hard items in
`08_sensitivity.json` were re-checked against the rebuilt merge, one by one: all 18 pitfall items and
both sensitivity items hold, with the ચમત્કાર/લોકકથા material (M1.S1.T1, M1.S1.T2, M3.S3.T5,
M3.S3.T6) consistently hedged with the chapter's own `કહેવાય છે` / `જાણે` / `જાણીતી કથા` framing, no
inner thought or feeling invented at any of the four flagged moments, all quoted spans
character-for-character matched against `original_chunk`, and neither M3.S3.T6's imprisonment nor
M4.S4.T7's ઊંચનીચ material pinned on a named community.

**The prior craft-label failure is now fixed and re-verified.** `05_with_content.json`'s
`M4.S4.T8.modified_chunk` was rewritten by its owner (`agents/05_verbatim_attachment.md`) to drop
`ઝૂલણા છંદ` from the paraphrase — it now reads `નરસિંહ મહેતાએ 'વસંતનાં પદ', 'કૃષ્ણલીલા', 'હૂંડી',
'મોસાળું' જેવાં અનેક ગાઈ શકાય એવાં પદો રચ્યાં…`, describing the padas without naming the metre, exactly
mirroring how the topic's own `explanation` already avoided the term. A programmatic scan of every
authored field in the rebuilt merge (`topic_name`, `explanation`, `real_life_example`, all three
summaries, `modified_chunk`, `concept_bullets`, `important_points`, `key_terms`,
`recall_questions[].prompt`/`.answer`, `concept_name`, concept `content[]`) for `અલંકાર`, `પ્રાસ`,
`સમાસ`, `સાહિત્યપ્રકાર`, `છંદ` returns **zero hits**. `છંદ` survives only twice in the whole plan —
inside `M4.S4.T8.original_chunk` and its byte-identical `publication_chunk` mirror, both licensed
because the book itself prints `ઝૂલણા છંદમાં`. `07_pitfalls.json`'s hard item for M4.S4.T8 ("No
authored field outside `original_chunk` uses 'ઝૂલણા છંદ' or 'છંદ' to teach a metrical or craft
label") is satisfied everywhere in this rebuilt merge, including the field that was the sole
exception before.

A field-by-field diff against the previous (failing) `13_merged.json` confirms this was the **only**
authored-content change anywhere in the plan — no other topic, concept, summary, recall question or
media node moved. Every other check that held in the prior run was re-run in full against the
rebuilt merge, not carried over by assumption, and holds again below.

### Contract — the 12 `json_contract.md` invariants.

All 12 hold, checked programmatically against the rebuilt merge: `phase: 2`; `plan_id` =
`chapter_id` + `_v1`; `chapter_id` = `gseb_eng_gujarati8_ch6`. Objectives registry O1–O8 unique,
every `home_topic_id` and every `anchor[]` id resolves, `strand_to_objective_map` covers L1–L8
one-to-one. Inline `learning_objectives[]` mirrors match root `objective_text` character for
character (string equality) and each carries `image_examples: []`. Concept ids run C1…C12
chapter-continuous, correctly diverging from the topic number from T3 onward (four topics carry two
concepts each). All 8 media ids match `MEDIA_ID_RE` (concept-scoped). Recalls are `.RQ{n}` with
`legacy_id` `.TR{n}`; **the string `.SR` occurs nowhere in the merged plan.** `publication_id` is
non-null (flagged placeholder, see Gaps). `topic_type` is the authored enum (`STORY_TELLING` ×7,
`CONCEPT` ×1) throughout, which Agent 14/15 maps to the closed server enum `instructional` at emit.
Summaries strictly increase on all 8 topics. Invariant 11 (`figures_of_speech` quotes only words
found verbatim) is vacuously satisfied — `[]` everywhere, nothing to verify. **Invariant 2** — no
authored field outside `original_chunk` carries a craft label — now holds on all 8 topics, including
M4.S4.T8, the one failure from the prior run.

### Exercises.

`coverage_report.blocks_found` = 14 = `exercise_inventory` length; every inventory
`verbatim_heading` present; `unanswered` is `[]`; all 61 items carry a non-empty answer. Unchanged
from the prior run — `10_exercise_solutions.json` was not touched by the owner's re-run.

### Media.

`reuse_report` `scenes: 8` equals the 8 topics whose `available_content_types` carry `"image"`;
`authored: 8`; `reused: 0`. Every node has `image_url: ""` **and** a non-empty `generation_prompt`;
no `[reused frame: …]` stamp anywhere; every `negative_prompt` carries `Devanagari script labels`.
`2d_tool` is `null` for the whole chapter — 0 of the permitted 1. Unchanged from the prior run.

### Publication.

`publication_text` on 8/8. `publication_chunk` byte-identical to `original_chunk` on 8/8 (verified
against the rebuilt merge). `concept_publication` blocks match `concepts[].content[]` by
`concept_id` + `content_index` on every one of the 12 paragraph-type blocks. `બાળકો`, `જુઓ —` and
`બોલો` occur **zero** times in any `publication_text` or `concept_publication.publication_text`.
Unchanged from the prior run — `16_publication.json` was not touched by the owner's re-run, and its
one paragraph for M4.S4.T8 already avoided the craft label even before A5's fix (only `05`'s own
`modified_chunk` carried the defect).

---

## E–G (reported)

- **30 of 61 exercise items are reported `unmapped`, and that is the honest number.** Never emptied
  by inventing a `covered_by_topics`. The families: personal-opinion વાતચીત (EX12, on other bhakti
  poets a child may know); the standalone સુભાષિત (EX21); all six generic પરિસ્થિતિ-આધારિત prompts
  (EX34–EX39); the four ઉદાહરણ-મુજબ vocabulary items whose headword never occurs in this chapter's
  own શબ્દાર્થ or reading text beyond the block's own example (EX40–EX43); the three Gandhi-letter
  and five mock-bill items that are exercise-embedded reading matter, never chapter text (EX44–EX51,
  per `01_meta.json`'s own extraction_notes); all nine generic સંયોજક-practice sentences
  (EX52–EX60); and the standing L1-medium અનુવાદ paragraph, which is about a different historical
  figure, રવિશંકર મહારાજ (EX61). Every mapped item's `covered_by_topics` id resolves to a real topic
  (checked against the registry above; 0 dangling refs).
- **The closing ચર્ચા-વિચારણા box (page 52, bullets `સંત કોને કહેવા ?` / `સંત બતાવે પંથ.`) is answered
  nowhere.** `01_meta.json`'s own `extraction_notes[]` records it explicitly as "NOT an exercise,
  recorded here instead," and it is correctly absent from `exercise_inventory` — so
  `coverage_report`'s `blocks_found`/`blocks_answered` parity (14 = 14) is genuinely complete against
  the inventory as scoped, not silently short.
- **Sensitivity soft items (4 of 6 in `08_sensitivity.json`), all held.** M1.S1.T2, M2.S2.T3,
  M2.S2.T4 and M3.S3.T5's ધર્મ cautions — keep the ચમત્કાર/લોકકથા material as literature and living
  devotional tradition, never theology to affirm, compare, or debunk — are honoured throughout the
  authored fields via the `કહેવાય છે` / `જાણે` hedge.
- **Craft ceiling now holds everywhere, with no exception.** `અલંકાર`, `પ્રાસ`, `સમાસ`,
  `સાહિત્યપ્રકાર` occur zero times anywhere in the merged plan; `છંદ` occurs exactly twice, both
  legitimately inside `M4.S4.T8.original_chunk`/`publication_chunk` (the book's own printed
  sentence) — the illegitimate third occurrence inside `modified_chunk` from the prior run is gone.
- **G, the seven usual mistakes: all seven now absent.** No સાર+બોધ+પ્રશ્નોત્તર substitution (this is
  narrative ચરિત્ર, taught as પ્રસંગ, not summarised-then-moralised); nothing merged or split that
  should not be (all eight printed ઘટના markers became exactly eight topics, four legitimately
  carrying two concepts each); no પદ split line by line or its ટેક lifted out (no independent પદ is
  printed at all); no poetic licence silently corrected; **mistake 5 (an અલંકાર/craft-device named
  because the field existed) — previously present in `modified_chunk` — is now absent**, confirmed by
  the zero-hit scan above; `real_life_example` is Indian, single, and inside std-8 reach on all 8
  topics; સ્વાધ્યાય was not cut as teaching topics.

---

## Media

`reuse_report`: **scenes 8 · authored 8 · reused 0 · rejected []** — no frame was rejected because no
Gujarati frame pool exists to draw from. One illustration per reading scene, one per topic, each
concept-scoped (`M1.S1.T1.C1.IMG1` … `M4.S4.T8.C12.IMG1`), all `image_url: ""` with a real
self-contained `generation_prompt`, all `negative_prompt`s carrying `Devanagari script labels`.
`2d_tool` is `null` for the whole chapter — 0 of the permitted 1. `Images: 0/8` is written as zero
deliberately: nothing is reused, nothing is generated yet.

---

## Gaps

- **`publication_id` is a flagged placeholder, not a verified value.** `1` is written to satisfy the
  non-null requirement, but `phase2_contract.md` rule 1 states plainly that `1` is CBSE's publication
  row and is not portable to GSEB. The real GSEB row must be fetched from the education DB
  (**VERIFY-2**) before any Phase 8 upload.
- **`chapter_master_id` is `null`.** Mandatory for upload, not discoverable from the LP2 API, fetched
  per chapter from the education DB (VERIFY-2). Never derived by arithmetic.
- **`textbook` carries `11_pages.json`'s board-profile convention `"ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 8"`,
  not a value confirmed off a rendered cover** — the std-8 cover was not among the supplied renders.
  Fail-soft, carried, flagged. Confidence `medium`. Owner `agents/01_ingestion_genre_diagnosis.md`,
  once a cover render exists.
- **`textbook_url` is a local path string** (`../Textbooks-pdf/std-8/ch-06-pid-parai-jane-re.pdf`) —
  the GSEB readers have no hosted URL. `textbook_pages` `46–52` is confidence `medium`, read off the
  printed folios on page-1 and page-7 renders and agreeing with the manifest row. Never blocks
  (`11_pages.json` fails soft by design).
- **`chapter_id` / `plan_id` board and medium segments are UNVERIFIED (VERIFY-1).**
  `gseb_eng_gujarati8_ch6` follows `naming_conventions.md`, but a wrong medium slot uploads clean and
  mis-files the plan under the wrong medium column. Confirm both segments against the live server
  before the first upload.
- **`subject_ref_id` and `medium_id` are `null` by design** — server-injected, in
  `VOLATILE_TOP_LEVEL_KEYS`. No GSEB subject record is confirmed; nothing carried over from the Hindi
  pack.
- **`english_plan_id` / `english_chapter_id` are `null`** — a Gujarati chapter has no English twin.
  Not a gap to be closed.
- **`ordering` is absent from the root by design** — Agent 14/15's to set at emit; 31 of the 32
  contract root keys are written here. `topic_title` is set to the printed chapter name
  `પીડ પરાઈ જાણે રે !`, mirroring `unit_title`; derived, not authored by any agent.
- **Render provenance is single-rasterisation**, per the orchestrator constraint (renders are shared
  and not re-run). This re-QC pass read no PNG under `_renders` — `00_chapter_normalized.md` and the
  upstream JSONs answered every question this pass needed, including confirming the corrected
  `modified_chunk` matches the rebuilt `05_with_content.json`.
- **`01_meta.json`'s own `structure_inventory.ghatna: 5` is a narrower count than the 8 topics
  cut** — Agent 5's `notes[]` reconciles this explicitly (5 counts "distinct named legends," 8 counts
  every printed `[[ઘટના: …]]` marker per Agent 2's one-marker-one-topic rule); the marker count (8)
  is the one this agent's own B-section check uses, and it is exact.

---

## LP2 validator

**Phase 8 Validation Run — 2026-08-29**

```json
{
  "success": false,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati8_ch6_v1",
  "validation_errors": [
    "root: 'publication_id' is required and must not be null"
  ],
  "message": "1 validation error(s)"
}
```

**Result: VALIDATION FAILED** — The learning plan requires `publication_id` to be set to a real GSEB publication row before upload. Per the Gaps section above, `publication_id` is currently a placeholder value `1` (CBSE's row) and must be replaced with the correct GSEB value from VERIFY-2.
