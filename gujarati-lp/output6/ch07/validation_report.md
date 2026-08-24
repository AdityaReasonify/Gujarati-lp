# Validation Report — std 6, ch 07 · ચોખ્ખાઈના સરદાર
સ્વરૂપ: ઊર્મિકાવ્ય-ગીત (કૂચગીત) — roster slug `urmikavya_geet` (confidence: high)   explanation unit: એક કડી
Topics: 6   Objectives: 6   Images: 0/6   Exercises: 38/38 items · 13/13 printed blocks

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + root fields of `01_meta.json` → `13_merged.json` (31 root keys; `ordering` left
to Agent 14/15). No working field survived the merge (markers, source-line spans, avoid_checks,
reuse scores, transcription and validation notes all dropped — checked mechanically).

## A–D (blocking)   **PASS**

**A — diagnosis and lens.** Four signals agree on a sung ગીત with a ટેક, and the blue intro box
names the form in the book's own words ('અહીં ‘કૂચગીત’ દ્વારા આ સંદેશ આપવામાં આવ્યો છે'), quoted as
evidence and not as the verdict. કૂચગીત is held under `urmikavya_geet.md`, whose explanation unit is
**one કડી** — and the cut is one કડી per topic, six of them. The `- સંકલિત` author slot (a લોકગીત
tell) was weighed and rejected on the profile's own near-miss row, with the reasoning recorded in
`01_meta.json` `extraction_notes[]` rather than decided silently.
**ટેક handled as content:** the ટેક's wording never changes across the poem, so it is taught **once**,
in `M1.S1.T1` (its own concept `C1`), and the five later કડી topics each list `M1.S1.T1` in
`depends_on` — 5/5, the identical-ટેક branch of the profile's structural gate. Apparatus stayed
apparatus: the blue intro box, the શબ્દાર્થ box, the chapter-final green વ્યાકરણપેટી and the
રમતપેટી are transcribed in `00_chapter_normalized.md` and became **no** topic. `guiding_question` is
built from this poem's own phrase and its કડી-by-કડી pictures.

**B — verbatim and structure.** Marker arithmetic: `00_chapter_normalized.md` carries **6** `[[કડી n]]`
markers and **1** `[[ટેક]]`; **6** topics carry a `[[કડી n]]` and exactly **1** carries the `[[ટેક]]`
— 6 = 6, 1 = 1. Zero `[[દુહો]]`, zero `[[પદ]]`, zero `[[ઘટના]]`. **None of the 13 `[[સ્વાધ્યાય: …]]`
blocks became a topic.**
The six `original_chunk`s were concatenated and compared line-for-line against the printed ટેક +
six કડી in `00_chapter_normalized.md`: **26 lines, 26 lines, byte-identical, in printed order** —
nothing merged, split, reflowed, re-spaced or reordered. The printed anomalies survive as set:
the ellipsis shorthand `ચોખ્ખાઈના સરદાર અમે સહુ...` is never expanded inside the verbatim; કડી પાંચની
ત્રીજી પંક્તિ keeps its **two** dots (`દેશનું નામ રોશન થાશે.. કેમકે,`) where the others print three;
કડી છ keeps `કેમકે` with no comma. Two-column verse was read **down** each column.
Script: every child-facing string is Gujarati (U+0A80–0AFF) — **no Roman, no Devanagari** outside a
bracketed technical term, and **no `।` anywhere**. Roman characters occur only in ids, enums and
provenance fields (`board`, `chapter_id`, `bloom_level`, `topic_type`, media prompts), which is
where the contract puts them. This chapter has **no** whitelisted printed non-Gujarati content, and
`01_meta.json` records the danda's total absence from the page.

**C — the teaching block.** All six topics carry a non-empty `explanation` **and**
`real_life_example`, every one inside the band:
explanation 78 / 71 / 79 / 76 / 68 / 77 · real_life_example 65 / 66 / 69 / 70 / 65 / 71 (band 55–90).
All six `objective_text` are 16–20 words (band 12–30). No band was widened and no prose was trimmed
by this agent — nothing needed it. Three-tier summaries increase strictly on all six topics
(22<51<102, 19<43<97, 18<40<92, 18<38<99, 19<44<100, 19<49<100). No numerals — Gujarati or Roman —
in any authored display string: `topic_name`, explanations, examples, the three summaries, bullets,
concept text, media titles/descriptions, recall prompts and answers all clean; `પહેલી કડી` /
`છેલ્લી કડી` throughout, never `કડી 1`.

**D — સ્વરૂપ essence.** `figures_of_speech` is `[]` on all six topics — correct and complete at
std 6, where no અલંકાર may be named; the mechanical "lines found verbatim in the chunk" check is
therefore vacuous and passes. No અલંકાર or છંદ name (સજીવારોપણ, રૂપક, ઉપમા, અનુપ્રાસ, પુનરુક્તિ,
અતિશયોક્તિ, માત્રામેળ …) appears anywhere in the plan. Every `rhyme_scheme.rhyming_words` string was
checked against its own `original_chunk` — all present, none invented, and each `note` says plainly
where the endings only half-match (`થાશે — ફરશે`: 'આખા છેડા સરખા નથી, પણ છેલ્લો શે અવાજ એક જ છે').
All **24 hard** `avoid_checks` in `07_pitfalls.json` were re-run mechanically against the merged plan:
- *Slogan gate* — the exhortative string `જોઈએ` appears in **no** `explanation`, `real_life_example`,
  summary, bullet, concept paragraph or recall answer. (Its one occurrence in the plan is noted under
  E–G below and is not an exhortation.)
- *Picture before feeling* — each of T1 / T3 / T4's first explanation sentence names a printed thing
  from its own કડી (વાળઝૂડ+ઘરમાં · શહેર/ગામ · મનથી/નિર્મળ).
- *Craft not skipped* — all six explanations name the કડી's sound (કરીએ-રાખીએ-દઈએ · ચક-ચક/ઝગ-મગ ·
  થાશે-ફરશે · રહીએ-ભૂલીએ · the closing 'શે' · 'ક્તિ' and the repeated 'ચોખ્ખાઈ આપણી').
- *Over-scientifying* — no જીવાણુ, જંતુ, બૅક્ટેરિયા, વાઇરસ, ચેપ, રોગપ્રતિકારક, મલેરિયા, ડેન્ગ્યુ anywhere.
- *Political framing* — no સરકાર, પક્ષ, યોજના, ઝુંબેશ, સેના, સરહદ, રાષ્ટ્રધ્વજ, તિરંગો, ધ્વજવંદન, and
  no real leader's name pulled off the title word 'સરદાર'. `દેશભક્તિ` is used only because કડી છ
  prints it.
- *No literal reading* — T5 states outright that no cloth flag is hoisted and no king is coming;
  T2 keeps 'તન અમારાં ઝગમગતાં' as the same ચકચકાટ as the washed થાળી-વાટકો.
- *Never modernise* — 'થાશે' is quoted as printed and glossed **outside** the quotation
  ('થાશે એટલે થશે'), never repaired inside it.
- *Poster test on the closing કડી* — the last sentence of T6's explanation, its detailed_summary and
  all three recall answers each name something the કડી prints (પ્રાણશક્તિ, દેશભક્તિ, or ટેકનો પોકાર).
- The placard `સ્વચ્છતા ત્યાં પ્રભુતા` printed inside the page-1 illustration is quoted **nowhere** —
  not as verse, not in a rhyme list, not in `key_terms`.
`08_sensitivity.json` carries **no hard items** (two soft topic notes — જાતિ-ભૂમિકા on T4,
સંઘર્ષ on T6 — plus one chapter-level સંઘર્ષ note); all three `areas` values are drawn from the fixed
seven and both soft guidances are visibly honoured in the authored text.

## Contract (json_contract.md, 12 invariants)   **PASS**
`phase: 2` · `chapter_id` = `gseb_eng_gujarati6_ch7` · `plan_id` = `gseb_eng_gujarati6_ch7_v1`.
Registry: 6 objectives, ids unique, every `home_topic_id` and every `anchor[]` concept resolves,
`strand_to_objective_map` covers L1–L6 exactly, every topic's `objective_ids` resolve. Inline
`learning_objectives[]` mirrors match the root `objective_text` **character for character** on all
six topics and each carries `image_examples: []`. Ids checked against traversal position: modules
M1–M2, segments M1.S1 → M2.S4 (chapter-continuous, never restarting), topics T1–T6, concepts
**C1–C7 chapter-continuous** (`M2.S4.T6.C7`). Media ids match `MEDIA_ID_RE` and are concept-scoped.
Recalls are `{topic_id}.RQ{n}` with `legacy_id` `{topic_id}.TR{n}` — **no `.SR{n}` anywhere**; every
answer non-empty. `topic_type` is `POEM` on all six, the authored enum the intermediate files carry;
Agents 14/15 map POEM → `instructional` at emit and the closed server enum correctly does not appear
here. Every topic has ≥1 concept with a resolving `objective_id` and non-empty `content[]`.

## E–G (reported)
- **`publication_id` is written as `1`, and `1` is CBSE's publication row.** `phase2_contract.md`
  says the server rejects `null` but that CBSE's value is **not portable**; `01_meta.json` and
  `04_validation.json` both keep it `null` pending **VERIFY-2**. It is written non-null here per
  `agents/13_assembly_validation.md` and to stay consistent with output6 ch01/ch03/ch04/ch05 — it is
  a placeholder, not a verified GSEB row. **Do not upload before VERIFY-2 replaces it.**
  `chapter_master_id`, `subject_ref_id` and `medium_id` are `null`, correctly.
- **Root `genre` is written as the roster slug `urmikavya_geet`**, not `01_meta.json`'s Gujarati
  `ઊર્મિકાવ્ય-ગીત (કૂચગીત)`. `phase2_contract.md` shows the slug in the root field, and A1 and A4
  both flagged this forward with the instruction that whoever writes the root plan use the slug.
  Recorded so the substitution is visible; the Gujarati form is not lost — it stays in `01_meta.json`.
- **`chapter_id` board/medium segments remain provisional until VERIFY-1.** `gseb_eng_…` uploads
  clean even if wrong and mis-files the plan under the wrong medium column.
- **`textbook` is written with a comma** — `ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 6` — per
  `profiles/boards/gseb_gujarati.md`'s cover reading, where `phase2_contract.md`'s inline sample
  shows a pipe. The cover reading wins; flagged so it is a choice, not a drift.
- **One `જોઈએ` in the plan**, in `M2.S4.T5.rhyme_scheme.note`: 'કડી બોલતાં પગ જાતે જ તાલમાં પડે —
  કૂચગીતને આ જ જોઈએ.' It is a statement about the form's rhythm, not an exhortation of the banned
  shape, and `rhyme_scheme.note` is not among the fields the slogan gate enumerates. Not a violation
  — but `12_authoring.json`'s own note claims the string "occurs nowhere in any authored field",
  which is inexact. Reported, no action.
- **`M2.overall_rhyme_scheme` is `null`.** Deliberate and explained by A12: this is one કૂચગીત split
  across two modules and the form fact is stated once, in `M1.overall_rhyme_scheme`. Not a gap.
- **Three module `difficult_words` are dictionary base forms** — ચકચકતું / ઝગમગતું (printed
  ચકચકતાં / ઝગમગતાં) and લહેરાવું (printed લહેરાશે). Standard glossary practice, not invention.
- **Segment evenness (A4's note, carried here as reported, never blocking):** M1.S2 and M2.S3 hold
  one topic each while M1.S1 and M2.S4 hold two; and `M1.S1.T1` carries six printed lines where the
  other five carry four, a direct consequence of the identical-ટેક fold. A2 and A4 both recorded the
  same judgement. No re-cut is called for.
- **Objectives 6 against reading scenes 7** is that same fold seen from the objectives side. O1's
  `anchor[]` lists both concepts of `M1.S1.T1`, so each of the seven printed scenes still has an
  objective anchor.
- **A stale prior tree was overwritten upstream** (A4's first note): the `04_*` files on disk at the
  start of that run validated a seven-topic tree with the ટેક as its own topic. The tree in this
  merge is the six-topic fold that `agents/02_structure.md` requires for an identical ટેક. Recorded.
- **A4 and A16 each re-rendered the chapter PDF** (`run-s6c7-04`, `run-s6c7-16`) despite the run
  instruction that renders are shared and pre-rasterised. Their readings agree with
  `_renders/page-1.png`…`page-4.png`; noted as a process deviation, not a content defect. This agent
  re-rendered nothing and opened no PNG — `00_chapter_normalized.md` answered every question.

## Media
`reuse_report`: **scenes 6 · authored 6 · reused 0 · rejected []** — and 6 topics carry `"image"` in
`available_content_types`, so 6 = 6 = 6. One image per reading scene, six media nodes, one per topic,
each landing on its own concept (`M1.S1.T1.C1`, `M1.S1.T2.C3`, `M1.S2.T3.C4`, `M2.S3.T4.C5`,
`M2.S4.T5.C6`, `M2.S4.T6.C7`). **Every `image_url` is `""` and every `generation_prompt` is a real
self-contained prompt (1,536–1,785 chars)** — no Gujarati frame pool exists, so a filled `image_url`
or a `[reused frame: …]` stamp would be a fabricated URL; neither appears. Every `negative_prompt`
carries `Devanagari script labels`, and each also blocks the specific hazards of this chapter
(slogan lettering, government emblems, the tricolour, any real leader's portrait, before-and-after
hygiene charts, pity framing, filth close-ups). Each prompt names the exact Gujarati narrator-bar
string to render. **`2d_tool` is `null` for the whole chapter** — 0 ≤ 1.

## Exercises
`exercise_inventory` = 13 blocks; `coverage_report.blocks_found` = 13, matched heading for heading in
printed order; `blocks_answered` = 13; **`unanswered` is empty**; 38 items, every one with a non-empty
answer, 17 of them correctly marked `is_model_answer` (the personal-opinion, પ્રવૃત્તિ and
teacher-addressed items). Every `covered_by_topics` id resolves to a real topic.
**`unmapped` carries 2 entries and is reported, not emptied:** EX31 (પ્રશ્નાર્થ વાક્ય) and EX32
(ઉદ્ગાર વાક્ય) of the વ્યાકરણ block — the poem prints no question mark and no exclamation mark, so
the two sub-items are prepared by the chapter-final green વ્યાકરણપેટી, which is printed matter and
not a reading scene. A10 declined to invent a topic mapping to close the report. Correct.

## Publication
All six topics carry a `publication_text` (75 / 70 / 75 / 73 / 66 / 71 words — inside the teaching
band). Each `publication_chunk` **contains its topic's `original_chunk` byte-for-byte** as its
opening block: the કડી is not rewritten, reflowed, re-punctuated or modernised anywhere in the
rewrite. No vocative or classroom instruction survived — `બાળકો`, `જુઓ —`, `બોલો` appear in **no**
`publication_text`, while the teaching `explanation` keeps them, which is the intended split.
`concept_publication` supplies **7 entries against 7 paragraph blocks**, matched by
`concept_id` + `content_index`, none renumbered, reordered or dropped; the `list` blocks correctly
carry none. Spot-read against `12_authoring.json`: the rewrite drops address and completes the
sentence, and adds no fact, example or reading the teaching block does not have.

## Gaps
- **`textbook_url` is a local path** (`../Textbooks-pdf/std-6/ch-07-chokhkhaina-sardar.pdf`) — the
  GSEB readers have no hosted URL. A11's own recorded gap; fail-soft, never a block.
- **`textbook_pages` `41–44` is high-confidence but partly counted, not re-read.** A11 read folios
  41 and 44 off the renders and counted 42–43 from the manifest's page span; A1's `extraction_notes`
  report all four folios read. Consistent, recorded.
- **`publication_id` and `chapter_master_id` are unverified GSEB rows** (VERIFY-2), and the
  `chapter_id` board/medium segments are unverified (VERIFY-1). These are the three things that must
  be resolved before this plan is uploaded; see E–G above.
- **`english_plan_id` / `english_chapter_id` are `null`.** A Gujarati chapter has no English twin;
  nothing was invented to fill them.
- **`ordering` is absent by design** — Agent 14/15 sets it. `05b_textbook_order.json` records the
  printed order for the textbook plan.
- No transcription was left unverified: A5's six chunks reproduce the printed verse exactly and A16
  re-checked them against page 41 independently.

## LP2 validator

- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json
- HTTP status: 200
- plan_id: gseb_eng_gujarati6_ch7_v1
- validation_errors: [] (none)
- message: Valid

---
**Verdict: A–D PASS.** No blocking item. `13_merged.json` is complete and ready for Agent 14.
The provisional root ids above are recorded gaps, not passes — the plan validates as shape and must
not be uploaded until VERIFY-1 and VERIFY-2 land.
