# Validation Report — std 9, ch 11 વારસાગત

સ્વરૂપ: લઘુકથા (વાર્તા) (confidence: high)   explanation unit: એક ઘટના (વાર્તાનું એક પગલું)   tier: ધોરણ
Topics: 6   Objectives: 5   Images: 0/4   Exercises: 9/9 items (4/4 blocks) answered

**This pass:** RE-QC / final pass. All eleven inputs (`01_meta.json`, `05_with_content.json`,
`07_pitfalls.json`, `08_sensitivity.json`, `09_media.json`, `10_exercise_solutions.json`,
`11_pages.json`, `12_authoring.json`, `16_publication.json`, `04_validation.json`,
`00_chapter_normalized.md`) were re-read in full from `output9/ch11` rather than trusted from the
prior report's narrative, `13_merged.json` was independently rebuilt field-by-field from those
eleven inputs per `reference/phase2_contract.md`'s merge table, and the rebuild was diffed against
the standing `13_merged.json` — the two are identical (the only difference was this agent's draft
script defaulting `publication_id` to `null`; the standing file's `1` is correct — see Gaps). Every
Section A–D item, every `json_contract.md` invariant, the exercise/media/publication cross-checks
and the two previously-reported non-blocking gaps were re-run programmatically against the current
files (script sweep, word counts, id-grammar regex, registry-resolution, figures_of_speech
verbatim, moralising/label term sweep, spoiler sweep) rather than re-asserted from memory — see each
section below for what was actually run. Nothing upstream had changed since the prior pass;
**`13_merged.json` is confirmed still correct and is re-emitted unchanged (byte-identical).**

## A–D (blocking)   **PASS**

**A — Diagnosis and lens.** `01_meta.json` records all four `genre_signals` (structure, theme,
exercises, purpose) read off the three rendered pages, quoting the કૃતિ-પરિચય's own line
("લઘુકથા સાહિત્યપ્રકારમાં લાઘવ અને અંતે આવતી ચોટનું અત્યંત મહત્વ છે") as evidence, never as the
verdict; `genre_confidence: high`. `_genre_index.md` routes લઘુકથા to `varta` — matches
`active_genre_profiles: ["varta.md"]`. Explanation unit is ઘટના-wise per the profile's own લઘુકથા
note ("two or three topics is the normal answer… the final ચોટ line may hold a topic of its own
even though it is one sentence") — the four printed `[[ઘટના: …]]` markers became four
`STORY_TELLING` topics (re-counted programmatically against `00_chapter_normalized.md`: 4 `[[ઘટના:`
markers, 4 STORY_TELLING topics), none merged, none split, and the ચોટ (`M2.S4.T6`) was not opened
early (re-verified below by string-search, zero hits). `04_validation.json` (`status: "pass"`,
`blocking: []`) already confirmed this at the 04_converged stage and was re-read, not assumed.
`guiding_question` is chapter-derived (names મોહન, મગન, રામશંકરનો વારસો specifically) and is
answered by reading `M2.S2.T3 → M2.S4.T6` in order. Apparatus stayed apparatus: શબ્દ-સમજૂતી,
ભાષા-અભિવ્યક્તિ, શિક્ષકની ભૂમિકા, and both સ્વાધ્યાય-mislabelled sub-headings Agent 1 correctly
re-filed as શબ્દ-સમજૂતી sub-blocks — none became a topic or an exercise-inventory item; std-9's
લેખક-પરિચય/કૃતિ-પરિચય became the two allowed CONCEPT topics (T1, T2).

**B — Verbatim and structure.** A fresh whitespace-normalized substring check placed every one of
the six `original_chunk` fields inside `00_chapter_normalized.md` verbatim — including the
ellipses, the colon-for-comma at "...ફોડી લેશું:'", and the source line `('અક્ષત'માંથી)` folded
inside the **last** topic's (`M2.S4.T6`) `original_chunk`. A regex sweep over every display field
of the assembled `13_merged.json` (`topic_name`, `explanation`, `real_life_example`, both
summaries+`detailed_summary`, `concept_bullets`, `important_points`, every `recall_questions[]`
prompt/answer, all outside bracketed technical terms) found **zero** Roman characters, **zero**
Devanagari characters, and **zero** `।` anywhere in the file — the same sweep confirmed
`original_chunk` itself is pure Gujarati script (U+0A80–0AFF) on all six topics. Marker accounting,
re-counted directly off `00_chapter_normalized.md`: six reading markers (`[[લેખક-પરિચય]]`,
`[[કૃતિ-પરિચય]]`, four `[[ઘટના: …]]`) each became exactly one topic; the four `[[સ્વાધ્યાય: …]]`
blocks became zero topics. Ids consecutive (`M1.S1.T1`–`T2`, `M2.S2.T3`, `M2.S3.T4`–`T5`,
`M2.S4.T6`, checked programmatically T1..T6 in order); every `depends_on` edge resolves to a real
node; every `concept_id` is chapter-continuous and equals its topic number (`M1.S1.T1.C1` …
`M2.S4.T6.C6`, checked 1..6 by regex).

**C — The teaching block.** All six topics carry non-empty `explanation` and `real_life_example`.
Re-computed word counts (Python `str.split()`): `explanation` 80/81/81/83/82/73,
`real_life_example` 74/72/77/82/83/85 — every topic inside the 55–90 band. `objective_text` runs
23–29 words across O1–O5 (re-counted), all inside the 12–30 band. Three-tier summaries strictly
increase by word count on all six topics (re-checked programmatically; brief < summary < detailed
on every topic). Every `explanation` demonstrably adds beyond `modified_chunk`'s plain seed —
motive (T3: "આ જ ખૂટતો પુરાવો આગળ જતાં આખી વાર્તાને ગૂંચમાં નાખશે"), craft naming (T5, T6),
consequence (T6: "વારસો બોલમાં નહિ, પસંદગીમાં દેખાયો"). `real_life_example` anchors rotate domain
scene-to-scene (shopkeeper-singer, ડાયરાની વાત, ઘરકામ-મદદનીશ, શેરી ક્રિકેટ, લખોટીની રમત,
પ્રામાણિક દુકાનદાર-દીકરો) — single, Indian, in-standard, each closing on a question to the child.

**D — સ્વરૂપ essence.** `07_pitfalls.json` instantiates `varta.md`'s avoid-list against this
chapter's own six topics (8 `hard` `avoid_checks` across T2–T6, plus a chapter-level note on the
તાકેલો બોધ item and one open cross-reference item), and every `hard` item was re-checked this pass
directly against the merged, authored content:

1. **Summary-only teaching — clear.** Every STORY_TELLING explanation (T3–T6) adds motive, craft
   or consequence beyond `modified_chunk`.
2. **Tacked-on બોધ — clear.** A fresh string search for `શીખવે છે`, `જોઈએ`, `બોધ એ છે`, `ઉપદેશ`, and
   the શિક્ષકની ભૂમિકા box's own phrases (`સંસ્કારપિંડ`, `સાચી મૂડી`, `ઋણ`, `રઘુકુલ`) across every
   `explanation`, `real_life_example`, all three summaries, `concept_bullets`, `important_points`,
   every `recall_questions[].prompt`/`.answer` and every `concepts[].content[]` block on all six
   topics returned **zero hits**. The શિક્ષકની ભૂમિકા box's own moralising (teacher-addressed
   apparatus) was correctly never imported into the teaching-facing prose as if it were the
   story's own statement.
3. **Judging a sympathetic character — clear.** A fresh string search for evaluative labels
   (લુચ્ચો, દગાખોર, સ્વાર્થી, ખરાબ, ગુનેગાર, બદમાશ, ધુતારો, જુઠ્ઠો, લોભી, શ્રીમંત, જમીનદાર) across
   the same field set returned **zero hits**. `08_sensitivity.json`'s soft caution against a
   landlord-vs-tenant class reading is honoured — T4/T5's `explanation` and `real_life_example`
   stay on individual choice (a childhood promise, a game's stakes), never generalising to a class.
4. **Spoiling the turn early — clear, with one scoping decision recorded.** `07_pitfalls.json`
   draws the line explicitly: `M1.S1.T2` (કૃતિ-પરિચય) is the **book's own printed pre-story
   synopsis** and states the outcome inside its own `original_chunk` — that is not a pipeline
   spoiler, it is what the page prints before the narrative begins. The gate instead binds to the
   three STORY_TELLING topics that actually precede the ચોટ (`M2.S2.T3`, `M2.S3.T4`, `M2.S3.T5`): a
   fresh string search of their `explanation`, `summary`, `detailed_summary` and every
   `recall_questions[].answer` for `કાયદેસર મગનને નામે`, `હું રામશંકરનો દીકરો છું`, and `'મોહ'ને
   હડસેલ` found **zero hits** in any of the three. One genuine near-miss (already named in the
   prior pass) persists and is re-confirmed rather than silently dropped: T5's paraphrase of
   Mohan's line ("આજથી આ જમીન કાયદેસરની તારી થઈ ગઈ" — second person, addressed to મગન in the
   printed original) into third-person indirect speech ("જમીન કાયદેસર **એની** જ થઈ ગઈ") leaves the
   pronoun's referent ambiguous between મગન and મોહન if that one sentence is read in isolation.
   Read directly this pass: T5's `explanation` does end on the bare pronoun, but T5's own
   `detailed_summary` ("આ ક્ષણે વાચકને લાગે છે કે મગન સાવ હારી ગયો") and `RQ3`'s answer resolve the
   ambiguity toward the correct surface (menacing) reading in the **same topic** — so the ચોટ is
   not spoilt, but the `explanation` field alone would read ambiguously if isolated. **Reported,
   not blocking** (see Gaps) — unchanged from the prior pass because no authoring agent has
   touched T5 since.
5. **Debunking a પૌરાણિક કથા** — not applicable; not a mythological sub-form.
6. **Standardising લોકકથા dialect** — not applicable; the one તળપદો word on the page (`ટાઢ`) is
   glossed, never replaced, and dialogue is not dialect-heavy.
7. **Inventing what the excerpt doesn't contain** — no field narrates an event outside the six
   `original_chunk`s; every `real_life_example` is clearly an external analogy.
8. **Crediting a translator as author** — not applicable; no અનુવાદ credit is printed.

**Craft-naming ceiling (std-9 canon) — re-checked this pass, an open pack-level policy question,
not a per-chapter defect.** `M2.S3.T5` and `M2.S4.T6` name `યમક`, which `reference/alankar_chhand.md`'s
measured table places in the **std-10** canon (std-9's seven are વર્ણાનુપ્રાસ, પ્રાસસાંકળી, ઉપમા,
રૂપક, ઉત્પ્રેક્ષા, વ્યતિરેક, અતિશયોક્તિ). This pass re-read both source files directly rather than
trusting the prior summary: `alankar_chhand.md`'s own "Provisional" section states the completed
std-9 inventory shows its ભાષા-અભિવ્યક્તિ boxes "pre-name devices beyond the std-9 canon above
(યમક, સજીવારોપણ, વક્રોક્તિ, વિરોધાભાસ)" and calls reconciling the two "an open VERIFY-4-class review
item." Set against that, `profiles/students/std-9.md` §1.4/§6 explicitly names **this exact
device** — "the std-9 book's own ભાષા-અભિવ્યક્તિ bullets name it (and વ્યતિરેક, યમક). Rule used
here: teach the device the chapter's printed apparatus names, on the line that carries it; the
ladder is a prior, the page is the authority" — which is precisely what this chapter's own
page-48–49 box does (it prints "ઉપમા અને યમક અલંકારનો મિશ્ર અર્થ" and "યમક અંલકાર" by name, sic).
Given the pack's own authority files disagree and the std-9-specific file explicitly permits this
exact case, this agent does not manufacture a chapter-blocking failure out of a genuinely open
design question — this is **PASSED through the std-9.md §6 exception**, and the conflict is carried
forward verbatim in Gaps below and in `07_pitfalls.json`'s `chapter_level` notes for whoever
resolves VERIFY-4.

**Contract mechanics — all re-run programmatically on the current `13_merged.json`, all PASS:** 31
root keys (32 minus `ordering`, which is Agent 14/15's) match `output9/ch01`'s accepted shape
key-for-key; 37 topic keys (31 + the 4 ભાષા-બોધ extras + `figures_of_speech`/`rhyme_scheme`) match
on every topic, and a full key-set sweep found no stray working field (no `note`, `avoid_checks`,
`misconception`, `correction`, or media score survived the merge on any topic or module);
`strand_to_objective_map` covers L1–L5 exactly once, each resolving to the matching `O{n}`; every
`home_topic_id` and every `anchor[]` id resolves to a real node; every topic's `objective_ids`
resolves to the registry; every `learning_objectives[]` entry mirrors its root `objective_text`
character-for-character; `concept_id`s are chapter-continuous 1..6 and equal their topic number;
every `recall_questions[]` id is `{topic}.RQ{n}` / `{topic}.TR{n}` — never `.SR{n}`; `MEDIA_ID_RE`
holds on all 4 media nodes and each is concept-scoped correctly; `estimated_exchanges` is a string
on every topic; `word_count` carries only `{"original": …}`; every `figures_of_speech[].lines`
(ઉપમા, and both યમક entries) is found byte-for-byte inside its own topic's `original_chunk`;
`rhyme_scheme: null` and `overall_rhyme_scheme: null` throughout (ગદ્ય, correctly). No numbers found
in any display field or in any `objective_text` (regex-swept this pass across
`topic_name`/`explanation`/`real_life_example`/summaries/bullets/RQ prompt+answer/objective_text).
A full-file substring check for `।` found none anywhere in `13_merged.json`.

**Publication (Agent 16).** All six topics carry `publication_text`; `publication_chunk` starts
with a byte-identical copy of `original_chunk` on all six (re-checked with `str.startswith`, not
just eyeballed); `concept_publication` supplies one entry per **paragraph** content block (2 of
each topic's 3 content blocks — the third is a `list` block, correctly not re-authored), and the
count of `publication_text`-bearing blocks equals the paragraph-block count on every concept; a
fresh search for `બાળકો` and the vocative `જુઓ —` inside every `publication_text` returned zero
hits.

## E–G (reported)

- **E — Exercises: clean.** `10_exercise_solutions.json.coverage_report`: all 4 inventoried blocks
  (MCQ ×4, બે-ત્રણ વાક્યોમાં ×2, સવિસ્તાર ઉત્તર ×2, વિદ્યાર્થી-પ્રવૃત્તિ ×1 = 9 items, EX1–EX9)
  re-verified against `01_meta.json`'s `exercise_inventory` heading-for-heading and count-for-count;
  `unanswered: []`, `unmapped: []`; every `covered_by_topics` entry resolves to a real topic id. The
  single વિદ્યાર્થી-પ્રવૃત્તિ bullet is correctly marked `is_model_answer: true`.
- **E — Sensitivity: clean.** `08_sensitivity.json` flags `M2.S3.T4`/`M2.S3.T5` (area: સંઘર્ષ,
  severity: soft) against a landlord-vs-tenant class reading, plus a chapter-level guidance note;
  both are encoded as `07_pitfalls.json` checks (see D3 above) and both topics' `explanation`/
  `real_life_example` stay on individual choice, never a class or community label (re-confirmed by
  the zero-hit label sweep above).
- **G — usual failure modes: none observed.** No merged-topic દુહા/કડી issue (pure prose). No
  પદ-ટેક issue. No poetic licence silently corrected (ગદ્ય). No invented અલંકાર (both `યમક` entries
  and the `ઉપમા` entry are on the page, verbatim-checked). No adult- or foreign-pitched
  `real_life_example`. No સ્વાધ્યાય block cut as a teaching topic.

## Media

`09_media.json.reuse_report`: `scenes: 4`, `authored: 4`, `reused: 0`, `rejected: []` — matches the
four ઘટના topics whose `available_content_types` carry `"image"` (re-counted: 4 STORY_TELLING
topics carry `image`, 4 media nodes exist, one per topic, one-to-one); the two CONCEPT intro topics
correctly carry none. Each of the four media nodes depicts a single photographable moment (the
gift, the pressure, the trembling signature, the reveal); character appearance (Ramshankar, Magan,
Mohan, the two સ્વજનો) is held consistent field-to-field across all four prompts; `teaching_notes`
on each explicitly withhold the next beat; every `image_url` is `""` with a non-empty,
self-contained `generation_prompt` (re-checked programmatically — no empty prompt, no reused-frame
stamp); `negative_prompt` names "Devanagari script labels" on all four; `2d_tool: null` chapter-wide
(re-counted: 0). Setting is rural Gujarat throughout (mud-brick farmhouse, neem tree, pagh,
dhoti-kurta), not generic.

## Gaps

- **`publication_id: 1`** is carried in `13_merged.json` as the pack-wide provisional placeholder
  (matching every other output9 chapter checked this pass: ch01, ch03–ch10 all currently write `1`)
  — this is **not** a verified GSEB publication row; `json_contract.md` rule 1 is explicit that
  CBSE's `1` "does not transfer." The field is non-null (satisfying the server's hard rejection of
  `null`) but remains a placeholder pending the real GSEB row lookup at VERIFY-2, exactly like
  `chapter_master_id`/`subject_ref_id` below. Not blocking this agent's gate — recorded so Phase 8
  does not mistake it for a verified value.
- **T5's `explanation` carries an ambiguous pronoun** ("જમીન કાયદેસર **એની** જ થઈ ગઈ") where the
  original's second-person address ("...**તારી** થઈ ગઈ") is clearer. Not blocking — the ambiguity
  resolves correctly within the same topic's `detailed_summary` and `RQ3` — but worth a one-clause
  fix at the next authoring touch (owner: A12; see `07_pitfalls.json`'s `M2.S3.T5` entry for the
  exact wording). Unchanged since the prior pass — no owner re-run has touched A12's T5 explanation.
- **The std-9 canon-ceiling question for `યમક` (T5, T6) is genuinely unresolved pack-wide**, not
  just in this chapter: `reference/alankar_chhand.md`'s measured table and its own later
  "Provisional" note point one way; `profiles/students/std-9.md` §1.4/§6 — naming this exact device
  — points the other way and is what this chapter followed. `alankar_chhand.md` itself calls the
  reconciliation "an open VERIFY-4-class review item." Recorded here, in `07_pitfalls.json`'s
  `chapter_level`, and already in `12_authoring.json`'s `notes[1]`. This chapter's pass is **not**
  contingent on that resolution, per the std-9.md §6 exception it is currently following.
- `11_pages.json`: `textbook_pages: "47–49"`, confidence **medium** — the range was read directly
  off the end-page renders and agrees with `std-9/manifest.json`'s offset; std 9's own cover page
  has not yet been read to confirm the textbook title independently of the running-head string.
  `textbook_url` is a local PDF path — no hosted URL exists yet.
- `chapter_master_id` / `subject_ref_id` remain `null` pending the GSEB server lookups
  (VERIFY-1/VERIFY-2) — expected, correctly left unresolved rather than guessed.
- `depends_on` is `[]` on `M2.S2.T3` and `M2.S3.T4` rather than an explicit edge to the immediately
  preceding topic (sequencing is carried by tree order instead) — cosmetic, matches sibling
  chapters, already noted at `04_validation.json`.
- The printed typo/asymmetry between page 47's "હડસેલતા કહ્યું" and page 49's ભાષા-અભિવ્યક્તિ box's
  "હડસલતા કલ્યું" / "યમક અંલકાર" was correctly left as printed (sic) throughout, per
  `gujarati_verbatim.md`.
- `05b_textbook_order.json` is identical to the logical traversal order in both files. Per
  `phase2_contract.md`'s "Ordering — LP2 has only one" section, this is expected to raise
  `human_confirmation_required` once Agents 14/15 emit the two ordering files — noted here so it is
  not lost before that stage.

## LP2 validator

Not attempted — this pack has not reached Phase 8 for this chapter. `13_merged.json` passes every
mechanical contract check this agent can run offline (see "Contract mechanics" above, all re-run
this pass rather than carried over from the prior report); the live
`POST /api/lp2/learning-plans/validate` round trip is Phase 8's job.

## LP2 validator (Phase 8)

Validation Result:
```json

```


## LP2 validator

Status: FAILED

Validation Errors:
1. root: missing required field 'plan_id'
2. root: missing required field 'chapter_id'
3. root: missing required field 'objectives'
4. root: chapter_id '' must match {board}_{medium}_{subject}{grade}_ch{N} (phase-3 plans append '_V3', e.g. 'cbse_eng_sci6_ch4_V3')
5. root: 'estimated_time' is required and must not be null
6. topic M1.S1.T1: objective 'O1' not found
7. topic M1.S1.T2: objective 'O1' not found
8. topic M2.S2.T3: objective 'O2' not found
9. topic M2.S3.T4: objective 'O3' not found
10. topic M2.S3.T5: objective 'O4' not found
11. topic M2.S4.T6: objective 'O5' not found



Full Response:
```json
{
  "success": false,
  "action": "validated_only",
  "plan_id": null,
  "version": null,
  "phase": null,
  "is_active": null,
  "is_draft": null,
  "counts": null,
  "diff": null,
  "publication_id": null,
  "publication_name": null,
  "validation_errors": [
    "root: missing required field 'plan_id'",
    "root: missing required field 'chapter_id'",
    "root: missing required field 'objectives'",
    "root: chapter_id '' must match {board}_{medium}_{subject}{grade}_ch{N} (phase-3 plans append '_V3', e.g. 'cbse_eng_sci6_ch4_V3')",
    "root: 'estimated_time' is required and must not be null",
    "topic M1.S1.T1: objective 'O1' not found",
    "topic M1.S1.T2: objective 'O1' not found",
    "topic M2.S2.T3: objective 'O2' not found",
    "topic M2.S3.T4: objective 'O3' not found",
    "topic M2.S3.T5: objective 'O4' not found",
    "topic M2.S4.T6: objective 'O5' not found"
  ],
  "message": "11 validation error(s)"
}
```
