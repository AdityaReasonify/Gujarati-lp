# Validation Report — std 8, ch 10, હલેસે હલેસે

સ્વરૂપ: ગઝલ (confidence: high)   explanation unit: એક શેર
Topics: 12   Objectives: 12   Images: 0/12   Exercises: 44/44 (18 correctly left unmapped, 0 unanswered)

## A–D (blocking)   PASS

- **A — Diagnosis and lens.** genre_signals carries all four signals (structure, theme, exercises,
  purpose), each read off `00_chapter_normalized.md`; the intro-box line `"આ એક ગઝલ છે"` is quoted as
  evidence, not as the verdict. explanation_unit `એક શેર` matches the ગઝલ roster row exactly; 12
  topics = 12 શેર = 12 `[[શેર …]]` markers, one-to-one. No ટેક in this chapter
  (`tek_occurrences: 0`), consistent with ગઝલ carrying none. Not a mixed chapter. Apparatus
  (પ્રવેશપેટી, શબ્દાર્થ, all 12 સ્વાધ્યાય blocks, ચર્ચા-વિચારણા) correctly excluded from the topic
  cut — verified against `05_with_content.json`'s `markers_deliberately_not_cut_as_topics`.
  `guiding_question` is chapter-specific (not copied from `gazal.md`'s own example question) and is
  answered by reading the 12 topics in order (the poem's shifting pictures of the sea, closing on
  why it is never caught).

- **B — Verbatim and structure.** All 12 `original_chunk` fields are non-empty Gujarati script
  (U+0A80–0AFF), no Roman characters, no stray Devanagari, no `।` introduced. Poetic licence
  preserved verbatim: `કદીયે` (not corrected to `ક્યારેય`), the third શેર's printed `અફળાય` kept
  exactly as printed even though the exercise block quotes the same line with `અથડાય` (flagged,
  correctly not harmonised). The તખલ્લુસ `'આદિલ'` stays inside the મક્તા's verse; the printed byline
  `- આદિલ મન્સૂરી` is appended as the attribution line inside the **last** topic's `original_chunk`
  only, per `gazal.md`'s named resolution for this exact chapter. The tenth શેર's single printed
  line is preserved unreflowed. 12 `[[શેર …]]` markers = 12 topics; 0 `[[સ્વાધ્યાય: …]]` blocks
  became topics. Ids run chapter-continuous and consecutive (M1–M3 / S1–S6 / T1–T12 / C1–C12).

- **C — Teaching block.** Every topic has non-empty `explanation` and `real_life_example`.
  Word-count bands (measured programmatically): `explanation` 58–72 words, `real_life_example`
  57–69 words — both inside 55–90 throughout; `objective_text` 15–29 words — inside 12–30
  throughout. `real_life_example` anchors are single, Indian, and inside std-8's reach (well-rope,
  dairy-can collection, kite-flying, temple bell, boiling milk, ST-bus mirage, mango-tree roots,
  classroom-monitor blame, a street dog in the shade, moonlit Kutch salt desert, monsoon puddle) —
  no adult scene, no scene outside India, no std-10-pitched abstraction. Craft ceiling honoured:
  `પ્રાસ` is named and glossed in the same sentence at its first use (M1.S1.T1, matching this
  chapter's own exercise wording `પ્રાસવાળા શબ્દો`); no `અલંકાર`/`છંદ`/`સમાસ` label anywhere
  (std-8 ceiling); `figures_of_speech: []` throughout, correctly.

- **D — સ્વરૂપ essence.** `gazal.md`'s avoid list checked item by item and not violated: no merged or
  split શેર (structural, already true at Agent 4); no running-story language across શેર anywhere in
  `explanation`/summaries/bullets/recall answers — scanned programmatically for ordinal + શેર/પંક્તિ
  cross-references and for the standard preview/link phrases, zero hits (the one apparent hit,
  `પહેલાં` in M1.S2.T2, is the shરત-connective "first a condition, then a result," not a
  cross-શેર reference); every topic's `explanation` names the return (`દરિયો`, verbatim, checked
  programmatically for all 12); mood-vocabulary list (સાકી, જામ, પ્યાલો, …) checked against the
  whole authored file — the one substring hit (`જામ` inside `એકબીજામાં`) is a false positive, not
  the word; no invented ટેક; no form-part named as an અલંકાર; તખલ્લુસ stays inside the verse;
  none of the three exercise-embedded poems (રજની મહેતા, સુન્દરમ્, સુરેશ દલાલ) leaked into any
  `original_chunk`, `figures_of_speech`, or explanation; poet not modernised. The one whole-poem
  recall question lives only at M3.S6.T12.RQ3, matching `gazal.md`'s own prescribed wording and
  recall-priors placement, and does not assert the મક્તા as the poem's "conclusion" — it explicitly
  restates that every શેર stays independent.

  **Judgement call reviewed and confirmed sound:** Agent 12 kept `શેર`/`રદીફ`/`કાફિયા`/`મત્લા`/`મક્તા`
  out of all child-facing fields (using `પંક્તિ-જોડ` instead), naming only `પ્રાસ` and — once,
  glossed — `તખલ્લુસ`. This satisfies every hard `avoid_check` in `07_pitfalls.json` (which
  conditions on *if* `શેર`/`પ્રાસ` is used, not that it must be) and matches `gazal.md`'s own
  std-band box (std 6–9 print only `પ્રાસ`; std 10 alone prints `શેર`/`રદીફ`/`કાફિયા` outright). No
  action needed; flagged here only for continuity with the upstream note.

## Contract (12 json_contract.md invariants — hard)   PASS

Checked programmatically against `13_merged.json`: `phase:2`, `chapter_id`/`plan_id` format;
every `original_chunk` Gujarati-only and non-empty; every topic has exactly one concept with a
valid `concept_id`, an `objective_id` resolving to the root registry, and non-empty `content[]`;
root `objectives[]` internally consistent (`home_topic_id`, `anchor[]`, `strand_to_objective_map`
all resolve, O1–O12 / L1–L12 one-to-one); inline `learning_objectives[]` mirrors match the root
`objective_text` character-for-character (added at merge — see note below); `MEDIA_ID_RE` holds for
all 12 concept-scoped `IMG1` ids; `RQ{n}`/`TR{n}` ids well-formed for all 36 recall questions, no
`.SR{n}` anywhere; 0 સ્વાધ્યાય topics and all 44 exercise items answered; three-tier summaries
strictly increase by word count for all 12 topics; no digit found in any display field (topic
names, explanations, examples, summaries, bullets, recall prompts/answers — scanned
programmatically); `figures_of_speech` is `[]` everywhere, trivially verbatim-safe;
`chapter_master_id`/`subject_ref_id`/`medium_id` correctly left `null` pending VERIFY-1/2 (never
invented).

**Merge note:** `learning_objectives[]` did not exist in any upstream layer (05/12), so it was
constructed at this step — a mechanical copy of each topic's root objective object plus
`image_examples: []`, with zero invented content, matching the shape the contract and sibling
chapters (`output8/ch01`–`ch09`, `ch13`–`ch14`) already carry.

## Publication check   PASS (verified against sibling precedent)

`publication_chunk` is **not** literally byte-identical to `original_chunk` for any topic — it is
`original_chunk` (unaltered, confirmed as an exact-prefix substring in all 12 topics) followed by
the topic's `publication_text` and a real-life anchor paragraph. This matches the established,
already-passed shape used across every other std-8 chapter in this pack (`ch01`–`ch09`, `ch13`,
`ch14`, spot-checked against `ch01`), so it is read as the intended meaning of "the rewrite never
touches verbatim" (the poem-lines substring is never reflowed or edited) rather than a literal
whole-field equality. `concept_publication[]` merges into `concepts[].content[]` by
`content_index` — only the `paragraph`-type content item receives a `publication_text`; the
`list`-type item does not, again matching the `ch01` precedent exactly. No vocative or classroom
instruction (`બાળકો`, `જુઓ —`, `બોલો`) survived into any `publication_text`/`publication_chunk`
(checked programmatically — the explanation fields' own `બાળકો, જુઓ —` opener is correctly stripped
in every rewrite). No meaning added beyond what `explanation`/`real_life_example` already state.

## E–G (reported)

- **Exercises.** All 12 inventoried સ્વાધ્યાય blocks (44 individually-numbered items) are answered
  in `10_exercise_solutions.json`; 0 unanswered. 18/44 items are reported unmapped to any topic for
  stated, genuine reasons (5 quote a different poet's lines printed only inside the exercise block;
  5 are general oral prompts with no echo in this ગઝલ's own imagery; 5 are standalone word-play/
  story/translation apparatus; the last-numbered item is std-8's standing L1-translation block,
  correctly answered in English and marked as such in `teacher_note` — a whitelisted, non-Gujarati
  exception per `qc_checklist.md`'s own script-check carve-out). No mapping was invented to close
  the report. Personal-opinion, પ્રવૃત્તિ (drawing, story-completion, reading another poem) and
  group-discussion items are answered with concrete teaching values and marked `is_model_answer`.
- **Sensitivity.** One soft item (`08_sensitivity.json`): M3.S5.T9's `ડૂબનારા` line, area સુરક્ષા.
  Addressed — the explanation stays on the people's-accusation reading rather than lingering on
  drowning, and the `real_life_example` was built as a classroom-blame scene with no water/swimming
  content at all (stricter than the guidance's own minimum ask).
- **Craft/std-band.** No craft term above the std-8 ceiling appears anywhere; see the D-section
  judgement-call note above.
- **Module/segment naming.** Grouped by shared imagery-type (human effort & the sea's reply / the
  sea's changing forms & reach / hiding, merging, elusiveness), not by narrative sequence — checked,
  no module or segment name reads as "first X, then Y."

## Media

`reuse_report`: `scenes: 12`, `authored: 12`, `reused: 0`, `rejected: []` — matches the 12 topics
whose `available_content_types` carry `"image"` exactly. Every scene carries `image_url: ""` and a
real, self-contained `generation_prompt` (no fabricated URL, no `[reused frame: …]` stamp anywhere —
correct, since no Gujarati frame pool exists). `negative_prompt` carries `Devanagari script labels`
on all 12. `2d_tool: null` chapter-wide (≤1 satisfied trivially). Media priors honoured: one
concrete, distinct image per શેર (net-and-sea, drop-and-khobo, ship-and-rock, cave-and-shell,
river-mouth, monsoon-rain, Rann-of-Kutch, foam-and-depth, storm-and-blame [no one shown in the
water, per the sensitivity note], receding-tide, horizon-merge, casting-net-at-dusk); no
whole-poem frame; no frame continuing a previous frame or a recurring character; no caption
repeating just `દરિયો`.

## Gaps

- `textbook` root field left `null` — this run's std-8 cover was not read (`01_meta.json` and
  `11_pages.json` both record this explicitly); carried through rather than guessed. (Note for the
  harness: sibling `output8/ch01`'s `11_pages.json` filled this field from a board-profile
  convention despite the identical "cover not read" caveat — an inconsistency across this pack's
  own std-8 chapters, surfaced here rather than resolved by copying either choice into this file.)
- `textbook_url` is a local PDF path (no hosted URL exists yet).
- `textbook_pages`: `"81-84"`, confidence `medium` (folio read off two page renders and
  cross-checked against the manifest; the reader's own front-matter index was not consulted).
- `chapter_master_id`, `subject_ref_id`, `medium_id`: `null`, pending VERIFY-2/VERIFY-1 against the
  live education DB — never invented, per policy.
- `publication_id`: written as `1`, matching the CBSE-derived placeholder value every other std-8
  chapter in this pack already carries (`ch01`–`ch09`, `ch13`, `ch14`) — itself explicitly
  provisional per `phase2_contract.md` ("CBSE's 1 does not transfer") and awaiting the real GSEB
  publication row from VERIFY-2 before upload.
- Exercise item 3.5 quotes the third શેર with `અથડાય` where the poem itself prints `અફળાય` — a
  page-level wording mismatch, transcribed exactly as printed in both locations, not harmonised
  (already recorded in `01_meta.json`'s `extraction_notes`).
- No page render was opened during this validation pass; `00_chapter_normalized.md` plus the
  upstream JSON layers answered every question raised.

## LP2 validator

Not run — filled in at Phase 8.

## LP2 validator

Validation endpoint: https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
Status: SUCCESS
Response:
```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati8_ch10_v1",
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
Validation Errors: NONE
Result: PASSED
