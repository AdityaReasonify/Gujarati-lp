# Validation Report — std 8, ch 02 · ત્યાગવીર દધીચિ ('સ્નેહરશ્મિ')

સ્વરૂપ: પૌરાણિક કથા (વાર્તા) — profile `varta.md` (confidence: high)   explanation unit: એક ઘટના (વાર્તાનું એક પગલું)

Topics: 9   Objectives: 9   Images: 0/9   Exercises: 69/69 items · 15/15 blocks

Deliverables: two — the plan (`13_merged.json`) and the exercise pack
(`10_exercise_solutions.json`). This unit prints a continuous reading text, so both ship.

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` → `13_merged.json` (31 of the 32 root keys; `ordering` is
Agent 14/15's and is deliberately absent). Every working field was dropped: no `markers`,
`source_lines_00_normalized`, `notes`, `tier`, `agent`, `cut_summary`, `not_cut_as_topics`,
`reuse_report`, `coverage_report`, `avoid_checks`, `severity`, `content_index` or
`concept_publication` survives — verified by a recursive key sweep over the merged file.

## A–D (blocking)   **PASS**

Every hard item below was executed mechanically against the merged plan, not asserted.

**A — diagnosis and lens.** સ્વરૂપ પૌરાણિક કથા (a `varta` sub-form per that profile's own
sub-form table and the VERIFY-3 index constraint — there is no separate પૌરાણિક-કથા profile),
`genre_confidence: high`, four `genre_signals` recorded off the render by A1. The blue
પ્રવેશપેટી's own words — 'આ એક પ્રેરક અને પૌરાણિક કથા છે' — are quoted as evidence, not taken
as the verdict; A1 re-diagnosed from the page and the std-8 inventory prior agrees.

Explanation unit `એક ઘટના` matches the roster row for વાર્તા ("one ઘટના"). Nine topics = the nine
printed `[[ઘટના: …]]` beats, none merged and none split; the arc runs
પરિચય → ગૂંચ → વળાંક → યાત્રા → ચોટ and `topic_category` records it
(`introduction, core, core, transition, core, transition, core, core, climax`).

Apparatus did not become a reading scene. `05_with_content.json`'s `not_cut_as_topics[]` records
nine deliberate exclusions and none of them appears as a topic: the શીર્ષક-પટ્ટી and લેખક-સ્લોટ
(header furniture), the blue પ્રવેશપેટી (teacher-addressed — and the single strongest genre
signal on the page, used as evidence only), the yellow શબ્દાર્થ-પેટી, the two answer-bearing
bullet blocks (શબ્દસમૂહ માટે એક શબ્દ, રૂઢિપ્રયોગ), the twelve numbered pink સ્વાધ્યાય headings,
the two standalone passages printed *inside* the સ્વાધ્યાય (અગસ્ત્ય ઋષિ; વેત્રવતી/વિદિશા/શૂદ્રક),
the સ્વાધ્યાય figures (તારાજૂથ, 8×8 શબ્દચોરસ), the two captionless `[[ચિત્ર]]`, and the closing
yellow ચર્ચા-વિચારણા box. The two embedded passages are the case the
સ્વાધ્યાય-is-never-a-topic rule exists for; both stayed in the exercise deliverable.

`guiding_question` is derived from this chapter alone — 'દધીચિ ઋષિ પોતાનો દેહ રાજીખુશીથી આપી
દેવાનું પસંદ કરે છે — એ પસંદગી આ વાર્તાને કયો વળાંક આપે છે ?' — and the nine explanations read in
order do answer it. It could not be transplanted to another chapter.

ટેક / mixed-chapter / revision-checkpoint clauses do not fire and were **not silently skipped**:
`00_chapter_normalized.md` carries zero `[[કડી]]`, `[[દુહો]]`, `[[પદ]]` markers and zero ટેક
occurrences; one સ્વરૂપ runs end to end; this is a numbered reading unit, not a checkpoint.

**B — verbatim and structure.** All nine `original_chunk` non-empty and Gujarati script only —
**zero Devanagari, zero Roman, zero `।`**, verified codepoint-wise across U+0A80–0AFF. Each chunk
was matched **as a whole string** against `00_chapter_normalized.md`; all nine matched exactly, so
nothing was reflowed, re-spaced or re-punctuated by the merge. `word_count.original` was
recomputed from each chunk and all nine agree (107, 179, 122, 21, 71, 78, 96, 30, 232).

Printed licence and printed inconsistency intact: `સાભ્રમતી` (the river's older name, glossed in
the teaching as such and explicitly *not* corrected to સાબરમતી), `મરણને શરણ થવું`,
`હાડોહાડ સળગી ઊઠવું`, `ગાત્ર ગળી જવાં`, `પાણી ઉતારવું`, `આશાની ટશરો ફૂટવી`, the space before
`?` and `!`, and the one place the page sets `શસ્ત્રથી!` tight with no space at the end of
`M2.S2.T3`. Header furniture (chapter-number box, the QR badge and its Latin code string, running
folios) entered no chunk.

Marker accounting: `00_chapter_normalized.md` prints **9** `[[ઘટના: …]]` reading markers and **9**
topics carry them, one each — the count matches exactly. It prints **15** `[[સ્વાધ્યાય: …]]`
blocks and **none** became a topic; all 15 are in the exercise deliverable.

Ids are consecutive against the traversal, not merely against each other: `M1 M2 M3`,
`M1.S1 M2.S2 M2.S3 M3.S4`, `T1…T9`, concepts `C1…C13` chapter-continuous. Every cross-reference
resolves — `depends_on` (8 edges incl. `M3.S4.T9 → [M2.S2.T3, M2.S3.T8]`), `home_topic_id`,
`anchor[]`, `objective_ids`, media `concept_id` / `home_concept_id`, and every
`covered_by_topics` id in the exercise pack.

**C — the teaching block.** Every topic has non-empty `explanation` **and** `real_life_example`.
Word counts, all inside the 55–90 band with no trimming required and **no band widened**:

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 83 | 64 |
| M1.S1.T2 | 76 | 71 |
| M2.S2.T3 | 80 | 76 |
| M2.S2.T4 | 76 | 71 |
| M2.S2.T5 | 88 | 67 |
| M2.S3.T6 | 75 | 73 |
| M2.S3.T7 | 80 | 67 |
| M2.S3.T8 | 79 | 75 |
| M3.S4.T9 | 83 | 74 |

`objective_text` O1–O9: 18, 21, 24, 19, 18, 22, 19, 21, 23 words — all inside 12–30.

L2 calibration held: glossing is at the point of first use in every topic and the "everyday word"
bar sits low — પ્રતિદિન, લહરી, રુદન, કારમો, ભયભીત, દવ, ન્યારી, વિરલા, શીતળતા, ફોરમ, મુનિવર,
કુશળ સમાચાર, સદ્ભાગ્ય are opened where they appear, in Gujarati, one new thing per sentence, with
no Hindi word standing in for a Gujarati one. The seven printed રૂઢિપ્રયોગ are glossed in the
printed block's own wording inside the topic whose chunk carries them.

`real_life_example` is Indian, concrete, single and inside std-8 reach in all nine: આંગણે ચણતાં
કબૂતર before a storm, the bull at the village પાદર, a puncture-wallah eliminating leaks one by
one, a street-cricket ball, the ગુરુદ્વારા લંગર, canal water first reaching the bank, a watered
courtyard on a dusty afternoon, a neighbour's welcome, a blood-donation camp. Not one is an
adult's example, an abstraction, three examples at once, or an anchor that needs its own glossary.

Craft is named at the std-8 ceiling — structure as play, in plain words. A sweep for
રૂપક / ઉપમા / સજીવારોપણ / ઉત્પ્રેક્ષા / અનુપ્રાસ / છંદ / સમાસ / સંધિ / અલંકાર over every authored
field on all nine topics returns **clean**: the chapter's own comparisons ('દવથી બળી ગયેલા પર્વત
જેવો', 'તણખલાની જેમ ઊછળતા પર્વતો', 'વૃક્ષ પરથી પાકું ફળ ખરી પડે', 'મોર … એકાદ પીંછું ખેરવે') are
pointed at in ordinary words and in one recall prompt, never labelled.

**D — સ્વરૂપ essence.** `varta.md`'s eight-item **avoid** gate holds:

1. *Summary-only teaching* — every `explanation` adds motive, craft or consequence that
   `modified_chunk` does not carry, and was read against it one by one: the 'પણ' that turns the
   opening (T1), the દેહ-વર્ણન standing complete before ઇંદ્ર is named so the ફડક is earned (T2),
   વિષ્ણુ counting out four impossibilities so the one left sounds like the only one (T3), the
   question moving the problem from a શસ્ત્ર to a માણસ (T4), વિષ્ણુની ટકોર as a character's speech
   (T5), description that **is** the event because it ends on the first change since the હાહાકાર
   (T6), the તપ shown by શીતળતા / સ્થિર તેજ / ફોરમ before the ઋષિ is seen (T7), the one about to be
   asked for everything bowing first (T8), and the ripe-fruit / peacock-feather images as the
   author's quiet way of showing the passing (T9). None is swappable for its `modified_chunk`.
2. *A tacked-on બોધ* — a sweep for `આપણે પણ …`, `આ વાર્તા આપણને શીખવે છે…`, `બોધ એ છે કે…`,
   `શીખ એ છે`, `… જોઈએ કે` over every `explanation`, `real_life_example`, summary,
   `concept_bullets`, `important_points`, concept content block and recall answer returns
   **zero hits**. Where the ત્યાગ-વાત is stated it is quoted as વિષ્ણુના or the ઋષિના own printed
   words ('ધરતી ઉપર એવા પણ વિરલા છે…', 'જો જગતના એક પણ જીવનો દુઃખભાર હળવો કરી શકાતો હોય તો…').
3. *Judging a sympathetic character* — a sweep for ડરપોક / કાયર / નબળો / મૂરખ / સ્વાર્થી /
   ભોગવિલાસી / નકામા returns **zero hits**. ઇંદ્ર's fear is reported in the text's own words
   ('ગાત્ર ગળી ગયાં', 'ફડક પેસી ગઈ') and read as the measure of વૃત્રની ભયાનકતા; વિષ્ણુની ટકોર
   'તમારા સ્વર્ગમાં બધાં ભોગનાં સગાં છે' stays a line spoken inside the story, not a verdict on
   the દેવો.
4. *Spoiling the turn* — the climax is `M3.S4.T9`. Every preceding topic's `explanation`,
   `summary`, `detailed_summary`, bullets and recall answers were scanned for દધીચિ, અસ્થિ,
   ત્યાગ, દેહત્યાગ, અમોઘ, વધ, હણાયો, કલ્યાણ. **No genuine hit.** (The only matches are the
   substrings inside વધવા / વધારે — a false positive of the search, checked in context.) The name
   દધીચિ first appears exactly where the page first prints it, in `M2.S2.T5`, quoted as વિષ્ણુ's
   direction and not unpacked into what he will give; T3 carries only the condition, T4 does not
   answer its own question, T8 stops on 'આવવાનું કારણ પૂછ્યું.'
5. *Debunking or verifying a પૌરાણિક કથા* — a sweep for `ખરેખર એવું ન બને`, `ખરેખર આવું`,
   `વૈજ્ઞાનિક`, `વધારીને કહ્યું`, `સાચે જ બન્યું` returns **zero hits** across all nine topics and
   all publication-facing text. Nothing dates, verifies or science-checks વૃત્ર, the દેવો, the
   વિમાનો, the સમાધિ or the અસ્થિમાંથી બનેલાં શસ્ત્રો.
6. *Standardising dialect* — not a લોકકથા; the tatsama register (અસ્થિ, મહાત્યાગી, ગંધર્વ, આયુધ,
   સંગ્રામ, અતિરથી, મુનિવર) is glossed, never replaced, and `સાભ્રમતી` is explicitly taught as the
   river's older name rather than corrected.
7. *Inventing what the excerpt does not contain* — not an excerpt; the chapter is complete and no
   field narrates an event absent from the nine chunks.
8. *Translator credited as author* — not applicable; the page prints `- 'સ્નેહરશ્મિ'` as author
   and no અનુવાદ credit.

All **17** `severity: "hard"` items in `07_pitfalls.json` (across nine topics; one further item is
soft) were checked in the
field each names, plus the six chapter-level bindings; each is satisfied, and the four that are
mechanically checkable (the spoiler gates on T1, T3, T4, T8) were run as string sweeps rather than
read.

`08_sensitivity.json` carries `areas[]` drawn only from the seven fixed labels — **ધર્મ** (T3
soft, T9 hard, chapter-level) and **સંઘર્ષ** (T9 hard, chapter-level). The one **hard** item,
M3.S4.T9, is addressed exactly as its `guidance` requires: the દેહત્યાગ is taught as the કથા's
ચોટ and as the author's craft (પાકું ફળ, પીંછું — "બંને ચિત્રો શાંત છે"), never as an instruction;
the recall answers stay grounded in what દધીચિ says and does; and the anchor is a
**રક્તદાન શિબિર** — giving something of one's own body and going back to work smiling — not death
and not self-sacrifice. No recall or exercise answer extends into 'a person should also be ready
to die for others'. The chapter-level ધર્મ binding holds: the કથા is taught as literature with a
living tradition behind it, never as theology and never as comparative religion.

`figures_of_speech` is `[]` on all nine and `rhyme_scheme` is `null` — correct for ગદ્ય, and
nothing was invented to fill a field. Contract invariant 11 therefore holds vacuously, and the
verbatim-in-chunk test (which would have run on any entry) has nothing to reject.

## E–G (reported)

**E — સ્વાધ્યાય and risk.** All 15 inventoried blocks answered. `coverage_report.blocks_found` = 15
= inventory length, and the 15 `verbatim_heading` strings match `blocks_found` **one-for-one and
exactly** (no fuzzy allowance needed this chapter). `unanswered` is empty; all 69 items carry a
non-empty answer, and 69 equals the inventory's own `items` total. 30 items are marked
`is_model_answer: true` — the whole વાતચીત block, the personal-opinion items, the reading-timing
pair activity, the શબ્દચોરસ and the ભાષાંતર are answered with teaching values rather than skipped,
and the empty printed grids (the seven-name તારાજૂથ figure, the blank lines of block 11) are filled
with teaching values. Skill spread: vocabulary 27, reading comprehension 16, grammar 11,
speaking 10, writing 5. Sensitivity guidance is applied inside the exercise answers as well as the
plan.

`unmapped` is **12 items, reported and not closed** — EX28–EX32 (the five questions on the
independent અગસ્ત્ય-ઋષિ passage), EX33 (the જોડાક્ષર list drawn from that same passage), EX34 (the
timed-reading pair activity on it), EX35–EX37 and EX39 (four of the તારાજૂથ-figure questions), and
EX69 (the ભાષાંતર passage about વેત્રવતી/વિદિશા/શૂદ્રક). Each is exercise-internal matter with no
preparing reading scene in this chapter. **No mapping was invented to empty the list**, and this is
not a signal that the cut missed a scene — A1's extraction notes and A2's `not_cut_as_topics[]`
independently record both passages as સ્વાધ્યાય-સામગ્રી.

**F — shape and media.** All 12 `json_contract.md` invariants hold on the merged plan:
`phase: 2`; `plan_id` = `{chapter_id}_v{version}` = `gseb_eng_gujarati8_ch2_v1`; `chapter_id` =
`gseb_eng_gujarati8_ch2`; every topic has ≥1 concept with a resolving `objective_id` and non-empty
`content[]`; the objectives registry is complete and consistent (9 unique ids, single strand `L` —
ભાષા અને સાહિત્ય, every `home_topic_id` and `anchor[]` entry resolves, `strand_to_objective_map`
covers L1–L9); every inline `learning_objectives[]` mirror matches its root entry **character for
character** on all ten fields and carries `image_examples: []`; concept ids are chapter-continuous
`M1.S1.T1.C1 … M3.S4.T9.C13` and were verified **against the traversal position**, which is what
the server checks; recalls are `.RQ{n}` with `legacy_id` `.TR{n}` and the string `.SR` occurs
**nowhere** in the file; media ids match `MEDIA_ID_RE` concept-scoped; `publication_id` is non-null;
summaries strictly increase on every topic; and no digit — Roman, Gujarati or Devanagari — occurs
in any name, explanation, example, summary, bullet, key term, prompt, recall answer, concept
content block, media title/description, objective text, module or segment name (the beats are named
પહેલી / બીજી, never કડી 2). Provenance fields keep their numerals as they should: `original_chunk`,
`prompt_verbatim`, ids, `word_count` and `textbook_pages`.

`topic_type` is `STORY_TELLING` on all nine. That is correct for an Agent-13 intermediate file:
`phase2_contract.md` fixes the authored enum for Agents 02–13 and has Agents 14/15 map
`STORY_TELLING → instructional` at emit. The closed server enum must appear in the emitted plans
and nowhere earlier.

Bands from `field_shape_rules.md`: `key_terms` 4–6 per topic (band 3–6) ✔; `concept_bullets` and
`important_points` 4 each (3–4) ✔; `recall_questions` 3 per topic (2–3) ✔, Bloom-laddered
remember → understand → analyze/evaluate with a real answer on each; `estimated_exchanges` small
integer strings ("3"/"4"/"5") ✔; `bloom_level` lowercase in recalls and Capitalised in
`objectives[]` — the asymmetry preserved ✔; `word_count` `{"original": int}` ✔.
`difficult_words` is `[]` at module level — see Gaps 5.

`chapter_id` / `plan_id` follow `gseb_eng_gujarati{grade}_ch{unit_number}` — **provisional until
VERIFY-1** (Gaps 4).

**G — the seven usual mistakes.** None present. The plan teaches the સ્વરૂપ (ઘટના + પાત્ર + વળાંક)
rather than સાર + બોધ + પ્રશ્નોત્તર; no beat merged and none split (mistakes 2 and 3 are
verse-shaped and do not arise, and the ઘટના cut was checked against the printed turns, not against
paragraph counts); no printed licence silently corrected (`સાભ્રમતી` is the live case and it
stands); no અલંકાર named because the field existed — `figures_of_speech` is `[]` nine times over;
every `real_life_example` is single, Indian and inside std-8 reach; સ્વાધ્યાય was not cut as
topics and the exercise deliverable is full at 69/69.

## Media

`reuse_report`: scenes **9**, authored **9**, **reused 0**, rejected none — matching exactly the 9
topics whose `available_content_types` carry `"image"`, one image per ઘટના. Every node carries
`image_url: ""` **and** a real, self-contained `generation_prompt` (1197–2156 chars). No
`[reused frame: …]` stamp and no fabricated URL anywhere in the pack — correct, because no Gujarati
frame pool exists. Every `negative_prompt` carries `Devanagari script labels`. `2d_tool` is `null`
for the whole chapter (≤1 satisfied). Media ids are concept-scoped and every `concept_id` /
`home_concept_id` resolves to a real concept.

The merge dropped the working key `topic_id` that `09_media.json` carries on each node; it is not
one of the contract's media-node keys, and `output8/ch01` / `output8/ch03` dropped it the same way.

## Gaps

Honest absences, each recorded rather than closed by invention.

1. **`publication_id` is provisional and must not ship as written.** The contract requires a
   non-null value and `phase2_contract.md` states plainly that CBSE's `1` is **not portable** to
   GSEB. `1` is written here as the placeholder the shape demands, as in `output8/ch01` and
   `output8/ch03`. **VERIFY-2 must resolve the real GSEB publication row before the first Phase 8
   upload.** Not an A–D failure of this run; a hard precondition of upload.
2. **`chapter_master_id` is `null`.** Mandatory for upload, not discoverable from the LP2 API,
   fetched per chapter from the education DB (VERIFY-2). Never derived by arithmetic — the Hindi
   `355 − chapter number` pattern is CBSE provenance and does not transfer.
3. **`textbook` title is not confirmed off a rendered cover.** `01_meta.json` sets it `null` on
   purpose (A1's note: the std-8 cover was not among the eight supplied renders, and
   `profiles/boards/gseb_gujarati.md` records that the std-8 cover has not been read). The merged
   plan carries `11_pages.json`'s `"ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 8"`, which comes from
   board-profile convention, not from a page — `11_pages.json` flags exactly this in its own
   `gaps[]`. Fail-soft, carried, flagged. Owner `01_ingestion_genre_diagnosis.md`.
   *Note the pack is inconsistent here: `output8/ch01` carried the 11_pages string as this file
   does, `output8/ch03` carried `null`. This spec's merge table assigns `textbook` to Agent 11, so
   the string is carried; a human should settle which the pack wants.*
4. **Board and medium segments are PROVISIONAL until VERIFY-1.** `gseb_eng_gujarati8_ch2` uploads
   **clean** under a wrong medium and mis-files the plan silently — the failure that shipped all
   23 Hindi plans under the wrong medium once. Confirm before the first upload. Note the medium
   slot is the medium of **instruction**, not the subject language.
5. **Module `difficult_words` is `[]` and `overall_rhyme_scheme` is `null` — a live reference
   conflict, resolved the same way `output8/ch03` resolved it, and reported not repaired.**
   `reference/alankar_chhand.md` and `agents/12_*` place both module-level fields under કાવ્ય
   topics and set them empty for ગદ્ય; `reference/shabd_gloss.md`'s per-standard table still asks
   for 7–9 module `difficult_words` at std 8 with no ગદ્ય carve-out, and
   `reference/field_shape_rules.md` lists the band as 5–10 unconditionally. The two references
   disagree for a prose L2 chapter. The vocabulary load is carried instead by per-topic
   `shabdarth` (5–6 entries on every topic, **50** in all) and by inline glossing inside
   `explanation`. If the orchestrator resolves the conflict in favour of `shabd_gloss.md`, the
   module lists can be filled from those same entries without touching any other field. **Not
   blocked** — blocking would send A12 back to undo what its own governing reference mandates.
6. **`textbook_url` is a local path string** (`../Textbooks-pdf/std-8/ch-02-tyagvir-dadhichi.pdf`)
   — the GSEB readers have no hosted URL. `textbook_pages` `7–14` is `confidence: medium`, read
   off the printed folios on the page-1 and page-8 renders and agreeing independently with the
   std-8 manifest row (printed_start 7, pdf 19–26) and with A1's `extraction_notes[]`.
7. **`topic_title` was derived, not authored.** No agent supplies it and the root key list requires
   it; it is set to the printed chapter title `ત્યાગવીર દધીચિ`, as in `output8/ch01` and
   `output8/ch03`. If GSEB expects something else, that is
   `01_ingestion_genre_diagnosis.md`'s field to set.
8. **`ordering` is deliberately absent** from `13_merged.json` — Agent 14/15's to set
   (`logical` / `textbook`), per this spec. The 31 root keys written are the contract's 32 minus
   that one.
9. **A transcription correction pass was applied to `00_chapter_normalized.md` after A1.** The
   deva's name was first transcribed with long ઈ; A5 re-checked the glyph against the page-2/3/4
   renders, found short ઇ in print (corroborated by the control word ઇતિહાસ in the પ્રવેશપેટી on
   page-1 and by સાર્થ જોડણીકોશ), and replaced all occurrences with `ઇંદ્ર`. The pre-fix copy is
   kept at `00_chapter_normalized.md.pre-indra-fix`. All nine merged chunks match the **corrected**
   file verbatim, and no `ઈંદ્ર` survives anywhere in the plan. Recorded so the correction is
   visible rather than silent; A5 re-verifies it against the renders on any re-run.
10. **A printed slip in the apparatus is carried uncorrected, and correctly enters nothing.** The
    blue પ્રવેશપેટી prints `વૃત્રાસરનું` where the reading text and the શબ્દાર્થ box print
    `વૃત્રાસુર` throughout. The box is apparatus, enters no `original_chunk`, and the slip is left
    as printed in `00_chapter_normalized.md`. Likewise the printed numeral inconsistency (the
    second item of સ્વાધ્યાય 2(બ) and of સ્વાધ્યાય 11 is numbered with Gujarati `૨.` while the
    rest are Roman) is preserved inside `prompt_verbatim` — provenance, not display text.
11. **Uneven topic length, non-blocking** (A2 → A4). `M2.S2.T4` is a single printed sentence and
    `M2.S3.T8` three short ones, while `M1.S1.T2` and `M3.S4.T9` are each a full long paragraph
    (21 words against 232). The unevenness follows the printed વાર્તા-પગલાં and A2 correctly
    declined to split or merge a beat to even them out — `varta.md` explicitly allows a single
    turning sentence to be its own topic. Reported, never repaired.
12. **`M3` holds only one topic, carrying both climax and resolution** (A4's note). The chapter
    prints the ઋષિ's decision, his દેહત્યાગ, વૃત્ર's death and the closing કલ્યાણ line inside one
    paragraph; no separate resolution topic is possible without splitting the turn. A consequence
    of the page, not a sizing defect.
13. **The ગુરુદ્વારા-લંગર anchor in `M2.S2.T5` touches ધર્મ without an `08_sensitivity.json` entry
    of its own.** It is handled with dignity — a real Indian practice of giving, named accurately,
    with no comparison of traditions and no requirement to profess belief — and it satisfies the
    chapter-level ધર્મ guidance. Reported so a human sees it, not blocked; A8 flagged T3 and T9
    only.
14. **The અનુવાદ / ભાષાંતર block's answer is in non-Gujarati script on purpose** (EX69, plus a
    हिन्दी alternative). This is the whitelisted case named in this spec and in `qc_checklist.md`
    §B: the block asks for the child's own first language, the answer is a model in the medium of
    instruction, and `teacher_note` says so explicitly ("આ એક જ જગ્યાએ જવાબમાં ગુજરાતી સિવાયની લિપિ
    અપેક્ષિત છે — એ ખામી નથી, બ્લૉકની જ માગણી છે"). Raising a script failure here would be a false
    positive. **Un-noted Devanagari inside an `explanation` would still be a hard fail — there is
    none: the merged plan contains zero Devanagari and zero Roman characters in any display field.**
15. **Context routing, reported not guessed.** All six documents this spec requires
    (`no_hallucination_policy.md`, `global_content_rules.md`, `qc_checklist.md`,
    `json_contract.md`, `phase2_contract.md`, `field_shape_rules.md`) were supplied and read in
    full, along with the active genre profile `profiles/genres/varta.md`. Every band, invariant and
    roster row quoted above comes from those files as read. `output8/ch01/13_merged.json` and
    `output8/ch03/13_merged.json` were read as shape precedents only — the merged file's root,
    topic, concept, module, media and `learning_objectives` key sets are **identical** to ch01's.
16. **No page render was opened by this agent.** `00_chapter_normalized.md` answered every question
    this gate asked, including the layout facts (the nine ઘટના boundaries, the apparatus boxes, the
    two captionless illustrations printed *between* beats, the head-of-chapter author slot), which
    A1 had already recorded in `extraction_notes[]` and A5 cross-checked against the renders.

## LP2 validator

Not run — filled in Phase 8. Two values must be resolved **before** that call or it will fail on
shape regardless of this pass: `publication_id` (gap 1) and `chapter_master_id` (gap 2). The
board/medium segments (gap 4) will **not** fail the validator — they upload clean and mis-file the
plan, which is why they need a human check rather than a validator run.

---

**Verdict: A–D PASS.** No hard item blocks; the run is complete for this gate. Sixteen items are
reported above, of which one is a genuine reference conflict needing a human decision (gap 5), one
is a pack inconsistency to settle (gap 3), and four are upload preconditions (gaps 1, 2, 4 and the
unhosted `textbook_url`). Nothing here is a partial pass presented as a pass: each A–D gate was
executed mechanically against the merged plan and each returned clean.

## LP2 validator

Ran Phase 8: POST learning_plan_logical.json to /agentapi/api/lp2/learning-plans/validate. Reachable (HTTP 200), plan_id gseb_eng_gujarati8_ch2_v1.

**Result: 1 validation_errors.**
- `root: 'publication_id' is required and must not be null`

This matches the pre-flagged gap 1 (publication_id) noted above. Not yet resolved; validator confirms it will block upload. gap 2 (chapter_master_id) did not independently surface as a separate error in this run — only publication_id was reported.
