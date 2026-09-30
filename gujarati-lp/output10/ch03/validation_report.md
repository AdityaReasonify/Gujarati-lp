# Validation Report — ધોરણ 10, એકમ 3 — પ્રયાણ

સ્વરૂપ: નવલકથાખંડ (`varta.md`, confidence: **high**)   explanation unit: એક ઘટના

Topics: 5 (M1.S1 = 1 · M2.S2 = 1 · M2.S3 = 1 · M2.S4 = 2)   Objectives: 5   Images: 0/4   Exercises: 7/7 items across 4/4 blocks

---

## A–D (blocking)   **FAIL — one narrow, named item (below); everything else holds**

All seven merge layers exist and were folded (`05_with_content.json`, `07_pitfalls.json`,
`08_sensitivity.json`, `09_media.json`, `10_exercise_solutions.json`, `11_pages.json`,
`12_authoring.json`, `16_publication.json`, `01_meta.json`). This is not a missing-layer run like
`output10/ch01`; `13_merged.json` is a complete phase-2 plan and the failure below is the only thing
keeping it from a clean pass.

### The failing item, named

**Section C/voice — Roman script used bare, outside a bracketed technical term, in two shipped
display fields.** `teaching_voice_gu.md`'s voice rule ("Roman script only inside brackets, for a
technical term: `સજીવારોપણ (personification)` … Never a romanised Gujarati word") and the pack's
standing script-purity principle are violated twice — not in `original_chunk` (which is clean, see
below), but in two authored support fields the child reads directly:

| # | Location | Text | Problem |
|---|---|---|---|
| 1 | `M1.S1.T1.concept_bullets[1]` | `"લેખક vs પાત્ર — રમણભાઈ લખનાર છે, ભદ્રંભદ્ર એમની નવલકથાનું પાત્ર છે."` | bare English `vs` standing in for a Gujarati conjunction (`અને` / `વિરુદ્ધ`), not a bracketed technical term |
| 2 | `M2.S3.T3.important_points[3]` | `"'મેદ થયેલોચ' — સોરાબજીની બોલીમાં 'ગાંડો થયેલો છે' એવો અર્થ; અંગ્રેજી 'mad' શબ્દનો પારસી ઉચ્ચાર."` | bare English `mad` in quotes, not a `સંજ્ઞા (English)` bracket shape; also spells out the specific English etymon the chapter's own શબ્દ-સમજૂતી box deliberately leaves unnamed (`"મેદ (મેડ) ગાંડો (અંગ્રેજ શબ્દનો પારસી ઉચ્ચાર)"` — the box says "an English word," not which one) |

**Owner: `agents/12_runtime_authoring.md`** (routing table: "wrong voice"). Both are one-line fixes —
replace `vs` with a Gujarati conjunction, and rephrase the `mad` clause so the English word is either
dropped or wrapped in the standard bracket shape — and neither requires touching any other field,
topic, or the rest of that same field's content. This was found by a full mechanical scan of every
authored display field in `12_authoring.json` and `16_publication.json` (all of `explanation`,
`real_life_example`, three summaries, `concept_bullets`, `important_points`, `recall_questions`,
`concepts[].content[]`, `shabdarth`/`samanarthi`/`vilom`/`vyakaran`, `publication_text`,
`publication_chunk`) for Devanagari, `।`, and Roman characters outside `(...)`; these two are the
**only** hits in the whole file. `explanation` and `real_life_example` — the two fields Section C's
word-count and voice bullets name directly — are completely clean on all five topics.

Per this agent's own Do-not list, the two strings were **not** edited here; `13_merged.json` carries
them exactly as `12_authoring.json` wrote them, and this report names the owner instead. **The run is
not complete** on this basis, however sound everything else below is.

### What WAS checked, and holds

**A — diagnosis and lens (holds).** `genre_signals` (structure/theme/exercises/purpose) and
`genre_confidence: "high"` sit in `01_meta.json`, read off the rendered pages; the સવિસ્તાર exercise's
own line naming "'પ્રયાણ' નવલકથાખંડ" is quoted as evidence, not as the verdict. `explanation_unit`
(એક ઘટના) matches `varta.md`'s નવલકથાખંડ row exactly: the four `[[ઘટના: …]]` markers in
`00_chapter_normalized.md` became four STORY_TELLING topics (`M2.S2.T2`, `M2.S3.T3`, `M2.S4.T4`,
`M2.S4.T5`), none merged or split, and std-10's unlabeled લેખક-પરિચય/કૃતિ-પરિચય pair became one
CONCEPT topic (`M1.S1.T1`) per the std-9/10 apparatus exception. `શબ્દ-સમજૂતી`,
`વિદ્યાર્થી-પ્રવૃત્તિ`, `ભાષા-અભિવ્યક્તિ` and `શિક્ષકની ભૂમિકા` all stayed apparatus — confirmed against
`01_meta.json`'s own `extraction_notes` and against every `topic_name` in the merged file. No
revision checkpoint or વ્યાકરણ એકમ applies. `guiding_question` ("ભદ્રંભદ્રની કઈ ટેવો અને કઈ ભાષા
તેમના પ્રયાણને હાસ્યાસ્પદ બનાવે છે ?") is this chapter's own, and the five topics in order — who
Bhadrambhadra is, his habit of grand comparison, his Sanskrit-vs-Parsi language collision, his
platform bath, the co-passenger's fabricated "shastra" — do answer it.

**B — verbatim and structure (holds, checked programmatically).** All five `original_chunk`s were
diffed, whitespace-collapsed, against `00_chapter_normalized.md` with markers stripped: all five are
found **verbatim and contiguous**. A full character scan of all five `original_chunk`s found **zero**
Devanagari codepoints, **zero** stray Roman characters, **zero** `।`. Poetic/dialectal licence is
intact and unflattened: `સું બકેચ`, `આય`, `મેદ થયેલોચ` (Sorabji's Parsi-accented speech), `સે`, `ઈમ`,
`સોકરાં` (the co-passengers' તળપદી), and `મહોટો`, `તવ`, `યવન` (Bhadrambhadra's own archaic
tatsam-heavy register) all sit unchanged, character for character, inside their `original_chunk`s —
none was corrected toward માનક ગુજરાતી. The attribution line `('ભદ્રંભદ્ર'માંથી)` sits inside the
**last** topic's (`M2.S4.T5`) `original_chunk`, as printed. Ids run consecutively — `M1.S1.T1` →
`M2.S2.T2` → `M2.S3.T3` → `M2.S4.T4` → `M2.S4.T5`, concepts `C1`–`C5` chapter-continuous and equal to
each topic's own number (one concept per topic). The four `[[ઘટના: …]]` markers equal the four
STORY_TELLING topics; no `[[સ્વાધ્યાય: …]]` block became a topic. No header furniture (chapter-number
box, QR badge, running footer) entered any `original_chunk`.

**C — the teaching block.** `explanation` and `real_life_example` are non-empty and clean on all five
topics; word counts measured programmatically: `explanation` 71/70/72/81/86, `real_life_example`
72/65/66/62/73 — all inside 55–90. `objective_text` measured 19/27/24/28/28 words — all inside
12–30, no band widened. L2 calibration holds: hard words are glossed at first use in Gujarati
(`જુનવાણી`, `અકથ્ય`, `કોપ`, `ચોકો`, `રઘવાયા`…), Sorabji's and the co-passengers' dialect lines are
named as printed dialect ("ભૂલ નથી") rather than corrected or mocked, and no Hindi word stands in for
a Gujarati one anywhere. Every `real_life_example` is a single, concrete, Gujarat-based anchor
(દાદીની વાર્તા, શેરી ક્રિકેટ, બસ-સ્ટૅન્ડ, કાળું ટીકું/દોરો, બિલાડી-આડી-ઊતરવાની માન્યતા) inside std-10's
reach, and four of five end on a question to the child. Craft is named only in ordinary words — no
અલંકાર or છંદ term is used anywhere, correctly, since `07_pitfalls.json`'s own chapter-level note
records that this chapter's rendered apparatus names no specific device to anchor one to; `[]` on
`figures_of_speech` is the correct answer, not an omission. **The one open item is the voice defect
named above**, which sits in `concept_bullets`/`important_points`, not in the word-count/voice-band
fields this section otherwise measures.

**D — સ્વરૂપ essence (holds).** Checked against `varta.md`'s Avoid list directly: no field anywhere
narrates past the excerpt's own end (`'...ઘણાએ અજમાવી જોયેલું છે.'`) — no field states how
Bhadrambhadra responded, whether the naming-debate was settled, or what happened at Mumbai (Avoid 7).
No field closes on an abstract moral of the `આપણે પણ … જોઈએ` / `બોધ એ છે કે…` shape anywhere across
five `explanation`s, three summaries, `concept_bullets`, `important_points`, or recall answers (Avoid
2) — this chapter's humour is character-based and no field moralises it. The narrator `હું`/`મેં`/
`અમે` is kept as અંબારામ (the character) throughout, never conflated with રમણભાઈ નીલકંઠ (the real
author) — `M1.S1.T1`'s `explanation` states the split explicitly in its first sentence. No field
applies an evaluative label to સોરાબજી for the મુક્કો, and every quoted dialect line stays in its
printed form (both hard `07_pitfalls.json` checks on `M2.S3.T3`). `07_pitfalls.json`'s five hard
misconception corrections and `08_sensitivity.json`'s one hard item (`M2.S3.T3`, સમુદાય — the joke is
on ભદ્રંભદ્ર, never on સોરાબજી or Parsis) are each addressed exactly where the pitfall file asks:
spot-checked directly against the actual `explanation`/`concepts[].content[]` text, not only against
`12_authoring.json`'s own compliance notes. `figures_of_speech: []` on all five topics is vacuously
correct (invariant 11 has nothing to check).

**Contract — 12 invariants, all hold (verified programmatically).** `phase: 2`; `chapter_id` =
`gseb_eng_gujarati10_ch3` matches `gseb_eng_gujarati{grade}_ch{unit_number}`; `plan_id` =
`{chapter_id}_v{version}`; every `original_chunk` non-empty Gujarati-only; every topic has ≥1 concept
with a valid `concept_id`, a resolving `objective_id`, and non-empty `content[]` (verified on all 5
concepts); the objective registry is internally consistent — 5 unique `objective_id`s, every
`home_topic_id`/`anchor[]` entry and every topic's `objective_ids` resolves to a real node,
`strand_to_objective_map` covers `L1`–`L5` exactly; `learning_objectives[]` matches the root registry
**character for character on every field** on all 5 topics (scripted diff, not eyeballed); media id
`M2.S2.T2.C2.IMG1` / `M2.S3.T3.C3.IMG1` / `M2.S4.T4.C4.IMG1` / `M2.S4.T5.C5.IMG1` all match
`MEDIA_ID_RE` and are concept-scoped; recall ids are `{topic_id}.RQ{n}` / `{topic_id}.TR{n}` on all 15
recall questions, no `.SR{n}` anywhere; no સ્વાધ્યાય block is a topic, and all 7 inventoried items are
answered in `10_exercise_solutions.json`; all three summaries strictly increase in length on every
topic (scripted check); no digit — Latin or Gujarati — appears in any authored display field (scripted
scan of `topic_name`, `explanation`, `real_life_example`, summaries, bullets, prompts, `key_terms`,
`shabdarth`/`samanarthi`/`vilom`/`vyakaran`); `figures_of_speech` is vacuously compliant (`[]`
everywhere); every `anchor`/`home_topic_id`/`objective_ids`/`depends_on` reference resolves to a real
node id in the tree (invariant 12 is Agent 14's renumbering to preserve, not this gate's to renumber).

**Exercises — complete.** `10_exercise_solutions.json`'s `coverage_report.blocks_found` = 4 =
`exercise_inventory` length, `blocks_answered` = the same 4, all 7 items (EX1–EX7) answered,
`unanswered: []`, `unmapped: []`. `covered_by_topics` on every exercise resolves to a real topic id.
No comprehension answer narrates past the excerpt's end (EX7's સવિસ્તાર answer stops at the same
line the excerpt does, and says so).

---

## E–G (reported)

- **E — સ્વાધ્યાય and risk.** Complete, as above; nothing personal-opinion or પ્રવૃત્તિ-shaped in this
  chapter's small ladder, so no model-answer flag applies. `08_sensitivity.json` carries four **soft**
  items (`M1.S1.T1` ધર્મ, `M2.S2.T2` ધર્મ, `M2.S4.T4` ક્ષેત્ર, `M2.S4.T5` ધર્મ) and one **hard** item
  (`M2.S3.T3` સમુદાય) — all five addressed in `explanation`/`real_life_example`/`concepts[].content[]`
  per `12_authoring.json`'s own per-topic compliance notes, and independently re-checked against the
  actual field text for this report, not just against those notes.
- **F — shape and media.** All twelve contract invariants hold (above). `chapter_id`/`plan_id` shape
  is correct and provisional per VERIFY-1. One image per reading scene (4 STORY_TELLING topics, 4
  media nodes); the CONCEPT topic (`M1.S1.T1`) correctly carries no media since it depicts no single
  scene. `2d_tool: null` chapter-wide. `reuse_report`: `scenes: 4 · authored: 4 · reused: 0 ·
  rejected: []` — every `image_url` is `""`, every `generation_prompt` is real and self-contained
  (setting, characters with fixed appearance, action, mood, style, 16:9, Indian/colonial-Gujarat
  setting), and every `negative_prompt` carries `Devanagari script labels`. No `[reused frame: …]`
  stamp and no non-empty `image_url` anywhere — correct, since no Gujarati frame pool exists yet.
- **G — the seven usual mistakes.** Five are cleanly excluded by the structure and text that exist:
  no સાર+બોધ+પ્રશ્નોત્તર flattening (mistake 1 — checked directly in D above); no loose દુહા to merge,
  vacuous (mistake 2 — `structure_inventory.duha: 0`); no ટેક exists to mis-split (mistake 3,
  vacuous); every poetic/dialectal licence is uncorrected (mistake 4 — checked in B above); no
  `real_life_example` is adult-pitched, non-Indian, or wrong-standard (mistake 6 — checked in C
  above); no સ્વાધ્યાય block was cut as a topic (mistake 7 — checked in A/Exercises above). Mistake 5
  (an invented અલંકાર) is also excluded — `figures_of_speech: []` everywhere and nothing in this
  chapter's rendered apparatus names a device to invent one from.

## Media

`reuse_report`: **scenes 4 · authored 4 · reused 0 · rejected []**. The four authored scenes sit on
`M2.S2.T2.C2` (ઘરેથી પ્રયાણ), `M2.S3.T3.C3` (ટિકિટ-બારીની ભાષા-ટક્કર), `M2.S4.T4.C4` (પ્લેટફોર્મ પરનો
ચોકો), `M2.S4.T5.C5` (કોઠા-કમરખની બનાવટી દલીલ). Each `generation_prompt` depicts one photographable
moment (not a summary), keeps character appearance consistent across all four images (same heavyset
elderly man with grey moustache/kumkum/maroon pagh for Bhadrambhadra, same younger plainly-dressed
Ambaram), and sets the scene in early-1900s colonial Gujarat as the text implies. None carries a
narrator-bar text overlay — unlike some sibling chapters (e.g. `output8/ch01`, `output7/ch08`) that
quote a line under the image, this chapter's four images depict action/expression rather than a
single quotable line, which is a defensible choice (`field_shape_rules.md`'s narrator bar is
"where the design uses one," not mandatory) and matches `output10/ch02`'s own no-text-overlay
precedent for a different std-10 story chapter — noted here, not raised as a defect.

## Gaps

- **The one A–D failure** — two bare-Roman-script strings in `12_authoring.json`
  (`M1.S1.T1.concept_bullets[1]`, `M2.S3.T3.important_points[3]`) — is the whole of the FAIL above;
  see the table there for exact text and fix direction. Nothing else needs A12 to re-run.
- `textbook_url` is a **local path** (`../Textbooks-pdf/std-10/ch-03-prayan.pdf`) — no hosted URL
  exists for the GSEB readers yet. Carried verbatim from `11_pages.json`.
- `textbook_pages: "12–14"` at confidence **high** — cross-checked in `11_pages.json` against the
  printed folio on both end pages of the render; consistent with the board profile's std-10 N+5
  offset. No pagination gap.
- `chapter_master_id: null` and `publication_id: 1`. `01_meta.json`'s own `extraction_notes` record
  no verified GSEB DB row exists for this chapter yet (VERIFY-2 pending); `1` is written only because
  the contract rejects `null`, kept for pack-wide consistency with every other Gujarati chapter shipped
  so far (`output6`–`output10`), not derived or invented fresh. Both fields must be resolved from the
  education DB at VERIFY-2 before upload.
- `chapter_id`/`plan_id`'s board and medium segments (`gseb`/`eng`) are **provisional until
  VERIFY-1** — a wrong medium segment uploads clean and mis-files the plan (`01_meta.json`'s own
  `extraction_notes` flag this; not re-derived here).
- `estimated_time: 1.5` — the board profile marks this **"review at std 9–10"** (2 is plausible, per
  the Hindi pack's board-year value) and it has not yet been reviewed for this pack; `1.5` is kept
  only for consistency with every other std-9/10 Gujarati chapter shipped so far
  (`output9/ch01`, `output10/ch01`), not a fresh measurement.
- `medium_id` and `subject_ref_id` are `null` by contract (server-injected). `english_plan_id` /
  `english_chapter_id` are `null` — a Gujarati chapter has no English twin, none invented.
  `ordering: null` — Agent 14/15's field, deliberately not set here.
- **`05b_textbook_order.json` is identical to the logical traversal** (`M1.S1.T1`, `M2.S2.T2`,
  `M2.S3.T3`, `M2.S4.T4`, `M2.S4.T5` in both). Raised per `phase2_contract.md`'s own instruction:
  ```jsonc
  {"human_confirmation_required": true,
   "reason": "textbook order is identical to logical order",
   "checked": "05b_textbook_order.json matches the logical traversal exactly"}
  ```
- Working fields dropped at merge, as required: `genre_signals`, `genre_confidence`,
  `active_genre_profiles`, `explanation_unit`, `structure_inventory`, `exercise_inventory`,
  `extraction_notes` (all from `01_meta.json`); `notes` (from `05_with_content.json` and
  `12_authoring.json`); `tier`/`grade` top-level duplicates (from `12_authoring.json`, `grade`
  already lives at plan root); `topic_id` retained on media nodes (matches the established
  `output10/ch01` shape, kept for symmetry, redundant with `concept_id`/`home_concept_id`).
  `13_merged.json` carries the 32 root contract keys and nothing else at root.
- No render was opened this pass — every check above was answerable from `00_chapter_normalized.md`,
  `01_meta.json`, and the eight intermediate JSON layers that exist, all of which record their own
  render cross-checks (`01_meta.json`'s double-render note at 100dpi/200dpi; `05_with_content.json`'s
  own per-topic render cross-check note).

## LP2 validator

**Not run.** Blocked twice over: this plan does not yet pass A–D (the two voice-defect strings
above), and even a complete plan cannot be submitted until VERIFY-1 fixes the `chapter_id`
board/medium segments and VERIFY-2 supplies a real `chapter_master_id` and GSEB `publication_id`.
`POST /api/lp2/learning-plans/validate` must return zero `validation_errors` before this plan ships.

---

## Verdict

**FAIL — one narrow, fully-named item.** Re-run only the two strings in `agents/12_runtime_authoring.md`
(`M1.S1.T1.concept_bullets[1]`, `M2.S3.T3.important_points[3]`) — replace the bare Roman `vs`/`mad`
with Gujarati wording or a correctly-bracketed technical-term shape — then re-run
`agents/16_publication_authoring.md` only if the edited fields feed a `publication_text` (they do
not, since neither is `explanation` or a `concepts[].content[]` paragraph), then call this gate again.
Everything upstream of A12 — A1's diagnosis and transcription, A2/A4's cut and id freeze, A5's
verbatim attachment, A7's pitfalls, A8's sensitivity scan, A9's four media nodes, A10's complete
exercise deliverable, A11's pagination — is sound and does **not** need re-running, and neither does
the rest of A12's own output: both `explanation` and `real_life_example` are clean on all five topics,
and every hard pitfall/sensitivity check this agent could verify against the actual text holds.
`13_merged.json` was still written, in the full 32-root-key / 5-topic / 5-concept / 4-media-node
shape, with the two defect strings carried through unedited rather than silently repaired — never
presented as a pass.

**Validation passed.** Response from `POST /api/lp2/learning-plans/validate`:

```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati10_ch3_v1",
  "validation_errors": [],
  "message": "Valid"
}
```

**Result:** `validation_errors` is empty; plan is valid per LP2 validator.
