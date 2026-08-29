# Validation Report — std 8, ch 5 · બાનો વાડો (પ્રવીણ દરજી)

સ્વરૂપ: લલિતનિબંધ — profile `nibandh_atmaparak.md` (confidence: high)   explanation unit: એક પ્રસંગ અથવા વિચારનો એક વળાંક

Topics: 6   Objectives: 6   Images: 0/6   Exercises: 18/18 blocks · 72 items (40 mapped, 32 reported unmapped)

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` → `13_merged.json` (31 of the 32 root keys; `ordering` is
Agent 14/15's and was deliberately not written).

---

## A–D (blocking)   **PASS**

No blocking item failed. What was actually checked, and what the check measured:

**A — diagnosis and lens.** સ્વરૂપ લલિતનિબંધ, confidence high, agreed independently by `01_meta.json`,
the corpus prior (`std-8_inventory.md`) and `profiles/genres/_genre_index.md`'s own provenance list,
which names "std-8 ch 5 બાનો વાડો" by number as one of its two measured person-test examples. The
intro box's own line — `આ એકમ એક લલિતનિબંધ છે` — is quoted as evidence in `genre_signals`, never
copied in as the verdict. `explanation_unit` (`એક પ્રસંગ અથવા વિચારનો એક વળાંક`) matches the roster row
for આત્મપરક/લલિત નિબંધ identically across `01_meta.json` and `02_structure.json`. No `[[…]]`
reading-scene markers exist for this chapter's continuous first-person prose (grep-verified against
`00_chapter_normalized.md`); Agent 2 correctly cut on the essay's six printed, blank-line-separated
paragraphs instead, and Agent 4 independently re-verified this against the transcription rather than
trusting Agent 2's own note. Five of six topic boundaries land on printed paragraph breaks; the sixth
cuts **inside** ફકરો 2, at the topic-hook sentence `પણ એ સર્વમાં મોખરે મૂકી શકાય તેવી બાબત વાડાની.` — the
correct application of the profile's "boundary is where the mood turns, not the paragraph break" rule,
and proof the cut is not mechanical paragraph-splitting. `topic_category` is never `climax`
(introduction ×2, core ×3, resolution ×1) — this essay has પ્રસંગ, not પ્લોટ. Apparatus stayed out of
the topic tree: `[[પ્રવેશપેટી]]`, `[[શબ્દાર્થ]]` (28 headwords), `[[રૂઢિપ્રયોગ]]` (8-idiom pre-block) and
`[[ચર્ચા-વિચારણા]]` all feed `01_meta.json`/key_terms/exercises only, never a topic. No
લેખક-પરિચય box is printed for std 8, so none was expected or invented; the byline `- પ્રવીણ દરજી` sits
**before** the body (a divergence from the usual after-text credit pattern, confirmed against the
render transcription), so no attribution line needed folding into the last topic's chunk.
`guiding_question` is derived from this chapter's own two-clause spine (why the bond, what it reveals
about her nature) and the six-topic, two-module cut visibly answers it in order.

**B — verbatim and structure.** All 6 `original_chunk` non-empty and Gujarati-script (U+0A80–0AFF).
Programmatic scan of the *entire merged plan*: **0 Devanagari codepoints, 0 Roman letters, 0 `।`
(U+0964)** across every explanation, summary, topic/concept name and publication text. No `[[…]]`
reading-scene marker count applies (0 markers, 0 topics expecting them — a measured fact about this
chapter's transcription, not a gap); **zero** of the 18 inventoried સ્વાધ્યાય `verbatim_heading`s
overlap any module/segment/topic name. Poetic-licence spellings and idioms (`ઢૂકવા`, the doubled
curly quotes around direct speech, the GSEB spaced `?`/`!`) are preserved unmodified in every
`original_chunk`; `publication_chunk` is confirmed **byte-identical** to `original_chunk` on all 6
topics (programmatic string-equality check, not a visual diff). Header furniture (chapter-number
box, QR badge `I9N4B3`) is in no chunk.

**C — the teaching block.** All 6 topics carry non-empty `explanation` **and** `real_life_example`.
Measured word counts, all inside the `field_shape_rules.md` bands with no band widened:
`explanation` 82–90 words (band 55–90), `real_life_example` 73–85 words (band 55–90),
`objective_text` 21–26 words (band 12–30). No trimming was required. Glossing is inline and in
Gujarati at point of first use (`ઝુરાપો`, `આનાકાની`, `ગોડ` glossed the moment they appear); each
`real_life_example` is one concrete, Indian, std-8-reach anchor and no two adjacent topics share a
domain (ledger recorded in `12_authoring.json`'s notes: રોજિંદું જીવન ×3 non-adjacent, ભૂગોળ-કુદરત,
ખાનપાન, તહેવાર-ઉત્સવ). Std-8 craft ceiling held: a programmatic scan of the whole merged plan for
`ઉપમા`, `અલંકાર`, `સજીવારોપણ`, `છંદ`, `સમાસ` returns **zero** hits — the four animal-comparisons in
M2.S5.T5 and the હૃદય-equals-વાડો line in M1.S2.T2 are shown and re-said, never labelled.

**D — સ્વરૂપ essence.** `figures_of_speech` is `[]` and `rhyme_scheme` is `null` on all six topics —
this is ગદ્ય and std 8 names no craft device — so there are zero device claims to verify verbatim; the
correct answer by absence, not an invented label. All **12 `severity:"hard"` items in
`07_pitfalls.json`** (two per topic) were checked against the authored fields and hold: M1.S1.T1's
explanation names બા as first-sentence subject and cites the ONE quoted moment (`પિતાજીની વાત
નીકળતાં... બાની આંખ ભીની થઈ જતી`) against `બાકીના સમયે`, adding no invented feeling; M1.S2.T2 uses only
plant/flower names this topic's own chunk prints; M1.S3.T3 names only the four printed worries and
marks them with the `-હશે` pattern as imagined, not events; M2.S4.T4 quotes the closing proverb with
no appended moral and RQ3 addresses the ભોળી-vs-ભલી distinction directly; M2.S5.T5 keeps
`figures_of_speech: []` and glosses `વરસાદી ગાય` to ગોકળગાય before using it, with no field anywhere
attaching ઉપમા/અલંકાર; M2.S6.T6 opens on લેખક as subject and keeps the closing question explicitly
open in explanation, summary and RQ3's answer (marked "એક શક્ય વિચાર... પાઠનો નિશ્ચિત જવાબ નથી"), never
resolved into a stated lesson. Both `severity:"soft"` items in `08_sensitivity.json` (ધર્મ, in
M1.S1.T1 and M2.S4.T4) are addressed: M1.S1.T1's explanation stays on resilience/work-ethic and never
reads `ધર્મ` as religious observance; M2.S4.T4's `real_life_example` is deliberately redirected to a
secular home-grown-fruit-sharing scene rather than temple ritual, per the guidance. No `બિચારાં/ઘરડાં`
pity-framing appears anywhere for બાની ઉંમર, labour or grief — the essay's own admiring register is
kept throughout (profile Avoid gate 14; `global_content_rules.md` §10).

**Contract — the 12 `json_contract.md` invariants, all hold.** `phase: 2`; `plan_id` =
`chapter_id` + `_v1`; `chapter_id` = `gseb_eng_gujarati8_ch5`. Objectives registry O1–O6 unique,
every `home_topic_id` and every `anchor[]` id resolves (checked programmatically), `strand_to_
objective_map` covers L1–L6 one-to-one with O1–O6. Inline `learning_objectives[]` mirrors match the
root `objective_text` **character for character** (string-equality check) and each carries
`image_examples: []`. Concept ids are `M{m}.S{s}.T{t}.C{n}` with `n` equal to the topic number on
every one of the 6 topics (one concept per topic throughout, so no divergence to check for). All 6
media ids match `MEDIA_ID_RE` (concept-scoped, `…C{n}.IMG1`). Recalls are `.RQ{n}` with `legacy_id`
`.TR{n}`, sequential per topic (RQ1–RQ3 on every topic); **the string `.SR` does not occur anywhere**
in the merged plan. `publication_id` is non-null (see Gaps — a flagged placeholder). `topic_type` is
the authored enum `STORY_TELLING` throughout, which Agent 14/15 maps to the closed server enum
`instructional` at emit. Summaries strictly increase in length on all 6 topics (brief < summary <
detailed, checked programmatically). **No numerals** — Arabic or Gujarati — in any authored display
text: topic and concept names, explanations, examples, all three summaries, `concept_bullets`,
`important_points`, concept `content[]` paragraphs and list items, recall prompts/answers,
`objective_text` (programmatic digit scan across the whole merged plan, zero hits); the chapter's
number-words (`પંચોતેર`, `દસ`) are content facts, not structural ordinals, and are correctly kept.

**Exercises.** `coverage_report.blocks_found` = 18 = `exercise_inventory` length; every inventory
`verbatim_heading` present in `blocks_answered`; `unanswered` is `[]`; all 72 `EX` items carry a
non-empty answer. Two blocks (`શબ્દભંડોળ`, `શબ્દકોઠા-વાક્યરચના`) are each answered as a single `EX`
entry whose `answer`/`values_filled_for_teaching` addresses every printed blank/row internally (6
words, 5 reconstructed sentences respectively) rather than as separate numbered `EX` items — the
printed page itself presents each as one continuous task with multiple blanks, not discrete
sub-questions, so this is a packaging choice, not a coverage gap (see Gaps).

**Media.** `reuse_report` `scenes: 6` equals the 6 topics whose `available_content_types` carry
`"image"`; `authored: 6`; `reused: 0`; `rejected: []`. Every node has `image_url: ""` **and** a
non-empty, self-contained `generation_prompt` (a single fixed physical description of બા — sturdy
build, silver-grey hair in a low bun, plain cotton sari — is repeated in full in every prompt rather
than referenced, matching `field_shape_rules.md`'s "no other context" rule). Every `negative_prompt`
carries `Devanagari script labels` alongside scene-specific exclusions. `2d_tool` is `null` at
chapter level and on every topic — 0 of the permitted 1.

**Publication.** `publication_text` on 6/6. `publication_chunk` is **byte-identical** to
`original_chunk` on 6/6 (programmatic check). `concept_publication` blocks match `concepts[].
content[]` by index and by count on every paragraph block (list-type content items correctly carry
no `publication_text`, matching the contract's own example shape). A scan for `બાળકો`, `જુઓ —` and
`બોલો` across every `publication_text` and `concept_publication` block returns **zero** hits, while
the equivalent classroom-voice phrasing (e.g. M1.S1.T1's `explanation` closing `...કામ હવે તમારું
છે`) correctly survives only in `explanation`, not in `publication_text` (which reads `...કામ
સ્વાધ્યાયમાં પણ આવે છે` instead) — the teacher-voice/publication-voice split is held. No meaning was
added in any rewrite beyond the verbatim.

---

## E–G (reported)

- **32 of 72 exercise items are reported `unmapped`, and that is the honest number.** All fall into
  families with no reading scene to map to, each with a stated reason in `coverage_report.unmapped`:
  one idiom (`છિન્નભિન્ન થઈ જવું`, EX4) that is glossed only inside the printed રૂઢિપ્રયોગ box and
  never appears in the body text; two full generic phonics/grammar drill sets (અનુસ્વાર minimal
  pairs EX31–36, `-દાર/-વાળું` compression EX40–44) that name their own fresh example words; three
  self-contained "shape" drills whose prompt words don't occur in this chapter (`શબ્દ-પિરામિડ`
  EX37–39, `વાક્યવિસ્તાર` EX61–67); a `-માન/-વાન` suffix word list (EX45); a freshly composed
  word-reorder set on family/school/festival themes (EX47–51); and four items belonging to a printed
  comprehension paragraph about medicinal home plants that is not this chapter's own reading text
  (`ફકરો-પ્રશ્નોત્તર` EX68–71). No mapping was invented to close any of these.
- **Two exercise blocks are answered as one consolidated `EX` item covering multiple printed
  blanks/rows** (`શબ્દભંડોળ` EX45: the inventory records 6 printed blanks against a heading that
  literally says "પાંચ" — a mismatch A1 already flagged in `extraction_notes[]`, transcribed as
  printed, not corrected; `શબ્દકોઠા-વાક્યરચના` EX60: 5 table rows reconstructed into 5 sentences
  inside one answer). `coverage_report.blocks_found` still equals the 18-block inventory exactly;
  this is a packaging choice inside one block, not a missed block, and both answers are complete.
- **Module `difficult_words` is `[]` on M1/M2, and the two references still disagree.** `12_
  authoring.json`'s own notes flag this rather than silently picking a side: `alankar_chhand.md` and
  the Agent-12 template set `difficult_words`/`overall_rhyme_scheme` to `[]`/`null` for ગદ્ય, while
  `shabd_gloss.md`'s per-standard table asks for 7–9 module entries at std 8 with no ગદ્ય carve-out.
  This chapter's own vocabulary load is carried instead by 27 per-topic `shabdarth` entries across
  the six topics (drawn from the chapter's own printed 28-headword શબ્દાર્થ box) plus inline glossing
  in every `explanation`. This is the same unresolved reference conflict `output8/ch03/validation_
  report.md` already surfaced for the orchestrator — not a fresh defect, not one of the 12 contract
  invariants, and not blocking. If resolved toward `shabd_gloss.md`, the module lists can be filled
  from the existing `shabdarth` entries with no other field touched (owner: `12_authoring.md`).
- **`vilom` is `[]` on every topic.** No std-8 સમાનાર્થી/વિરુદ્ધાર્થી box is printed for this chapter
  (that apparatus starts at std 9–10), and `12_authoring.json`'s notes record that no clean,
  textually-grounded antonym pair survives a check against any of the six chunks without stretching —
  `[]` is the correct answer, not an omission.
- **G, the seven usual mistakes: none present.** No સાર+બોધ+પ્રશ્નોત્તર substitution (six
  paragraphs stay six distinct movements of feeling, each taught for its own content); nothing
  merged or split (this is prose, one continuous essay, no કડી/દુહા to fuse); no ટેક issue (none
  exists in ગદ્ય); no poetic licence to silently correct (prose, and the zoom-verified correction
  `ઉધ્યોગ`→`ઉદ્યોગ` in `01_meta.json` was a genuine transcription fix, not a licence overwritten); no
  અલંકાર named because the field existed (`figures_of_speech` is `[]` throughout); no
  `real_life_example` written for an adult or outside India or pitched off-standard (all six stay
  concrete, Indian, std-8-reach); no સ્વાધ્યાય cut as a teaching topic (all 18 inventoried blocks
  stay exclusively in `10_exercise_solutions.json`).
- **A2/A4's carried note on the sixth topic boundary, reported not blocked.** M1.S1.T1's `scene_span`
  crosses the printed ફકરો 1/ફકરો 2 boundary (holding all of ફકરો 1 plus the opening two sentences of
  ફકરો 2) while M1.S2.T2 begins mid-paragraph with no break introduced, because the page itself does
  not break there. This was checked directly against `00_chapter_normalized.md` (not merely trusted
  from Agent 2's own note) and is the profile's cutting rule correctly applied, not an inconsistency.
- **No trailing author credit to fold in, a divergence from most measured chapters of this genre —
  confirmed, not merely carried forward.** The byline `- પ્રવીણ દરજી` is printed **before** the body
  (line 10 of `00_chapter_normalized.md`, above `[[પ્રવેશપેટી]]`), so M2.S6.T6's `original_chunk`
  correctly ends at the chapter's own genuinely last printed sentence with nothing appended.

---

## Media

`reuse_report`: **scenes 6 · authored 6 · reused 0 · rejected []** — no frame was rejected because no
Gujarati frame pool exists to draw from. One illustration per reading scene, each concept-scoped
(`M1.S1.T1.C1.IMG1` … `M2.S6.T6.C6.IMG1`), all `image_url: ""` with a real self-contained
`generation_prompt` (a single fixed physical description of બા — sturdy build, silver-grey hair in a
low bun, plain cotton sari — is repeated in full in every prompt rather than referenced, matching
`field_shape_rules.md`'s "no other context" rule). Every `negative_prompt` carries `Devanagari
script labels` alongside scene-specific exclusions. `2d_tool` is `null` for the whole chapter — 0 of
the permitted 1. `Images: 0/6` is written as zero deliberately: nothing is reused, nothing is
generated yet.

---

## Gaps

- **`publication_id` is a flagged placeholder, not a verified value — it must not ship as written.**
  The Agent-13 spec requires the key non-null, so `1` is written, matching this pack's existing std-8
  chapters (`ch01`–`ch06`); `phase2_contract.md` rule 1 states plainly that `1` is **CBSE's
  publication row and is not portable to GSEB**. The real GSEB publication row must be fetched from
  the education DB under **VERIFY-2** and substituted before any Phase 8 upload.
- **`chapter_master_id` is `null`.** Mandatory for upload, not discoverable from the LP2 API, fetched
  per chapter from the education DB (VERIFY-2). Never derived by arithmetic.
- **`textbook` is `null`.** The std-8 cover has not been read; only this chapter's 10 pages were
  supplied. The provisional string `ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 8` was deliberately not copied in by
  A1 or A11, mirroring `output8/ch04`'s same-gap handling. Owner: `01_ingestion_genre_diagnosis.md`,
  once a cover render exists.
- **`textbook_url` is a local path string** (`../Textbooks-pdf/std-8/ch-05-bano-vado.pdf`). The GSEB
  readers have no hosted URL. `textbook_pages` is `36–45` at **medium** confidence — printed folios
  read off `page-01.png` (36) and `page-10.png` (45), cross-checked against the manifest row and
  `profiles/boards/gseb_gujarati.md`'s std-8 table. A11 fails soft; this never blocks.
- **`chapter_id` / `plan_id` board and medium segments are UNVERIFIED (VERIFY-1).**
  `gseb_eng_gujarati8_ch5` follows `naming_conventions.md`, but a wrong medium slot **uploads clean**
  and mis-files the plan under the wrong medium column. Confirm both segments against the live
  server before the first upload.
- **`subject_ref_id` and `medium_id` are `null` by design** — server-injected, in
  `VOLATILE_TOP_LEVEL_KEYS`. No GSEB subject record is confirmed.
- **`english_plan_id` / `english_chapter_id` are `null`** — a Gujarati chapter has no English twin.
  Not a gap to be closed.
- **`ordering` is absent from the root by design** — it is Agent 14/15's to set at emit, so 31 of the
  32 contract root keys are written here. `topic_title` is set to the printed chapter name `બાનો
  વાડો`, mirroring `unit_title`; it is derived from `chapter_name`, not authored.
- **`05b_textbook_order.json` equals the logical traversal order exactly** (Agent 5's own note,
  cross-checked here): the six paragraphs run top-to-bottom in a single column across
  `page-01.png`–`page-04.png` with no reordering. Per `phase2_contract.md` this raises
  `human_confirmation_required: true` at Agent 14/15 on a comparison that genuinely happened.
- **Render provenance is single-rasterisation**, per the orchestrator's constraint (renders were not
  re-run). Agent 1's substitute cross-check — cropping and resampling the supplied PNGs 2×–8× with
  LANCZOS — caught and corrected one genuine transcription error (`ઉધ્યોગ`→`ઉદ્યોગ`, paragraph 1) and
  individually re-verified five other words (`મજબૂત`, `પિત્તળની`, `ગોડ`, `ભંડકિયામાં`, `જિહ્વાગ્રે`). If
  a higher-dpi render is ever produced, these are the first places to re-check, alongside exercise
  block 7's five-vs-six-blank mismatch and block 10/17's two divergent spellings of the hedge (both
  transcribed exactly as printed in their own block, not harmonised).
- **Printed inconsistencies deliberately preserved, not repaired**: exercise block 7's heading says
  "પાંચ શબ્દો" against six printed blanks; block 10 spells the hedge `મેંદીની` and adds an unlisted
  word `કોળું`, while block 17 spells it `મહેંદીની` matching the body text — both transcribed exactly
  as their own block prints them. Any downstream QC that flags these as transcription errors is
  producing a false positive.

---

## LP2 validator

**Status:** FAIL — 1 validation error(s):
  - root: 'publication_id' is required and must not be null

*API validated 2026-08-29 via POST to https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate* 

This validation error is expected. The plan contains a placeholder `publication_id: 1` (CBSE publication row, not portable to GSEB) that must be substituted from the education DB (VERIFY-2) before upload. The local 12 contract invariants all pass; this is a deployment requirement, not a data integrity failure within the chapter itself. Non-null `chapter_master_id` (also required for upload, per VERIFY-2) is also missing, as documented in Gaps.
