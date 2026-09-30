# Validation Report — std 8, ch 15, પોર્ટરના પંજામાં

સ્વરૂપ: આત્મકથાત્મક પ્રસંગ (હાસ્યપ્રસંગ / સંસ્મરણ) — profile `nibandh_atmaparak` (confidence: high)   explanation unit: એક પ્રસંગ

Topics: 6   Objectives: 6   Images: 0/6   Exercises: 15/15 blocks answered (74/74 items; 0 unanswered)

## A–D (blocking)   **PASS**

**A — Diagnosis and lens: PASS.** `genre_signals`/`genre_confidence: high` recorded off the rendered
page in `01_meta.json`, quoting the પ્રવેશપેટી box as evidence, not verdict. Explanation unit (એક
પ્રસંગ) matches the profile roster for આત્મપરક/લલિત નિબંધ. No topic carries `topic_category:
"climax"` (categories used: introduction/core/core/core/transition/resolution — profile Avoid item 2
holds). `guiding_question` is chapter-derived and answered by the topic sequence. Apparatus
(`[[પ્રવેશપેટી]]`, `[[શબ્દાર્થ]]`, `[[શબ્દસમૂહ માટે એક શબ્દ]]`, `[[રૂઢિપ્રયોગ]]`, `[[કહેવત]]`, all
`[[સ્વાધ્યાય: …]]` blocks) correctly did not become topics.

**B — Verbatim and structure: PASS.** All 6 `original_chunk`s are pure Gujarati script
(U+0A80–0AFF), no Roman/Devanagari outside the licensed bracketed shape (none needed here), no `।`
introduced (checked programmatically). `publication_chunk` is byte-identical to `original_chunk` for
all 6 topics (verified programmatically). The 6 `[[ઘટના: …]]` markers in `00_chapter_normalized.md`
equal the 6 topics carrying them (re-confirmed by direct grep: 6). No `[[સ્વાધ્યાય: …]]` block became
a topic (12 `[[સ્વાધ્યાય: …]]` markers exist in the render, 0 became topics). Dialectal/spoken forms
(`બી`, `કે'`, `કો'ક`, `કો'તો`, `બિચારું` inside the writer's own quoted line) kept exactly as printed
and glossed, never modernised.

**C — The teaching block: PASS.** Every topic has non-empty `explanation` and `real_life_example`.
Word counts (recomputed on the current file): `explanation` 79–90 words, `real_life_example` 76–81
words — all inside the 55–90 band; all 6 `objective_text`s are 22–29 words, inside the 12–30 band
(checked programmatically, zero out-of-band). `real_life_example`s are Indian, concrete, single-anchor,
std-8-appropriate (શાકવાળા કાકા, મોસાળે લાડુ, શેરી ક્રિકેટ). No craft device is named beyond std 8's
ceiling — the M2.S2.T4 simile ('વાઘનો શિકાર કરી લાવ્યો હોય એ રીતે') is noticed in plain words, never
labelled ઉપમા.

**D — સ્વરૂપ essence: PASS.** The prior blocking finding is resolved. `07_pitfalls.json` carries an
identical hard `avoid_check` on every topic instantiating profile Avoid item 1 ("the first sentence of
`explanation` names કિશોર/લેખક as the grammatical subject"). A12 (`12_authoring.json`) re-authored the
first sentence on exactly the three topics named in the previous report, restructuring each around
કિશોર as subject while preserving every fact, quote and register already present — verified literally
against the current `13_merged.json`:

| Topic | New first sentence of `explanation` | Grammatical subject |
|---|---|---|
| `M2.S2.T4` | "કિશોર પોર્ટરના હાથે સ્ટેશનમાસ્તરની ઓફિસ સુધી લઈ જવાય છે." | **કિશોર** (passive construction — કિશોર is taken) |
| `M2.S2.T5` | "કિશોર ડૂસકાં ભરતાં ભરતાં પણ પોતાની વાત પર અડગ રહે છે." | **કિશોર** |
| `M2.S3.T6` | "કિશોર જ્યાં દર વખતે ઊતરતો હતો એ વીશીના સજ્જનને ટોળા વચ્ચેથી અંદર આવતા જુએ છે." | **કિશોર** |

Diffed against the previously-shipped text: only these three `explanation` strings changed anywhere in
the chapter (every other field — `key_terms`, summaries, `concept_bullets`, `important_points`,
`recall_questions`, media, publication, exercises — is byte-identical to the prior merge). Every fact
and every quoted line present before the fix ('વાઘનો શિકાર કરી લાવ્યો હોય એ રીતે', 'ભગવાનના સોગન!',
'સાચું બોલી જા, છોડી દઈશ', 'ટિકિટના પછી પૈસા લેશે તો ઈડરથી ટિકિટ શાની કઢાવીશ?', 'હા ખરી વાત હો! એ જ
વિદ્યાર્થી છે!') is still present verbatim in the new text — the rewrite added no fact and removed
none. `M1.S1.T1`, `M1.S1.T2` and `M2.S2.T3` continue to open on કિશોર as grammatical subject and were
re-checked unchanged.

All other D items re-checked and hold: no field matches any "તાકેલો બોધ" pattern (`આ પાઠ આપણને
શીખવે…`, `આપણે પણ … જોઈએ`, `બોધ એ છે કે…`, `સાચું બોલવું જોઈએ`, `સત્ય જીતે છે`, `સત્યમેવ જયતે`) —
scanned programmatically across `explanation`, `real_life_example`, both summaries, `concept_bullets`,
`important_points` and every recall `answer`, zero hits; no pity/judgement register (`બિચારો`,
`બિચારાં`, `ગરીબ બિચારી`, `અભણ`, `પછાત`) appears in any authored field (the one occurrence of
`બિચારું` is inside the writer's own quoted line `'માથું તો બિચારું ના-ના કરતું હતું'`, verified
verbatim in `M1.S1.T2`'s `original_chunk` — the writer's self-mockery, not the plan's voice, and
licensed by the genre's own "admission" emphasis); no joke is explained or apologised for (this
chapter is not routed to the હાસ્ય sub-form — its comedy is mockery *at* the boy, so Avoid item 14,
not item 4, is the operative gate, per `07_pitfalls.json`'s chapter-level note, and no field softens or
extends the crowd's mockery, nor calls the crowd `ખરાબ લોકો`); no dialectal form is silently corrected;
no interiority invented for the real-named સ્ટેશનમાસ્તર or the unnamed વીશીના સજ્જન beyond what
`original_chunk` states; `figures_of_speech: []` on every topic, correctly (ગદ્ય, no printed poetic
device, std-8's craft-label ceiling holds); no outside historical/geographic fact imported about the
Modasa–Talod–Idar line (per `07_pitfalls.json`'s chapter-level note).

## E–G (reported)
- **E — સ્વાધ્યાય:** all 15 inventoried blocks answered (74/74 individual items across them;
  `unanswered: []`). `coverage_report.unmapped` correctly lists **41** items (recounted directly from
  `10_exercise_solutions.json` on this pass — the earlier "39" was a stale figure in a prior draft of
  this report; the underlying `10_exercise_solutions.json` itself has not changed since) — independent
  grammar/vocabulary drills (`શબ્દ-વિચાર` ×12, `વાક્યસંયોજન` ×9), idiom/કહેવત pre-block entries whose
  exact words are not printed in this chapter's own reading-scene text (`રૂઢિપ્રયોગ` ×8, `કહેવત` ×3), a
  supplied unrelated reading-fluency paragraph, an unrelated translation paragraph, an open cloze and an
  open creative block — each carries a stated reason in `10_exercise_solutions.json` rather than an
  invented `covered_by_topics` link. The single sensitivity flag (M1.S1.T2, jumping off a moving train)
  is correctly answered as guidance, not censorship.
- **F — Shape:** the 12 `json_contract.md` invariants hold (checked programmatically this pass —
  objective registry consistency, `strand_to_objective_map` completeness, inline `learning_objectives[]`
  mirrors matching `objective_text` character-for-character, `MEDIA_ID_RE` concept-scoped ids with
  chapter-continuous `.C1`–`.C7`, `RQ{n}`/`TR{n}` ids with no `SR{n}` anywhere, three-tier summaries
  strictly increasing at every topic, zero digits in any display-text field, `concept_publication`
  entries matching `concepts[].content[]` by `content_index` and by total count — 7 paragraph-type
  content items, 7 `concept_publication` entries, all text-identical). `topic_type` carries the
  authored intermediate value (`STORY_TELLING`) throughout, per `phase2_contract.md` — the closed-enum
  mapping to `instructional` is explicitly Agent 14's step, not this merge's.
- **G — Seven mistakes:** none present. No 7-topic-becomes-6 miscount (see Gaps); no દુહા/multi-poem
  fusion (N/A, prose); no ટેક split (N/A); no silently-corrected poetic licence (`બી`, `કે'`, `કો'ક`
  all intact); no invented અલંકાર (`figures_of_speech: []` everywhere, correctly); no
  `real_life_example` risk (all six re-checked: Indian, concrete, std-8-scaled); સ્વાધ્યાય fully
  separated from the topic deliverable.

## Media
`reuse_report`: `scenes: 6`, `authored: 6`, `reused: 0`, `rejected: []` — matches the 6 topics whose
`available_content_types` carries `"image"`. Every media node carries `image_url: ""` and a
non-empty, self-contained `generation_prompt` (setting, named-fixed-appearance characters, action,
mood, style, 16:9, narrator-bar line specified). `negative_prompt` carries "Devanagari script
labels" on all 6. At most one `2d_tool` in the chapter — actually zero (`null`), well within the
≤1 limit. No fabricated `image_url` or `[reused frame: …]` stamp anywhere. Media ids are
concept-scoped and chapter-continuous (`M2.S2.T5.C6.IMG1` correctly targets the topic's second
concept, not a `.T5.IMG1` topic-scoped id).

## Gaps
- **`textbook` is `null`.** `profiles/boards/gseb_gujarati.md` records "std 8 cover not read yet";
  Agent 1 and Agent 11 both correctly left this `null` rather than composing it from the filename or
  manifest. Needs the std-8 cover page rendered and read before this field can be filled.
- **`textbook_url` is a local PDF path** (`../Textbooks-pdf/std-8/ch-15-portarna-panjama.pdf`) — no
  hosted URL exists yet. Expected at this stage.
- **`textbook_pages` confidence is `medium`** (`123–132`, cross-checked two independent ways in
  `11_pages.json` — folio read off renders and the manifest's `pdf_start`/`pdf_end` offset
  arithmetic — both agree, but the source calls its own confidence medium, carried forward as-is).
- **`chapter_id`/`plan_id`'s `eng` medium segment is unverified (VERIFY-1)** and **`publication_id`
  is the pack-wide provisional placeholder `1`** (the CBSE/Hindi row, not a confirmed GSEB value —
  same known issue tracked in `RESUME.md` for every std-6 chapter; **VERIFY-2** must resolve the real
  GSEB row before upload). **`chapter_master_id` stays `null`**, to be fetched from the education DB
  per `upload_reference/chapter_master_map.json` — never derived or invented.
- **`01_meta.json`'s `structure_inventory.ghatna: 7` vs. the render's 6 `[[ઘટના: …]]` markers.**
  Already investigated and resolved by Agent 4/5 (`04_validation.json`, `05_with_content.json`'s own
  `notes[]`): the render is authoritative at exactly 6 markers, and the "seventh movement" 01_meta.json
  counted is correctly absorbed as `M2.S2.T5`'s genuine two-concept split (`C5`+`C6`) rather than a
  manufactured seventh topic — matches the profile's own "two concepts, never a third topic"
  instruction. Recorded here per this agent's own note-carrying duty, not reopened.
- **`07_pitfalls.json`'s M1.S1.T2 sensitivity flag** (severity hard, area સુરક્ષા: the line "ખભે
  ભરાવેલી પોટલી ઉપર હાથ રાખી કૂદી પડ્યા" — jumping off the train — could read as an ordinary quick
  move) is correctly addressed: `real_life_example` for M1.S1.T2 anchors on a maasi giving a laddu,
  not on jumping on/off a moving vehicle, and `explanation` does not describe the jump at all, keeping
  the scene inside the boy's helpfulness only.
- **`coverage_report.unmapped` count corrected to 41** (see E above) — a reporting correction on this
  pass, not a change to the underlying exercise deliverable, which is unchanged and was already fully
  answered.

## LP2 validator
**Phase 8 validation result (2026-08-30):**

Endpoint: `POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate`
File: `learning_plan_logical.json`
Status: **PASS** ✓

Response:
```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati8_ch15_v1",
  "validation_errors": [],
  "message": "Valid"
}
```

**Validation errors:** None (empty array)
**Status:** Ready for upload

