# Validation Report — std 7, ch 11 · અંધેરી નગરી

સ્વરૂપ: `kathakavya` — sub-form **રમૂજ-બોધ કથાકાવ્ય (satire)** (confidence: high)   explanation unit: **એક વાર્તા-પગલું (ઘટના), સીમા હંમેશાં છાપેલી કડીના છેડે**
Topics: 10   Objectives: 10   Images: 0/10   Exercises: 17/17 blocks (72/72 printed items answered)

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` → `13_merged.json` (31 root keys, 37 topic keys, 3 modules,
6 segments, 10 topics, 12 concepts, 10 media nodes, 1 `2d_tool`). `ordering` is deliberately absent —
Agent 14/15 sets it. No working field survived the merge: `provenance` (ghatna/kadi markers,
`printed_lines`), `genre_signals`, `cut_accounting`, `structure_inventory`, `extraction_notes`,
pitfall `avoid_checks` and `severity`, sensitivity `areas`/`caution`/`guidance`, `reuse_report`,
`coverage_report` and every agent's `notes[]` were all dropped. Only contract keys ship.

---

## A–D (blocking)   **PASS**

### A — diagnosis and lens

`01_meta.json` records the four signals off the rendered page and the book names the form itself:
the blue પ્રવેશપેટી on p. 71 prints "આ એક કથાકાવ્ય છે." — quoted as **evidence, not verdict**.
Measured signals: rhymed કડી (AABB throughout — રાજા-ખાજાં, એકે-વિવેકે, ચેલો-પેલો, ખાસો-રાતવાસો,
દ્વાર-ચાર, અપાર-લગાર, વિશેષ-લેશ, અંગ-પ્રસંગ, પસ્તાય-ઉપાય, આપ-પ્રતાપ, પાંચ-આંચ), named પાત્રો
(ગુરુ, ચેલો, વણિક/શેઠ, કડિયો, પખાલી, મુલ્લા, ડોશી, રાજા), a chain of ઘટના, a result at the end, and
**`tek_occurrences: 0`** — the measured absence of a ટેક is one of the reasons this is not routed to
`urmikavya_geet.md`.

**Explanation unit matches the roster row.** કથાકાવ્ય — "one વાર્તા-પગલું cut at a printed કડી
boundary". Verified mechanically against `00_chapter_normalized.md`:

- **11** `[[કડી n]]` markers, **10** `[[ઘટના: …]]` markers, **17** `[[સ્વાધ્યાય: …]]` blocks,
  0 `[[દુહો]]`, 0 `[[પદ]]` — re-derived from the transcription by this agent, not taken on trust.
- **10 instructional topics = 10 ઘટના markers**, one-to-one and in printed order; the emitted
  `ghatna_marker` sequence equals the file's marker sequence string-for-string.
- **11 કડી markers carried by exactly one topic each**, none split, none uncarried. 10 < 11, so
  `kathakavya.md` hard gate 2 (step-wise, not કડી-wise) holds.
- The one step that spans two કડી is `M1.S2.T3` (કડી 3 + કડી 4) — it keeps the ગુરુ's reason and the
  શિષ્ય's refusal in one topic, which is exactly what gate 3 (never end mid-episode) requires.
- The opening scene-setting કડી is its own topic with `topic_category: "introduction"`, as the
  profile prescribes by name for this chapter.

**Apparatus stayed out of the plan.** The teacher-addressed blue પ્રવેશપેટી (p. 71), the ~44-entry
શબ્દાર્થ box and the boxed રૂઢિપ્રયોગ (p. 73), and the chapter-final grammar box
"કાળ અને સહાયકારક રૂપો" (p. 76) are each transcribed under their own **non-સ્વાધ્યાય** markers and
none is a topic. std 7 prints no student-addressed કવિ-પરિચય paragraph, so no CONCEPT topic is owed.

**`guiding_question` is derived from this poem** — "જ્યાં દરેક ચીજ એક જ ભાવે વેચાય છે એ નગરીમાં વાંક
એક જણ પરથી બીજા પર કેમ સરકતો જાય છે, અને છેલ્લે શૂળીએ કોણ ચઢે છે ?" — and reading the ten
explanations in order does answer it: one price → the ગુરુ's warning → the wall → the chain
વણિક → કડિયો → ગારો કરનાર → પખાલી → મુલ્લા → the size test → the ગુરુ's invention → the king on the
શૂળી. Not copied from the profile (the profile's shape question is "આ કડીઓમાં શું બન્યું, અને એ કોણ
કહે છે?").

### B — verbatim and structure

- Every topic's `original_chunk` is **non-empty** and is found **byte-identical** inside
  `00_chapter_normalized.md` once the `[[…]]` scaffolding lines are stripped. Concatenating the ten
  chunks in traversal order reproduces the printed poem's **56 verse lines in printed sequence,
  exactly once each** — checked line-for-line, not by word count.
- Per-topic printed-line ranges walk 1–4, 5–8, 9–16, 17–28, 29–32, 33–36, 37–40, 41–48, 49–52,
  53–56 = 56, agreeing with `kadi_line_counts` `[4,4,4,4,12,4,4,4,8,4,4]`.
- **Script:** zero Roman and zero Devanagari characters in any `original_chunk` or `modified_chunk`,
  and **zero `।` anywhere in the merged plan.** Across the whole merged file the only Roman strings
  are ids, the `genre` slug, the `topic_category` / `topic_type` / `bloom_level` / `difficulty`
  enums, and the media `generation_prompt` / `negative_prompt` (English by contract, read by an image
  model). No bracketed technical term was needed and none appears.
- 19th-century Dalpatram forms survive uncorrected in the chunks and in every quotation of them:
  `ત્યહાં`, `તહાં`, `આંહીં`, `જ્યાંહીં`, `ક્યાંહીં`, `વસીજે`, `સધ`, `તણો`, `નીસર્યા`, `છાંડો`,
  `દિશ`, `ઝાઝા`, `રાતેમાતે`, `ગંડુ`, `પુરી`, `ભૂપ`, `નૃપ`, `પુરપતિ`. Nothing was modernised; the
  chapter's own printed inconsistency (`આંહી`/`જ્યાંહી` in the box against `આંહીં`/`જ્યાંહીં` in the
  verse) is preserved on both sides, neither levelled onto the other.
- Line breaks, the printed stanza gap inside `M1.S2.T3`, the doubled single quotes `‘‘ … ’’`, the
  space before `:` in `કહે શિષ્ય :`, the internal commas of the later couplets and the explicit
  halant in `અદ્‌ભુત` are all as printed. Header furniture never entered the text — the chapter
  number box, the QR code string `S1E4T4` and the running folios appear nowhere.
- **No `[[સ્વાધ્યાય: …]]` block became a topic.** All 17 `verbatim_heading` strings from
  `01_meta.json`'s inventory were matched against every `module_name`, `segment_name` and
  `topic_name`: **zero collisions**, and no topic's provenance named a સ્વાધ્યાય, શબ્દાર્થ,
  રૂઢિપ્રયોગ, પ્રવેશપેટી or વ્યાકરણપેટી marker.
- Ids are consecutive and match traversal position exactly — M1–M3, S1–S6, T1–T10, C1–C12 — with
  zero mismatches.

### C — the teaching block

All ten topics carry non-empty `explanation` **and** `real_life_example`. Word counts, measured on
lexical tokens (see §E–G for the method) and cross-checked under a naive whitespace split, are
**inside band on every field under both counts**:

| field | min | max | band |
|---|---|---|---|
| `explanation` | 75 | 85 (naive 89) | 55–90 ✓ |
| `real_life_example` | 63 | 78 (naive 80) | 55–90 ✓ |
| `objective_text` | 20 | 26 | 12–30 ✓ |

No band was widened and no prose was trimmed by this agent — nothing needed it.

Glossing is at the point of first use and calibrated for L2: `ટકો`, `શેર`, `ખાજું`, `ભાવ`, `હાટ`,
`આટો`, `ખાટવું`, `ખાતર`, `ખૂન`, `ઠાર`, `તણો`, `ખોડ`, `લગાર`, `ચૂક`, `વિશેષ`, `લેશ`, `નીસર્યા`,
`દિશ`, `છાંડો`, `રીસ`, `ફળ`, `ચાકર`, `ભૂપ`, `આપ`, `ગાઉ`, `આંચ` are each explained where they first
appear, in Gujarati, with no Hindi word standing in. The chapter's five names for one king
(રાજા, નૃપ, પુરપતિ, ભૂપ, અધિપતિ) are reconciled in plain Gujarati wherever a new one first
appears — the chapter-level L2 pitfall A7 raised, and it is addressed.

`real_life_example` anchors are Indian, concrete, single and inside std-7 reach, and none repeats:
શેરી-ક્રિકેટ, ઉત્તરાયણ, દરિયાકિનારો (માંડવી), પોળની શેરી, નવરાત્રિનો રાસ, આંગણું, વર્ગખંડ,
શાકની લારી, રિસેસનો ડબ્બો, મેળાનું ચકડોળ.

**Craft ceiling held for std 7.** `figures_of_speech` is `[]` on all ten topics and **no છંદ and no
અલંકાર is named anywhere in the plan** — a full scan for છંદ / અલંકાર / ઉપમા / રૂપક / અનુપ્રાસ /
સજીવારોપણ / ઉત્પ્રેક્ષા / શ્લેષ / યમક / વ્યતિરેક returns zero hits. પ્રાસ is taught as a *sound*:
one sentence per topic after the event is clear, plus `rhyme_scheme`, whose every
`rhyming_words` entry is **two words printed in that topic's own `original_chunk`** (26 pairs,
zero misses). The metre changes mid-chapter at `તસ્કર ખાતર પાડવા, ગયા વણિકને દ્વાર,` and the book
names no છંદ, so none is asserted.

### D — સ્વરૂપ essence

**All 26 `severity: "hard"` items in `07_pitfalls.json` are addressed.** Each was tested against the
fields its own check names:

- **Tacked-on બોધ gate (avoid 5), all ten topics.** Zero hits for `આપણે પણ …`, `આ કાવ્ય આપણને શીખવે
  છે…`, `બોધ એ છે કે…`, `શીખ એ છે` in any `explanation`, `summary`, `detailed_summary`,
  `concept_bullets`, `important_points` or `recall_questions[].answer`. `M3.S6.T10` — where it is
  hardest to resist, since the intro box promises a શીખ the verse never prints — ends on what
  happens: "‘રાજા શૂળી પર રહ્યો, અંગે વેઠી આંચ.’ — છેલ્લે રાજા પોતે શૂળી પર રહી જાય છે."
- **Spoiling-the-turn gate (avoid 9).** `વિમાન`, `ઉગારિયો` and `ઉપાય` appear for the **first time in
  the whole plan** in `M3.S6.T9`; zero occurrences in T1–T8. No topic before `M3.S6.T10` states that
  the રાજા himself ends up on the શૂળી — every earlier king+શૂળી sentence is the king *sentencing
  someone else*, which is the plot and is correct.
- **Community-and-trade gate (avoid 13), the chapter's sharpest item.** વણિક, કડિયો, ગારો કરનાર,
  પખાલી and મુલ્લા are each named as one more innocent person the sentence slides onto; a scan for
  trait words attached to any of them returns **zero hits**. The named target is
  "નગરીનો વિવેક વગરનો ન્યાય" / "સજાનું કારણ ગુનો નથી, દાખલો બેસાડવો છે."
- **Inventing-a-speaker gate (avoid 10).** `‘‘ખૂબ ખાટ્યો.’’` → શિષ્ય, stated twice
  ("ગુરુ નહીં, શિષ્ય બોલે છે."); `‘‘મુલ્લા નીસર્યા મારગે…’’` → પખાલી, and the plan says outright
  "મુલ્લા બોલતા નથી — સાંકળનું આગલું નામ, બસ એટલું જ."; the untagged couplet in `M2.S3.T5` is
  reported as untagged ("આ પંક્તિ કોણ બોલે છે તે કવિ છાપતા નથી").
- **Prose-summarising gate (avoid 4).** Each named topic's `explanation` quotes at least one phrase
  character-for-character from its own chunk — `લીધી સુખડી હાટથી આપી આટો`,
  `રહ્યા શિષ્યજી તો ત્યહાં દિન ઝાઝા`, `ફળ જાડું શૂળી તણું, મુલ્લા પાતળે અંગ,`,
  `આ અવસર શૂળીએ ચઢે, વેગે મળે વિમાન.` — and adds motive the `modified_chunk` does not carry.
- **Old measure and coin gate (avoid 12).** `ટકો`, `શેર`, `ખાજું` and `ગાઉ` carry the printed
  શબ્દાર્થ box's own wording only. No rupee price, no kilogram, no kilometre, no "today it would
  cost" figure anywhere.
- **Modernising-the-poet gate (avoid 11).** The verse's `નહીં યોગ્ય આંહીં રહ્યો રાતવાસો.` and
  `મારી ચૂક ન લેશ.` are what the teaching quotes; the exercise page's `રહ્યે` and `ના લેશ` stay in
  the exercise deliverable. Neither printed form is corrected.
- **Craft-displacing-the-story gate (avoid 6).** The first sentence of `explanation` on both named
  topics opens on a character and an action ("ગુરુજી છેલ્લી વાર સમજાવે છે…", "ચેલો સૌથી પહેલો કૂદી
  પડે છે…"), not on લય/છંદ/પ્રાસ/અલંકાર.
- **Numbers-in-display-text gate (avoid 14), `M1.S2.T3`.** Zero digits and no `કડી 3` / `કડી 4`
  anywhere in that topic's display text.

**Both `severity: "hard"` items in `08_sensitivity.json` are addressed**, and its `areas[]` draw
only on the seven fixed labels (ધર્મ ×2, વિકલાંગતા, plus chapter-level સંઘર્ષ and સુરક્ષા):

- `M2.S4.T7` (ધર્મ, hard) — the મુલ્લા is explained exactly as કડિયો and પખાલી before him
  ("સાંકળ જેના પર જઈ પડી એવા એ બીજા નિર્દોષ માણસ છે"), no trait, no comment on faith; the anchor is
  a classroom blame-chain, not religion.
- `M2.S5.T8` (ધર્મ, hard) — the explanation stays on the absurdity of the king's rule
  ("કોણે શું કર્યું એ સવાલ રહ્યો નથી, હવે માપ જ જોવાય છે"); the anchor is a vegetable-seller
  balancing a scale; the recall answers stay on "the wrong person got blamed", never on belief.
- `M2.S3.T5` (વિકલાંગતા, soft) — `ખોડ` carries the printed gloss **plus** its idiomatic sense here
  ("અહીં 'મારી જરાય ખામી નથી' એ અર્થમાં"), and the anchor is a દાંડિયા mis-step, not a person's body.
- Chapter-level સંઘર્ષ / સુરક્ષા — the શૂળી is never made graphic and the execution is never
  endorsed; the dramatisation block's `teacher_note` carries the mime-it-symbolically guidance.

`figures_of_speech` is `[]` on every topic, so invariant 11 holds vacuously and correctly — no
device was named because the field existed.

### Contract — the 12 `json_contract.md` invariants

| # | invariant | result |
|---|---|---|
| 1 | `phase: 2`; `plan_id = {chapter_id}_v{version}`; `chapter_id = gseb_eng_gujarati7_ch11` | ✓ (board/medium segments provisional — Gap 4) |
| 2 | every `original_chunk` non-empty, Gujarati-script, no Roman/Devanagari | ✓ 10/10 |
| 3 | every topic ≥1 concept, valid `concept_id`, resolving `objective_id`, non-empty `content[]` | ✓ 12 concepts |
| 4 | root `objectives[]` complete and consistent | ✓ O1–O10 unique, all `home_topic_id` and all 12 `anchor` ids resolve, `strand_to_objective_map` covers L1–L10 exactly once, zero orphans |
| 5 | inline mirrors match the registry character for character | ✓ 10/10, each with `image_examples: []` |
| 6 | `MEDIA_ID_RE` concept-scoped; `RQ{n}` + `TR{n}`; **never `.SR{n}`** | ✓ 10 media ids, 30 recall pairs, zero `.SR` in the file |
| 7 | no સ્વાધ્યાય block is a topic; every inventoried block answered | ✓ 0 collisions; 17/17 blocks, 72/72 items |
| 8 | three-tier summaries strictly increase | ✓ 10/10 (e.g. 16 < 32 < 83 words) |
| 9 | no numbers in display text | ✓ zero digits in any name, explanation, example, summary, bullet, prompt, recall answer, concept name, media title/description/teaching_note, objective_text, module/segment name or the `2d_tool` spec (one `key_terms` note — see §E–G) |
| 10 | media (soft) | ✓ — see Media below |
| 11 | `figures_of_speech` lines found verbatim | ✓ vacuous — all `[]` |
| 12 | every reference survives renumbering | ✓ all `depends_on`, `objective_ids`, `anchor`, `home_topic_id`, media and recall ids resolve today; `04_converged.json` freezes the id set for Agent 14 |

Concept numbering is **chapter-continuous** — `M2.S3.T4` carries C4+C5 and `M2.S3.T5` carries C6, so
the concept number stops equalling the topic number from C5 onward. That is correct under
`phase2_contract.md`; A4 flagged it for Agent 14 and the flag is carried forward here (Gap 9).

### Exercises

`coverage_report.blocks_found` = **17** = the length of `01_meta.json`'s `exercise_inventory`,
entry for entry **in printed order** (blocks 1–17, folios 74–76); every heading matched exactly, so
fuzzy matching was not needed. `blocks_answered` mirrors it entry for entry. **`unanswered` is
empty**, and all **72** printed items carry a non-empty `answer`
(8+7+18+5+5+7+4+1+1+1+3+1+1+1+5+1+3 = 72, which is the inventory's own item sum). Every
`covered_by_topics` id resolves to a real node; none is invented. 16 items are marked
`is_model_answer` (the personal-opinion, પ્રવૃત્તિ, જૂથકાર્ય and teacher-addressed ones). Skills:
reading comprehension 24, literary device 18, speaking 13, grammar 12, listening 4, vocabulary 1.

`unmapped` carries **19** entries and is **reported, not emptied** — see Gap 6.

### Media

`reuse_report`: `scenes: 10`, `authored: 10`, `reused: 0`, `rejected: []` — and 10 is exactly the
count of topics whose `available_content_types` carry `"image"` (all ten). Every node carries
`image_url: ""` **and** a non-empty, self-contained `generation_prompt`; no `[reused frame: …]`
stamp anywhere; every `negative_prompt` carries `Devanagari script labels` (and, chapter-specifically,
`digits or numerals anywhere in the frame`, `price boards`, `written signboards` and
`caricature or mockery of any religious or occupational community`). Media ids are concept-scoped
and match `MEDIA_ID_RE`. **One image per reading scene is 10 of 10.**

Exactly **one `2d_tool`** in the whole chapter, on `M3.S6.T10` — an event-order strip earned by the
chapter's own printed ordering block (`નીચેની પંક્તિઓ ઘટનાક્રમમાં ગોઠવીને ફરીથી લખો.`). It names the
exact Gujarati on-screen string to render (`પંક્તિઓને કાવ્યમાં જે ક્રમે બની તે ક્રમે ગોઠવો.`),
identifies cards by icon rather than by number, and leaves the written answer to the સ્વાધ્યાય
deliverable.

### Publication

All 10 topics carry `publication_text` and `publication_chunk`. Each `publication_chunk` contains its
topic's `original_chunk` **byte-identical**, unreflowed and unrepunctuated, as its opening block —
the rewrite did not touch the verbatim. `concept_publication` matches `concepts[].content[]` **by
index and by count** on every topic: twelve paragraph blocks across twelve concepts, in order, none
renumbered, reordered or dropped, and every `list` block correctly carries no `publication_text`.
The classroom address is gone — `બાળકો`, `જુઓ —`, `બોલો`: **zero hits** in any `publication_text`
or `concepts[].content[].publication_text`.

**No meaning was added.** A character-level diff of all ten `explanation` → `publication_text` pairs
shows only removals and tense shifts and nothing else: `બાળકો, જુઓ — ` deleted (T1, T2),
`જુઓ — ` deleted (T7), `ધ્યાન રાખો` deleted (T6, T9), `હવે એનો હુકમ સાંભળો` → `એનો હુકમ આવો છે` (T8),
`…શે` → `…ે છે` (T4, T5, T6); T3 and T10 are byte-identical to the teaching text, which is the
correct outcome for blocks that carried no vocative.

> **Note on the checklist wording.** Agent 13's spec says "`publication_chunk` is byte-identical to
> `original_chunk`". Read literally that contradicts `agents/16_publication_authoring.md`, which
> defines `publication_chunk` as the whole publication-facing block **with the verbatim
> `original_chunk` kept verbatim inside it**. The check was run in the sense the rule protects —
> the `original_chunk` substring inside `publication_chunk` is byte-identical on all ten topics, and
> it is the chunk's opening block. Flagged so the spec text can be reconciled with 16's, not treated
> as a defect in this chapter. (The same note stands in `output7/ch08/` and `output7/ch10/`.)

---

## E–G (reported)

- **Word-count method.** Bands are counted on *words*: tokens carrying at least one letter. Gujarati
  typography spaces `:` `?` `!` `—` off as free-standing tokens, so a naive whitespace split inflates
  the count. This chapter is inside band under **both** counts — the widest naive value is 89
  (`M2.S3.T5`, `M2.S4.T7`, `M2.S5.T8` explanations), one word under the ceiling — so nothing turns on
  the method here. Recorded for consistency with `output7/ch02` and `output7/ch10`.
- **E — સ્વાધ્યાય and risk.** All 17 printed blocks answered and skill-tagged; 16 model answers,
  each marked as one possible response; the printed કોષ્ટક (block 15) and the ક્રિયારૂપ grid
  (block 17) are filled with teaching values rather than left as grids. The dramatisation block
  (14) and the singing block (13) are answered as methods, not skipped. Sensitivity notes are
  applied inside the exercise deliverable too — block 14's `teacher_note` carries the
  mime-the-શૂળી-symbolically guidance, block 11's the "keep it off the મુલ્લા's faith" guidance.
- **F — `ordering`** is deliberately absent; the root key count is therefore 31 of the contract's 32.
- **F — `publication_id` is `null`** and the server rejects null. See Gap 3.
- **F — script whitelist.** Nothing in this chapter needs the printed-non-Gujarati whitelist: the
  reading text is entirely Gujarati script and `01_meta.json`'s `extraction_notes[]` raise no
  non-Gujarati printed content. `10_exercise_solutions.json` carries **zero Devanagari**; its Roman
  strings sit only in `teacher_note`, which is mechanism prose in English by design. Block 9's
  printed paragraph keeps its Roman numeral `2013` as the page prints it — provenance, not display.
- **F — one digit sits in a `key_terms` gloss.** `M1.S1.T1` carries
  `શેર — વજનનું જૂનું માપ; મણનો ચાળીસમો ભાગ (500 ગ્રામ)`. `(500 ગ્રામ)` is the **printed શબ્દાર્થ
  box's own wording**, quoted rather than authored, and A7's hard old-measure gate explicitly
  requires that wording. `key_terms` is not one of the fields the digits rule enumerates (names,
  explanations, examples, summaries, bullets, prompts, recall answers), and the number is a
  measurement gloss, not a structural reference (`કડી 2` / `પ્રશ્ન 4`). Reported so the choice is
  visible; **not treated as a defect**, and not silently edited — editing it would break the A7 gate.
- **G — the seven usual mistakes:** (1) not સાર+બોધ+પ્રશ્નોત્તર — the plan teaches the ઘટના chain and
  the joke; (2) no દુહા merged (0 દુહો markers, and A1 declined to call the later couplets દુહા
  because the book neither labels nor prints them as such); (3) no પદ split and no ટેક lifted
  (0 ટેક); (4) no poetic licence corrected — see §B; (5) no અલંકાર named — `figures_of_speech` is
  `[]` everywhere; (6) anchors are std-7-sized and Indian; (7) સ્વાધ્યાય is fully answered in its own
  deliverable and none of it became a topic.
- **A4's non-blocking notes travel here.** (a) `01_meta.json` and `02_structure.json` disagree on
  where the climax sits — meta's `explanation_unit` wording puts વળાંક and પરિણામ together on the
  last કડી, while A2 follows `kathakavya.md` §Emphasise and marks `M3.S6.T9` (`વેગે મળે વિમાન`)
  `climax` and `M3.S6.T10` `resolution`. A2 recorded the disagreement openly and followed the
  profile, which is the unit authority. The downstream consequence — enforce the spoiler gate
  against **both** boundaries — was enforced and passes. (b) `topic_type` is `POEM` on all ten topics
  although the cut is ઘટના-wise; both authored values are defensible for a કથાકાવ્ય and both map to
  `instructional` at Agent 14/15, so nothing downstream turns on it. (c) Topic length is uneven —
  `M2.S3.T4` is a 12-line કડી (71 words) against `M1.S2.T2`'s 23 — the unit is the ઘટના and gate 1
  forbids splitting a કડી, so this is reported, never fixed.

---

## Media

`scenes: 10` · `authored: 10` · `reused: 0` · `rejected: []` · `2d_tool: 1` (`M3.S6.T10`).

**`Images: 0/10`** — the zero is written, not omitted: no Gujarati frame pool exists, so reuse is
dormant and every scene carries an authored prompt with `image_url: ""`. No rejected frames to
report, because no pool was searched.

---

## Gaps

Honest absences, all reported, none blocking:

1. **`textbook_url` is a local path** — `../Textbooks-pdf/std-7/ch-11-andheri-nagari.pdf`. The GSEB
   readers have no hosted URL (`11_pages.json` `gaps[]`). The renders for this run came from a copy
   of the same unit at `gujarati-lp/book/ch-11-andheri-nagari.pdf`.
2. **`chapter_master_id` is `null`.** Required for upload; the GSEB row must be fetched from the
   education DB (VERIFY-2). `upload_reference/chapter_master_map.json`'s row for
   `gseb_eng_gujarati7_ch11` is the provisional all-null row and says in terms "Never invent an id".
   The Hindi pack's `355 − chapter number` is CBSE provenance and does not transfer.
3. **`publication_id` is `null`, and the server rejects null.** Agent 13's spec asks for a non-null
   provisional value; the registry holds no GSEB publication row, and inventing one — or borrowing
   CBSE's `1`, which `phase2_contract.md` names as not portable — is a `no_hallucination_policy.md`
   violation. `null` is written, matching `ch01`, `ch09` and `ch10`. **This must be filled with the
   verified GSEB publication row before the first Phase 8 upload (VERIFY-2)** — an upload blocker,
   not a content one, and `publication_id` sits in the checklist's **§F (reported)**, not in A–D.
   The pack is currently inconsistent about it: `ch02`–`ch08` wrote `1`, while `ch01`, `ch09`,
   `ch10` and this chapter wrote `null`. Whichever VERIFY-2 lands, all fifteen std-7 chapters need
   the same value.
4. **`chapter_id` / `plan_id` board and medium segments are provisional (VERIFY-1).** A wrong medium
   slot uploads clean and mis-files the plan.
5. **`subject_ref_id` and `medium_id` are `null`** — server-injected; no confirmed GSEB subject
   record exists.
6. **19 exercise items are `unmapped`, and the report was not closed by inventing mappings.** They
   are the ones no reading scene of this chapter prepares, and A10 gives a reason for each: the
   milk-foods vocabulary warm-up (EX2); the four pronunciation tongue-twisters (EX51–54); the modern
   non-fiction salt-survey paragraph and the two blocks scored on it (EX56, EX57); the tense-drill
   and grammar-table items (EX58–60, EX64–68, EX70–72); and the library activity (EX62). All are
   exercise-page matter with no counterpart in the poem — **nothing was missed by the cut.**
7. **Root `genre` records the slug `kathakavya`, not `01_meta.json`'s `"કથાકાવ્ય"`.**
   `phase2_contract.md` requires a slug and `05_with_content.json` already carries one. Reported for
   A1 to align `01_meta.json`; not a blocker. Note the pack is inconsistent here too — `ch01`,
   `ch05`, `ch06` and `ch09` shipped Gujarati-script `genre` values.
8. **Root `topic_number` is `11`, taken from `01_meta.json`** (`= unit_number`). Sibling std-7
   chapters disagree: `ch02`–`ch05` set `topic_number = unit_number` while `ch01`, `ch06`, `ch08`,
   `ch09` and `ch10` set `1`. Reported for A1; the value was not overridden here.
9. **Concept numbering stops equalling topic numbering from C5 onward** — `M2.S3.T4` carries C4+C5
   and `M2.S5.T8` carries C9+C10, so `M3.S6.T10` carries C12. This is correct under
   `phase2_contract.md` ("`c` is chapter-continuous"), but **Agent 14's renumber must preserve
   continuity across the traversal, not the one-concept-per-topic equality** shown in that file's
   example row. Carried forward from `04_validation.json`.
10. **`ordering` is absent from `13_merged.json` by design** — Agent 14 sets `"logical"` and
    Agent 15 `"textbook"`.
11. **`05b_textbook_order.json` matches the logical traversal exactly** (T1 → T10, the whole poem on
    printed folios 71–72). Per `phase2_contract.md` §Ordering this must be raised for human
    confirmation at emit: `{"human_confirmation_required": true, "reason": "textbook order is
    identical to logical order", "checked": "05b_textbook_order.json matches the logical traversal
    exactly"}`.
12. **The attribution line is at the head, not the foot.** `gujarati_verbatim.md` §5 puts
    `— કવિનું નામ` inside the last topic's `original_chunk`; here `- દલપતરામ` is printed under the
    title on p. 71 and **nothing follows** the last verse line
    `રાજા શૂળી પર રહ્યો, અંગે વેઠી આંચ.`. The last topic's chunk therefore ends at that verse line.
    Recorded by A1 as a measured fact about the page, not an omission — and the phase-2 contract has
    no author field, so the credit rides only in `00_chapter_normalized.md` and `extraction_notes[]`.
13. **Printed peculiarities carried through, each with the repair noted rather than applied:** the
    poem prints `નહીં યોગ્ય આંહીં રહ્યો રાતવાસો.` (p. 71) where exercise block 4 prints `રહ્યે`;
    block 6 prints `મારી ચૂક ના લેશ.` where the verse prints `ન લેશ`; blocks 4 and 6 drop the poem's
    internal commas; the શબ્દાર્થ box prints `ખોડ` twice with the same gloss and spells
    `આંહી`/`જ્યાંહી` without the anusvāra that the verse carries; the grammar box prints
    `આ કોષ્ટકનો અભ્યાસ કરો :.` and `‘ખાઈએ છીએ છીએ,’`. None was levelled onto the other; each is
    verified at 5×–6× and recorded in `extraction_notes[]`.
14. **Re-rendering was forbidden for this run**, so A1's spec'd double-render cross-check at higher
    dpi could not be performed as written. The substitute actually run — every verse and exercise
    line re-read against 2×–6× LANCZOS upscaled crops of the supplied 1300×1831 px (≈150 dpi)
    renders, plus a per-row ink-profile measurement of the stanza gaps — is recorded in
    `extraction_notes[]` as a **method substitution, not a clean pass of the stated check**. It
    corrected the corpus prior: `reference/corpus/std-7_inventory.md` records "~17 stanzas"; the page
    prints 11 blocks totalling 56 lines. No transcription defect was found against the renders by
    A5 or A10, and nothing was repaired.
15. **`concepts[].key_terms` is `[]` on all 12 concepts.** The glosses live at topic level
    (`key_terms`, 6 per topic, `શબ્દ — અર્થ`) and in `shabdarth`. The contract does not require the
    concept-level array to be non-empty; noted so its emptiness reads as a choice, not a loss.
16. **No page render was opened by this agent.** Every question this gate asked was answerable from
    `00_chapter_normalized.md` and the upstream JSON — the byte-exact line-range and marker-count
    checks against the transcription were the stronger test.

---

## LP2 validator

Not run — filled in Phase 8. `POST /api/lp2/learning-plans/validate` must return zero
`validation_errors`, and `chapter_master_id` plus the real GSEB `publication_id` (Gaps 2 and 3) must
be in place before that call. On today's file the validator will report one error:

```
root: 'publication_id' is required and must not be null
```

---

**Verdict: A–D PASS. No blocking failure. `13_merged.json` is complete and ready for Agent 14.**

## LP2 validator
- Status: FAILED (validation_errors present)
- validation_errors:
  1. root: 'publication_id' is required and must not be null
- Raw response: {"success":false,"action":"validated_only","plan_id":"gseb_eng_gujarati7_ch11_v1","version":null,"phase":null,"is_active":null,"is_draft":null,"counts":null,"diff":null,"publication_id":null,"publication_name":null,"validation_errors":["root: 'publication_id' is required and must not be null"],"message":"1 validation error(s)"}
