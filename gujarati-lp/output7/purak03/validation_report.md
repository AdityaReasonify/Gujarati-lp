# Validation Report — std 7, ch 18 (પૂરક વાચન 3) · રામરાજ્યનાં મોતી

સ્વરૂપ: `varta` — sub-form **પૌરાણિક વાર્તા (દૃષ્ટાંતકથા)** (confidence: high)   explanation unit: **એક ઘટના**
Topics: 6   Objectives: 6   Images: 0/6   Exercises: 0/0 (the unit prints no સ્વાધ્યાય; one deliverable, not two)

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` → `13_merged.json` (31 root keys, 37 topic keys, 3 modules,
5 segments, 6 topics, 6 concepts, 6 media nodes, `2d_tool: null`). `ordering` is deliberately absent —
Agent 14/15 sets it, not this agent.

**Identity.** This is the third પૂરક વાચન piece of the std-7 reader (printed pp. 115–118, file
`purak-03-ramrajyana-moti.pdf`). `chapter_id` `gseb_eng_gujarati7_ch18`, `unit_number` and
`topic_number` 18 are **orchestrator provenance**, required so `{board}_{medium}_{subject}{grade}_ch{N}`
validates; the page itself prints a plain `3.` in its number box. Purak units continue the numbering
after the book's 15 numbered chapters (P1→16, P2→17, this P3→18, P4→19). Recorded in
`01_meta.json`'s `extraction_notes`; `chapter_master_id` stays `null` as the run context requires.

No working field survived the merge. Dropped: `markers`, `source_lines_00_normalized`, `cut_summary`,
`not_cut_as_topics`, `converged_source`, `verbatim_notes`, `unit_type_note`, `genre_subform`,
`explanation_unit`, `active_genre_profiles`, `genre_signals`, `genre_confidence`,
`structure_inventory`, `extraction_notes`, `exercise_inventory`, pitfall `avoid_checks` /
`misconception` / `correction`, sensitivity `areas` / `caution` / `guidance` / `severity`, media
`reuse_report` and the routing key `topic_id` on each media node, publication `concept_publication`
(folded into `concepts[].content[].publication_text` by index), authoring `tier`, and every agent's
`notes[]`. A recursive key scan of the merged file found none of them. Only contract keys ship.

Verification method: 81 mechanical checks were run against the merged file and its input layers
(script kept outside the output directory). 80 pass. The one that reports FAIL is the **literal**
reading of this spec's `publication_chunk` wording, discussed under Publication and Gap 8 — it is a
conflict between two spec files, not a defect in the chapter. No render PNG was opened: the
transcription answered every question this run had.

---

## A–D (blocking)   **PASS**

### A — diagnosis and lens

`01_meta.json` records the signals off the rendered page, and the book names its own subject in the
blue પ્રવેશપેટી (p. 115), quoted as **evidence, not verdict**: "આ એક પૌરાણિક વાર્તા છે, જેમાં આદર્શ
રાજ્ય કેવું હોય એનું સરસ દૃષ્ટાંત આપવામાં આવ્યું છે." Measured signals: prose with named પાત્રજૂથો
(રાજા, કાગડો, ચાર ઉત્તમ પુરુષો, પ્રધાન, રાજાનો ભાઈ, રાણી, ઝવેરી), a chain of ઘટના, dialogue inside
quotes, one embedded પૌરાણિક કથા (the crow's સીતા–રામરાજ્ય tale), and a વળાંક. The page and the
board profile's std-7 purak prior agree; `genre_confidence: high`. `structure_inventory` records
`kadi: 0, duha: 0, pad: 0, tek_occurrences: 0`.

**Explanation unit matches the roster row.** વાર્તા — one ઘટના. Verified mechanically against
`00_chapter_normalized.md`: **6** `[[ઘટના: …]]` markers, **0** `[[કડી …]]` / `[[દુહો …]]` /
`[[પદ …]]`, **0** `[[સ્વાધ્યાય: …]]`; **6** topics carrying **6** `markers[]` entries between them,
one each, in printed order M1.S1.T1 → M3.S5.T6.

- **Apparatus stayed apparatus.** `[[પૂરક ક્રમાંક]]`, `[[પ્રવેશપેટી]]`, `[[શબ્દાર્થ]]` (16 entries) and
  `[[કહેવતો/રૂઢિપ્રયોગ]]` (4 entries) are not nodes in the merged plan, and none of their text sits
  inside any `original_chunk`. The પ્રવેશપેટી's last sentence is teacher-addressed ("આ એકમ ભણાવતી વખતે
  …"), so it is not the std-10 student-facing કવિ-પરિચય shape that would earn a CONCEPT topic.
- **The bard's two stanzas stay inside M1.S1.T1** as quoted verse inside a prose scene, per
  `varta.md` ("couplets quoted inside a scene stay verbatim inside that scene's topic"). They are
  not a પદ topic, and no ટેક handling arises.
- **Not a mixed chapter:** `active_genre_profiles` is `varta.md` alone. The frame story and the
  embedded કથા are both prose and stay under one unit; the embedded tale is a separate ઘટના
  (M3.S4.T5) opened by its hand-over sentence, exactly as the frame-story rule asks.
- No revision-checkpoint or વ્યાકરણ unit is involved.

`guiding_question` — "સાચું રામરાજ્ય એટલે શું, અને આ રાજાનું રાજ્ય એના જેવું કેમ નથી — એ કાગડો કેવી
રીતે સાબિત કરે છે ?" — is derived from this chapter (it is not the profile's shape) and could fit no
other. Reading the six explanations in order does answer it: the song's claims and the crow's denials,
the four men who hide a pearl each, the court's chain of grabbing, the count that exposes everyone,
the tale in which no one touched the plate, and the crow's yardstick.

### B — verbatim and structure

- All 6 `original_chunk` values are non-empty and **byte-identical** to `05_with_content.json` after
  the merge (asserted programmatically; nothing was reflowed, re-spaced or re-punctuated).
- Every chunk was matched against `00_chapter_normalized.md` by its true line range. Five of six are
  **byte-for-byte** equal; M3.S4.T5 is equal word-for-word and differs in one separator only (see
  Gap 11).
- Script: the base script is Gujarati (U+0A80–0AFF) throughout (Gujarati-letter ratio 0.92–0.96 per
  chunk, the remainder being punctuation, spaces and quote marks). **Zero** Roman and **zero**
  Devanagari characters, and **no `।`**, in any `original_chunk`, `topic_name`, `concept_name`,
  segment/module name, `explanation`, `real_life_example`, summary, bullet, `key_terms` entry, recall
  prompt/answer, concept content block, `objective_text`, `publication_text`, `modified_chunk`, or
  media `title` / `description` / `teaching_notes`. No media prompt carries a Devanagari character.
  The §"What the script check must not flag" whitelist does not arise: this unit prints no
  non-Gujarati content and `extraction_notes[]` records none.
- Printed oddities recorded by Agent 1/5 stand intact in the verbatim and were **not** corrected:
  `અંદરોઅદર`, `કપડાંમા` (no અનુસ્વાર), `ઘરઆગળ`, `વીત્યા` beside `વીત્યાં`, `રામ રાજ્યનાં` written apart in
  the crow's last speech, the minister's two lines printed without quotation marks, and the three
  unmatched single quotes (`' વર્ષો વીત્યાં`, `'આમ કહી …`, `'હેં, થાળ ક્યાં ગયો ?`).
- This unit prints no author byline, translator line or source note, so there is no attribution
  line to carry in the last topic and nothing was dropped.
- Header furniture (the number box `3.`, the intro box, the two apparatus boxes) never entered a
  chunk. There is no QR badge on a પૂરક unit.
- Ids consecutive and traversal-consistent: modules `M1..M3`, segments `M1.S1..M3.S5` (1–5, never
  restarting), topics `T1..T6`, concepts `C1..C6` **chapter-continuous**. Every id was checked
  against its traversal position, which is the check the LP2 validator itself performs.
- `word_count.original` equals the whitespace-token count of each chunk: 154, 118, 151, 262, 253, 227.

### C — the teaching block

Every topic has non-empty `explanation` **and** `real_life_example`. Measured word counts, inside
the 55–90 band under **both** counting methods (whitespace tokens / without stand-alone punctuation):

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 85 / 79 | 63 / 58 |
| M2.S2.T2 | 84 / 81 | 63 / 62 |
| M2.S3.T3 | 76 / 66 | 64 / 59 |
| M2.S3.T4 | 88 / 81 | 63 / 60 |
| M3.S4.T5 | 86 / 80 | 69 / 66 |
| M3.S5.T6 | 87 / 83 | 67 / 65 |

`objective_text` word counts: O1 27, O2 22, O3 25, O4 30, O5 24, O6 30 — all inside 12–30 (O4 and O6
sit on the ceiling; no band was widened and no prose needed trimming).

Voice and L2 calibration hold: second person (`બાળકો, જુઓ —`), સરળ બોલચાલની શિષ્ટ ગુજરાતી, one new
thing per sentence, and glossing at the point of first use (`લલકાર્યું`, `જાણે`, `મેહ`, `મજલ`, `નિર્જન`,
`અંદરોઅદર`, `તિજોરી`, `સેરવવું`, `આરોપ`, `તાણી`, `ખૂટે`, `હઠ`, `પારણું`, `અર્પણ`, `પ્રતિહારી`, `ગજ`,
`લોભ`, `સ્પર્શ`, `અદૃશ્ય`). The printed રૂઢિપ્રયોગ box is this chapter's real L2 trap and each idiom is
glossed with the book's own words where it occurs. Anchors are Indian, concrete, single and inside a
std-7 child's reach — શેરી ક્રિકેટ, ગોળપાપડીનો ડબ્બો, એસ.ટી. બસમાં રહી ગયેલી થેલી, ઉત્તરાયણની
ફિરકીની ગૂંચ (a પોળ rooftop with a friend named ઇમરાન as a lived moment), નાનીનો ઓટલો, મેળાનો
ફુગ્ગો — six different pictures across four of the anchor bank's domains (રોજિંદું જીવન, ખાનપાન,
કામ-આજીવિકા, તહેવાર-ઉત્સવ), none needing its own glossary. Craft naming: a scan for ઉપમા, રૂપક,
અલંકાર, છંદ, વ્યંગ, કટાક્ષ, કથામાં-કથા, સાહિત્યપ્રકાર, પ્રાસ, સમાસ, સજીવારોપણ across every authored field
returned **zero** hits, which is correct for std 7. A limited scan for common Hindi stand-ins
(`બહુત`, `લેકિન`, `ઔર`, `હૈ`, `કૈસે`, `ક્યોંકિ`) also returned zero; this one is a spot check, not a
proof.

### D — સ્વરૂપ essence

`07_pitfalls.json` instantiates **15 hard** avoid-checks across the 6 topics (plus 10 soft);
`08_sensitivity.json` carries **2 hard** items (M3.S4.T5, M3.S5.T6). Each was re-run mechanically
against the merged plan's authored fields:

- **Gate 1 — summary-only teaching.** No `explanation` equals its `modified_chunk`. The topic-specific
  content each hard check demands is present in `explanation`: T1 sets the song's two claims
  (`સૌ સુખી`, `માગતાં … મેઘવૃષ્ટિ`) beside the crow's two denials and glosses `જાણે`; T2 sets 'ઉપાડો થાળ !
  આપણે એ રાજાની કચેરીમાં રજૂ કરવાનો છે.' beside the hiding, using the printed word `છુપાવી`; T3 names the
  three unasked questions (`થાળ કોનો છે`, `ક્યાંથી આવ્યો`, `શા માટે છે`) and the `સીધો હુકમ`; T4 gives the
  count once and names the cues (`આરોપ`, `કરડી આંખ`, `બીતાં બીતાં`) with **zero** hits for `પસ્તાવો`,
  `શરમ`, `ભૂલ સમજાઈ`, `અંતરાત્મા`; T5 ties the tale to the court by the printed objects (`સોનાનો થાળ`,
  `અઢાર મોતી`, `ઘંટ`, `વડ`) and glosses `દીકરી`; T6 carries the crow's yardstick sentence and glosses
  `ગજ` as a measure, "હાથી નહિ".
- **Gate 2 — tacked-on બોધ.** Scanned `explanation`, all three summaries, `concept_bullets`,
  `important_points` and every recall `answer` for `આ વાર્તા આપણને`, `શીખવે છે`, `બોધ`, `આપણે પણ`,
  `જોઈએ`, `સમાનતા`, `બંધુતા`, `ન્યાયપ્રિયતા`, `પ્રામાણિકતા`, `લોભ ન`. The only hits are three `જોઈએ` inside
  the ઝવેરી's own printed line 'હાર માટે પૂરાં અઢાર મોતી જોઈએ' (M2.S3.T3). The પ્રવેશપેટી's
  teacher-addressed aim was **not** recycled as a child-facing moral anywhere. Closing sentences of
  every explanation and summary were read: none ends on a moral. The chapter's own printed moral
  'લોભનો સ્પર્શ થયો એટલે એ અદૃશ્ય થઈ ગયાં !' is quoted verbatim in M3.S5.T6 and followed by nothing.
- **Gate 3 — judging a sympathetic character.** `ગાંડ` appears in **no** authored or publication field
  of any topic (only inside the શેઠ's printed words in M3.S4.T5's `original_chunk`). The one `ખોટો`
  hit is the book's own શબ્દાર્થ gloss `હઠ — જીદ, ખોટો આગ્રહ` carried in Agent 5's `key_terms`, which
  `07_pitfalls.json` expressly permits ("glossed … without becoming a verdict"). No label of any kind
  falls on the નગરશેઠની પુત્રવધૂ, the tale's નગરશેઠ or the પ્રતિહારી, who covers the plate because it
  'વચમાં નડ્યો'. The કલાકાર is never called જૂઠો/ખુશામતખોર; the idiom 'જૂઠાને માથે છી !' is quoted only
  as the crow's cry with the book's gloss.
- **Gate 4 — spoiling the turn.** `topic_category: "climax"` sits on M2.S3.T4. Every banned word in
  `07_pitfalls.json`'s per-topic lists was searched in T1, T2 and T3 across `explanation`,
  `brief_summary`, `summary`, `detailed_summary` and every recall `answer` (the gate's own fields):
  **zero hits** in all three. A wider scan of every display field (real_life_example, bullets,
  key_terms, concept content, `publication_text`, media titles/descriptions/teaching notes) found
  **no** hit in T1 or T2, and in T3 only the word `ચોરી` inside `topic_name` / `concept_name` — see
  Gap 15. T4's and T5's soft stop-lines hold: T4 stops on the king's question 'હું કેવો છું ?' and
  names no ending; T5 stops on the વડ and names none of અદૃશ્ય, `લોભનો સ્પર્શ`, કાકભુશુંડી, nor any
  added fact (વનવાસ, રાવણ, લવ-કુશ, જનક, રામાયણ, રામચરિતમાનસ).
- **Gate 5 — debunking / verifying a પૌરાણિક કથા.** Zero hits for ખરેખર, વૈજ્ઞાનિક, કલ્પના, કલ્પિત, જાદુ,
  સપન, ભ્રમ, વાસ્તવ, ઇતિહાસ, હકીકત, વાર્તામાં જ, દંતકથા, માન્યતા in any field. The speaking crow is
  'કાગડો કહે છે' throughout. T6's vanishing is supplied with **no** mechanism: no સંતાડ, no `કાગડાએ
  લઈ`, no જાદુ, no ભ્રમ, no સપન anywhere in T6's fields — the only cause is the crow's printed
  'લોભનો સ્પર્શ થયો એટલે'.
- **Gates 6, 7, 8** name sub-forms this unit is not (લોકકથા dialect, excerpt, translated story); the
  unit is a complete tale with no byline, so no field supplies an author, translator or source book.
- **`figures_of_speech: []` on all 6 topics**, `rhyme_scheme: null`, `overall_rhyme_scheme: null` on
  all 3 modules. This is ગદ્ય below the std-9 named-device gate; the empty list is the complete
  answer, so the verbatim-quotation check has nothing to fail on and no device was invented.
- **Sensitivity (`08_sensitivity.json`):** `areas[]` drawn only from the seven fixed labels (ધર્મ,
  જાતિ-ભૂમિકા, સુરક્ષા). **Two hard items, both addressed.** M3.S4.T5 (ધર્મ, જાતિ-ભૂમિકા): taught as the
  crow's tale with no claim it did or did not happen; સીતાજી's two printed sentences are joined and
  the refusal is her own stated reason, with no second cause added; `ગાંડી હઠ` is never reused;
  the example is a grandmother's lap, not a વ્રત instruction; and in the media layer સીતા is **not
  drawn** (no likeness, deity-like figure, halo or idol). M3.S5.T6 (ધર્મ): the crow's lineage and
  the disappearance are taken at face value; the printed moral is quoted without an appended one;
  recall answers stay on what the court saw; the frame shows the result (empty hands, no plate, no
  pearl, no sparkle or smoke) and not a mechanism. The soft T3 item (સુરક્ષા) holds too: the sword
  appears only as one link in the chain, and in the image prompt it stays sheathed with the hand
  away from the hilt while the negative prompt refuses a drawn or raised sword.

### Contract — the 12 `json_contract.md` invariants

1. `phase: 2`; `chapter_id` = `gseb_eng_gujarati7_ch18`; `plan_id` = `gseb_eng_gujarati7_ch18_v1`. ✔
2. 6/6 non-empty Gujarati-script `original_chunk`, no Roman, no Devanagari. ✔
3. 6/6 topics carry ≥1 concept; 6 concepts, each with a valid id, a resolvable `objective_id`, and
   non-empty `content[]` (20 blocks: 14 paragraphs, 6 lists). ✔
4. `objectives[]` O1–O6 unique; every `home_topic_id` and every `anchor[]` id resolves to a real
   node; `strand_to_objective_map` covers L1–L6 exactly once; every topic's `objective_ids`
   resolve. ✔
5. Inline mirrors: `learning_objectives[]` rebuilt from the root registry and asserted equal to it
   **character for character** (every field, plus `image_examples: []`). ✔
6. Id grammar: all 6 media ids match `MEDIA_ID_RE` concept-scoped with chapter-continuous `.C{c}`;
   all 18 recall ids are `{topic_id}.RQ{n}` with `legacy_id` `{topic_id}.TR{n}`, lowercase
   `bloom_level`, non-empty answers; **no `.SR{n}` anywhere**. There are no segment-level recalls.
   `publication_id` is non-null (but see Gap 1). ✔
7. No સ્વાધ્યાય block is a topic, and `exercise_inventory` is `[]` so there is nothing to answer. ✔
8. Three-tier summaries strictly increase at topic level on all 6 (characters, words, and sentences:
   1 / 3 / 6 on every topic, counted by reading because quoted speech carries its own terminators);
   there are no segment- or module-level summaries in this plan. ✔
9. **No numbers in display text** — zero ASCII or Gujarati digits across every `topic_name`,
   `concept_name`, segment/module name, `explanation`, `real_life_example`, summary, bullet,
   `key_terms` entry, recall prompt/answer, concept content block, `objective_text`,
   `publication_text`, `modified_chunk` and media title/description/teaching-note. Every pearl count
   is written in words. `original_chunk` (which prints no digits anyway), `word_count`, ids and
   `textbook_pages` are provenance and exempt. ✔
10. Media: one image per reading scene, `2d_tool: null`. ✔ (detail below)
11. `figures_of_speech` — `[]` everywhere, nothing to verify, nothing invented. ✔
12. Every reference resolves as the plan stands; ids are consecutive, so Agent 14's renumber is a
    no-op for this chapter. ✔

`topic_type` is `STORY_TELLING` on all 6 topics — the pack's **authored** enum, correct for an
intermediate file per `phase2_contract.md`. It maps to the closed server enum
(`STORY_TELLING → instructional`) at Agent 14/15's emit; no literary genre label sits in that field.

### Exercises

`01_meta.json`'s `exercise_inventory` is **`[]`** — a measured fact, not a gap: all four rendered
pages carry no numbered સ્વાધ્યાય, no વિદ્યાર્થી-પ્રવૃત્તિ, no ભાષા-અભિવ્યક્તિ, only the પ્રવેશપેટી and
two reference boxes that ask the child nothing. `coverage_report.blocks_found` is `[]` (length 0 =
inventory length), `blocks_answered` is `[]`, `unanswered` is `[]`, `unmapped` is `[]`, and
`exercises` is `[]`. This unit does have reading text, so it is **not** the "no reading text" case
and the topic count is 6, not 0; it ships a plan and an empty-by-fact exercise file, and nothing
was invented to make the shape look complete.

### Publication

All 6 topics carry `publication_text`, and all 14 paragraph blocks carry a non-empty
`publication_text`. `concept_publication` maps one-to-one onto the paragraph blocks of
`concepts[].content[]` — 14 entries across 6 concepts, index set matched in **both** directions per
concept, with `list` blocks correctly skipped and no index renumbered. No vocative or classroom
instruction survived: `બાળકો`, `જુઓ`, `બોલો`, `વિચારો`, `વાંચો` return zero hits in publication prose
(the crow's printed 'બોલો કવિ' stays only inside the verbatim). Diffing each `publication_text` against
its `explanation` shows only the dropped vocative opener and, on two topics (M2.S2.T2, M2.S3.T4), a one- or two-word
swap of an imperative for a descriptive phrase (`મૂકો` → `આવે છે`, `જુઓ —` → `આમ બેસે છે :`); the concept
paragraphs differ by `બે` → `બંને`, `જોડો` → `જોડાય છે`, and in T6 by dropping `બોલો` and adding
`'કવિ' કહીને`. No meaning is added: the example rewrites replace each closing second-person question
with a sentence that restates what the explanation already says (for example the T4 line about the
counts eight, four, two, four).

`publication_chunk`: on all 6 topics the verbatim `original_chunk` is a **byte-exact prefix** of
`publication_chunk`, followed by the rewritten explanation and the rewritten example. **Read
literally, this spec's "byte-identical to `original_chunk`" fails on all six** — see Gap 8, which
records why that wording was not routed to Agent 16.

---

## E–G (reported)

- **E — સ્વાધ્યાય and risk.** No inventoried block exists, so nothing is unmapped or unanswered.
  Sensitivity notes are applied where the chapter touches ધર્મ (રામ, સીતા, કાકભુશુંડી as a living
  tradition's figures, named only as the chunks name them), જાતિ-ભૂમિકા (સીતાજીનું માતૃવત્ સ્નેહ) and સુરક્ષા
  (the drawn-sword threat) — flagged and guided, never censored.
- **F — shape and media.** The 12 invariants hold (above). `topic_type` is inside the authored enum
  with a clean mapping; recalls are `.RQ{n}`; concept numbers are chapter-continuous.
  `chapter_id` / `plan_id` follow `gseb_eng_gujarati{grade}_ch{unit_number}` — **⚠ the board and
  medium segments are provisional until VERIFY-1**. `publication_id` is a provisional placeholder —
  see Gap 1. Field shapes: `key_terms` 6 per topic (band 3–6), `concept_bullets` 4 and
  `important_points` 4 per topic (band 3–4), every `key_terms` / bullet / point in `કીવર્ડ — gloss`
  shape, `recall_questions` 3 per topic (band 2–3) laddered remember → understand → analyze/apply
  with the harder rung on the topics carrying the turn, `estimated_exchanges` `"4"`/`"5"`.
  **Out of band: module-level `difficult_words` is `[]` on all three modules** (band 5–10) and the
  four ભાષા-બોધ fields are `[]` — see Gap 5. ⚠ The 55–90 and 12–30 word bands remain **provisional
  until VERIFY-4**; they were enforced exactly as written.
- **G — the seven usual mistakes.** None present. (1) The teaching is ઘટના + પાત્ર + વળાંક, not સાર +
  બોધ + પ્રશ્નોત્તર. (2)/(3) No દુહા or પદ in the chapter; the bard's stanzas are neither fused nor
  lifted out. (4) Printed licence preserved, not corrected (`અંદરોઅદર`, `કપડાંમા`, the stray quotes).
  (5) No અલંકાર named. (6) Anchors are std-7-sized and Indian. (7) There is no સ્વાધ્યાય to cut.

**Agent 4's non-blocking notes, carried here as specified:**

- **The routing gap is now closed.** `04_validation.json` records that `profiles/genres/varta.md`
  was not routed to Agent 4, so two lines Agent 2 attributed to it could not be checked. That file
  was routed to this run and read in full: both lines exist ("Repetition with escalation is a chain
  of beats, not one beat: in std-7 P3 each of the four "ઉત્તમ પુરુષો" who pockets a મોતી is a beat of
  the same test", and the rule that quoted couplets stay inside the scene's topic). The cut-granularity
  question that raises is reported as Gap 13 and is not blocking.
- **No pre-reading topic exists, and none should** — the only pre-reading matter is the
  teacher-addressed પ્રવેશપેટી. **No REVIEW topic exists, and none should** — the closing line is the
  last sentence of the final ઘટના.
- **Uneven topic length** — word counts per chunk run 118 (M2.S2.T2) to 262 (M2.S3.T4). Reported, not
  blocked: each is one coherent beat.
- Every topic carries exactly one concept (so concept number equals topic number).

## Media

`reuse_report`: **scenes 6, authored 6, reused 0, rejected []**. `scenes` equals the 6 topics whose
`available_content_types` carry `"image"` — verified by recount, not read off the report. Every
node carries `image_url: ""` **and** a real, self-contained `generation_prompt` (1359–2828
characters each); no node carries a `[reused frame: …]` stamp, and no fabricated URL appears
anywhere. Every `negative_prompt` carries `Devanagari script labels`. **`2d_tool: null` for the
whole chapter** — correct for a પૌરાણિક દૃષ્ટાંતકથા with no staged process.

One frame per ઘટના, hung on the concept whose moment it actually depicts. Each narrator bar names
**one exact Gujarati string**, and every string was verified as a contiguous substring of that
topic's own `original_chunk` (so no printed misspelling such as `અંદરોઅદર` is lettered into a picture):

| media id | frame | narrator bar |
|---|---|---|
| M1.S1.T1.C1.IMG1 | પાઘડી પર બેઠેલો કાગડો | ત્યાં ક્યાંકથી એક કાગડો ઊડી આવ્યો |
| M2.S2.T2.C2.IMG1 | વડ નીચેનો થાળ | એકેક મોતી ઉપાડી પોતાના પહેરવેશમાં છુપાવી દીધું |
| M2.S3.T3.C3.IMG1 | થાળ લઈને ચાલતા પ્રધાનની સામે | પ્રધાન થાળ લઈને ચાલ્યો |
| M2.S3.T4.C4.IMG1 | રાજા સામે ધરેલાં મોતી | એક એક મોતી કાઢીને રાજાને દઈ દીધું |
| M3.S4.T5.C5.IMG1 | ચોકમાં પડેલો થાળ | કોઈ એ થાળને અડક્યું સુધ્ધાં નહીં |
| M3.S5.T6.C6.IMG1 | ત્યાં કશું જ નહોતું | રાજાએ જોયું તો મોતી કે થાળ કશું જ ત્યાં નહોતું |

Each is a single photographable moment, not a summary of its beat. The setting is Hastinapur's
court, a hilltop above the Sarayu and an Ayodhya courtyard because the chapter names them, so no
Gujarati dress or objects were added. Character likeness is held constant by repeating the same
appearance sentence in every prompt; no prompt refers to another image or to the chapter by name.
The **frame/embedded-tale distinction** the profile asks for is met: the court frames use deep
maroon, gold and green, the hilltop uses tan and gold, and the crow's tale (T5) is painted in pale
honey-gold and faded rose with fading edges. The spoiler gate holds in the media layer: T1's frame
shows no pearl, plate, bell, minister, queen or brother; T2's shows no brother, minister, queen,
jeweller or necklace; T3's shows no queen and no crow, and its Gujarati title and description name
nothing T3's own chunk does not contain (no queen, no count). **Rejected frames: none** — reuse is dormant in this pack, so nothing
was offered to reject.

## Gaps

Honest absences and judgement calls, surfaced rather than closed:

1. **`publication_id` is the provisional placeholder `1`, not a verified GSEB value.** The spec and
   invariant 6 require a non-null value, `upload_reference/chapter_master_map.json` holds `null` for
   every GSEB row (those rows live in the education DB and must be fetched, never invented —
   VERIFY-2), and `1` is the value every non-null plan in this pack already carries. It is the
   **CBSE/Hindi publication row**, which `phase2_contract.md` says is not portable. The server only
   checks non-null, so a passing validator run would **not** prove it correct. **The plan cannot be
   uploaded until the real GSEB row replaces it.** Same for `chapter_master_id`, which is `null` by
   the run context (a પૂરક unit under a synthetic ch18 identity may have no board-assigned master row
   at all).
2. **`subject_ref_id` and `medium_id` are `null`** — server-injected keys; no real GSEB subject
   record is confirmed, and `null` is the only correct value until one is.
3. **`chapter_id` / `plan_id` board and medium segments are PROVISIONAL** (VERIFY-1). The medium slot
   is the medium of instruction, not the subject language, and a wrong value **uploads clean** and
   mis-files the plan. The trailing `18` is the orchestrator's provenance numbering, not a printed
   figure (the page prints `3.`).
4. **`textbook_url` is a local path string** (`../Textbooks-pdf/std-7/purak-03-ramrajyana-moti.pdf`)
   — the GSEB readers have no hosted URL. Recorded by Agent 11 as a gap, not guessed at.
   **Pagination is high-confidence, not a gap:** `textbook_pages` `115–118`, read off the printed
   folios on page-1.png and page-4.png and cross-checked against the manifest row; both agree.
5. **The ભાષા-બોધ fields were NOT AUTHORED — an omission, not "the text has none".**
   `shabdarth`, `samanarthi`, `vilom` and `vyakaran` are `[]` on all six topics, and `difficult_words`
   is `[]` on all three modules. Agent 12's own note says `reference/bhasha_bodh.md` (and three other
   references its spec cites) was not routed to it, so it declined to guess at their bands, caps and
   `prakar` vocabulary. `bhasha_bodh.md` states that `shabdarth` "almost never returns `[]` in an L2
   pack", and this unit prints a 16-entry શબ્દાર્થ box and a 4-entry રૂઢિપ્રયોગ box that feed exactly
   those fields; the module-level `difficult_words` band is 5–10 in `field_shape_rules.md`, and
   std-7 prose precedent (ch12) authored them. These keys are **optional** in `phase2_contract.md`
   and no A–D item or contract invariant covers them, so this is reported, not blocking — but the
   plan is thinner for an L2 reader without them. **Owner: Agent 12 (`12_runtime_authoring.md`),
   re-run with `bhasha_bodh.md`, `teaching_block_format.md`, `alankar_chhand.md` and `shabd_gloss.md`
   routed.** Agent 12 also listed words missing from Agent 5's `key_terms` (`જાણે`, `મેહ`, the
   idioms, `ગણ્યાં`, `સ્પર્શ`, `ઘંટ`); `key_terms` is Agent 5's field and is untouched here.
6. **`topic_title` was authored by no agent.** The 32-root-key contract requires it and the merge
   table does not assign it. It is set to the chapter's own printed title, `રામરાજ્યનાં મોતી`, the same
   value `unit_title` carries — the std-7/8 precedent. Flagged for Agent 1 to confirm. `topic_number`
   is `18`, as `01_meta.json` sets it and the run context states.
7. **Root `genre` is the slug `varta`, not `01_meta.json`'s `"પૌરાણિક વાર્તા (દૃષ્ટાંતકથા)"`.**
   `phase2_contract.md` and `schema/gujarati_learning_plan_skeleton.json` ("one of
   profiles/genres/*.md, or 'mixed'") both require a slug, Agent 4/5 carry `varta` with the
   sub-form as a working field, and std-7 ch08/ch10/ch12/ch13 are merged the same way. This **departs
   from this spec's merge table** (which says `genre` lands from `01_meta.json`) and from the
   std-8/9 chapters, which carry the Gujarati free text. A pack-level inconsistency for the
   orchestrator to settle once; flagged, not blocked.
8. **A spec conflict on `publication_chunk`, resolved against the literal text and recorded.** This
   spec says `publication_chunk` is "byte-identical to `original_chunk`". `agents/16_publication_authoring.md`
   — the file that owns the field — says it is "the publication-facing version of the topic's block as
   a whole" with the verbatim "stays verbatim **inside** it". Agent 16 followed its own spec. The
   shipped corpus follows the same reading (`output8/purak01`'s validation report records that
   `output8/ch01`, `output7/purak04` and three `output6` chapters all have 0 byte-identical and all
   begin with the verbatim). Here, all six chunks are byte-exact prefixes
   and none is byte-identical. The check was run as **containment** (the property that protects the
   verse) and **not** routed to Agent 16, because Agent 16 cannot satisfy both specs and routing
   would only loop. If the orchestrator wants the literal reading enforced, spec 16 must change first.
9. **Media nodes: the `topic_id` routing key was dropped.** Agent 9's nodes carry a `topic_id` that
   `phase2_contract.md`'s media-node shape does not list; the node already sits inside its topic.
   Dropped here per "only contract keys survive", matching `output8/ch14`. Older std-7 merged files
   kept it; Agent 14's whitelist would drop it either way. `objective_id: null` on media follows the
   contract's own example, although the registry O1–O6 exists (Agent 9 asked for this to be checked).
10. **Quotation-mark glyphs.** The book prints double quotation as a pair of curly single marks and
    single quotation as one curly mark; `00_chapter_normalized.md` and therefore every `original_chunk`
    record them as straight ASCII `"` and `'`. Agent 5 checked every position against the render
    (single-versus-double agrees; only the glyph shape differs). This is the convention std-7 ch02,
    ch07, ch08, ch10, ch12 and ch13 were run with; ch03, ch04, ch06 and ch11 kept the curly glyphs.
    Not a word-level defect. **Owner if glyph-exact quotes are wanted: Agent 1.**
11. **A transcription separator and stale line ranges, checked and not blocked.** M3.S4.T5's
    `original_chunk` joins the hand-over sentence (normalized line 91) to the embedded tale (lines
    94–96) with a single `\n`, where the normalized file has a blank line and a marker between them;
    the sentence was deliberately moved from the end of M2.S3.T4 to open M3.S4.T5, per the varta
    rule that the sentence handing over to the teller opens the embedded topic. Both blocks are
    byte-identical to the transcription; only the separator width differs. The frozen
    `source_lines_00_normalized` strings in `02_structure.json` (`56-92`, `93-97`) are therefore stale
    for those two topics (effective ranges 57–89 and 91 + 94–96); that field is a working field and
    is not carried into the merged plan.
12. **Agent 1's double-render cross-check was weaker than a true second render.** The renders were
    supplied pre-rasterised and, per the run constitution, were not re-rendered; the second pass was
    a crop-and-upscale re-read of the same PNGs. Words resolved that way: `ગાળિયો` (ળ, glossed by the
    book's own શબ્દાર્થ box) and `પટ્ટણનું દટ્ટણ` (doubled ટ્ટ, glossed by the idiom box). Agent 5 then
    re-read both against the render and found no defect. Recorded as a known limitation, not as an
    equivalent check.
13. **Cut granularity under `varta.md` — for human confirmation, not blocking.** The profile says
    repetition with escalation is a chain of beats and gives std-7 P3's four ઉત્તમ પુરુષો as the
    example. The cut keeps (a) the four men's pocketing inside M2.S2.T2 and (b) the king's order, the
    brother's, minister's and queen's takings and the jeweller's line as one beat in M2.S3.T3.
    Reasons it stands: the printed text gives the four men **one shared sentence** ("ચારે જણાએ
    અંદરોઅદર ઈશારે વાત કરી લઈ એકેક મોતી … છુપાવી દીધું"), so a per-man topic would need verbatim that
    does not exist; the corpus inventory the profile was written from summarises the unit as "each steals
    a મોતી" rather than describing a per-man passage; and the palace chain is one continuous court
    scene with one arc. Agent 1's own marker names that chain as one scene, and Agent 2 and Agent 5
    each flagged the question for review. If a finer cut of M2.S3.T3 is wanted,
    the owner is **Agent 2 → Agent 4** (`02_structure.md` → `04_mapping_convergence.md`), and every
    downstream layer would have to be re-run.
14. **Objective wording, soft.** O4's `objective_text` says the jeweller learns "અઢાર મોતી ખૂટે છે",
    while the text has the jeweller say 'હાર માટે પૂરાં અઢાર મોતી જોઈએ' (eighteen are needed; ten are
    missing). It is inside the 12–30 band and Agent 12 is forbidden to touch it; reported for
    **Agent 2** so the registry and its mirrors can be corrected together.
15. **Structural names carry `ચોરી` and `પર્દાફાશ`, soft.** `topic_name` / `concept_name` / segment
    name of M2.S2.T2 read '…મોતીની ચોરી', M2.S3.T3's `topic_name` / `concept_name` read '…મોતીની
    ચોરીની સાંકળ', and module M2's name carries `ચોરીની સાંકળ`. Agent 1's own marker for M2.S2.T2 was
    `…મોતીપ્રાપ્તિ`; the name was changed in `02_structure.json`. Segment M2.S3 (which holds T3 and
    T4) is named '…સત્યનો પર્દાફાશ', so the turn is named one level above T3. The varta spoiler gate
    scopes to explanation, summaries and recall answers, so none of this is a gate breach, and
    `ચોરી` is the crow's own word at the end of the book; but these names label the men's act and the
    turn before the book does. Reported for **Agent 2** to rename if wanted.
16. **Working-file inconsistencies, not carried.** `05_with_content.json`'s `not_cut_as_topics` says
    the શબ્દાર્થ box has 18 entries; the box prints **16** (Agent 5's `notes` says sixteen).
    `02_structure.json`'s own `notes` carry a Devanagari-script slip in English mechanism prose
    (reported by Agent 5 for Agent 2's owner). Neither reaches `13_merged.json`.
17. **`ordering` is absent from `13_merged.json` by instruction** — Agent 14/15 sets it. The root
    therefore carries 31 of the contract's 32 keys, by design. `05b_textbook_order.json` records the
    printed order equal to the logical order, so Agent 14/15 should raise the
    `human_confirmation_required` note `phase2_contract.md` describes; this agent only restates it.
18. **Bands and ids are provisional.** The 55–90 / 12–30 word bands (VERIFY-4) and the `chapter_id`
    board/medium segments (VERIFY-1) were enforced exactly as written; nothing was widened, softened
    or dropped to reach PASS.

## LP2 validator

**VALIDATION PASSED** — Phase 8 execution, 2026-10-06. `POST /api/lp2/learning-plans/validate` returned:

```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati7_ch18_v1",
  "version": null,
  "phase": null,
  "is_active": null,
  "is_draft": null,
  "counts": null,
  "diff": null,
  "publication_id": null,
  "publication_name": null,
  "validation_errors": [],
  "message": "Valid"
}
```

**Result: validation_errors is empty. Plan passes LP2 schema validation.** The placeholder `publication_id: 1` satisfied the server's non-null check. No real `chapter_master_id` exists for this પૂરક unit (Gap 1 remains); the upload path cannot proceed until VERIFY-2 and Gap 1 are resolved, but the schema contract itself validates clean.

---

**Verdict: A–D PASS.** All four blocking sections and the 12 contract invariants pass on every
mechanical check, with 15 hard avoid-checks and 2 hard sensitivity items verified as genuinely
addressed rather than declared. `13_merged.json` is written and is ready for Agent 14. The gaps above
are reported absences and judgement calls, not silent ones; none is an A–D failure. The two that
most affect the plan's usefulness are Gap 1 (`publication_id` is unverified, so the plan cannot be
uploaded) and Gap 5 (the ભાષા-બોધ fields were never authored).
