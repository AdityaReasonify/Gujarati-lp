# Validation Report — gseb_eng_gujarati7_ch2 (ત્રણ સવાલ)
સ્વરૂપ: varta / વાર્તા — ચાતુર્યકથા (confidence: high)   explanation unit: એક ઘટના
Topics: 9   Objectives: 9   Concepts: 11   Images: 0/9   Exercises: 13/13 blocks (39/39 items)

Two deliverables ship for this unit: the plan (`13_merged.json`) and the exercise pack
(`10_exercise_solutions.json`). Merge source: 05 base + 12 authoring + 09 media + 16 publication +
11 pages + 01 meta root fields. Working fields (pitfall notes, media scores, validation flags,
transcription markers, `source_lines_00_normalized`) were dropped; a key-by-key audit of the merged
file found no leakage.

## A–D (blocking)   **PASS**

Every hard item was checked mechanically against `13_merged.json` itself, not against the inputs.
Zero failures.

**A — diagnosis and lens.** સ્વરૂપ diagnosed off the rendered page from all four signals and
recorded with `genre_signals` + `genre_confidence: high`; the blue intro box names ચાતુર્યકથા and is
quoted as evidence, not as the verdict. Explanation unit `એક ઘટના` matches the વાર્તા line of the
roster. Apparatus stayed apparatus: the blue intro box, the શબ્દાર્થ box, the chapter-final
વિરામચિહ્નો grammar table and the રમૂજ box are all marked *ટૉપિક નથી* in the normalized file and none
became a reading scene. `guiding_question` is derived from this chapter's own દૂધ/દીવો choice.
ટેક does not arise — this is prose, `tek_occurrences: 0`. Not a mixed chapter: no verse anywhere.

**B — verbatim and structure.** All 9 `original_chunk` non-empty, Gujarati script (U+0A80–0AFF),
zero Roman and zero Devanagari characters outside brackets, zero `।` introduced. Marker arithmetic
in `00_chapter_normalized.md`: **7 `[[ઘટના]]` + 2 `[[સંવાદ]]` = 9 reading markers → 9 topics**, in
printed order. **13 `[[સ્વાધ્યાય]]` markers → 13 exercise-inventory blocks → 0 topics.** No
સ્વાધ્યાય block became a topic. The merge did not touch, reflow or re-space any chunk (asserted
byte-for-byte against `05_with_content.json` post-merge). Printed oddities survive as printed —
`રાજ્યસભા` used once against `રાજસભા` elsewhere, five printed double spaces, `આાગળ`/`આાવી` with the
doubled ા-માત્રા inside pink exercise text, block 9's fifth item printed without a full stop.
Header furniture stayed out: the number box, the pink title bar, the QR badge (its Latin code was
deliberately not transcribed), and the author line `- હરીશ નાયક`.

**C — the teaching block.** All 9 topics carry non-empty `explanation` and `real_life_example`.
Word counts inside `field_shape_rules.md` bands — see the counting note under E–G:
explanation 79–89, real_life_example 60–74, `objective_text` 12–30 across all nine objectives.
Anchors are Indian, concrete, single and inside std-7's reach: મીઠું in the cooking pot, the school
bell, the morning ST bus, the cricket trial. Craft is named as sound/structure only — no અલંકાર
canon and no છંદ, correct for std 7 and for a prose unit.

**D — સ્વરૂપ essence.** All 26 `severity: "hard"` avoid-checks in `07_pitfalls.json` verified:

- *Spoiling the turn* (varta avoid 4) — the climax is `M2.S3.T6`. Ran the forbidden-token list for
  each of T1–T5 across `explanation`, all three summaries, `concept_bullets`, `important_points`,
  `real_life_example` and every `recall_questions[].answer`: **0 hits** for દૂધ, માખણ, દીવો, પ્રકાશ,
  સિંહાસન, પ્રધાનજી, અદલાબદલી, કવિબાળા, દીકરી, 'ચારે દિશામાં', 'રાજસભામાં સામેલ'.
- *Tacked-on બોધ* (avoid 2) — no `આપણે પણ …`, no `આ વાર્તા આપણને શીખવે છે`, no `બોધ એ છે કે`.
  Three `જોઈએ` matches were inspected and are false positives: two are the story's own printed line
  `તો તે કાઢીને બતાવો જોઈએ` (which the pitfall check *requires* be kept, and which is verbatim inside
  T6's `original_chunk`), and one is the colloquial `પછી જોઈએ` = "then we'll see" inside a quoted
  line of T2's cricket anchor. Neither is a moral clause.
- *Judging a sympathetic character* (avoid 3) — 0 hits for અજ્ઞાની, મૂરખ, નબળા, ડરપોક, અહંકારી,
  અન્યાયી, સ્વાર્થી, અભણ, નિષ્ફળ, હાર્યા, બહાનું, ટોણો anywhere in the plan.
- *Summary-only teaching* (avoid 1) — each topic's required demonstration beat is present, not
  paraphrased away: `માખણ છે ખરું` + `કાઢીને બતાવો જોઈએ` + the વલોવવું chain at T6; `દીવો સળગાવી` +
  `કઈ દિશામાં` at T7; `પ્રધાનજીની જગાએ બેસશો` + `ચમકી ગયા` at T8; `આવડતા જ ન હતા` +
  `જ્ઞાનને ઉંમર સાથે લેવાદેવા નથી` at T9.
- `figures_of_speech: []` and `rhyme_scheme: null` on all 9 topics; `overall_rhyme_scheme: null` on
  all 3 modules. Correct — this is prose and not one line of verse is printed in the unit. Nothing
  was invented to fill the fields, so invariant 11 has nothing to catch.
- `08_sensitivity.json`: all four `areas[]` are the single fixed label `ધર્મ`; the three hard items
  (T6, T7, T8) are addressed. No field asserts that ભગવાન છે or નથી, none compares faiths, none
  tests the three દૃષ્ટાંતો against science, and the anchors deliberately avoid religious parallels
  (salt in the dal, the school bell, the bus timetable). No frame depicts a deity and every
  `negative_prompt` refuses halo, deity and devotional posture.

## Contract   **PASS** — 12/12 invariants

`phase: 2`; `plan_id = chapter_id + _v1`; `chapter_id = gseb_eng_gujarati7_ch2`. Registry
consistent — 9 unique `objective_id`, every `home_topic_id` and every `anchor[]` id resolves,
`strand_to_objective_map` covers L1–L9, every topic's `objective_ids` resolve. Inline
`learning_objectives[]` mirrors were built at merge and match the root `objective_text` **character
for character** (asserted), each carrying `image_examples: []`. Ids: topics T1–T9 consecutive,
segments in traversal position, concepts **chapter-continuous C1–C11** (T7→C8, T8→C9+C10, T9→C11 —
correct per phase2 rule 4, not a defect). All 9 media ids match `MEDIA_ID_RE` concept-scoped. All
recalls are `.RQ{n}` with `legacy_id` `.TR{n}` — **zero `.SR{n}`**; no segment-level recalls exist in
this chapter. `publication_id` non-null. Three-tier summaries strictly increase on all 9 topics.
Digits check on authored display text only: **0 digits** in any `topic_name`, `objective_text`,
`explanation`, `real_life_example`, summary, bullet, `important_points`, recall prompt/answer,
concept paragraph, concept list item, `publication_text` or `difficult_words[].example`.
`original_chunk`, `prompt_verbatim`, ids, `word_count` and `textbook_pages` keep their numerals as
provenance, correctly.

## Exercises   **PASS** — 13/13 blocks, 39/39 items, `unanswered: []`

`coverage_report.blocks_found` lists 13 entries matching `01_meta.json`'s `exercise_inventory`
verbatim and in printed order; `blocks_answered` matches entry for entry. Item counts
(6, 7, 4, 1, 1, 1, 6, 4, 5, 1, 1, 1, 1) sum to 39 = EX1–EX39. Every item has a real answer, a skill
tag and `is_model_answer` set; personal-opinion, પ્રવૃત્તિ, જૂથકાર્ય and teacher-assisted blocks are
answered as model answers rather than skipped. 28 of 39 items map to preparing topics.
`unmapped` carries 11 items and is **reported, not emptied** — see Gaps.

## Media   **PASS**

`reuse_report: {scenes: 9, reused: 0, authored: 9, rejected: []}`. `scenes` equals the 9 topics
carrying `"image"` in `available_content_types`; `authored == scenes`; `reused == 0`. Every node
carries `image_url: ""` **and** a non-empty, self-contained `generation_prompt` — no fabricated URL
and no `[reused frame: …]` stamp anywhere in the pack. Every `negative_prompt` carries
`Devanagari script labels`. One image per reading scene; `2d_tool: null` for the whole chapter
(≤1 satisfied). Each narrator bar was checked against its own topic's `original_chunk`: **all 9
strings are verbatim fragments**, Gujarati script, no digits, no transliteration.

## Publication   **PASS, with one spec conflict recorded below**

All 9 topics carry `publication_text`. `concept_publication` blocks land on `concepts[].content[]`
**by index**, one per `paragraph` block, in order, none renumbered, reordered or dropped — verified
per concept: the emitted index set equals the paragraph index set exactly for all 11 concepts, and
every `list` block correctly carries no `publication_text`. No vocative or classroom instruction
survived (`બાળકો`, `જુઓ —`, `બોલો`: 0 hits). Spot-checked for added meaning — the rewrites drop the
address and keep the gloss, and add no fact absent from the teaching block.

## E–G (reported)

- **Word-count method.** Bands are counted on *words*: tokens containing at least one letter.
  Gujarati typography spaces `:` `?` `!` `—` off as free-standing tokens, so a naive
  whitespace split inflates the count. Under the lexical count every field is inside band
  (explanation 79–89, example 60–74). Under a naive whitespace split three explanations would read
  93 (`M1.S2.T5`), 96 (`M2.S3.T6`) and 95 (`M2.S3.T7`). **No band was widened** — the three are
  reported here so the difference is visible rather than buried, and the margin at the ceiling is
  thin. If VERIFY-4 settles on naive tokenisation, those three want a trim from A12; nothing else in
  the chapter moves.
- **`topic_type` stays authored.** All 9 topics carry `STORY_TELLING` in `13_merged.json`, which is
  correct for an intermediate file per `phase2_contract.md` ("intermediate files (Agents 02–13)
  carry POEM | STORY_TELLING | CONCEPT | REVIEW"). **Agents 14/15 must map STORY_TELLING →
  `instructional` at emit.** The closed server enum is not yet present in this file by design.
- **`ordering`** is deliberately absent — Agent 14/15 sets it. Root key count is therefore 31 of the
  contract's 32.
- **Invariant 8 at segment and module level** has nothing to check: this chapter's segments and
  modules carry no summaries (only `segment_name` / `module_name`). Verified at topic level only.
- **Shape (F).** `key_terms` 5–6 per topic; `concept_bullets` and `important_points` 4 each;
  `recall_questions` 2–3 per topic, Bloom-laddered (remember/understand/analyze) with a real answer
  each; `difficult_words` 8/7/8 per module; `estimated_exchanges` a string ("3"–"5"). `bloom_level`
  Capitalised in `objectives[]` and lowercase in `recall_questions[]` — the accepted asymmetry, kept.
- **Non-Gujarati script whitelist.** One case in this chapter: the six answers of the
  `નીચેનાં વાક્યોનો પ્રથમ ભાષામાં અનુવાદ કરો.` block are written in English, the medium of
  instruction, and `teacher_note` says so explicitly. A script failure raised against these is a
  false positive. Checked the whole exercise pack outside that block: **zero** Roman and **zero**
  Devanagari characters in any `answer` or `explanation`.
- **G — the seven usual mistakes.** None present. Not a summary-plus-બોધ plan; no merging (prose, no
  દુહા); no split પદ; no silently corrected licence (`રાજ્યસભા`, the double spaces and the doubled
  માત્રા all stand as printed); no invented અલંકાર; no adult or non-Indian anchor; સ્વાધ્યાય was not
  cut as teaching topics and the exercise deliverable is complete.
- Agent 4's notes carried here: uneven topic lengths (M1.S2.T4 is one printed paragraph while
  M2.S3.T6 and M3.S4.T8 run ten and six printed lines) follow the printed beats — no beat was split
  or padded. Reported, never blocking.

## Gaps

1. **`publication_id` is a provisional placeholder — resolve before any upload.** The contract
   requires a non-null value, and no verified GSEB publication row exists. `13_merged.json` carries
   `1`, which `phase2_contract.md` names explicitly as **CBSE's row, not portable**. **VERIFY-2 must
   replace it from the education DB.** A wrong value here uploads clean and mis-files the plan.
2. **`chapter_master_id` is `null`** — mandatory for upload, not discoverable from the LP2 API,
   fetched per chapter from the education DB (VERIFY-2). It was left null rather than derived by
   arithmetic; the CBSE `355 − chapter` pattern does not transfer.
3. **Spec conflict on `publication_chunk`, recorded not resolved.**
   `13_assembly_validation.md` §Publication asks for `publication_chunk` **byte-identical to**
   `original_chunk`; `16_publication_authoring.md` §`publication_chunk` defines it as the whole
   block "with the verbatim `original_chunk` staying verbatim **inside it**". A16's output follows
   A16's own spec: on all 9 topics the `original_chunk` is present as a **byte-identical prefix**,
   followed by the publication prose (verified programmatically, all 9). The stated intent of the
   A13 check — *the rewrite never touches verbatim* — is therefore satisfied, so this is **not**
   raised as a D-level block. **A human should reconcile the two spec files** so the next chapter
   is not gated on the reading chosen here. Owner if it is decided the A13 wording governs:
   `16_publication_authoring.md`.
4. **`chapter_id` / `plan_id` board and medium segments are PROVISIONAL until VERIFY-1.** A wrong
   medium slot does not fail loudly — it uploads clean under the wrong DB column.
5. **`textbook_url` is a local path** (`../Textbooks-pdf/std-7/ch-02-tran-saval.pdf`) — the GSEB
   readers have no hosted URL. An honest gap, not a defect. `textbook_pages: "5–10"` is
   **high confidence**: read off the printed folios on renders p.1 and p.6 and cross-checked against
   the manifest (printed_start 5, pdf 18–23 → 10). No pagination gap.
6. **Root `genre` disagreement between inputs.** `01_meta.json` holds the Gujarati label `વાર્તા`;
   `02_structure.json` / `05_with_content.json` hold the roster slug `varta`. `phase2_contract.md`
   requires the slug in the emitted root, so **`13_merged.json` carries `varta`**. Owner to
   reconcile the label/slug split in the meta file: `01_ingestion_genre_diagnosis.md`. Reported, not
   blocking — `active_genre_profiles: ["varta.md"]` corroborates the slug.
7. **`topic_title` is not produced by any upstream agent.** It is a required root key. Set to the
   printed chapter title `ત્રણ સવાલ`, parallel to `unit_title` and consistent with
   `topic_number == unit_number == 2` for a single-unit chapter. Flagged so A1 can confirm rather
   than have it pass silently.
8. **`structure_inventory.ghatna: 7` is not a topic count.** Agent 1 counted only `[[ઘટના]]`
   markers; the two `[[સંવાદ]]` scenes are reading scenes too, giving 9. A counting-scope
   difference already documented by A1 and A4, repeated here so no downstream agent reads 7 as the
   topic count.
9. **11 exercise items reported `unmapped`, correctly.** EX20 (the proof-reading paragraph about
   અમેરિકા/અવકાશ), EX21–EX26 (the six અનુવાદ sentences, whose content is a ઋતુ passage unrelated to
   the story) and EX27–EX30 (the four tongue-twisters). Each carries a stated reason: the printed
   material has no connection to any scene, and nothing was missed by the cut. **No mapping was
   invented to empty this list.**
10. **`subject_ref_id` and `medium_id` are `null`** — server-injected, and no real GSEB subject
    record is confirmed. Correct per contract; do not hand-fill.
11. The double-render cross-check could not be run as a second `pdftoppm` pass (the run contract
    forbids re-rendering the shared renders). A1 recorded this; transcription fidelity rests on the
    single provided render set.

## LP2 validator

Not run — Phase 8. `POST /api/lp2/learning-plans/validate` must return zero `validation_errors`
before upload, and **Gaps 1, 2 and 4 must be closed first**: a plan uploaded with the placeholder
`publication_id`, a null `chapter_master_id` or an unconfirmed medium segment either fails at
upload or, worse, succeeds into the wrong row.

---

**Verdict: A–D PASS. No blocking failure. `13_merged.json` written (9 topics, 9 objectives, 11
concepts, 9 media nodes, 31 root keys).** This is a full pass of the blocking gate, not a partial
one — the eleven items above are reported gaps and provisional values, none of which is an A–D
failure, and three of which (1, 2, 4) are hard preconditions for **upload**, which is a later phase.

## LP2 validator
- Endpoint: POST /agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json
- Result: validation_errors = [] (0 errors)
- plan_id: gseb_eng_gujarati7_ch2_v1
- message: Valid
