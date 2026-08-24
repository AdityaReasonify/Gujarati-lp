# Validation Report — std 7, ch 8 · સાદ વરત્યો

સ્વરૂપ: `varta` — sub-form **લોકકથા** (confidence: high)   explanation unit: **એક ઘટના**
Topics: 7   Objectives: 7   Images: 0/7   Exercises: 14/14 blocks (51/51 printed items answered)

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` → `13_merged.json` (31 root keys, 37 topic keys, 3 modules,
5 segments, 7 topics, 10 concepts, 7 media nodes, 0 `2d_tool`). `ordering` is deliberately absent —
Agent 14/15 sets it. No working field (pitfall note, media reuse score, validation flag,
`markers`, `source_lines_00_normalized`, transcription note) survived the merge.

## A–D (blocking)   **PASS**

**A — diagnosis and lens.** `genre_signals` records all four signals off the render; the blue
પ્રવેશપેટી's own label is quoted as evidence, not as the verdict ("તેમણે શૌર્ય અને સ્વાર્પણની લોકકથાઓ
પણ આપી છે. તેમાંની જ આ એક કથા છે."). લોકકથા is a sub-form folded onto `varta.md`, so the roster's
વાર્તા row governs: **one ઘટના per topic**, and all seven topics are cut on a printed ઘટના boundary.
Apparatus stayed out of the plan: the પ્રવેશપેટી, the 25-entry શબ્દાર્થ box, the four-idiom
રૂઢિપ્રયોગ box and the chapter-final green ક્રિયાવિશેષણ box are recorded in
`00_chapter_normalized.md` and are not topics. `guiding_question` is derived from this chapter (the
moment the voice is recognised) and the seven explanations, read in order, answer it.

**B — verbatim and structure.** All 7 `original_chunk`s non-empty and **byte-identical**, line for
line, to the `source_lines_00_normalized` ranges of `00_chapter_normalized.md` (the chunk joins the
transcription's blank separator lines and changes no character). Base script Gujarati
(U+0A80–0AFF) throughout; **zero** Roman and **zero** Devanagari characters anywhere in the plan —
`original_chunk`, teaching prose, publication prose, concept content, recall prompts and answers all
scanned. No `।` introduced anywhere. Discontinuous verbatim on `M2.S3.T5` (line 69, then 75–79)
correctly skips the interleaved `[[ચિત્ર]]` / `[[પૃષ્ઠ 52]]` furniture, and the mid-utterance
`''…તમે છાના રો''` is carried as printed, unclosed. Marker arithmetic: **7 `[[ઘટના: …]]` markers =
7 topics**; `kadi`/`duha`/`pad`/`tek` are 0 by measurement (this is ગદ્ય); **14 `[[સ્વાધ્યાય: …]]`
blocks, 0 of which became a topic.**

**C — the teaching block.** Every topic has non-empty `explanation` **and** `real_life_example`.
All bands hold with no trimming needed:

| topic | orig | explanation | real_life_example | publication_text |
|---|---|---|---|---|
| M1.S1.T1 | 99 | 83 | 66 | 84 |
| M1.S1.T2 | 69 | 75 | 79 | 69 |
| M1.S2.T3 | 148 | 82 | 79 | 81 |
| M2.S3.T4 | 54 | 87 | 75 | 85 |
| M2.S3.T5 | 88 | 85 | 69 | 77 |
| M2.S4.T6 | 97 | 83 | 81 | 82 |
| M3.S5.T7 | 131 | 84 | 67 | 83 |

`objective_text` runs 17–23 words across O1–O7 (band 12–30). Glossing is at the point of first use
and in Gujarati (`ખરખરો`, `સનાન`, `છતરાયા`, `પછેડી`, `જતિ`, `ગૂડો`, `થોકેથોક`); the four printed
રૂઢિપ્રયોગ are glossed where they occur and never read literally. Anchors are Indian, single and
inside std-7 reach — દૂધવાળા ભાઈ, ઢાંકેલી થાળી, રાતે દવા લેવા જવું, ગરબાનું કૂંડાળું, વર્ગમાં આંખો
દબાવવી, ભરેલી બસમાં કંડક્ટર, ફળિયાનાં દાદી — one domain each, no repeats. No craft label above the
std-7 ceiling: no અલંકાર, no છંદ, no સમાસ named anywhere.

**D — સ્વરૂપ essence.** `varta.md`'s avoid list holds:

- *Gate 1 (summary-only)* — every `explanation` adds what `modified_chunk` does not: the order of
  the recognition (hand, then name, then the uncovering), the father's own stated reason for
  `છતરાયા નથી જાવું`, the single word `આજ` in વજેસંગ's ruling, the crowd's astonishment being the
  crowd's and not the author's verdict.
- *Gate 2 (tacked-on બોધ)* — no `explanation`, summary, bullet or recall answer closes on an
  abstract moral; scanned for `શીખવે છે` / `બોધ એ છે` / `આપણે પણ … જોઈએ` / `શિખામણ` / `ઉપદેશ`:
  zero hits.
- *Gate 3 (judging a sympathetic character)* — zero hits on `લૂંટારો` / `ગુનેગાર` / `ક્રૂર` /
  `ખરાબ માણસ` / `દુષ્ટ` / `મૂરખ` anywhere. The chapter's own word `બહારવટિયો` is used and glossed,
  never turned into a verdict on જોગીદાસ or હાદા ખુમાણ.
- *Gate 4 (spoiling the turn)* — `topic_category: "climax"` sits once, on `M2.S3.T5`. The four
  topics before it were scanned for the outcome's own words (`વરત્યો`, `વરતાય`, `વજ પડ્યું`,
  `પરખાય`, `તલવાર`, `હાકોટા`, `જતિનો અવતાર`, `રામરામ`, `અહોભાવ`): **zero hits in all four.**
- *Gate 6 (standardising the dialect)* — every તળપદો form is quoted in its printed shape and glossed
  beside, never replaced: આપા, દી', સનાન, ખરખરો, ડાયરો, ગરાસ, છતરાયા, હાકોટા, જતિ, પાસવાન, મ્હોં,
  થોકેથોક, વરત્યો. The પ્રવેશપેટી's own standing order ("આ પાઠમાં વપરાયેલા તળપદા શબ્દોનો બાળકોને ખાસ
  પરિચય કરાવવો") is met.
- Gates 5, 7 and 8 do not engage: this is not a પૌરાણિક કથા, not an excerpt, and the page prints no
  translator credit.
- `figures_of_speech: []` and `rhyme_scheme: null` on all seven topics, `overall_rhyme_scheme: null`
  on all three modules. **Correct and complete, not a gap** — there is no verse anywhere in the unit
  and std 7 may not name a device. The verbatim-quotation check on `figures_of_speech[].lines` is
  therefore vacuous by measurement.

**07 pitfalls / 08 sensitivity — every `severity: "hard"` item addressed.**
The three hard sensitivity items land where they were raised: `M1.S2.T3` keeps the focus on
હાદા ખુમાણનો નિર્ણય and attaches no criminal label; `M2.S3.T5` keeps the danger real
("નામ પડતાં જ સહુએ પોતપોતાની તલવાર સંભાળી; જોખમ સાચું છે") rather than flattening the turn into
friendship; `M3.S5.T7` frames the rumoured violence as the townspeople's own belief and says so in
the text ("આ લોકોના મનની વાત છે, લેખકનો ચુકાદો નહિ") without expanding the imagery. The two soft
items also hold — `M2.S3.T4` names કાઠી, કણબી, મુસદી exactly as printed, and `M1.S1.T2` teaches
`સનાન` on its own terms. `08_sensitivity.json`'s `areas[]` use only the fixed labels (સંઘર્ષ,
સમુદાય, ક્ષેત્ર).

**Contract — all 12 invariants hold.** `phase: 2`; `plan_id = {chapter_id}_v{version}`;
`chapter_id = gseb_eng_gujarati7_ch8`; every topic has ≥1 concept with resolving `objective_id` and
non-empty `content[]`; `objectives[]` unique, every `home_topic_id` and `anchor[]` resolving;
`strand_to_objective_map` covers L1–L7; **every inline `learning_objectives[]` mirror is
character-for-character identical to the root registry entry** (built at merge from the registry
itself, plus `image_examples: []`); id traversal checked against position —
M1/M2/M3, S1–S5, T1–T7, and **chapter-continuous C1–C10** (three topics carry two concepts, so the
concept counter deliberately runs ahead of the topic counter); all 7 media ids match
`MEDIA_ID_RE` concept-scoped; recall ids are `{topic_id}.RQ{n}` with `legacy_id` `{topic_id}.TR{n}`
— **no `.SR{n}` anywhere**; `publication_id` non-null; `topic_type` is the authored enum
`STORY_TELLING` on all seven, which Agent 14 maps to `instructional`; all three summary tiers
strictly increase on all seven topics; **no digit (Roman or Gujarati) in any display text** —
names, explanations, examples, summaries, bullets, prompts, recall answers, concept content and
publication text all scanned; `original_chunk`, `word_count` and `textbook_pages` keep their
provenance numerals as printed.

**Exercises.** `coverage_report.blocks_found` = 14 = the length of `01_meta.json`'s
`exercise_inventory`, entry for entry in printed order; `unanswered` is empty; all 51 discrete
printed prompts carry a non-empty answer; every `covered_by_topics` id resolves to a real node.

**Media.** `reuse_report`: `scenes: 7`, `authored: 7`, `reused: 0`, `rejected: []` — and 7 is
exactly the count of topics whose `available_content_types` carry `"image"`. Every node has
`image_url: ""` **and** a non-empty self-contained `generation_prompt`; no `[reused frame: …]`
stamp anywhere; every `negative_prompt` carries `Devanagari script labels`; `2d_tool` is `null`
chapter-wide.

**Publication.** All 7 topics carry `publication_text`. Each `publication_chunk` contains its
topic's `original_chunk` **byte-identical**, unreflowed and unrepunctuated, as its opening block —
the verbatim was not touched by the rewrite. `concept_publication` matches
`concepts[].content[]` by index and by count on every topic (paragraph blocks only, as authored;
no index renumbered). The classroom address is gone — `બાળકો`, `જુઓ —`, `બોલો`, `હવે વિચારો`: zero
hits in any `publication_text` or `publication_chunk`. Spot-read against the teaching blocks, no
`publication_text` adds a fact, gloss or reading the teaching block does not have; the only
deletions are the vocative and the classroom instruction (e.g. `M2.S3.T5` drops the pointer to the
રમત block, `M1.S1.T1` drops the homework instruction and states the same fact declaratively).

> **Note on the checklist wording.** Agent 13's spec says "`publication_chunk` is byte-identical to
> `original_chunk`". Read literally that contradicts `agents/16_publication_authoring.md`, which
> defines `publication_chunk` as the whole publication-facing block **with the verbatim
> `original_chunk` kept verbatim inside it**. The check was run in the sense the rule protects: the
> `original_chunk` substring inside `publication_chunk` is byte-identical. Flagged so the spec text
> can be reconciled with 16's, not treated as a defect in this chapter.

## E–G (reported)

- **E** — all 14 printed blocks answered and skill-tagged (reading comprehension 15, writing 9,
  grammar 8, vocabulary 7, listening 6, speaking 5, values 1). 22 of the 51 items are flagged
  `is_model_answer` — the personal-opinion, પ્રવૃત્તિ, રમત and teacher-addressed items are answered
  with teaching values, not skipped. The cloze block's eight blanks are filled in
  `values_filled_for_teaching`. **25 items are reported `unmapped`** and no mapping was invented to
  shrink that list: two open વાતચીત prompts about the child's own school, eight free
  sentence-completion stems, two sentence-expansion seeds, five tongue-twisters/ચારણી lines, the
  civic-imagination prompt, the library activity, the translation ફકરો, five grammar-drill
  sentences and the cloze ફકરો — every one of them printed matter the exercise page supplies from
  outside the story. That is a fact about the page, not a signal the cut missed a scene.
- **F** — the four server-rejection shapes all correct (`publication_id` non-null, `.RQ{n}` not
  `.SR{n}`, chapter-continuous concept numbers, closed `topic_type` enum after Agent 14's mapping).
  `chapter_id` / `plan_id` follow `naming_conventions.md` and stay **provisional until VERIFY-1**.
  One image per reading scene; ≤1 `2d_tool`. Summaries increase; no numbers in display text.
- **G** — none of the seven usual mistakes present: the teaching is not સાર+બોધ+પ્રશ્નોત્તર; there
  is no verse to merge or split; no licence was silently corrected (`મ્હોં`, `દી'`, `છાના રો'`,
  `કે'વાય`, `ના'વું` all intact); no અલંકાર was named to fill a field; every anchor is a std-7
  Indian one; and all 14 સ્વાધ્યાય blocks live in the exercise deliverable, none as a topic.

## Media

`scenes 7 / authored 7 / reused 0 / rejected 0`. No Gujarati frame pool exists, so `Images` reads
**0/7** by design. One image per ઘટના, each written as a single photographable moment
(the news arriving in the hills; the river bath; the father's ruling; the covered head inside the
five-hundred-man ડાયરો; the hand on the head at the turn; the raised hand against the sword-hilts;
the bazaar making way). Character appearance is fixed and repeated across prompts so the seven
frames read as one chapter. `negative_prompt` blocks Devanagari and Roman labels, devotional
poster art, and drawn-sword/battle imagery — which also serves the `08_sensitivity.json` guidance
on `M2.S4.T6`. No `2d_tool`: a story does not need one here.

## Gaps

Honest absences, all reported and none blocking:

1. **`textbook_url` is a local path**, `../Textbooks-pdf/std-7/ch-08-saad-vartyo.pdf` — the GSEB
   readers have no hosted URL (`11_pages.json` `gaps[]`). `textbook_pages: "50–56"` is
   **high** confidence, read off the printed folios on renders 1 and 7.
2. **`chapter_master_id` is `null`.** Required for upload; the GSEB row must be fetched from the
   education DB (VERIFY-2). Never derived by arithmetic — the Hindi pack's `355 − chapter number`
   is CBSE provenance and does not transfer.
3. **`publication_id` is written as `1` — provisional and known non-portable.** The server rejects
   `null`, so a value must stand; `1` is CBSE's publication row, carried by this pack's own
   convention (see the sibling std-7 chapters). It **must** be replaced by the verified GSEB
   publication row before the first Phase 8 upload (VERIFY-2).
4. **`chapter_id` / `plan_id` board and medium segments are provisional (VERIFY-1).** A wrong
   medium slot uploads clean and mis-files the plan.
5. **`subject_ref_id` and `medium_id` are `null`** — server-injected; no confirmed GSEB subject
   record exists.
6. **Root `genre` records the slug `varta`, not `01_meta.json`'s `"લોકકથા"`.** A1 wrote the
   Gujarati sub-form name into `genre`; `04_validation.json` ruled explicitly that the root value
   is the slug with `genre_subform: "લોકકથા"`, and `phase2_contract.md` requires a roster slug.
   Reported for A1 to align `01_meta.json`; not a blocker, and the sub-form is preserved in this
   report and in `05_with_content.json`.
7. **Root `topic_number` is `1`, taken from `01_meta.json`.** Sibling std-7 chapters set
   `topic_number = unit_number` (ch 3 → 3, ch 5 → 5). Reported for A1; the value was not
   overridden here.
8. **`ordering` is absent from `13_merged.json` by design** — Agent 14 sets `"logical"` and
   Agent 15 `"textbook"`.
9. **`05b_textbook_order.json` matches the logical traversal exactly** (T1 → T7, read off printed
   pp. 50–52). Per `phase2_contract.md` §Ordering this must be raised for human confirmation at
   emit: `{"human_confirmation_required": true, "reason": "textbook order is identical to logical
   order"}`.
10. **Printed defect carried through, not corrected:** the સ્વાધ્યાય numbering jumps 3 → 5; there is
    no block "4" on any rendered page. Fourteen blocks numbered 1, 2, 3, 5–15. All fourteen are
    answered and no block 4 was manufactured.
11. **Printed variance between story and exercise, both transcribed as printed:** the story reads
    `''સાચે લખમણ જતિનો અવતાર !''` and `''બીતો હોત તો આવત શા માટે રાજ ?''`, while `જોડકાં જોડો.`
    prints `''સાચો લક્ષ્મણ જતિનો અવતાર !''` and `''… રાજ !''`; the story prints `દાદભા` where the
    ડાયરા sentence prints `કુંવરદાદાભા`. Teaching fields quote the story's wording, exercise answers
    the exercise's. Neither was levelled to the other.
12. **Printed count mismatch in block 15:** nine words in the bank, eight dotted blanks on the page.
    Counted twice off the render; `items` recorded as 8.
13. **Agent 4's non-blocking notes travel here:** topic length is uneven — `M2.S3.T4` is two printed
    sentences while `M3.S5.T7` runs seven paragraphs. The cut is by ઘટના, and merging T4 into T5
    would put the concealment and the recognition in one topic and destroy the turn. Reported,
    not blocking.
14. **No transcription defect to report.** Agent 5 cross-checked all seven chunks character by
    character against the 150 dpi renders and found no mismatch with Agent 1's transcription;
    nothing was repaired.

## LP2 validator

Not run — filled in Phase 8. `POST /api/lp2/learning-plans/validate` must return zero
`validation_errors`, and `chapter_master_id` + the real GSEB `publication_id` must be in place
before that call.

---

**Verdict: A–D PASS. No blocking failure. `13_merged.json` is complete and ready for Agent 14.**

## LP2 validator

- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json
- HTTP status: 200
- validation_errors: [] (zero)
- message: "Valid"
- Result: PASS
