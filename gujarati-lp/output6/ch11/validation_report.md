# Validation Report — std 6, ch 11 · કામની મજા ને મજાનું કામ (- સંકલિત)
સ્વરૂપ: varta — વાર્તા (ઘરેલુ, સંવાદપ્રધાન), અંતે પાત્રોએ ભેગાં મળીને રચેલી કવિતા (confidence: high)
explanation unit: એક ઘટના (varta.md); the chapter-final family-made poem is ONE topic, never re-cut કડી-wise
Topics: 6   Objectives: 6   Images: 0/6   Exercises: 18/18

**VERDICT: PASS.** Sections A–D pass with zero blocking items. `13_merged.json` is written from
`05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json` +
`11_pages.json` + `01_meta.json`; 31 root keys, 6 topics, 8 concepts, 6 media nodes, no working
field carried through.

Four things are **reported and should be read before this ships** (none is an A–D failure): the
આઇસક્રીમ transcription dispute settled under **Gaps 1**, the root `genre` value under **Gaps 2**,
the provisional `publication_id` / null `chapter_master_id` under **Gaps 3**, and the
publication-chunk convention note under **Publication**.

---

## A–D (blocking)   PASS

### A — Diagnosis and lens   PASS
- સ્વરૂપ diagnosed off the rendered page with all four signals recorded in `01_meta.json`
  (`genre_signals.structure / theme / exercises / purpose`) and `genre_confidence: high`. The blue
  પ્રવેશપેટી names **no** form — A1 records that absence explicitly rather than inventing a quote,
  and rests the verdict on the signals. The drop-the-frame test against `mahitiprad_gadya.md` (the
  tea-making detail) and against a સંવાદ reading is written out in `extraction_notes[5]–[8]`,
  including the one weakness (no ઘટના-ક્રમ block, no counterfactual block printed here).
- Explanation unit matches the roster line for વાર્તા — **one ઘટના**. Measured: 6 `[[ઘટના: …]]`
  markers in `00_chapter_normalized.md` → 6 topics, one-to-one; zero `[[કડી]]`, zero `[[દુહો]]`,
  zero `[[પદ]]`; `structure_inventory` records `kadi 0 · duha 0 · pad 0 · ghatna 6 ·
  tek_occurrences 0`.
- Mixed-chapter clause examined and **deliberately not applied** — recorded, not silent
  (`extraction_notes[6]`). Both profiles are loaded and each part is cut under its own unit:
  `varta.md` governs all six topics; the `urmikavya_geet.md` gates bind **only** M2.S4.T6, the
  eleven printed verse lines with coloured speaker labels. The poem prints no કડી division and no
  ટેક, so the "one કડી" rule resolves to "the whole poem is one unit" — and it is never cut between
  speaker turns.
- ટેક: **zero** — a measured fact, not an empty box. No line recurs, no ellipsis refrain shorthand
  is printed.
- Apparatus did not become a reading scene. Not cut, each with a reason on file: the blue
  પ્રવેશપેટી (teacher-addressed), the શબ્દાર્થ box (p. 73), the eighteen numbered સ્વાધ્યાય blocks,
  the dotted ચર્ચા-વિચારણા instruction under વાતચીત, and the chapter-final ‘ભજિયાં’ writing box.
- `guiding_question` is derived from this chapter and quotes its own two poles — ‘મારે શું કરવાનું
  છે હીર ?’ → ‘ઘરનું કામ સાથે મળીને કરવાની કેવી મજા આવે છે નહીં ?’ — and reading the six
  explanations in order answers it.
- `topic_category` runs introduction → core → core → climax (M2.S3.T4) → resolution → resolution.
  Two resolutions under one climax: free text, and the page genuinely resolves twice (પપ્પા joining
  the cooking, then the three composing the poem). Recorded by A4, not a block.

### B — Verbatim and structure   PASS
- 6/6 topics carry a non-empty `original_chunk`. **Every line of every chunk matched a line of
  `00_chapter_normalized.md` character for character** (mechanical check, zero misses).
- Script: Gujarati (U+0A80–0AFF) throughout. **Zero** Roman and **zero** Devanagari characters in
  any `original_chunk`, and zero in any authored display field outside brackets. **No `।`
  anywhere** — A1 records that the unit prints none and none was introduced.
- The one Devanagari scare in this chapter is a measured false positive already on file: the
  thirteenth block's heading word `નામ` read as `नाम` at 150 dpi and resolved to Gujarati at
  300 dpi (`extraction_notes[1]`, clause અ). No whitelist case (std-8 P4, std-9 V2–V4, std-9 ch 9,
  std-10 ch 11 / ch 7) applies here — this chapter prints no non-Gujarati content at all.
- Printed oddities kept as printed, not repaired: the closing quotation mark set after the
  narrator's clause on p. 70 (`‘‘આ રીતે વળાતું હશે ! એને કહ્યું.’’`), ઓમ's unquoted
  `ચોક્કસ મદદ કરીશ !` on p. 68, the spaced `?` / `!`, the two poem lines that end without a full
  stop (`…બેનબા દાળ વઘારે`, `…હસતાં માણી લઈએ`), the colloquial `કરતો’તો`, and `ફૂ..`.
- Verse handled as verse: eleven lines, ten speaker turns, the speaker names `ઓમ  :` / `પપ્પા :` /
  `હીરવા:` and their spacing intact, ઓમ's first turn's second line indented as printed, no line
  reflowed into a paragraph. The two-column tail of p. 68 was read **down each column**.
- No attribution line is attached to any chunk — the chapter prints only `- સંકલિત` in the
  title band and the poem has no author box. A blank author is the correct answer here
  (`no_hallucination_policy.md`); nothing was invented to fill it.
- Header furniture kept out: the `11` number box, the QR badge and its Latin code `F7U5P9`, the
  running folios.
- Marker accounting: ઘટના 6 · કવિતા 1 · સ્વાધ્યાય 18 · topics 6. M2.S4.T6 carries **two** markers
  (`[[ઘટના: બધાં ભેગાં મળીને કવિતા રચે છે]]` + `[[કવિતા: …]]`) because the second is printed
  immediately under the first and the whole ઘટના *is* that poem plus its three closing prose lines.
  No marker was swallowed and no marker-less topic was created. **No `[[સ્વાધ્યાય: …]]` block became
  a topic** — all 18 live in `10_exercise_solutions.json` alone.
- Ids match traversal position exactly: M1.S1.T1 → M2.S4.T6, segments S1…S4 chapter-continuous,
  concepts C1…C8 chapter-continuous. `word_count.original` equals the whitespace-token count of
  each chunk on all six topics (171 / 214 / 244 / 528 / 112 / 128).

### C — The teaching block   PASS
- 6/6 topics carry non-empty `explanation` **and** `real_life_example`; all summaries, bullets,
  points and recalls non-empty.
- Bands, measured on the merged file: `explanation` **78 / 78 / 78 / 89 / 86 / 83**;
  `real_life_example` **59 / 58 / 59 / 61 / 64 / 63** — all inside 55–90. `objective_text`
  **20 / 23 / 20 / 20 / 17 / 23** — all inside 12–30. Nothing was widened; nothing needed trimming.
- Three-tier summaries strictly increase on every topic (16<47<101, 16<57<99, 18<47<121,
  17<64<134, 14<54<116, 19<56<139).
- L2 calibration held. The glossed set is the household-object vocabulary an L2 child actually
  stops on, not the તત્સમ list: ચોકડી, તબડકું, ઘોડો, પાટલી, ઠેસી, તિખારો, ખાંડણી, ગળણી, ઊભરો, ફરસ,
  સાવરણી, બંદા, બેનબા, ભાઈલો — each glossed in Gujarati at first use, and the idiom
  `પાણીમાં બેસી જવું` glossed where it is quoted, with the literal reading explicitly refused
  (‘ઓમ ખરેખર પાણીમાં બેઠો નથી’). `key_terms` run 5–6 per topic, inside the 3–6 band.
- `real_life_example` is Indian, concrete, single and inside std-6 reach in all six: the ડેરી milk
  errand, the guest-night pile of વાસણ, a street-cricket ball in the gutter, the ઉત્તરાયણ roof and
  ફિરકી, a classroom ભીંતપત્ર, a શેરી ગરબો. Two carry a second community's child by name — ઇકબાલ,
  પરવીન — both lifted from this chapter's own printed સ્વાધ્યાય sentences, so the spread costs no
  invented claim.
- Craft ceiling for std 6 held absolutely: a sweep for અલંકાર · છંદ · ઉપમા · રૂપક · સજીવારોપણ ·
  અનુપ્રાસ · યમક · શ્લેષ · સમાસ · સાહિત્યપ્રકાર · **પ્રાસ** · કેન્દ્રવર્તી/મધ્યવર્તી વિચાર across
  every child-facing field returns **zero hits**. The poem's returning end-sound is taught as a
  sound to hear — ‘લઈએ, દઈએ, કહીએ, કરીએ… એકસરખો અવાજ પાછો આવે છે’ — and never named.

### D — સ્વરૂપ essence   PASS
All 27 `severity: "hard"` items across `07_pitfalls.json` (26) and `08_sensitivity.json` (1) were
checked against the merged text, and the seven chapter-level notes with them.

- **varta gate 1 (summary-only teaching)** — every `explanation` carries something its
  `modified_chunk` does not: T1 identifies the two unspoken narrator lines after `તો મમ્મી હસવા
  લાગી.` and ties them to મમ્મીની શરત; T2 walks ઓમના મનની ગતિ in the page's own order
  (અણગમો → કંટાળો → ‘થોડીક ફાવટ આવી ગઈ !’ → ‘ઓમને હાશ થઈ !’) beside હીરવાની ક્રમબદ્ધ રીત;
  T3 names the *cause* of ‘‘લાવ સાવરણી !’’ — હીરવાનું મહેણું; T4 carries the turn together with the
  private doubt (`મનમાં તો એમ થયું કે ચા કોઈ દિવસ આપણે બનાવી તો નથી !`) and points back at
  `મારે શું કરવાનું છે હીર ?`; T5 separates the praise of the **પ્રયાસ** from the tea that had gone
  ભૂખરી and been corrected twice, and carries પપ્પા joining the work; T6 names the turn-by-turn
  composition and shows the lines pointing back at the day's own events.
- **varta gate 2 (a tacked-on બોધ)** — a sweep for the sixteen named slogan shapes
  (`આપણે પણ ઘરકામમાં મદદ કરવી જોઈએ`, `ભાઈ-બહેને ઝઘડવું ન જોઈએ`, `ભૂલમાંથી શીખવું જોઈએ`,
  `સૌએ ઘરકામ વહેંચીને કરવું જોઈએ`, `આ વાર્તા આપણને શીખવે છે…` and the rest) returns **zero hits**;
  so does a blanket search for the word **જોઈએ** in any child-facing field. A 6-word-run comparison
  between the blue પ્રવેશપેટી and every authored field returns **zero shared runs** — the box's
  sentences did not leak into the teaching, which A7 named as this chapter's single largest risk.
  T3 closes on the laugh, T6 leaves હીરવાનો પ્રશ્ન a question and says so outright
  (‘એ પ્રશ્ન છે, નિયમ નથી; પાઠ એનો જવાબ છાપતો નથી’).
- **varta gate 3 (judging a sympathetic character)** — a sweep for આળસુ · નકામો · નફ્ફટ ·
  બેજવાબદાર · જિદ્દી · ઝઘડાળુ · દાદાગીરી · મૂરખ · બેદરકાર · ઉતાવળિયો · ખરાબ છોકરો/ભાઈ across every
  field of every topic returns **zero hits**. The page's own words about ઓમ are quoted and left as
  the page's.
- **varta gate 4 (spoiling the turn early)** — the per-topic forbidden lists were run token by
  token against T1, T2 and T3. Zero real hits: `ચા`, `આદુ`, `ખાંડણી`, `વખાણવાલાયક`, `કવિતા`,
  `આઇસક્રીમ`, `ઠેસી`, `દૂધ` are absent from the gated fields of every pre-climax topic. Five
  substring matches surfaced and all five are the letters ચા inside `ચાલે` / `ચાવી` / `ચાલો` —
  not the drink. A12's own deliberate flag (`દૂધ` in **T1**'s anchor, where T1's list does not name
  it and nothing about the climax is disclosed) is confirmed as correctly reasoned.
- **urmikavya_geet gates on M2.S4.T6** — the first sentence of `explanation` names what can be
  seen and done using the poem's own printed words (`કચરો, પોતું, વાસણ, કપડાં, શાક ને દાળ`), not
  વહેંચણી or સંપ; one sentence carries the line-end sound with no label attached; the printed forms
  બેનબા · ભાઈલો · વઢી · સમારે · વઘારે · ધૂએ · ‘બોર થાતી’ · ‘કાચી-પાકી રોટી’ are all present verbatim
  in the chunk and are explained as the family's own words with `એને સુધારવાના નથી` stated;
  the turns are referred to as ઓમની પહેલી વારી / પપ્પાની પંક્તિ / છેલ્લી પંક્તિ — no numbered
  reference anywhere.
- **`figures_of_speech`** — `[]` on all six topics. That is the correct and complete answer at
  std 6, not an extraction gap, and it is stated as such in A12's notes. `rhyme_scheme` is `null`
  on the five prose topics and filled only on the poem topic; its six `rhyming_words`
  (દઈએ, લઈએ, કહીએ, કરીએ, મારે, વઘારે) were each confirmed present in that topic's own
  `original_chunk`, and its `note` says plainly that ‘ધૂએ’ and ‘ખોલે’ do **not** fit the pattern
  rather than asserting a scheme the lines do not carry.
- **`08_sensitivity` hard item (M2.S3.T4, સુરક્ષા)** — honoured. The ગેસ-લાઇટર, the ઠેસી and the
  ઊભરો are told as ઓમની ભૂલો inside the story, never as steps; the anchor is entirely flame-free
  (ઉત્તરાયણ roof, દોર, ફિરકી) — a sweep of that `real_life_example` for લાઇટર · ગેસ · સળગાવ ·
  દીવાસળી · ચૂલો · બાળો returns zero, and the supervising adult is present in the picture.
- **Chapter-level જાતિ-ભૂમિકા note** — honoured by demonstration only. No field anywhere says
  `છોકરાઓએ પણ ઘરકામ કરવું જોઈએ` or `ઘરકામ ફક્ત સ્ત્રીઓનું નથી`, and a boy washing વાસણ or a father
  making ચા is never framed as unusual or praiseworthy-because-unusual.

## Contract (the 12 invariants)   PASS
`phase: 2` · `chapter_id: gseb_eng_gujarati6_ch11` · `plan_id: …_v1` — derivation checked, not
assumed. Every topic has ≥1 concept with resolving `objective_id` and non-empty `content[]`; six
unique objectives, every `home_topic_id` and every `anchor[]` id resolves, `strand_to_objective_map`
covers L1–L6 both ways, every topic's `objective_ids` resolve, every `depends_on` resolves. Inline
`learning_objectives[]` match the root registry **character for character** on all six. Recall ids
are `{topic_id}.RQ{n}` with `legacy_id` `{topic_id}.TR{n}` — **zero `.SR{n}`** — and `bloom_level`
is lowercase there and Capitalised in `objectives[]`, the asymmetry kept. Media ids match
`MEDIA_ID_RE`, concept-scoped, with chapter-continuous `.C{c}`. `publication_id` non-null.
`topic_type` is the **authored** enum (`STORY_TELLING` ×5, `POEM` ×1) as intermediate files carry
it; Agents 14/15 map both to `instructional` at emit. Summaries strictly increase at topic level;
the module carries `difficult_words` (8 + 8, inside 5–10) and `overall_rhyme_scheme` (`null` on M1,
filled on M2). **No digits in display text** — a sweep of Latin and Gujarati numerals across every
name, explanation, example, summary, bullet, point, key term, recall prompt/answer, concept name,
concept content, publication text and media title/description/teaching-note returns **zero hits**;
numerals survive only in ids, `word_count` and `textbook_pages`.

## E–G (reported)
- **E — સ્વાધ્યાય.** 18 inventoried blocks, 18 found, 18 answered, `unanswered: []`. Headings match
  the inventory verbatim. Personal-opinion and પ્રવૃત્તિ blocks (વાતચીત, અનુવાદ, પાસાની શબ્દરમત,
  કવિતાની લયબદ્ધ રજૂઆત) all carry `is_model_answer: true` with a stated alternative set, answered
  with teaching values rather than skipped; the empty printed grids (દ્વિરુક્ત rows,
  ઈલો/ઈલી/ઈલું, ભાવવાચક નામ, પાસાની રમત) are filled. The **અનુવાદ** block's answers are in Roman
  English on purpose — medium of instruction — and `teacher_note` says so explicitly; that is the
  one whitelisted non-Gujarati script in this pack and is **not** a script failure.
  `unmapped: 3` (EX11 શબ્દશોધ, EX12 ઈલો/ઈલી/ઈલું, EX13 ભાવવાચક નામ) — each carries a written reason
  that the block's own material appears nowhere in the reading text. **Reported as unmapped; no
  mapping was invented to empty the field.**
- **F — Shape and media.** All twelve invariants above hold. One image per reading scene, six
  scenes, six authored prompts, zero reuse. `chapter_id` / `plan_id` follow
  `naming_conventions.md` with medium `eng`; ⚠ the board and medium segments are **provisional
  until VERIFY-1** — a wrong medium uploads clean and mis-files the plan.
- **G — the seven usual mistakes.** None present. (1) The plan teaches the સ્વરૂપ, not
  સાર+બોધ+પ્રશ્નોત્તર. (2) N/A — no દુહા page. (3) The poem is not split and has no ટેક to lift.
  (4) No poetic licence corrected — see B. (5) `figures_of_speech: []` everywhere. (6) Every anchor
  is std-6 and Indian. (7) All 18 સ્વાધ્યાય blocks are in the exercise deliverable and none was cut
  as a topic.

## Media
`reuse_report`: **scenes 6 · authored 6 · reused 0 · rejected 0**, and `scenes` equals the six
topics whose `available_content_types` carry `"image"`. Every node has `image_url: ""` **and** a
long, self-contained `generation_prompt`; zero `[reused frame: …]` stamps; every `negative_prompt`
carries `Devanagari script labels` alongside the standing set plus scene-specific exclusions (no
recipe diagram or gas-lighter close-up on the kitchen scene, no poster-with-a-moral anywhere, no
servants, no caricature). `2d_tool` is `null` for the chapter — **zero** interactive tools, inside
the ≤1 limit. Nothing to report as rejected.

## Publication
6/6 topics carry `publication_text`; 15 `paragraph` blocks across the 8 concepts, **15** matching
`concept_publication` entries, matched by index, none renumbered, reordered or dropped, and no
`list` block wrongly carries one. A word-level diff of every `explanation` against its
`publication_text` shows **only** deletions and de-imperativisation — `બાળકો, જુઓ —` removed six
times, `ધ્યાન રાખો —` once, `તમારે … બનાવવાનાં છે` → `… બનાવવાનું કામ આવે છે`, `હવે છેડા બોલી જુઓ`
→ `પંક્તિઓના છેડા બોલી જોતાં સંભળાય છે`. **No meaning was added anywhere.** A sweep for `બાળકો`,
`જુઓ —` and `બોલો` in every publication field returns zero; the surviving second-person forms are
all inside quoted speech (પપ્પાનું `‘‘તમારો આ પ્રયાસ વખાણવાલાયક છે !’’`, મમ્મીનું `‘‘…તમે ચિંતા ન
કરો !’’`), which is the printed text, not a classroom address.

**Convention note, reported not blocking.** `13_assembly_validation.md` describes
`publication_chunk` as "byte-identical to `original_chunk`". `16_publication_authoring.md` — the
agent that owns the field — defines it as the publication-facing version of the whole topic block,
*with the verbatim `original_chunk` kept verbatim inside it*. A16 built it to its own spec:
`original_chunk` + `publication_text` + the reader-facing anchor paragraph. The gate that actually
matters was therefore run as containment, and it passes: **each topic's `original_chunk` occurs
byte-identically inside its `publication_chunk`** on all six — no reflow, no re-spacing, no
re-punctuation, the poem's eleven line breaks and its indent intact. The two spec files should be
reconciled; nothing here needs re-authoring.

## Gaps
1. **`આઇસક્રીમ` — a transcription dispute, examined and settled in favour of the text.**
   `01_meta.json`'s `extraction_notes[1]` clause (ક) states that a 400 dpi crop shows **long ઈ**
   in `આઈસક્રીમ` in both places (the poem's last line and પપ્પા's following sentence), and
   `04_validation.json` repeats that read and instructs A5 to transcribe long ઈ. But A1's *own*
   `00_chapter_normalized.md` prints **short ઇ** at lines 143 and 147 — the note contradicts the
   file it belongs to. A5 re-read the render, kept the short ઇ, and recorded a falsifiable reason:
   in `લઈએ` on the same line the upper stroke rises, curves right and returns down, while in
   `આઇસક્રીમ` it stays short and ends on a point — the same shape as `લાઇટરથી` on p. 71.
   **Checked this run** against `_renders/page-05.png`, cropping both glyphs off the same printed
   line at 16×: the two are visibly different in exactly the way A5 describes. **A5 is right; the
   chunk is correct and nothing was edited.** What is left is a defect in A1's note (and A4's echo
   of it), not in the text — **owner A1**, to reconcile `extraction_notes[1]` with lines 143/147.
   A4's parallel claim that the page prints `જરુર` (short ુ) where `00`/`05` carry `જરૂર` rests on
   the same 150 dpi read and is **unconfirmed** — my own crop is inconclusive at this resolution;
   it should be settled in the same pass, at 400 dpi, by whoever fixes the note.
2. **Root `genre`.** `01_meta.json` writes `genre` as a Gujarati description
   (`વાર્તા (ઘરેલુ, સંવાદપ્રધાન વાર્તા) — …`), which `phase2_contract.md` wants as a roster **slug**.
   A1 flagged this itself (`extraction_notes[14]`, item 1) and A4 confirmed it. The merged plan
   carries the slug **`varta`** — the value `05_with_content.json` already holds, not a new one —
   and the Gujarati description stays in `01_meta.json` where it was written. **Owner A1** if the
   prose form is meant to be authoritative. Sibling chapters in `output6/` are split on this
   (ch01/ch07/ch08/ch10 slug, ch02/ch05/ch06/ch09 Gujarati); worth one decision for the whole pack.
3. **Ids that are placeholders, not facts.** `publication_id: 1` is **PROVISIONAL** — it is CBSE's
   publication row and does not transfer; the GSEB row must be fetched (**VERIFY-2**) before the
   first Phase 8 run. `chapter_master_id: null` and `subject_ref_id: null` / `medium_id: null` —
   no GSEB record is confirmed and nothing was copied from the Hindi pack or derived by arithmetic.
   `chapter_master_id` is **mandatory for upload**, so this chapter cannot ship until VERIFY-2
   lands. Not an A–D failure; a hard stop before upload.
4. **`textbook_url` is a local path** — `../Textbooks-pdf/std-6/ch-11-kamni-maja-ne-majanu-kam.pdf`.
   The GSEB readers have no hosted URL. `11_pages.json` records this honestly and it is carried
   through unchanged. `textbook_pages: "68–78"` at **high** confidence: folio 68 read off the
   opener render, folio 78 off the last, cross-checked against the manifest offset.
5. **`textbook` string.** `ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 6` with a comma, per A1's cover reading;
   `phase2_contract.md`'s example writes a `|`. Every sibling chapter in `output6/` uses the comma
   form, so this is consistent within the pack — flagged only so the divergence from the contract's
   example is not mistaken for drift later.
6. **`ordering` is absent from `13_merged.json`** by design — it belongs to Agents 14/15, so the
   merged plan has 31 root keys, not 32. `topic_title` is set to `chapter_name`; `01_meta.json`
   carries no `topic_title` of its own and every sibling chapter resolves it the same way.
7. **`05b_textbook_order.json` matches the logical traversal exactly** (T1…T6 in printed order).
   Per `phase2_contract.md` §Ordering this must be raised for human confirmation rather than
   silently emitted as a second ordering:
   `{"human_confirmation_required": true, "reason": "textbook order is identical to logical order",
   "checked": "05b_textbook_order.json matches the logical traversal exactly"}`.
8. **A4's `notes[]`, carried here and not blocking.** (a) M2.S3.T4 holds lines 68–122, about a third
   of the reading text, while M2.S4.T5 is short — keeping both whole is right, the printed marker
   treats the tea as one ઘટના, and T4's two internal moves are carried as two concepts. (b) A2's own
   boundary note cites "લીટી 130" where `00_chapter_normalized.md` has the sentence on line 129
   (line 130 is blank), so T5's `source_lines_00_normalized` trails one blank line — a provenance
   field, dropped at merge, harmless. (c) The concept counter is chapter-continuous, so from C5
   onward the concept number no longer equals the topic number (T4→C4+C5, T5→C6, T6→C7+C8); that is
   the contract's behaviour, and `naming_conventions.md`'s "concept number equals topic number" line
   is an example that assumes one concept per topic. (d) M2.S4.T6 carries `topic_type: POEM` while
   also covering three prose lines — defensible, and both POEM and STORY_TELLING map to
   `instructional` at emit.
9. **A16 note-count slip.** `16_publication.json`'s third note says the file carries "કુલ તેર entry"
   of `concept_publication`; the actual count is **15**, and 15 is correct — it equals the number of
   `paragraph` blocks exactly, index for index. The data is right; only the note miscounts.

## LP2 validator
Not run — Phase 8. `POST /api/lp2/learning-plans/validate` must return zero `validation_errors`
before anything ships, and **must not be attempted until VERIFY-2 supplies the real GSEB
`publication_id` and `chapter_master_id`** (Gaps 3). Staging DNS is flaky; retry two or three times
before believing a failure.

## LP2 validator

- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json
- HTTP status: 200
- plan_id: gseb_eng_gujarati6_ch11_v1
- validation_errors: [] (none)
- message: Valid
