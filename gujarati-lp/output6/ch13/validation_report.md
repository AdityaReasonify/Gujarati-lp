# Validation Report — std 6, ch 13 · સૂર્ય સુધી પહોંચાય ? (- સંકલિત)
સ્વરૂપ: varta — વાર્તા, sub-form **વાર્તા-માં-વાર્તા** (a વર્ગખંડ frame carrying an embedded પૌરાણિક કથા) (confidence: high)
explanation unit: **એક ઘટના** (varta.md) — frame ઘટના and embedded ઘટના kept as separate topics
Topics: 8   Objectives: 8   Images: 0/8   Exercises: 17/17 blocks answered
(82 solution entries against 85 inventoried items — two benign item-count deltas, explained under **E**)

**VERDICT: PASS.** Sections A–D pass with zero blocking items. `13_merged.json` is written from
`05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json` +
`11_pages.json` + `01_meta.json`; 31 root keys, 3 modules, 5 segments, 8 topics, 11 concepts,
8 media nodes, 8 inline objective mirrors, no working field carried through.

Five things are **reported and should be read before this ships** (none is an A–D failure): the
provisional `publication_id` and null `chapter_master_id` under **Gaps 1**, the root `genre` slug
under **Gaps 2**, the `05b` ordering confirmation under **Gaps 5**, the `word_count.modified`
trim under **Gaps 6**, and the publication-chunk convention note under **Publication**.

---

## A–D (blocking)   PASS

### A — Diagnosis and lens   PASS
- સ્વરૂપ diagnosed off the rendered page, with `genre_signals` and `genre_confidence: high` in
  `01_meta.json`. The blue પ્રવેશપેટી names **no** form — A1 records the absence rather than
  inventing a quote, and rests the verdict on the printed signals: named પાત્રો, a chain of ઘટના,
  dialogue inside doubled turned commas with narrator ties, and a printed વળાંક. varta.md's
  Signal C is present twice over: the chapter prints an event-ordering block
  (`નીચેનાં વાક્યોને પાઠના ઘટનાક્રમ મુજબ ગોઠવો.`) and the counterfactual
  (`ખરેખર હનુમાનજી સૂર્યને ગળી ગયા હોત તો શું થાત ?`) inside વાતચીત — both are named in varta.md's
  own std-6 ch 13 rows.
- **Not a mixed chapter.** Both layers — the classroom frame and the embedded કથા — are prose
  narrative and route to the same profile, so only `varta.md` is loaded. A1 wrote the reasoning out
  (`extraction_notes[2]`), including the near-miss test against `samvad_nibandh` (no પાત્રો box, no
  speaker-name-colon line, no રંગસૂચના) and against `natak_ekanki`.
- Explanation unit matches the roster line for વાર્તા — **one ઘટના**. Measured: **9** `[[ઘટના: …]]`
  markers in `00_chapter_normalized.md`; zero `[[કડી]]`, zero `[[દુહો]]`, zero `[[પદ]]`;
  `structure_inventory` records `kadi 0 · duha 0 · pad 0 · tek_occurrences 0`, so the કડી/દુહો/પદ/ટેક
  rules are vacuous here.
- **Nine markers → eight topics, declared, not swallowed.** M3.S5.T8 carries both
  `[[ઘટના: વાર્તા પૂરી — તાળીઓ]]` (line 48) and `[[ઘટના: ભાસ્કરભાઈનો સેતુ — ચંદ્રયાનથી સૂર્યયાન સુધી]]`
  (lines 52–54). varta.md's frame-story clause says the sentence that returns to the frame *opens*
  the closing frame topic, and `આદિત્યે વાત પૂરી કરી. ભાસ્કરભાઈ અને વિદ્યાર્થીઓએ એના માનમાં તાળીઓ
  પાડી.` is exactly that sentence. Both markers are frame-level, so the frame/embedded boundary is
  not crossed. **Checked this run:** T8's `original_chunk` carries *both* spans verbatim, in printed
  order — A4's `ACTION FOR AGENT 5` was honoured and no reading text was lost.
- **Frame and tale stay separate** (varta.md's frame-story rule, and A7's chapter-level gate). Frame
  layer: M1.S1.T1, M1.S2.T2, M2.S3.T3, M2.S4.T5, M3.S5.T8. Embedded layer: M2.S3.T4, M2.S4.T6,
  M2.S4.T7. No topic mixes the two casts; the two hand-over hinges are topics of their own
  (M2.S3.T3 ભાસ્કરભાઈ માંડે છે, M2.S4.T5 આદિત્ય હાથમાં લે છે), both `topic_category: transition`.
- ટેક: **zero** — a measured fact. No line recurs and no refrain shorthand is printed.
- Apparatus did not become a reading scene. Not cut, each with a written reason in
  `05_with_content.json`'s `not_cut_as_topics`: the blue પ્રવેશપેટી (p. 85, teacher-addressed), the
  શબ્દાર્થ box (p. 87, eighteen glosses), the unnumbered રૂઢિપ્રયોગ gloss list (p. 87), the seventeen
  numbered સ્વાધ્યાય blocks, and the chapter-final 'શબ્દોની ફેરકૂદરડી' fun box (p. 91).
- `guiding_question` is derived from this chapter and traces its own arc — મિહિરનો પ્રશ્ન → બાળ
  હનુમાનની વાર્તા → સૂર્યયાનનું સપનું — and reading the eight explanations in order answers it.
- `topic_category` runs introduction → core → transition → **climax** → transition → core →
  resolution → resolution. The climax sits on M2.S3.T4 (the reveal `ખરેખર એ ફળ નહોતું. ઊગતો સૂર્ય
  હતો.`) rather than on the loudest event (the વજ્રપ્રહાર in M2.S4.T6). That placement is A1's
  reading, A2 declared it openly and A4 accepted it non-blocking; it is free text and I have not
  moved it. See **E–G** for the field-level consequence, which was checked and is clean.

### B — Verbatim and structure   PASS
- 8/8 topics carry a non-empty `original_chunk`. **Every line of every chunk was matched against
  `00_chapter_normalized.md` character for character** (mechanical check, zero misses).
- Script: Gujarati (U+0A80–0AFF) throughout. **Zero** Roman and **zero** Devanagari characters in
  any `original_chunk`, and zero in any authored display field outside brackets. **No `।` anywhere**
  in the chapter file or in the plan — A1 records that the unit prints none and none was introduced.
- **Whitelist checked before flagging.** The one non-Gujarati item in this unit is block 14's Avadhi
  couplet from the હનુમાન ચાલીસા — `જુગ સહસ્ર જોજન પર ભાનુ, / લીલ્યો તાહિ મધુર ફલ જાનુ.` It is
  printed **in Gujarati script**, is recorded in `extraction_notes[17]`, lives in
  `10_exercise_solutions.json` (EX68) and never became a topic. No Devanagari code point appears
  anywhere in the exercise file either. The અનુવાદ block's five answers are in Roman English on
  purpose — medium of instruction — and EX78's `teacher_note` says so explicitly; that is the
  documented whitelist case, not a script failure. English `teacher_note` prose throughout the
  exercise file is mechanism prose for the teacher, not child-facing text.
- Printed oddities kept as printed, not repaired, and none called a mistake anywhere in the
  teaching: `સૂર્યગ્રહણ વિષે` beside `એના વિશે` in one speech; `લાલચટ્ટક` (body) / `લાલચટ્ટ`
  (શબ્દાર્થ) / `લાલચટ્ટાક` (exercises); `બાળ હનુમાનજી` (intro box) beside `બાલ હનુમાન` (body);
  the doubled word and double space in `ભયંકર  જાણે ભયંકર મેઘગર્જના થઈ.`; the four-dot middle
  ellipsis in `વાર્તા... વાર્તા.... વાર્તા...`; the missing opening quotation mark on the teacher's
  long speech; the unspaced `સંભળાવું!`; the `ઈ` fifth option label in block 12. A1's `વજ`→`વજ્ર`
  correction against the corpus prior was re-verified at 6× and stands.
- **તળપદી diction preserved and glossed, never standardised** (varta.md avoid #6, A7's M1.S2.T2 hard
  gate). `અલી`, `વ્હાલીડાં`, `કહેને`, `હા વળી`, `હાય હાય`, `છે...ક` are each present verbatim in
  M1.S2.T2's own `original_chunk` and are carried into `key_terms` / `concept_bullets` in the printed
  form with the gloss beside them and the words **`ભૂલ નથી`** stated. Mechanical check: every
  quotation inside every `explanation`, summary, bullet and recall field was matched against its own
  topic's `original_chunk` — three strings did not match and all three were inspected and cleared
  (`બેસ હવે` and `ચલાવ, ચલાવ !` are speech invented *inside* the authored real-life anchors, not
  claimed quotations; `કહો ને` is the gloss printed *after* the headword `કહેને`, which is the
  permitted shape, not a swap).
- Header furniture kept out: the `13` number box, the QR badge and its Latin code string, the
  running folios 85–91.
- Marker accounting: ઘટના 9 · સ્વાધ્યાય 17 · topics 8. **No `[[સ્વાધ્યાય: …]]` block became a topic**
  — mechanically confirmed by testing every printed સ્વાધ્યાય heading against every topic chunk
  (zero hits); all 17 live in `10_exercise_solutions.json` alone.
- Ids match traversal position exactly: M1→M3, S1→S5, T1→T8, concepts C1…C11 chapter-continuous.
  `word_count.original` equals the whitespace-token count of each chunk on all eight
  (100 / 193 / 74 / 86 / 29 / 168 / 100 / 91).

### C — The teaching block   PASS
- 8/8 topics carry non-empty `explanation` **and** `real_life_example`; all summaries, bullets,
  points and recall answers non-empty.
- Bands, measured on the merged file: `explanation` **73 / 76 / 80 / 85 / 72 / 79 / 74 / 77**;
  `real_life_example` **64 / 63 / 57 / 68 / 61 / 61 / 69 / 66` — all inside 55–90.
  `objective_text` **20 / 22 / 19 / 23 / 18 / 21 / 18 / 19** — all inside 12–30. Nothing was
  widened; nothing needed trimming.
- Three-tier summaries strictly increase on every topic (23<66<111, 20<86<145, 21<77<120,
  22<67<95, 21<45<84, 21<75<140, 23<75<110, 22<68<108).
- L2 calibration held. The glossed set is the words an L2 std-6 child actually stops on, not a
  તત્સમ list: પ્રાર્થનાસભા, હરોળ, અંતરિક્ષયાન, દલીલ, નારાજગી, સહર્ષ, જંપવું, મનસૂબો, ગોળમટોળ,
  લાલચટ્ટક, એક્કા, ગ્રહણકાળ, શિક્ષા, વજ્ર, મેઘગર્જના, બેહોશ, સૃષ્ટિ, ગૂંગળાવું, હાહાકાર, રીસ,
  વરદાન, હડપચી, માન, કૃપા — each glossed in Gujarati **at the point of first use** as well as in
  `key_terms`. The three printed રૂઢિપ્રયોગ are glossed where they are quoted (`મોંમાં પાણી આવવું`,
  `સૂર પુરાવવો` — with `ગાવાની વાત નથી` stated, `એક કાન થઈ જવું`). `શિક્ષા` is glossed explicitly as
  **સજા, ભણતર નહિ** — the false friend an L2 child reads as "education". `key_terms` run 4–6 per
  topic, inside the 3–6 band; `difficult_words` run 8 / 9 / 7 per module, inside 5–10.
- `real_life_example` is Indian, concrete, single and inside std-6 reach in all eight: a દાદી telling
  sky-stories on an આંગણાનો ખાટલો, નવરાત્રિ દાંડિયા in the ફળિયું, an ઈદની સવાર waiting for સેવૈયા,
  a પાકી કેરી on the શેઢાની આંબાની ડાળ walking home hungry, learning to ride a cycle, an ઉત્તરાયણ
  પતંગનો પેચ, a household gone quiet round a sister's fever, and the ગામનાં નામ board at an એસ.ટી.
  ડેપો. Each is one anchor, each ends on a question to the child, and none needs its own glossary.
  Two carry a second community's occasion by name (ઈદ, and the ઉત્તરાયણ/નવરાત્રિ pair) — no invented
  claim is made about either.
- Craft ceiling for std 6 held absolutely: a sweep for અલંકાર · છંદ · ઉપમા · રૂપક · સજીવારોપણ ·
  અનુપ્રાસ · યમક · શ્લેષ · સમાસ · સાહિત્યપ્રકાર · **પ્રાસ** · કેન્દ્રવર્તી/મધ્યવર્તી across every
  child-facing field returns **zero hits**. Where craft is taught it is taught as a thing to notice,
  not a thing to name — M2.S3.T4's `explanation` says the writer shows the hunger before the object
  and keeps the fruit's identity back for two short closing sentences, without ever labelling the
  technique.

### D — સ્વરૂપ essence   PASS
All **19** `severity: "hard"` items in `07_pitfalls.json`, the one `severity: "hard"` item in
`08_sensitivity.json` (M1.S1.T1, area ધર્મ), the four chapter-level pitfall notes and the one
chapter-level sensitivity note were each checked against the merged text. `08`'s `areas[]` are all
`ધર્મ`, matched as strings against the fixed seven.

- **varta gate 1 (summary-only teaching)** — every `explanation` carries something its
  `modified_chunk` does not. T1 names *who is speaking and where she got it* (`એ પોતે જ કહે છે,
  ‘મારા દાદા કહેતા હતા’`), which is the whole point of the beat; T2 names the discussion as
  સામસામી and quotes the chapter's own verdict on it (સાહેબને આનંદ થાય છે) instead of judging any
  child; T3 names the teacher's own aside about તોફાન as *his* words; T4 names the writer's order —
  ભૂખ first, object second, identity last — so the reader looks at the sun with હનુમાનની ભૂખી નજર;
  T5 names the hand-over of the teller and that ભાસ્કરભાઈ **gives way** rather than merely agreeing;
  T6 supplies the motive A7 asked for (`બંને એક જ સૂર્ય તરફ જાય છે`) and ઇન્દ્રનું છંછેડાવું in his
  own printed words; T7 names the એટલે/તો જ causal chain and draws the conclusion A7 specified —
  **`એટલે વરદાન દયામાંથી નહિ, આ શરતમાંથી આવે છે`**; T8 names the placement move (કથાની વાત ને આજની
  વાત, પાસે પાસે).
- **varta gate 2 (a tacked-on બોધ)** — a sweep for `આ વાર્તા આપણને શીખવે`, `બોધ એ છે`,
  `આપણે પણ`, `શીખવે છે`, `સંદેશ એ છે` and a blanket search for **જોઈએ** across every child-facing
  field of every topic returns **zero hits**. The chapter's own printed moral —
  `‘ભાઈ! તોફાન તો ન જ કરાય ને !’` — is quoted inside quotation marks and attributed to ભાસ્કરભાઈ in
  M2.S3.T3, exactly as A7's hard check requires, and no field adds one on top of it. T8's
  `‘‘તમારામાંથી જ ભવિષ્યમાં કોઈક સૂર્યયાન બનાવીને સૂર્ય સુધી પણ પહોંચી શકશે.’’` stays inside
  quotation marks and attributed to ભાસ્કરભાઈ in every field that carries it — `explanation`,
  `important_points`, both concept blocks and both publication texts — and is never re-issued to the
  reader as advice. The thanks to મિહિર is likewise reported, never converted into a rule about
  asking questions.
- **varta gate 3 (judging a sympathetic character)** — a sweep for અંધશ્રદ્ધા · ભોળી · અજ્ઞાન ·
  મૂરખ · ગુનેગાર · લોભી · ખાઉધરો · જિદ્દ · ઉદ્ધત · ગાંડો · ખોટું વર્તન · દોષ across every field of
  every topic returns **zero hits**. સવિતા and her દાદા, મિહિરની printed `થોડીક નારાજગી`, ઉષાનું
  `‘‘એકવાર હનુમાનદાદા પણ આખો સૂર્ય ગળી ગયા હતા’’`, પ્રભાનું `‘‘એમ ના હોય’’` and નાનકડા હનુમાનની
  ભૂખ are each described only by what the page shows them doing.
- **varta gate 4 (spoiling the turn early)** — run token by token. `ફળ નહોતું`, `ઊગતો સૂર્ય`,
  `વજ્ર`, `બેહોશ`, `હડપચી`, `વરદાન`, `ઇન્દ્ર`, `પવનદેવ`, `મનસૂબો`, `ગોળમટોળ`, `લાલચટ્ટ`,
  `સૂર્યલોક`, `ચંદ્રયાન`, `સૂર્યયાન` are **absent from every gated field of M1.S1.T1, M1.S2.T2 and
  M2.S3.T3** (zero hits). A7's stricter T3 list (ફળ · સૂર્ય · રાહુ · ઇન્દ્ર · વજ્ર · વરદાન ·
  હડપચી) also returns **zero hits**. A4's extra instruction — that T4–T5 must not pre-empt the
  T6–T7 outcome — was run separately and also returns **zero hits**. The one place the outcome
  appears early is ઉષાનું printed frame line, quoted from M1.S2.T2's *own* `original_chunk`, which
  A7 names explicitly as not a breach: the tale's ending is not the protected reveal; the
  ફળ↔સૂર્ય identity is, and it appears nowhere before M2.S3.T4.
- **varta gate 5 (no debunking a પૌરાણિક કથા)** — the chapter's defining risk, and the reason the
  sensitivity file exists. A sweep for `ખરેખર એવું ન બને`, `વૈજ્ઞાનિક રીતે`, `આ તો કલ્પના`,
  `સાબિત`, `માન્યતા ખોટી`, `સાચું તો વિજ્ઞાન`, `હકીકતમાં` across every field returns **zero hits**.
  Nothing confirms the tale either. સવિતાના દાદાની વાત is taught as reported speech and left there;
  the `સૂર્યગ્રહણ` gloss in `key_terms` is a dictionary meaning, which A7 states in advance is not a
  breach. M3.S5.T8 sets the two sentences side by side in the chapter's own printed order and lets
  neither cancel the other — `કથાની વાત ને આજની વાત — સાહેબ બંનેને એક પછી એક, પાસે પાસે મૂકે છે.`
  No theology is added anywhere; the frame's people and the tale's people are never mixed.
- **varta gate 6 (dialect)** — see **B**. Every colloquial form is printed as printed, glossed, and
  marked `ભૂલ નથી`.
- **Soft item, honoured** — the doubled `ભયંકર  જાણે ભયંકર મેઘગર્જના થઈ.` line is never quoted in a
  mended form: the three fields that touch that moment paraphrase it without quotation marks
  (`મેઘગર્જના જેવો ભયંકર અવાજ થયો`), which is the alternative A7 permits, and no field calls the
  line a misprint or supplies a missing word.
- **`figures_of_speech`** — `[]` on all eight topics, and `rhyme_scheme` `null` on all eight. That is
  the correct and complete answer for a prose chapter at std 6, not an extraction gap. Invariant 11
  is therefore vacuously satisfied, and no device was named because the field existed.

## Contract (the 12 invariants)   PASS
`phase: 2` · `chapter_id: gseb_eng_gujarati6_ch13` · `plan_id: gseb_eng_gujarati6_ch13_v1` —
derivation re-checked from `grade` and `unit_number`, not assumed. Every topic has ≥1 concept with a
resolving `objective_id` and non-empty `content[]`; eight unique objectives, every `home_topic_id`
and every `anchor[]` id resolves, `strand_to_objective_map` covers L1–L8 both ways, every topic's
`objective_ids` and every `depends_on` resolves. Inline `learning_objectives[]` match the root
registry **character for character** on all eight, each carrying `image_examples: []`. Media ids
match `MEDIA_ID_RE`, concept-scoped, with chapter-continuous `.C{c}`. Recall ids are
`{topic_id}.RQ{n}` with `legacy_id` `{topic_id}.TR{n}` — **zero `.SR{n}`** — and `bloom_level` is
lowercase there and Capitalised in `objectives[]`, the asymmetry kept. `publication_id` non-null.
`topic_type` is the **authored** enum (`STORY_TELLING` ×8) as intermediate files carry it; Agents
14/15 map it to `instructional` at emit. Summaries strictly increase at topic level. Concepts run
C1…C11 chapter-continuous, so from C3 on the concept number no longer equals the topic number — that
is the contract's behaviour on the three two-concept topics (T2, T6, T8). **No digits in display
text** — a sweep of Latin and Gujarati numerals across every name, explanation, example, summary,
bullet, point, key term, recall prompt/answer, concept name, concept content, publication text and
media title/description/teaching-note returns **zero hits**; numerals survive only in ids,
`word_count`, `textbook_pages` and the aspect-ratio token inside `generation_prompt`, which is an
image-model instruction, not display text.

## E–G (reported)
- **E — સ્વાધ્યાય.** 17 inventoried blocks, 17 found, 17 answered, `unanswered: []`; 82 solution
  entries against 85 inventoried items. Headings match the inventory on all 17 under fuzzy match.
  Two item-count deltas, both benign and both explained: block 1 (વાતચીત) has 8 numbered prompts but
  **9** answers, because A10 also answered the standing unnumbered closing bullet A1 deliberately
  left out of the item count — more answered than inventoried is not a gap; block 9
  (`ઉદાહરણ મુજબના બીજા પાંચ શબ્દો લખો.`) is inventoried as 5 items and answered as **one** entry
  supplying all five words plus five alternatives, which is the right shape for an open list block.
  23 entries carry `is_model_answer: true` with stated alternatives — the personal-opinion,
  પ્રવૃત્તિ, જૂથકાર્ય, library-research and oral-game blocks are answered with teaching values, not
  skipped. Every `covered_by_topics` id resolves to a real topic. `unmapped: 3` (EX58 પ્રકાશ; EX69–72
  / EX74–75 the -ઇક derivation drill; EX80 the sea-crossing translation sentence) — each carries a
  written reason that the block's own material appears nowhere in this chapter's reading text.
  **Reported as unmapped; no mapping was invented to empty the field.** In particular EX80's reason
  is the right one and worth keeping: the sentence narrates an event this chapter's કથા does not
  contain, and inventing a mapping there would have breached varta.md avoid #7.
  Sensitivity notes applied where flagged (ધર્મ on T1, T3, T6, T7) — flagged and guided, never
  censored.
- **F — Shape and media.** All twelve invariants above hold. One image per reading scene, eight
  scenes, eight authored prompts, zero reuse. `chapter_id` / `plan_id` follow
  `naming_conventions.md` with medium `eng`; ⚠ the board and medium segments are **provisional
  until VERIFY-1** — a wrong medium uploads clean and mis-files the plan.
- **G — the seven usual mistakes.** None present. (1) The plan teaches the સ્વરૂપ — ઘટના, પાત્ર,
  વળાંક and the frame/tale layering — not સાર+બોધ+પ્રશ્નોત્તર. (2) N/A — no દુહા page. (3) N/A —
  no પદ, no ટેક. (4) No poetic or printed licence corrected — see **B**. (5)
  `figures_of_speech: []` everywhere. (6) Every anchor is std-6, Indian and single. (7) All 17
  સ્વાધ્યાય blocks are in the exercise deliverable and none was cut as a topic.
- **Style note, reported only.** All eight `explanation` fields open with the same three-word
  teacher vocative `બાળકો, જુઓ —`. It is the pack's established opener (ch 11 does the same) and
  publication strips it cleanly, so nothing here is wrong; it is recorded because eight identical
  openings in one chapter is a monotony a later editorial pass may want to vary. Not an A–D item and
  **not** something for A12 to redo on my say-so.

## Media
`reuse_report`: **scenes 8 · authored 8 · reused 0 · rejected 0**, and `scenes` equals the eight
topics whose `available_content_types` carry `"image"`. Every node has `image_url: ""` **and** a
long, self-contained `generation_prompt` (1315–1767 chars); zero `[reused frame: …]` stamps; every
`negative_prompt` carries `Devanagari script labels`. Every prompt names an exact Gujarati narrator
string in Gujarati script. `2d_tool` is `null` for the chapter — **zero** interactive tools, inside
the ≤1 limit. Nothing to report as rejected.

varta.md's frame-story media prior is honoured and is visible at a glance: the five frame images are
classroom interiors (a raised hand in the third row, a class arguing across the desks, the teacher
starting the tale, a pupil standing up mid-story, applause) and the three embedded-tale images are
sky and world (the red-round something seen far off, હનુમાન and રાહુ converging on one sun, a world
with its air stopped). A child can tell which layer they are looking at. Each is a single
photographable moment, not a summary — the depiction test passes on all eight. The routing field
`topic_id` that `09_media.json` carries on each node is a working field and was dropped at merge, as
the contract's media node has no such key.

## Publication
8/8 topics carry `publication_text`; 30 content blocks across the 11 concepts, of which **23**
are `paragraph` and 7 are `list`; **23** matching `concept_publication` entries, matched by index and by count, none renumbered, reordered or
dropped, and no `list` block wrongly carries one. A word-level diff of every `explanation` against
its `publication_text` shows **only** deletions and de-imperativisation: `બાળકો, જુઓ —` removed
eight times; `તમારી પડખે` → `વર્ગનાં બાળકોની પડખે`; `સાંભળવાની છે` → `સંભળાય છે`;
`સાંકળ ધ્યાનથી પકડો.` → `આ ભાગ એક સાંકળ છે.` **No meaning was added anywhere.** A sweep for the
vocative `બાળકો`, `જુઓ —` and `બોલો` across every publication field returns eight `બાળકો` hits, and
all eight were inspected: every one is a third-person narrative noun (`વર્ગનાં બાળકોની`,
`બીજાં ત્રણ-ચાર બાળકોએ`, `બધાં બાળકોએ`) or sits inside the printed `original_chunk` carried within
`publication_chunk`. **No vocative survived.**

**Convention note, reported not blocking.** `13_assembly_validation.md` describes `publication_chunk`
as "byte-identical to `original_chunk`". `16_publication_authoring.md` — the agent that owns the
field — defines it as the publication-facing version of the whole topic block, with the verbatim
`original_chunk` kept verbatim inside it, and A16 built it to its own spec. The gate that actually
matters was therefore run as containment, and it passes: **each topic's `original_chunk` occurs
byte-identically inside its `publication_chunk`** on all eight — no reflow, no re-spacing, no
re-punctuation, the doubled turned commas, the four-dot ellipsis and the double space in `ભયંકર
 જાણે` all intact. The two spec files should be reconciled; nothing here needs re-authoring. This
is the same finding ch 11 recorded, unchanged.

## Gaps
1. **Ids that are placeholders, not facts.** `publication_id: 1` is **PROVISIONAL** — it is CBSE's
   publication row, `phase2_contract.md` says plainly it does not transfer, and the GSEB row must be
   fetched (**VERIFY-2**) before the first Phase 8 run. It is written as `1` only because the server
   rejects `null` and every sibling chapter in `output6/` carries the same placeholder.
   `chapter_master_id: null` and `subject_ref_id: null` / `medium_id: null` — no GSEB record is
   confirmed, and nothing was copied from the Hindi pack or derived by arithmetic (the Hindi
   `355 − chapter number` pattern is CBSE provenance and was **not** applied).
   `chapter_master_id` is **mandatory for upload**, so this chapter cannot ship until VERIFY-2
   lands. Not an A–D failure; a hard stop before upload.
2. **Root `genre`.** `01_meta.json` writes `genre` as the Gujarati word `વાર્તા`;
   `phase2_contract.md` wants a roster **slug**. The merged plan carries the slug **`varta`** — the
   value `05_with_content.json` already holds, not a new one — and the Gujarati word stays in
   `01_meta.json` where A1 wrote it. **Owner A1** if the Gujarati form is meant to be authoritative.
   The `output6/` siblings are still split on this (ch01/ch07/ch08/ch10 slug, ch02/ch05/ch06/ch09/
   ch13 Gujarati); it is worth one decision for the whole pack rather than a per-chapter judgement.
3. **`textbook_url` is a local path** — `../Textbooks-pdf/std-6/ch-13-surya-sudhi-pahonchay.pdf`.
   The GSEB readers have no hosted URL. `11_pages.json` records this honestly and it is carried
   through unchanged. `textbook_pages: "85–91"` at **high** confidence: the printed folio boxes read
   85 on render page 1 and 91 on render page 7.
4. **`textbook` string.** `ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 6` with a comma, per A1's cover reading;
   `phase2_contract.md`'s example writes a `|`. Every sibling chapter in `output6/` uses the comma
   form, so this is consistent within the pack — flagged only so the divergence from the contract's
   example is not later mistaken for drift.
5. **`05b_textbook_order.json` matches the logical traversal exactly** (T1…T8 in printed order,
   `matches_logical_order: true`). Per `phase2_contract.md` §Ordering this must be raised for human
   confirmation rather than silently emitted as a second ordering:
   `{"human_confirmation_required": true, "reason": "textbook order is identical to logical order",
   "checked": "05b_textbook_order.json matches the logical traversal exactly"}`.
   A05b's own note that M3.S5.T8 spans two printed stretches and occupies one slot at the position
   of its first span is correct and consistent with the A-section marker accounting.
6. **`word_count` was normalised at merge.** `05_with_content.json` carries
   `{"original": n, "modified": m}`; `field_shape_rules.md` and the accepted sibling shape define
   the field as `{"original": <int>}`, so the merged plan carries `original` only and `modified` was
   dropped as a working sub-key. The `original` value was independently re-computed from each
   `original_chunk` and matches on all eight — nothing was taken on trust.
7. **`ordering` is absent from `13_merged.json`** by design — it belongs to Agents 14/15, so the
   merged plan has 31 root keys, not 32. `topic_title` is set to `chapter_name`; `01_meta.json`
   carries no `topic_title` of its own and every sibling chapter resolves it the same way.
8. **A4's `notes[]`, carried here and not blocking.** (a) Nine markers → eight topics, resolved
   under **A** and re-verified against T8's chunk. (b) The climax placement on M2.S3.T4 rather than
   on the વજ્રપ્રહાર in M2.S4.T6 — A4 asked Agents 7/12/13 to make sure the field-level consequence
   is clean, and it is: the pre-climax spoiler sweep and the T4–T5 pre-emption sweep both return
   zero. (c) `topic_type: STORY_TELLING` on all eight, mapped to `instructional` by Agents 14/15 at
   emit. (d) M2.S3.T4 carries `depends_on: []` although it continues M2.S3.T3 — `[]` is the correct
   default and only real dependence is recorded. (e) Three two-concept topics (T2, T6, T8), each a
   genuinely separable pair. (f) A4 opened no page render; nor did I — see below.
9. **Uneven topic lengths, reported not blocking.** `original_chunk` runs from 29 words (M2.S4.T5,
   the hand-over — a request and a yes) to 193 (M1.S2.T2). Both extremes are right: the hand-over is
   a printed hinge that varta.md's frame-story clause makes a topic in its own right, and splitting
   the argument scene would cut the સામસામી exchange that is the beat. M2.S4.T5 carries two recall
   questions rather than three, which is inside the 2–3 band and appropriate to its size.
10. **No page render was opened this run.** `00_chapter_normalized.md` answered every question this
    gate asked — marker counts and positions, line spans, chunk-to-source matching, script and
    punctuation, quoted-fragment provenance. Nothing about layout or a figure came up that the
    transcription could not settle, so per the run context no PNG was read. A1's and A5's own
    render-level readings (the 6×–10× glyph checks on `હું`, `વજ્ર`, `લાલચટ્ટક`, `વિષે`/`વિશે`,
    `બાળ`/`બાલ`) are recorded in `extraction_notes[]` and were taken as given, not re-litigated.

## LP2 validator
Not run — Phase 8. `POST /api/lp2/learning-plans/validate` must return zero `validation_errors`
before anything ships, and **must not be attempted until VERIFY-2 supplies the real GSEB
`publication_id` and `chapter_master_id`** (Gaps 1). Staging DNS is flaky; retry two or three times
before believing a failure.

## LP2 validator
- Endpoint: POST /agentapi/api/lp2/learning-plans/validate (staging), file=learning_plan_logical.json
- HTTP status: 200
- plan_id: gseb_eng_gujarati6_ch13_v1
- validation_errors: [] (none)
- message: Valid
- Result: PASS
