# Validation Report — std 7, ch 12 · બે રૂપિયા

સ્વરૂપ: `varta` — sub-form **ઘરેલુ / સામાજિક વાર્તા** (confidence: high)   explanation unit: **એક ઘટના**
Topics: 8   Objectives: 8   Images: 0/8   Exercises: 16/16 blocks (74/74 printed items answered)

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` → `13_merged.json` (31 root keys, 37 topic keys, 3 modules,
6 segments, 8 topics, 15 concepts, 8 media nodes, `2d_tool: null`). `ordering` is deliberately
absent — Agent 14/15 sets it, not this agent.

No working field survived the merge. Dropped: `markers`, `source_lines_00_normalized`,
`cut_summary`, `not_cut_as_topics`, `convergence`, `verbatim_provenance`, `content_type_basis`,
`genre_signals`, `genre_confidence`, `structure_inventory`, `extraction_notes`,
`exercise_inventory`, `active_genre_profiles`, `explanation_unit`, `genre_subform`,
`word_count.modified`, pitfall `avoid_checks` / `misconception` / `correction`, sensitivity
`areas` / `caution` / `guidance` / `severity`, media `reuse_report`, exercise `coverage_report`,
publication `concept_publication` (folded into `concepts[].content[].publication_text` by index),
`tier`, and every agent's `notes[]`. Only contract keys ship.

---

## A–D (blocking)   **PASS**

### A — diagnosis and lens

`01_meta.json` records the four signals read off the rendered page, and the book names its own
subject in the blue પ્રવેશપેટી (p. 77), quoted as **evidence, not verdict**:
"આ વાર્તામાં એક દીકરીની પ્રામાણિકતાની સરસ વાત છે." Measured signals: prose with named પાત્રો
(આનંદી, માણેકલાલ, અવંતિકાબહેન, મંગુબાઈ, ડૉક્ટર બાઈ, મોટાં બહેન), past-tense narration, dialogue
inside `''…''`, a chain of ઘટના, and one clear વળાંક. `varta.md` Signal C is present in the
apparatus: the વાતચીત block prints the form's own counterfactual tell —
"આનંદીએ લેડી ડૉક્ટરને બે રૂપિયા પાછા ન આપ્યા હોત તો ?" — plus motive questions in the written
block. `structure_inventory` records `kadi: 0, duha: 0, pad: 0, tek_occurrences: 0`, so every
verse-side rule is vacuously satisfied, confirmed against the transcription rather than assumed.

**Explanation unit matches the roster row.** વાર્તા — "one ઘટના". Verified mechanically against
`00_chapter_normalized.md`:

- **8** `[[ઘટના: …]]` markers, **0** `[[કડી …]]` / `[[દુહો …]]` / `[[પદ …]]`, **16**
  `[[સ્વાધ્યાય: …]]` blocks.
- **8** topics, carrying **8** `markers[]` entries between them — one marker per topic, in printed
  order M1.S1.T1 → M3.S6.T8. Marker count equals topic count exactly.
- **No `[[સ્વાધ્યાય: …]]` block became a topic.** All sixteen `verbatim_heading` strings from
  `01_meta.json`'s inventory were compared against all eight `topic_name` values: zero matches.
- Apparatus stayed apparatus: `[[પ્રવેશપેટી]]`, `[[શબ્દાર્થ]]`, `[[રૂઢિપ્રયોગ]]` and the
  chapter-final `[[વ્યાકરણપેટી: હકારવાચક અને નકારવાચક વાક્યરચના]]` are all in
  `not_cut_as_topics` and none is a node in the merged plan.
- ટેક handling does not arise (`tek_occurrences: 0`); this is ગદ્ય.
- Not a mixed chapter: `active_genre_profiles` is `varta.md` alone.

`guiding_question` is derived from this chapter and could fit no other —
"મળી ગયેલી બે રૂપિયાની નોટ પાછી આપતાં પહેલાં આનંદીના મનમાં શું શું ચાલ્યું, અને એ ક્ષણે એણે શું
પસંદ કર્યું ?" Reading the eight explanations in order does answer it: the શરત, the ઘરની તંગી, the
છુપાવેલી વાત, the રાતની પ્રાર્થના, the નોટ, the નળ પરનું દ્વંદ્વ, the હાથમાં મુકાયેલી નોટ, the
પરિણામ.

### B — verbatim and structure

- All 8 `original_chunk` values non-empty and **byte-identical** to `05_with_content.json` after
  the merge (asserted programmatically; the merge reflowed, re-spaced and re-punctuated nothing).
- Every `original_chunk` paragraph was located **verbatim** inside `00_chapter_normalized.md`.
- Script: the base script is Gujarati (U+0A80–0AFF) throughout. **Zero** Devanagari and **zero**
  Roman characters outside bracketed terms in any `original_chunk`, `topic_name`, `concept_name`,
  `explanation`, `real_life_example`, summary, bullet, `key_terms` entry, recall prompt/answer,
  concept content block, `objective_text`, `publication_text`, or media
  `title`/`description`/`teaching_notes`. **No `।` anywhere.** The whitelist in §"What the script
  check must not flag" does not arise: this chapter prints no non-Gujarati content, and
  `extraction_notes[]` records none. (The one place non-Gujarati script legitimately appears is the
  standing અનુવાદ block's answers in `10_exercise_solutions.json`, written in the medium of
  instruction on purpose and marked as such in `teacher_note` — a separate deliverable, and a false
  positive if flagged.)
- The chapter's printed oddities recorded by Agent 1 stand intact in the verbatim and were **not**
  "corrected": `માંડયો` / `પડયું` without the halant conjunct, `ઊનાંઊનાં` as one word, the vocative
  `હે` outside the opening quotes of the prayer, the unclosed single quote at
  `'તું સાચું બોલી એનું ઇનામ !`, `'હું જ કમનસીબ છું?'` with no space before the `?`, and the
  page's own `સ્ત્રીદાક્તર` / `દાક્તર` / `મમ્મી` / `મોટાં બેન` forms.
- The attribution line `- વિનોદિની નીલકંઠ` is header furniture on p. 77, correctly excluded from
  the topics along with the chapter-number box and the QR code string `K9V6Q2`.
- Ids consecutive and traversal-consistent: modules `M1..M3`, segments `M1.S1..M3.S6` (1–6, never
  restarting), topics `T1..T8`, concepts `C1..C15` **chapter-continuous**. Every id was checked
  against its traversal position, which is the check the LP2 validator itself performs.

### C — the teaching block

Every topic has non-empty `explanation` **and** `real_life_example`. Measured word counts, all
inside the 55–90 band:

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 80 | 68 |
| M1.S2.T2 | 77 | 69 |
| M1.S2.T3 | 75 | 71 |
| M2.S3.T4 | 75 | 74 |
| M2.S4.T5 | 81 | 68 |
| M3.S5.T6 | 83 | 75 |
| M3.S5.T7 | 84 | 74 |
| M3.S6.T8 | 81 | 73 |

`objective_text` word counts: O1 22, O2 21, O3 22, O4 20, O5 22, O6 21, O7 21, O8 22 — all inside
12–30. No band was widened and no prose needed trimming.

Voice and L2 calibration hold: second person, સરળ બોલચાલની શિષ્ટ ગુજરાતી, one new thing per
sentence, and glossing at the point of first use (`પર્યટન`, `શેતરંજી`, `ટંક`, `ભાથું`, `ભાન`,
`પાણિયારું`, `પર્સ`, `અથથી ઇતિ સુધી`, `પગે પાંખો આવવી`). The printed રૂઢિપ્રયોગ box is this
chapter's real L2 trap and each of its idioms is glossed where it occurs. Anchors are Indian,
concrete and single, and inside a std-7 child's reach — the શેરી cycle ride, the શાકની લારી, the
રિસેસનો ડબ્બો, the આંગણે ખાટલો, the ઉત્તરાયણ પતંગ, શેરી ક્રિકેટ, the first ઝાપટું, the ફળિયાનો
ગરબો. Craft is named at std-7 level only (doubled-word intensity in `રાજી રાજી`, two facing
sentences, the printed order of decision-then-question) — no અલંકાર, no છંદ, no સાહિત્યપ્રકાર
label anywhere, which is correct for this standard.

### D — સ્વરૂપ essence

`07_pitfalls.json` instantiates **16 hard** avoid-checks across the 8 topics (plus 2 soft). Each
was re-run mechanically against the merged plan's authored fields:

- **avoid 1 — summary-only.** No `explanation` equals its topic's `modified_chunk`; each adds
  motive, craft or consequence (T1 names the શરત as the cause of the fallen face; T8 separates the
  surrendered note from the ડૉક્ટરના પર્સમાંથી નીકળેલા જુદા બે રૂપિયા).
- **avoid 2 — tacked-on બોધ.** Zero matches for `આ વાર્તા આપણને શીખવે છે`, `બોધ એ છે કે`,
  `આપણે પણ … જોઈએ`, `આપણને શીખવે છે` in any explanation, summary, bullet, recall answer or
  publication text. The પ્રવેશપેટી's teacher-addressed
  "વિષમ પરિસ્થિતિમાં પણ પ્રામાણિકતા જાળવી રાખવાની ભાવના પ્રેરણાદાયી છે" was **not** recycled as a
  child-facing moral anywhere.
- **avoid 3 — judging a sympathetic character.** Zero matches for ગાંડો/ગાંડા/ગાંડી, મૂરખ, ખોટો,
  ગુનેગાર, અંધશ્રદ્ધાળુ, ચોર, નાલાયક, બેવકૂફ in any authored field. માણેકલાલ, આનંદી and મંગુબાઈ
  carry no evaluative label. The ડૉક્ટરની શંકા "કોણ જાણે એ જૂઠુંય બોલતી હોય" is not repeated as the
  story's claim.
- **avoid 4 — spoiling the turn.** `topic_category: "climax"` sits on **M3.S5.T7**. Every authored
  field of T1–T6 was scanned for મંગુબાઈ / મંગુ / ઇનામ / માફી વિદ્યાર્થિની / પાછી આપ… : **zero
  hits**, in teaching prose, in publication prose and in media titles, descriptions, teaching notes
  and generation prompts alike.
- **avoid 5, 6, 7, 8** are inert here and were confirmed inert rather than skipped: no પૌરાણિક કથા
  (nothing debunked or verified — the ભગવાન/નોટ question is held exactly as the chapter holds it,
  both sentences, in the chapter's own order), no તળપદી dialect register to standardise, not an
  excerpt (the story is complete on the page), and the only printed credit is the author's.
- **`figures_of_speech: []` on all 8 topics** and `rhyme_scheme: null`, `overall_rhyme_scheme:
  null` on all 3 modules. This is ગદ્ય below the named-device gate: the empty list is the complete
  answer, not a gap. The verbatim-quotation check therefore has nothing to fail on, and no device
  was invented to fill the field.
- **Sensitivity `08_sensitivity.json`:** 6 topics flagged, `areas[]` drawn only from the seven fixed
  labels (વિકલાંગતા ×1, જાતિ-ભૂમિકા ×1, ધર્મ ×4). **One hard item** (M1.S2.T2, વિકલાંગતા) — and it
  is genuinely addressed: the period phrases `મગજ અસ્થિર થઈ ગયું` and `ગાંડાની ઇસ્પિતાલ` were
  searched across every authored and publication field of every topic and appear **nowhere outside
  `original_chunk`**; the teaching says only that the father's સીવવાનું કામ stopped because of his
  તબિયત, and it keeps the family's dignity and the mother's work framed as this family's response
  rather than a statement about women.

### Contract — the 12 `json_contract.md` invariants

1. `phase: 2`; `chapter_id` = `gseb_eng_gujarati7_ch12`; `plan_id` = `gseb_eng_gujarati7_ch12_v1`. ✔
2. 8/8 non-empty Gujarati-script `original_chunk`, no Roman, no Devanagari. ✔
3. 8/8 topics carry ≥1 concept; 15 concepts, each with a valid id, a resolvable `objective_id`, and
   non-empty `content[]`. ✔
4. `objectives[]` O1–O8 unique; every `home_topic_id` and every `anchor[]` id resolves to a real
   node; `strand_to_objective_map` covers L1–L8 exactly once; every topic's `objective_ids`
   resolve. ✔
5. Inline mirrors: `learning_objectives[]` built from the root registry and asserted **character
   for character** on `objective_text` and on every other field, plus `image_examples: []`. ✔
6. Id grammar: all 8 media ids match `MEDIA_ID_RE` concept-scoped with chapter-continuous `.C{c}`;
   all 24 recall ids are `{topic_id}.RQ{n}` with `legacy_id` `{topic_id}.TR{n}`; **no `.SR{n}`
   anywhere**. There are no segment-level recalls in this chapter. ✔
7. No સ્વાધ્યાય block is a topic; all 16 inventoried blocks are answered in
   `10_exercise_solutions.json`. ✔
8. Three-tier summaries strictly increase on all 8 topics. ✔
9. **No numbers in display text** — zero ASCII or Gujarati digits across every `topic_name`,
   `concept_name`, `explanation`, `real_life_example`, summary, bullet, `key_terms` entry, recall
   prompt/answer, concept content block, `objective_text`, `publication_text` and media
   title/description/teaching-note. `original_chunk`, `word_count`, ids and `textbook_pages` are
   provenance and were correctly exempt from the check. ✔
10. Media: one image per reading scene, `2d_tool: null`. ✔ (detail below)
11. `figures_of_speech` — `[]` everywhere, nothing to verify against a chunk, nothing invented. ✔
12. Every reference resolves as the plan stands; ids are frozen for Agent 14's renumber. ✔

`topic_type` is `STORY_TELLING` on all 8 topics — the pack's **authored** enum, correct for an
intermediate file per `phase2_contract.md`. It maps cleanly to the closed server enum
(`STORY_TELLING → instructional`) at Agent 14/15's emit; no `POEM`/`CONCEPT`/`REVIEW` value and no
literary genre label sits in that field.

### Exercises

`coverage_report.blocks_found` = **16**, exactly the length of `01_meta.json`'s
`exercise_inventory`, entry for entry and in printed order (matched fuzzily for the
લખો/આપો · વાક્યમાં/વાક્યોમાં · સવિસ્તર/સવિસ્તાર drift — no drift occurred here). `blocks_answered`
= 16. **`unanswered` is empty.** All 74 printed items are answered, matching the inventory's item
sum of 74 exactly; every `answer` is non-empty.

### Publication

All 8 topics carry `publication_text`. The verbatim is intact: each topic's `original_chunk` was
asserted to sit **byte-identically inside** its `publication_chunk`. `concept_publication` maps
one-to-one onto the `paragraph` blocks of `concepts[].content[]` — 42 entries across 15 concepts,
index set matched in **both** directions per concept, with `list` blocks correctly skipped and
surviving indices never renumbered; every paragraph block in the merged plan now carries a
non-empty `publication_text`. No vocative or classroom instruction survived: `બાળકો`, `જુઓ —` and
`બોલો` return zero hits in publication prose (they appear only in the teaching-voice `explanation`,
where they belong). Reading the rewrites against their teaching sources found no meaning added —
the rewrite drops the address and turns the second person impersonal, and nothing else.

---

## E–G (reported)

- **E — સ્વાધ્યાય and risk.** All 16 blocks answered and skill-tagged (vocabulary 38, writing 15,
  speaking 7, reading comprehension 7, grammar 6, values 1). 48 of 74 items are marked
  `is_model_answer` — the personal-opinion, પ્રવૃત્તિ, જૂથકાર્ય, નિબંધ, ચિત્રલેખન and
  teacher-addressed items are answered with teaching values rather than skipped, and marked as one
  possible response. 36 items carry `values_filled_for_teaching`, including the 7×6 શબ્દ-ચોરસ grid
  and the printed તત્સમ grid. 58 of 74 items are mapped to the topics that prepare them.
  **`unmapped` is reported, not emptied**: 16 items across 3 blocks (2 word-pairs in the
  વાક્યપ્રયોગ battery, 13 of the 18 તત્સમ જૂથકાર્ય words, and the ફકરા-વિભાજન block, whose two
  paragraphs come entirely from outside this chapter). No mapping was invented to close the report.
  Sensitivity notes are applied where the chapter touches ધર્મ, વિકલાંગતા and જાતિ-ભૂમિકા — flagged
  and guided, never censored; the written block asks about the father's condition directly and is
  answered with dignity.
- **F — shape and media.** The 12 invariants hold (above). `topic_type` is inside the authored enum
  with a clean mapping; recalls are `.RQ{n}`; concept numbers are chapter-continuous. `chapter_id` /
  `plan_id` follow `gseb_eng_gujarati{grade}_ch{unit_number}` — **⚠ the board and medium segments
  are provisional until VERIFY-1**. `publication_id` is `null` — see Gaps. Summaries strictly
  increase; no digits in display text. Field shapes all inside `field_shape_rules.md`: `key_terms`
  5–6 per topic (band 3–6), `concept_bullets` 4 and `important_points` 4 per topic (band 3–4),
  `recall_questions` 3 per topic (band 2–3), `difficult_words` 8/7/8 per module (band 5–10),
  `estimated_exchanges` "4"–"5".
  ⚠ The 55–90 and 12–30 word bands remain **provisional until VERIFY-4**; they were enforced
  exactly as written.
- **G — the seven usual mistakes.** None present. (1) The teaching is ઘટના + પાત્ર + વળાંક, not
  સાર + બોધ + પ્રશ્નોત્તર. (2)/(3) No verse in the chapter, so no દુહા merged and no પદ split.
  (4) Printed licence preserved, not corrected. (5) No અલંકાર named. (6) Anchors are std-7-sized
  and Indian. (7) સ્વાધ્યાય was cut as a separate deliverable, complete at 74/74.

**Agent 4's non-blocking notes, carried here as specified:**

- **No pre-reading topic exists, and none should.** This chapter's only pre-reading matter is the
  teacher-addressed blue પ્રવેશપેટી ("શિક્ષકે વિદ્યાર્થીઓ પાસે … કહેવડાવવા."), which is apparatus.
  The student-facing pre-reading CONCEPT topic is reserved for std 9–10's કવિ/લેખક-પરિચય prose,
  which this reader does not print. Cutting the blue box as a topic would itself have been the hard
  fail.
- **No REVIEW topic exists, and none should.** The chapter's closing sentence is the last sentence
  of the final ઘટના, held inside M3.S6.T8, not a separately printed wrap.
- **Uneven topic length.** M2.S4.T5 (ખુરશી નીચે પડેલી નોટ, one concept, ~287 chars) is roughly a
  third of M2.S3.T4. Agent 2 declined to merge it because the chapter's two-step — the note taken
  as an answered prayer, then re-read as somebody's loss — collapses if T5 joins either neighbour.
  Reported, not blocked.
- Seven of eight topics carry two concepts, M2.S4.T5 carries one. None reaches three.

## Media

`reuse_report`: **scenes 8, authored 8, reused 0, rejected []**. `scenes` equals the 8 topics whose
`available_content_types` carry `"image"` — verified by recount, not read off the report. Every
node carries `image_url: ""` **and** a real, self-contained `generation_prompt` (1314–1633
characters each); no node carries a `[reused frame: …]` stamp, and no fabricated URL appears
anywhere. Every `negative_prompt` carries `Devanagari script labels`. **`2d_tool: null` for the
whole chapter** — correct for a ઘરેલુ વાર્તા with no staged process.

One frame per ઘટના, hung on the concept whose moment it actually depicts:

| media id | concept | frame |
|---|---|---|
| M1.S1.T1.C2.IMG1 | C2 | પ્રાર્થનાસભામાં પડી ગયેલું મોઢું |
| M1.S2.T2.C4.IMG1 | C4 | થંભી ગયેલી કાતર |
| M1.S2.T3.C6.IMG1 | C6 | 'કાંઈ નહીં બા' |
| M2.S3.T4.C8.IMG1 | C8 | તારાના અજવાળામાં જોડાયેલા હાથ |
| M2.S4.T5.C9.IMG1 | C9 | ખુરશી નીચેની નોટ |
| M3.S5.T6.C11.IMG1 | C11 | નળ પર થંભી ગયેલી આનંદી |
| M3.S5.T7.C13.IMG1 | C13 | ડૉક્ટરના હાથમાં મુકાયેલી નોટ |
| M3.S6.T8.C14.IMG1 | C14 | પગે પાંખો આવી |

Each is a single photographable moment, not a summary of its beat. Setting is Ahmedabad because the
chapter names it (બાલારામ અમદાવાદથી બહુ દૂર તો નથી; ભદ્રના કિલ્લાની ઘડિયાળ). Character likeness is
held constant by repeating the appearance sentence in every prompt; no prompt refers to another
image or to the chapter by name. The ધર્મ frames show a child, a window and starlight — no deity,
no idol, no halo — and no frame asserts that the note was or was not sent. The spoiler gate holds
in the media layer too (checked above). The બાલારામ ઉજાણી itself is deliberately not drawn: T8's
photographable moment is the ઇનામ and the પગે પાંખો, and one image per topic is the contract.
**Rejected frames: none** — reuse is dormant in this pack, so nothing was offered to reject.

## Gaps

Honest absences, surfaced rather than closed:

1. **`publication_id` is `null`.** `upload_reference/chapter_master_map.json` is a provisional file
   in which every GSEB `chapter_master_id`, `publication_id` and `path` is still null — those rows
   live in the education DB and **must be fetched, never invented** (VERIFY-2). CBSE's `1` is not
   portable. `qc_checklist.md` places this item in §F (reported), so it does not block Agent 13 —
   but **the plan cannot be uploaded until it is filled**, because the LP2 server rejects a null
   `publication_id`. The same holds for `chapter_master_id`, which is mandatory for upload and is
   not discoverable from the LP2 API. Consistent with the ch10/ch11 precedent in this pack.
2. **`subject_ref_id` and `medium_id` are `null`** — server-injected keys; no real GSEB subject
   record is confirmed, and `null` is the only correct value until one is.
3. **`chapter_id` / `plan_id` board and medium segments are PROVISIONAL** (VERIFY-1). The medium
   slot is the medium of instruction, not the subject language, and a wrong value **uploads clean**
   and mis-files the plan. Confirm against the live server before the first upload.
4. **`textbook_url` is a local path string** (`../Textbooks-pdf/std-7/ch-12-be-rupiya.pdf`) — the
   GSEB readers have no hosted URL. Recorded by Agent 11 as a gap, not guessed at.
5. **Pagination is high-confidence, not a gap:** `textbook_pages` `77–84`, read off the printed
   folios on page-1.png and page-8.png and cross-checked against the manifest row and the std-7
   offset table (N+13); both agree.
6. **`topic_title` was authored by no agent.** The 32-root-key contract requires it and the merge
   table does not assign it. It is set to the chapter's own printed title, `બે રૂપિયા` — the same
   value `unit_title` already carries — matching the ch10/ch11 precedent in this pack. Flagged for
   Agent 1 to confirm rather than silently owned here.
7. **`topic_number` is `1`** as `01_meta.json` sets it. Across std 7, eight chapters set
   `topic_number` to the chapter number and six set it to `1`; the pack has not settled the
   convention. Taken from `01_meta.json` per the merge table and reported as a **pack-level
   inconsistency for Agent 1 / the orchestrator**, not silently normalised. Non-blocking.
8. **`ordering` is absent from `13_merged.json` by instruction** — Agent 14/15 sets it. The root
   therefore carries 31 of the contract's 32 keys, by design.
9. **Agent 1's double-render cross-check was weaker than a true second render.** The renders were
   supplied pre-rasterised at ~150 dpi and, per the run constitution, were not re-rendered; the
   second pass was a crop-and-upscale re-read (2.3×–8× LANCZOS) of the same PNGs. Words resolved
   this way: `ઊનાંઊનાં`, `ડૉક્ટર`, `ઇસ્પિતાલ`, `ઇનામ`, `ઇતિ`, `હૉસ્પિટલ`, `માંડયો`, `પડયું`,
   `કર્યુ`. Recorded as a known limitation, not as an equivalent check.
10. **A transcription formatting detail, checked and not blocked.** M1.S2.T2's `original_chunk`
    joins the chapter's two printed paragraphs (p. 78) with a single `\n`, while
    `00_chapter_normalized.md` separates them with a blank line. Both paragraphs are byte-identical
    to the transcription and the printed paragraph break is preserved; only the separator width
    differs. Reported for visibility, not a verbatim defect.
11. **A spec conflict, resolved and recorded.** `agents/13_assembly_validation.md` says
    `publication_chunk` is "byte-identical to `original_chunk`", while
    `agents/16_publication_authoring.md` — the file that owns the field — says `publication_chunk`
    is "the publication-facing version of the topic's block as a whole", with "the verbatim
    `original_chunk` … verbatim inside it". Agent 16's definition was followed and the check was run
    as **containment**: every `original_chunk` appears byte-identically inside its
    `publication_chunk`. Read literally, Agent 13's wording would fail every chapter in the pack.
    Flagged so the owning file can be fixed rather than the check quietly relaxed each run.
12. **Media nodes carry a `topic_id` key** not listed in `phase2_contract.md`'s media-node shape. It
    is Agent 9's routing key and it was kept, matching the ch10/ch11 precedent in this pack, so all
    of std 7 presents Agent 14 with the same shape. Agent 14 may drop it at emit.
13. **`unmapped` exercises stand unmapped** (item E above) — 16 items whose material comes from
    outside this chapter's reading text. Reported, never given an invented mapping.
14. **Bands and ids are provisional.** The 55–90 / 12–30 word bands (VERIFY-4) and the `chapter_id`
    board/medium segments (VERIFY-1) were enforced exactly as written; nothing was widened, softened
    or dropped to reach PASS.

## LP2 validator

_Not run — filled in Phase 8._ `POST /api/lp2/learning-plans/validate` must return zero
`validation_errors`. Note that the upload path additionally requires a non-null `publication_id`
and a real `chapter_master_id` (Gap 1), neither of which exists yet for GSEB.

---

**Verdict: A–D PASS.** All four blocking sections pass on every mechanical check, with 16 hard
avoid-checks and 1 hard sensitivity item verified as genuinely addressed rather than declared.
`13_merged.json` is written and is ready for Agent 14. The gaps above are reported absences, not
silent ones — and none of them is an A–D failure.

## LP2 validator (Phase 8 run)

`POST /api/lp2/learning-plans/validate` — HTTP 200, request succeeded on first attempt (no retry needed).

```json
{
  "success": false,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati7_ch12_v1",
  "validation_errors": [
    "root: 'publication_id' is required and must not be null"
  ],
  "message": "1 validation error(s)"
}
```

**Result: 1 validation_errors.** This matches the previously reported Gap 1 (no `publication_id` /
`chapter_master_id` exists yet for GSEB) — expected given that gap, not a new defect.
