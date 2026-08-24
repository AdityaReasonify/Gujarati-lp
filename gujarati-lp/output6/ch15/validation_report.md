# Validation Report — std 6, ch 15 · લો, પાથરી મારી વાત

સ્વરૂપ: આત્મકથનાત્મક નિબંધ (`nibandh_atmaparak`, confidence: high)   explanation unit: એક પ્રસંગ, અથવા વિચારનો એક વળાંક
Topics: 11   Objectives: 11   Images: 0/10   Exercises: 18/18 blocks (59/59 item entries answered)

Merged plan written to `13_merged.json` — 32 root keys, 4 modules / 5 segments / 11 topics /
13 concepts / 11 objectives / 10 media nodes / 0 `2d_tool`.

---

## A–D (blocking)   **FAIL** — three items, all in `05_with_content.json` (owner: `agents/05_verbatim_attachment.md`)

### D-1 (hard) — an invented life-fact about a real named person
`M1.S1.T1.modified_chunk` reads
`પાલુબેન પોતાની ઓળખ પોતે જ આપે છે — પોતાનું નામ, **ધણીનું નામ** અને પોતાનો ધંધો.`

The chapter prints only `હું પાલુબેન વશરામભાઈ.` Neither the body, nor the શબ્દાર્થ box, nor the
blue intro box says whose name વશરામભાઈ is. `07_pitfalls.json` names this exact wording as a
**hard** check on this topic ("a gloss of the shape 'ધણીનું નામ' or 'પતિનું નામ' is a life-fact the
page does not carry"), and `nibandh_atmaparak.md` Avoid gate 8 bars **any** field from attributing a
life-fact to a real named person that the page does not state. `modified_chunk` is a shipping,
child-facing contract field, so the gate applies to it.
Every other agent obeyed the check: A12's `explanation` correctly says only
`એ બે શબ્દ એક જ વ્યક્તિનું આખું નામ છે`.

### D-2 (hard) — a measure supplied from outside the chapter
`M2.S2.T4.key_terms[2]` reads `મણ — વજનનું જૂનું માપ; **એક મણ એટલે આશરે વીસ કિલો.**`

### D-3 (hard) — the same fact again, in prose
`M2.S2.T4.modified_chunk` reads `ત્રણ-ચાર મણ **(એક મણ એટલે આશરે વીસ કિલો)** માલ ભરીને…`

`07_pitfalls.json` `chapter_level[5]` is explicit: the printed apparatus "**ARE** the limit of what
may be asserted: two things the box does not carry, **the size of a મણ** and any fact about ‘સેવા’
beyond its printed line, must be left unfilled rather than filled from outside knowledge."
`nibandh_atmaparak.md` Avoid gate 9 (hard) says the same for every **measure**. The chapter's
શબ્દાર્થ box glosses thirteen words and મણ is not among them.
Here too every downstream agent held the line — A12's `difficult_words` and `explanation` gloss મણ
only as `વજન કરવાનું જૂનું માપ`, with no kilo equivalent anywhere, and A10 says so in its own note.

**Route:** A5 re-emits `05_with_content.json` with the ધણી clause and both વીસ-કિલો clauses removed.
`original_chunk`, ids, the objectives registry and every other layer are unaffected, so nothing
downstream needs re-running; A13 re-merges and re-gates. **This run is not complete.**

### A–D items that PASS

- **A — diagnosis and lens.** સ્વરૂપ diagnosed off the render on four signals (`genre_signals`),
  `genre_confidence: high`; the blue intro box's own line
  `વિદ્યાર્થીઓને આત્મકથનાત્મક નિબંધસ્વરૂપનો પરિચય કરાવવો.` is quoted as evidence, not as the verdict,
  and the two near-misses (`mahitiprad_gadya`, `charitra_prasang`) are recorded as examined and
  rejected. The explanation unit is the profile's own — one પ્રસંગ / one વળાંક — and the eleven
  topics follow the cut `nibandh_atmaparak.md` prints for **this** chapter by name. Apparatus stayed
  apparatus: the blue intro box, the શબ્દાર્થ box, the રૂઢિપ્રયોગ pre-block, the p.101 market
  illustration and the printed byline are all listed in `markers_deliberately_not_cut` and none
  became a topic. `guiding_question` is chapter-specific and the eleven explanations read in order
  answer it. No ટેક / કડી / દુહો / પદ sub-rule applies — this is unbroken prose.
- **B — verbatim and structure.** All eleven `original_chunk`s are non-empty, pure Gujarati
  (U+0A80–0AFF), and each is found verbatim in the reading body of `00_chapter_normalized.md`
  (whitespace-normalised containment; see the one render-settled divergence under **Gaps**). No
  Roman and no Devanagari anywhere outside bracketed glosses, in any field of the merged plan; no
  `।` introduced. Ten `[[ફકરો n]]` reading-scene markers map onto eleven topics through the full
  `marker_to_topic_map` with no marker swallowed — ફકરો 3 cut four ways at the writer's own turns,
  ફકરો 8–10 held as one closing gesture, both departures argued from the unit and re-verified here.
  All 18 `[[સ્વાધ્યાય: …]]` blocks sit outside the topic tree; **no સ્વાધ્યાય block became a
  topic**. The spoken register survives untouched (દા'ડો, કો'કવાર, હારુ, બચારાં, બોણી, વઢ, આયખું,
  ઢસરડા, ન્યાત, ઠૂસ). Profile gate 13 holds: the chapter's last printed sentence
  `આવજો ત્યારે પૃથાબેન !` closes `M4.S5.T11.original_chunk`, and there is no post-text credit to
  pull in (see **Gaps**).
- **C — the teaching block.** Every topic has a non-empty `explanation` (70–88 words) **and**
  `real_life_example` (60–68 words); all 22 inside the 55–90 band. All eleven `objective_text`
  values are 21–27 words, inside 12–30. No band was widened. Every real-life anchor is Indian,
  single and inside std-6 reach (વર્ગમાં પરિચય, ઉત્તરાયણની ફિરકી, એસ.ટી. ડેપોની બારી, રિસેસનો નળ,
  શેરી ક્રિકેટની છેલ્લી ઓવર…). No craft label a std-6 child may not meet appears in any
  child-facing field — નિબંધ, આત્મકથા, પ્રથમ પુરુષ, અલંકાર, વ્યંગ, કટાક્ષ are absent throughout.
- **D — સ્વરૂપ essence (apart from D-1…D-3).** `figures_of_speech` is `[]` on all eleven topics and
  `rhyme_scheme` is `null` — correct and complete for prose, and the profile's gate 15 is therefore
  vacuously satisfied. No topic carries `topic_category: "climax"` (Avoid 2). No pity or judgement
  register anywhere — બિચારાં / ગરીબ / અભણ / પછાત / લાચાર / "આ લોકો" occur in no field (Avoid 14);
  the chapter's own printed `બચારાં !` is quoted only inside `original_chunk`. No tacked-on બોધ:
  no field closes on "આ પાઠ આપણને શીખવે છે…" or "આપણે પણ … જોઈએ" (Avoid 3); પાલુબેનનું
  `પણ છોકરાંને ભણાવીશ. તો જ ઉજળા દિવસો આવશે.` is quoted and taught as her own નિર્ધાર. Avoid gate 1
  holds on all eleven: પાલુબેન is the grammatical subject of the first sentence of every
  `explanation`. The chapter is not routed to the હાસ્ય sub-form, so gates 4–5 do not bite and
  nothing is labelled વ્યંગ or કટાક્ષ. The **one hard sensitivity item** —
  `M3.S4.T8` / `સંઘર્ષ` — is genuinely addressed: T8 reports only what the chunk prints, ascribes no
  motive to the મ્યુનિસિપાલિટીવાળા / પોલીસ / દબાણ ખસેડવાવાળા, closes on her own
  `આખરે નુકસાન તો અમારું જ થતું.`, and none of its three recall questions asks the child to judge
  the authorities. The four soft sensitivity items (જાતિ-ભૂમિકા ×3, સમુદાય ×1) are all followed, and
  every `areas[]` label is one of the fixed seven.

## Contract (the 12 `json_contract.md` invariants)   PASS

1. `phase: 2`; `chapter_id: gseb_eng_gujarati6_ch15`; `plan_id: gseb_eng_gujarati6_ch15_v1`. ✔
2. Every topic carries a non-empty Gujarati-script `original_chunk`. ✔
3. Every topic has ≥1 concept, each with a valid `concept_id`, a resolvable `objective_id` and
   non-empty `content[]` (the content arrives from A12; A5's spine carries it empty by design). ✔
4. Registry complete and consistent: 11 unique `objective_id`s, every `home_topic_id` and every
   `anchor[]` entry resolves, `strand_to_objective_map` covers L1–L11 one-to-one, every topic's
   `objective_ids` resolve, every `depends_on` resolves. ✔
5. Inline mirrors built at merge from the root registry and compared character for character —
   11/11 identical, each carrying `image_examples: []`. ✔
6. Id grammar: M1–M4 / S1–S5 / T1–T11 match traversal position exactly; concepts run
   **chapter-continuous** C1…C13 (`M4.S5.T11.C13`); media match `MEDIA_ID_RE` and are
   **concept-scoped**; recalls are `{topic}.RQ{n}` with `legacy_id` `{topic}.TR{n}`. **No `.SR{n}`
   anywhere.** ✔
7. No સ્વાધ્યાય block is a topic; all 18 inventoried blocks are answered in
   `10_exercise_solutions.json`. ✔
8. Three-tier summaries strictly increase on all eleven topics (e.g. 22 < 45 < 96 words). ✔
9. No numbers in display text — a digit scan over every name, explanation, example, summary,
   bullet, key term, concept paragraph, recall prompt/answer, objective, media title and
   `difficult_words` entry returns zero hits. Digits survive only in ids, `word_count`,
   `textbook_pages` and inside `original_chunk` / `prompt_verbatim`, where the page's own numerals
   belong. ✔
10. Media — see below. ✔
11. `figures_of_speech` is `[]` everywhere, so no device is asserted that the lines do not carry. ✔
12. Every reference resolves as merged; ids are frozen per `04_converged.json` and renumbering is
    Agent 14's. ✔

`topic_type` is `STORY_TELLING` on all eleven — the authored enum the intermediate files carry;
Agents 14/15 map it to `instructional`. `publication_id` is non-null (see **Gaps**).

## E–G (reported)

- **E — સ્વાધ્યાય and risk.** All 18 printed blocks inventoried, found and answered; 59 item-level
  entries; `unanswered: []`. Personal-opinion, પ્રવૃત્તિ and interview blocks (the ફેરિયાની
  દિનચર્યા composition, the ‘એક સાઈકલ’ની આત્મકથા, the vendor-interview task, the vendor cries, the
  time-sentence bullets) are answered as marked model answers rather than skipped. The printed
  grids — the ordering list, the paragraph cloze, the dialogue completion, the જોડકાં, the
  long-word hunt — are filled with teaching values. The standing L2 block
  **નીચેનાં વાક્યોનો તમારી પ્રથમ ભાષામાં અનુવાદ કરો.** is answered in the medium of instruction on
  purpose and marked as such in `teacher_note` — that is not a script failure.
  **One block is reported `unmapped` and was not closed by inventing a mapping**: EX43
  (`નીચેનો ફકરો વાંચો. તેમાં પાંચ કે વધુ અક્ષરવાળા જે જે શબ્દો હોય તેની યાદી કરો.`) prints its own
  stand-alone paragraph whose words occur nowhere in the chapter, so no reading scene prepares it.
  Correct behaviour; recorded, not fixed.
- **F — shape and media.** The four shape items the LP2 server rejected on the Hindi pack's first
  run all hold here: `publication_id` non-null, `topic_type` from the authored enum (mapped at
  emit), segment recalls would be `.RQ{n}` (this chapter authors none), concept numbers
  chapter-continuous. `chapter_id` / `plan_id` follow `naming_conventions.md`; **the board and
  medium segments remain PROVISIONAL until VERIFY-1** — a wrong medium uploads clean and mis-files
  the plan.
  Minor, reported only: all 13 `concepts[].key_terms` are `[]` (the glosses live on the topic's
  `key_terms`, 4–6 per topic, and in `shabdarth`); `01_meta.json.genre` holds the Gujarati form
  `આત્મકથનાત્મક નિબંધ` rather than the roster slug, so the merge took `genre: "nibandh_atmaparak"`
  from `05_with_content.json.genre_slug`, which is what the phase-2 contract asks for — worth
  fixing in A1 so the two files agree; `textbook` reads
  `ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 6` (comma) where `phase2_contract.md`'s example uses a pipe —
  A1 and A11 agree with each other and both read it off the title page, so it is left as read.
- **G — the seven usual mistakes.** None present. The plan is not સાર + બોધ + પ્રશ્નોત્તર (1); there
  are no દુહા to merge (2) and no પદ to split (3); no poetic licence was corrected — every printed
  spoken form stands and `00`'s own note lists them (4); no અલંકાર was invented, `[]` throughout
  (5); every `real_life_example` is a std-6 Indian anchor (6); the સ્વાધ્યાય deliverable is complete
  and no exercise was cut as a teaching topic (7).

## Media

`reuse_report: {scenes: 10, reused: 0, authored: 10, rejected: []}` — and it matches the plan
exactly: 10 topics carry `"image"` in `available_content_types` (all but `M1.S1.T2`, the reflective
hours-against-વળતર topic, which is deliberately imageless), and 10 media nodes exist, one per scene,
each on the concept it belongs to. **Every node carries `image_url: ""` and a non-empty, self-
contained `generation_prompt`** — correct, because no Gujarati frame pool exists; a filled
`image_url` here would be a fabricated URL. No `[reused frame: …]` stamp anywhere, so `rejected: []`
is an honest empty rather than an unreported reuse. Every `negative_prompt` carries
`Devanagari script labels`. `2d_tool` is `null` for the whole chapter — this સ્વરૂપ rarely earns it,
and at most one would be permitted.

## Gaps

- **`chapter_master_id` is `null` and `subject_ref_id` / `medium_id` are `null`.** No GSEB record has
  been fetched. `chapter_master_id` is required for upload and must come from the education DB
  (**VERIFY-2**) — never invented, never derived by arithmetic. `subject_ref_id` / `medium_id` are
  server-injected and correctly left null.
- **`publication_id` is written as `1` and is PROVISIONAL.** The server rejects `null`, so a
  non-null value had to be written; `1` is **CBSE's publication row and is not portable**. The real
  GSEB row must be looked up (**VERIFY-2**) before the first Phase 8 upload. Do not treat this
  value as verified.
- **`chapter_id` board/medium segments PROVISIONAL until VERIFY-1** — `gseb` and `eng` are reasoned
  from the Hindi precedent, not read from the live server, and a wrong medium uploads clean.
- **`textbook_url` is a local path**, `../Textbooks-pdf/std-6/ch-15-lo-pathri-mari-vat.pdf` — the
  GSEB readers have no hosted URL. A11 records the gap; `textbook_pages: "101–107"` is
  high-confidence (folios read off page-1 and page-7 renders and cross-checked against the PDF
  manifest), so pagination is a recorded absence, not a block.
- **One transcription defect in `00_chapter_normalized.md`, settled on the render.**
  `[[ફકરો 7]]` of the normalized file reads `થાકીને **ઠુસ** થઈ ગઈ હોઉં` (હ્રસ્વ ુ) where
  `05_with_content.json`'s `M4.S5.T10.original_chunk` reads `ઠૂસ` (દીર્ઘ ૂ). Because the two
  authoritative files disagreed, `_renders/page-2.png` (folio 102) was opened — the only render read
  in this pass, and the reason it was needed. At 16× the mark under ઠ is the broad open hook, glyph-
  identical to the દીર્ઘ ૂ under સૂ in `સૂઈ ગયાં` two lines below, and plainly unlike the tight
  closed હ્રસ્વ ુ under ડ in `મોડું` on the same line. Folio 103's bold રૂઢિપ્રયોગ box does print
  `થાકીને ઠુસ થઈ જવું` with હ્રસ્વ ુ, so **the book itself is inconsistent between its paragraph and
  its idiom box**. The plan is right: A5's chunk follows the printed paragraph, and A12/A16 quote
  `ઠૂસ` while glossing it with the box's own printed meaning. Two files should be corrected to
  match the page: `00_chapter_normalized.md` ફકરો 7 and its `extraction_notes[]` spoken-forms list
  (owner **A1**), and the `M4.S5.T10` hard check in `07_pitfalls.json` that quotes `'ઠુસ'` as the
  body form (owner **A7**). Neither blocks — nothing that ships carries the wrong form — but leaving
  them uncorrected will re-raise this flag on every future pass.
- **A4's carry-forward on the byline is a false alarm and is closed here.** `04_validation.json`
  told A5 that the printed attribution `- પૃથાબેન વ્યાસ` must land inside `M4.S5.T11.original_chunk`
  under profile gate 13. `page-1.png` shows the byline printed at the **top of the chapter, above
  the blue intro box, before the text** — it is not a post-text credit, and gate 13 asks only for
  credits printed **after** the text. A7's M4.S5.T11 check reads it the same way. A5 correctly left
  it out; no action.
- **Uneven topic length, reported not blocked** (A4's note): `M4.S5.T11` spans about twenty printed
  words while `M2.S2.T4` and `M3.S4.T8` run four to six times that. The short topic is the
  chapter's closing gesture, which the profile requires to stand alone.
- **Context-routing gaps recorded by earlier agents**, passed on so the orchestrator can widen the
  bundles: A12 was not given `teaching_block_format.md`, `alankar_chhand.md`, `shabd_gloss.md`,
  `bhasha_bodh.md` or `profiles/students/std-6.md` (it read all five from disk); A4 was not given
  `loop_protocol.md`, `explanation_unit_map.md`, `phase2_contract.md` or `naming_conventions.md`.
  This agent was given every document its own spec cites.
- **`05b_textbook_order.json` matches the logical traversal.** Per `phase2_contract.md` §Ordering
  this must be raised for human confirmation at emit; `ordering` is left `null` in `13_merged.json`
  because it is Agent 14/15's to set.

## LP2 validator

Not run — filled in Phase 8. `POST /api/lp2/learning-plans/validate` must return zero
`validation_errors`, and it must not be attempted before VERIFY-1 (board/medium) and VERIFY-2
(`publication_id`, `chapter_master_id`) land, since both are still provisional above.

---

**Verdict: FAIL on A–D.** Three hard items, one file, one owner
(`agents/05_verbatim_attachment.md`). Everything else in this chapter — the cut, the verbatim, the
teaching block, the exercises, the media plan, the publication layer and all twelve contract
invariants — passes, but a run with any A–D failure is not complete, and this one is not being
presented as a pass.

## LP2 validator (Phase 8 update)

`POST /api/lp2/learning-plans/validate` run against `learning_plan_logical.json`. HTTP 200 on
first attempt (no retry needed).

```json
{"success":true,"action":"validated_only","plan_id":"gseb_eng_gujarati6_ch15_v1","version":null,"phase":null,"is_active":null,"is_draft":null,"counts":null,"diff":null,"publication_id":null,"publication_name":null,"validation_errors":[],"message":"Valid"}
```

`validation_errors`: **empty**. Result: **PASS** (validator-clean). No upload performed —
validation only, per instructions.
