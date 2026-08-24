# Validation Report — std 7, ch 09 · અલ્લક દલ્લક
સ્વરૂપ: ઊર્મિકાવ્ય-ગીત (confidence: high)   explanation unit: એક કડી
Topics: 8   Objectives: 8   Images: 0/6   Exercises: 47/47 entries covering 12/12 printed blocks

*Final RE-QC pass, after the owner re-runs. `12_authoring.json` and `16_publication.json` are the
files A12 and A16 last wrote; no layer file has changed since. This pass did **not** trust the
previous verdict: `13_merged.json` was **rebuilt from the layer files from scratch** and the whole
checklist was re-run mechanically against the rebuilt plan, not spot-checked. Result below.*

## A–D (blocking)   **PASS**

**A — diagnosis and lens. PASS.** ઊર્મિકાવ્ય-ગીત, `genre_confidence: high`, diagnosed off the render
by A1 from all four `genre_signals`; the blue પ્રવેશપેટી's own words (`આ રાધા-કૃષ્ણનું ઊર્મિગીત છે`)
are quoted as evidence, not taken as the verdict — and `urmikavya_geet.md`'s near-miss table settles
the one live alternative in the same direction (*a modern poet writing રાધા-કૃષ્ણ is still a ગીત,
not a પદ*; there is no છાપ inside the verse and the author slot prints `- બાલમુકુન્દ દવે`). The
roster unit for this profile is **one કડી** and the cut is one કડી per topic.

**ટેક handled as content, not repetition.** The two printings differ in wording —
`અલ્લક દલ્લક, ઝાંઝરઝલ્લક,` (p. 57) against `અલ્લક દલ્લક ઝાંઝર ઝલ્લક,` (p. 58): the comma after
`દલ્લક` is gone and `ઝાંઝરઝલ્લક` is set as two words. The profile's changed-words branch therefore
applies: **two distinct wordings → two ટેક topics** (M1.S2.T2, M2.S5.T8), T8 teaches *what changed*
and lists T2 in `depends_on`. Checked mechanically this pass: two `[[ટેક]]`-family markers, two
topics carrying them, `depends_on` resolves.

**Apparatus stayed apparatus.** `marker_topic_map` routes `[[પ્રવેશપેટી]]`, `[[શબ્દાર્થ]]` and
`[[રૂઢિપ્રયોગ]]` to APPARATUS and no topic's `original_chunk` contains any of them. This chapter
prints no chapter-final green ભાષા-બોધ box and no ભાષા-અભિવ્યક્તિ block (A1 `extraction_notes[]`).
`guiding_question` is derived from this poem's own rattling sound-words
(`અલ્લક, ઝલ્લક, ઢમ્મક, છલ્લક જેવા રણકતા શબ્દો દ્વારા…`), not copied from the profile, and reading
the eight explanations in order answers it.

**B — verbatim and structure. PASS.**

- All eight `original_chunk`s non-empty. Script scan over the whole merged plan: **zero** Devanagari
  characters, **zero** `।`, and no Roman characters in any `original_chunk`. (The only Roman text
  anywhere in the pack sits in `10_exercise_solutions.json`'s અનુવાદ answers — see E, whitelisted.)
- **Seven of the eight chunks match a `00_chapter_normalized.md` marker block byte-for-byte**
  (`ટેક`, `કડી 1`–`કડી 5`, `ટેક (પુનરાવર્તન)`), asserted by equality this pass, not by eye. The
  eighth (M1.S1.T1) is the `[[શીર્ષક]]` + `[[કવિ-પરિચય]]` markers joined into the pre-reading topic;
  both printed lines (`અલ્લક દલ્લક`, `- બાલમુકુન્દ દવે`) are present verbatim. A marker join, not a
  reconstruction.
- **Marker accounting, recounted off `00_chapter_normalized.md` this pass:** `[[કડી …]]` = **5
  markers → 5 topics** carrying them (T3–T7). `[[દુહો]]`, `[[પદ …]]`, `[[ઘટના: …]]` = 0 markers, 0
  topics. `[[સ્વાધ્યાય: …]]` = **12 markers, 0 topics** — the string `સ્વાધ્યાય` appears in no
  `original_chunk`, and all twelve are routed to Agent 10.
- Printed licence intact wherever quoted: `આલને`, `ચરિતર`, `રુએ`, `ભેળો`, `જડ્યાં`, `મલ્લક`, `જમના`,
  `રાધાગોરી`, `ઝાંઝરઝલ્લક`, `વણાયે`, `તણાયે`. The printed punctuation oddities survive —
  `બધાં જડ્યાં પણ એક ખૂટે છે.` and `રીસ ચડી ગોપીજનવલ્લભ.` end in `.` where neighbouring lines end in
  `!`, and `રાસ રચ્યો છે અલ્લક દલ્લક` carries no terminal mark at all. No field calls any of them a
  mistake.
- `word_count.original` **recomputed from `original_chunk` on all eight topics — all eight match**
  (5 / 14 / 20 / 20 / 21 / 17 / 18 / 15).
- Ids consecutive and every cross-reference resolves: M1–M2, S1–S5, T1–T8, C1–C8 chapter-continuous
  (each `concept_id` asserted equal to `{topic_id}.C{running}`); every `depends_on` and
  `source_topic_ids` id resolves to a live node.

**C — the teaching block. PASS.** Every topic has non-empty `explanation` **and**
`real_life_example`. Word counts, recounted this pass, all inside the 55–90 band:

| | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 |
|---|---|---|---|---|---|---|---|---|
| `explanation` | 73 | 76 | 78 | 87 | **90** | 83 | 89 | 80 |
| `real_life_example` | 69 | 75 | 70 | 67 | 77 | 73 | 71 | 85 |

`objective_text` 21 / 23 / 25 / 20 / 23 / 25 / 23 / 27 words (band 12–30). **No band was widened and
no prose was trimmed by this agent.** Summaries strictly increase on all eight (15<36<83, 20<47<96,
20<43<86, 18<38<96, 22<50<104, 19<42<93, 18<44<96, 19<53<116 words).

L2 glossing is at point of first use throughout — `આભે — આકાશમાં`, `ચગ્યો છે` taken from the book's
own શબ્દાર્થ box, `જડ્યાં — શોધતાં મળી આવ્યાં`, `રુએ — રડે છે`, `આલને — આપી દે ને`,
`ચરિતર — કરેલાં કામ`, `ચિત્ત — મન`, `અધીરું — ઉતાવળું`, `કદંબ — એક ઝાડનું નામ`, and
`ઉર તણાવું — દિલ ખેંચાવું` lifted from the printed રૂઢિપ્રયોગ box. Craft is named at the std-7
ceiling only (`પ્રાસ`, `લય`, `તાલ`, `રણકો`, `છેડા`, `સૂર`, `બેવડાયેલો શબ્દ`); a scan of every
child-facing field of every topic for `અલંકાર, છંદ, ઉપમા, વર્ણાનુપ્રાસ, અનુપ્રાસ, સજીવારોપણ, રૂપક,
યમક, શ્લેષ, ઉત્પ્રેક્ષા` returns **zero hits**.

**D — સ્વરૂપ essence. PASS.** All **28** `severity: "hard"` items in `07_pitfalls.json` are addressed
(4/3/5/4/4/4/4/4 across T1–T8; the remaining four are `soft`). `08_sensitivity.json` carries **no**
`severity: "hard"` item — one chapter-level entry only.

- **Picture before feeling** — holds on all eight. First sentence of `explanation` checked against
  that topic's own `original_chunk` this pass: T1 `અલ્લક દલ્લક`; T2 `ઝાંઝર` (printed inside the
  joined form `ઝાંઝરઝલ્લક`, and the item asks for `ઝાંઝર` character-for-character, which it is);
  T3 `આભે / ચાંદ / ઊગ્યો / રાસ / ચગ્યો`; T4 `રાધિકાનો / હાર / તૂટે / મોતી / ચલ્લક`;
  **T5 `લીધું / હોય / તો / આલને / મારું / મોતી` + `કાના` inside `કાનાને`** — the item's own named
  words, and the picture (the asking, the pearl) rather than the ભાવ; T6 `કાને / ત્યાંથી / દોટ /
  મૂકી / રીસ / ચડી`; T7 `રાધા / દોડે / ચિત્ત / અધીરે`; T8 `ઝાંઝર / રઢિયાળો / જમનાનો / મલ્લક /
  મુખડું / ઝલ્લક / ઝળકે`.
- **Slogan gate** — `જોઈએ` occurs in **no** child-facing field of **any** topic: explanation,
  example, all three summaries, `concept_bullets`, `important_points`, `key_terms`, every recall
  prompt and answer, every `concepts[].content[]` block and list item, every `publication_text`, and
  every media title / description / teaching note. The gate bites hardest at T4 (a lost pearl) and
  T6 (a sulk); neither carries a બોધ.
- **Never modernise the poet** — holds; every quoted line keeps its printed form and each is glossed
  *beside* the quotation, never inside it.
- **Nothing stated as fact that the કડી states as a condition** (T5) — holds explicitly.
  `નોંધો, 'લીધું હોય તો' એ શરત છે.` stands in the explanation; the strings `કાનાએ મોતી લીધું` /
  `લીધું જ હતું` appear only inside negations (`કડી ક્યાંય એમ કહેતી નથી કે કાનાએ મોતી લીધું જ હતું`),
  in the detailed summary and in the concept paragraph alike. RQ3's answer says
  `એ ચોક્કસ આરોપ મૂકતી નથી` and closes `કડી કારણ છાપતી નથી, એટલે આ આપણું અનુમાન છે.` No field says
  the theft happened.
- **No over-scientifying** — the banned list (પરિભ્રમણ, કક્ષા, ઉપગ્રહ, ગ્રહણ, પ્રતિબિંબ, બાષ્પીભવન,
  જલચક્ર, ગુરુત્વાકર્ષણ, પ્રકાશસંશ્લેષણ) returns **zero hits** across every field of every topic.
- **No literal reading of a figurative line** — `ચગ્યો` is glossed from the book's own શબ્દાર્થ box
  (`સરસ રીતે ખેલાઈ રહ્યો છે, ઝડપથી ગોળગોળ ફરી રહ્યો છે`), never as anything rising or flying; T7
  states outright `કોઈ એને હાથે ખેંચતું નથી` so `ઉર તણાવું` is not made physical; no field says the
  કદંબ bowed out of devotion or that the મુખડું emits light.
- **No political framing** — સરકાર, યોજના, પક્ષ, સેના, સરહદ, અભિયાન: **zero hits** anywhere.
- **The craft named but not labelled** — the profile requires every poem topic to carry either a
  non-empty `figures_of_speech[]` **or** a craft sentence. `figures_of_speech` is `[]` on all eight,
  so each explanation was read for its craft limb this pass and **all eight carry one**: T1 (`રણકો`,
  `તાલ માટે હોય છે`), T2 (`દલ્લક, મલ્લક, ઝલ્લક : પંક્તિઓના છેડા એક જ રણકે પૂરા થાય છે`), T3
  (`છમ્મક છમ્મક ને ઢમ્મક ઢમ્મક પર પૂરી થાય છે — એક પગનો તાલ, ને એક ઢોલકનો`), T4
  (`એક જ ઘાટના બે રણકા, પણ એક હરખનો ને એક આંસુનો`), T5 (`મલ્લક પોતે બેવડાઈને પ્રાસ પૂરો કરે છે`), T6
  (`અહીં ગીતનો રણકો પહેલી વાર ધીમો પડે છે`), T7 (`'ધીરે ધીરે' ને 'પલ્લક પલ્લક' — બંને જોડી કડીની ચાલ
  ધીમી કરી દે છે`), T8 (the ring, `જેથી સૌ ફરી સાથે ગાઈ શકે`). T7's limb is its **closing** sentence
  and a keyword scan for `પ્રાસ|લય` alone misses it — the requirement is the effect, and the effect
  is stated.
- **T8's two printings described as a print difference only** — holds, in words, with no numeral and
  with no claim that either printing is a mistake (`શબ્દો બંને ઠેકાણે એના એ જ છે`).
- **Invented અલંકાર** — `figures_of_speech` is `[]` on all eight topics, the correct std-7 answer, so
  the lines-found-verbatim check passes **vacuously**: no device was invented anywhere. Every
  `rhyme_scheme` is a real `{pattern, rhyming_words[], note}` object whose `rhyming_words` are lifted
  from the printed lines, and T3's `note` says plainly that `ઊગ્યો છે` / `ઘૂસ્યો છે` are not an exact
  rhyme — an asserted pattern would have been the violation, and it was not asserted.
- **Sensitivity** — `08_sensitivity.json`'s one chapter-level entry carries `area: "ધર્મ"`, a valid
  string from the seven fixed labels, and its guidance is applied: the રાસલીલા is taught as a sung
  literary scene inside the book's own frame — never theology, never comparative religion, never
  modernised into an ordinary romance.

**Contract (the 12 invariants) — all hold**, re-run mechanically against the rebuilt plan with
**zero** violations:

1. `phase: 2`; `plan_id == {chapter_id}_v{version}` (`gseb_eng_gujarati7_ch9_v1`); `chapter_id ==
   gseb_eng_gujarati{grade}_ch{unit_number}`.
2. All eight `original_chunk`s non-empty, Gujarati-script, no Roman, no Devanagari, no `।`.
3. Every topic has ≥1 concept, each with a resolving `objective_id` and non-empty `content[]`.
4. Root registry complete and consistent: O1–O8 unique, every `home_topic_id` and every `anchor[]`
   id resolves to a live node, `strand_to_objective_map` covers L1–L8 exactly and one-to-one, every
   topic's `objective_ids` resolve.
5. All eight inline `learning_objectives[]` mirrors match the root entry **character for character**
   on every mirrored field including `objective_text` and `anchor`, each carrying
   `image_examples: []`.
6. All six media ids match `MEDIA_ID_RE`, concept-scoped, `.C2`–`.C7`; recalls are `{topic_id}.RQ{n}`
   with `legacy_id` `{topic_id}.TR{n}` on all 24, and the substring **`.SR` appears nowhere** in the
   merged plan.
7. No સ્વાધ્યાય block is a topic; all 12 inventoried blocks answered (see E).
8. Three-tier summaries strictly increase at topic level; segments and modules carry no summary
   fields in this pack's shape.
9. **No digits (ASCII, Gujarati or Devanagari) in any display text** — scanned across `topic_name`,
   all three summaries, `explanation`, `real_life_example`, `modified_chunk`, `publication_text`,
   `publication_chunk`, `concept_bullets`, `important_points`, `key_terms`, every recall prompt and
   answer, every concept content block and list item, every media title/description/teaching note,
   and every `objective_text`. Digits occur only in ids, `word_count`, `textbook_pages`,
   `unit_number`, `topic_number` and `estimated_exchanges` — all provenance or contract fields.
10. Media: one image per reading scene, `2d_tool` null chapter-wide (see Media).
11. `figures_of_speech` `[]` everywhere — vacuously satisfied, nothing invented.
12. Every reference resolves as the plan stands; Agent 14's renumber has not run.

`topic_type` is the **authored** enum (`CONCEPT` on T1, `POEM` on T2–T8), correct for an intermediate
file — Agent 14 owes the `CONCEPT|POEM → instructional` mapping at emit. The one invariant that
cannot be satisfied here is `publication_id` non-null; see **Gaps 1**.

## E–G (reported)

- **E — સ્વાધ્યાય.** All **12** inventoried blocks answered. `coverage_report.blocks_found` is
  **identical, entry for entry and in printed order**, to `01_meta.json`'s `exercise_inventory`
  `verbatim_heading` list (asserted by string equality on all twelve this pass — no fuzzy match was
  needed); `blocks_answered` covers the same twelve; `unanswered` is `[]`. 47 answer entries, none
  with an empty `answer`, skill-tagged across reading comprehension (13), speaking (10), grammar (9),
  vocabulary (8) and writing (7). The વાતચીત block, the two performance blocks, the ચિત્રવર્ણન, the
  parent-help તળપદા block and the two open writing tasks are answered as model answers rather than
  skipped. Every `covered_by_topics` id resolves.
- **E — 7 items reported unmapped, none invented away.** EX31–EX36 are the last six sentences of the
  ક્રિયાવિશેષણ drill, supplied by the exercise page itself (મનસુખભાઈ, મિલન, ક્રિકેટ મેચ, બસ, જયદીપ,
  આકાશ) and not drawn from the ગીત; EX47 is built on a borrowed prose paragraph
  (`રસભરી તો આ સૃષ્ટિ છે…`) that is not from this poem. Neither is a signal that the cut missed a
  reading scene.
- **E — whitelisted script.** The five અનુવાદ answers are in Roman-script English on purpose — the
  medium of instruction — and each says so in `teacher_note`. They live in
  `10_exercise_solutions.json`, not in the merged plan, and a script-purity flag against them would
  be a false positive; none was raised.
- **C/E — T5's explanation sits exactly on the 90-word ceiling.** In band, so not a finding —
  recorded because the field has **no headroom**: any future edit to `M2.S3.T5.explanation` must trim
  before it adds. Owner if it ever needs to change: `agents/12_runtime_authoring.md`.
- **E — T5's first `concepts[].content[]` paragraph still opens on the structural observation**
  (`આ કડી રાધા પોતે બોલે છે.`) rather than on the picture, where the `explanation` opens on the
  picture. **Not** a violation: both the profile's hard gate and the instantiated pitfall item scope
  "picture before feeling" to `explanation`, and the paragraph names રાધા, કાના, મોતી and આલને in its
  own second sentence. Reported so the asymmetry is a visible decision rather than an oversight.
- **F — root `genre` is the Gujarati display name, not the roster slug.** The plan carries
  `"genre": "ઊર્મિકાવ્ય-ગીત"`; `phase2_contract.md`'s example shows a slug (`urmikavya_geet`, the form
  `05_with_content.json`'s `active_genre_profiles` uses). Merged from `01_meta.json` as this agent's
  spec directs, and consistent with ch01–ch08 of this pack. Reported, not repaired — root fields are
  A1's. Not one of the 12 invariants.
- **F — `teaching_lens` is `ચિત્ર + ભાવ + લય`**, where `urmikavya_geet.md`'s heading prints
  `ચિત્ર + ભાવ + અલંકાર`. The profile's own Lens section licenses લય in that third slot for a sung
  ગીત ("in a sung ગીત … લય and પ્રાસ occupy the same third slot as અલંકાર"), and the અલંકાર canon does
  not open until std 9. Deliberate, consistent across A1, A4, A7, A12 and A16. Recorded, not flagged.
- **F — `ordering` is deliberately not written**; it is Agent 14/15's, per this agent's spec. The
  merged plan therefore carries **31 of the 32 root keys**, the missing one being `ordering`.
  `chapter_id` / `plan_id` are frozen in **PROVISIONAL** form pending VERIFY-1.
- **F — merge hygiene, this pass.** `13_merged.json` was **rebuilt from `05_with_content.json`,
  `12_authoring.json`, `09_media.json`, `16_publication.json`, `11_pages.json` and `01_meta.json`**
  rather than patched. Working fields dropped at the merge: `source_markers` (A5 routing), `topic_id`
  on media nodes (A9 routing), `word_count.modified` (A5 working figure — `field_shape_rules.md`
  defines `word_count` as `{"original": <int>}`). A grep of the finished file for `source_markers`,
  `reuse_score`, `match_score`, `pitfall`, `validation_flag`, `transcription_note` and
  `"modified"` returns nothing. Shape: 2 modules (each carrying `difficult_words` — 6 and 7 entries,
  band 5–10 — and `overall_rhyme_scheme`), 5 segments, 8 topics, 8 objectives, 8 concepts, 6 media
  nodes, 24 recall questions. Topic key counts 34–37: the 31 contract keys plus
  `figures_of_speech` + `rhyme_scheme` on every topic and the ભાષા-બોધ extras where A12 authored them
  (`shabdarth`, `samanarthi`, `vilom`, `vyakaran` — romanized keys kept as the server stores them).
- **G — the seven usual mistakes.** None present: no સાર+બોધ+પ્રશ્નોત્તર substitution; no કડી merged
  and none split; no ટેક lifted out as decoration (both are taught as content, the second as the
  ring); no licence silently corrected; no invented અલંકાર; no adult or non-Indian anchor (ફેરિયાનો
  સાદ, વાર્ષિક કાર્યક્રમનો હૉલ, ગામને પાદર મેળાનું ઢોલ, ખિસ્સામાંથી ખૂટતી લખોટી, રિસેસનું થેપલું,
  પોળનો ઓટલો, પતરાના છાપરા પરનું ઝાપટું, ઘરના પ્રસંગની ગીતની લીટી — all std-7 reach); no સ્વાધ્યાય
  cut as a topic.
- **G — style observation, not a defect, carried forward a third time.** All eight explanations open
  on the identical vocative `બાળકો, જુઓ —`. It is teacher voice, no rule forbids it, and A16 strips
  it cleanly from every publication field. Recorded again because uniformity that exact is usually a
  template, and a template is where a genre gate goes unnoticed — which is exactly where T5's earlier
  failure sat.

## Media
`reuse_report`: **scenes 6, authored 6, reused 0, rejected []**. Verified against the rebuilt plan:
exactly six topics carry `"image"` in `available_content_types` (T2–T7) and exactly those six carry
one media node each. T1 (masthead) and T8 (the reprinted ટેક) carry no scene by design — correct,
since the profile forbids a ટેક topic's image from repeating the previous picture and T8's picture
*is* T2's. Every node carries `image_url: ""` **and** a self-contained `generation_prompt`, as
required while no Gujarati frame pool exists; there is **no** `[reused frame: …]` stamp and **no**
fabricated URL anywhere. Every `negative_prompt` contains `Devanagari script labels`. Every prompt
names its own setting, characters, action, mood and the 16:9 watercolour style, and each names the
exact Gujarati narrator-bar string to render. `2d_tool` is `null` chapter-wide and on every topic
(≤1 satisfied). Media ids are concept-scoped `…C{n}.IMG1`, `.C2`–`.C7`.

## Publication
All eight topics carry a non-empty `publication_text`. `concept_publication` matches
`concepts[].content[]` **by index and by count**, re-verified mechanically: each topic has one
concept shaped `[paragraph(0), paragraph(1), list(2)]`, and the publication blocks land on exactly
paragraph indices `[0, 1]` — 16/16 paragraph blocks covered, 0 list blocks touched (a `list` block
carries no `publication_text` in the contract's node shape), no index out of range. The classroom
address is gone from every publication field: `બાળકો`, `જુઓ`, `બોલો`, `સાંભળો`, `ધ્યાન દો`, `નોંધો`,
`ચાલો`, `યાદ રાખો`, `વાંચજો`, `પૂછો`, `લખો`, `વિચારો`, `કહો` all scanned across
`publication_text`, `publication_chunk` and every concept `publication_text` — the single string hit
was `લખોટીઓ` inside T4's anchor, a false positive. Every fact and every point-of-use gloss survives
in place; the teaching sentence `'જાણે' શબ્દ ધ્યાનથી વાંચજો` is correctly rendered as
`'જાણે' શબ્દ ધ્યાન માગે છે` rather than dropped. No meaning was added anywhere.

*One reconciled spec conflict, recorded rather than hidden.* This agent's spec says
`publication_chunk` is "byte-identical to `original_chunk`". `agents/16_publication_authoring.md`,
which **owns** the field, defines it as the topic's whole reader-facing block with "the verbatim
`original_chunk` stays verbatim inside it". A16 followed its owning spec: all eight
`publication_chunk`s **open with the topic's `original_chunk` byte-identical** (`startswith`
asserted on all eight this pass) and then append the publication prose and the anchor paragraph. The
binding intent — *the rewrite never touches verbatim* — is satisfied exactly. Treated as **PASS**,
identically to ch01–ch08 of this pack; the two spec texts should be reconciled in one direction.

## Gaps
1. **`publication_id` is `null`, and the server requires it non-null.**
   `upload_reference/chapter_master_map.json` holds `publication_id: null` for
   `gseb_eng_gujarati7_ch9` with an explicit `_comment` that it must be fetched from the education DB
   (VERIFY-2) and **never invented**. This agent's spec asks for a non-null provisional value;
   `no_hallucination_policy.md` and the map's own note forbid inventing one, and CBSE's `1` does not
   transfer. `null` is written and the gap is surfaced here. **Blocks Phase-8 upload, not this run.**
2. **`chapter_master_id` is `null`** for the same reason (VERIFY-2 — fetched from the education DB,
   never derived by arithmetic; the Hindi pack's `355 − chapter number` is CBSE provenance and does
   not transfer). Also required for upload.
3. **`chapter_id` / `plan_id` board and medium segments are unverified** (VERIFY-1). A wrong medium
   uploads **clean** and mis-files the plan. A correction changes those two strings only.
4. **`textbook_url` is a local path** (`../Textbooks-pdf/std-7/ch-09-allak-dallak.pdf`), not a hosted
   URL — the GSEB readers have none. Carried from `11_pages.json`, where the gap is recorded too.
   Page range `57–62` is `confidence: high`, read off the printed folios on `page-1.png` and
   `page-6.png` and cross-checked against the std-7 manifest row.
5. **`topic_title` was not authored.** No agent produced one and the root contract requires it; it is
   filled from `chapter_name` (`અલ્લક દલ્લક`), the same string `unit_title` already carries. Recorded
   so it is a decision, not a silent default. Owner if it should be otherwise:
   `agents/01_ingestion_genre_diagnosis.md`.
6. **`estimated_time` is `1.5`**, the contract's stated per-grade default. No agent authored a
   chapter-specific value. Recorded, not derived.
7. **Reference-data defect upstream, still open.** `profiles/genres/urmikavya_geet.md` ("nine printed
   કડી-units, eight distinct topics") and `reference/corpus/std-7_inventory.md` ("opening કડી + 7
   more … 9 કડી-units printed, 8 distinct") both carry a **stale prior** for this chapter. The
   renders show **seven** printed four-line units — three on p. 57 (ટેક, કડી 1, કડી 2) and four on
   p. 58 (કડી 3, કડી 4, કડી 5, ટેક reprinted). The plan follows the page, not the prior; the two
   reference files should be corrected. Raised by A1 and A4, repeated here so it is not lost.
8. **The prior also asserted the ટેક is repeated verbatim; it is not.** The comma after `દલ્લક` is
   absent in the closing printing and `ઝાંઝરઝલ્લક` is set as two words. A1 and A4 each confirmed this
   on the render. It is what makes T8 a topic rather than a `depends_on` reference, so the correction
   is load-bearing, not cosmetic.
9. **QR-badge occlusion, narrowed but not closed.** The badge overlaps the right end of the
   પ્રવેશપેટી box's first printed line, immediately after `લયનું`. A4 read the sentence complete
   across the line break (`એમાં શબ્દો, પ્રાસ, લયનું અદ્ભુત સંયોજન છે.`). The gap stays recorded
   because the badge still occludes page area; it touches apparatus only and is quoted in no
   `original_chunk`. The badge's Latin code string was deliberately not transcribed.
10. **Render-method gap, carried from A1.** The renders were supplied pre-rasterised and re-rendering
    is forbidden by the run context, so A1's spec'd double-render cross-check was substituted with a
    crop-and-upscale pass on the same PNGs. That verifies glyph shape but cannot add optical detail a
    higher-dpi re-render would have. Recorded as a method gap, not a clean double-render.
11. **A4's non-blocking notes, carried here as instructed.** M1.S1.T1 is the thinnest topic in the
    chapter — at std 7 the `[[કવિ-પરિચય]]` marker is only the author slot `- બાલમુકુન્દ દવે`, so the
    pre-reading topic leans on the શીર્ષક and the blue box's framing. Segment sizes are uneven
    (1, 2, 2, 1, 2 across S1–S5), a deliberate content decision A2 recorded rather than repairing to
    even segments. Both reported, neither blocking.
12. **Printed-content note (A1), for whoever owns the exercise deliverable.** Block 12's answer list
    prints fifteen bullets, but `પાલવ` has no corresponding phrase anywhere in the passage printed
    above it. A10 answered the other fourteen from the passage and marked `પાલવ` openly as not
    findable there. Transcribed as printed; not repaired.
13. **Context routing.** The run context routed six policy documents; this spec names five of them
    and the run context added `global_content_rules.md`. All six were supplied and read in full, plus
    the resolved genre profile `urmikavya_geet.md`. No document was inferred, and no cited document
    was missing.
14. **Page renders were not opened by this agent on any pass.** Every question this gate asks was
    answerable from `00_chapter_normalized.md` and the layer files, and A1/A4 had already settled the
    two layout questions (unit count, ટેક wording) against the renders first-hand. Recorded per the
    run context's instruction to say why a render was or was not needed.

## LP2 validator
Not run — filled in Phase 8. Expect at minimum one blocking server error until VERIFY-2 lands:
`publication_id` must not be null (`json_contract.md` rule 1). `chapter_master_id` is required by the
upload endpoint and is likewise null. Neither is a content defect and neither is closable here
without inventing a value.

---
**Verdict: A–D PASS.** This final pass rebuilt `13_merged.json` from the layer files and re-ran the
whole checklist mechanically against the rebuilt plan: **0 contract violations, 0 band failures, 0
script failures, 0 digit-in-display-text hits, 0 slogan hits, 0 invented devices, 0 unanswered
exercises, 0 fabricated media URLs.** The blocker raised two passes ago
(`M2.S3.T5.explanation`, owner A12) is closed and re-verified from the current file, and A16's
matching publication fields follow it. `13_merged.json`: 31 root keys (the 32 minus `ordering`,
which is Agent 14/15's), 2 modules, 5 segments, 8 topics, 8 objectives, 8 concepts, 6 media nodes,
24 recall questions. No authoring was repaired by this agent, no band was widened, no hard item was
softened, no id was renumbered, and no gap was closed by invention. The run is complete on content;
the three upload-blocking gaps above (`publication_id`, `chapter_master_id`, VERIFY-1 ids) remain
open and are Phase 8's, not this gate's.

## LP2 validator

- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json
- HTTP status: 200
- validation_errors: 1
  - root: 'publication_id' is required and must not be null
