# Validation Report — std 7, ch 05 આપણે ભરોસે
સ્વરૂપ: ઊર્મિકાવ્ય-ગીત (confidence: high)   explanation unit: એક કડી
Topics: 4   Objectives: 4   Images: 0/4   Exercises: 13/13 blocks (52 answer entries, 57 printed items)

**Re-QC after owner re-runs — final pass.** The previous gate failed one §C item: `explanation`
ran 95 words on M1.S1.T2 and 91 on M2.S2.T4 against the 55–90 band. Agent 12 was re-run and both
fields were **trimmed**, not the band widened; Agent 16 re-emitted the matching `publication_text`.
This report re-runs the full checklist against the re-merged plan.

Merged fresh from `05_with_content.json` + `12_authoring.json` + `09_media.json` +
`16_publication.json` + `11_pages.json` + `01_meta.json` into `13_merged.json` — 32 root keys, none
missing, none extra; 37 keys on every topic (the contract's 31 + `figures_of_speech` +
`rhyme_scheme` + the four ભાષા-બોધ extras `shabdarth` / `samanarthi` / `vilom` / `vyakaran`, kept
romanized as the server stores them). Working fields dropped: `source_markers`,
`marker_accounting`, `notes`, `agent05_notes`, `convergence`, `genre_signals`, `genre_confidence`,
`active_genre_profiles`, `explanation_unit`, `structure_inventory`, `exercise_inventory`,
`extraction_notes`, `tier`, and `topic_id` off each media node. `ordering` left `null` — Agent
14/15's to set.

## A–D (blocking)   **PASS**

### The item that failed last pass — now closed

| Topic | field | words | band | previous |
|---|---|---|---|---|
| M1.S1.T1 | `explanation` | 89 | 55–90 | 89 (was in band) |
| M1.S1.T2 | `explanation` | **88** | 55–90 | **95 — FAIL** |
| M2.S2.T3 | `explanation` | 80 | 55–90 | 80 (was in band) |
| M2.S2.T4 | `explanation` | **88** | 55–90 | **91 — FAIL** |

M1.S1.T2 lost the ખુદ/ખુદા માત્રા aside's tail and tightened the `- હો ભેરુ.` sentence; the
one-માત્રા fact itself survives — it is still stated in the explanation, and in full in
`concepts[].content[1]` and `detailed_summary`, so nothing was taught away to reach the band.
M2.S2.T4 lost the શબ્દસાંકળ forward-reference sentence from `explanation`; that pointer survives in
`concepts[].content[1]`, where it belongs. No band was widened and no other field moved.

**A — diagnosis and lens: PASS.** ઊર્મિકાવ્ય-ગીત at high confidence off four page signals (ટેક + કડી
of near-equal length; a modern named poet, no છાપ inside the verse; exercises working on the
કાવ્યપંક્તિ with no story signal; a blue box that says "આ ગીત" and prescribes પઠન અને ગાન).
Explanation unit is **એક કડી**, the roster's unit for this સ્વરૂપ. Marker accounting balances
exactly: `[[ટેક]]`×1 + `[[કડી 1]]`/`[[કડી 2]]`/`[[કડી 3]]`×3 = 4 reading-text markers = 4 topics,
one marker per topic, none merged, none split. ટેક handled per the identical-refrain rule —
`tek_words_changed` is false, so the refrain is taught once at M1.S1.T1 and referenced after:
T2 → `depends_on ["M1.S1.T1"]`, T3 → `["M1.S1.T1"]`, T4 → `["M1.S1.T1","M2.S2.T3"]`, every id
resolving. Apparatus stayed out of the topic tree: the `[[પ્રવેશપેટી]]` blue box, the `[[શબ્દાર્થ]]`
box and the QR badge are not topics. `guiding_question` is derived from this poem's own
boat–sail–rudder picture and its closing line.

**B — verbatim and structure: PASS.** All four `original_chunk`s are non-empty and each is found
**character-for-character inside `00_chapter_normalized.md`** (exact substring match, line breaks
included). Script scan of every `original_chunk` and of every authored display string — topic names,
explanations, examples, three summaries, bullets, points, key terms, concept names, concept content
(both `text` and `publication_text`), media titles, descriptions and teaching notes, recall prompts
and answers, objective texts, module and segment names, `difficult_words`, `overall_rhyme_scheme`,
`rhyme_scheme` notes and rhyming words, `guiding_question` — returns **zero Roman and zero
Devanagari characters** outside bracketed terms, and **no `।`** anywhere. Marker accounting as
above; **none of the 13 `[[સ્વાધ્યાય: …]]` blocks became a topic** (all 13 inventory headings
cross-checked against all four `topic_name`s — zero collisions). Printed licence intact and
uncorrected: હાલીએ, ભેરુ, ઝાલીએ, નકામ, છો ને, પિછાણીએ, મોઝારે, કો, છઈએ, and the લય-carrying રે. The
refrain shorthand `- હો ભેરુ.` is reproduced as printed inside each કડી's last line and expanded
only in `explanation`.

**C — the teaching block: PASS.** All four topics carry a non-empty `explanation` **and**
`real_life_example`. Bands: `explanation` 89 / 88 / 80 / 88; `real_life_example` 77 / 72 / 81 / 81
(55–90); `objective_text` 23 / 23 / 26 / 25 (12–30). Voice is second-person spoken શિષ્ટ ગુજરાતી
throughout; glossing is at point of first use (ભેરુ, ઝાલીએ, હામ, મોઝારે, સઢ, સુકાન, કરવૈયો, કો, છઈએ,
ઉગારે, પિછાણીએ) at the L2 bar. Anchors are Indian, single, concrete and inside std-7's reach, and
rotate domain without repeating: શેરીનો ખૂણો સાફ કરવો / ઉત્તરાયણની ફિરકી / સાયકલનો છૂટી ગયેલો હાથ /
ડુંગરનાં પગથિયાં. Craft is named at std-7 level only — પ્રાસ and લય as *sound*, no device name, no
છંદ.

**D — સ્વરૂપ essence: PASS.** The `urmikavya_geet` avoid list checked mechanically across
`explanation`, `real_life_example`, all three summaries, `concept_bullets`, `important_points`,
every `recall_questions[].prompt` and `.answer`, every `concepts[].content[]` string and every
`publication_text`:

- **Slogan gate** — `જોઈએ` occurs **nowhere** in any teaching or publication field of any topic, and
  it occurs in no `original_chunk`. The chapter's two ready-made slogans (the exercise paraphrase
  `દોસ્ત, આપણે આપણા ભરોસે જ જીવવું જોઈએ` and the writing topic `'જાત મહેનત જિંદાબાદ'`) stayed inside
  `10_exercise_solutions.json` and were not echoed. M2.S2.T4's closing-topic form of the gate holds
  after the trim: the last sentence of `explanation` lands on `'આપણે જ આપણે છઈએ'; છઈએ એટલે છીએ`, the
  last sentence of `detailed_summary` on `આખું ગીત આવીને અટકે છે 'આપણે જ આપણે છઈએ' પર`, and every
  recall answer on the કડી's own words (`કોણ લઈ જાય સામે પાર` / `આપણે જ આપણે છઈએ` / `કરવૈયો આપણે જ
  આપણે છઈએ`) — no rule of conduct anywhere.
- **Feeling before picture** — each `explanation`'s first sentence names something printed in that
  topic's own chunk: `હો ભેરુ મારા` / `એકતારો`, `ગાઈ ગાઈને`, `'તારે ભરોસે રામ !'` / `બાહુમાં`,
  `હૈયામાં` / `ડુબાડે`, `ઉગારે`, `સામે પાર`. Both trimmed explanations still open on the picture.
- **Skipping the craft** — `figures_of_speech` is `[]` on all four (correct at std 7: no named
  device at any tier), so the craft is carried in prose, and each explanation still carries it after
  the trim: હાલીએ–ઝાલીએ and the twice-printed sung line; નકામ–રામ plus the doubled `ખોટું રે ખોટું`;
  ભરી–ધરી plus the બ-બ-બ of `બળને બાહુમાં ભરી`; the repeated `કોણ રે`, the લય-carrying `રે` and the
  doubled `આપણે`.
- **Invented અલંકાર** — vacuously clean: `figures_of_speech` is empty everywhere, so no `lines`
  string can fail the verbatim test. `[]` here is the correct and complete answer.
- **Never modernise the poet** — મોઝારે, કો, છઈએ, હાલીએ, ભેરુ appear exactly as printed inside every
  quoted line and are glossed as બોલી or as લય; no field calls any of them ભૂલ, અશુદ્ધ or ખોટી જોડણી.
  M2.S2.T4 explicitly teaches `કો` as `કોઈ`'s short form, `ભૂલ નથી`.
- **Over-scientifying / political framing / literal reading** — zero hits for બાષ્પીભવન, જલચક્ર,
  ઘનીભવન, પ્રકાશસંશ્લેષણ, ગુરુત્વાકર્ષણ, ભરતી-ઓટ; zero for સરકાર, યોજના, અભિયાન, સેના, પક્ષ, સરહદ,
  જિંદાબાદ, આત્મનિર્ભર ભારત, સ્વચ્છ ભારત. No field asserts a real voyage or turns the કડી into boat
  instruction; `સઢ` and `સુકાન` are glossed as the boat's parts and nothing more.
- **07 hard items** — all 17 `severity: "hard"` `avoid_checks` across the four topics re-checked
  against the re-merged text and addressed (the mechanically checkable ones above; the
  reading-level ones by inspection). The two re-authored explanations were re-checked item by item
  against their own topic's hard list.
- **08 hard item (M1.S1.T2, `areas: ["ધર્મ"]` — a valid label from the seven)** — addressed, and
  still addressed after the trim. `નકામ` never stands without the કડી's own condition
  `ખુદનો ભરોસો જેને હોય નહીં રે તેને` in the same sentence or the one before; `ખુદ` and `ખુદા` are
  glossed side by side; `'તારે ભરોસે રામ !'` is presented every time as the singer's own quoted
  words, marked by the printed અવતરણચિહ્ન; and no field in the plan says or implies that ખુદા or રામ
  is false or that praying is useless. The એકતારો singer keeps his dignity in the prose and in the
  media prompt.

**Contract invariants (all 12): PASS.** `phase: 2`; `plan_id` = `{chapter_id}_v{version}` =
`gseb_eng_gujarati7_ch5_v1`; `chapter_id` = `gseb_eng_gujarati7_ch5`. Every topic has ≥1 concept,
each with non-empty `content[]` and an `objective_id` in the root registry. Registry consistent:
O1–O4 unique, L1–L4 unique, `strand_to_objective_map` equals the registry's `legacy_id → objective_id`
pairing exactly, every `home_topic_id` and every `anchor[]` id resolves, every topic's
`objective_ids`, `depends_on` and `source_topic_ids` resolve. **Inline `learning_objectives[]`
mirrors match the root `objective_text` character for character** on all four topics, each carrying
`image_examples: []`. Id grammar checked against traversal position: `M{m}` / `M{m}.S{s}` /
`M{m}.S{s}.T{t}` consecutive, concept counter chapter-continuous and equal to the topic number
(C1…C4); recalls are `{topic_id}.RQ{n}` with `legacy_id` `{topic_id}.TR{n}` and every answer
non-empty — **no `.SR{n}` anywhere**; media match `MEDIA_ID_RE` concept-scoped and each node's
`concept_id` equals its id prefix. `topic_type` is the authored enum `POEM` on all four, correct for
an intermediate file (Agents 14/15 map it to `instructional`). Summaries strictly increase on every
topic (22<53<105, 27<57<121, 27<53<109, 32<60<95 words). **No numerals — Arabic or Gujarati — in any
display text.** `publication_id` is non-null. `figures_of_speech` is `[]` everywhere, so invariant
11 holds vacuously.

**Exercises: PASS.** `coverage_report.blocks_found` lists 13 headings = `exercise_inventory` length
13; `blocks_answered` 13; `unanswered` `[]`; 52 answer entries covering 57 printed items (three
composite blocks answered whole with every printed slot filled). Headings match the inventory
verbatim. The અનુવાદ block's answers are written in English on purpose (medium of instruction) and
say so in `teacher_note` — whitelisted, not a script failure.

**Media: PASS.** `reuse_report`: `scenes` 4 = the 4 topics whose `available_content_types` carry
`"image"`; `authored` 4; `reused` 0; `rejected` `[]`. Every node carries `image_url: ""` **and** a
non-empty self-contained `generation_prompt` (1384–1529 chars); no `[reused frame: …]` stamp
anywhere. Every `negative_prompt` carries `Devanagari script labels`. `2d_tool` is `null` on every
topic and at chapter level — zero tools in the chapter (≤1).

**Publication: PASS, re-verified after the re-emit.** All four topics have a non-empty
`publication_text`; `publication_chunk` is **byte-identical** to `original_chunk` on all four.
`concept_publication` blocks match `concepts[].content[]` by index and by count on every concept —
the two `paragraph` blocks each carry `publication_text` at indices 0 and 1, and the third block is
a `list`, which the contract's content shape gives no `publication_text`; no index is skipped and
none is invented. No vocative or classroom instruction survived: `બાળકો`, `જુઓ —` and `બોલો` appear
in `explanation` (where they belong) and in **zero** publication strings. M1.S1.T2's and M2.S2.T4's
`publication_text` now mirror the **trimmed** explanations — the re-emit landed on the right
version, and the rewrite adds no meaning the explanation did not carry (the only deltas are dropped
address, re-sequenced clauses, and `એક જ તારનું` for `એક તારનું`, which is emphasis, not content).

## E–G (reported)
- **E** — all 13 blocks answered and skill-tagged; personal-opinion and પ્રવૃત્તિ items carry model
  answers explicitly marked `(એક શક્ય જવાબ)` with `acceptable_alternatives`; empty printed grids
  (શબ્દસાંકળ's six slots, વાક્યવિસ્તાર's three rule-lines per sentence) filled with teaching values.
  22 items are reported **unmapped** with reasons and no mapping was invented — see Gaps.
  Sensitivity notes applied where the chapter touches ધર્મ — flagged and guided, never censored.
- **F** — the 12 invariants hold (above). `publication_id` non-null, `topic_type` inside the closed
  enum after the Agent-14 mapping, recalls `.RQ{n}`, concept numbers chapter-continuous — the four
  the server rejected on the first Hindi run are all correct here. `chapter_id`/`plan_id` follow
  `gseb_eng_gujarati{grade}_ch{unit_number}`, board and medium segments **provisional until
  VERIFY-1**. One image per reading scene, ≤1 `2d_tool`, summaries increase, no numbers in display
  text. Two minor shape observations, neither an invariant and neither blocking: `word_count`
  carries a second key `modified` beside `original` (`field_shape_rules.md` names only `original`),
  and `concepts[].key_terms` is `[]` on all four concepts — the 3–6 glosses live at topic level
  (`key_terms` runs 5 / 6 / 6 / 6), which is where the band is stated.
- **G** — none of the seven present. Not સાર+બોધ+પ્રશ્નોત્તર (the સ્વરૂપ is taught, and the બોધ the
  poem could carry is never printed as a rule); no દુહા to merge; the ટેક is neither split off as
  filler nor re-taught four times; no licence silently corrected; no અલંકાર named to fill a field;
  every anchor is a std-7 Indian moment; no સ્વાધ્યાય block became a topic.

## Media
`scenes 4 / authored 4 / reused 0 / rejected []`. Reuse is dormant — **no Gujarati frame pool
exists**, so `Images` reads `0/4` by design, not by omission. One `image` node per કડી-topic, each
showing that કડી's own picture (the clasped hand of મહેનત; the singer with the એકતારો; the hands on
સઢ and સુકાન; the far shore and the arm being hauled in) — no frame illustrates the whole poem and
no frame illustrates a moral. The ટેક topic's frame shows the ટેક's own words rather than repeating
a boat. `2d_tool: null` — a ગીત has no staged process a child could operate. Rejected frames: none,
because nothing was scored — there was no pool to score against.

## Gaps
Honest absences, none of them blocking, each recorded rather than filled:

1. **`publication_id` is provisional.** Written as `1` to satisfy the contract's non-null
   requirement. That is **CBSE's publication row and does not transfer**; the GSEB row must be
   fetched from the education DB at **VERIFY-2** and written in before the first Phase 8 upload.
2. **`chapter_master_id` is `null`.** Required for upload, not discoverable from the LP2 API,
   fetched per chapter at VERIFY-2. Not derived by arithmetic, not invented.
3. **`chapter_id` / `plan_id` board and medium segments unverified (VERIFY-1).** `eng` is the medium
   of instruction, not the subject language; a wrong medium uploads clean and mis-files the plan.
4. **Root `genre` carries the Gujarati form `ઊર્મિકાવ્ય-ગીત`,** while `phase2_contract.md`'s root-key
   example shows the roster **slug** (`urmikavya_geet`) — which is also what `active_genre_profiles`
   resolves to. Not an A–D item and not one of the 12 invariants, so it does not block, but it
   should be settled by **`agents/01_*`** before Phase 8 rather than at emit.
5. **`textbook_url` is a local path string** (`../Textbooks-pdf/std-7/ch-05-aapne-bharose.pdf`) — the
   GSEB readers have no hosted URL. Carried from `11_pages.json`'s own gap list.
   `textbook_pages` `25–29` is high-confidence (printed folios read off page-1 and page-5 renders).
6. **Transcription defect found by Agent 5, reported and not repaired.** Printed folio 25 sets the
   quoted line in typographic single quotes — ‘તારે ભરોસે રામ !’ (U+2018/U+2019) — while
   `00_chapter_normalized.md` writes ASCII apostrophes. M1.S1.T2's `original_chunk` carries the
   ASCII form exactly as `00` has it, so the plan is internally consistent. Owner of the fix is
   **`agents/01_*`**; if that file is corrected, M1.S1.T2's chunk and its `publication_chunk` must
   be re-copied. Gujarati letters, માત્રા, અનુસ્વાર, spacing and the space before `!` are all
   correct — the deviation is the quote glyph only.
7. **Double-render cross-check was replaced by an upscale pass.** The run context supplied the
   renders already rasterised at ~150 dpi and forbade re-rendering, so Agent 1 re-read every line
   against 2×–18× LANCZOS crops of the same PNGs. That settles glyph shape and every doubtful
   reading in this chapter, but it cannot add optical detail a true higher-dpi re-render would have
   added. Recorded as a **method gap**, not a clean double-render.
8. **A printed inconsistency inside the chapter, recorded not repaired.** The verse on folio 25 sets
   `કો` and `છઈએ`; the MCQ block on folio 27 quotes the same line as `કો'` and `છીએ`. Reading scenes
   carry the verse's forms; Agent 10 answers the exercise from the exercise's own printed wording.
   Neither spelling is presented to the child as the wrong one. Likewise `હોટેલમાં`/`હોટલથી` inside
   one exercise paragraph, and the single nukta in `તોફ઼ાની` — all transcribed as printed.
9. **22 exercise items reported `unmapped`, correctly.** 6 from the ચિત્ર-આધારિત block (built on a
   printed photograph of collapsed buildings — a કુદરતી આફત, which no કડી of this poem prepares),
   5 વાક્યવિસ્તાર drill sentences, 5 અર્થ-સ્પષ્ટતા sentences, 4 ભૂલ-સુધાર sentences, 1 કાળ-ફેરફાર
   paragraph, 1 અનુવાદ sentence. Each carries a reason; **no mapping was invented to empty the
   report**, and nothing was missed by the cut.
10. **No segment-level or module-level three-tier summaries, and no segment recall questions, were
    authored** — so the strictly-increasing check runs at topic level only, where it passes on all
    four. Reported so the absence is visible rather than read as a silent pass.
11. **`overall_rhyme_scheme` is stated once, on M1; M2 carries `null`.** Agent 12's own note records
    this as deliberate — the form fact is said once for the whole poem rather than repeated per
    module. Non-blocking; flagged so a downstream reader does not read M2's `null` as a miss.
12. **Topic count 4 exceeds `structure_inventory.kadi` 3** because Agent 2 cut the opening four-line
    ટેક block as its own topic — a judgement Agent 1 explicitly delegated to it, marker-backed
    (`[[ટેક]]`), carrying a picture no કડી repeats (`એક મહેનતના હાથને ઝાલીએ.`). Non-blocking, and it
    satisfies rather than violates the identical-refrain gate: exactly one topic carries the ટેક.
13. **`ordering` is `null`** in `13_merged.json` — Agent 14/15 sets it. `05b_textbook_order.json`
    records the printed order for the ordering comparison that follows this gate.
14. **This chapter prints no end-of-poem attribution line.** The poet's name appears only in the
    title masthead as `- પ્રહ્લાદ પારેખ`, so it is **not** attached to the last topic's
    `original_chunk` — attaching it would place text where the page does not print it. Recorded as
    an absence rather than filled in.

## LP2 validator
Not run — filled in at Phase 8. `POST /api/lp2/learning-plans/validate` must return zero
`validation_errors`, and `publication_id` / `chapter_master_id` (gaps 1 and 2) must be resolved
before that call.

---

**Verdict: PASS. A–D clear, no blocking item outstanding.** The one §C failure from the previous
gate is closed by trimming, not by widening: `explanation` now runs 89 / 88 / 80 / 88 words against
the 55–90 band, with the material that came out preserved in the concept content and the detailed
summary rather than lost. Every check re-run from scratch on the re-merged plan — the 12 contract
invariants, the marker accounting, the verbatim substring match, the script and digit scans, the
17 hard pitfall items, the one hard sensitivity item, exercise coverage, the media pack and the
publication layer — passes. The fourteen items under **Gaps** are reported absences and provisional
values, not failures; two of them (`publication_id`, `chapter_master_id`) must be resolved at
VERIFY-2 before Phase 8. Ready for Agent 14.

## LP2 validator
- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json (multipart field "file")
- HTTP status: 200
- validation_errors: [] (none)
- Result: Valid
