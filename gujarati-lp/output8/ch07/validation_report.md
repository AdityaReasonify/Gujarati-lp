# Validation Report — std 8, ch 7 · કંકોતરી

સ્વરૂપ: લોકગીત (લગ્નગીત) — profile `lok_geet.md` (confidence: high)   explanation unit: એક કડી, અથવા એક ટેક-રાઉન્ડ

Topics: 3   Objectives: 3   Images: 0/3   Exercises: 14/14 blocks · 52/52 items

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` → `13_merged.json` (31 of the 32 root keys; `ordering` is
Agent 14/15's and was deliberately not written). This is a first QC pass — no prior failure to
re-verify.

---

## A–D (blocking)   **PASS**

### A — diagnosis and lens.   Holds.

સ્વરૂપ લોકગીત (લગ્નગીત), confidence high, diagnosed off the rendered page from the four signals
recorded in `01_meta.json` (structure, theme, exercises, purpose all agree — the intro box's own
words `આ એક લગ્નગીત છે. લગ્નગીત એ લોકગીતનો જ એક પ્રકાર છે.` and the author-slot `- લોકગીત` are
quoted as evidence, not as the verdict) and cross-agreed by `04_validation.json`. The explanation
unit `એક કડી, અથવા એક ટેક-રાઉન્ડ` matches `lok_geet.md`'s round-wise roster row, and this exact
chapter is that profile's own worked example. `ટેક` is handled as content, not repetition: the
refrain is printed word-for-word identical four times and is taught once (M1.S1.T1) and referenced
(never re-taught, never hunted for a change) at M1.S1.T2/T3 — confirmed both structurally
(`05_with_content.json`'s `depends_on`) and in the authored text (see D below). Apparatus stayed
apparatus: the blue પ્રવેશપેટી (tagged by Agent 1 itself `શિક્ષક માટે — વાચન-દૃશ્ય નથી`), the yellow
શબ્દાર્થ box, and the closing ચર્ચા-વિચારણા box with its two-column table are outside the topic
tree and carry no topic. No pre-reading CONCEPT topic exists — measured (this chapter's intro box
is teacher-addressed, unlike std-10's student-facing પરિચય), not omitted. `guiding_question` is
derived from this chapter's own કાકા→મામા→માસી round structure and reading T1→T3 in order answers
it. This is not a mixed chapter (single genre, single printed poem across all six rendered pages).

### B — verbatim and structure.   Holds.

All 3 `original_chunk` non-empty. Programmatic scan of the full merged plan: **0 Devanagari
codepoints, 0 Roman letters, 0 `।` (daṇḍa)** in any `original_chunk`. `publication_chunk` starts
with `original_chunk` byte-identical on 3/3 (checked programmatically). Marker parity: three
`[[કડી N]]` markers in `00_chapter_normalized.md` against three topics, one `[[કડી N]]` marker
each, in printed order — the four `[[ટેક]]` occurrences are not `[[કડી]]`/`[[દુહો]]`/`[[પદ]]`/
`[[ઘટના]]` markers and are folded into the round topic they frame, per `lok_geet.md`'s inverted
ટેક rule (`05_with_content.json`'s upstream `marker_accounting` documents every one of the 7 raw
markers explicitly, none silently swallowed). **No સ્વાધ્યાય block became a topic** — all fourteen
`[[સ્વાધ્યાય: …]]` markers, including block 8's embedded second લગ્નગીત and block 9's `મંગલ પરિણય`
cloze, match `01_meta.json`'s `exercise_inventory` exactly with zero overlap against any topic
name or chunk. Poetic licence preserved, not corrected: `રોપિયો` (printed five times across all
three topics) kept exactly, never silently replaced with `રોપ્યો` and never called an error in any
authored field. Line-internal echoes `માણેકથંભ રોપિયો...` and `...કંકોતરી...` kept exactly where
and how printed. The closing ટેક's `.` (full stop, vs `,` at the three earlier printings) is kept
as printed. Header furniture (chapter-number box, QR badge, footers) never entered the text.

### C — the teaching block.   Holds.

All 3 topics carry non-empty `explanation` **and** `real_life_example`. Measured word counts, all
inside `field_shape_rules.md` bands, no band widened (checked programmatically):
`explanation`/`real_life_example` T1 78/76, T2 66/62, T3 76/69 — all within 55–90;
`objective_text` O1/O2/O3 all within 12–30. No numerals — Arabic or Gujarati — in any authored
display text (topic names, explanations, examples, three summaries, concept bullets, important
points, concept `content[]`, recall prompts/answers, objective texts, `guiding_question`): checked
programmatically, zero hits (`પહેલી કંકોતરી`/`બીજી કંકોતરી`/`ત્રીજી કંકોતરી` are the poem's own
printed ordinal words, used as such, never a bare numeral). Glossing sits at point of first use, in
Gujarati, calibrated to L2 (`રોપિયો`, `હોંશે`, `મોસાળું`, `ભાણેજ` all glossed the moment they
appear). Craft: `figures_of_speech` is `[]` on all three topics per the std-8 grade gate (named
devices start at std 9) — the song's sound-play (`મોકલો`-rhyme, the line-internal echoes) is
described plainly inside `rhyme_scheme` instead, matching the gate's "notice, don't name" rule.

### D — સ્વરૂપ essence.   Holds.

All 8 `severity:"hard"` items across `07_pitfalls.json`'s three topics were checked against the
merged authored text:

- **No author named** anywhere in any topic's `explanation`/`real_life_example`/summaries/recall
  answers — confirmed by scan; the book's own `- લોકગીત` slot is respected.
- **`રોપિયો` never silently standardised or called an error** — `explanation`, `key_terms` and
  `shabdarth` all state it is `રોપ્યો`, the folk-ઢાળ form, "ભૂલ નથી," at first occurrence in every
  topic that carries it.
- **`બેની ~ નાગરવેલનો છોડ` named as comparison, never literal fact** — T1's `explanation`, its
  RQ2 answer, and its concept paragraph all explicitly say "આ સરખામણી છે, બેની ખરેખર છોડ નથી" /
  "શબ્દશઃ ન લેવી."
- **Line-internal echoes never called filler** — `માણેકથંભ રોપિયો...` and `...કંકોતરી...` are
  named as the song's ઢાળ-carrying પડઘો throughout.
- **No tacked-on બોધ** — no `explanation`, summary, bullet or recall answer in any of the three
  topics closes on an `...જોઈએ` exhortation; a scan for `જોઈએ` across every authored field
  (explanation, real_life_example, summaries, bullets, recall prompts/answers, concept content)
  returns zero hits.
- **No hunting for a change in the unchanged ટેક (T2, T3)** — every `બદલા/બદલાય/ફેરફાર`-adjacent
  sentence found by a keyword scan is, on inspection, an explicit **negation** of change
  (`બદલાયા વિના`, `શબ્દોમાં કંઈ ફેરફાર નથી`), matching `07_pitfalls.json`'s own prescribed
  `correction` wording for T3 verbatim. No field asks what changed in an unchanged refrain.
- **T2's મોસાળું kept as ઉમંગ, not obligation** — `real_life_example` explicitly states
  "મા-પક્ષનો આ સ્નેહ કોઈ ફરજ નથી, હોંશ છે" (a negation of duty-framing, not an assertion of it),
  matching `08_sensitivity.json`'s soft-severity guidance for this topic; no cost or obligation
  language anywhere else in T2.
- **T3's માસી-ભાણેજ material kept inside હોંશ, not duty** — confirmed, no obligation framing.

`figures_of_speech` invariant is vacuously satisfied (`[]` on all three topics — nothing to
verify). Sensitivity soft items (all 3 topic-level + 1 chapter-level in `08_sensitivity.json`) are
honoured: kinship words (કાકા, મામા, માસી, ભત્રીજ, ભાણેજ) kept exact throughout, never generalised
to "સગાં-વહાલાં"; the region/custom is taught as living tradition, never as "even today" curiosity.

### Contract — the 12 `json_contract.md` invariants.

All 12 hold, checked programmatically against the merged plan: `phase: 2`; `plan_id` =
`chapter_id` + `_v1`; `chapter_id` = `gseb_eng_gujarati8_ch7`. Objectives registry O1–O3 unique,
every `home_topic_id` and every `anchor[]` id resolves, `strand_to_objective_map` covers L1–L3
one-to-one. Inline `learning_objectives[]` mirrors match root `objective_text` character for
character and each carries `image_examples: []`. Concept ids run `C1`→`C2`→`C3`, chapter-continuous
and equal to the topic number (one concept per topic throughout). All 3 media ids match
`MEDIA_ID_RE` (concept-scoped: `M1.S1.T1.C1.IMG1` etc.). Recalls are `.RQ{n}` with `legacy_id`
`.TR{n}`; **the string `.SR` occurs nowhere in the merged plan.** `publication_id` is non-null
(flagged placeholder, see Gaps). `topic_type` is the authored enum (`POEM` ×3) throughout, which
Agent 14/15 maps to the closed server enum `instructional` at emit. Summaries strictly increase on
all 3 topics (word-count checked programmatically). Invariant 11 (`figures_of_speech` quotes only
words found verbatim) is vacuously satisfied.

### Exercises.

`coverage_report.blocks_found` = 14 = `exercise_inventory` length; every inventory
`verbatim_heading` present; `unanswered` is `[]`; all 52 recorded items carry a non-empty answer
(programmatically checked). Two printed multi-blank cloze blocks (block 6's 6-word word-bank
paragraph; block 9's 15-blank `મંગલ પરિણય` card) are each answered as one consolidated exercise
item with every blank filled in `values_filled_for_teaching` — the printed block is a single
fill-in task, not 6/15 separable questions, so this is a faithful representation, not a coverage
shortfall. Every `covered_by_topics` id resolves to a real topic (checked; 0 dangling refs).

### Media.

`reuse_report` `scenes: 3` equals the 3 topics whose `available_content_types` carry `"image"`;
`authored: 3`; `reused: 0`; `rejected: []`. Every media node has `image_url: ""` **and** a
non-empty, self-contained `generation_prompt`; every `negative_prompt` carries `Devanagari script
labels`. `2d_tool` is `null` on all three topics — 0 of the permitted 1 (matching
`lok_geet.md`'s own note that a lokgeet rarely needs one).

### Publication.

`publication_text` on 3/3. `publication_chunk` begins with `original_chunk` byte-identical on 3/3
(the rewrite is appended after a blank line, never overwriting the verbatim). `concept_publication`
blocks match `concepts[].content[]` by `concept_id` + `content_index` on all 3 paragraph-type
blocks (the accompanying list-type block correctly carries no `publication_text`, matching the
sibling-chapter pattern). `બાળકો`, `જુઓ —` and `બોલો` occur **zero** times in any `publication_text`
or `concept_publication.publication_text` — `12_authoring.json`'s `explanation` fields open with
`બાળકો, જુઓ —` (acceptable teaching-voice address, not a publication field) and this address is
correctly stripped in every `16_publication.json` rewrite. No meaning was added in the rewrite
beyond what `explanation`/`real_life_example` already say.

---

## E–G (reported)

- **14 of 52 exercise items are reported `unmapped`, and that is the honest number.** Never
  emptied by inventing a `covered_by_topics`. The families: block 8's embedded second, unfinished
  લગ્નગીત (`EX36` — a family-completion task, not this chapter's own text); block 9's `મંગલ પરિણય`
  cloze invitation card (`EX37` — invented fruit-name realia, no line in this chapter's poem); all
  six generic કર્તરિ-કર્મણિ voice-change practice sentences (`EX38–EX43` — journalists, doctors, a
  truck strike, a builder, a manager); four of six generic redundancy-deletion sentences
  (`EX44, EX46–EX49`); and the standing L1-medium અનુવાદ paragraph about Ganga and Biharilal,
  unrelated characters (`EX51`). Every mapped item's `covered_by_topics` resolves to a real topic
  (checked; 0 dangling refs).
- **The closing ચર્ચા-વિચારણા box (`લગ્ન સાદાઈથી કરવાં જોઈએ કે નહીં`) and its two-column table are
  answered nowhere**, by design — `01_meta.json`'s own `extraction_notes[]` records this box as
  apparatus, not an exercise, matching `lok_geet.md`'s explicit routing of this exact box. Correctly
  absent from `exercise_inventory`, so the 14=14 block parity is genuinely complete against the
  inventory as scoped.
- **Sensitivity soft items (3 topic-level + 1 chapter-level in `08_sensitivity.json`), all held** —
  see D above for the topic-level detail; the chapter-level ક્ષેત્ર guidance (teach the customs as
  a regional wedding tradition with its own logic and warmth, kinship words kept exact) is honoured
  throughout.
- **EX36's answer includes one illustrative, clearly-marked sample completion** of the exercise's
  own family-song-completion task ("ફક્ત ઉદાહરણરૂપ પૂર્તિ," explicitly flagged as an example, not
  the traditional printed verse) — consistent with `no_hallucination_policy.md`'s rule that a
  personal/family-sourced answer gets a model response marked as one possible option, not asserted
  as *the* answer. Not a fabrication of this chapter's own text.
- **G, the seven usual mistakes: all seven absent.** No સાર+બોધ+પ્રશ્નોત્તર substitution (this is a
  round-wise લોકગીત, taught as કડી/ટેક-round, not summarised-then-moralised); no દુહા merged (n/a —
  no દુહા in this chapter); no પદ split (n/a — this is a લોકગીત, not a પદ; and its own ટેક is
  correctly taught once and referenced, never split or re-taught); no poetic licence silently
  corrected (`રોપિયો` kept, five instances, glossed as folk form); no `figures_of_speech` named
  because the field existed (`[]` everywhere, correct for the std-8 grade gate); `real_life_example`
  is Indian, single, concrete and inside std-8 reach on all 3 topics (T1: family readying and
  sending its own કંકોતરી; T2: મોસાળ-visit and kinship gift-giving; T3: a favourite માસી/ફોઈ's
  eager arrival — no domain repeats verbatim, no adult-pitched or std-10-level anchor); સ્વાધ્યાય
  was not cut as teaching topics.

---

## Media

`reuse_report`: **scenes 3 · authored 3 · reused 0 · rejected []** — no frame was rejected because
no Gujarati frame pool exists to draw from. One illustration per reading round, concept-scoped
(`M1.S1.T1.C1.IMG1`, `M1.S1.T2.C2.IMG1`, `M1.S1.T3.C3.IMG1`), all `image_url: ""` with a real
self-contained `generation_prompt`, all `negative_prompt`s carrying `Devanagari script labels`.
`2d_tool` is `null` for the whole chapter — 0 of the permitted 1. `Images: 0/3` is written as zero
deliberately: nothing is reused, nothing is generated yet.

---

## Gaps

- **`publication_id` is a flagged placeholder, not a verified value.** `1` is written to satisfy
  the non-null requirement (matching the placeholder already used in this pack's earlier std-8
  chapters), but `phase2_contract.md` rule 1 states plainly that `1` is CBSE's publication row and
  is not portable to GSEB. The real GSEB row must be fetched from the education DB (**VERIFY-2**)
  before any Phase 8 upload.
- **`chapter_master_id` is `null`.** Mandatory for upload, not discoverable from the LP2 API,
  fetched per chapter from the education DB (VERIFY-2). Never derived by arithmetic.
- **`textbook` is `null` — an honest gap, not a filled placeholder.** `11_pages.json` and
  `01_meta.json` both record that the std-8 cover was not among this run's supplied renders, so the
  printed reader title could not be confirmed off a render and was left `null` rather than composed
  from the filename or a manifest field. (Note: three of this pack's earlier std-8 chapters —
  `ch01`, `ch02`, `ch06` — carry a filled `textbook` string in their own `13_merged.json` despite
  the same upstream `null`; this chapter's own `11_pages.json` explicitly declines to do that, and
  this agent followed that chapter's own file rather than the sibling precedent. Worth a
  cross-chapter reconciliation pass once a std-8 cover render exists, but not a blocker for ch07 on
  its own terms.) Owner `agents/01_ingestion_genre_diagnosis.md`, once a cover render exists.
- **`textbook_url` is a local path string** (`../Textbooks-pdf/std-8/ch-07-kankotari.pdf`) — the
  GSEB readers have no hosted URL. `textbook_pages` `53–58` is confidence `medium`, read off the
  printed folios on page-1 and page-6 renders, cross-checked against the manifest and the std-8
  offset table. Never blocks (`11_pages.json` fails soft by design).
- **`chapter_id` / `plan_id` board and medium segments are UNVERIFIED (VERIFY-1).**
  `gseb_eng_gujarati8_ch7` follows `naming_conventions.md`, but a wrong medium slot uploads clean
  and mis-files the plan under the wrong medium column. Confirm both segments against the live
  server before the first upload.
- **`subject_ref_id` and `medium_id` are `null` by design** — server-injected, in
  `VOLATILE_TOP_LEVEL_KEYS`. No GSEB subject record is confirmed; nothing carried over from the
  Hindi pack.
- **`english_plan_id` / `english_chapter_id` are `null`** — a Gujarati chapter has no English twin.
  Not a gap to be closed.
- **`ordering` is absent from the root by design** — Agent 14/15's to set at emit; 31 of the 32
  contract root keys are written here. `topic_title` is set to the printed chapter name `કંકોતરી`,
  mirroring `unit_title`; derived, not authored by any agent.
- **Render provenance is single-rasterisation**, per the orchestrator constraint (renders are
  shared and not re-run this pass). This QC pass read no PNG under `_renders` — the six-page
  `00_chapter_normalized.md` and the upstream JSONs (which themselves record line-by-line render
  verification at Agent 5) answered every question this pass needed.
- **`concept_bullets` and `important_points` are identical lists on all three topics** (a valid
  authoring choice under `field_shape_rules.md` — nothing requires the two fields to differ — but
  noted here as a style observation, not a defect).
- **`01_meta.json`'s own `structure_inventory` note explains the 7-marker-to-3-topic fold** (four
  `[[ટેક]]` occurrences plus three `[[કડી N]]` markers, folded into three round-topics per
  `lok_geet.md`'s round-wise unit and inverted-ટેક rule) — not a coverage gap; every one of the 7
  raw markers is individually accounted for in `05_with_content.json`'s upstream
  `marker_accounting`, and this agent's own B-section check (3 `[[કડી N]]` markers = 3 topics
  carrying them) is exact.

---

## LP2 validator

Validated at staging endpoint on 2026-08-29.

**Request:** POST `/agentapi/api/lp2/learning-plans/validate` (multipart field "file")

**Response:**

```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati8_ch7_v1",
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

**Result:** PASS — zero validation errors. Plan is ready for VERIFY-2 and upload (publication_id and chapter_master_id required before Phase 8 completion).
