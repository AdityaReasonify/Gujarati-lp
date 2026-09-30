# Validation Report — std 8, ch 13 · લીલી નજર

સ્વરૂપ: વાર્તા (પ્રેરક સંવેદનકથા) — profile `varta.md` (confidence: high)   explanation unit: એક ઘટના

Topics: 6   Objectives: 6   Images: 0/6   Exercises: 64/64 items · 12/12 blocks

Deliverables: two — the plan (`13_merged.json`) and the exercise pack
(`10_exercise_solutions.json`). This unit prints a continuous reading text, so both ship.

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` → `13_merged.json` (31 of the 32 root keys; `ordering` is
Agent 14/15's and is deliberately absent). Every working field was dropped: no `markers`,
`source_lines_00_normalized`, `notes`, `tier`, `agent`, `cut_summary`, `not_cut_as_topics`,
`reuse_report`, `coverage_report`, `avoid_checks`, `severity`, `content_index` or
`concept_publication` survives — verified by a recursive key sweep over the merged file. Root,
topic, module, segment, concept, media and `learning_objectives` key sets are byte-identical to
the sibling `output8/ch02`, `ch03`, `ch04` merges (checked programmatically), confirming the same
shape is being emitted.

## A–D (blocking)   **PASS**

Every hard item below was executed mechanically against the merged plan, not asserted.

**A — diagnosis and lens.** સ્વરૂપ વાર્તા (પ્રેરક સંવેદનકથા), a `varta` root form, `genre_confidence:
high`, four `genre_signals` recorded off the render by A1 (structure, theme, the સ્વાધ્યાય tells —
event-ordering block 5 and speaker-attribution block 3 — and purpose). The blue પ્રવેશપેટી's own
words — "આ એક પ્રેરણાદાયી સંવેદનકથા છે" — are quoted as evidence, not taken as the verdict.

Explanation unit `એક ઘટના` matches the roster row for વાર્તા. Six topics = the six printed
`[[ઘટના: …]]` beats, none merged and none split; the arc runs
પરિચય → ગૂંચ → સંઘર્ષ/કોયડો → ખુલાસો → વળાંક → પરિણામ and `topic_category` records it
(`introduction, core, core, core, climax, resolution`).

Apparatus did not become a reading scene. `05_with_content.json`'s `not_cut_as_topics[]` records
seven deliberate exclusions and none of them appears as a topic: the શીર્ષક-પટ્ટી and લેખક-સ્લોટ
(header furniture) plus the QR badge's code, the blue પ્રવેશપેટી (teacher-addressed — and the
single strongest genre signal on the page, used as evidence only), the yellow શબ્દાર્થ box, the
two answer-bearing pre-blocks (શબ્દસમૂહ માટે એક શબ્દ, રૂઢિપ્રયોગ), the twelve numbered
સ્વાધ્યાય headings, and the closing ચર્ચા-વિચારણા box.

`guiding_question` is derived from this chapter alone — "એક ગરીબ વૃદ્ધ પોતાના મૃત દીકરાની યાદમાં
વાવેલાં વૃક્ષો કઈ રીતે એની 'લીલી નજર' બનીને પશુ-પંખી અને વટેમાર્ગુ સૌનું ભલું કરે છે ?" — and the
six explanations read in order do answer it: it names the trees, the son's memory and the title
phrase, none of which could be transplanted to another chapter.

ટેક / mixed-chapter / revision-checkpoint clauses do not fire and were **not silently skipped**:
`00_chapter_normalized.md` carries zero `[[કડી]]`, `[[દુહો]]`, `[[પદ]]` markers and zero ટેક
occurrences (`structure_inventory` confirms kadi=duha=pad=tek=0); one સ્વરૂપ runs end to end; this
is a numbered reading unit, not a checkpoint.

**B — verbatim and structure.** All six `original_chunk` non-empty and Gujarati script only —
**zero Devanagari, zero Roman, zero `।`**, verified codepoint-wise across U+0A80–0AFF (programmatic
sweep on the merged file). `word_count.original` recomputed per chunk agrees with what is stored:
47, 144, 45, 82, 96, 50 — 464 words of reading text total.

Printed licence intact and *not* levelled across locations: the narrative's own dialectal forms
(`ટોઉં`, `ભેણાં`, `પછે ફકર નહીં`, `બે ચાર ઘડા` with no hyphen, `ડૉકટર` with no virama) stand as
printed inside `original_chunk`, while the સ્વાધ્યાય blocks that quote the same lines keep their
own printed forms (`બે-ચાર ઘડા` hyphenated, `પછી ફકર નહિ`) unharmonised in
`10_exercise_solutions.json` — both are printed content, kept exactly where each occurs.

Two render-verified corrections are threaded through cleanly (see Gaps 8): `M3.S3.T5`'s
`original_chunk` reads `તમારા ઝાડવાંની` (no અનુસ્વાર) and `M3.S3.T6`'s reads `બીજા વર્ષે દેખાયા
નહીં` (with અનુસ્વાર) — both matching what A5 found on the page-2 render at high zoom, not what
`00_chapter_normalized.md` currently prints at those two lines. `publication_chunk` is
byte-identical to the corrected `original_chunk` in all six topics (verified by direct string
comparison, not by inspection).

Marker accounting: `00_chapter_normalized.md` prints **6** `[[ઘટના: …]]` reading markers and **6**
topics carry them, one each — exact match. It prints **12** `[[સ્વાધ્યાય: …]]` blocks and **none**
became a topic; all 12 are in the exercise deliverable, matching `01_meta.json`'s
`exercise_inventory` one-for-one.

Ids are consecutive against the traversal: `M1 M2 M3`, `M1.S1 M2.S2 M3.S3`, `T1…T6`, concepts
`C1…C9` chapter-continuous (three topics carry two concepts, three carry one — the concept
counter never restarts). Every cross-reference resolves: `depends_on` (5 edges, a straight chain
T1→T2→T3→T4→T5→T6, matching `01_meta.json`'s own printed ઘટનાક્રમ arrow), `home_topic_id`,
`anchor[]`, `objective_ids`, media `concept_id`/`home_concept_id`, and every `covered_by_topics`
id in the exercise pack — all checked programmatically against the merged file's own node set.

Paragraph breaks preserved as `\n\n` inside `original_chunk` for `M1.S1.T2` and `M2.S2.T3` (each
three printed paragraphs / speaker turns); the other four topics are single unbroken paragraphs.
No attribution line exists to place — this ચિત્રકથા prints no "- લેખકનું નામ" foot-note (unlike a
poem's છાપ); the author "મકરંદ દવે" sits under the title as header furniture only, already
excluded.

**C — the teaching block.** Every topic has non-empty `explanation` **and** `real_life_example`.
Word counts, all inside the 55–90 band with no trimming required and **no band widened**:

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 70 | 86 |
| M1.S1.T2 | 78 | 75 |
| M2.S2.T3 | 78 | 84 |
| M2.S2.T4 | 81 | 90 |
| M3.S3.T5 | 77 | 81 |
| M3.S3.T6 | 89 | 89 |

`objective_text` O1–O6: 21, 23, 23, 21, 23, 22 words — all inside 12–30.

L2 calibration held: `ટોઉં` and `ભેણાં` — dialectal words the printed શબ્દાર્થ box itself does not
gloss — are opened at first use in `M1.S1.T2`'s `explanation` and `key_terms`, explicitly marked
as spoken forms rather than printing errors, per the specific misconception `07_pitfalls.json`
names for that topic. Other L2-tier words (`રે'ઠાણ`, `મે'નત`, `પાણોતિયો`, `છેટે`, `ધર્મશાળા`) are
glossed at the Ring-2 std-8 bar even though a first-language pack would skip them.

`real_life_example` is Indian, concrete, single and inside std-8 reach in all six: Kutch/Saurashtra
water-turn scarcity, a neighbour's fielded cricket ball, an ST bus stop with no signage, a roadside
water પરબ, a grandmother's embroidery, an old village well nobody remembers the digger of. Not one
is an adult's example, an abstraction, three examples at once, or an anchor needing its own
glossary; each ends on a direct question to the child.

Craft is named at the std-8 ceiling. A sweep for રૂપક / ઉપમા / સજીવારોપણ / ઉત્પ્રેક્ષા / અનુપ્રાસ
/ છંદ / સમાસ / સંધિ / અલંકાર over every authored field on all six topics returns **clean** — no
literary device is labelled anywhere, matching std 6–8's "form experienced, never labelled" rule.

**D — સ્વરૂપ essence.** `varta.md`'s eight-item **avoid** gate holds, checked as string sweeps over
the merged plan, not by reading alone:

1. *Summary-only teaching* — every `explanation` adds motive or craft `modified_chunk` does not
   carry: the 'પણ' turn that opens the trouble (T1), what "પૂછ્યા વિના લઉં તો ચોરી કહેવાય" shows
   about character (T2), the story's own withheld answer as craft (T3), the ધર્મશાળા/વૃક્ષ
   contrast (T4), the seen image causing the response — બતાવ્યું, કહ્યું નહીં (T5), the open
   ending read as the title's own payoff (T6).
2. *A tacked-on બોધ* — a sweep for `આ વાર્તા આપણને શીખવે છે`, `આપણે પણ`, `બોધ એ છે કે`,
   `આપણે બધાએ` over every `explanation`, summary, bullet, concept content block and recall answer
   returns **zero hits**.
3. *Judging a sympathetic character* — a sweep for `ભિખારી`, `ગાંડો`, `મૂરખ`, `ખોટો`, `ગુનેગાર`,
   `અંધશ્રદ્ધાળુ`, `દયામણ` returns **zero hits**; the old man's own negated words ("નથી ભાંગી
   પડ્યો કે નથી ભીખ માગતો") are quoted, never turned into a label.
4. *Spoiling the turn early* — the climax is `M3.S3.T5`. Every preceding topic's `explanation`,
   `summary`, `detailed_summary` and recall answers were swept for the outcome words (`અનાયાસ`,
   `હાથ જોડાઈ`, `જવાબદારી મારે માથે`, `સોમાને હાંક`) — **zero hits**. The resolution topic
   (`M3.S3.T6`)'s own outcome words (`બીજા વર્ષે દેખાયા નહીં`, `લીલી નજર`) were separately swept
   against every earlier topic — **zero hits**.
5. *Debunking or verifying* — not applicable to this sub-form (પ્રેરક સંવેદનકથા, not પૌરાણિક); no
   field science-checks or verifies any event regardless.
6. *Standardising dialect* — not a લોકકથા; `ટોઉં`/`ભેણાં` are glossed as spoken forms, never
   replaced, per the specific hard check `07_pitfalls.json` names for `M1.S1.T2`.
7. *Inventing what the text does not contain* — `M3.S3.T6`'s `explanation`, summaries and every
   recall answer keep "બીજા વર્ષે દેખાયા નહીં" exactly as printed and open-ended; no field states
   or implies the old man died, matching both `07_pitfalls.json`'s hard check and
   `08_sensitivity.json`'s guidance for that topic.
8. *Translator credited as author* — not applicable; no અનુવાદ credit is printed anywhere in this
   chapter.

All **7** `severity: "hard"` items in `07_pitfalls.json` (T1×1, T2×1, T4×2, T5×2, T6×1 — T3 carries
only a soft item) plus its three chapter-level bindings were checked in the field each names; the
spoiler and moral-pattern gates were run as string sweeps rather than read. `08_sensitivity.json`
carries **no `severity: "hard"` item** — all three per-topic notes (T4, T5, T6) and both
chapter-level notes (ધર્મ, સંઘર્ષ) are soft, and each is honoured anyway: T4's explanation centres
on what the old man *does* with his grief rather than the death itself; T5 keeps the text's own
hope-framing (trees and birds, not fear) and gives the doctor's change of heart equal weight; T6
never states "વૃદ્ધનું અવસાન થયું" and instead carries the legacy-continuing frame the guidance
asks for; `ભૈરવની મૂર્તિ`/`જગ્યા` appears only as a location landmark in T1 and T6, never unpacked
as devotional content, in both `explanation` fields.

`figures_of_speech` is `[]` on all six and `rhyme_scheme` is `null` — correct for ગદ્ય, and nothing
was invented to fill a field. Contract invariant 11 holds vacuously.

## E–G (reported)

**E — સ્વાધ્યાય and risk.** All 12 inventoried blocks answered. `coverage_report.blocks_found` = 12
= inventory length, and all 12 `verbatim_heading` strings match exactly. `unanswered` is empty; all
64 items carry a non-empty answer, and 64 equals the sum of the inventory's own `items` counts.
19 items are marked `is_model_answer: true` — the whole વાતચીત block, the report-writing block and
several વાક્ય-રચના items are answered with teaching values rather than skipped. Skill spread:
reading comprehension 31, grammar 12, vocabulary 11, speaking 8, writing 2. Sensitivity guidance is
carried into the exercise answers too — EX9's and EX13's `teacher_note` both explicitly restate the
"never say the old man died" hard gate for the class.

`unmapped` is **9 items, reported and not closed** — EX56–EX63 (the eight-item સંયોજક
paragraph-correction drill: cricket, પાણીપૂરી, a balloon, brushing teeth, clay-modelling, a
farmer's બાજરી/ઘઉં દ્વિધા) and EX64 (the standing, chapter-independent "ચંદ્રમા" અનુવાદ
paragraph). Each is exercise-internal matter with no preparing reading scene in this chapter — the
same std-8 pattern `output8/ch02`'s Gaps record for its own standing અનુવાદ block. **No mapping
was invented to empty the list.**

**F — shape and media.** All 12 `json_contract.md` invariants hold on the merged plan (verified
programmatically): `phase: 2`; `plan_id` = `gseb_eng_gujarati8_ch13_v1`; `chapter_id` =
`gseb_eng_gujarati8_ch13`; every topic has ≥1 concept with a resolving `objective_id` and non-empty
`content[]`; the objectives registry is complete and consistent (6 unique ids, single strand `L` —
ભાષા અને સાહિત્ય, every `home_topic_id`/`anchor[]` resolves, `strand_to_objective_map` covers
L1–L6); every inline `learning_objectives[]` mirror matches its root entry **character for
character** on all fields and carries `image_examples: []`; concept ids are chapter-continuous
`M1.S1.T1.C1 … M3.S3.T6.C9` and were checked against traversal position; recalls are `.RQ{n}` with
`legacy_id` `.TR{n}` and the string `.SR` occurs **nowhere**; media ids match `MEDIA_ID_RE`
concept-scoped; `publication_id` is non-null; summaries strictly increase on every topic; and no
digit — Roman, Gujarati or Devanagari — occurs in any name, explanation, example, summary, bullet,
key term, recall prompt/answer, concept content block, objective text, module or segment name
(beats are named by their own action, never `ઘટના 2`). Provenance fields keep their numerals as
printed: `original_chunk`, `prompt_verbatim`, ids, `word_count`, `textbook_pages`.

`topic_type` is `STORY_TELLING` on all six — correct for an Agent-13 intermediate file;
`phase2_contract.md` fixes this authored enum for Agents 02–13 and has Agents 14/15 map
`STORY_TELLING → instructional` at emit.

Bands from `field_shape_rules.md`: `key_terms` 4–6 per topic (band 3–6) ✔; `concept_bullets` and
`important_points` 4 each (3–4) ✔; `recall_questions` 3 per topic (2–3) ✔, Bloom-laddered
remember → understand → analyze (evaluate on the climax topic) with a real answer each;
`estimated_exchanges` small integer strings ✔; `bloom_level` lowercase in recalls, Capitalised in
`objectives[]` ✔; `word_count` `{"original": int}` ✔; `shabdarth` 4–6, `samanarthi` 2, `vilom` 1,
`vyakaran` 1–2 per topic, inside the std-8 working caps. `difficult_words` is `[]` at module level
— see Gaps 5 (same live reference conflict `output8/ch02` already flagged).

`chapter_id`/`plan_id` follow `gseb_eng_gujarati{grade}_ch{unit_number}` — **provisional until
VERIFY-1** (Gaps 4).

**G — the seven usual mistakes.** None present. The plan teaches the સ્વરૂપ (ઘટના + પાત્ર + વળાંક)
rather than સાર + બોધ + પ્રશ્નોત્તર; mistakes 2–3 are verse-shaped and do not arise (this is prose,
zero કડી/દુહો/પદ markers); the two render-corrected forms (Gaps 8) are reported as corrections, not
silently applied; no અલંકાર named because the field existed — `figures_of_speech` is `[]` six times
over; every `real_life_example` is single, Indian and inside std-8 reach; સ્વાધ્યાય was not cut as
topics and the exercise deliverable is full at 64/64.

## Media

Reuse-report analogue built from the merged file: scenes **6** (every topic whose
`available_content_types` carries `"image"`), authored **6**, **reused 0**, matching
`09_media.json`'s own `reuse_report` (`scenes: 6, authored: 6, reused: 0, rejected: []`). Every
node carries `image_url: ""` **and** a real, self-contained `generation_prompt`; no
`[reused frame: …]` stamp and no fabricated URL anywhere. Every `negative_prompt` carries
`Devanagari script labels`. `2d_tool` is `null` for the whole chapter (0 ≤ 1 satisfied). Media ids
are concept-scoped (`MEDIA_ID_RE` match on all six) and every `concept_id`/`home_concept_id`
resolves to a real concept.

The merge dropped the working key `topic_id` that `09_media.json` carries on each node; it is not
one of the contract's media-node keys, matching how `output8/ch01`–`ch04` dropped it.

## Gaps

Honest absences, each recorded rather than closed by invention.

1. **`publication_id` is provisional and must not ship as written.** The contract requires a
   non-null value and `phase2_contract.md` states CBSE's `1` is **not portable** to GSEB. `1` is
   written here as the placeholder the shape demands, matching `output8/ch01`–`ch05`.
   **VERIFY-2 must resolve the real GSEB publication row before the first Phase 8 upload.** Not an
   A–D failure of this run; a hard precondition of upload.
2. **`chapter_master_id` is `null`.** Mandatory for upload, not discoverable from the LP2 API,
   fetched per chapter from the education DB (VERIFY-2). Never derived by arithmetic.
3. **`textbook` title is not confirmed off a rendered cover.** `01_meta.json` sets it `null` on
   purpose — the std-8 cover was not among the six renders supplied for this chapter, and
   `profiles/boards/gseb_gujarati.md` records the std-8 cover as not yet read. The merged plan
   carries `11_pages.json`'s `"ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 8"`, board-profile convention rather
   than a confirmed page — `11_pages.json` flags exactly this in its own `gaps[]`. Fail-soft,
   carried, flagged. Owner `01_ingestion_genre_diagnosis.md`.
4. **Board and medium segments are PROVISIONAL until VERIFY-1.** `gseb_eng_gujarati8_ch13` uploads
   **clean** under a wrong medium and mis-files the plan silently — the failure that shipped all
   23 Hindi plans under the wrong medium once. Confirm before the first upload.
5. **Module `difficult_words` is `[]` and `overall_rhyme_scheme` is `null` — a live reference
   conflict, the same one `output8/ch02` and `ch03` already flagged, reported not repaired here
   either.** `field_shape_rules.md`'s own table lists `difficult_words[]` as "module level, 5–10"
   with no ગદ્ય carve-out stated in that file, while Agent 12's governing references (not supplied
   to this run — `reference/alankar_chhand.md`, `reference/shabd_gloss.md`) reportedly place both
   module-level fields under કાવ્ય topics and leave them empty for ગદ્ય. This agent was not given
   those two files and cannot adjudicate which side is right (per this run's CONTEXT ROUTING
   instruction) — the conflict is reported, not resolved. The vocabulary load is carried instead by
   per-topic `shabdarth` (5–6 entries on every topic, **31** in all) and by inline glossing inside
   `explanation`. **Not blocked** — blocking would send A12 back to undo what its own governing
   reference reportedly mandates.
6. **`textbook_url` is a local path string** (`../Textbooks-pdf/std-8/ch-13-lili-najar.pdf`) — the
   GSEB readers have no hosted URL. `textbook_pages` `108–113` is `confidence: medium`, read off
   the printed folios on the page-1 and page-6 renders per `11_pages.json`.
7. **`topic_title` was derived, not authored.** No agent supplies it and the root key list requires
   it; set here to the printed chapter title `લીલી નજર`, matching `output8/ch01`–`ch04`'s
   convention. If GSEB expects something else, that is `01_ingestion_genre_diagnosis.md`'s field to
   set.
8. **Two render-verified transcription corrections are threaded into `original_chunk` but were not
   retro-applied to `00_chapter_normalized.md`.** A5's own notes in `05_with_content.json` report
   both, and this run re-confirmed both are still present in `00_chapter_normalized.md` as read for
   this gate: line 58 there still reads `તમારાં ઝાડવાંની જવાબદારી મારે માથે` (with અનુસ્વાર) where
   the page-2 render, re-checked at 8–10× zoom, shows `તમારા` (no dot); line 64 there still reads
   `બીજા વર્ષે દેખાયા નહિ` (no અનુસ્વાર) where the render shows `નહીં` (with dot, distinguishable
   from the genuinely dot-less `નહિ` two lines earlier at line 57). `13_merged.json`'s
   `original_chunk`/`publication_chunk` correctly carry the **render-verified** forms (`તમારા`,
   `નહીં`) in both places — confirmed by direct string comparison in this gate — so the merged plan
   itself is not affected. Recorded so a future re-run of A1/A5 against
   `00_chapter_normalized.md` sees the still-stale readings rather than silently re-introducing
   them. Owner (of the `.md` file, not of the plan): `01_ingestion_genre_diagnosis.md`.
9. **A small three-way wording inconsistency inside one exercise answer, non-blocking.**
   `10_exercise_solutions.json`'s EX22 (the ફકરા-સુધારણા block) reconstructs the corrected
   paragraph with `તમારાં ઝાડવાંની જવાબદારી મારે માથે` — but the exercise's own printed prompt (not
   one of its five underlined blanks) reads `તમારી ઝાડવાંની`, and the story's render-verified
   `original_chunk` reads `તમારા ઝાડવાંની` (Gaps 8). Three different forms across three locations
   for a word that was never one of the five words the exercise asks the child to fix. Does not
   affect any A–D gate (the five graded substitutions — ખાણી→પાણી, કાને→માથે, હોકો→હાંક,
   બાળા→બાપા, જ્ઞાન→ધ્યાન — are all correct) and is reported rather than silently edited, since
   repairing exercise answers is `10_exercise_solutions.md`'s job, not this gate's. Owner
   `10_exercise_solutions.md` (A10), if a human wants it tightened.
10. **Uneven topic length, non-blocking** (A2 → A4). `M1.S1.T2` (144 words, three paragraphs of
    dialogue) is the chapter's longest topic while `M2.S2.T3` (45 words) is its shortest. The
    unevenness follows the printed વાર્તા-પગલાં and A2 correctly declined to split or merge a beat
    to even them out.
11. **`M2.S2.T3` deliberately withholds the reveal**, per its own soft pitfall item — the topic
    ends on the doctor's unanswered "શું કામ ?" and no field in this topic states or implies the
    son's-memory reason, which belongs to `M2.S2.T4`. Verified by direct read and by the same
    string sweep used for the hard spoiler gates; reported here because it is the one place the
    "do not explain ahead of the text" instinct could most easily slip.
12. **Context routing, reported not guessed.** All six documents this spec requires
    (`no_hallucination_policy.md`, `global_content_rules.md`, `qc_checklist.md`,
    `json_contract.md`, `phase2_contract.md`, `field_shape_rules.md`) were supplied and read in
    full, along with the active genre profile `profiles/genres/varta.md`. Two files Agent 12's own
    notes cite (`reference/alankar_chhand.md`, `reference/shabd_gloss.md`) were **not** supplied to
    this run — see Gaps 5, where their content is reported as cited, not guessed at.
    `output8/ch02`'s `13_merged.json` was read as a shape precedent only — the merged file's root,
    topic, concept, module, segment, media and `learning_objectives` key sets are **identical** to
    it (checked programmatically), and its `validation_report.md` was read to confirm this report's
    format matches the established one for this pipeline.
13. **No page render was opened by this agent.** `00_chapter_normalized.md` plus
    `05_with_content.json`'s own render-cross-check notes (including the two corrections in Gaps 8)
    answered every question this gate asked, so no PNG in `_renders/` needed to be consulted
    directly.
14. **The pipeline-wide "બાળકો, જુઓ —" explanation opener is a known, established convention, not a
    chapter-13 defect.** All six `explanation` fields open with this phrase; a check against
    `output8/ch02`, `ch03` and `ch04` shows every one of their topics opens the same way. This spec
    scopes the "no vocative or classroom instruction survived (`બાળકો`, `જુઓ —`, `બોલો`)" check
    explicitly to `publication_text`/`publication_chunk`/`concept_publication` — and those fields
    are clean here (grepped, zero hits). `field_shape_rules.md` separately labels `explanation` as
    "teacher voice", which this framing is consistent with. Reported for visibility, not raised as
    an A–D failure, since no document supplied to this run bans it from `explanation` itself.

## LP2 validator

Not run — filled in Phase 8. Two values must be resolved **before** that call or it will fail on
shape regardless of this pass: `publication_id` (Gap 1) and `chapter_master_id` (Gap 2). The
board/medium segments (Gap 4) will **not** fail the validator — they upload clean and mis-file the
plan, which is why they need a human check rather than a validator run.

---

**Verdict: A–D PASS.** No hard item blocks; the run is complete for this gate. Fourteen items are
reported above, of which one is a genuine reference conflict needing a human decision (Gap 5), one
is a small exercise-answer wording inconsistency worth a human glance (Gap 9), and several are
upload preconditions (Gaps 1, 2, 4, 6). Nothing here is a partial pass presented as a pass: each
A–D gate was executed mechanically against the merged plan and each returned clean.

### Result

POST to `https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate`:

```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati8_ch13_v1",
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

**Status: Valid** — `validation_errors` is empty.

