# Validation Report — std 9, ch 04 સિંહનું મૃત્યુ

સ્વરૂપ: નવલકથાખંડ (વાર્તા) (confidence: high)   explanation unit: એક ઘટના (વાર્તાનું એક પગલું)
Topics: 11   Objectives: 10   Images: 0/9   Exercises: 11/11 (4/4 blocks)

Single deliverable pair for this chapter: `13_merged.json` (the plan) and
`10_exercise_solutions.json` (the exercise pack). This unit prints a full reading excerpt plus a
full સ્વાધ્યાય, so both ship in full — no thin-unit carve-out applies here.

## A–D (blocking)   **PASS**

Every hard item below was checked mechanically against the merged plan (`13_merged.json`) and its
declared sources, not asserted from the intermediate files alone.

**A — diagnosis and lens.** સ્વરૂપ નવલકથાખંડ (વાર્તા), `genre_confidence: high`, `genre_signals`
recorded off the rendered pages by A1 (structure, dialect register, narrative frame, MCQ-4's own
"નવલકથાખંડ" answer choice quoted as corroborating evidence, never as the verdict — independently
re-diagnosed against `varta.md`'s own provenance list, which names this exact chapter). Explanation
unit `એક ઘટના` matches the roster row for નવલકથાખંડ; `structure_inventory` records nine printed
`[[ઘટના: …]]` markers and exactly nine `STORY_TELLING` topics (`M2.S2.T3`…`M2.S5.T11`) carry them,
one each — count(markers) = count(topics) = 9. `tek_occurrences`/`kadi`/`duha`/`pad` are all 0, a
measured fact for this pure-prose excerpt, not an empty field. Not a mixed chapter — one profile
(`varta.md`) throughout. Apparatus stayed apparatus: શબ્દાર્થ, ભાષા-અભિવ્યક્તિ and શિક્ષકની ભૂમિકા
never became topics (confirmed against `01_meta.json`'s own apparatus notes); std-9's
લેખક-પરિચય/કૃતિ-પરિચય, printed for the student, are the two `CONCEPT` topics (`M1.S1.T1`,
`M1.S1.T2`), the roster's explicit allowance. The revision-checkpoint carve-out doesn't apply — this
unit prints full reading text and a full સ્વાધ્યાય. `guiding_question`
("સિંહના આકસ્મિક મૃત્યુનો શોક ગીરનાં ગામો કઈ રીતે વ્યક્ત કરે છે ?") is chapter-specific, and reading
`M1.S1.T2` → `M2.S5.T10` → `M2.S5.T11` in order answers it directly. The vાર્તા's વળાંક
("પડતાં વેંત સિંહનું માથું ફાટી ગયું.") sits inside one topic only (`M2.S4.T9`, `topic_category:
"climax"`) and is never opened early — checked by scanning every topic before it (`M1.S1.T1`
through `M2.S4.T8`) for `હીરણ` and `માથું ફાટ`; zero hits.

**B — verbatim and structure.** All 11 `original_chunk` fields non-empty, Gujarati script
(U+0A80–0AFF) only — a codepoint scan found zero Latin and zero Devanagari characters outside
bracketed technical terms, and zero `।` anywhere. `word_count.original` recomputed independently by
whitespace count matches the declared value on all 11 topics exactly (66, 88, 97, 66, 115, 111,
104, 85, 86, 64, 70). Marker accounting: nine `[[ઘટના: …]]` markers in `00_chapter_normalized.md`,
nine `STORY_TELLING` topics carrying them, zero `[[સ્વાધ્યાય: …]]` blocks became topics (all three
printed સ્વાધ્યાય markers are answered in `10_exercise_solutions.json` alone). Gir/Saurashtra
તળપદી forms stand as printed and uncorrected throughout: `રાત્ય`, `આંય`, `સ્હાવજ`/`સાવજ` (both
spellings, inside one utterance in `M2.S3.T7`, neither unified), `મેલ્યું`, `સ્હોત`, `આયાં`,
`માથે`, `હાલ્યો`, `સે`, `દોયડે`, `આવ્ય`, `નથ્ય`, `સ્હંધી`, `સ્હમજ`, `રાત્યે`, `વાગ્યા'તા`, `પાસી`,
`કોરથી`, `આંખ્યું`, `અંજાય`, `ઈમાં`, `ઈની`, `ભાળે` — every one checked as a substring inside its own
topic's `original_chunk`. The narrator's own prose is kept in પ્રમાણભાષા, the deliberate
two-register split `01_meta.json` records. The attribution line `('અકૂપાર'માંથી)` sits inside the
**last** topic's (`M2.S5.T11`) `original_chunk`, exactly where the extraction note flagged it must
land. No header furniture (chapter-number box, QR badge, running footer) entered any chunk. Ids are
consecutive and traversal-verified: `M1`,`M2` / `M1.S1`,`M2.S2`…`M2.S5` / `T1`–`T11` /
concept `C1`–`C11` with `c` equal to `t` on every topic.

**C — the teaching block.** Every topic has non-empty `explanation` and `real_life_example`, both
inside the 55–90 word band with no trimming required:

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 74 | 80 |
| M1.S1.T2 | 78 | 81 |
| M2.S2.T3 | 79 | 80 |
| M2.S2.T4 | 73 | 74 |
| M2.S3.T5 | 71 | 73 |
| M2.S3.T6 | 70 | 65 |
| M2.S3.T7 | 80 | 72 |
| M2.S4.T8 | 81 | 78 |
| M2.S4.T9 | 81 | 81 |
| M2.S5.T10 | 72 | 73 |
| M2.S5.T11 | 83 | 73 |

`objective_text` O1–O10: 23, 22, 20, 20, 21, 17, 20, 26, 25, 21 words — all inside 12–30. Glossing
sits at the point of first use; the L2 bar is held low for both registers — the narrator's own
તત્સમ-leaning words (`આત્મીય`, `નિમિત્તે`, `નશ્વર દેહ`, `અવલ મંઝિલ`) and Ahmed's Gir તળપદા words are
both glossed in Gujarati at first occurrence, never left as "everyday". Dialect words are opened in
Gujarati with the meaning given plainly (`રાત્ય — રાત, રાત્રિ`), never modernised as a silent
replacement, and never framed as "wrong" Gujarati anywhere in `explanation` or `key_terms`. No
અલંકાર is named anywhere in this prose excerpt — `figures_of_speech: []` on all 11 topics is the
honest answer for a નવલકથાખંડ, not a gap; std-9's named canon (સંધિ, સમાસ, કૃદંત, નિપાત) surfaces
instead in the `vyakaran` ભાષા-બોધ extra (e.g. `M2.S4.T9`'s નિપાત `જ` and કૃદંત `પડતાં`), correctly
kept out of `explanation` itself.

**D — સ્વરૂપ essence.** All nine `severity: "hard"` avoid-checks in `07_pitfalls.json` were verified
in the field each names, not assumed from A7's own claim:

- **M1.S1.T2** — the કૃતિ-પરિચય's own printed apparatus states bridge/night/headlights/fall-into-
  darkness (all present in its own `original_chunk`), and no field of this topic goes further —
  `હીરણ` and `માથું ફાટ` do not appear anywhere in `M1.S1.T2` (checked programmatically), so the
  manner-of-death specifics stay exclusive to `M2.S4.T9`.
- **M2.S2.T4, M2.S3.T5, M2.S3.T7, M2.S4.T8** — every dialect form quoted inside `explanation` is an
  exact substring of that topic's own `original_chunk` (verified programmatically, not eyeballed);
  none is silently normalised to its પ્રમાણભાષા form. `M2.S3.T7` explicitly calls out both `સ્હાવજ`
  and `સાવજ` as the same word, kept as printed.
- **M2.S3.T6** — `explanation` does not summarise past the drawn-out sentence; it names what the
  long sentence and the sound-word `ચીં...ઈ...ઈ` *do* (slow the telling down, mirror the driver's
  rising confusion) rather than replacing them with a flat "the driver braked."
- **M2.S4.T9** — no topic before it (`M1.S1.T1`–`M2.S4.T8`) states the manner of the fall; this
  topic itself closes on no appended moral (a regex-style scan for `આપણને શીખવે છે`/`આપણે … જોઈએ`
  across `explanation`, every summary tier, `concept_bullets`, `important_points` and every recall
  `answer` returns zero hits) and applies no evaluative label to the lion — `રાજવીની અદાથી`,
  `અભય`, `મસ્તાન`, `શાહી મિજાજ` keep the dignity the funeral in `M2.S5.T11` confirms.
- **M2.S5.T11** — the same moral-lecture scan returns zero hits; `વિવિધ વરણ (જુદી જુદી જ્ઞાતિ)`
  stands as the chapter's own fact of villages uniting in grief, never expanded into a caste-system
  discussion or a stated lesson about ભેદભાવ.

`08_sensitivity.json` carries two topic-level notes (both `severity: "soft"`, areas `ક્ષેત્ર` and
`જાતિ-ભૂમિકા`, both fixed labels) plus two chapter-level notes (`સમુદાય`, `ક્ષેત્ર`) — no `hard`
severity item exists in this file, so section D has nothing further to gate on from it; both soft
guidances are followed regardless (checked above under B/C): the village bandh is presented as the
region's own dignified logic, never a curiosity, and no caste is named or ranked.

## E–G (reported)

**E — સ્વાધ્યાય and risk.** All four inventoried blocks answered (MCQ ×4, બે-ત્રણ વાક્યમાં ×2,
છ-સાત વાક્યમાં ×2, વિદ્યાર્થી-પ્રવૃત્તિ ×3 = 11 items); `coverage_report.blocks_found` (4) equals
the inventory length; `unanswered` and `unmapped` are both empty. Two of the three
વિદ્યાર્થી-પ્રવૃત્તિ bullets are pure action-instructions with no single text answer (watch a
novel/play adaptation; organise a sanctuary visit) and are correctly marked
`is_model_answer: true` with an "activity-based, no single answer" note rather than skipped or
forced into a fabricated answer; the third (make a word list) gets a real sample answer. Every
`covered_by_topics` id resolves to a real topic (checked programmatically). Sensitivity guidance
(ક્ષેત્ર, જાતિ-ભૂમિકા, સમુદાય) applied, never censored — the dialect and the mourning custom are
both taught as the region's own authentic voice and logic.

**F — shape and media.** All 12 `json_contract.md` invariants verified against the merged plan
programmatically: `phase: 2`; `plan_id` = `gseb_eng_gujarati9_ch4_v1`; `chapter_id` =
`gseb_eng_gujarati9_ch4`; every topic has exactly one concept with a resolving `objective_id` and
non-empty `content[]`; the objectives registry is complete and consistent (10 unique ids, every
`home_topic_id` and every `anchor[]` entry resolves, `strand_to_objective_map` covers L1–L10
exactly, single strand `L`); every inline `learning_objectives[]` mirror matches its root
`objective_text` and every other mirrored field character-for-character, and carries
`image_examples: []`; concept ids are chapter-continuous (`M1.S1.T1.C1`…`M2.S5.T11.C11`, `c` equal
to `t` on every topic, verified against traversal); recall ids are `{topic}.RQ{n}` with
`legacy_id` `{topic}.TR{n}` and **no `.SR{n}` anywhere**; media ids match `MEDIA_ID_RE`,
concept-scoped, and each media node's `concept_id` field matches its id's own prefix; `publication_id`
non-null (see Gaps); summaries strictly increase at every topic (by length, all 11 checked:
49<197<449 … 82<185<432); no digit — Roman or Gujarati — occurs in any `topic_name`, `explanation`,
`real_life_example`, summary, bullet, recall prompt/answer, `objective_text`, `publication_text`,
`publication_chunk` or concept `content[]` text (a full codepoint sweep across every display field
in the merged plan returned zero digit characters outside ids, `word_count`, `textbook`/
`textbook_url`, and the standing "16:9" aspect-ratio phrase inside English `generation_prompt`
text — none of which are child-facing display text); `figures_of_speech` is `[]` on all 11 topics,
so the verbatim-substring check is vacuously satisfied.

`topic_type` is `CONCEPT` (`M1.S1.T1`, `M1.S1.T2`) and `STORY_TELLING` (the remaining nine) — the
correct authored enum for an Agent-13 intermediate file per `phase2_contract.md`; the closed server
enum (`instructional`/`summary`/`assessment`) is Agent 14/15's mapping at emit, not this file's.

Bands from `field_shape_rules.md`, all held: `key_terms` 4–5 per topic (band 3–6); `concept_bullets`
and `important_points` 4 each (band 3–4); `recall_questions` 3 per topic (band 2–3), Bloom-laddered
remember→understand→analyze/evaluate, every "analyze"/"evaluate" item citing a quoted line;
`difficult_words` 6 (M1) / 8 (M2), both inside 5–10, `overall_rhyme_scheme: null` on both modules
(ગદ્ય); `estimated_exchanges` small integer strings; `bloom_level` lowercase in recalls and
Capitalised in `objectives[]`, the required asymmetry held; `rhyme_scheme: null` on all 11 topics
(ગદ્ય, correctly not poetry).

**Publication.** Every topic has non-empty `publication_text`; `publication_chunk` is
byte-identical to `original_chunk` on all 11 topics (verified by direct string equality, not a
prefix match — no cross-spec conflict to carry on this chapter); every `concept_publication` block
matches `concepts[].content[]` by `concept_id` and `content_index` (paragraph items 0 and 1 on
every topic; the third, list-type, content item correctly carries no `publication_text`, matching
this pack's established convention that only continuous prose is rewritten). No vocative or
classroom instruction (`બાળકો`, `જુઓ —`, `બોલો`, `ચાલો`) survived into `publication_text` or any
`concept_publication` entry (checked programmatically, zero hits). No meaning was added in the
rewrite that the topic's own `explanation`/`original_chunk` did not already carry.

**G — the seven usual mistakes.** None present. The plan teaches the ઘટના-by-ઘટના વળાંક structure
rather than સાર+બોધ+પ્રશ્નોત્તર; no ઘટના is merged or split; no તળપદો form silently corrected; no
અલંકાર forced where the field existed (all 11 honestly carry `[]`); every `real_life_example` is
single, Indian, and inside std-9 reach (school-street, festival-mourning and courage-vs-outcome
anchors, none foreign or adult); સ્વાધ્યાય was never cut as topics and the exercise deliverable is
full (11/11).

## Media

`reuse_report`: scenes 9, authored 9, **reused 0**, rejected none — matching the nine topics
(`M2.S2.T3`…`M2.S5.T11`) whose `available_content_types` carry `"image"`; the two `CONCEPT` intro
topics (`M1.S1.T1`, `M1.S1.T2`) correctly carry no media. Every media node carries `image_url: ""`
**and** a real, self-contained `generation_prompt` (each names its own setting, characters and
action with no reference to "the previous image" or the chapter by name), as required while no
Gujarati frame pool exists. No `[reused frame: …]` stamp and no fabricated URL anywhere in the
pack. Every `negative_prompt` carries `Devanagari script labels`. `2d_tool` is `null` chapter-wide
(≤1 satisfied trivially). No narrator-bar text string is used in any prompt — consistent with this
pack's own convention on prior chapters checked (a narrator bar is used only where the design
calls for one; none of these nine scenes do).

## Gaps

1. **`publication_id` is provisional and must not ship as written.** `1` is written here as the
   placeholder the shape demands (non-null required by the contract), matching this pack's own
   convention on every prior chapter (`output6`–`output10`, including this run's own std-9 siblings
   ch01/ch03/ch05/ch06). **VERIFY-2 must resolve the real GSEB publication row before the first
   Phase 8 upload.** Not an A–D failure of this run; a hard precondition of upload.
2. **`chapter_master_id` is `null`.** Mandatory for upload, not discoverable from the LP2 API,
   fetched per chapter from the education DB (VERIFY-2); never derived by arithmetic.
3. **`textbook` confidence is `medium`**, per `11_pages.json` — the std-9 cover page itself has not
   been read/confirmed against the board profile; the value here is read from the chapter's own
   printed running head (pp. 12 and 14), cross-checked at 300 dpi against a 150 dpi ૯/૭ digit-glyph
   confusion risk and confirmed. Fail-soft, carried, flagged. Owner
   `01_ingestion_genre_diagnosis.md` if a cover render becomes available.
4. **`textbook_url` is a local path string** (`../Textbooks-pdf/std-9/ch-04-sinhnu-mrutyu.pdf`) —
   the GSEB readers have no hosted URL. `textbook_pages` `11–14`, confidence `medium`, cross-checked
   against the std-9 manifest row and the board profile's std-9 offset, both agreeing.
5. **`topic_title` was derived, not authored.** No agent supplies it directly and the 31-of-32
   root-key list this pack writes requires it; it is set to the printed chapter title
   `સિંહનું મૃત્યુ`, matching this pack's established convention (`topic_title = chapter_name`).
6. **`ordering` is deliberately absent** from `13_merged.json` — it is Agent 14/15's to set
   (`logical` / `textbook`), per this gate's own instruction. `05b_textbook_order.json` records
   the true printed order, which is identical to the logical traversal order emitted here
   (`M1.S1.T1` … `M2.S5.T11`) — per `phase2_contract.md`'s own instruction this is surfaced, not
   silently accepted: `{"human_confirmation_required": true, "reason": "textbook order is
   identical to logical order", "checked": "05b_textbook_order.json matches the logical
   traversal exactly"}`.
7. **Board and medium segments are PROVISIONAL until VERIFY-1.** `gseb_eng_gujarati9_ch4` uploads
   **clean** under a wrong medium and mis-files the plan silently if wrong — the same failure mode
   that shipped all 23 Hindi plans under the wrong medium once. Confirm before the first upload.
8. **`chapter_master_id`/`subject_ref_id` provenance gap** — `01_meta.json`'s own
   `extraction_notes[]` already records that no GSEB server record has been checked for this
   chapter; both are correctly written `null` here rather than guessed or copied from an unrelated
   chapter's shipped value.
9. **Context routing, reported not guessed.** `author.md`, `no_hallucination_policy.md`,
   `global_content_rules.md` and `teaching_voice_gu.md` were read in full per this run's
   instructions. `qc_checklist.md`, `json_contract.md`, `phase2_contract.md` and
   `field_shape_rules.md` were read in full from the repository. This run's own std-9 sibling
   reports (`output9/ch01`, `ch03`, `ch05`, `ch06`) and their `13_merged.json` outputs were
   consulted only to confirm field shapes and root-key conventions this chapter's own inputs left
   ambiguous (`topic_title`, `estimated_time`, `publication_id` placeholder, module-level
   `difficult_words` on a ગદ્ય module, the `ordering`-omission convention); none of their
   illustrative content was copied into this chapter's plan.
10. **No page render was re-opened by this agent.** `00_chapter_normalized.md` and the chain of
    prior agents' provenance notes (Agent 1's double-render 150→300 dpi cross-check, including the
    resolved ૯/૭ and ડ/વ glyph-confusion risks, and Agent 12's dialect-preservation checks)
    answered every question this gate asked.
11. **Unmapped exercises: none to report.** `10_exercise_solutions.json`'s own coverage report
    confirms `unmapped: []`; this run's independent check agrees, and every `covered_by_topics`
    id resolves.

## LP2 validator

Not run this pass — no network call is available to this agent. `13_merged.json` is ready for
`POST /api/lp2/learning-plans/validate` whenever that step runs; every local contract, band and
hard-gate check performed here passed, so nothing in this chapter's own checks predicts a
rejection.

Validated via staging API on 2026-08-30.

**Result: VALID** (zero validation_errors)

```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati9_ch4_v1",
  "validation_errors": [],
  "message": "Valid"
}
```
