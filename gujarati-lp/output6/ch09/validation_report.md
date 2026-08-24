# Validation Report — std-6 ch 9 ગરવી ગુજરાતનો ગરબો

સ્વરૂપ: માહિતીપ્રદ ગદ્ય (profile `mahitiprad_gadya.md`) (confidence: high)   explanation unit: એક માહિતી-ખંડ
Topics: 13   Objectives: 13   Images: 0/9   Exercises: 19/19 blocks (64/64 items answered)

Merged plan: `13_merged.json` — 31 root keys, 2 modules, 7 segments, 13 topics, 17 concepts, 9 media
nodes, 0 `2d_tool`.
Layers folded: `05_with_content.json` (base) · `12_authoring.json` · `09_media.json` ·
`16_publication.json` · `11_pages.json` · `01_meta.json`.
Re-merged after `16_publication.json` was rewritten at 03:26 — the 03:21 merge predated it and is
superseded.

---

## A–D (blocking)   **PASS**

### A — Diagnosis and lens
- સ્વરૂપ diagnosed off the rendered page (the PDF is image-only) and recorded with `genre_signals`
  and `genre_confidence: high`. The evidence is structural, not asserted: 29 printed prose
  paragraphs, **zero** કડી / દુહો / પદ / ટેક in `structure_inventory` (all four counts are 0), and a
  fact-chain that survives the drop-the-frame test — ઉદ્ગમ → શક્તિપૂજા → ઘડો → શબ્દની સફર → પ્રતીક →
  ગરબો/ગરબીનો ભેદ → મંજીરાં → હીંચ → ટિપ્પણી.
- Explanation unit matches the સ્વરૂપ: **one માહિતી-ખંડ per topic**. `00_chapter_normalized.md`
  carries **13** `[[માહિતી-ખંડ: …]]` markers and the plan carries **13** topics — 1:1, none merged,
  none swallowed, none invented. Topic length runs one paragraph to seven, i.e. cut on the fact step
  and not on the paragraph or the page.
- The profile's own line "the same holds for std-6 ch 9's list of regional dances" was checked
  against the printed page and **the page won**: p. 57 prints no one-word litany — મંજીરાં, હીંચ and
  ટિપ્પણી each get a developed fact-block, and each carries its own marker. Agent 4 confirmed this
  and recorded it as a deliberate choice; it is reported here, not treated as a miscut.
- Speaker turns did not become the cut: 38 quoted turns against 13 topics, and every boundary also
  closes a fact step.
- Apparatus did not become a reading scene: `[[શીર્ષક-પટ્ટી]]`, `[[લેખક-નામ]]` (`- સંકલિત`),
  `[[પ્રવેશપેટી — વાદળી ખાનું]]`, `[[ચિત્ર: …]]`, `[[શબ્દાર્થ]]` and the chapter-final green
  અલ્પવિરામ-અવતરણચિહ્ન box are all outside the topic cut. The QR badge's Latin code was never
  transcribed.
- `guiding_question` is derived from this chapter and could fit no other:
  *ગરબો શબ્દ ક્યાંથી આવ્યો, ગરબા ને ગરબીમાં શો ફેર, ને ગુજરાતના જુદા જુદા પ્રદેશો પોતાનું નૃત્ય કઈ રીતે
  ઊભું કરે છે ?* Reading the thirteen explanations in order answers it.

### B — Verbatim and structure
- All 13 `original_chunk`s non-empty. **Every chunk was located character-for-character inside
  `00_chapter_normalized.md`**, and I re-rendered the source PDF myself (`pdftoppm -png -r 150`) and
  read printed pages **55, 56 and 57** line by line against the chunks: they match, including
  `હિલોળે`, `રળિયામણી`, `ઘેલું`, `જમી - પરવારીને` (spaces round the dash), `ઉદ્ગમ`, `પ્રકૃતિમાતાની ગોદ`,
  `છિદ્રો પાડેલો`, `ગરબો કોરાવ્યો`, `ગર્ભદીપ → ગર્ભો → ગરબો`, `માંડવડી`, `નરઘાં`, `પઢારો`, `નળકાંઠો`,
  `કાંસીજોડ`, `બગલિયું`, `શ્રમહારી`, `કોઠાસૂઝ`, `ગડબો`, `સિંધુડો`, `પ્રભાતિયા`, `અલ્યા`, `રે લોલ`.
- The printed inconsistencies were kept, not repaired: the opening-quote-inside-quote of
  `''અરે, વાહ ! પપ્પા તો આ સાંભળીને રાજીના રેડ થઈ ગયા.''`, પપ્પાનું unquoted reply after it, the
  મંજીરાં paragraph that runs from an unopened quote to a closing `!''`, `ટિપ્પણી નૃત્ય` /
  `ટિપ્પણીનૃત્ય` and `હલકા કંઠે` / `હલકથી` both standing, and `'ગુજરાતનાં લોકનૃત્યો'` ending with no
  full stop.
- Script: base script Gujarati (U+0A80–0AFF) throughout. **Zero Devanagari characters and zero `।`**
  anywhere in `13_merged.json`. The only Roman characters in the file are ids and provenance
  (`M1.S1.T1`, `O1`, `L1`, `IMG1`, `gseb`, the media `generation_prompt`/`negative_prompt`, the local
  `textbook_url`) — **no Roman character appears in any authored display field**. The English
  loanwords the chapter deliberately prints (`ડાન્સ`, `આર્ટિકલ`, `પોઇન્ટ`, `વન મિનિટ`, `રેકોર્ડ`,
  `વાઉ`, `સો વંડરફૂલ`, `થેન્ક યુ વેરી મચ`, `લાઇવ`, `થેન્ક્સ અ લોટ`) stand in **Gujarati script** as
  printed, so no script whitelist exemption was even needed here.
- `word_count.original` recomputed from every chunk and matches all thirteen stated values
  (119/120/133/53/12/45/58/103/67/70/97/120/128).
- Marker balance: 13 `[[માહિતી-ખંડ]]` = 13 topics. **19 `[[સ્વાધ્યાય: …]]` blocks, 0 of them topics** —
  no સ્વાધ્યાય text appears inside any `original_chunk`.
- Ids consecutive by traversal position: M1–M2, S1–S7, T1–T13, and concepts **chapter-continuous**
  C1–C17 (`M1.S1.T1.C1`, `M1.S1.T1.C2`, `M1.S1.T2.C3` … `M2.S7.T13.C17`).

### C — The teaching block
- All 13 topics carry a non-empty `explanation` **and** `real_life_example`.
- Bands hold with no trimming needed: `explanation` **60–77** words, `real_life_example` **58–69**
  words (band 55–90); all 13 `objective_text` **17–21** words (band 12–30). ⚠ Bands remain
  provisional until VERIFY-4; they were applied as written and never widened.
- Glossing is at the point of first use and in Gujarati, at the low L2 bar the pack asks for —
  `હિલોળે ચડવું`, `ઘેલું`, `અખબાર`, `રાજીના રેડ`, `ઉદ્ગમ`, `પારણું`, `પ્રાચીન`, `છિદ્ર`, `કોરવું`,
  `પ્રચલિત`, `મૂળ શબ્દ`, `બ્રહ્માંડ`, `પ્રતીક`, `ફેર`, `માંડવડી`, `નરઘાં`, `પ્રદેશ/પ્રાદેશિક`,
  `મુખપૃષ્ઠ`, `કુશળતાપૂર્વક`, `રાસ`, `ગાગર`, `હીંચ`, `પંથક`, `શ્રમહારી`, `કોઠાસૂઝ`, `ધરબવું`, `અલ્યા`.
  Two glosses do the L2 job of blocking a wrong guess outright: `'કોરું' એટલે ખાલી, પણ એ અર્થ અહીં નથી`
  and `હીંચકે ઝૂલવાની વાત અહીં નથી`.
- Every `real_life_example` is **one** Gujarat anchor inside a std-6 child's reach and ends by handing
  the thinking over: પિતરાઈને નિશાળ બતાવવી · પતરાના છાપરે પહેલું ઝાપટું · રિસેસનો ડબ્બો · ઉનાળાનું નવું
  માટલું · ઘરનું ટૂંકું નામ · દિવાળીનું કોડિયું · મેદાનની લંગડી ને ખો-ખો · એસ.ટી. સ્ટૅન્ડનું પાટિયું ·
  શેરીની રમતનો પોતાનો નિયમ · કૂવેથી ભરેલી ડોલ · વર્ગના બાંકડા · રસોડાની થાળી-વેલણ · દાદીની અધૂરી વારતા.
  Thirteen different domains, none repeated, none needing its own glossary, none adult, none abstract.
- Craft ceiling held: **no** અલંકાર, છંદ, સમાસ, સંધિ, પ્રાસ-as-a-label or સાહિત્યપ્રકાર term appears
  anywhere in the authored text. The chapter's figurative lines (`સંસ્કૃતિનું પારણું બંધાયું`,
  `ઘડો એ બ્રહ્માંડની કલ્પના છે`, `કેસરિયો રંગ તને લાગ્યો અલ્યા, ગરબા !`) are re-said in plain Gujarati
  instead of being labelled.

### D — સ્વરૂપ essence
- **All 32 `severity: "hard"` items in `07_pitfalls.json` verified addressed**, string by string.
  The generic-substitute ban holds — `પઢાર`, `ભાલ`, `નળકાંઠો`, `કાઠિયાવાડ`, `સૌરાષ્ટ્ર`,
  `ચોરવાડ પંથક`, `અંબેચોક`, `અમેરિકા`, `શિકાગો` all travel in their printed forms and **no** field
  carries `આદિવાસી`, `ગામડાના લોકો`, `એ લોકો`, `ત્યાંની પ્રજા`, `પછાત`, `અભણ`, `જંગલી`, `ગરીબ` or
  `મજૂર` as a substitute. (The one string match on `એ લોકો` is a media `teaching_notes` line
  instructing the teacher **not** to say it — the rule being obeyed, not broken.)
- Nothing was imported from outside the page: no `સિંધુ` / `હડપ્પા` / `આદિમાનવ` in the ઉદ્ગમ topic;
  no `સંસ્કૃત` / `પ્રાકૃત` / `અપભ્રંશ` / `વ્યુત્પત્તિ` in the શબ્દયાત્રા topic; no `સૂર્યમાળા` /
  `ગ્રહો` / `વૈજ્ઞાનિક` correction of the બ્રહ્માંડ કલ્પના; no `સિમેન્ટ` / `કૉંક્રીટ` in the ટિપ્પણી
  topic; no `હવે થતું નથી` / `લુપ્ત` / `જૂનું નૃત્ય` moving a living dance into the past.
- મમ્મીની printed qualification `કોઈ વાર પુરુષો એમાં જોડાય એવું બને` travels with every statement of
  who sings ગરબો, and no field supplies a reason the chapter does not give.
- **No બોધ, no ઉપદેશ, no poster line.** No field closes on `…જોઈએ`, `આપણે પણ…`, `આ પાઠ શીખવે છે…`,
  `સંસ્કૃતિ જાળવવી` or a culture-preservation sentence. The closing topic ends on પપ્પાનું printed
  વચન and the sung line, exactly as the profile requires.
- The chapter is prose and std 6, so **`figures_of_speech: []` on all 13 topics and
  `rhyme_scheme: null` throughout** — the correct, complete answer, and the verbatim-quote check is
  therefore vacuously satisfied (there is no device entry to fail it).
- One sensitivity item is `severity: "hard"` — M2.S5.T9, keep the પઢાર community's own name.
  Verified: the name appears in `topic_name`, `explanation`, `summary`, `detailed_summary`,
  `concept_bullets`, both recall answers and the media node, and the dance is described as
  `આ નૃત્ય એમનું પોતાનું છે` — theirs, not watched from outside. `areas[]` across all seven
  sensitivity entries draw only on the seven fixed labels (ધર્મ, સમુદાય, ક્ષેત્ર, જાતિ-ભૂમિકા).
- Judgement call recorded: the T3 gloss `શક્તિ એટલે અહીં માતાજી` was checked against the ban on deity
  names the chapter does not print. **`માતાજી` is printed in this chapter** (સ્વાધ્યાય block 7's
  ફકરો: `મંદિરમાં/મંદિર પર માતાજી હોય. માતાજીની…`), and the chapter-level pitfall note names
  "a printed line of this chapter — its સ્વાધ્યાય included" as the ceiling. It passes, and the
  reasoning is recorded here rather than left implicit.

---

## E–G (reported)

**E — સ્વાધ્યાય and risk.** All **19** printed blocks inventoried by Agent 1 appear in
`10_exercise_solutions.json`; `blocks_found` = 19 = inventory length, and `blocks_found` matches the
inventory's `verbatim_heading` strings **exactly, in printed order** — no fuzzy allowance was needed.
`unanswered: []`; 64 answer entries, none empty; every `covered_by_topics` id resolves to a real
topic; 21 entries are flagged `is_model_answer` (વાતચીત, પ્રવૃત્તિ, જૂથકાર્ય, ચિત્ર-વર્ણન, અનુવાદ and the
teacher-addressed block 16), answered with teaching values rather than skipped. Item counts follow
the inventory except three documented cases: વાતચીત carries 6 entries for 5 numbered items plus the
printed un-numbered bullet; the nine-blank ખાલી જગ્યા ફકરો and the seventeen-choice છેકી નાખો ફકરો are
each one entry because the book prints each as a single continuous paragraph, with the per-item values
carried in `values_filled_for_teaching`.

**F — Shape and media.** All 12 `json_contract.md` invariants hold. Objectives registry: 13 unique
`objective_id`s, every `home_topic_id` and every `anchor[]` id resolves, `strand_to_objective_map`
covers all 13 `legacy_id`s, every topic's `objective_ids` resolve, and every inline
`learning_objectives[]` mirror matches its root `objective_text` **character for character** and
carries `image_examples: []`. `publication_id` is non-null. `topic_type` is the authored `CONCEPT`
on all 13 (correct at this stage; Agent 14 maps it to `instructional`). No `.SR{n}` anywhere: the 36
topic recalls are `{topic_id}.RQ{n}` with `legacy_id` `{topic_id}.TR{n}`, and there are no segment
recalls to get wrong. All 9 media ids match `MEDIA_ID_RE` and are concept-scoped, with
`concept_id` = `home_concept_id` = the id prefix. Three-tier summaries strictly increase on all 13
topics. **No digits — Latin or Gujarati — in any display text**; numerals survive only in ids,
`word_count` and `textbook_pages`. Root keys: 31 of the contract's 32; `ordering` is deliberately
left for Agent 14/15 to set.

**G — the seven usual mistakes.** None present. (1) Not સાર+બોધ+પ્રશ્નોત્તર: each explanation teaches
its fact-cluster and lands on a Gujarat anchor. (2)–(4) do not arise — no દુહા, no પદ, no verse to
merge, split or silently correct; the one quoted ગરબા line stays inside its prose topic and keeps
`અલ્યા` and `રે લોલ`. (5) No અલંકાર named because a field existed — `[]` throughout. (6) No adult,
foreign or over-pitched anchor. (7) No સ્વાધ્યાય block cut as a topic.

**Voice note (reported, not blocking).** The std-6 register table caps `explanation` sentences at
roughly 10–12 words. Eleven of the thirteen explanations carry at least one sentence longer than 14
words (longest 26, in M2.S5.T9's opening three-part gloss chain). The blocking C band is the 55–90
word count, which every field passes; the sentence cap is a reported calibration note for A12 and is
itself research-derived rather than measured against GSEB prose (VERIFY-4).

---

## Media
`reuse_report`: **scenes 9, authored 9, reused 0, rejected []** — and 9 is exactly the number of
topics whose `available_content_types` carry `"image"` (T1, T2, T4, T6, T7, T9, T10, T11, T12). The
four text-only topics (T3, T5, T8, T13) carry no media and declare none. Every media node has
`image_url: ""` **and** a non-empty, self-contained `generation_prompt`; no `[reused frame: …]` stamp
and no fabricated URL exists in this pack. Every `negative_prompt` carries `Devanagari script labels`
along with the standing bans. One image per scene, never two. `2d_tool` is **null** for the chapter
and on every topic — zero, which is inside the ≤1 limit.

## Gaps
- **`textbook_url` is a local path** — `../Textbooks-pdf/std-6/ch-09-garvi-gujaratno-garbo.pdf`. The
  GSEB readers have no hosted URL. Recorded by Agent 11 and carried through unchanged. (A11)
- **`publication_id: 1` is provisional.** `1` is CBSE's publication row, carried across the pack; the
  GSEB row must be looked up in the education DB (**VERIFY-2**) before the first Phase 8 upload. The
  contract forbids `null`, so `1` is written as a placeholder that is knowingly wrong. (A1 /
  VERIFY-2)
- **`chapter_master_id: null`** — mandatory for upload, not discoverable from the LP2 API, fetched
  per chapter from the education DB (**VERIFY-2**). Never derived, never invented. (VERIFY-2)
- **`chapter_id` board/medium segments provisional** (`gseb_eng_gujarati6_ch9`, **VERIFY-1**). A wrong
  medium uploads clean and mis-files the plan.
- **Root `genre` carries the Gujarati name, not the roster slug.** This plan writes
  `"genre": "માહિતીપ્રદ ગદ્ય"`, while `phase2_contract.md` shows a slug and the active profile is
  `mahitiprad_gadya.md`. The pack is split on this — ch01/ch07 write `urmikavya_geet`, ch08 writes
  `patra_pravas`, ch04 writes `mixed`, while ch02/ch03/ch05/ch06/ch09 write Gujarati names. Reported,
  not blocking; it needs one decision applied across std 6. (A1)
- **Two whitespace details Agent 1's own notes record but the file does not carry.**
  `extraction_notes[]` says the printed double spaces in `સ્ત્રીઓનું શ્રમહારી નૃત્ય છે  એ તો !` and
  `મળે છે.  આ એકમમાં` were kept; `00_chapter_normalized.md` and therefore the merged chunks carry
  single spaces at both points. The render shows the wider gap is justification spacing, not content,
  so this is reported rather than raised as a verbatim failure — but the note and the file disagree
  and should be reconciled. (A1)
- **Two exercise items reported `unmapped`, correctly.** EX43 `પ્રીત` and EX49 `અંતર` in the
  સમાનાર્થી અક્ષર-કોષ્ટક appear nowhere in the chapter's reading text — the book put out-of-lesson
  words in its own grid. No topic mapping was invented to close the report. (A10 — no action)
- **Uneven topic length, reported by Agent 4, not blocking.** M1.S3.T5 is a 12-word single printed
  line while M2.S7.T13 runs 128 words over seven paragraphs. The cut is right — the word-journey is
  its own fact step and carries its own marker — and Agent 12 filled T5's band without importing an
  outside fact.
- **One pre-topic hook was moved across a marker boundary**, on Agent 4's explicit approval: printed
  p. 56's `''સાચે જ આજે તો ઘણું બધું જાણવા મળ્યું… પ્રાદેશિક લોકનૃત્યો પણ હશે જ ને ?''` sits under the
  ગરબો/ગરબી marker in `00_chapter_normalized.md` but raises the question T8 answers, so the whole
  paragraph travels into M2.S5.T8's `original_chunk`. The paragraph is unbroken and the marker counts
  are unaffected.
- **Transcription-verification scope, stated honestly.** Agent 1 could not produce two independent
  dpi renders and verified by enlarging crops of one render. I re-rendered the PDF at 150 dpi
  independently and read **printed pages 55, 56 and 57** — the whole reading text, i.e. every
  `original_chunk` — against the chunks line by line; they match. Printed pages 58–62 (the શબ્દાર્થ
  box, the 19 સ્વાધ્યાય blocks and the closing વ્યાકરણ box) were **not** re-verified by me beyond
  block counts and headings; that text feeds `10_exercise_solutions.json`, not any `original_chunk`.
- **Spec tension, resolved and recorded.** Agent 13's brief says `publication_chunk` is
  "byte-identical to `original_chunk`", while Agent 16's own spec defines it as the topic's whole
  block for a reader — verbatim chunk **inside**, surrounding prose rewritten. This plan follows
  Agent 16: in all 13 topics the `original_chunk` is present at index 0 of `publication_chunk`,
  **byte-for-byte**, followed by the publication prose and the de-vocativised anchor. The intent the
  Agent-13 line protects — the rewrite never touches the verbatim — is verified and holds; the two
  spec files should be reconciled in wording.
- **Publication rewrite is minimal and adds no meaning.** Eleven of thirteen `publication_text`
  values are identical to their `explanation` because those explanations carry no vocative and no
  direct instruction. The two that differ change exactly the imperative:
  `…મોટેથી બોલી જુઓ` → `…મોટેથી બોલવાથી ફેર સંભળાય છે` (T5) and `શબ્દને ટુકડે ટુકડે ખોલો :` →
  `શબ્દ ટુકડે ટુકડે ખૂલે છે :` (T11). All 18 `concept_publication` entries match
  `concepts[].content[]` by concept id **and** by index, one per `paragraph` block, none renumbered,
  reordered or dropped. No `બાળકો`, `જુઓ —` or `બોલો` survives.

## LP2 validator
Not run — filled in Phase 8. `POST /api/lp2/learning-plans/validate` must return zero
`validation_errors`; `publication_id` and `chapter_master_id` must carry their verified GSEB rows
(VERIFY-2) and `chapter_id` its confirmed board/medium segments (VERIFY-1) before that call.

---

**Verdict: A–D PASS.** No blocking failure; nothing routed to an owner. The E–G notes and the Gaps
above are reported, and the four provisional root values (`publication_id`, `chapter_master_id`,
`chapter_id` segments, the `genre` slug question) are open items for VERIFY-1/VERIFY-2 and A1 —
not defects in this chapter's teaching.

## LP2 validator

- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json
- Result: success, validation_errors: [] (Valid)
- Raw response: {"success":true,"action":"validated_only","plan_id":"gseb_eng_gujarati6_ch9_v1","validation_errors":[],"message":"Valid"}

## LP2 validator

- POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate → validation_errors: [] (none) — PASS
- Run: 2026-08-23 17:16 IST (validation only; no upload)
