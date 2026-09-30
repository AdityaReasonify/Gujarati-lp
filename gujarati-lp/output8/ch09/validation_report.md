# Validation Report — std 8, ch 9 · શતરંગી ભારત (સંકલિત)

સ્વરૂપ: માહિતીપ્રદ / સાંસ્કૃતિક ગદ્ય — profile `mahitiprad_gadya.md` (confidence: **low** — documented,
still-open tension with `samvad_nibandh`, see A below)   explanation unit: એક માહિતી-ખંડ

Topics: 7   Objectives: 7   Images: 0/2   Exercises: 12/12 blocks · 66 items (42 mapped, 24 reported
unmapped)

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` → `13_merged.json` (31 of the 32 root keys; `ordering` is
Agent 14/15's and was deliberately not written).

---

## A–D (blocking)   **PASS**

No blocking item failed. What was actually checked, and what the check measured:

**A — diagnosis and lens.** `01_meta.json` records `genre_confidence: "low"` for a **genuine,
documented** two-profile tension on this exact chapter: `reference/genre_diagnosis.md` and
`profiles/genres/_genre_index.md` both list "std-8 ch 9 શતરંગી ભારત" by name as an open
mahitiprad_gadya-vs-samvad_nibandh case, and `reference/corpus/std-8_inventory.md`'s own prior calls
it "વાર્તારૂપ સંવાદ". Agent 1's `extraction_notes[]` weighs four documents (including
`samvad_nibandh.md`'s own near-miss table, which names this chapter and resolves it *to*
`mahitiprad_gadya.md` because "the second voice asks questions and never holds a position") and the
rendered page itself (ગાર્ગી, the questioning voice, appears only in the opening four lines and never
again) before recording `mahitiprad_gadya` as the best-supported single call — not a silent pick. Per
`qc_checklist.md`'s own instruction, this gate validates that the **structure obeys the active
profile**, which it does throughout, and does **not** re-litigate Agent 1's diagnosis; the doubt is
carried to Gaps below rather than hidden. The intro box's own line
("…પરિચય વાર્તાસ્વરૂપે આપવામાં આવ્યો છે… આ એકમમાં પ્રશ્નો દ્વારા સંવાદ આગળ વધે છે") is quoted in
`genre_signals` as evidence — `પરિચય` (the payload) is the profile's own diagnostic example, never
treated as the verdict on its own. `explanation_unit` ("એક માહિતી-ખંડ — વક્તા બદલાય ત્યાં કાપવાનું
નહીં, તથ્ય-પગલે કાપવાનું") matches the roster row identically across `01_meta.json` and
`02_structure.json`. All 7 `[[માહિતી-ખંડ N: …]]` markers in `00_chapter_normalized.md` became exactly
7 topics, one per marker (grep-verified: `grep -c` returns 7, and `04_validation.json` independently
re-confirmed the same count against the transcription, not merely trusting Agent 2's note). No topic
carries `topic_category: "climax"` (introduction ×2, core ×4, resolution ×1) and `topic_type` is
`CONCEPT` on all seven, never `STORY_TELLING` — the drop-the-frame test's own payload (regional
dances, food, dress, "સંસ્કૃતિ એટલે માત્ર નૃત્ય નહીં") survives removal of the ગાર્ગી/વિનુદાદા/society
frame, so the essay is taught as fact-report, never as a story with a character's choice or a
વળાંક — satisfying the profile's Avoid gate 1. The blue પ્રવેશપેટી, the yellow શબ્દાર્થ box, the
રૂઢિપ્રયોગ pre-block and the closing ચર્ચા-વિચારણા box are apparatus and feed `01_meta.json` /
`key_terms` / `10_exercise_solutions.json` only — none became a topic. `guiding_question` is derived
from this chapter's own two-condition experiment (બીજા રાજ્યની કૃતિ ભજવવી → સાચી વિવિધતામાં એકતા)
and the seven-topic, three-module cut visibly answers it in order (the condition → the response → the
outcome → the message).

**B — verbatim and structure.** All 7 `original_chunk` non-empty and Gujarati-script (U+0A80–0AFF).
Programmatic scan of the *entire merged plan* (every `original_chunk`, `modified_chunk`,
`publication_chunk`, `explanation`, summary, `concept_bullets`, `important_points`, `key_terms`,
concept `content[]`, `shabdarth`/`samanarthi`/`vilom`/`vyakaran`, recall prompts/answers,
`topic_name`/`concept_name`, `objective_text`): **0 Devanagari codepoints, 0 Roman letters, 0 `।`**
across every child/teacher-facing field. (Roman letters exist only in `media[].generation_prompt` /
`negative_prompt`, which are mechanism prose written for an image model — English by design per the
Constitution and `field_shape_rules.md` — and in JSON keys/ids; neither is child-facing text.) The
code-switched Punjabi-Hindi dialogue (સમશેરસિંગ, વિનુદાદાનો જવાબ: `"ઐસે કૈસે કરેંગે ?..."`,
`"હમારે બચ્ચે... હૈ"`) is confirmed to be **Gujarati-script transcription of Hindi-register speech**,
not Devanagari — it scans clean in the Unicode check and is taught as the character's own dialect per
`07_pitfalls.json`'s soft item, never corrected. `[[માહિતી-ખંડ N: …]]` marker count (7) equals topic
count (7); **zero** of the 12 inventoried સ્વાધ્યાય `verbatim_heading`s overlap any module/segment/
topic name (cross-checked against all 7 `topic_name`s). Poetic/dialect spellings, the printed GSEB
spaced `?`/`!`, and the doubled-quote/single-quote convention are preserved unmodified in every
`original_chunk`; `publication_chunk` is confirmed **byte-identical** to `original_chunk` on all 7
topics (programmatic string-equality check). Header furniture (chapter-number box, QR badge) is in no
chunk. Ids are consecutive and every cross-reference resolves (see Contract below).

**C — the teaching block.** All 7 topics carry non-empty `explanation` **and** `real_life_example`.
Measured word counts, all inside the `field_shape_rules.md` bands with no band widened:
`explanation` 82–90 words (band 55–90), `real_life_example` 70–76 words (band 55–90),
`objective_text` 15–23 words (band 12–30). No trimming was required. Glossing is inline and in
Gujarati at point of first use (`મંત્રી`, `આમન્યા`, `કપરું`, `લહેકો` glossed the moment they appear —
L2-calibrated, glossing words an L1 std-8 reader might skip); each `real_life_example` is one
concrete, Indian, std-8-reach anchor (school event, a sports-day team draw, a neighbour's craft help,
a friend's borrowed accent, a shared meal) and the domain ledger in `12_authoring.json`'s notes
records a deliberate rotation, never three examples in one field. Std-8 craft ceiling held: this is
ગદ્ય and `figures_of_speech` is `[]` on all 7 topics — the one genuine simile in the text
("સ્વિચ પાડ્યા પછી થોડીક વારે ટ્યૂબલાઈટ ચાલુ થાય એ રીતે", M2.S4.T4) is shown and re-said in plain
words inside `explanation`/concept content, never labelled ઉપમા, matching the std-9-only
named-device-canon rule.

**D — સ્વરૂપ essence.** `figures_of_speech: []` and `rhyme_scheme: null` on all 7 topics (ગદ્ય; a
correct answer by absence, not an invented label). All **13 `severity:"hard"` items in
`07_pitfalls.json`** were checked against the merged fields and hold: M1.S1.T1's `explanation` opens
on the '`એક ભારત શ્રેષ્ઠ ભારત`' programme name itself, not on ગાર્ગી/ચા, and states no programme
content (dances/food/costumes) this topic's chunk does not yet carry; M1.S2.T2 marks the
છત્તીસગઢ exchange `'ઉદાહરણ તરીકે'` in both `explanation` and RQ3, which directly tests that it is
Vinudada's illustration and not the society's decided plan; M2.S3.T3 names every community
(ગુજરાતી, પંજાબી, મરાઠી, તમિલ, બંગાળી, મારવાડી, હરિયાણવી, છત્તીસગઢી) as printed with no generic
substitute, is taught as a rule-plus-reasoning report (never a story climax — `topic_category:
"core"`, never `"climax"`), and frames સમશેરસિંગ/વિનુદાદાનું હિન્દી-ઘાટીનું બોલવું explicitly as the
character's own dialect, "છાપકામની ભૂલ નથી" (soft item); M2.S4.T4 carries both halves of Vinudada's
clarification (the rule AND the workaround) in `explanation` and RQ2, keeps `figures_of_speech: []`
correctly rather than forcing a label, and never substitutes a generic term for 'બંગાળી'; M3.S5.T5
names every region (મરાઠી, બંગાળી, તમિળ, ગુજરાતી, પંજાબ-હરિયાણા, દક્ષિણ ભારત) as printed and frames
જોસેફભાઈની 'મોંમાં આંગળાં નાખવાં' explicitly as admiration/astonishment ("એટલે દંગ થઈ ગયા, મજાકમાં
નહીં"), grounded in the chunk's own "તોપણ…મજા આવી"; M3.S6.T6 ranks no group's કૃતિ above another's,
closes on Vinudada's own reasoning (તેર દિવસમાં…નજીક આવ્યાં) rather than an invented moral, and
transcribes 'ભારત માતા કી જય' only as printed with no political development; M3.S6.T7 reproduces the
ten printed dishes exactly (લાડુ, સુખડી, થેપલાં, ઈડલી, રસગુલ્લાં, રોટલાનું ચૂરમું, ગાંઠિયા, બાટી,
દહીં, લસ્સી) with no invented dish and closes on the chapter's own shared-પ્રસાદ image, not an
appended proverb. The 1 hard `08_sensitivity.json` item (M3.S5.T5, ધર્મ) is addressed: each concept
paragraph naming નરસિંહ મહેતા, સ્વામી વિવેકાનંદ, રાજા રામમોહન રાય and ઈશ્વરચંદ્ર વિદ્યાસાગર carries
an explicit guard sentence ("આ…સ્ટેજ પરની ભૂમિકાઓ છે, પાઠ…બીજું કંઈ કહેતો નથી") so no biography or
doctrine is implied beyond the printed stage-performance fact. All 3 soft sensitivity items (M2.S3.T3
dialect-as-mimicry; M3.S5.T5 ખાપ પંચાયત as curiosity; M3.S5.T5 જોસેફભાઈ's accent as mockery) are also
held — none of the three failure modes appears anywhere in the merged fields.

**Contract — the 12 `json_contract.md` invariants, all hold** (verified programmatically against the
merged plan, not read by eye alone). `phase: 2`; `plan_id` = `chapter_id` + `_v1`; `chapter_id` =
`gseb_eng_gujarati8_ch9`. Objectives registry O1–O7 unique; every `home_topic_id` and every
`anchor[]` id resolves to a real topic/concept; `strand_to_objective_map` covers L1–L7 one-to-one
onto O1–O7. Inline `learning_objectives[]` mirrors match the root `objective_text` **character for
character** on every topic, each carrying `image_examples: []`. Concept ids are
`M{m}.S{s}.T{t}.C{n}` with `n` chapter-continuous (C1…C11 across the 7 topics, verified explicitly
across the four two-concept topics M2.S3.T3(C3,C4), M2.S4.T4(C5,C6), M3.S5.T5(C7,C8),
M3.S6.T6(C9,C10) — no restart, no gap). Both media ids (`M1.S1.T1.C1.IMG1`, `M3.S5.T5.C8.IMG1`)
match `MEDIA_ID_RE`, concept-scoped. Recalls are `.RQ{n}` with `legacy_id` `.TR{n}`, three per topic,
sequential; **the string `.SR` occurs nowhere** in the merged plan. `publication_id` is non-null (see
Gaps — a flagged placeholder, not a verified value). `topic_type` is the authored enum `CONCEPT`
throughout, which Agent 14/15 maps to the closed server enum `instructional` at emit. Summaries
strictly increase in length on all 7 topics (`brief_summary` < `summary` < `detailed_summary`,
checked programmatically). **No numerals** in any authored display text except the chapter's own
printed date `26 જાન્યુઆરી` (M1.S2.T2's `explanation`/`summary`/`detailed_summary`/
`important_points`/concept content/`publication_text`) — a printed fact the chapter itself states,
never a structural ordinal (programmatic digit scan across the whole merged plan found this single
value and nothing else).

**Exercises.** `coverage_report.blocks_found` = 12 = `exercise_inventory` length; every inventory
`verbatim_heading` present in `blocks_answered`; `unanswered` is `[]`; all 66 `EX` items carry a
non-empty `answer`. Item counts per block match the inventory exactly (7+10+5+7+5+5+6+1+7+5+12+1,
with the 6-event ઘટનાક્રમ block correctly answered as one `EX40` entry covering all six items, matching
how the page itself prints it as a single ordering task).

**Media.** `reuse_report.scenes: 2` equals the 2 topics (M1.S1.T1, M3.S5.T5) whose
`available_content_types` carry `"image"`; `authored: 2`; `reused: 0`; `rejected: []` — no Gujarati
frame pool exists, so every scene is authored. Both media nodes carry `image_url: ""` **and** a real,
self-contained `generation_prompt`; both `negative_prompt`s carry `Devanagari script labels`.
`2d_tool` is `null` at chapter level and on every topic — 0 of the permitted 1.

**Publication.** `publication_text` on 7/7. `publication_chunk` is **byte-identical** to
`original_chunk` on 7/7 (programmatic check, not a visual diff). `concept_publication` blocks match
`concepts[].content[]` by index and by count on every topic (16/16 paragraph blocks across all 7
topics carry a matching `publication_text`). A regex scan for the vocative pattern `બાળકો,` and the
instruction markers `જુઓ —` / `બોલો` across every `publication_text` and concept `publication_text`
returns **zero** hits — the teacher-voice opener `"બાળકો, જુઓ — …"` that begins every `explanation`
correctly survives only there, never in publication text (a raw substring check for the bare word
`બાળકો` does surface two topics, but both are the chapter's own content word "children" inside
Vinudada's quoted dialogue — `"આપણાં બાળકો ને છત્તીસગઢનાં બાળકો…"` — not a classroom address; verified
by inspecting each hit's context). No meaning was added beyond the verbatim: the concept-level guard
sentences about નરસિંહ મહેતા/વિવેકાનંદ etc. are pre-existing authored teaching content from Agent 12
(present identically in `12_authoring.json` before the publication rewrite), required by
`08_sensitivity.json`'s hard item, and restrict rather than add to the chapter's own facts.

---

## E–G (reported)

- **24 of 66 exercise items are reported `unmapped`, and that is the honest number.** All fall into
  families with no reading scene to map to, each with a stated reason in `coverage_report.unmapped`:
  seven word-choice sentences (`યોગ્ય વિકલ્પ પસંદ કરીને વાક્ય ફરીથી લખો.`, EX42–EX48) about a tailor,
  a farmer, a teacher and other generic figures with no tie to this chapter — `01_meta.json`'s own
  `extraction_notes` claims blocks 1–9 all quote/paraphrase the chapter, and this run's read of block 8
  disagrees; the disagreement is recorded, not silently resolved. Four of the five `બંધબેસતો શબ્દ`
  colour-word items (EX49, EX50, EX51, EX53) are generic Gujarati word-pairings with no chunk source
  (EX52, ત્રિરંગી-ધ્વજ, *is* mapped, tying to the chunk's own `ધ્વજવંદન`). All 12 items of the
  `સાચા વાક્ય/ખોટા વાક્ય` block (EX54–EX65) are generic cause-effect sentences unconnected to this
  chapter's characters or events — here too `01_meta.json`'s claim that only items 6–12 are generic is
  checked against this agent's own read and found to understate the count (items 1–5 are equally
  unconnected); both disagreements are surfaced for the orchestrator, neither quietly patched. EX66
  (the અનુવાદ paragraph) is a generic village-rain paragraph with no character or place name from this
  chapter, matching `01_meta.json`'s own note.
- **EX66's answer is written in English, intentionally** — `teacher_note` marks this explicitly
  ("ANSWER ફિલ્ડમાં અંગ્રેજી… સ્ક્રિપ્ટ અહીં ઇરાદાપૂર્વક છે — સ્ક્રિપ્ટ-ખામી નથી"), matching the
  standing convention for this pack's અનુવાદ block (written in the medium of instruction on purpose).
  Not a script defect; not re-flagged.
- **Sensitivity notes applied where the chapter touches સમુદાય and ધર્મ** — see D above; all four
  `08_sensitivity.json` items (1 hard, 3 soft) hold in the merged fields.
- **Empty tables/lists**: none printed in this chapter (no phonics grid, no word-search puzzle) —
  nothing to fill.
- **G, the seven usual mistakes: none present.** No સાર+બોધ+પ્રશ્નોત્તર substitution (seven
  માહિતી-ખંડ each teach their own fact-step, never a moral wrap); nothing merged that should have
  split or split that should have merged (one marker → one topic throughout, checked against
  `00_chapter_normalized.md` directly); no ટેક issue (ગદ્ય, none exists); no poetic licence to
  silently correct (prose; the code-switched Hindi-register dialogue is dialect, kept as printed, not
  "corrected" toward standard Gujarati); no અલંકાર named because the field existed
  (`figures_of_speech` is `[]` throughout, including at M2.S4.T4 where a genuine simile exists but is
  taught unlabelled per the std-8 ceiling); no `real_life_example` written for an adult, outside
  India, or pitched off-standard (all 7 stay concrete, Indian, std-8-reach — school events, a
  neighbour's help, a friend's accent); no સ્વાધ્યાય cut as a teaching topic (all 12 inventoried
  blocks stay exclusively in `10_exercise_solutions.json` — the event-ordering block, which reads
  most like a વાર્તા-retelling exercise, was correctly kept out of the topic tree).
- **`05b_textbook_order.json` equals the logical traversal order exactly** (T1→T2→T3→T4→T5→T6→T7,
  cross-checked here against the merged plan's own module/segment/topic sequence). Per
  `phase2_contract.md` this raises `human_confirmation_required: true` at Agent 14/15 on a comparison
  that genuinely happened, not a default.
- **Media `generation_prompt`s carry no explicit narrator-bar string.** `field_shape_rules.md`'s
  narrator-bar guidance is conditional ("where the design uses one"); neither of the two authored
  prompts for this chapter includes one. Not treated as blocking — no contract invariant requires it
  — but flagged here as a design choice to confirm with Agent 9's owner spec if a narrator bar is
  in fact expected on every image in this pack.
- **Uneven topic length, by design, not oversight** (carried from `02_structure.json`/
  `05_with_content.json`'s own notes): M1.S1.T1 and M3.S6.T7 are short single-concept topics;
  M2.S3.T3 and M3.S5.T5 are the chapter's densest paragraphs (code-switched dialogue, five regions'
  performances) and carry two concepts each with `difficulty: "hard"`.

---

## Media

`reuse_report`: **scenes 2 · authored 2 · reused 0 · rejected []**. One illustration per reading
scene carrying `"image"` in `available_content_types` (M1.S1.T1 — ગાર્ગીની સવાર; M3.S5.T5 —
ધ્વજવંદન-કૃતિ-રજૂઆત), each concept-scoped (`M1.S1.T1.C1.IMG1`, `M3.S5.T5.C8.IMG1`), both
`image_url: ""` with a real self-contained `generation_prompt` (Indian setting, fixed physical
description, no reference to "the previous image" or the chapter by name). Both `negative_prompt`s
carry `Devanagari script labels` alongside scene-specific exclusions (for M3.S5.T5, additionally:
caricature exaggeration, mocking expression, community dress as stereotype, scoreboard/ranking
numbers — matching the topic's own sensitivity guard). `2d_tool` is `null` for the whole chapter — 0
of the permitted 1. `Images: 0/2` is written as zero deliberately: nothing is reused, nothing is
generated yet.

---

## Gaps

- **`publication_id` is a flagged placeholder, not a verified value — it must not ship as written.**
  The Agent-13 spec requires the key non-null, so `1` is written, matching this pack's other std-8
  chapters (`ch02`, `ch03`, `ch05`); `phase2_contract.md` rule 1 states plainly that `1` is **CBSE's
  publication row and is not portable to GSEB**. The real GSEB publication row must be fetched from
  the education DB under **VERIFY-2** and substituted before any Phase 8 upload.
- **`chapter_master_id` is `null`.** Mandatory for upload, not discoverable from the LP2 API, fetched
  per chapter from the education DB (VERIFY-2). Never derived by arithmetic.
- **`textbook` is `null`.** The std-8 cover has not been read; only this chapter's 9 pages were
  supplied. The provisional string `ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 8` was deliberately not copied in,
  mirroring `output8/ch04`/`ch05`'s same-gap handling. Owner: `01_ingestion_genre_diagnosis.md`, once
  a cover render exists.
- **`textbook_url` is a local path string** (`../Textbooks-pdf/std-8/ch-09-shatrangi-bharat.pdf`). The
  GSEB readers have no hosted URL. `textbook_pages` is `72–80` at **medium** confidence — printed
  folios read off the render, cross-checked against the manifest row and the std-8 offset in
  `profiles/boards/gseb_gujarati.md`. `11_pages.json` fails soft; this never blocks.
- **`chapter_id` / `plan_id` board and medium segments are UNVERIFIED (VERIFY-1).**
  `gseb_eng_gujarati8_ch9` follows `naming_conventions.md`, but a wrong medium slot **uploads clean**
  and mis-files the plan under the wrong medium column. Confirm both segments against the live server
  before the first upload.
- **`subject_ref_id` and `medium_id` are `null` by design** — server-injected, in
  `VOLATILE_TOP_LEVEL_KEYS`. No GSEB subject record is confirmed.
- **`english_plan_id` / `english_chapter_id` are `null`** — a Gujarati chapter has no English twin.
  Not a gap to be closed.
- **`ordering` is absent from the root by design** — it is Agent 14/15's to set at emit, so 31 of the
  32 contract root keys are written here. `topic_title` is set to the printed chapter name
  `શતરંગી ભારત`, mirroring `unit_title`/`chapter_name`; it is derived, not separately authored (no
  input agent supplies a distinct `topic_title` value for this reader's chapter-is-the-unit
  granularity, matching precedent in `output8/ch05`, `ch02`, `ch03`).
- **Genre routing remains a documented, unresolved tension — carried forward, not settled here.**
  `01_meta.json`'s `genre_confidence: "low"` for a mahitiprad_gadya-vs-samvad_nibandh call on this
  exact chapter is a **pipeline-level reference conflict** (between `mahitiprad_gadya.md`'s own
  "contested chapter" note, which is internally stale, and `explanation_unit_map.md`/
  `samvad_nibandh.md`'s near-miss table, which both currently resolve it here) rather than a defect in
  this chapter's authored content. This gate confirms the **structure correctly obeys the active
  profile** throughout (no `topic_category: "climax"`, no story-arc framing, cut by માહિતી-ખંડ never
  by speaker-turn) and does not re-litigate the diagnosis itself, per `qc_checklist.md`'s own
  instruction. If `_genre_index.md`'s roster status is later fixed toward `samvad_nibandh`, this whole
  cut would need re-review against that profile's Avoid list, not a patch. Owner if revisited:
  `01_ingestion_genre_diagnosis.md` → `02_structure.md` (cut) → `07_pitfalls.md`/`12_runtime_
  authoring.md` (re-check avoid-gates).
- **`05b_textbook_order.json` equals the logical traversal order exactly** — flagged above under E–G;
  repeated here because `phase2_contract.md` requires the `human_confirmation_required` flag to be
  raised at Agent 14/15, not silently dropped.
- **Media `generation_prompt`s carry no narrator-bar string** — flagged above under E–G as a design
  question for Agent 9's owner spec, not a contract violation.
- **Render provenance is single-rasterisation**, per the orchestrator's constraint (renders were not
  re-run). Agent 1's substitute cross-check — cropping and resampling the supplied PNGs 1.7×–3× with
  LANCZOS — caught and corrected one genuine transcription error ("ઊલ્ભો"→"ઊભો" in the intro box) and
  individually re-verified several other words (`તત્ત્વ`, `દૂરંદેશી`, `ટ્યૂબલાઈટ`, `સ્વિચ`,
  `કૌશિક શિવાસુબ્રહ્મણ્યમ્`). If a higher-dpi render is ever produced, these are the first places to
  re-check, alongside the idiom-count correction against the prior (7 idioms measured on the page vs.
  8 claimed in `std-8_inventory.md`) and blocks 10–11's generic, chapter-unconnected sentences.
- **Printed inconsistency deliberately preserved, not repaired**: the body text spells the idiom
  `માથાકૂટ`, while the printed રૂઢિપ્રયોગ box spells it `માથાફૂટ` — both transcribed exactly as their
  own location prints them (`01_meta.json`/`10_exercise_solutions.json` EX2's `teacher_note`). Any
  downstream QC that flags this as a transcription error is producing a false positive.

---


## LP2 validator

**Validation run: Phase 8 · POST to https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate**

Request: `/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output8/ch09/learning_plan_logical.json` as multipart field "file"

Response (HTTP 200):
```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati8_ch9_v1",
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

**Result: VALID** — `validation_errors` is empty. The plan structure is correct and ready for upload.
