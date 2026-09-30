# Validation Report — std9/ch02 (પરોપકારી મનુષ્યો)

સ્વરૂપ: હાસ્યનિબંધ (nibandh_atmaparak) (confidence: high)   explanation unit: એક ઘટના (એક સલાહ-પ્રસંગ)
Topics: 13   Objectives: 13   Images: 0/11   Exercises: 4/4 blocks (9/9 items) answered

**RE-QC note (this pass):** `12_authoring.json` has landed since the prior report (all 13 topics
now carry `explanation`, `real_life_example`, summaries, `concepts[].content[]`,
`figures_of_speech`, the ભાષા-બોધ extras). It was checked in full below and clears every mechanical
and textual gate. `16_publication.json` has **not** landed. That single remaining absence still
blocks the merge — the verdict stays **FAIL**, narrower than last time but not closed.

## A–D (blocking)   **FAIL** (narrowed to Publication only)

- **A — Diagnosis and lens: PASS.** Unchanged from the prior pass. `04_validation.json` records
  `status: "pass"` for `genre_fidelity`: 11 `[[ઘટના: …]]` markers in `00_chapter_normalized.md` map
  1:1 to the 11 `STORY_TELLING` topics (`M2.S1.T3`…`M2.S5.T13`), and 2 `[[…-પરિચય]]` apparatus
  markers map 1:1 to the 2 `CONCEPT` topics (`M1.S1.T1`, `M1.S1.T2`). No `[[સ્વાધ્યાય: …]]` block
  became a topic. `guiding_question`/`teaching_lens` are chapter-derived per `01_meta.json`.
- **B — Verbatim and structure: PASS.** Unchanged. Every topic in `05_with_content.json` carries a
  non-empty Gujarati-script `original_chunk`; ids are consecutive; the 11 `[[ઘટના: …]]` marker count
  re-confirmed against `00_chapter_normalized.md` (lines 13,16,31,36,41,50,57,60,69,74,77) equals
  the 11 `STORY_TELLING` topics; no `[[સ્વાધ્યાય: …]]` block is a topic.
- **C — The teaching block: PASS, now checked in full.** `12_authoring.json` exists and every one
  of the 13 topics carries non-empty `explanation` and `real_life_example`. Programmatic checks on
  all 13 topics: word counts for both fields land inside 55–90 for every topic (no band failures);
  script check (Roman/Devanagari outside bracketed technical terms, `।`) is clean across
  `explanation`, `real_life_example`, all three summaries, `concept_bullets` and `important_points`;
  no digit (Arabic or Gujarati numeral) appears in any authored display field, recall prompt, or
  recall answer. `real_life_example` anchors are Indian, single, in-standard, and — per
  `12_authoring.json`'s own notes — deliberately rotate domain scene to scene (school/recess,
  cricket, market/bookshop, a game's "sure trick", an exam superstition, road safety, a stuck
  bicycle tyre, a stuck dosa, kitchen help, a bicycle mechanic) so no picture repeats, and none
  reaches for a health/eye/skin remedy (the chapter-level સુરક્ષા guidance below).
- **D — સ્વરૂપ essence: PASS.** `figures_of_speech` is `[]` on every topic except `M2.S5.T13`,
  where the single entry (`અતિશયોક્તિ`, lines `"દવાઓનો ડુંગર સાફ કરાવ્યો"`) was checked
  programmatically against that topic's `original_chunk` and is found verbatim — not invented.
  `rhyme_scheme` is `null` throughout (ગદ્ય), matching the module's `difficult_words: []` /
  `overall_rhyme_scheme: null`. Both `severity:"hard"` sensitivity items were read directly in the
  authored text and hold:
  - `M2.S3.T8` — `explanation` keeps the narrator's refusal as the scene's point ("લેખિકા સ્પષ્ટ ના
    પાડે છે — 'ભૈયાજી હું ભાંગ કે બીજો કોઈ કેફી પદાર્થ પીતો નથી.'... લેખિકા આ સલાહનો ક્યાંય અમલ
    કરતાં નથી") and never states ભાંગ/યાકૂતી as a working remedy; `real_life_example` swaps the
    medical scenario for a non-medical safety refusal (a helmet-less bike ride), per the
    chapter-level guidance in `08_sensitivity.json`.
  - `M2.S4.T10` — `explanation` states plainly "'પરિણામમાં દરદ વધ્યું' — પહેલી વાર કોઈ સલાહ ખરેખર
    નુકસાન કરે છે"; `real_life_example` (a worsened bicycle-tyre puncture) never suggests applying
    heat, sindoor or onion juice to an eye or skin.
  - The chapter-level સુરક્ષા note (every remedy stays inside the essay's comic catalogue; no
    `real_life_example` tries a remedy on a body part) and the chapter-level સમુદાય note (the
    Hindi-mixed ભૈયો, the Parsi-inflected friend, and "મારવાડી" are quoted/named as the essay's own
    device, never turned into a community generalisation) both hold in the two explanations that
    touch them (`M2.S3.T8`, `M2.S4.T10`, `M2.S4.T11`) — checked by direct reading, not merely
    asserted.
  - `12_authoring.json`'s own `notes[]` walk all 25 hard `avoid_checks` from `07_pitfalls.json`
    topic-by-topic (T1 through T13) explaining how each is honoured; spot-read against the actual
    `explanation` text for T8/T10 (above) confirms the notes describe what was actually written,
    not just what was intended.
  - `પરોપકારી મનુષ્યો` and `M2.S3.T9`'s `પરદુ:ખભંજન` are nowhere taken as sincere praise; the essay's
    નર્મ-મર્મ કટાક્ષ register is preserved (per `12_authoring.json`'s chapter-level note, confirmed
    against `explanation` text) — no imposed બોધ, no ઉપદેશ, no "this essay teaches us" line found in
    any of the 13 topics' authored fields.

**Contract mechanics (checked ahead of merge, all PASS on what exists):** the 13
`objective_text` entries in `05_with_content.json`'s root registry are each 14–20 words (inside the
12–30 band); `concept_id`s are chapter-continuous and match the topic number exactly
(`M1.S1.T1.C1` … `M2.S5.T13.C13`); every `recall_questions[]` entry carries `id={topic}.RQ{n}` and
`legacy_id={topic}.TR{n}` — never `.SR{n}`; `key_terms` runs 4–5 per topic (inside the 3–6 band);
`estimated_exchanges` is a numeric string on every topic; the three summaries strictly increase in
length on all 13 topics; `09_media.json`'s 11 media nodes each carry `image_url:""` **and** a
non-empty `generation_prompt`, `negative_prompt` names "Devanagari script labels", `reuse_report`
reads `scenes:11 authored:11 reused:0`, and `2d_tool` is `null` — all clean.

- **Contract / Publication: still FAIL, blocking.** `16_publication.json` **does not exist** in
  `output9/ch02/` (confirmed again this pass — `find . -iname "*publication*"` returns nothing).
  `publication_text`, `publication_chunk`, and `concepts[].content[].publication_text` remain
  entirely unauthored; `12_authoring.json`'s own closing note says so explicitly ("publication_text,
  publication_chunk and every media/exercise field are out of scope for this agent"). These are
  required topic keys in `phase2_contract.md`'s Topic keys (31) list — a merge that omits them on
  every topic is not "one phase-2 plan per the contract," it is a plan missing two required fields
  on all 13 topics. Agent 16 (Publication Authoring) has still not run for this chapter.

**`13_merged.json` is not emitted this run.** Everything upstream of Agent 16 — diagnosis, verbatim,
authoring, sensitivity, media, exercises — now checks out clean and is ready to fold. But folding
`05_with_content.json` + `12_authoring.json` + `09_media.json` + `11_pages.json` + `01_meta.json`
while leaving `publication_text`/`publication_chunk`/`concepts[].content[].publication_text` null or
absent on all 13 topics would ship a plan that fails the Publication check on every topic — a
known-broken artifact. Per this agent's own instructions ("do not fix authoring yourself… name the
owner and stop"), the merge is withheld again, now for exactly one reason instead of three.
**Re-run this agent once `16_publication.json` lands — nothing else is blocking.**

## E–G (reported)

- **E — Exercises: clean, re-confirmed.** `10_exercise_solutions.json.coverage_report`: all 4
  inventoried blocks (MCQ ✓, કારણ આપો, બે-ત્રણ વાક્ય, પાંચ-છ વાક્ય — 9 items total) answered as
  EX1–EX9; `unanswered: []`, `unmapped: []`. Every item's mapping to a reading-scene topic is
  recorded in the `_note` (EX1→M2.S1.T3; EX2/EX5→M2.S5.T12; EX3/EX4/EX6→M2.S1.T4; EX7→M2.S2.T6 and
  M2.S3.T7; EX8→M2.S2.T5; EX9→ all 11 ઘટના topics). This chapter prints no વિદ્યાર્થી-પ્રવૃત્તિ block
  and no વ્યાકરણ એકમ (confirmed against the render), so 9/9 is the complete set. Transcription
  defect owned by Agent 1: `00_chapter_normalized.md` line 123 has `હજમે` where the page-4 render
  (300 dpi) clearly shows `હજામે`; EX7's `prompt_verbatim` was kept per the render, not the
  transcription file — not blocking, carried forward.
- **E — Sensitivity: both hard items now checked against authored text and hold** — see D above for
  the specifics (`M2.S3.T8`, `M2.S4.T10`). The two `severity:"soft"` items on `M2.S3.T7`
  ("વાંઝણી" not repeated as commentary) and `M2.S4.T11` (Parsi-inflected speech quoted, not mocked)
  and the `severity:"soft"` items on `M2.S3.T8`/`M2.S4.T10` (Hindi-mixed speech, "મારવાડી" naming)
  were also read directly in the corresponding `explanation` text and hold — no mockery, no
  generalisation to a community, quoted forms kept exact.
- **F — Shape: PASS on everything that exists** (see Contract mechanics above); the 12
  `json_contract.md` invariants that depend on the publication layer (none of the 12 explicitly do —
  they gate registry consistency, id grammar, media, `figures_of_speech`, summaries, digits) are all
  independently verifiable now and hold. The only invariant that cannot be closed until Agent 16 has
  run is the Topic-keys completeness implied by `phase2_contract.md`'s key list, not one of the 12
  numbered invariants itself.
- **G — usual failure modes: none observed.** Genre kept as હાસ્યનિબંધ throughout; no ઘટના split
  from its setup; no ચરિત્ર/biographical fact invented in `M1.S1.T1`/`T2`; no અલંકાર named beyond the
  one verbatim-checked અતિશયોક્તિ; no `real_life_example` set outside India, pitched at the wrong
  standard, or reaching for a health remedy; સ્વાધ્યાય not cut as teaching topics.

## Media

`09_media.json.reuse_report`: `scenes: 11`, `authored: 11`, `reused: 0`, `rejected: []` — matches
the 11 topics whose `available_content_types` carry `"image"` (the 11 `STORY_TELLING` ઘટના topics;
the 2 `CONCEPT` પરિચય topics carry none). Every one of the 11 media nodes checked individually:
`image_url:""`, non-empty `generation_prompt`, `negative_prompt` containing "Devanagari script
labels". `2d_tool: null`. Structurally clean and ready to fold; not folded this run per the FAIL
above.

## Gaps

- `11_pages.json`: `textbook_pages: "3–7"`, confidence **medium** — the page range itself was read
  directly off both end-page renders (folio 3 / folio 7, agreeing with `manifest.json` and the
  board profile's std-9 N+4 offset), but the std-9 cover page has not itself been read/confirmed
  per `profiles/boards/gseb_gujarati.md`, so the title-page confirmation is the open gap, not the
  pagination. `textbook_url` is a local PDF path — no hosted URL exists.
  `chapter_master_id`/`publication_id` remain unresolved server-side lookups (VERIFY-2), unrelated
  to this run's blocker.
- Transcription defect `હજમે` → `હજામે` at `00_chapter_normalized.md:123`, owned by Agent 1, already
  worked around in `10_exercise_solutions.json`'s EX7 (see above) — carried forward, not blocking.
- **The one remaining blocking gap:** `16_publication.json` is absent from `output9/ch02/`.
  `12_authoring.json` landed since the prior pass and is now fully verified clean. Everything else
  (`01,04,05,07,08,09,10,11,12`) is present, mutually consistent, and requires no rework.

## LP2 validator

**Phase 8 validation attempt (2026-08-29):** `learning_plan_logical.json` does not exist in `output9/ch02/`. The merged learning plan file that should be validated is not available. Validation cannot proceed. This is consistent with the pre-merge block documented above — the plan merge is blocked until `16_publication.json` lands and the merge can complete.
