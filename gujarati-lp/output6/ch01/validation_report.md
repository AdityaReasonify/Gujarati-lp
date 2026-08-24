# Validation Report — એક જ ડાળનાં પંખી (std 6, ch 1)

સ્વરૂપ: ઊર્મિકાવ્ય-ગીત / `urmikavya_geet` (confidence: high)   explanation unit: એક કડી
Topics: 3   Objectives: 3   Images: 0/3   Exercises: 13/13 blocks (43 items, 0 unanswered)

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` +
`16_publication.json` + `11_pages.json` + `01_meta.json` → `13_merged.json`
(31 root keys; `ordering` deliberately left to Agent 14/15).

---

## A–D (blocking)   **PASS**

### A — Diagnosis and lens   PASS
- સ્વરૂપ diagnosed off the rendered page with all four signals recorded in `genre_signals`;
  `genre_confidence: "high"`. The blue intro box is quoted as **evidence** only — its verdict word
  `મહિમા` appears in no teaching field (checked mechanically, 0 hits).
- Explanation unit **એક કડી** matches the roster line for ઊર્મિકાવ્ય-ગીત. Three printed કડી → three
  topics.
- **ટેક handled as content, not repetition.** The ટેક's wording is identical at all four
  occurrences (`tek_wordings_distinct: 1`), so it is taught once inside `M1.S1.T1` and referenced
  after; `M1.S1.T2` and `M1.S2.T3` both carry `depends_on: ["M1.S1.T1"]`. The printed shorthand
  `- એક જ.` is expanded in exactly one `explanation` (T1) and nowhere else — verified by string
  search.
- Apparatus did not become a reading scene: the blue પ્રવેશક-પેટી, the શબ્દાર્થ-પેટી, the 13
  numbered સ્વાધ્યાય blocks and the appended `અમે એક જ...` box are all in `not_cut_as_topics`.
- Not a mixed chapter — pages 2–5 carry apparatus and exercises only, no appended reading matter.
- `guiding_question` is derived from this chapter's own three pictures (ડાળ / ઊંચે આભ /
  ધરતીનો ખોળો) and the three explanations in order do answer it.

### B — Verbatim and structure   PASS
- Re-rendered the source PDF myself (`pdftoppm -png -r 150`, plus page 1 at 300 dpi) and read the
  printed poem line by line against all three `original_chunk`s. **Character-for-character match**,
  including: દીર્ઘ `ઊ` in `ઊંચે` / `ઊડી-ઊડી` against હ્રસ્વ `ઉ` in `ઉમંગી`; `ળ` in `ડાળનાં` and
  `ખોળે`; the `લ્લ` જોડાક્ષર in `કલ્લોલ`; the વિસર્ગ in `દુઃખમાં`; the missing comma at the end of
  `કરીએ કુદરત-ગાન અમે સહુ`; the double space before `- એક જ.` in the first કડી only.
- `- એક જ.` copied as printed in all three chunks — never expanded inside verbatim.
- The poet line `- શાન્તિલાલ શાહ` is printed **above** the poem, not at its foot, and correctly sits
  in no `original_chunk`. The header furniture (chapter-number box, QR badge and its Latin code
  string, the folio) never entered any chunk.
- Verbatim was taken from the poem page, not from સ્વાધ્યાય block 10, which reprints the same lines
  with different spelling and punctuation (`કુદરતગાન`, `દુઃખ માં`, `પ્રવાસ નાં`). Confirmed on the
  render.
- **Script:** every authored and display string is Gujarati-script only. Mechanical scan over topic
  names, explanations, examples, all three summaries, bullets, important points, recall prompts and
  answers, every `concepts[].content[]` block and every `publication_text` — **zero** Devanagari
  characters, **zero** Roman characters, **zero** `।`. The Roman strings in the plan are confined to
  media `generation_prompt` / `negative_prompt` (an image model's input, not display text) and to
  ids and enum values.
- Marker accounting: `00_chapter_normalized.md` prints 4 reading-scene markers
  (`[[ટેક]] [[કડી 1]] [[કડી 2]] [[કડી 3]]`) and the three topics between them carry all 4
  (`markers_carried_by_topics: 4`). **No `[[સ્વાધ્યાય: …]]` block became a topic** — 13 સ્વાધ્યાય
  markers, 0 topics.
- Ids consecutive; every `depends_on`, `home_topic_id`, `anchor[]`, `objective_ids` and media
  `concept_id` resolves against a node that exists in `13_merged.json`.

### C — The teaching block   PASS
- All three topics carry non-empty `explanation` **and** `real_life_example`.
- Word counts, all inside 55–90 / 12–30, measured on the merged file:

  | topic | explanation | real_life_example | brief < summary < detailed |
  |---|---|---|---|
  | M1.S1.T1 | 82 | 72 | 18 < 41 < 72 |
  | M1.S1.T2 | 70 | 68 | 16 < 46 < 71 |
  | M1.S2.T3 | 72 | 69 | 17 < 46 < 75 |

  `objective_text`: O1 = 23, O2 = 19, O3 = 22 words. Bands remain **provisional until VERIFY-4**;
  nothing was widened to fit.
- L2 calibration held: point-of-use glossing in every explanation (વિહરીએ, આભ, કલ્લોલ, ઉમંગી /
  વઢીએ, તોયે, નિરંતર / બાળ, કુદરત-ગાન, કેરા, સંગી), all glosses in Gujarati, no Hindi word standing
  in for a Gujarati one.
- Anchors are single, concrete, Gujarati and within a std-6 child's reach — ઉત્તરાયણનું ધાબું /
  શેરી ક્રિકેટનો `આઉટ છે, નથી !` ઝઘડો / શાળાની પ્રાર્થનાસભા. Three different domains, no anchor
  needing its own glossary, each closing on a question to the child.
- Craft ceiling respected: `figures_of_speech: []` on all three topics, and **no** label —
  અલંકાર, છંદ, યમક, પુનરુક્તિ, સમાસ, સાહિત્યપ્રકાર, ઊર્મિકાવ્ય, even પ્રાસ — occurs anywhere in a
  teaching field (mechanical scan, 0 hits). The sound is still taught, as sound: `ઊંચે`–`નીચે`,
  `રહીએ`–`થઈએ`, and the return of `અમે સહુ`.

### D — સ્વરૂપ essence   PASS
Every `severity: "hard"` item in `07_pitfalls.json` was checked mechanically against the merged
fields, and each one holds:

- **Slogan gate (all three topics)** — `જોઈએ` occurs **0 times** in any explanation, example,
  summary, bullet, important point, recall answer or publication text. No sentence in the plan
  could be printed on a classroom poster.
- **Picture before feeling (all three)** — first sentence of each explanation names the કડી's own
  concrete words: T1 `ડાળ`/`પંખી`, T2 `સુખ`/`દુઃખ`, T3 `ધરતીને ખોળે`/`બાળ`. None opens on સંપ,
  એકતા or કાવ્યનો ભાવ.
- **Craft not skipped (all three)** — one unlabelled sound sentence per explanation, as listed
  under C.
- **Refrain-shorthand expansion (T1 only)** — stated once in T1, absent from T2 and T3.
- **Literal reading of a figurative line (T3)** — `ધરતીને ખોળે` is presented as a picture the poet
  draws (`મા ખોળામાં બેસાડે તેમ`) in explanation, summary, detailed summary, concept content and the
  media `teaching_notes`. Nowhere stated as fact about the earth.
- **Never modernise the poet (T3)** — `જીવન કેરા` is quoted as printed everywhere; `કેરા` is glossed
  as the poem's own older way of saying `-નાં` and is never called ભૂલ, ખોટું or જૂની જોડણી.
  `shabdarth` tags it `કાવ્ય-રૂપ`.
- **Over-scientifying (T3)** — પર્યાવરણ, જૈવવિવિધતા, પ્રકૃતિ-સંતુલન, ઋતુચક્ર, પ્રદૂષણ: 0 hits.
- **`સહુ`–`સહુ` is not a rhyme (T3)** — `rhyme_scheme.note` says so in as many words.
- `08_sensitivity.json` is `none_found: true` with a reasoned review of all seven fixed areas
  (ધર્મ, સમુદાય, ક્ષેત્ર, વિકલાંગતા, સંઘર્ષ, જાતિ-ભૂમિકા, સુરક્ષા) — **no** hard sensitivity item
  to address. The review is argued from the text, not waved through.
- `figures_of_speech` is `[]` on every topic, so invariant 11 (device lines found verbatim in the
  chunk) is satisfied vacuously and correctly — `[]` is the right answer at std 6.

---

## E–G (reported)

**Contract invariants (F).** Checked on `13_merged.json`:

| # | invariant | result |
|---|---|---|
| 1 | `phase: 2`, `plan_id = {chapter_id}_v{version}`, `chapter_id = gseb_eng_gujarati6_ch1` | OK (board/medium segments provisional, VERIFY-1) |
| 2 | non-empty Gujarati-script `original_chunk` on every topic | OK |
| 3 | ≥1 concept per topic, valid `concept_id`, resolvable `objective_id`, non-empty `content[]` | OK (4 concepts, all with content) |
| 4 | root `objectives[]` complete and consistent; `strand_to_objective_map` covers every `legacy_id` | OK (L1→O1, L2→O2, L3→O3) |
| 5 | inline `learning_objectives[]` text identical to the registry, character for character | OK (asserted) |
| 6 | `MEDIA_ID_RE` concept-scoped; recalls `RQ{n}` + `legacy_id` `TR{n}`; **no `.SR{n}`** | OK — `M1.S1.T1.C1.IMG1`, `M1.S1.T2.C3.IMG1`, `M1.S2.T3.C4.IMG1`; 9 recalls, all `.RQ{n}`/`.TR{n}` |
| 7 | no સ્વાધ્યાય block is a topic; every inventoried block answered | OK |
| 8 | three-tier summaries strictly increase | OK at topic level (see C). No segment- or module-level summaries were authored, so nothing to check there |
| 9 | no numbers in display text | OK — digit scan over all display strings returns 0. Numerals survive only in ids, `word_count`, `textbook_pages` |
| 10 | one image per reading scene; ≤1 `2d_tool` | OK — 3 scenes, 3 images, `2d_tool: null` |
| 11 | `figures_of_speech` lines found verbatim | OK — `[]` on all three |
| 12 | every reference survives renumbering | holds now; re-assert after Agent 14 |

Concept numbering is chapter-continuous (`C1, C2` on T1, then `C3`, `C4`) — the concept number does
**not** equal the topic number here because T1 carries two concepts, which the contract permits.

**Exercises (E).** `coverage_report.blocks_found` = 13 = the length of `01_meta.json`'s
`exercise_inventory`, entry-to-entry in printed order. `unanswered: []`, `unmapped: []`. 43 entries
answered (42 items across the 13 numbered blocks, plus the appended `અમે એક જ...` box as EX43).
Teacher-addressed and જૂથકાર્ય items (વાતચીત, ઉખાણાં-પ્રવૃત્તિ, સમૂહગાન) are answered as model
answers rather than skipped. The અનુવાદ block's answers are written in the medium of instruction on
purpose and marked as such — not a script failure.

**Media (F).** `reuse_report`: `scenes: 3`, `authored: 3`, `reused: 0`, `rejected: []`. Matches the
three topics carrying `"image"` in `available_content_types`. Every node has `image_url: ""` **and**
a real self-contained `generation_prompt`; no `[reused frame: …]` stamp anywhere. Every
`negative_prompt` carries `Devanagari script labels`. Each narrator bar names one exact printed
Gujarati line — `અમે સહુ એક જ ડાળનાં પંખી.`, `તોયે નિરંતર રહેતાં સંપી.`, `જીવન કેરા પ્રવાસનાં સંગી.`
— all three verified against the render. Settings spread across central Gujarat, Saurashtra and the
ડાંગ; no community costume placed on anyone the text does not place there.

**Publication (F).** All three topics carry `publication_text`. `publication_chunk` opens with the
topic's `original_chunk` **byte-identical** (asserted programmatically) and then adds the
publication prose — the verbatim is untouched, unreflowed and unrepunctuated. `concept_publication`
maps one entry per `paragraph` block, by index, with counts matching exactly: C1 [0,1], C2 [0,1],
C3 [0,1], C4 [0,1] — 8 entries for 8 paragraph blocks, `list` blocks correctly left alone. No
vocative or classroom instruction survives (`બાળકો, જુઓ —`, `બોલી જુઓ`, `પાછું ગાઓ`, the closing
questions — all removed); the single `બાળકો` hit in T3's chunk is the noun `બાળકોથી` inside the
પ્રાર્થનાસભા anchor, not an address. Spot-read against `12_authoring.json`: no meaning added.

**G — the seven usual mistakes.** None present. The plan teaches the કડી, not સાર + બોધ +
પ્રશ્નોત્તર; the ટેક is neither split out nor re-taught; nothing was silently corrected; no અલંકાર
was named; the anchors are std-6 Gujarat; the સ્વાધ્યાય is a separate, fully answered deliverable.

---

## Gaps

Honest absences, all recorded rather than filled:

1. **`publication_id` — the one item that must be resolved before upload.** The contract requires a
   non-null value, so `13_merged.json` carries the placeholder `1`. **That is CBSE's publication
   row and it is NOT portable to GSEB.** The real GSEB publication row must be fetched from the
   education DB (**VERIFY-2**) and written in before any Phase 8 upload. Shipping `1` would upload
   clean and mis-file the plan.
2. **`chapter_master_id: null`** — mandatory for upload, fetched per chapter from the education DB
   (VERIFY-2), never derived by arithmetic. Not invented here.
3. **`subject_ref_id` / `medium_id`: null** — server-injected; no GSEB subject record is confirmed.
4. **`chapter_id` / `plan_id` board and medium segments (`gseb`, `eng`) are provisional until
   VERIFY-1.** A wrong medium slot uploads clean and mis-files the plan — confirm against the live
   server before the first upload.
5. **`textbook_url` is a local path** (`../Textbooks-pdf/std-6/ch-01-ek-j-dalna-pankhi.pdf`) — the
   GSEB readers have no hosted URL. `11_pages.json` records this as its only gap.
   `textbook_pages: "1–5"` is high-confidence (printed folio read off the render, agreeing with the
   manifest row and the std-6 N+11 offset).
6. **`genre` label mismatch, owner A1 — reported, not blocking.** `01_meta.json` stores the Gujarati
   label `ઊર્મિકાવ્ય-ગીત`; `02_structure.json` / `05_with_content.json` and `phase2_contract.md`
   want the slug. `13_merged.json` carries the slug `urmikavya_geet`. Agent 4 flagged this too.
   Worth fixing at source so nobody downstream picks the label.
7. **`topic_title` was not authored anywhere.** It is one of the contract's 32 root keys and no
   agent produces it, so it is set to the printed chapter name, matching `unit_title`. Flagging it
   rather than pretending it was supplied.
8. **`topic_type` carries the authored enum `POEM`.** Per `phase2_contract.md`, Agents 02–13 keep
   the literary value and **Agents 14/15 map it at emit** (`POEM → instructional`). The closed
   server enum must appear in the emitted plans, not here.
9. **`ordering` is absent by design** — Agent 14/15 sets it. `05b_textbook_order.json` records the
   printed order; the textbook order is identical to the logical order for this chapter, which
   Agent 14/15 must raise as `human_confirmation_required` per the contract.
10. **Segment cut is uneven** (`M1.S2` holds a single topic) — Agent 2's own note, carried by Agent
    4. The poem's turn genuinely falls there. Reported, never blocking.
11. **No કવિ-પરિચય or કૃતિ-પરિચય is printed** — only the poet's name line. Not one biographical fact
    about શાન્તિલાલ શાહ appears anywhere in the plan, and none may be added. This is a measured gap,
    not a hole to fill.
12. **Transcription defect surfaced by Agent 10, owner A1 — reported.** Block 3's printed heading
    uses `(√)`; `00_chapter_normalized.md` and `01_meta.json` both record `(✓)`. Agent 10 kept the
    inventory form in `blocks_found` so the entry-to-entry match holds, used the printed `(√)` in
    `prompt_verbatim`, and recorded the difference instead of correcting it silently. Cosmetic; no
    answer depends on it.
13. **Word bands are provisional (VERIFY-4).** 55–90 and 12–30 are inherited from the
    first-language Hindi pack and have not been re-measured against L2 GSEB chapters. Everything in
    this chapter sits inside them; the measurements themselves still owe VERIFY-4.

## LP2 validator

Not run — filled in Phase 8. **Do not upload until Gaps 1–4 are resolved**: `publication_id` is a
placeholder, `chapter_master_id` is null, and the `chapter_id` board/medium segments are unconfirmed.

---

**Verdict: A–D PASS. `13_merged.json` is complete and internally consistent, and this run is
complete as a Phase-2 authoring pass.** It is **not** upload-ready: the four provisional/null root
ids above are real blockers for Phase 8, not for this gate.

## LP2 validator
- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json
- HTTP status: 200
- plan_id: gseb_eng_gujarati6_ch1_v1
- validation_errors: [] (none)
- message: Valid

## LP2 validator

- Status: HTTP 200, success=true
- plan_id: gseb_eng_gujarati6_ch1_v1
- validation_errors: none (empty array)
- message: Valid
