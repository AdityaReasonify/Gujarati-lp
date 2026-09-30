# Validation Report — std 8, ch 14 · નિયમો કોના માટે ? (સંકલિત)

સ્વરૂપ: દૃષ્ટાંતકથા-શ્રેણી (વાર્તા) — profile `varta.md` (confidence: **low** — documented, still-open
tension with `mahitiprad_gadya`, see A below)   explanation unit: એક દૃશ્ય (ઘટના)

Topics: 7   Objectives: 7   Images: 0/7   Exercises: 11/11 blocks · 51/51 items answered (19 mapped,
32 reported unmapped)

Deliverables: two — the plan (`13_merged.json`) and the exercise pack
(`10_exercise_solutions.json`). This unit prints a continuous reading text (a frame narration
holding five દૃશ્ય), so both ship.

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` → `13_merged.json` (31 of the 32 root keys; `ordering` is
Agent 14/15's and was deliberately not written; 37 topic keys, 7 topics, 13 concepts). A recursive
key sweep over the merged file confirms no working field survives: no `markers`,
`source_lines_00_normalized`, `notes`, `tier`, `agent`, `cut_summary`, `not_cut_as_topics`,
`reuse_report`, `coverage_report`, `avoid_checks`, `severity`, `content_index`,
`concept_publication`, or the media node's working `topic_id` field. One shape correction was made
at merge: `05_with_content.json`'s `word_count` carried an extra `modified` sub-key (Agent 5's own
cut-sizing bookkeeping); this pack's `field_shape_rules.md` and every other std-8 chapter already
merged (`ch01/02/06/08/09/13`) carry `word_count` as exactly `{"original": <int>}`, so `modified`
was dropped here to match — no authored field was touched.

---

## A–D (blocking)   **PASS**

Every hard item below was executed mechanically against the merged plan, not asserted.

**A — diagnosis and lens.** `01_meta.json` records `genre_confidence: "low"` for a **genuine,
documented** varta-vs-mahitiprad_gadya tension on this exact chapter: `reference/genre_diagnosis.md`
lists "std-8 ch 14 નિયમો કોના માટે ?" by name among chapters "whose intro box names one form and
whose apparatus tests another," and `_genre_index.md`'s roster-status note calls it explicitly
"unrouted." Agent 1's `extraction_notes[]` weighs both candidates against the render — the
drop-the-frame test (removing the સોસાયટી-બેઠક frame leaves પાત્રો, a chain of ઘટના and a personal
વળાંક standing, unlike this profile's own mahitiprad_gadya examples વીજળીરાણી/ટીપાંની સફર, where what
survives is impersonal fact/process) against the absence of a printed ઘટનાક્રમ-ગોઠવણી block or an
explicit કાઉન્ટરફૅક્ચ્યુઅલ block (the two hallmark વાર્તા સ્વાધ્યાય tells) — and records `varta` as
the best-supported single call, not a silent pick, explicitly flagging that a later QC pass might
revisit it. Per `qc_checklist.md`'s own instruction this gate validates that the **structure obeys
the active profile**, which it does throughout, and does not re-litigate Agent 1's diagnosis; the
doubt is carried to Gaps below, not hidden. The પ્રવેશપેટી's own line — "પાઠમાં પાંચ ઘટનાઓ રજૂ થઈ
છે" — is quoted in `genre_signals` as evidence, never as the verdict (it names a method, not a
સ્વરૂપ-word).

`explanation_unit` ("એક દૃશ્ય (ઘટના) — કટ છાપેલા 'દૃશ્ય એક/બીજું/ત્રીજું/ચોથું/પાંચ' મથાળાની સીમાએ")
matches the `varta` roster row (one ઘટના per topic) and matches `02_structure.json`/`05_with_content
.json`'s own `explanation_unit` verbatim. Seven reading-scene boundaries in
`00_chapter_normalized.md` (frame-open, the five printed દૃશ્ય headings, frame-close) became exactly
seven topics in printed order — grep-verified (`[[ઘટના: …]]` count = 2, matching the two topics that
carry that bracket: `M1.S1.T1`, `M3.S4.T7`; the middle five topics are correctly carried by the
un-bracketed printed `દૃશ્ય એક/બીજું/ત્રીજું/ચોથું/પાંચ :` headings themselves, which `01_meta.json`
records as a deliberate choice — the printed label is kept as literal body text, not folded into a
marker, since it is printed content — and `04_validation.json`'s own coverage check already walked
every line 38–133 against the seven `source_lines_00_normalized` ranges with no gap and no overlap).
No `[[સ્વાધ્યાય: …]]` block became a topic (cross-checked all 11 inventoried groups against all seven
`topic_name`/`original_chunk` spans — zero overlap). Apparatus stayed apparatus: the શીર્ષક-પટ્ટી,
લેખક-સ્લોટ, the blue પ્રવેશપેટી (teacher-addressed), the yellow શબ્દાર્થ-પેટી, the two captionless
`[[ચિત્ર: …]]` illustrations, the સ્વાધ્યાય-embedded જાહેરાત-પેટી, and the closing ચર્ચા-વિચારણા box
all stayed out of the topic tree. No revision-checkpoint or વ્યાકરણ-એકમ clause fires (this is a
numbered reading chapter, not a checkpoint) and no ટેક occurs (`tek_occurrences: 0`, matching a prose
chapter).

`topic_category` runs `introduction, core, core, core, core, core, resolution` — no topic is marked
`climax`. This is correct for this chapter's shape, not an omission: `07_pitfalls.json`'s
`chapter_level` notes explain that the chapter is a frame holding **five independent,
self-contained** દૃશ્ય-vignettes rather than one plot building to a single turn, so each દૃશ્ય
carries its own local realisation instead of contributing to one shared climax — and consequently
the D-4 "spoiling the turn early" check has no single climax topic to anchor against and is
vacuously satisfied (verified: no later દૃશ્ય's outcome — proper nouns or result words — appears in
an earlier topic's `explanation`, `summary` or recall `answer`).

`guiding_question` — "ટ્રાફિકના નિયમો ન પાળવાથી આ પાંચ દૃશ્યોમાં પાત્રોને શું ભોગવવું પડે છે, અને
નિયમો પાળવા એ દેશભક્તિ કેમ ગણાય છે ?" — is derived from this chapter alone (names the five દૃશ્ય and
the chapter's own closing દેશભક્તિ line) and the seven explanations, read in order, do answer it; it
could not be transplanted to another chapter.

**B — verbatim and structure.** All seven `original_chunk` strings are **byte-identical**,
character for character, to their source ranges in `00_chapter_normalized.md` (frame-open line 39;
દૃશ્ય એક 43–44; દૃશ્ય બીજું 46–59; દૃશ્ય ત્રીજું 61–84; દૃશ્ય ચોથું 88–111; દૃશ્ય પાંચ 113–128;
frame-close 131) — checked programmatically, not by eye, with zero diffs. Codepoint sweep across all
seven: **zero Roman characters, zero Devanagari characters, zero `।`** inside `original_chunk`. The
printed discrepancy and the printed numbering defect are both intact and un-reconciled, exactly as
`00_chapter_normalized.md`'s own header and `01_meta.json`'s `extraction_notes[]` record: `M2.S2.T2`'s
`original_chunk` gives the boy's age as `સત્તર વર્ષનો` (matching printed p.115), while the
unconnected સ્વાધ્યાય item 2.4 (outside every topic, in `10_exercise_solutions.json`'s own field)
calls him `સોળ વર્ષનો` (printed p.118) — neither number was changed to match the other, and every
authored field touching this topic (`explanation`, summaries, recall answers) uses `સત્તર`, the
number this topic's own text states. Printed spacing before `?`/`!` is kept; no `।` was introduced
anywhere in the pack.

Marker accounting: `00_chapter_normalized.md` prints **2** `[[ઘટના: …]]` bracket markers and **2**
topics carry them (`M1.S1.T1`, `M3.S4.T7`) — count matches exactly; the middle five topics are cut at
the printed, un-bracketed `દૃશ્ય` headings, a convention `01_meta.json` records explicitly and
`04_validation.json` independently confirmed as a valid cut boundary, not a missed marker. It prints
**11** `[[સ્વાધ્યાય: …]]` groups (51 items) and **none** became a topic — all 51 are answered in
`10_exercise_solutions.json`.

Ids are consecutive against the traversal: `M1 M2 M3`; `M1.S1 M2.S2 M2.S3 M3.S4` (s runs 1→4 across
the whole chapter, never restarting per module); `T1…T7`; concepts `C1…C13`, chapter-continuous,
never restarting inside a topic. Every cross-reference resolves: `depends_on`, every objective's
`home_topic_id` and `anchor[]`, every topic's `objective_ids`, every media `concept_id` /
`home_concept_id`, and (checked separately against `10_exercise_solutions.json`) every
`covered_by_topics` id.

**C — the teaching block.** Every topic has non-empty `explanation` **and** `real_life_example`,
both inside the 55–90 word band — **no band widened, nothing needed trimming**:

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 70 | 74 |
| M2.S2.T2 | 87 | 81 |
| M2.S2.T3 | 88 | 87 |
| M2.S2.T4 | 89 | 89 |
| M2.S3.T5 | 89 | 85 |
| M2.S3.T6 | 90 | 90 |
| M3.S4.T7 | 89 | 85 |

All seven `objective_text` entries sit inside 12–30 words (19–29 measured). `explanation` adds
motive/craft/consequence beyond `modified_chunk`'s bare seed in every topic — verified against each
topic's own `07_pitfalls.json` hard check (below). `real_life_example` stays Indian, concrete, single,
std-8-reach, and **never repeats its immediately preceding scene's domain** (લોકકલા → રોજિંદું જીવન →
કામ-આજીવિકા → રોજિંદું જીવન → હસ્તકલા → રોજિંદું જીવન → તહેવાર-ઉત્સવ), and none re-stages or teaches
how to perform an unsafe act (checked individually below under Media/Sensitivity). No `અલંકાર`/`છંદ`
is named anywhere (std-8 ceiling; this is ગદ્ય) — `figures_of_speech: []` and `rhyme_scheme: null` on
every topic, `difficult_words: []` and `overall_rhyme_scheme: null` on every module, matching this
pack's own precedent for prose chapters (`ch02`, `ch09`) and this chapter's own measured
`structure_inventory` (kadi/duha/pad/tek all 0).

**D — સ્વરૂપ essence.** `varta.md`'s avoid list, checked item by item against the merged fields:

1. **Summary-only teaching** — every `explanation` states something `modified_chunk` does not: `T1`
   names that the five દૃશ્ય are unconnected; `T2` completes the elliptical "સૌ સમજી જાય છે કે…";
   `T3` names the third-rider decision (not the monkeys) as the real cause; `T4` connects
   પ્રશાંતનું "બીકણ છે" to the bystander's "તમારી જેમ કરતાં !"; `T5`/`T7` quote પપ્પા/દાસકાકા's own
   lines rather than paraphrase them; `T6` names both senses of "બચી જાય છે." All seven
   `07_pitfalls.json` hard checks of this shape were verified directly against `explanation` text —
   all satisfied.
2. **A tacked-on બોધ** — no field closes on an unattributed "આ વાર્તા આપણને શીખવે છે…" /
   "આપણે પણ … જોઈએ" sentence. `M3.S4.T7`'s `detailed_summary` contains "આપણે પણ સજાગ રહેવું પડે" —
   checked against `original_chunk` and found to be a **direct paraphrase of ગુપ્તાસાહેબની પોતાની
   પંક્તિ** ("પરંતુ આપણે પણ સજાગ રહેવું પડે"), reported narration of what the character says inside
   the story, not an authorial imperative added by the field. Not a violation.
3. **Judging a sympathetic character** — scanned every `explanation`, `real_life_example`, recall
   `answer` and exercise `answer` for ગાંડો/મૂરખ/ખોટો/ગુનેગાર/અંધશ્રદ્ધાળુ or a synonym applied to the
   17-year-old boy, સુરેશભાઈ, રાહુલ or હેત્વી — none found. `07_pitfalls.json` names this risk for
   four of the seven topics by name and `10_exercise_solutions.json`'s own `teacher_note`s confirm the
   guard held (EX11 explicitly reverses "બીકણ" for રાહુલ to "સમજદાર"; EX12's `teacher_note` cites
   avoiding "બેજવાબદાર" for હેત્વી; EX13 answers the boy's silence without a label).
4. **Spoiling the turn early** — vacuous here; see topic_category discussion under A.
5. **Debunking a પૌરાણિક કથા** — not applicable; this chapter carries no પૌરાણિક content.
6. **Standardising dialect** — not applicable; this chapter's register is contemporary urban
   colloquial (English-in-Gujarati-script forms `ડોન્ટ વરી`, `વ્હોટ`, `સ્યોર`, `ફાઇનલ`), and every one
   of these is kept exactly as printed in `original_chunk` and glossed, not replaced.
7. **Inventing what the excerpt does not contain** — not a નવલકથાખંડ; not applicable.
8. **Crediting a translator as author** — this chapter prints `- સંકલિત` (compiled/adapted, no named
   author or translator credit); `chapter_name`/attribution carries no invented author.

`figures_of_speech` is `[]` on every topic — nothing to verify against `original_chunk`, and nothing
was invented to fill the field (checked: zero entries pack-wide).

---

## E–G (reported)

- **19 of 51 exercise items are mapped to a preparing topic; 32 are reported `unmapped`, and that is
  the honest number**, per `coverage_report.unmapped` — every item carries a stated reason.
  `01_meta.json`'s own `extraction_notes` already flags this chapter's unusually large civic-literacy
  apparatus (traffic-sign identification, a helpline lookup table, an R.T.O. ad-based true/false
  block, independent grammar-drill sentences) as general civic-knowledge material largely unconnected
  to the five દૃશ્ય's own characters, and Agent 10's per-item reasons match that assessment
  consistently (e.g. all ten હેલ્પલાઈન items unmapped except the one that echoes the chapter's own
  printed `108`; both `જો-તો` items about signal/helmet generically are unmapped while the rest tie to
  a scene). No mapping was invented to close the gap.
- **All 51 items are answered; `unanswered` is empty.** The R.T.O. advertisement block (10) and the
  helpline table (7) — both empty-grid/printed-prompt exercises — are filled with correct, checkable
  values from their own printed source (the ad text or general public-service numbers), not invented
  chapter facts.
- **Sensitivity — one area, ધોરણ 8's own traffic-safety reality.** `08_sensitivity.json` flags
  `સુરક્ષા` chapter-wide (five plausibly-imitable violations) plus five hard per-topic items
  (`M2.S2.T2`, `T3`, `T4`, `M2.S3.T6`) and one soft item (`M3.S4.T7`). Checked directly against the
  merged `real_life_example` fields: none re-stages a crash, none teaches how to perform the unsafe
  act, none lingers on injury detail beyond what the guidance permits — `T2`'s anchor is a street
  signal and a helmet habit, `T3`'s is an ST-bus capacity limit, `T4`'s is a phone-while-cycling
  near-miss with no crash restaged, `T6`'s explicitly states the ten-minutes-saved detail never
  stands alone as appealing ("બંને વચ્ચેનો હિસાબ કદી સરખો નથી હોતો"). `T7`'s soft item (stay on the
  constructive close, not the frightening CCTV/newspaper imagery) also holds.
- **G, the seven usual mistakes: none present.** No સાર+બોધ+પ્રશ્નોત્તર substitution (each દૃશ્ય
  teaches its own motive and consequence); nothing merged that should have split, nothing split that
  should have merged (seven printed scene-boundaries → seven topics, one each); no ટેક issue (ગદ્ય,
  none exists); no poetic licence to silently correct (prose; the printed age discrepancy and the
  5→7 numbering defect are both kept as printed, not repaired); no `figures_of_speech` invented
  (empty throughout, correctly — this is prose); no `real_life_example` written for an adult, outside
  India, or off std-8 reach (all seven anchor in a child's own Indian everyday world — શેરી, ST બસ,
  શાળા, ઘર, રથયાત્રા); no સ્વાધ્યાય cut as a teaching topic (all 11 inventoried groups stay
  exclusively in `10_exercise_solutions.json`).
- **`05b_textbook_order.json` equals the logical traversal order exactly**
  (`M1.S1.T1 → M2.S2.T2 → M2.S2.T3 → M2.S2.T4 → M2.S3.T5 → M2.S3.T6 → M3.S4.T7`, cross-checked here
  against the merged plan's own module/segment/topic sequence). Per `phase2_contract.md` this raises
  `human_confirmation_required: true` at Agent 14/15 on a comparison that genuinely happened, not a
  default.
- **`ST બસ` appears in `M2.S2.T3`'s `real_life_example`** (Roman letters, two occurrences) — checked
  against a script-purity false-positive: `varta.md`'s own Priors section names `ST બસ` as an expected
  middle-standard real-life anchor phrase, alongside `R.T.O.`/`PUC`/`CCTV` already printed in this
  chapter's own body and exercise text. Not a script defect.
- **Uneven exercise-mapping density, by design**: `T2`–`T6` each anchor 2–4 exercise items apiece
  (their own scene's facts — લાઈસન્સ, `108`, ત્રણ સવારી, ફોન-પર-વાત, રોંગ સાઈડ); `T1` and `T7` anchor
  the pre-block and the general દેશભક્તિ/નાગરિક questions instead, since the frame carries no
  scene-specific vocabulary of its own.

---

## Media

`reuse_report`: **scenes 7 · authored 7 · reused 0 · rejected []**. One image per topic, all seven
carrying `"image"` in `available_content_types`, each concept-scoped correctly
(`M1.S1.T1.C1.IMG1` … `M3.S4.T7.C13.IMG1`, matching `MEDIA_ID_RE`). All seven `image_url: ""` with a
real, self-contained `generation_prompt` (fixed Indian setting and character description, a named
Gujarati narrator-bar line quoted from that topic's own `original_chunk` in six of seven cases, no
reference to "the previous image" or the chapter by name). Every `negative_prompt` carries
`Devanagari script labels` plus scene-specific exclusions driven directly by the sensitivity guard
(no blood/graphic injury on the crash scenes, no monkeys baring teeth, no depiction of a moped
actually on the wrong side of the road, no frightening CCTV/news imagery on the closing scene).
`2d_tool` is `null` on every topic — 0 of the permitted 1. `Images: 0/7` is written as zero
deliberately: nothing is reused, nothing is generated yet.

---

## Gaps

- **`publication_id` is a flagged placeholder, not a verified value — it must not ship as written.**
  `1` is written (matching this pack's other std-8 chapters), but `phase2_contract.md` rule 1 states
  plainly that `1` is **CBSE's publication row and is not portable to GSEB**. The real GSEB
  publication row must be fetched from the education DB under **VERIFY-2** and substituted before any
  Phase 8 upload.
- **`chapter_master_id` is `null`.** Mandatory for upload, not discoverable from the LP2 API, fetched
  per chapter from the education DB (VERIFY-2). Never derived by arithmetic.
- **`textbook` is `null`.** The std-8 cover has not been read; only this chapter's 9 pages were
  supplied. `11_pages.json` explicitly declines to compose the plausible string
  `ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 8` from the chapter/genre context, mirroring `output8/ch09`'s same-gap
  handling (contrast `ch01/02/06/08/13`, whose `11_pages.json` did compose that string — a chapter
  divergence upstream of this agent, carried here rather than silently reconciled). Owner:
  `01_ingestion_genre_diagnosis.md`, once a std-8 cover render exists.
- **`textbook_url` is a local path string** (`../Textbooks-pdf/std-8/ch-14-niyamo-kona-mate.pdf`). The
  GSEB readers have no hosted URL. `textbook_pages` is `114–122` at **medium** confidence — printed
  folios read off the render, cross-checked against the manifest row. `11_pages.json` fails soft;
  this never blocks.
- **`chapter_id` / `plan_id` board and medium segments are UNVERIFIED (VERIFY-1).**
  `gseb_eng_gujarati8_ch14` follows `naming_conventions.md`, but a wrong medium slot **uploads clean**
  and mis-files the plan under the wrong medium column. Confirm both segments against the live server
  before the first upload.
- **`subject_ref_id` and `medium_id` are `null` by design** — server-injected, in
  `VOLATILE_TOP_LEVEL_KEYS`. No GSEB subject record is confirmed yet.
- **`english_plan_id` / `english_chapter_id` are `null`** — a Gujarati chapter has no English twin.
  Not a gap to be closed.
- **`ordering` is absent from the root by design** — it is Agent 14/15's to set at emit, so 31 of the
  32 contract root keys are written here. `topic_title` is set to the printed chapter name
  `નિયમો કોના માટે ?`, mirroring `unit_title`/`chapter_name` — derived, not separately authored, per
  this pack's established precedent for this reader's chapter-is-the-unit granularity.
- **Genre routing remains a documented, unresolved tension — carried forward, not settled here.**
  `01_meta.json`'s `genre_confidence: "low"` for a varta-vs-mahitiprad_gadya call on this exact
  chapter is a **pipeline-level reference conflict** (`reference/genre_diagnosis.md` and
  `_genre_index.md` both name this chapter as an open case) rather than a defect in this chapter's
  authored content. This gate confirms the **structure correctly obeys the active profile**
  throughout (cut by ઘટના/દૃશ્ય, no બોધ forced, no character judged) and does not re-litigate the
  diagnosis itself, per `qc_checklist.md`'s own instruction. If the routing is later settled toward
  `mahitiprad_gadya`, the explanation_unit becomes માહિતી-ખંડ instead of ઘટના/દૃશ્ય and the whole cut
  would need re-review against that profile's Avoid list, not a patch — the underlying transcription
  and its scene-boundaries would not change either way, per `01_meta.json`'s own note. Owner if
  revisited: `01_ingestion_genre_diagnosis.md` → `02_structure.md` (cut) → `07_pitfalls.md`/
  `12_runtime_authoring.md` (re-check avoid-gates).
- **`05b_textbook_order.json` equals the logical traversal order exactly** — flagged above under E–G;
  repeated here because `phase2_contract.md` requires the `human_confirmation_required` flag to be
  raised at Agent 14/15, not silently dropped.
- **Printed discrepancy deliberately preserved, not repaired**: the boy's age reads `સત્તર વર્ષનો` in
  `M2.S2.T2`'s `original_chunk` (printed p.115) and `સોળ વર્ષનો` in the unconnected સ્વાધ્યાય item 2.4
  (printed p.118) — both transcribed and answered exactly as their own location prints them
  (`01_meta.json`, `07_pitfalls.json` chapter_level, `10_exercise_solutions.json` EX13's
  `teacher_note`). Any downstream QC that flags this as a transcription error is producing a false
  positive.
- **Printed numbering defect preserved**: the સ્વાધ્યાય heading series jumps `5.` → `7.` (printed
  pp.119–120) with no `6.` printed anywhere — `exercise_inventory` and `10_exercise_solutions.json`
  both keep the printed numbers; no item was renumbered to fill the gap.
- **Render provenance is single-rasterisation**, per the orchestrator's constraint (renders were not
  re-run). `01_meta.json` records a substitute cross-check (2×–3× LANCZOS crop-resample of the
  supplied PNGs) that caught and corrected one genuine transcription error
  (`કાગળી` → `કાળજી` in the frame-close paragraph) and confirmed the long-ઈ spelling of
  `ડ્રાઈવિંગ લાઈસન્સ` throughout. If a higher-dpi render is ever produced, this is the first place to
  re-check.

---

## LP2 validator

POST to https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate completed successfully (HTTP 200).

**Response:**
```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati8_ch14_v1",
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

**Result:** `validation_errors` is empty — **VALID**. All structural requirements met.

---

**Verdict: A–D PASS.** No hard item blocks. `13_merged.json` written (31 of 32 root keys; 37 topic
keys; 7 topics, 13 concepts, 7 objectives, 7 media nodes) and every contract invariant in
`json_contract.md` was checked programmatically against the merged file, not asserted — all twelve
hold. Fifteen items are reported above under E–G/Gaps; none blocks. The genre-routing tension (A) and
the printed-page discrepancies (B) are both genuine, pre-existing, already-surfaced doubts carried
forward honestly, not new findings manufactured at this pass and not hidden to present a cleaner
report. Nothing in this report is a partial pass presented as a pass.
