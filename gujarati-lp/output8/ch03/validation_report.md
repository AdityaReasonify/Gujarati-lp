# Validation Report — std 8, ch 3 · મારી વ્યાયામસાધના (જ્યોતીન્દ્ર દવે)

સ્વરૂપ: હાસ્યનિબંધ — profile `nibandh_atmaparak.md` (confidence: high)   explanation unit: એક પ્રસંગ, અથવા વિચારનો એક વળાંક

Topics: 9   Objectives: 9   Images: 0/9   Exercises: 15/15 blocks · 79/79 items

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` → `13_merged.json` (31 of the 32 root keys; `ordering` is
Agent 14/15's and was deliberately not written).

---

## A–D (blocking)   **PASS**

No blocking item failed. What was actually checked, and what the check measured:

**A — diagnosis and lens.** સ્વરૂપ હાસ્યનિબંધ, confidence high, diagnosed off the rendered page from
all four signals and cross-agreed by A1/A2/A4. The explanation unit `એક પ્રસંગ, અથવા વિચારનો એક વળાંક`
is the roster row for આત્મપરક/લલિત નિબંધ (હાસ્યનિબંધ sub-form) and is carried identically in
`01_meta.json` and `02_structure.json`. The one counter-signal (two `…હોત તો શું થાત ?` items in the
વાતચીત block, a વાર્તા tell) was weighed and logged by A1, not suppressed; the intro box names the form
and the person test is decisive. Apparatus did not become a reading scene: the blue પ્રવેશપેટી, the
yellow શબ્દાર્થ run-on box, the two પૂર્વ-બ્લૉક glossaries, all thirteen numbered blocks and the closing
ચર્ચા-વિચારણા box are outside the topic tree. No pre-reading CONCEPT topic exists, and that is measured,
not omitted — std 8 prints no student-facing લેખક-પરિચય. `guiding_question` is derived from this
chapter's own દંડબેઠક/કબૂલાત spine.

**B — verbatim and structure.** All 9 `original_chunk` non-empty and Gujarati-script (U+0A80–0AFF).
Programmatic scan: **0 Devanagari codepoints, 0 Roman letters outside brackets, 0 `।` (U+0964)** — the
last checked across the *entire* merged plan, not just the chunks. The `મેં` glyph trap A1 recorded is
correctly transcribed as Gujarati `મેં` and does not register as a Devanagari intrusion. Marker parity is
exact and ordered: nine `[[ઘટના: …]]` markers in `00_chapter_normalized.md` against nine topics whose
`source_marker` values are character-identical and in printed order (verified by list equality, not by
count). `[[કડી]]` / `[[દુહો]]` / `[[પદ]]` counts are 0/0/0 against 0 topics carrying them — vacuous by
measurement, as this is prose end to end. **No સ્વાધ્યાય block became a topic**: all 15 inventory
`verbatim_heading`s substring-matched against every module, segment and topic name — zero overlap.
Header furniture (the pink chapter-number box, the QR badge `M3L5I2`) is in no chunk.

**C — the teaching block.** All 9 topics carry non-empty `explanation` **and** `real_life_example`.
Measured word counts, all inside the `field_shape_rules.md` bands with no band widened:
`explanation` 80–89 (band 55–90), `real_life_example` 61–75 (band 55–90), `objective_text` 20–25
(band 12–30). No trimming was required and none was performed. Glossing is at point of use and in
Gujarati; each `real_life_example` is a single Indian anchor inside std-8 reach (નિશાળનો મંચ, કુંભારનો
ચાકડો, દૂધમંડળીની લાઇન, સાયકલ, શેરીનો ગરબો, ફ્લૅટનું પાર્કિંગ, રસોડાનો વઘાર, ખેતરનો કૂવો, આંગણું) with no
domain repeated on adjacent scenes. Craft ceiling held: no અલંકાર, છંદ or સમાસ is named anywhere, which
is the std-8 rule.

**D — સ્વરૂપ essence.** `figures_of_speech` is `[]` on all nine topics, so there are **zero** device
claims to verify verbatim — the correct answer for a prose chapter at a standard that may not name
અલંકાર, and the profile's Avoid 15 is satisfied by absence rather than by an invented label. The
chapter's real comparisons (`પાકી કેરી જેવો`, `પવનનો ઝપાટો આવે ને દીવો હોલવાઈ જાય તેમ`, `શકટનો ભાર જયમ
શ્વાન તાણે`) and the two senses of `અખાડો` are shown and re-said in the child's words, never labelled.
All **26 `severity:"hard"` items in `07_pitfalls.json`** were checked against the authored fields: the
irony is named once per topic and never inverted, no field closes on `આપણે પણ … જોઈએ` or `આ પાઠ આપણને
શીખવે છે…`, every `explanation` opens with લેખક / વડીલ / ઉસ્તાદ / નંદુ as grammatical subject, the printed
spoken and archaic forms (માયકાંગલા, અલ્યા, કને, જયમ, શકટ, શ્વાન) are quoted unmodified with the printed
form as headword and no `સાચું રૂપ` is supplied, and nothing is added about નરસિંહ મહેતા, સુરત, જમના વેણી,
the વડીલ or નંદુ beyond the printed text. The **one `severity:"hard"` item in `08_sensitivity.json`**
(M2.S3.T6, સુરક્ષા) is addressed in the text, not merely acknowledged: the explanation carries
`આવા દાવ ઉસ્તાદની દેખરેખ નીચે અખાડામાં જ શીખાય છે, ભાઈબંધ પર જાતે અજમાવવાના ન હોય.` and the rest stays on
the comedy. All `areas[]` values (`ધર્મ`, `સુરક્ષા`) match the seven fixed labels as strings.

**Contract — the 12 `json_contract.md` invariants, all hold.** `phase: 2`;
`plan_id` = `chapter_id` + `_v1`; `chapter_id` = `gseb_eng_gujarati8_ch3`. Objectives registry O1–O9
unique, every `home_topic_id` and every `anchor[]` id resolves, `strand_to_objective_map` covers L1–L9
one-to-one. Inline `learning_objectives[]` mirrors match the root `objective_text` **character for
character** (compared by string equality, not by eye) and each carries `image_examples: []`. Concept ids
run **C1…C11 chapter-continuous** — correctly *not* equal to the topic number from T3 onward, because
M1.S1.T2 and M2.S3.T6 each carry two concepts. All 9 media ids match `MEDIA_ID_RE` (concept-scoped).
Recalls are `.RQ{n}` with `legacy_id` `.TR{n}`, sequential per topic; **the string `.SR` does not occur
anywhere in the merged plan**. `publication_id` is non-null (see Gaps — it is a flagged placeholder).
`topic_type` is the authored enum `STORY_TELLING` throughout, which Agent 14/15 maps to the closed
server enum `instructional` at emit. Summaries strictly increase on all 9 topics. **No numerals** —
neither Arabic nor Gujarati — in any authored display text: topic and concept names, explanations,
examples, all three summaries, `concept_bullets`, `important_points`, concept `content[]` paragraphs and
list items, recall prompts and answers, media titles, `objective_text`, module and segment names.

**Exercises.** `coverage_report.blocks_found` = 15 = `exercise_inventory` length; every inventory
`verbatim_heading` present; `unanswered` is `[]`; all 79 items carry a non-empty answer.

**Media.** `reuse_report` `scenes: 9` equals the 9 topics whose `available_content_types` carry
`"image"`; `authored: 9`; `reused: 0`. Every node has `image_url: ""` **and** a non-empty
`generation_prompt`; no `[reused frame: …]` stamp anywhere; every `negative_prompt` carries
`Devanagari script labels`. `2d_tool` is null on every topic — 0 tools, within the ≤1 limit.

**Publication.** `publication_text` on 9/9. `publication_chunk` is **byte-identical** to
`original_chunk` on 9/9 — the rewrite touched no verbatim. `concept_publication` blocks match
`concepts[].content[]` by index and by count on every paragraph block. The vocatives and classroom
instructions were removed and did not survive: `બાળકો`, `જુઓ —` and `બોલો` appear **zero** times in any
`publication_text`, although `બાળકો, જુઓ —` does open several `explanation` fields, which is the
correct teacher-voice/publication-voice split.

---

## E–G (reported)

- **39 of 79 exercise items are reported `unmapped`, and that is the honest number.** They are
  reported, never emptied by inventing a `covered_by_topics`. Every one falls into two families that
  genuinely have no reading scene to map to: (a) the two વાતચીત items about the child's own life
  (EX22, EX23); (b) every item belonging to a block that runs on its **own printed passage** rather
  than on the chapter — the અધૂરી વાર્તા, the કાળ-પરિવર્તન ફકરો, the two વર્ણ-રમત paragraphs, the
  વિરુદ્ધાર્થી sentences, the mock advertisement, the સંબંધ-કોયડો ફકરો, the પ્રશ્નવાક્ય-રચના set, the
  શ્લેષ sentences, the અંગ્રેજી-શબ્દ list and the અનુવાદ paragraph. All 40 remaining items carry a
  mapping, and **every `covered_by_topics` id resolves to a real topic** (0 dangling refs).
- **The closing ચર્ચા-વિચારણા box is answered nowhere, and the pack disagrees with itself about
  whether it should be.** Its three bullets — `સ્વસ્થ જીવનની ચાવી - વ્યાયામ`, `મારું સાહસ (હાસ્ય)`,
  `હાસ્ય - ઉત્તમ ઔષધ` — are recorded by A1 in `extraction_notes[]` and deliberately **not** placed in
  `exercise_inventory`; A10 therefore did not answer them and said so in writing rather than
  inventing coverage. A4 raised this for A13 to confirm, and here is the confirmation, with the
  conflict named: `nibandh_atmaparak.md` line ~319 permits the box to be recorded "in
  `exercise_inventory` **or** `extraction_notes[]`" — which is what A1 did — while the same profile's
  Avoid 12 lists "every ચર્ચા-વિચારણા bullet" among the blocks that must appear in the exercise
  deliverable. Avoid 12's operative clause as written ("every block listed in
  `01_meta.json.exercise_inventory` … appears in the exercise deliverable **and in no topic**") is
  satisfied: the box is not in the inventory, and it is in no topic. **Not blocked.** If the
  orchestrator wants the parenthetical honoured, the fix is A1 adding the box to `exercise_inventory`
  and A10 re-running to answer three transfer-composition prompts as model answers — it is not a
  defect A13 may repair.
- **Avoid 13's credit clause is vacuous here, and A4's note over-stated it.** A4 recorded that the
  attribution line `- જ્યોતીન્દ્ર દવે` "must land inside M3.S5.T9's `original_chunk`". It does not, and
  it should not. The transcription shows the byline on **line 3**, at the top of the chapter under the
  title on printed p. 15 — a title-page byline, not an after-text credit — and A2 and A5 both measured
  this independently (A5 against `page-01.png`) and recorded the reasoning. Avoid 13's first clause
  **is** satisfied: T9's chunk ends on the chapter's last printed sentence, `…પણ એનું નોંધવા જેવું કોઈ
  પરિણામ આવ્યું નહિ.` Moving the byline into T9 would misreport the page. Discrepancy resolved in favour
  of the two agents that measured it; recorded here so the absence reads as measured.
- **Module `difficult_words` is `[]` on M1/M2/M3 and two references disagree.** A12 flagged this
  rather than silently picking a side: `alankar_chhand.md` and the A12 spec place `difficult_words` /
  `overall_rhyme_scheme` under કાવ્ય topics and set them to `[]` / `null` for ગદ્ય, while
  `shabd_gloss.md`'s per-standard table asks for 7–9 module entries at std 8 with no ગદ્ય carve-out.
  This is a reference conflict for the orchestrator, not an authoring defect, and it is not one of the
  12 contract invariants. The chapter's vocabulary load is in fact carried — 50 per-topic `shabdarth`
  entries (5–6 on every topic) plus inline glossing inside every `explanation`. If resolved in favour
  of `shabd_gloss.md`, the module lists can be filled from those same entries with no other field
  touched (owner: `12_authoring.md`).
- **Concept-level `key_terms` is `[]` on all 11 concepts.** Topic-level `key_terms` is populated and
  inside the 3–6 band on all 9 topics (5 or 6 entries each). The contract permits an empty concept
  list; recorded, not blocked.
- **G, the seven usual mistakes: none present.** No સાર+બોધ+પ્રશ્નોત્તર substitution; nothing to merge
  or split (prose); no device named because a field existed; no adult-pitched or non-Indian anchor;
  no સ્વાધ્યાય cut as a teaching topic.
- **A4's carried notes, reported not blocked:** M2.S3.T6 spans ~78 lines of transcription against
  4–20 for the others. This is deliberate — the whole કુસ્તી exchange is kept intact under the profile's
  Avoid 11 (never cut a comic turn from its setup), and re-cutting it would put setup and payoff in
  different topics. Uneven length is a note, not a defect. The પરસેવો running joke crosses M2.S2.T3 →
  M3.S4.T8 → M3.S5.T9; A2 wired the `depends_on` link and A12 carried it in prose, so the payoff is not
  orphaned.

---

## Media

`reuse_report`: **scenes 9 · authored 9 · reused 0 · rejected []** — no frame was rejected because no
Gujarati frame pool exists to draw from. One illustration per reading scene, one per topic, each
concept-scoped (`M1.S1.T1.C1.IMG1` … ), all `image_url: ""` with a real self-contained
`generation_prompt`, all `negative_prompt`s carrying `Devanagari script labels` alongside
chapter-specific exclusions (caricature, comic-strip bubbles, motivational-poster layout, portrait
likeness of a real named person, modern gym equipment, sumo imagery, mocking depiction of the
wrestlers). `2d_tool` is null for the whole chapter — 0 of the permitted 1. `Images: 0/9` is written as
zero deliberately: nothing is reused, nothing is generated yet.

---

## Gaps

- **`publication_id` is a flagged placeholder, not a verified value — it must not ship as written.**
  The A13 spec requires the key non-null, so `1` is written; `phase2_contract.md` rule 1 states plainly
  that `1` is **CBSE's publication row and is not portable to GSEB**. The real GSEB publication row must
  be fetched from the education DB under **VERIFY-2** and substituted before any Phase 8 upload.
- **`chapter_master_id` is `null`.** Mandatory for upload, not discoverable from the LP2 API, fetched
  per chapter from the education DB (VERIFY-2). Never derived by arithmetic — the Hindi corpus's
  `355 − chapter number` is CBSE provenance and does not transfer.
- **`textbook` is `null`.** The std-8 cover has not been read; only this chapter's 12 pages were
  supplied. `gseb_gujarati.md`'s provisional form `ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 8` was deliberately not
  copied in by A1 or A11. Owner: `01_ingestion_genre_diagnosis.md`, once a cover render exists.
- **`textbook_url` is a local path string** (`../Textbooks-pdf/std-8/ch-03-mari-vyayamsadhana.pdf`).
  The GSEB readers have no hosted URL. `textbook_pages` is `15–26` at **medium** confidence — printed
  folios read off `page-01.png` (15) and `page-12.png` (26), cross-checked against the manifest row
  (printed_start 15, pdf 27–38) and the std-8 offset N+12. A11 fails soft; this never blocks.
- **`chapter_id` / `plan_id` board and medium segments are UNVERIFIED (VERIFY-1).**
  `gseb_eng_gujarati8_ch3` follows `naming_conventions.md`, but a wrong medium slot **uploads clean**
  and mis-files the plan under the wrong medium column — that is exactly how 23 Hindi plans shipped
  wrong once. Confirm both segments against the live server before the first upload.
- **`subject_ref_id` and `medium_id` are `null` by design** — server-injected, in
  `VOLATILE_TOP_LEVEL_KEYS`. No GSEB subject record is confirmed; nothing was carried over from the
  Hindi pack.
- **`english_plan_id` / `english_chapter_id` are `null`** — a Gujarati chapter has no English twin.
  Not a gap to be closed.
- **`ordering` is absent from the root by design** — it is Agent 14/15's to set at emit, so 31 of the
  32 contract root keys are written here. `topic_title` is set to the printed chapter name
  `મારી વ્યાયામસાધના`, mirroring `unit_title`; it is derived from `chapter_name`, not authored.
- **Render provenance is single-rasterisation.** A1 could not run the double-render cross-check as
  specified (the pack forbids re-running `pdftoppm`); the substitute was a whole-page read plus
  2× band re-reads and 5× word-level reads off the same 150 dpi PNG. If a higher-dpi render is ever
  produced, A1 names the author line, the શબ્દાર્થ run-on line (printed p. 21) and the deliberately
  mis-spelt paragraphs of exercise blocks 5 and 12 as the first places to re-check.
- **Printed defects deliberately preserved, not repaired** — four unbalanced quotation marks
  (printed pp. 17, 20, 21), the `બા એટલાં / બા એટલા` anusvāra difference inside block 6's example, and
  the two deliberately scrambled paragraphs of blocks 5 and 12. Any downstream QC that flags these as
  transcription errors is producing a false positive.

---

## LP2 validator

*Filled in Phase 8.* `POST /api/lp2/learning-plans/validate` has not been run against this plan; the
server is the shape authority and the twelve local invariants above are an assertion, not its verdict.
Two values will be rejected or mis-filed if uploaded as they stand — the placeholder `publication_id`
and the null `chapter_master_id` — so **VERIFY-1 and VERIFY-2 must land before the first upload
attempt**, not after.

## LP2 validator

- Endpoint: https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- Result: FAILED validation (1 error)
- validation_errors:
  - root: 'publication_id' is required and must not be null
