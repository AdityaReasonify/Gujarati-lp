# Validation Report — ધોરણ 6, એકમ 6 — સંસ્કારે સર્જ્યું સ્વર્ગ

સ્વરૂપ: માહિતીપ્રદ ગદ્ય (સંવાદ-શૈલી) — `mahitiprad_gadya.md` પ્રમુખ, `samvad_nibandh.md` નો બે-અવાજનો gate સાથે (confidence: **low**)
explanation unit: એક માહિતી-ખંડ (તથ્ય-ગુચ્છ) — સીમા વક્તા-વળાંક પર નહીં, તથ્ય-પગલા પર

Topics: 8 (M1 = 4 · M2 = 4)   Objectives: 8   Images: 0/8   Exercises: 77/77 items across 16/16 blocks

## A–D (blocking)   **PASS**

**A — diagnosis and lens.** `genre_signals` (structure / theme / exercises / purpose) and
`genre_confidence: "low"` were recorded off the rendered pages by A1; **two** profiles are active and
A7 wrote the split explicitly — every `mahitiprad_gadya` content gate binds chapter-wide, and from
`samvad_nibandh` only G1 (both speakers reported), G2 (no directive to the child), G4 (quoted speech
never converted to reported speech in the verbatim) and G5 (no guilt) bind, while G7
(argument-not-payload) is recorded as **not** binding because this chapter is deliberately cut by
fact-step. The blue પ્રવેશપેટી's own label — `આ સંવાદ પ્રકારનો એકમ છે.` — is quoted inside
`genre_signals.purpose` **as evidence, never as the verdict**, and that sentence appears in no
child-facing field of the plan.

The explanation unit declared in `01_meta.json` and the unit A2 actually cut on are the same string
(`એક માહિતી-ખંડ`); A4 re-checked it and all eight topics are fact-clusters — none is a speaker turn,
a paragraph or a page. Twenty-five quoted turns against eight topics: every topic spans two or more
turns, so no boundary is a bare change of speaker. Apparatus stayed apparatus: the શીર્ષક-પટ્ટી and
QR badge, the લેખક-સ્લોટ (`- સંકલિત`), the teacher-addressed પ્રવેશપેટી, the printed શબ્દાર્થ box,
the રૂઢિપ્રયોગ and કહેવતો bullet lists, the two printed pictures and the chapter-final yellow
`ગુજરાતી શબ્દકોશ ક્રમ` box carry **no topic** — all seven are itemised in `05_with_content.json`'s
`not_cut_as_topics`. No verse units arise (`[[કડી]]` / `[[દુહો]]` / `[[પદ]]` / `[[ટેક]]` all measure
zero in `00_chapter_normalized.md` and in `01_meta.json`'s `structure_inventory`), so the
દુહો-not-merged, પદ-not-split and changed-words-ટેક rules are satisfied vacuously, not waived.
`guiding_question` is derived from this chapter's own printed chain and reading T1→T8 in order
answers it.

**B — verbatim and structure.** All eight `original_chunk`s are non-empty and Gujarati script only
(U+0A80–0AFF). A programmatic scan of every string in the merged plan finds **no Roman letter and no
Devanagari character** in any authored or verbatim field, and **no `।`** anywhere — the printed `.`
is the stop throughout. The chapter prints no whitelisted non-Gujarati content, so no false-positive
case arises here; `01_meta.json`'s `extraction_notes` record the two glyphs that could have produced
one (`મેં` mis-read as Devanagari `में` at low dpi, and `ડ્રેગનફ્રુટ`), both re-read at 600 dpi and
confirmed Gujarati. Printed licence and printed inconsistency are intact and uncorrected: the mixed
spacing before `?` and `!` (`કોણ ?`, `હાસ્તો !`, `અદ્ભુત !` beside `વાહ!`, `આવે છે?`), the extra
space inside `'' શી વાત છે !`, the transitive/intransitive pair `ઊછેરી`/`ઊછરી` left unlevelled, and
`પશાભાઈ` as પુરુષોત્તમભાઈ's second name of address — kept as printed and, importantly, **never
treated downstream as a second character** (it survives only inside the two verbatim chunks).

Marker arithmetic: `[[સંવાદ: …]]` = **8** in `00_chapter_normalized.md` and exactly 8 marker strings
are carried, one per topic. `[[સ્વાધ્યાય: …]]` = **16** = `exercise_inventory` length, and **no
સ્વાધ્યાય block became a topic** — every topic's source marker is a `[[સંવાદ]]`. Ids run
consecutively by traversal (M1–M2, S1–S4, T1–T8) and the concept counter is chapter-continuous
**C1…C11** with no restart inside a topic.

**C — the teaching block.** All eight topics carry non-empty `explanation` and `real_life_example`.
Measured, with no band widened: explanations **71 74 73 70 65 64 74 66** words and examples
**70 69 65 69 65 66 70 65** words (band 55–90); the eight `objective_text` run **18–24** words
(band 12–30). Glossing is at point of first use and L2-calibrated — `સિકલ`, `શ્રેય`, `દરકાર`,
`સંકલ્પ`, `ઘેઘૂર`, `વનરાજી`, `મબલખ`, `પ્રોત્સાહન`, `યજ્ઞકાર્ય`, `ઉપવન` are opened in Gujarati inside
the sentence that needs them — and the three corrections A7 asked for land where they matter: that
`સંસ્કાર` here is a boy's name and not a quality (T1's first sentence), that વાવવું and ઉછેરવું are
two different jobs (T2's first sentence), and that `લોઢાના ચણા ચાવવા` is an idiom for a very hard
task (T5). One anchor per topic, all Indian, all inside std-6 reach, one domain each and no domain
twice in a row: વેકેશન પછીનું નિશાળનું મેદાન · ભરવાડકાકાનું ધણ · શેરી ક્રિકેટ · ઉત્તરાયણનું ધાબું ·
ઘરે પહેલી રોટલી · બસ-સ્ટૅન્ડનું પાટિયું · મહોલ્લાની તહેવાર-તૈયારી · સાંજનો દરિયાકિનારો. Craft is
**noticed, never named**: `આ લીલાંછમ ઝાડ પણ જાણે બોલે છે` and `શાળા તો ઉપવન જેવી લાગે છે` both stand
in the verbatim, and no field anywhere says સજીવારોપણ, ઉપમા, અલંકાર, રૂપક or છંદ — the std-6 ceiling
holds.

**D — સ્વરૂપ essence.** All **26** `severity: "hard"` items in `07_pitfalls.json` were checked field
by field and hold, and `08_sensitivity.json`'s single item (soft, ધર્મ, M2.S3.T6) is applied as
written. The load-bearing ones:

- **No બોધ, no ઉપદેશ.** No explanation, summary, detailed_summary, concept_bullet or recall answer
  closes on `આપણે પણ … જોઈએ` / `આ પાઠ આપણને શીખવે છે`. The two કહેવત stay inside their printed
  attribution (`સંસ્કારની પાસે તો એક જ વાત હતી`), સવજીભાઈ's `આપણી તો ફરજ થાય ને ?` stays his line and
  is reported as `ગામલોકોની તો ફરજ થાય`, and the resolution topic still ends on the chapter's own
  પુરુષોત્તમભાઈ/સવજીભાઈ exchange. The imperatives printed in the સુલેખન exercise
  (`વૃક્ષો વાવો ને ચોફેર સફાઈ રાખો.`) appear in **no** teaching field.
- **No added facts.** The village, the district and the `પરદેશ` country are never named on the page
  and are named nowhere in the plan; no community is named. The seven people who are named but never
  speak — સંસ્કાર, શિવરામકાકા, સરતાનકાકા, સુશીલાબેન, નારાયણભાઈ, શ્રવણભાઈ, ભૂરાભાઈ — get no line, no
  motive and no scene: they appear only doing what સવજીભાઈ reports they did. No વનસ્પતિ is listed for
  the ઔષધબાગ and no શાકભાજી for the કિચનગાર્ડન — filling those in would also have stolen the printed
  વાતચીત question.
- **Numbers.** Every count is the chapter's own, in the printed Gujarati words (`અઢી દાયકા`,
  `પચીસેક વર્ષ`, `છઠ્ઠા ધોરણ`, `એકસો દસ`, `સાડત્રીસ`); a scan of all display text finds **zero**
  numerals, and no subtraction, percentage, average, year or planting date was derived.
- **The reported claim stays reported.** સવજીભાઈ's `પરીક્ષામાં ઝળહળતી સફળતા` appears only in
  `detailed_summary` and one concept paragraph, each time attributed (`સવજીભાઈ ઉમેરે છે કે…`, and
  explicitly `આ સવજીભાઈના પોતાના શબ્દો છે`). It is absent from every `explanation`,
  `real_life_example`, `concept_bullets` line and every recall answer. નક્ષત્ર-વન is taught as a real
  `સરકારની યોજના` rooted in a traditional practice — neither an astrology lesson nor a debunking —
  which is exactly `08_sensitivity.json`'s guidance.
- **Both voices.** T1 and T6, the two topics where A7 made the two-voice gate explicit, name both
  પુરુષોત્તમભાઈ and સવજીભાઈ in their `explanation` and report what each says; `અદ્ભુત !` stays
  attributed to પુરુષોત્તમભાઈ. No unattributed turn is given a speaker anywhere — the twelve turns the
  book leaves open stay open, which is what makes exercise block 6 answerable.
- **No invented device.** The chapter is ગદ્ય: `figures_of_speech` is `[]` on all eight topics and
  `rhyme_scheme` is `null` on all eight, with `overall_rhyme_scheme: null` on both modules. There is
  therefore nothing to quote-check, and nothing was named that is not in the lines.
- **Exercise material never entered teaching prose.** The deliberately-wrong ર/ળ forms printed in
  block 13 (`મરવા`, `સીતાફર`, `દાર`, `ભેરા`, `મોકરાશ` …) and the strike-out pairs of block 2 appear
  in no teaching field. `આશ્રમ` — which is printed only in the સ્વાધ્યાય, never in the reading text —
  likewise appears nowhere in the plan.

**Contract (the 12 invariants).** All hold, checked mechanically on `13_merged.json`:
`phase: 2`; `plan_id` = `gseb_eng_gujarati6_ch6_v1` = `{chapter_id}_v{version}`; eight non-empty
Gujarati `original_chunk`s; eleven concepts, each with a valid id, a registry `objective_id` and
non-empty `content[]`; eight unique objectives whose `home_topic_id` and every `anchor` resolve;
`strand_to_objective_map` covers all eight `legacy_id`s (L1–L8 → O1–O8); every inline
`learning_objectives[]` entry matches its root registry entry **character for character** (plus the
`image_examples: []` the server adds); media ids are concept-scoped and match `MEDIA_ID_RE`; topic
recalls are `RQ{n}` with `legacy_id` `TR{n}` and **no `.SR{n}` string exists anywhere in the file**;
`publication_id` is non-null; `topic_type` carries the authored enum (`CONCEPT` on all eight) for
Agent 14 to map to the closed server enum; all eight summary triples strictly increase
(`brief_summary` < `summary` < `detailed_summary`); no numbers in display text; `figures_of_speech`
is empty everywhere.

## E–G (reported)

**E — સ્વાધ્યાય and risk.** All **16** inventoried blocks are answered in
`10_exercise_solutions.json` and nowhere else; `coverage_report.blocks_found` = 16 = the inventory
length, `unanswered` is **empty**, and all **77** items carry a real answer (77 = the inventory's own
item total). Thirteen are marked `is_model_answer` — the જૂથકાર્ય, the જોડીકાર્ય, the
નામ-અક્ષર ફકરો, the personal-opinion વાતચીત questions — and fifty carry teaching values filled into
printed grids and blanks. The અનુવાદ block's answers are written in the medium of instruction on
purpose and are marked as such in `teacher_note`; that is not a script failure. Block 6's split is
handled as A1 asked: items 5–7 are near-verbatim from the text, items 1–4 are inference sentences
printed nowhere in the lesson, and the answers say so rather than asserting a speaker.

**F — shape and media.** `chapter_id` is `gseb_eng_gujarati6_ch6` and `plan_id`
`gseb_eng_gujarati6_ch6_v1`, both in the pack's provisional form (VERIFY-1 — see Gaps). Eight reading
scenes, eight `available_content_types: ["image"]`, eight media nodes, one per scene. No `2d_tool` in
the chapter (`null`) — inside the ≤1 ceiling. `reuse_report` reads `scenes: 8 · authored: 8 ·
reused: 0 · rejected: []`, every node carries `image_url: ""` **and** a real self-contained
`generation_prompt` (1400–2000 chars each), and every `negative_prompt` carries
`Devanagari script labels`. No `[reused frame: …]` stamp and no non-empty `image_url` exists in the
pack — as it should not, since no Gujarati frame pool exists yet. Media titles, descriptions and
`teaching_notes` are Gujarati and digit-free; the English inside `generation_prompt` /
`negative_prompt` is model-facing instruction, not child-facing display text.

**G — the seven usual mistakes.** None present. (1) The plan teaches the સ્વરૂપ, not
સાર+બોધ+પ્રશ્નોત્તર. (2)(3) No verse in the chapter, so no દુહા merged and no પદ split. (4) Printed
licence is uncorrected. (5) No અલંકાર named. (6) Every `real_life_example` is Indian, single and at
std-6 pitch. (7) No સ્વાધ્યાય block was cut as a teaching topic and the exercise deliverable is full.

Three small deviations, reported and not blocking:

- `key_terms` is at the top of its 3–6 band (six entries) on all eight topics, so three glosses A7's
  `correction` field asked to be placed there — `સંસ્કાર` (a boy's name), the વાવવું/ઉછેરવું pair,
  and `લોઢાના ચણા ચાવવા` — sit in `explanation`, `concept_bullets` and `vyakaran` instead. The
  misconception each one targets is corrected at point of use; only the field placement differs.
  A12 flagged this itself and asked A5 to look at the three.
- O2's `objective_text` compresses the printed `રોજ વહેલી સવારે અને સાંજે` to `રોજ સવાર-સાંજ`
  (A4's note). Same fact, no invention — and A12's teaching prose carries the printed wording.
- Topic weight is uneven: M1.S1 holds a single topic, M2.S3.T5 holds the chapter's longest single
  paragraph (one speaker turn, eight-plus unfamiliar tree names) and M2.S4.T7 holds only two turns.
  That is the printed page's own shape; evening it out would have split a fact-step.

## Media

`reuse_report`: **scenes 8 · authored 8 · reused 0 · rejected []**. Eight authored scenes, one per
topic, each on the topic's own concept — C1, C4, C5, C6, C7, C9, C10, C11 — so no concept carries two
images and no scene is unillustrated. `2d_tool: null` for the whole chapter. **No frames were
rejected because none were offered**: there is no Gujarati frame pool, so reuse is dormant rather
than exhausted. Each `generation_prompt` is self-contained (setting, figures, action, mood, style,
16:9, Indian village setting, narrator bar naming the exact Gujarati string) and none refers to a
previous image or to the chapter by name. The two pictures the book itself prints — the drawn
planting scene on folio 34 and the aerial garden photograph on folio 36 — are page matter and opened
no topic, per A7's chapter-level rule.

## Gaps

- **`textbook_url` is a local path**, `../Textbooks-pdf/std-6/ch-06-sanskare-sarjyu-swarg.pdf`. The
  GSEB readers have no hosted URL. Carried as A11 recorded it; honest gap, not a block.
- **`chapter_master_id` is `null`** and `upload_reference/chapter_master_map.json` has no GSEB row
  for `gseb_eng_gujarati6_ch6` — every row in that file is null pending **VERIFY-2**. It is
  mandatory for upload and must be fetched from the education DB, never derived. Phase 8 cannot
  upload until it lands.
- **`publication_id` is `1` and is PROVISIONAL.** The contract forbids `null`, so a value is written;
  `1` is **CBSE's publication row** and does not transfer to GSEB. It matches what output6/ch01,
  ch03, ch04 and ch05 carry, so the correction is one pass across the pack. Replace with the verified
  GSEB publication row (VERIFY-2) **before** the first upload.
- **`chapter_id` / `plan_id` board and medium segments are provisional until VERIFY-1.** A wrong
  medium segment uploads clean and mis-files the plan — it must be confirmed against the live server,
  never reasoned out.
- **`genre_confidence` is `low`, and the pack's own files disagree about this chapter.**
  `reference/genre_diagnosis.md`'s near-miss table names std-6 ch 6 and routes it to
  varta.md/mahitiprad_gadya.md; `samvad_nibandh.md` is anchored on this very chapter and the printed
  પ્રવેશપેટી calls it `આ સંવાદ પ્રકારનો એકમ`. A1 resolved it to mahitiprad_gadya on the drop-the-frame
  test (remove the two men and the whole fact payload still stands) and loaded both profiles; A4
  measured the consequence and found the eight boundaries also fall between samvad_nibandh's four
  argument moves, so a re-route would move **no** boundary — only the module/segment names and the
  emphasis of the objectives. **Worth one human eye**; it does not block.
- **18 exercise items are reported `unmapped`** and the mapping was not invented to close the report:
  the eight શ-સ / ર-ળ minimal pairs and the six ળ-words of blocks 9 and 12, the two સ્વાધ્યાય-only
  paragraphs of blocks 10 and 13, the નામ-અક્ષર ફકરો of block 14, and block 8's `આ——મ = આશ્રમ` —
  whose heading says `પાઠમાં આપેલા જોડાક્ષરવાળા શબ્દ શોધો` although `આશ્રમ` is printed only in the
  સ્વાધ્યાય. None of these is prepared by a reading scene; the cut did not miss them, the book's own
  pronunciation apparatus is their source. Reported as unmapped, answered in full.
- **A spec discrepancy, resolved in favour of Agent 16's own spec and recorded here.**
  `agents/13_assembly_validation.md` says `publication_chunk` is *byte-identical* to
  `original_chunk`; `agents/16_publication_authoring.md` §`publication_chunk` says it is the
  publication-facing version of the topic's block *as a whole*, with the verbatim `original_chunk`
  standing verbatim **inside** it. A16 built it the second way. The substantive rule both files share
  — the verbatim is never rewritten, reflowed or re-punctuated — was checked programmatically and
  **holds on all eight topics**: each `original_chunk` occurs as an exact substring of its
  `publication_chunk`, paragraph breaks and printed punctuation included. Not treated as a block. One
  of the two spec sentences should be corrected so the next chapter does not re-litigate it.
- **No PNG render was opened by this agent.** The gate was run entirely against
  `00_chapter_normalized.md`, `01_meta.json` and the ten upstream JSON layers; nothing in the merge or
  the checklist raised a layout or figure question that the transcription could not answer.
- `ordering` is written as `null` — it is Agent 14/15's to set at emit, not this agent's.
- `subject_ref_id`, `medium_id` and `_activate` are `null`/`false` by contract; the server owns them.
  `english_plan_id` and `english_chapter_id` are `null` — a Gujarati chapter has no English twin and
  none was invented to fill them.

## LP2 validator

Not yet run — Phase 8. `POST /api/lp2/learning-plans/validate` must return zero `validation_errors`,
and it cannot be attempted until `chapter_master_id` and the real GSEB `publication_id` land
(VERIFY-2) and the board/medium segments are confirmed (VERIFY-1).

---

**Verdict: A–D PASS.** `13_merged.json` carries 32 root keys, 2 modules, 4 segments, 8 topics,
11 concepts, 8 objectives, 8 media nodes and 24 recall questions, with only contract keys — the
working fields (`markers`, `source_lines_00_normalized`, media `topic_id`, pitfall notes, reuse
scores, validation flags, transcription notes) were dropped at the merge. This unit ships two
deliverables: the plan and `10_exercise_solutions.json`.

## LP2 validator

- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json
- HTTP status: 200
- plan_id: gseb_eng_gujarati6_ch6_v1
- validation_errors: [] (none)
- message: "Valid"
- Result: PASS

## LP2 validator

- POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate → validation_errors: [] (none) — PASS
- Run: 2026-08-23 17:16 IST (validation only; no upload)
