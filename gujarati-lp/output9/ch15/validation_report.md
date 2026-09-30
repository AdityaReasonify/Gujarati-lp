# Validation Report — std 9, ch 15 સો ટચનું સોનું

સ્વરૂપ: સંસ્મરણ / આત્મકથાખંડ (confidence: high)   explanation unit: એક ઘટના (એક પ્રસંગ)
Topics: 15   Objectives: 15   Images: 0/13   Exercises: 13/13 (4/4 blocks)

Deliverable: `13_merged.json`, folding `05_with_content.json` + `12_authoring.json` +
`09_media.json` + `16_publication.json` + `01_meta.json`/`11_pages.json` root fields into one
phase-2 plan. The exercise deliverable (`10_exercise_solutions.json`) already existed and is
gated here, not rewritten.

## A–D (blocking)   **PASS**

Every hard item below was checked programmatically against the merged plan (`13_merged.json`),
not asserted from the intermediate files alone.

**A — diagnosis and lens.** સ્વરૂપ સંસ્મરણ/આત્મકથાખંડ, `genre_confidence: high`, four
`genre_signals` (structure, theme, exercises, purpose) recorded off the rendered page, correctly
naming the near-miss (the page's own કૃતિ-પરિચય calls it "વાર્તા" and the સવિસ્તાર pair
"ચઢતી વર્ણવો"/"પાત્રાલેખન કરો" superficially resembles ચરિત્ર-પ્રસંગ) and resolving it against
`profiles/genres/nibandh_atmaparak.md`'s own provenance list, which names this exact chapter —
the running "હું" is લેખિકા (સુધા મૂર્તિ) herself, who draws her own conclusion and is reminded of
her own mother. Explanation unit `એક ઘટના (એક પ્રસંગ)` matches the roster row for
વાર્તા/ચરિત્ર-શૈલી નિબંધ. `structure_inventory` (`ghatna: 13`) matches the 13 `[[ઘટના: …]]`
markers exactly; `kadi`/`duha`/`pad`/`tek_occurrences` are correctly `0` for this prose piece.
Not a mixed chapter. Apparatus stayed apparatus: `[[શબ્દ-સમજૂતી]]`, `[[ભાષા-અભિવ્યક્તિ]]` and
`[[શિક્ષકની ભૂમિકા]]` carry no topic; `[[લેખક-પરિચય]]` and `[[કૃતિ-પરિચય]]`, printed for the
student, are the two CONCEPT topics the roster allows. No topic carries `topic_category:
"climax"` — verified across all 15 topics — matching the profile's avoid-gate that this chapter
has પ્રસંગ, not પ્લોટ. `guiding_question` ("કુતમ્માની આખી રાતની વાતો સાંભળ્યા પછી લેખિકા પોતે
ભણતરના 'સાચા સોના' વિશે શું સમજે છે…") is chapter-specific and is answered by reading the 15
topics in their printed order, which `05b_textbook_order.json` confirms is identical to the
logical order.

**B — verbatim and structure.** All 15 `original_chunk` fields non-empty; a full codepoint sweep
found **zero** Latin characters, **zero** Devanagari characters (U+0900–097F) and **zero** `।` in
any `original_chunk`. Marker accounting: `00_chapter_normalized.md` carries exactly 15
topic-bearing markers (`[[લેખક-પરિચય]]`, `[[કૃતિ-પરિચય]]`, 13× `[[ઘટના: …]]`) and each is carried
by exactly one topic, in order; **no** `[[સ્વાધ્યાય: …]]` block became a topic. The printed
translator credit `અનુવાદક : સોનલ મોદી` sits inside the **last** topic's (`M4.S7.T15`)
`original_chunk`, exactly where `gujarati_verbatim.md`'s credits-are-text rule places it, and the
render-verified spelling `દિપાવે` (not the more common `દીપાવે`) stands as printed. Every
તળપદું/dialectal form is intact and uncorrected across the plan — `બૌંવ`, `નોં`, `મૂઈ`, `મે'નત`,
`વરહ`, `એરુ`, `ચિંત્યા`, `ગગા`, `ટિચાવું`, `ટેમ`, `ઘૈડું`, `પાળી`, `અલકમલક`, `રૂપકડું` all stand
unmodified wherever quoted, in `original_chunk` and in every field that glosses them. The
Sanskrit-origin શ્લોક (`જનની જન્મભૂમિશ્ચ, સ્વર્ગાદપિ ગરિયસી.`) sits inside `M3.S5.T12`'s
`original_chunk` as chapter content, not an added citation. No header furniture (chapter-number
box, era line, page folios, MCQ option letters) entered any `original_chunk` — those are correctly
recorded as printed apparatus in `01_meta.json`'s `extraction_notes[]` instead. Ids are
consecutive and traversal-verified: `M1`–`M4` / seven segments / `T1`–`T15` / `C1`=`T1` through
`C15`=`T15`.

**C — the teaching block.** Every topic has non-empty `explanation` and `real_life_example`,
both inside the 55–90 word band, verified by direct word count (no trimming needed):

| topic | expl | rle | topic | expl | rle |
|---|---|---|---|---|---|
| M1.S1.T1 | 74 | 81 | M3.S4.T9 | 81 | 67 |
| M1.S1.T2 | 77 | 70 | M3.S4.T10 | 73 | 65 |
| M2.S2.T3 | 73 | 77 | M3.S5.T11 | 77 | 81 |
| M2.S2.T4 | 77 | 74 | M3.S5.T12 | 86 | 65 |
| M2.S2.T5 | 72 | 76 | M4.S6.T13 | 77 | 65 |
| M2.S3.T6 | 68 | 68 | M4.S6.T14 | 80 | 68 |
| M2.S3.T7 | 81 | 73 | M4.S7.T15 | 87 | 70 |
| M3.S4.T8 | 79 | 74 |  |  |  |

`objective_text` O1–O15: 18, 20, 15, 14, 18, 18, 16, 18, 22, 19, 18, 21, 16, 21, 24 words — all
inside 12–30. L2 glossing sits at the point of first use throughout and the everyday-word bar is
held low for this chapter's dense તળપદું register (`બૌંવ`, `મૂઈ`, `નિસાસો`, `આડે પડખે`, `પેટે
પાટા બાંધવા`, `વસમું`, `ખમીરવંતાં` all opened in Gujarati, never silently modernised). Every
`explanation` on a topic whose own chunk carries a first-person form correctly names લેખિકા or
કુતમ્મા as its grammatical subject — including the two nested-quotation hazards
(`M3.S5.T12`'s લેખિકા→કુતમ્મા→her-own-દાદા layer and `M4.S6.T13`'s લેખિકા→કુતમ્મા→ઐયપ્પાના
શબ્દોમાં layer), both resolved layer by layer, naming who speaks at each turn. The two-`બા`
hazard is handled correctly at both its occurrences: `M2.S3.T7` reads "…પોતાનાં (સામે બેઠેલાં
કુતમ્મા નહિ, પોતાનાં) બા યાદ આવી ગયાં" and `M4.S6.T13` reads "'બા' શબ્દ ઐયપ્પાની પોતાની મા
કુતમ્માનો જ છે, લેખિકાનો નહિ." Craft is named only at the std-9 ceiling and only where the
chapter's own ભાષા-અભિવ્યક્તિ apparatus flags it: `વર્ણાનુપ્રાસ` on `M2.S2.T4` ('નાનકડા,
રૂપકડા ગામે'), `M2.S3.T7` ('ભાવુક, ભદ્ર સન્નારી' and 'વિવિધ વ્યંજનો') and `M3.S5.T12` ('શીળું
સ્મિત') — all four `lines` strings verified as exact substrings of their own topic's
`original_chunk`; every other topic correctly carries `figures_of_speech: []` and `rhyme_scheme:
null` (this is ગદ્ય). No દંડ, no Devanagari, no Roman character outside a bracketed technical
term anywhere in an authored field.

**D — સ્વરૂપ essence.** All hard `avoid_checks` in `07_pitfalls.json` (27 items across the 15
topics) and the six chapter-level notes were verified in the field each names, not assumed:

- **Narrator identity.** `M1.S1.T1.explanation`'s first sentence separates સુધા મૂર્તિ's own
  identity (લેખિકા, ઇન્ફોસીસ ફાઉન્ડેશનનાં ચેરપર્સન) from her husband's ("તેમના પતિ નારાયણ
  મૂર્તિએ ઇન્ફોસીસની સ્થાપના કરી હતી, એ એક જુદી ઓળખ છે") — the exact misreading
  `07_pitfalls.json` names is pre-empted. No field anywhere makes the translator (સોનલ મોદી) the
  source of an observation or feeling.
- **No hallucinated biography or institution.** Every proper noun, book title, degree or award
  across all 15 topics traces to `M1.S1.T1`'s own `original_chunk` (કર્ણાટક/શીગાવ, નારાયણ મૂર્તિ,
  ઇન્ફોસીસ, ઇન્ફોસીસ ફાઉન્ડેશન, ઇલેક્ટ્રિકલ એન્જિનિયર, the five named books, પદ્મશ્રી) or to that
  topic's own chunk elsewhere in the chapter (a programmatic sweep for extra
  પુરસ્કાર/ડિગ્રી/ઍવોર્ડ/કૉલેજ mentions outside `M1.S1.T1` found only "કૉલેજ" on `M3.S5.T11` and
  `M4.S6.T13`, both tracing to the chunk's own "રાતની કોલેજ" / "કૉલેજ મોકલવા" — no institution
  named that the text does not name itself). The મોતીભાઈ અમીન reference inside the teacher-only
  `શિક્ષકની ભૂમિકા` apparatus does not appear in any topic's `explanation`, `summary` or recall
  `answer`.
- **No בોધ/ઉપદેશ forced.** A sweep of every `explanation`, `real_life_example` and summary field
  for generalising-lecture patterns (`આપણે પણ`, `શીખવે છે કે`, `બોધ મળે છે`, `જોઈએ.`) returned
  **zero** hits beyond the chapter's own printed synopsis line, which is correctly attributed to
  the text itself, never appended as the plan's own moral.
- **No plot-language on a પ્રસંગ-શ્રેણી.** No topic carries `topic_category: "climax"`; a sweep
  for `વળાંક` / `કસોટી-જીત` across every authored field returned zero hits. `M3.S4.T10`'s
  snake-bite scene is framed in its own `explanation` as a second memory reaffirming કુતમ્માની
  resolve, not a turning point.
- **તળપદું intact.** No field anywhere offers a "correct form" for a printed dialectal or
  colloquial word — checked against the full list (`બૌંવ`, `નોં`, `મૂઈ`, `ટિચાવું`, `ટેમ`,
  `ઘૈડું`, `પાળી`, `ગગા`, `અલકમલક`, `રૂપકડું`) across every field that quotes or glosses them.
- **Dignity held on every soft sensitivity item.** All six `08_sensitivity.json` topics (severity
  `soft` throughout — no `hard` items in this file) were checked in the actual authored fields:
  `M1.S1.T2`'s "ગરીબ વિધવા" carries no widow-pity framing; `M2.S2.T3`'s hospitality point restates
  the chunk's own correlation without adding a poverty-produces-virtue lecture, and its
  `real_life_example` anchors on the concrete welcome, not a wealth comparison; `M3.S4.T9`'s
  family-planning line stays કુતમ્માની પોતાની યાદ, never a rule prescribed to the class;
  `M3.S5.T11`'s explanation and example praise ઐયપ્પાની ધીરજ and night-study, not child labour
  itself; `M3.S5.T12` explains the શ્લોકનો ભાવ (love of one's own land) without unpacking સ્વર્ગ
  as doctrine; `M4.S7.T15` stays tied to the line's own point about one educated woman, without
  generalising women's role or duty. No field anywhere uses "બિચારાં"/"ગરીબ-બિચારી" framing. The
  chapter-level guidance that કુતમ્માની બોલી is the Gujarati translator's stylistic choice
  (Saurashtra-flavoured તળપદું for a Karnataka-coast character), not authentic Kanara speech, is
  respected — no field claims otherwise.
- `figures_of_speech` — see C above; all four verified verbatim substrings, none invented.

## E–G (reported)

**E — સ્વાધ્યાય and risk.** All four inventoried blocks (MCQ×5, બે-ત્રણ વાક્યમાં×3, સવિસ્તાર×2,
વિદ્યાર્થી-પ્રવૃત્તિ×3 = 13 items) are answered in `10_exercise_solutions.json`;
`coverage_report.blocks_found` (4) equals the inventory length, `unanswered` and `unmapped` are
both empty, and every `covered_by_topics` id resolves to a real topic. The three
વિદ્યાર્થી-પ્રવૃત્તિ items are the only ones marked `is_model_answer: true`, correctly. EX5 (the
cross-chapter MCQ whose three wrong options are other chapters' titles) is handled exactly as
`no_hallucination_policy.md` requires: the correct option is verified against this chapter's own
text, and the `teacher_note` states plainly that the other three options could not be checked
against text this agent does not have, rather than guessing. Sensitivity guidance from
`08_sensitivity.json` is applied, not censored, on every topic it names (see D above).

**F — shape and media.** All 12 `json_contract.md` invariants verified programmatically against
`13_merged.json`: `phase: 2`; `chapter_id` = `gseb_eng_gujarati9_ch15`; `plan_id` =
`gseb_eng_gujarati9_ch15_v1`; every topic has exactly one concept with a resolving `objective_id`
and non-empty `content[]`; the objectives registry is complete and consistent (15 unique ids,
every `home_topic_id` and every `anchor[]` entry resolves, `strand_to_objective_map` covers
L1–L15 exactly, single strand `L`); every inline `learning_objectives[]` mirror matches its root
`objective_text` character for character and carries `image_examples: []`; concept ids are
chapter-continuous and equal their topic number throughout (`C1`=`T1` … `C15`=`T15`), verified
against the traversal; recall ids are `{topic}.RQ{n}` with `legacy_id` `{topic}.TR{n}` and **no
`.SR{n}` anywhere** (45 recall questions swept); media ids match `MEDIA_ID_RE`, concept-scoped;
`publication_id` non-null (see Gaps); summaries strictly increase at every one of the 15 topics
(verified by length); a full digit sweep (Latin and Gujarati numerals) across every `topic_name`,
`explanation`, `real_life_example`, summary, bullet, recall prompt/answer, `objective_text`,
`publication_text` and `publication_chunk` returned **zero** hits.

`topic_type` is `CONCEPT` (M1.S1.T1, M1.S1.T2) and `STORY_TELLING` (the other 13) throughout —
the correct authored enum for an Agent-13 intermediate file per `phase2_contract.md`'s own
statement that "intermediate files (Agents 02–13) carry `POEM | STORY_TELLING | CONCEPT |
REVIEW`"; the closed server enum (`instructional`/`summary`/`assessment`) is Agent 14/15's
mapping at emit, not this file's.

Bands from `field_shape_rules.md`, all held: `key_terms` 5 per topic (band 3–6); `concept_bullets`
and `important_points` 4 each (band 3–4); `recall_questions` 3 per topic (band 2–3),
Bloom-laddered remember→understand→analyze, every "analyze" item citing a quoted line;
`shabdarth` 5 per topic, `samanarthi` 2 per topic, `vilom` 0–1 per topic, `vyakaran` 3 per topic —
all inside `bhasha_bodh.md`'s 3–6/2–4/0–3/2–3 bands; every `vyakaran.bindu` value drawn from the
canonical + std-9 additions list (કૃદંત, જાતિ, નામયોગી, સર્વનામ, વિશેષણ, કાળ, નિપાત, સંયોજક,
ક્રિયાવિશેષણ, વિરામચિહ્નો, રૂઢિપ્રયોગ, સમાસ) — no છંદ, no પ્રયોગ, no બહુવ્રીહિ/દ્વિગુ anywhere.
Every `shabdarth`/`samanarthi`/`vilom` headword traces to its own topic's `original_chunk` (idiom
headwords given in dictionary/infinitive form — `લાગણીતંતુ બંધાવો` for the chunk's `બંધાઈ ગયો`,
`આડે પડખે થવું` for `આડે પડખે થઈ` — is the expected citation convention, not a mismatch).
`estimated_exchanges` is `"4"` throughout, a small-integer string. `bloom_level` lowercase in
recalls and Capitalised in `objectives[]`, the required asymmetry held.

**G — the seven usual mistakes.** None present. The plan teaches the સંસ્મરણ (voice + episode +
self-reflection) rather than સાર+બોધ+પ્રશ્નોત્તર; this genre has no કડી/દુહો/પદ to merge or split;
no dialectal form silently corrected; no અલંકાર named because the field existed (14 of 15 topics
honestly carry `[]`); every `real_life_example` is single, Indian, and inside std-9 reach; the
family-planning, child-labour and શ્લોક sensitivity items are handled with dignity rather than
softened or amplified; સ્વાધ્યાય was not cut as topics and the exercise deliverable is full
(13/13).

## Media

`reuse_report`: scenes 13, authored 13, **reused 0**, rejected none — matching the 13 topics
(all except the two CONCEPT intro topics `M1.S1.T1`/`M1.S1.T2`) whose `available_content_types`
carry `"image"`. Every media node carries `image_url: ""` **and** a real, self-contained
`generation_prompt`; no `[reused frame: …]` stamp and no fabricated URL anywhere. Every
`negative_prompt` carries `Devanagari script labels`, several tailored per scene (e.g. `M2.S2.T3`
adds "pitying or mocking depiction of poverty" and "'poor unfortunate' framing" given its
hospitality/poverty sensitivity note). `2d_tool` is `null` chapter-wide (≤1 satisfied trivially).
`M1.S1.T1`/`M1.S1.T2` correctly carry `media: []` (CONCEPT topics, `available_content_types: []`).

## Gaps

1. **`publication_id` is provisional and must not ship as written.** Written as `1`, matching
   this pack's established placeholder convention on every prior chapter checked (`output6`
   through `output10`), but the contract states plainly that CBSE's `1` is not portable to GSEB.
   **VERIFY-2 must resolve the real GSEB publication row before the first Phase 8 upload.** Not
   an A–D failure of this run; a hard precondition of upload.
2. **`chapter_master_id` is `null`** — mandatory for upload, not discoverable from the LP2 API,
   fetched per chapter from the education DB (VERIFY-2); never derived by arithmetic.
3. **`textbook` title is carried at `medium` confidence**, per `11_pages.json`: read from this
   chapter's own page-1 running footer (`ગુજરાતી (દ્વિતીય ભાષા), ધોરણ ૯`), not from a confirmed
   std-9 cover render. Fail-soft, carried, flagged. Owner
   `agents/01_ingestion_genre_diagnosis.md` if a cover render becomes available.
4. **`textbook_url` is a local path string** — the GSEB readers have no hosted URL.
   `textbook_pages` `76–79` at `medium` confidence, cross-checked against the manifest's std-9
   offset row and agreeing.
5. **`topic_title` was derived, not authored** — set to the printed chapter title `સો ટચનું
   સોનું`, matching `chapter_name`, per this pack's established convention where there is no
   separate topic layer above the chapter.
6. **`ordering` is deliberately absent** from `13_merged.json` — it is Agent 14/15's to set. 31 of
   the contract's 32 root keys are written; `ordering` is the one withheld.
7. **Board and medium segments are PROVISIONAL until VERIFY-1.** `gseb_eng_gujarati9_ch15`
   uploads clean under a wrong medium and mis-files the plan silently. Confirm before the first
   upload.
8. **`publication_chunk` — the same documented tension between two specs as on prior chapters,
   resolved the same way.** This gate's own spec text says `publication_chunk` is
   "byte-identical to `original_chunk`"; `agents/16_publication_authoring.md` says the field is
   "the publication-facing version of the topic's block **as a whole**," inside which "the
   verbatim `original_chunk` **stays verbatim**." The file follows the producing agent's own
   spec: on all 15 topics, `publication_chunk` was verified (not eyeballed) to carry
   `original_chunk` byte-identical as a prefix, followed by publication-facing prose built from
   `explanation` and `real_life_example` with every vocative and direct second-person question
   stripped (e.g. `M1.S1.T2`'s closing "તમારા ઘરમાં તમારા ભણતર માટે…?" does not survive into its
   `publication_chunk`). The narrative prose itself is not rewritten, reflowed or re-punctuated;
   the translator credit line and every dialectal spelling stand exactly as printed. The
   substantive invariant — the rewrite never touches verbatim — holds. Not blocked, for the same
   reason as on prior chapters: doing so would send `16_publication_authoring.md` back to undo
   what its own spec mandates. The two specs still need a human reconciliation.
9. **`vyakaran.udaharan` sometimes abbreviates the quoted line with an ellipsis** rather than
   reproducing it byte-for-byte (e.g. `M2.S2.T4`'s "આપને તેમના ઘરે રહેવું ફાવશે? … રોકાઈ જ…").
   `reference/bhasha_bodh.md` requires only that the grammar point's headword/example be "from the
   text," and the hard byte-verbatim requirement in `json_contract.md` item 11 names
   `figures_of_speech.lines` specifically, not `vyakaran.udaharan` — all four
   `figures_of_speech.lines` strings *were* verified as exact substrings (see C/D above). Not
   blocking; noted for consistency review.
10. **12_authoring.json's own `notes[]` states "vilom is empty for every topic in this chapter,"**
    but the data itself carries two non-empty `vilom` entries (`M2.S2.T4`: અપરિણીત–પરિણીત;
    `M2.S3.T6`: સાદું–ભપકાદાર), both verified as genuine chunk-anchored pairs. The note is stale
    documentation inside Agent 12's own file, not a defect in the plan; recorded here rather than
    silently corrected, since Agent 13 does not repair another agent's authored file.
11. **Textbook order equals logical order** (`05b_textbook_order.json` matches
    `05_with_content.json`'s traversal exactly) — this chapter has no separate printed sequencing
    to reconcile. Per `phase2_contract.md`, Agent 14/15 should raise
    `human_confirmation_required` for this when emitting the two deliverables; not this agent's
    output to produce.
12. **Context routing, reported not guessed.** `author.md`, `no_hallucination_policy.md`,
    `global_content_rules.md` and `teaching_voice_gu.md` were read in full per this run's
    instructions; `qc_checklist.md`, `json_contract.md`, `phase2_contract.md`,
    `field_shape_rules.md` and `reference/bhasha_bodh.md` were read in full from the repository.
    `output9/ch01`'s own `13_merged.json` and `validation_report.md`, plus `output10/ch01`'s
    `13_merged.json`, were read to confirm field shapes and root-key conventions this chapter's
    own inputs left ambiguous (`topic_title`, `estimated_time`, the `publication_id` placeholder,
    the media-node key set, `word_count`'s stripped `modified` key); none of their illustrative
    content was copied into this chapter's plan.
13. **No page render was re-opened by this agent.** `00_chapter_normalized.md` and the chain of
    prior agents' own provenance notes (Agent 1's 150+200 dpi cross-check recorded in
    `extraction_notes[]`, Agent 10's fresh-render coverage check) answered every question this
    gate asked.
## LP2 validator

**PASS.** Validation complete at 2026-08-30 Phase 8.

POST to https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate returned HTTP 200:

```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati9_ch15_v1",
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

**Validation errors: 0**
