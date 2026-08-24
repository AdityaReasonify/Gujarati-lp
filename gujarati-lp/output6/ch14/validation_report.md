# Validation Report — એક છોકરો રિસાણો (std 6, ch 14)

સ્વરૂપ: સંવાદ (`samvad_nibandh` પ્રમુખ + `natak_ekanki` સાથે લોડ) (confidence: high)   explanation unit: સંવાદનું એક પગલું — વાંધો, સ્વીકાર, પુરાવો કે સવાલ (વારો વચ્ચેથી કપાય નહીં) / one move of the argument
Topics: 5   Objectives: 5   Images: 0/5   Exercises: 15/15 blocks (52 entries, 0 unanswered, 5 unmapped)

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` +
`16_publication.json` + `11_pages.json` + `01_meta.json` → `13_merged.json`
(31 root keys; `ordering` deliberately left to Agent 14/15).

First pass on this chapter — no owner re-run preceded it. Every check below was run
mechanically against the merged bytes (~370 assertions over topics, concepts, objectives,
recall ids, media nodes, exercise entries and the transcription), not read by eye; the
five hard pitfall corrections and the one hard sensitivity item were asserted as strings
against the merged fields. **0 failures, 0 warnings.**

---

## A–D (blocking)   **PASS**

### A — Diagnosis and lens   PASS

- સ્વરૂપ diagnosed off the rendered page with all four signals recorded in `genre_signals`
  (structure / theme / exercises / purpose), `genre_confidence: "high"`. The blue પ્રવેશપેટી is
  quoted as **evidence** — `…પ્રસંગ અહીં સંવાદ સ્વરૂપે રજૂ થયો છે` — and not taken as the verdict.
- The routing is the one `profiles/genres/natak_ekanki.md` prints for this exact chapter
  (near-miss table, row **std-6 ch-14 એક છોકરો રિસાણો**): four labelled speakers, **zero**
  bracketed રંગસૂચના, no `પાત્રો` box, no `પ્રવેશ`/`અંક`, no `પડદો` → dominant
  `samvad_nibandh.md`, `natak_ekanki.md` loaded alongside for the explanation unit and the
  directions-are-text gate. `samvad_nibandh`'s G6 label-position reroute gate is **waived by
  that printed exception** and correctly did not fire. Exercise block 12
  (`આ કૃતિને વર્ગમાં નાટક સ્વરૂપે રજૂ કરો.`) is a performance task and was correctly not read
  as evidence of form.
- Explanation unit matches the સ્વરૂપ: five topics = the five argument-moves the page makes,
  sitting 1:1 on Agent 1's five `[[સંવાદ: …]]` stretches. Re-derived here from the
  transcription: **83 turns split 12 + 17 + 21 + 23 + 10 = 83**, equal to
  `structure_inventory.dialogue_turns`; every line of every `original_chunk` begins with a
  printed speaker label, so **no boundary falls inside a speaker's turn**; the five spans occur
  in ascending printed order and are contiguous.
- `teaching_lens` is the profile's own — **તર્ક + દૃષ્ટિકોણ + જવાબદારી** (samvad_nibandh.md line 60).
- Apparatus did not become a reading scene: the blue પ્રવેશપેટી, the શબ્દાર્થ box (p. 97), the
  p. 100 ચિત્રવર્ણન illustration and all fifteen સ્વાધ્યાય blocks sit outside every
  `original_chunk`, asserted directly.
- `guiding_question` is derived from this chapter
  (`મનન કઈ વાત પર રિસાય છે, અને ઘરનાં કયાં કયાં પગલાં પછી એ પોતે જ પોતાનો રસ્તો કાઢે છે ?`) and the five
  explanations read in order do answer it: the trip arrives (T1) → the demand and its first
  refusal (T2) → the રીસ and the two different reasons (T3) → પપ્પાની સામી દરખાસ્ત (T4) →
  મમ્મીની છેલ્લી વાત and મનન's own decision (T5).
- No ટેક and no mixed-genre part in this chapter, so those roster rows do not apply.

### B — Verbatim and structure   PASS

- All 5 `original_chunk`s non-empty and pure Gujarati (U+0A80–0AFF): **0 Roman characters, 0
  Devanagari characters, 0 `।`/`॥`** anywhere in the chunks, and none in any authored display
  field of the merged plan either. This chapter prints no non-Gujarati island at all —
  `extraction_notes[]` says so explicitly, and the whitelist did not need to be invoked.
- **Every line of every `original_chunk` was found verbatim in `00_chapter_normalized.md`** (83
  string assertions, 83 hits). Nothing was reflowed, re-spaced or re-punctuated by the merge.
- Printed-as-is forms survive into the merged plan and are never "corrected": `ભાઈલુ` in T1
  against `ભઈલું` elsewhere, `મજ્જા` in T4, the spaced hyphens `હાથ - પગ` / `આજવા - નિમેટા`, the
  double spaces (`ભઈલું,  ખોટી જીદ`, `દીદીના  ટીચરને`), the spaced `?` and `!`, both `નહિ` and
  `નહીં`, `ચડ્યો` with `ડ`. The full stop is the chapter's પૂર્ણવિરામ throughout and no daṇḍa was
  introduced.
- **Marker counts:** `[[કડી]]` / `[[દુહો]]` / `[[પદ]]` / `[[ઘટના]]` = 0, matching
  `structure_inventory` (this is prose). `[[સંવાદ: …]]` = **5 = 5 topics**.
  `[[સ્વાધ્યાય: …]]` = **15 = 15 inventory entries, and none became a topic** — asserted, including
  the trap: the five-line rhyme `એક છોકરું  રિસાણું…` is printed inside exercise block 5 and appears
  in **no** `original_chunk`.
- Ids consecutive and every cross-reference resolves (see Contract below).

### C — The teaching block   PASS

- All 5 topics carry non-empty `explanation` **and** `real_life_example`.
- Word bands, recounted on the merged bytes: `explanation` **86 / 88 / 88 / 89 / 86**;
  `real_life_example` **68 / 68 / 71 / 70 / 72**; `objective_text` **23 / 24 / 20 / 21 / 21**.
  All inside 55–90 and 12–30. ⚠ Bands provisional until VERIFY-4 — none was widened.
- L2 calibration: every hard word is glossed at first use inside `explanation`
  (નોટિસ, ભાઈલુ/ભઈલું, સેર, રીસ, મનામણાં, વાડી, રજા, તારા), the sentence-final `ને ?` is glossed
  exactly once at first appearance, and the English loanwords printed in Gujarati script are kept
  as printed — which matters, because exercise block 8 runs on exactly those words.
- `real_life_example` is Indian, concrete, single and inside std-6 reach in all five — ઘરે દોડીને
  ખબર આપવી, ગામનો મેળો ને ચકડોળ, થાળી આઘી ઠેલવી ને દાદીનું ઢોકળું, મામાના ગામની વાડી ને આંબો,
  ફળિયામાં દોરડા-કૂદનો વારો. Four of the five close on a question to the child.
- Craft ceiling held: no અલંકાર, છંદ, સમાસ or સાહિત્યપ્રકાર is named anywhere, and no field asks the
  child to name the form.

### D — સ્વરૂપ essence   PASS

All hard items from `07_pitfalls.json` (5 topics) and `08_sensitivity.json` (1 chapter item) hold.

- **G1 — both voices.** Asserted as strings: every **printed speaker label** holding a turn in a
  topic occurs in that topic's `explanation` — T1 ઝલક + વનિતાબેન; T2 all four; T3 મનન + વનિતાબેન +
  ઝલક; T4 મહેશભાઈ + મનન; T5 all four. `મમ્મી`/`પપ્પા` alone were not accepted, per the chapter's own
  decidability note.
- **G2 / no બોધ.** `જોઈએ`, `બોધ`, `સંદેશ`, `શિખામણ`, `ઉપદેશ` occur in **zero** teaching fields
  (explanation, example, three summaries, every recall answer) across all five topics. The
  ready-made moral the સ્વાધ્યાય prints next door
  (`પ્રવાસમાં જતાં પહેલાં પૂરતી તૈયારી કરી લેવી જોઈએ.`) was not imported.
- **G3 / no flattened opponent.** T3 keeps the two refusals **separate and different** — ઝલક's
  (અજાણી જગ્યાએ આખો દિવસ સાચવવો પડે) and વનિતાબેન's (શિક્ષકો બહારનાં બાળકોને લઈ જઈ ન શકે) — in
  `explanation`, `detailed_summary` and concept C5. T5 does not retrospectively re-describe મનન.
- **No supplied narrator / nothing offstage invented.** No interior state is attributed to any
  speaker; the account stops exactly where the page stops, at
  `જોયું ? મારો દીકરો કેટલો સમજદાર છે !`.
- **The five misconception corrections are each delivered in the field 07 names** — T1 the
  ભાઈલુ/ભઈલું one-person gloss; T2 `તારાથી ના અવાય` restated as `તું આવી ન શકે` with both refusers
  named; T3 રીસ and મનામણાં glossed as a pair with the two lines set side by side; T4 `રજા` glossed
  as the day school is closed; T5 `તારા` glossed as stars against `તારા પપ્પા`.
- **08 hard સુરક્ષા item (M2.S3.T4) — held.** The adult stays present wherever tree-climbing and
  the open tank appear: `explanation` ends on `હું તારી સાથે જ હોવાનો ને !`, concept C6 says
  outright that both happen પપ્પાની હાજરીમાં, RQ3 asks about that very line, and
  `real_life_example` is a supervised outing with મામા standing under the branch. The T4 image
  prompt shows only the indoor swing-seat conversation — it depicts neither hazard. `areas[]`
  is `["સુરક્ષા"]`, one of the seven fixed labels.
- `figures_of_speech` is `[]` on all five topics and `rhyme_scheme` / `overall_rhyme_scheme` are
  `null` — the correct empty answers for ગદ્ય at std 6, not gaps. Nothing to check verbatim,
  and nothing was invented to fill the field.

---

## E–G (reported)

**E — સ્વાધ્યાય and risk.** All **15** inventoried blocks answered, **52** entries, `unanswered: []`.
Item counts match the inventory block for block (7·1·5·8·1·6·5·1·2·6·2·1·5·1·1). Skills tagged
(reading comprehension 24, writing 10, speaking 9, grammar 6, vocabulary 3); **25** entries are
marked `is_model_answer` — every personal-opinion, પ્રવૃત્તિ, જૂથકાર્ય and teacher-addressed item is
answered as a model answer rather than skipped, including block 11 (`…રમાડવી.`, addressed to the
teacher) and blocks 12/14 (class activities). Three printed grids are filled with teaching values.
Every `covered_by_topics` id resolves to a real topic. **5 entries are reported `unmapped`** (below)
and no mapping was invented to close them. Roman script appears in exactly the two places the
whitelist allows — the અનુવાદ block's model answers (EX46–EX50, medium of instruction, marked in
`teacher_note`) and the English-loanword block EX34, whose printed task is to list those very words.
No Devanagari anywhere in the exercise pack.

**F — Shape and media.** The 12 `json_contract.md` invariants hold; see Contract below. Provisional
values carried, not resolved: `chapter_id` board/medium segments (VERIFY-1), `publication_id`
(VERIFY-2), the word bands (VERIFY-4).

**G — the seven usual mistakes.** None present. (1) The plan teaches the સંવાદ's moves, not
સાર+બોધ+પ્રશ્નોત્તર. (2)/(3) do not apply — no verse in this chapter. (4) No poetic licence was
silently corrected (`ભાઈલુ`, `મજ્જા` intact). (5) No અલંકાર named. (6) All five anchors are std-6
Indian ones. (7) No સ્વાધ્યાય was cut as a teaching topic and the exercise deliverable is full.

### Contract invariants

| # | Invariant | Result |
|---|---|---|
| 1 | `phase: 2`, `plan_id = {chapter_id}_v{version}`, `chapter_id = gseb_eng_gujarati6_ch14` | PASS (board/medium provisional, VERIFY-1) |
| 2 | Gujarati-script `original_chunk`, no Roman / Devanagari | PASS |
| 3 | ≥1 concept per topic, valid `concept_id`, resolving `objective_id`, non-empty `content[]` | PASS (8 concepts) |
| 4 | Root `objectives[]` complete and consistent; `strand_to_objective_map` covers L1–L5 | PASS |
| 5 | Inline `learning_objectives[]` mirrors match the registry character for character | PASS |
| 6 | `MEDIA_ID_RE` concept-scoped; recalls `RQ{n}` + `TR{n}`; **no `.SR{n}` anywhere** | PASS (15 recalls, 5 media) |
| 7 | No સ્વાધ્યાય block is a topic; every inventoried block answered | PASS (15/15) |
| 8 | Three-tier summaries strictly increase | PASS on all 5 topics |
| 9 | No numbers in display text | PASS — 0 digits (Latin or Gujarati) in any name, explanation, example, summary, bullet, key term, concept text, recall prompt or answer |
| 10 | Media — one image per reading scene, ≤1 `2d_tool`, `image_url: ""` + real prompt | PASS |
| 11 | `figures_of_speech` lines verbatim in the chunk | PASS (vacuously — all `[]`) |
| 12 | Every reference survives renumbering | Verified against the current ids; re-assert after Agent 14 |

Also asserted: id grammar M1–M2 / S1–S4 (chapter-continuous, never restarting under M2) /
T1–T5 / **C1–C8 chapter-continuous**; `topic_type` inside the authored enum (`STORY_TELLING` ×5 →
`instructional` at Agent 14's emit); `bloom_level` Capitalised in `objectives[]` and lowercase in
`recall_questions[]`; `publication_id` non-null; 31 root keys with no working field carried
through (`source_span`, `structure_notes`, `provenance_05`, `genre_signals`, `tier`,
`reuse_report`, pitfall notes and coverage report all absent from `13_merged.json`).

### Publication

Every topic has `publication_text`. Diffed against `explanation` character by character: the
**only** difference on all five topics is the deleted vocative `બાળકો, જુઓ — ` — no fact, gloss or
reading was added or dropped. `original_chunk` sits **verbatim and unbroken inside**
`publication_chunk` on all five (asserted as an exact substring; the surrounding prose is the
publication-facing frame Agent 16's spec calls for). `concept_publication` matches
`concepts[].content[]` **by index and by count** — 10 entries for the 10 `paragraph` blocks, none
renumbered, reordered or dropped. One concept block (M2.S3.T4.C6 index 2) additionally
de-instructs `ધ્યાનમાં રાખવા જેવી છે` → `ધ્યાન ખેંચે એવી છે`, which is the rewrite doing its job.
No vocative or classroom instruction survives anywhere in publication text. (The string `બાળકો`
does occur inside two publication blocks, but as the chapter's own noun in
`શિક્ષકો બહારનાં બાળકોને લઈ જઈ ન શકે` — content, not address.)

## Media

`reuse_report`: **scenes 5, authored 5, reused 0, rejected []** — and 5 is exactly the number of
topics carrying `"image"` in `available_content_types`. Every node has `image_url: ""` and a real,
self-contained `generation_prompt` (1296–1670 chars), because **no Gujarati frame pool exists**;
no `[reused frame: …]` stamp and no fabricated URL anywhere. Every `negative_prompt` carries the
full minimum set including **`Devanagari script labels`**, plus this chapter's own guards
(speech bubbles, comic panel layout, theatre stage with curtain, motivational poster layout).
Each prompt is self-contained — no "previous image", no "same character as before", no chapter
name — and each names the **exact** Gujarati narrator-bar string; all five strings were checked
against the transcription and are printed chapter lines
(`આજે સ્કૂલમાં નોટિસ આવી હતી`, `મારે પણ દીદી સાથે જવું છે`, `મારે કોઈની વાત સાંભળવી જ નથી ને`,
`આપણે કરસનકાકાની વાડીએ જઈએ તો કેવું`, `મને દીદી તો જોઈએ`). `2d_tool` is `null` on every topic and at
chapter level — 0 tools, within the ≤1 rule.

The book's own two reading-scene illustrations (p. 93 inside T2, p. 95 inside T4) are recorded as
printed matter, not planned as media; the p. 100 beach illustration belongs to the final
ચિત્રવર્ણન exercise.

## Gaps

Honest absences, all reported and none closed by invention:

1. **`textbook_url` is a local path** — `../Textbooks-pdf/std-6/ch-14-ek-chhokro-risano.pdf`. The
   GSEB readers have no hosted URL (Agent 11's own gap, fail-soft). `textbook_pages: "92–100"`,
   confidence **high**, read off the folios on page-1 and page-9 renders.
2. **`chapter_master_id` is `null`.** Required for upload and **not discoverable from the LP2
   API** — it must be fetched from the education DB into
   `upload_reference/chapter_master_map.json` (VERIFY-2). Not derived, not invented.
3. **`publication_id` is written as `1` and is provisional.** The contract rejects `null`, but `1`
   is CBSE's publication row and does **not** transfer; the GSEB row must be looked up before the
   first Phase 8 upload (VERIFY-2).
4. **`chapter_id` / `plan_id` board and medium segments are provisional (VERIFY-1).** A wrong
   medium slot uploads clean and mis-files the plan.
5. **Root `genre` carries the roster slug `samvad_nibandh`, not `01_meta.json`'s Gujarati label
   `સંવાદ`.** `phase2_contract.md` requires the slug; Agent 4 recorded the same disagreement as
   non-blocking and named `02_structure.json` as the file to carry forward. Consistent with
   ch01/ch08/ch10/ch11/ch12 in this pack — but ch03, the other સંવાદ chapter, shipped the Gujarati
   word, so **the pack is internally inconsistent on this field** and A1/A14 should settle it once.
6. **5 exercise entries are `unmapped`** — EX9, EX11, EX12 (three જોડકાં halves about trip
   preparation, trip troubles and 'સ્ટેચ્યૂ ઑફ યુનિટી', none of which the chapter mentions), EX43
   (the kitchen-vocabulary minute game — the chapter has no kitchen scene) and EX52 (the p. 100
   ચિત્રવર્ણન illustration). The book itself printed out-of-chapter material in the સ્વાધ્યાય; no
   topic was manufactured and no mapping invented.
7. **`key_terms` gaps, reported by Agent 12, owner Agent 5.** Four glosses that
   `07_pitfalls.json` asks to be placed in `key_terms` are not there —
   `ભઈલું` (T1), the paired `રીસ`/`મનામણાં` (T3), `રજા` (T4), `તારા` (T5). All four **are** delivered
   inline in `explanation` at first use and carried in `shabdarth` and `concept_bullets`, so the
   hard correction holds; T4's list is already at the six-entry cap. Non-blocking; Agent 5 may
   swap one entry per list.
8. **Agent 4's non-blocking notes travel here:** the profile prior reads this chapter as three
   beats where the cut is five (finer, and marker-aligned — the right answer); topic length is
   uneven (T4 23 turns, T3 21, against T5's 10), held as single moves per the profile;
   `topic_type: STORY_TELLING` on an argument-move is the nearest authored value and maps to
   `instructional` regardless.
9. **Two corpus-prior disagreements, both resolved in favour of the page:**
   `reference/corpus/std-6_inventory.md` records 11 numbered સ્વાધ્યાય blocks (the render prints 14
   numbered + 1 unnumbered = 15), and places the family illustration at p. 95 (the render shows it
   at p. 93, with a different illustration at p. 95). The stale prior should be corrected.
10. **Explanations sit tight against the ceiling** — 86–89 words against a band of 55–90, with the
    opening `બાળકો, જુઓ — ` costing three of them, and that same formula opens all five. Inside the
    band, so not a block; worth a trim if VERIFY-4 narrows the band.
11. **Folio markers stop at p. 97** in `00_chapter_normalized.md`; the સ્વાધ્યાય pages 98–100 carry
    no `[[પૃષ્ઠ n]]` line. Provenance detail only — the exercise blocks themselves are all
    transcribed and inventoried.
12. **`05b_textbook_order.json` records `equals_logical_order: true`.** Per
    `phase2_contract.md` §Ordering, Agents 14/15 must therefore raise
    `{"human_confirmation_required": true, "reason": "textbook order is identical to logical order"}`
    in the run report rather than emitting a re-sequenced second plan.

## LP2 validator

Not run — filled in Phase 8. `POST /api/lp2/learning-plans/validate` must return zero
`validation_errors`; the four values it has historically rejected (`publication_id` null,
`.SR{n}` recalls, a genre string in `topic_type`, `.C1`-restarting concepts) are all asserted
clean above, but the server is the authority and gaps 2–4 must be resolved before that call.

---

**Verdict: A–D PASS. No blocker, no owner re-run required.** The run is complete as far as this
gate reaches; the four provisional values in Gaps 2–4 are verification work owed before upload,
not authoring defects.

## LP2 validator

- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json
- HTTP status: 200
- plan_id: gseb_eng_gujarati6_ch14_v1
- validation_errors: [] (none)
- message: Valid
