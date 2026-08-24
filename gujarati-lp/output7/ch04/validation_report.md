# Validation Report — std 7, ch 4 · ટીપાંની સફર
સ્વરૂપ: mixed — માહિતીપ્રદ-સાંસ્કૃતિક ગદ્ય (પ્રમુખ) + વાર્તા (કારીગરી-સ્તર) (confidence: high)   explanation unit: એક માહિતી-ખંડ
Topics: 6   Objectives: 6   Images: 0/6   Exercises: 11/11 blocks (49/49 items answered)

## A–D (blocking)   **PASS**

This is the **re-QC pass** after the owner re-run. The single blocker the previous pass raised is
resolved, no new failure appeared, and every A–D item now passes. The run is complete.

### The previous blocker, and its resolution

The previous pass failed §C's craft gate on one string — `M2.S3.T5.key_terms[0]` named the
અલંકાર `સજીવારોપણ` in child-facing text at std 7, where `qc_checklist.md` §C permits the device to
be *shown* but not *named* before std 9. Owner was **A5** (`key_terms` is A5's field).

A5 re-ran and changed **that clause and nothing else**:

> `પવનકુમાર — પવનને અહીં માણસનું નામ આપીને બોલાવ્યો છે; ~~આ સજીવારોપણ છે~~ **આ પાઠની રજૂઆતની રીત છે**, ભૂલ નથી.`

The first clause — the one that teaches the move without labelling it — is untouched, which is
what the standard permits. The replacement wording is A12's own suggestion, filed in
`12_authoring.json` `notes[3]`; A5 recorded the change in `verbatim_notes[11]`.

Verified three ways this pass:

1. **The merge was rebuilt from source, not patched.** Re-folding all six layers onto
   `05_with_content.json` from scratch reproduces the previous `13_merged.json` **key for key and
   value for value**, with exactly one difference: that one `key_terms[0]` string. No other field
   moved, and no working field leaked in.
2. **Full-file label sweep.** `સજીવારોપણ` / `અલંકાર` / `રૂપક` / `ઉપમા` / `ઉત્પ્રેક્ષા` / `અનુપ્રાસ` /
   `છંદ` / `personification` now appear in **zero** child-facing fields across the whole merged plan
   — `topic_name`, `explanation`, `real_life_example`, all three summaries, `key_terms`,
   `concept_bullets`, `important_points`, `recall_questions[].prompt/.answer`, `publication_text`,
   `concepts[].concept_name`, `concepts[].content[]`, `shabdarth` / `samanarthi` / `vilom` /
   `vyakaran`, `objectives[].objective_text` and the module `difficult_words[]`. Every surviving
   occurrence sits in an agent's own `notes[]` / `verbatim_notes[]` / `07_pitfalls.json` check text,
   all of which the merge drops.
3. **07's own check now holds.** `07_pitfalls.json` `topics[4].avoid_checks[2]` asserts that
   `સજીવારોપણ` appears in no child-facing field **including `key_terms`**. That assertion was false
   last pass and is true now — §D strengthened rather than merely staying put.

`figures_of_speech` remains `[]` on all six topics, which is the complete and correct answer here.

### A–D, item by item

| § | Result | Evidence |
|---|---|---|
| **A** diagnosis & lens | PASS | સ્વરૂપ diagnosed off the renders with `genre_signals` + `genre_confidence: high`; the mixed chapter loaded both profiles and cut every part under the dominant one (`એક માહિતી-ખંડ`). Apparatus stayed out: the blue પ્રવેશપેટી, the `[[શબ્દાર્થ]]` box, the two printed ચિત્રો and the closing વ્યાકરણપેટી are all in `not_cut_as_topics`. `guiding_question` is derived from this chapter and the six explanations answer it in order. |
| **B** verbatim & structure | PASS | All six `original_chunk`s non-empty and found as **contiguous substrings of `00_chapter_normalized.md`** once the `[[…]]` scaffolding is stripped. Base script Gujarati U+0A80–0AFF throughout: **zero** Roman and **zero** Devanagari characters outside bracketed technical terms in any authored or verbatim field, and **no `।`** anywhere in the file. Marker accounting below. Ids consecutive; concepts chapter-continuous C1–C8; `word_count.original` recomputed from each chunk and matches on all six (52 / 70 / 170 / 149 / 56 / 196). |
| **C** teaching block | PASS | All 6 topics carry non-empty `explanation` **and** `real_life_example`, **every one inside 55–90 words** (explanations 72–83; examples 65–73). All 6 `objective_text` inside **12–30 words**. Three-tier summaries strictly increase on all 6. 2–3 recall questions per topic, each with a real answer, ids `{topic_id}.RQ{n}` with `legacy_id` `{topic_id}.TR{n}`, `bloom_level` lowercase (Capitalised in `objectives[]`, as the contract requires). **No digits — Roman or Gujarati — in any display text** (`બાર રીતો`, never `12 રીતો`). Craft gate now clean, above. |
| **D** સ્વરૂપ essence | PASS | All **15** `severity: "hard"` items in `07_pitfalls.json` verified addressed in the field each names: no science correction of the talking drops or of `હવાનું દબાણ`; no unprinted facts or measures added (`44 ડિગ્રી` is printed in T3's chunk and is not repeated in display text); no બોધ tacked onto the closing topic; no evaluative label on the `તળાવવાળું ટીપું` (varta avoid #3); `વસ્ત્રાપુરનું તળાવ` kept in its printed form; **all twelve rain-words present in T6's teaching fields in their printed forms** — ફરફર, છાંટા, ફોરાં, કરા, પછેડિયો, નેવાધાર, મોલિયો, ઢેફાંભાંગ, અનરાધાર, અરધિયો, સાંબેલાધાર, હેલી; and no invented meaning for `અરધિયો` or `છાંટા`, the two the printed શબ્દાર્થ box does not gloss. `07`'s one remaining `soft` item was the label gate, now moot. `08_sensitivity.json` carries one `soft` item, `areas: ["ધર્મ"]` — a valid label from the seven — on T6; its guidance is followed: ઇન્દ્રદેવ is glossed only as `વરસાદના દેવ` and framed as the same make-believe as the talking drops, neither literalised nor debunked, and T6's `real_life_example` stays inside the child's own experience of rain. `figures_of_speech` is `[]` on all six, so the "lines found verbatim" check has nothing to fail on. |

### Marker accounting (B)

`00_chapter_normalized.md` carries **no** `[[કડી …]]`, `[[દુહો …]]`, `[[પદ …]]` or `[[ઘટના: …]]`
markers at all — count **0**, matching **0** topics carrying them. It carries **11**
`[[સ્વાધ્યાય: …]]` markers and **0** સ્વાધ્યાય topics: no exercise block became a topic. The four
`[[સંવાદ: …]]` markers are named in `01_meta.json` `extraction_notes[19]` as **reading-order marks,
not cut marks** — `mahitiprad_gadya.md` avoid #2 (hard) forbids cutting where the speaker changes —
and all four are accounted for across T2–T6 with none swallowed. The remaining markers are page
folios, the two `[[ચિત્ર: …]]`, `[[શબ્દાર્થ]]`, `[[વ્યાકરણપેટી: …]]` and the `[[પ્રવેશપેટી]]`, all
apparatus and all correctly outside the cut.

## E–G (reported)

**E — સ્વાધ્યાય and risk.** All 11 inventoried blocks answered.
`coverage_report.blocks_found` has length 11, equals `01_meta.json.exercise_inventory`'s length 11,
and matches it **heading for heading, verbatim and in printed order** — no fuzzy match was even
needed. `unanswered: []`. 49 exercise entries, **none with an empty `answer`**, every one carrying a
`skill` tag, and every `covered_by_topics` reference resolving to a real node. Item granularity is
one entry per separately-answerable printed item, except three blocks that are one integrated
printed task and are answered in full inside a single entry — the nine-blank ફકરો (EX31), the
eight-row જોડકાં કોષ્ટક (EX42) and the અવિકારી-સંજ્ઞા list-plus-five-sentences (EX46); A10 records
this in `coverage_report._note`. Model answers are marked (`is_model_answer`, 21 entries) on the
oral વાતચીત items, the personal વર્ષાગીત line, the અનુવાદ block (answered in the medium of
instruction on purpose and marked in `teacher_note` — a script flag against it is a false positive)
and the મેઘાણી પ્રવૃત્તિ. **12 items are reported `unmapped`, correctly and honestly**: two ભૂગોળ
questions inside the oral વાતચીત block, the વર્ષાગીત item, two અનુવાદ sentences (મેઘધનુષ, મોર), six
adjective-practice blanks and the મેઘાણી પ્રવૃત્તિ. None signals a missed reading scene — the reading
text is six fact-steps carried by talking drops and prints none of that material. No mapping was
invented to empty the list.

**F — shape and media.** The 12 `json_contract.md` invariants hold, checked mechanically against
the emitted file: `phase: 2`; `plan_id` = `{chapter_id}_v{version}`; `chapter_id` =
`gseb_eng_gujarati7_ch4`; every topic has ≥1 concept with a resolving `objective_id` and non-empty
`content[]`; the root registry is complete and consistent (6 unique `objective_id`, every
`home_topic_id` and every `anchor[]` entry resolving, `strand_to_objective_map` L1–L6 covering all
six, single strand `L`, all `status: "taught"`); **inline `learning_objectives[].objective_text`
matches the root registry character for character** on all six topics; media ids match
`MEDIA_ID_RE` concept-scoped with chapter-continuous `.C{c}`; recall ids are `RQ{n}` + `TR{n}` and
**the string `.SR` does not occur anywhere in the file** (this chapter carries no segment-level
recalls at all); `publication_id` is non-null; summaries strictly increase at topic and module
level; no numbers in display text; every `depends_on` resolves. `topic_type` carries the authored
enum (5 × `CONCEPT`, 1 × `STORY_TELLING`) — Agents 14/15 map both to `instructional`; the closed
server enum is theirs to write, not Agent 13's, and `ordering` is likewise left unset here.
`chapter_id`'s board/medium segments remain provisional until VERIFY-1.

**G — the seven usual mistakes.** (1) Not a સાર+બોધ pack — every explanation opens on its
માહિતી-ખંડ's fact. (2) No merge failure to check: this is ગદ્ય; `kadi`/`duha`/`pad`/`tek` are all 0.
(3) No પદ to split. (4) No poetic licence corrected — `કાળાંડિબાંગ`, `રડમસ`, `ઢેફાંભાંગ`,
`પછેડિયો`, `નેવાધાર`, `અરધિયો` all stand as printed; `ળ` never levelled to `લ`. (5) **Now clean in
both directions** — no અલંકાર was named because the field existed (`figures_of_speech` correctly
`[]`), and the device name no longer leaks into a gloss either. (6) The six `real_life_example`s are
Indian, concrete, single and inside std-7 reach — દૂધમંડળી, નિશાળનું મેદાન, ઉનાળાનું બપોર, મેળામાં
છૂટેલો હાથ, ઉત્તરાયણનો કપાયેલો પતંગ, પતરાના છાપરા નીચેનો વરસાદ. (7) No સ્વાધ્યાય block became a
topic.

## Media
`reuse_report`: `scenes: 6`, `authored: 6`, `reused: 0`, `rejected: []` — **no frames rejected,
because no Gujarati frame pool exists to draw from**. Six topics carry `"image"` in
`available_content_types` and there are exactly six media nodes, one per reading scene (T4 and T6
each hold two concepts but one image, which is the rule — one image per *scene*, not per concept).
Every node has `image_url: ""` **and** a real self-contained `generation_prompt` (1 076–1 291
chars, each naming its own setting, characters, action, mood, style and the exact Gujarati narrator
string to render); no `[reused frame: …]` stamp and no fabricated URL anywhere. Every
`negative_prompt` carries `Devanagari script labels`. Media `title`, `description` and
`teaching_notes` are pure Gujarati with no digits. Exactly **one** `2d_tool` in the chapter, landed
on `M2.S3.T5` as a string — an interactive 'ટીપું ક્યાં જાય છે ?' panel that keeps to the chapter's
own words and puts no ઇન્દ્રદેવ figure and no number on screen. `Images: 0/6` is written, not
omitted.

## Gaps

Unchanged from the previous pass; none of them blocks, and none was closed by invention.

- **`publication_id` is provisional and wrong-by-default.** Written as `1` to satisfy the server's
  non-null rule. That is **CBSE's publication row and does not transfer to GSEB**
  (`phase2_contract.md` rule 1). `upload_reference/chapter_master_map.json` still carries `null` for
  every GSEB row. **VERIFY-2 must replace it before any Phase 8 upload.**
- **`chapter_master_id` is `null`** — the GSEB row is fetched from the education DB, never derived
  and never invented. Upload is blocked on VERIFY-2 until it lands.
- **`chapter_id` board/medium segments provisional (VERIFY-1).** A wrong medium slot uploads clean
  and mis-files the plan.
- **`textbook_url` is a local path**, `../Textbooks-pdf/std-7/ch-04-tipani-safar.pdf` — the GSEB
  readers have no hosted URL. `11_pages.json` records this; pagination itself is `19–24` at
  `confidence: high`, read off the printed folios on renders of pages 1 and 6.
- **`teaching_lens` ships as the headline clause** `તથ્ય + પરંપરા + જિજ્ઞાસા`. `01_meta.json`
  appends A1's guidance prose to the same headline (and that prose itself contains the word
  `સજીવારોપણ`, which is why the shipping value must stay the clean headline);
  `02_structure.json` and `05_with_content.json` both carry the clean headline, and A4 recorded,
  non-blocking, that the shipping lens must not concatenate the guidance paragraph. Flagged so the
  orchestrator can overrule if A1 intended otherwise.
- **`topic_title` set to the chapter name** `ટીપાંની સફર`, pairing with `unit_title`; no agent
  authored this root key and the contract requires it.
- **`publication_chunk` is a composite, not a byte-copy of `original_chunk`.** Each one is
  `original_chunk` + the publication prose + the publication-facing example. Agent 13's spec says
  "byte-identical"; `agents/16_publication_authoring.md` says the chunk is the publication-facing
  version of the topic's block *as a whole*, with the verbatim `original_chunk` staying verbatim
  **inside** it. A16 followed its own spec. Verified mechanically again this pass: on all six topics
  `original_chunk` is a **byte-exact prefix** of `publication_chunk` — the verbatim is intact and
  untouched. Recorded as a **pack-internal wording discrepancy between two specs**, not as a defect
  in A16's output; someone should reconcile the two files.
- **Marker-to-topic mapping is documented, not 1:1, and that is deliberate** — see the marker
  accounting above. One topic, **T1**, sits on an unmarked printed reading paragraph (line 10) that
  Agent 1's own structure inventory counts as the first માહિતી-ખંડ: a printed reading scene, not an
  invented topic.
- **Agent 4's non-blocking notes travel here:** topic length is uneven (T5 is a single printed
  quoted turn at 56 words; T6 spans the twelve-rain-ways litany at 196, which the profile names this
  chapter to protect and which must not be split); **M2 holds a single segment**, because the
  water's descent is one continuous printed stretch and splitting it would produce one-topic
  segments. Both reported, neither corrected.
- Chapter provenance: the author slot prints `- સંકલિત`, not a name, so this unit has **no
  લેખક-પરિચય box and no CONCEPT topic for one**, and no end-of-text attribution line exists to carry
  inside the last `original_chunk`.
- This chapter reached Agent 4 on its **third** pass (pass 1 failed to A1, pass 2 to A2; both
  preserved under `_invalid/`), and reached Agent 13 on its **second** (this one), after the A5
  re-run above. Every blocking item from all of them is resolved, and `04_converged.json` records
  `converged: true` against `02_structure.json` at sha256 `2a4df0ba…`.

## LP2 validator
Not run — filled in Phase 8. It cannot be run meaningfully yet in any case: `chapter_master_id` is
`null` and `publication_id` is CBSE's provisional row (see Gaps). A–D passing here is the pack's own
gate, not the server's.

## LP2 validator

- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json
- Status: reachable (HTTP 200)
- validation_errors:
  1. root: 'publication_id' is required and must not be null
