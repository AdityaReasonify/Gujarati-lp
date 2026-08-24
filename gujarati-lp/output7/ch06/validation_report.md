# Validation Report — std 7, ch 6 જો કરી જાંબુએ
સ્વરૂપ: રમૂજી પ્રસંગકથા / `nibandh_atmaparak` (confidence: high)   explanation unit: એક પ્રસંગ — હાસ્ય-ઉપસ્વરૂપમાં એક હાસ્ય-વળાંક (દરેક વાહક એક topic, setup અને પરિણામ સાથે)
Topics: 7   Objectives: 7   Images: 0/7   Exercises: 15/15

## A–D (blocking)   **PASS**

Final re-QC pass, run after A1's `teaching_lens` correction and the A12 / A16 re-runs had all
landed (`01_meta.json` 14:50, `12_authoring.json` 14:20, `16_publication.json` 14:34; the merge and
this gate follow them). Nothing was taken on trust from the previous report: every check below was
re-measured against the source layers this pass, and the two places where the previous report's
arithmetic was loose are corrected in-line and flagged as such.

`13_merged.json` was re-emitted this pass and is byte-identical to the merge that was verified here
(sha256 `26f73749ac724dee826bff53236b251de5dee0854121a735e44af7d9d9268f47`, 203 197 bytes).
Re-verified field-by-field against every source layer with **zero provenance mismatches**: all root
keys against `01_meta.json` and `11_pages.json`; all 7 topics' base fields, all 3 module names and
all 6 segment names against `05_with_content.json`; all 7 topics' authored fields and all 3 modules'
`difficult_words` / `overall_rhyme_scheme` against `12_authoring.json`; all 7 topics'
`publication_text` / `publication_chunk` and all 8 concepts' `concept_publication` against
`16_publication.json`; all 7 media nodes against `09_media.json`. The only field of any source layer
that does not appear in the merge is `09_media.json`'s working `topic_id` on each media node, which
is not a contract media key and was correctly dropped.

### The previous run's blocker stays closed

The blocker two runs back was root `teaching_lens` in `01_meta.json` carrying 754 characters of
mixed Gujarati + bare Roman pipeline prose (`lens`, `field`, `topic`, `hard gate`, and the repo path
`nibandh_atmaparak.md`) outside any bracketed technical term, against §B's single permitted shape
`સજીવારોપણ (personification)`. A1 re-ran and rewrote the field. It now reads
**`સ્વર + પ્રસંગ + પુનરાવર્તન`** — 26 characters, pure Gujarati (U+0A80–0AFF), zero Roman, matching
the shape every sibling chapter uses (`output7/ch01` `ચિત્ર + ભાવ + લય`, `output7/ch03`
`ઘટના + પાત્ર + વળાંક`, `output7/ch04` `તથ્ય + પરંપરા + જિજ્ઞાસા`). Re-measured this pass in both
`01_meta.json` and `13_merged.json`: still clean. Nothing was lost — the third-person caveat and the
repetition-with-escalation account remain at length in `01_meta.json`'s `extraction_notes[5]` and
`genre_signals.structure`, and the caveat is instantiated as a hard item in `07_pitfalls.json`'s
`chapter_level[0]`.

A1's `explanation_unit` still carries the Roman word `topic` in its prose. That field is a diagnosis
note; it is **not** one of the contract's 32 root keys and does not ship in the plan, so §B does not
reach it and it is not raised as a defect. It is carried as Gaps item 11.

### A — diagnosis and lens   PASS

સ્વરૂપ diagnosed off the render with four signals and `high` confidence; the પ્રવેશપેટી's own
`રમૂજી પ્રસંગ` quoted as evidence, not as the verdict. The explanation unit matches the roster row
for આત્મપરક/લલિત નિબંધ — one પ્રસંગ, and in the હાસ્ય sub-form one રમૂજ-વળાંક never cut from its
setup. Apparatus stayed out of the reading scenes: the teacher-addressed વાદળી પ્રવેશપેટી, the
શબ્દાર્થ box and the chapter-final green વ્યાકરણ box are all marked in `00_chapter_normalized.md`
under non-ઘટના markers and none became a topic — re-counted this pass, the marker roster is
1 `[[પાઠ-શીર્ષક]]`, 1 `[[લેખક-પરિચય]]`, 1 `[[પ્રવેશપેટી …]]`, 1 `[[શબ્દાર્થ પેટી]]`,
1 `[[વ્યાકરણ પેટી …]]`, 7 `[[ઘટના: …]]` and 15 `[[સ્વાધ્યાય: …]]`. The head byline
`- જયંતી ધોકાઈ` (line 12, under the title) is a byline, not a student-facing લેખક-પરિચય, and
correctly is not a CONCEPT topic. `guiding_question` is derived from this chapter and names its
comic engine without giving away the withheld ending; reading the seven explanations in order
answers it.

### B — verbatim and structure   PASS

- All 7 `original_chunk`s non-empty and pure Gujarati (U+0A80–0AFF).
- **Every `original_chunk` matched back to the transcription this pass.** Each of the 7
  `[[ઘટના: …]]` blocks in `00_chapter_normalized.md` was extracted and compared against its topic's
  chunk: **7 of 7 match exactly**, character for character, in printed order. None of the 7 chunks
  occurs inside the સ્વાધ્યાય region of the file.
- **Script sweep re-run over the whole merged plan: 0 hits.** No Roman and no Devanagari anywhere
  outside bracketed technical terms, in any root field, module or segment name, `topic_name`,
  `explanation`, `real_life_example`, summary, bullet, `key_terms`, concept name, concept content,
  recall prompt or answer, `publication_text` or `objective_text`. Devanagari count over the entire
  file, provenance fields included: **0**. The Latin that remains is ids (`O1`–`O7`,
  `strand_to_objective_map`, media `home_concept_id`) and the media `generation_prompt` /
  `negative_prompt` pair, which is written for an image model and is not child-facing display text.
  No `।` anywhere in the file: **0**.
- `extraction_notes[19]` confirms no Devanagari occurs in this chapter at all, so no printed
  non-Gujarati whitelist case arises in the reading text.
- Marker arithmetic exact: **7 `[[ઘટના: …]]` markers, 7 topics carrying them**, one-to-one through
  `marker_to_topic_map`. No verse markers. **None of the 15 `[[સ્વાધ્યાય: …]]` blocks became a
  topic.**
- `word_count.original` re-computed from each `original_chunk` and agrees on all 7 topics
  (115, 103, 170, 143, 184, 104, 107).
- Profile gate 11 re-checked at the content layer: 5 courier topics for the 5 marked couriers
  (મગન, રામજી, નાથિયો, મોંઘીમા, પશી); the first two markers are અમથાલાલ's own setup beats.
- Gate 13 re-checked: the last printed sentence stands whole inside `M3.S6.T7.original_chunk`, and
  no end-credit was invented for a chapter that prints none.

### C — the teaching block   PASS

All 7 topics carry a non-empty `explanation` and `real_life_example`. Word counts re-measured this
pass, all inside 55–90, no band widened:

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 84 | 70 |
| M1.S2.T2 | 78 | 71 |
| M2.S3.T3 | 85 | 71 |
| M2.S3.T4 | 80 | 70 |
| M2.S4.T5 | 85 | 72 |
| M3.S5.T6 | 81 | 69 |
| M3.S6.T7 | 83 | 75 |

All 7 `objective_text` inside 12–30 words (18, 20, 25, 22, 21, 23, 20). Glossing is at point of use
and L2-calibrated (`છેટે`, `લૂલી`, `બોખું`, `ભાળીને`, `આંટો` all glossed although ordinary
Gujarati). `real_life_example` anchors are Indian, single and inside std-7 reach — a શેરી ફેરિયો,
લખોટી, a chevdo jar on the માળિયું, a પ્રાર્થનાસભા yawn, an ઉત્તરાયણ પેચ, a પાણીનું ટૅન્કર,
ફળિયામાં ક્રિકેટ. No અલંકાર/છંદ vocabulary anywhere — correct for std 7, and separately re-swept:
**zero occurrences** of કટાક્ષ, વ્યંગ, ઉપમા, રૂપક, અનુપ્રાસ, સજીવારોપણ, છંદ or અલંકાર across all
263 display strings in the plan.

### D — સ્વરૂપ essence   PASS

`07_pitfalls.json` carries **25 topic-level `avoid_checks` with `severity: "hard"`** (plus one
non-hard) and **8 chapter-level items** — of which 5 are explicitly marked hard, 2 carry no explicit
severity marker and are treated as hard here, and `chapter_level[7]` is explicitly marked
`Severity: soft`. *(The previous report called all 8 chapter-level items hard; corrected here. It
changes no verdict — every one of the 8 is addressed either way.)* Each was checked against the
authored text:

- *Gate 6 / the third-person caveat* (`chapter_level[0]`) — every `explanation` opens with a
  character as grammatical subject (અમથાલાલ, મગન, રામજી, મોંઘીમા). A first-person sweep returns
  6 hits for `હું `, and every one is licit: two are quotations of મોંઘીમા's own printed thought
  (`‘હવે હું થેલી આપવા જાઉં તો…’`, in a concept paragraph and its publication rewrite), and four are
  inside `એક શક્ય જવાબ : ‘હું …’` model answers where the **child** is speaking. No field ascribes a
  first-person admission, confession or self-deprecation to the writer of a chapter whose running
  prose carries no `હું`.
- *Gate 2* — no topic carries `topic_category: "climax"` (introduction ×2, core ×4, resolution ×1),
  and every motive quoted is one the page prints (`વજન સરખું કરવા`,
  `આપણે વળી ક્યાં સુધી આંટો ખાવો ?`). No supplied motive, no verdict on a carrier.
- *Gate 3* — zero hits for `આ પાઠ આપણને શીખવે`, `આપણે પણ`, `બોધ એ છે`, `શીખ એ છે` across every
  display string. `M3.S6.T7` ends on the chapter's own open question and says so explicitly
  (`‘હશે’ એટલે અંદાજ`).
- *Gate 4* — at most one clause per explanation talks about the humour (`મજા આ ફેરમાં છે :`,
  `મજા બીજા પગલામાં છે :`, `પણ પગથિયું અહીં ચડે છે :`, `ત્યાં જ ચોટ પડે છે :`). Zero hits for
  `રમૂજી છે કારણ કે`, `લેખક મજાક કરે`, `હસવું આવે એવું`, `(મજાક)`, `આ તો મજાક છે`,
  `ખરેખર તો આવું ન કરાય`.
- *Gate 5* — `ભાઈનો તો વિશ્વાસ કરાયને !` is pointed at and set beside what happens next, never
  repaired into a rule. Per A7's std-7 instantiation and `chapter_level[2]` ("no device labels at
  std 7"), the line is correctly **not** labelled કટાક્ષ/વ્યંગ at this standard.
- *Gate 7 / `chapter_level[1]`* — every printed તળપદું and બોલચાલનું રૂપ is quoted as printed and
  glossed with the printed form as the headword (`હોવ્વે!`, `હત્તારીની !`, `નખ્ખોદિયો`,
  `પટ કરતાંક`, `કે’જે`, `બે’ક`, `રાજીના રેડ`, `લૂલી`, `ઝાપટી ગયા`, `હુંયે`, `નાનકી`). Several
  glosses say outright `ભૂલ નથી`. Zero hits for `સાચું રૂપ` anywhere. The three printed variant
  pairs stay un-normalised in both directions: માંહ્યલીકોર (T4) / માંયલીકોર (T5) — and T4's own
  gloss records the variant; ડોસીને / ડોશીથી (both T6); અડધો માઈલ (T2) / અર્ધો માઈલ (exercise કોઠો).
- *Gates 8, 9 / `chapter_level[3]`* — no biography for જયંતી ધોકાઈ anywhere; the name occurs in no
  display string at all (0 hits for both `જયંતી` and `ધોકાઈ`). No price, weight, distance or place
  beyond what the page prints; `માઈલ` uses only the chapter's own શબ્દાર્થ gloss. `આસ્તેક` —
  glossed in the printed શબ્દાર્થ box but absent from the story text (`chapter_level[6]`) — appears
  in no display field (0 hits), as required.
- *Gate 12 / `chapter_level[4]`* — no `objective_text` or `explanation` teaches how to write a
  રમૂજી પ્રસંગ as a method; all 15 inventoried blocks live in the exercise deliverable and in no
  topic.
- *Gate 14 / `chapter_level[5]` "five carriers, not five culprits"* — zero hits for ચોર, લુચ્ચો,
  લોભી, બેઈમાન, ગરીબ, અભણ, પછાત or `આ લોકો` about any carrier, and nothing mocking મોંઘીમા's age or
  teeth. The sweep returns exactly two hits for `બિચારા`, both inside `M3.S6.T7.C8`'s quotation of
  the chapter's own printed closing sentence (`…તેની બિચારાની શી દશા થઈ હશે !`, once in the concept
  paragraph and once in its publication rewrite), set in quote marks as the chapter's register — not
  an authored one. Correct, and not a violation.
- *Gate 15* — `figures_of_speech: []` on all 7 topics, correct for prose at std 7, so the
  verbatim-quotation check has nothing to fail on. `rhyme_scheme: null` throughout;
  `overall_rhyme_scheme: null` on all three modules.
- `08_sensitivity.json` reports `none_found: true` with empty `topics[]` and `chapter_level[]`, so
  no hard sensitivity item is outstanding and no `areas[]` label needed matching against the seven
  fixed labels.

### Contract — the 12 invariants   PASS

Re-run mechanically this pass; **0 errors across all twelve**.

`phase: 2`; `chapter_id` `gseb_eng_gujarati7_ch6`; `plan_id` `gseb_eng_gujarati7_ch6_v1`;
`publication_id` non-null. Ids checked against traversal position, not merely against each other:
modules `M1`–`M3`, segments `M1.S1`–`M3.S6` never restarting, topics `T1`–`T7` never restarting.
Every topic has ≥1 concept with a non-empty `content[]`; **concept ids are chapter-continuous
through the two-concept topic** (`…T5.C5`, `…T5.C6`, `…T6.C7`, `…T7.C8`) — each verified against its
expected `{topic_id}.C{n}`. All 7 objectives unique, all on strand `L`, all `bloom_level`
Capitalised; every `home_topic_id` and every `anchor[]` entry resolves to a real node;
`strand_to_objective_map` covers exactly the 7 `legacy_id`s and no more; every topic's
`objective_ids`, `depends_on` and `source_topic_ids` resolve; **all inline `learning_objectives[]`
mirrors match their registry `objective_text` character for character (0 mismatches)** and all carry
`image_examples`. Recall ids are `{topic_id}.RQ{n}` with `legacy_id` `{topic_id}.TR{n}`, all 21
carrying a real answer, a lowercase `bloom_level` from the closed set and a `difficulty` from
`easy|medium|hard` — the string `.SR` occurs **0 times** in the file, and this chapter authors no
segment recalls at all. `topic_type` is the authored enum (`STORY_TELLING` ×7) for Agent 14 to map
to `instructional`. Summaries strictly increase on all 7 topics (1 sentence / 3–4 / 5–8).
**No numerals in display text**: the digit sweep over all 263 display strings returns hits only in
`root.textbook` (`ધોરણ 7`, the reader's printed title), `strand_to_objective_map` (ids) and
`estimated_exchanges` (the contract's "small integer as a string") — all provenance, none display.
Carriers are named (મગન, રામજી, નાથિયો, મોંઘીમા, પશી), never numbered, while the chapter's own
printed quantities stay inside the verbatim.

No working field, score or note survived the merge. Key whitelists re-checked: topics carry exactly
the 31 contract keys plus `figures_of_speech`, `rhyme_scheme` and the four ભાષા-બોધ extras
(`shabdarth`, `samanarthi`, `vilom`, `vyakaran`, romanized as the server stores them); concepts
carry exactly `concept_id / concept_name / objective_id / key_terms / content`; media nodes carry
exactly the 14 contract keys; objectives exactly the 10; modules exactly
`module_id / module_name / difficult_words / overall_rhyme_scheme / segments`. `difficult_words`
counts are 7 / 8 / 7 per module, inside the 5–10 band, every entry `{word, meaning, example}`.

### Exercises   PASS

`coverage_report.blocks_found` lists 15 headings and matches `01_meta.json`'s `exercise_inventory`
of 15 **entry for entry, string for string, in printed order** — re-compared this pass, 15/15 exact,
no fuzzy match needed. `blocks_answered` is 15; `unanswered` is empty; 63 entries cover the 74
printed items (the two printed grids are each one composite entry with the filled grid in
`values_filled_for_teaching`, and block fifteen's paragraph and its un-numbered sub-task are two
entries). The standing L2 block `નીચેનાં વાક્યોનો તમારી પ્રથમ ભાષામાં અનુવાદ કરો.` carries English
answers by design and says so in its `teacher_note` — the whitelisted non-Gujarati case, not a
script failure. Two consecutive printed blocks are both numbered `10.` (`extraction_note[13]`):
15 blocks under 14 printed numerals, both inventoried and both answered.

### Media   PASS

`reuse_report` = `{scenes: 7, reused: 0, authored: 7, rejected: []}`, matching the 7 topics whose
`available_content_types` carry `"image"`; `authored` equals `scenes`, `reused` is `0`. All 7 media
ids match `MEDIA_ID_RE` and are concept-scoped; every node carries `image_url: ""` **and** a real
self-contained `generation_prompt` naming an exact Gujarati narrator-bar string; every
`negative_prompt` carries `Devanagari script labels`; no `[reused frame: …]` stamp anywhere.
`2d_tool` is `null` on every topic and `null` in `09_media.json` — 0 tools, inside the ≤1 limit.

### Publication   PASS

All 7 topics carry a non-empty `publication_text`, byte-identical to `16_publication.json`'s.
`concept_publication` matched **by index and by count** on all 8 concepts: the 8 source entries
(all `content_index: 0`) map exactly onto the 8 `paragraph` blocks that carry a `publication_text`,
and the 8 `list` blocks carry none — 0 mismatches in either direction. No vocative or classroom
instruction survived the rewrite: `બાળકો` (8 hits), `જુઓ —` (2) and `બોલો` (0) are present in the
teaching `explanation` and concept content where they belong, and the sweep over all 15 publication
strings returns **0 hits** for `બાળકો`, `જુઓ`, `બોલો`, `ચાલો`, `વિચારો` and `તમે`. Each topic's
`original_chunk` stands verbatim and unaltered at the head of its `publication_chunk` — see Gaps
item 2 for the shape note this raises.

## E–G (reported)

- **E — સ્વાધ્યાય and risk.** Every block skill-tagged and mapped. `unmapped` holds **9** items and
  is reported, not emptied: EX26 (a જાતિ-agreement drill about a વાંદરો and a બિલાડી), EX49–EX51
  (generic cause-and-effect pairs naming મૈત્રી and મિતાંશ), EX52–EX55 (વાક્યવિસ્તાર frames about a
  film, a મેળો, breakfast and a brother) and EX62 (the exercise's own ભોલુ paragraph). Re-counted
  this pass: 9 exercises carry an empty `covered_by_topics`, and they are exactly the 9 listed in
  `unmapped`. None of their content occurs in the chapter, so no reading scene prepares them —
  unmapped **by construction**, and A10 correctly did not invent a mapping to close the report.
  Personal-opinion and પ્રવૃત્તિ items (block nine `તમારા જીવનમાં બનેલ રમૂજી પ્રસંગ વર્ગમાં કહો.`,
  the જોડીકાર્ય અભિનય) are answered as model answers with `is_model_answer` set. Sensitivity:
  `none_found: true` — this chapter's comedy touches nobody's community, body or poverty in a way A8
  judged flaggable, and the hard items that do guard the humour live in `07_pitfalls.json` instead.
- **F — shape and media.** All 12 invariants hold. The four Hindi-run rejections are clear:
  `publication_id` non-null, `topic_type` mappable to the closed enum, segment recalls not `.SR{n}`,
  concept numbers chapter-continuous. `chapter_id` and `plan_id` follow `naming_conventions.md` and
  are **provisional until VERIFY-1** — the `gseb` board and `eng` medium segments are reasoned from
  Hindi precedent, not read from the live server, and a wrong medium uploads clean.
- **G — the seven usual mistakes.** None present. The chapter is taught as a repetition-with-
  escalation joke, not as સાર + બોધ + પ્રશ્નોત્તર; no scene is merged or split; no licence is
  corrected; no અલંકાર is named; no example is pitched at an adult; no સ્વાધ્યાય block is a topic.
- **A4 notes carried here, all non-blocking.** `04_validation.json` records `status: pass`,
  `converged: true`, `blocking: []`, `ids_frozen: true` on its third invocation and first on this
  artifact. Its open notes: uneven topic length (`M2.S4.T5` is one long printed paragraph carrying
  two moves, hence its two concepts; `M3.S6.T7` is a single printed line) — the lengths follow the
  printed beats and were correctly not evened out. Segment name `લલચાયેલા બે ભાઈબંધ` uses `લલચા-`,
  which is not a printed word in this chapter though it describes what the page shows; it is not the
  evaluative ખોટો/લોભી/ચોર register the avoid-list bars, and I let it stand. O2 and O5 use
  `કેમ`/`કઈ રીતે` phrasings near gate 2's bar on motive-hunting; both are answered from printed
  words in the authored recall answers, so they stay inside the line.

## Media

7 scenes, 7 authored prompts, 0 reused, 0 rejected — `Images: 0/7` is the correct reading in this
pack, not a missing field: **no Gujarati frame pool exists**, so reuse is dormant and every scene
carries an authored `generation_prompt` with `image_url: ""`. One image per પ્રસંગ, each a single
photographable moment; each narrator bar names its exact Gujarati line (`જાંબુ લ્યો ! મીઠાં મધ જેવાં
જાંબુ !`, `મગનની લૂલી જરા લબક લબક થવા લાગી.`, `જાંબુને બદલે હાથમાં આવ્યા ઠળિયા !`, …). No `2d_tool`
— this સ્વરૂપ rarely earns the one permitted per chapter and did not earn it here. The chapter's two
printed illustrations (the fruit-cart market scene on printed p. 30 and the two-men-on-a-path scene
on p. 31, `extraction_note[23]`) are page matter and correctly opened no topic of their own.

## Gaps

1. **`textbook_url` is a local path**, `../Textbooks-pdf/std-7/ch-06-jo-kari-jambue.pdf`. The GSEB
   readers have no hosted URL. Recorded by A11 as an honest gap, fail-soft, never blocking. A11's
   pagination itself is `high` confidence — `30–36` agrees across the printed footers, the manifest
   row and the std-7 `+13` offset, so pagination is a filled field, not a gap.
2. **`publication_chunk` is `original_chunk` + `\n\n` + the publication rewrite + `\n\n` + the
   rewritten anchor, not `original_chunk` alone.** This agent's spec states the check as
   "`publication_chunk` is byte-identical to `original_chunk`". Here it is not — but the verbatim is
   untouched and stands whole and byte-exact at the head of the field on all 7 topics, which is the
   rule the check exists to protect. **This is a pack-wide inconsistency, not a ch06 defect**, and
   it was re-measured across the pack this pass: `output7/ch01` (0/5 identical), `ch02` (0/9),
   `ch03` (0/13), `ch04` (0/6), `output6/ch01` (0/3) all build `publication_chunk` the same way;
   only `output7/ch05` (4/4) writes it byte-identical. Reported, not blocked (§Publication is not an
   A–D section, and §B's verbatim requirement is met). **A16's contract and this spec line should be
   reconciled once, pack-wide, rather than per chapter** — and whichever way it settles, `ch05` or
   `ch01`–`ch06` will need a re-emit.
3. **`chapter_master_id` and `subject_ref_id` are `null`.** No GSEB record is confirmed; both must be
   fetched from the education DB at VERIFY-2. Neither was invented and neither was derived by
   arithmetic — the Hindi `355 − chapter number` pattern is CBSE provenance and does not transfer.
4. **`publication_id` is written as `1`, and `1` is CBSE's publication row.** It is written non-null
   because the server rejects null, and it matches this pack's standing provisional value
   (`output7/ch02`–`ch05`, `output6/ch01`). **It must be replaced by the verified GSEB publication
   row at VERIFY-2 before any Phase 8 upload.** Shipping `1` unverified mis-files the plan.
5. **Root `genre` carries the descriptive Gujarati form name `રમૂજી પ્રસંગકથા`,** merged from
   `01_meta.json` as this agent's spec directs, while `phase2_contract.md` wants the roster **slug**
   in the emitted plan. `05_with_content.json` carries both (`genre` and
   `genre_slug: "nibandh_atmaparak"`), and A4 flagged this as an emit-time mapping: **Agent 14 must
   emit `genre_slug`'s value in root `genre`** and must not ship the descriptive phrase. Not
   blocking here, and no re-run is needed for it.
6. **Root `topic_title` was authored by nobody.** It is absent from `01_meta.json` and absent from
   this agent's merge table, but it is one of the contract's 32 root keys. It is mirrored from
   `chapter_name` (`જો કરી જાંબુએ`), which is what `output7/ch01`–`ch05` did. A1 should confirm the
   field rather than leave it inferred.
7. **Root `ordering` is not written** — this agent's spec assigns it to Agent 14/15, so the merged
   plan carries 31 root keys and Agent 14 writes the 32nd. (`output7/ch05` wrote `ordering: null` at
   this stage; `ch01`–`ch04` omitted it. Omission matches the spec.)
8. **The verbatim's double-render cross-check was never run as specified** (`extraction_note[12]`).
   The run supplied a single ≈150 dpi render set and forbade re-rasterising, so A1 substituted
   2.2×–8× LANCZOS crops of the same PNGs on each measured confusion class (ધ/ઘ, ળ/ય, ળ/લ, શ/ષ/સ,
   અનુસ્વાર presence). That is weaker evidence than an independent higher-dpi rasterisation. **A 200
   dpi re-render is recommended before the verbatim is treated as VERIFIED.** This gate could
   confirm that each `original_chunk` matches `00_chapter_normalized.md` exactly — and it does, 7 of
   7 — but that establishes fidelity to the transcription, not the transcription's fidelity to the
   page. This is a standing caveat on the transcription, not a defect found in it.
9. **`original_chunk` collapses the transcription's blank-line paragraph separators to a single
   `\n`.** Newly measured this pass, and recorded so nobody later reads it as drift: on 6 of the 7
   topics the `[[ઘટના: …]]` block in `00_chapter_normalized.md` separates paragraphs with `\n\n`
   while the chunk uses `\n` (T7 is a single line and is byte-identical). Every paragraph boundary
   survives and **not one Gujarati character differs** — only the markdown authoring blank line was
   dropped. Non-blocking, and it did not come from this merge, which reproduced
   `05_with_content.json`'s chunks byte for byte.
10. **Printed defects transcribed as printed, never repaired** — recorded so no downstream agent
    "fixes" them: two exercise blocks both numbered `10.`; `નાથીમાનું નાક` in exercise block three's
    કોઠો where the story prints `નાથિયાનું`; `આસ્તેક` glossed in the શબ્દાર્થ box but absent from the
    story; five unclosed or mismatched quotation pairs on printed pp. 30–32; the spaced `કે’ જે` at a
    justified line start; GSEB's spaced ` !` and ` ?`.
11. **Profile gate 11's literal wording does not fit two of the five carriers.** The gate expects
    each carrier topic to hold "both the eating and the substitution". The page prints a substitution
    for મગન, રામજી and નાથિયો only; મોંઘીમા finds ઠળિયા after eating one જાંબુ, and પશી eats the
    single one left. Each of those topics still holds its own setup and its own payoff in one piece.
    **No substitution may be invented for them to complete the pattern** — the asymmetry is the
    escalation the chapter is built on.
12. **`01_meta.json`'s `explanation_unit` carries the Roman word `topic` in its prose.** Not a
    deliverable defect — the field is a diagnosis note, is not a contract root key, and does not
    ship — but it is the same habit that produced the `teaching_lens` blocker, and A1 may want to
    settle it while the file is open.

## LP2 validator

Not run — filled in Phase 8. `POST /api/lp2/learning-plans/validate` must return zero
`validation_errors` before upload, and the three provisional values above (`publication_id`,
`chapter_master_id`, and the `chapter_id` board/medium segments) must be resolved first.

---

**Verdict: PASS on A–D.** This is the final gate pass, run after every owner re-run had landed, and
nothing was inherited on trust: A–D, the 12 contract invariants, and the exercise, media and
publication checks were all re-measured this pass against the source layers, and the merge itself
was re-verified field by field with zero provenance mismatches. Two loose statements in the previous
report are corrected above — the chapter-level pitfall severities (5 explicitly hard, 2 unmarked,
1 explicitly soft, not 8 hard) and the addition of the paragraph-separator note as Gaps item 9;
neither changes a verdict. Twelve gaps are surfaced deliberately rather than closed by invention;
four of them (`publication_id`, `chapter_master_id`, the `chapter_id` medium segment, and the
`genre`-slug emit mapping) must be resolved before anything is uploaded, and Gaps item 2 asks for a
one-time pack-wide decision on `publication_chunk`. **No re-run is owed by any agent. This chapter
is cleared for Agent 14.**

## LP2 validator

- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json
- HTTP status: 200
- plan_id: gseb_eng_gujarati7_ch6_v1
- validation_errors: [] (none)
- message: "Valid"
