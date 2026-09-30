# Validation Report — std 9, ch 06 ભાષા જાય તો સંસ્કૃતિ જાય

સ્વરૂપ: ચિંતનાત્મક નિબંધ (વિચારનિબંધ; સમવાદ-નિબંધ, single-voice arm) (confidence: high)   explanation unit: તર્કનો એક તંતુ (એક લંડન-મુલાકાત-ઘટના, અથવા દલીલનું એક પગલું)
Topics: 13   Objectives: 13   Images: 0/3   Exercises: 8/8 (3/3 blocks)

**This run's verdict: FAIL.** This is the RE-QC (final) pass, run independently against every
input file rather than against the prior report's conclusions. The prior pass's own re-run fix
(the two numbered-label renames and the SMS-example digit fix, all confirmed still in place) holds
and is not re-litigated here. But a fresh, literal re-check of every Section-D hard `avoid_check`
in `07_pitfalls.json` against the *current* `12_authoring.json` text — not against the previous
report's summary of it — turns up one hard item that does not hold. That is a blocking failure by
this gate's own rule: "A run with any A–D failure is not complete, however good the rest looks,"
and the prior report's PASS on this exact section was wrong to close it.

## The blocking failure

**Topic `M3.S3.T7` (દીકરો ગુજરાતી બોલશે, વાંચશે કે વાપરશે ખરો ?) — `real_life_example` fails its
own hard `avoid_check` in `07_pitfalls.json`.**

The check reads: *"real_life_example must not frame a child's own weaker spoken/written Gujarati
(a real possibility for this pack's L2 reader) as a personal failing; it must land on one small,
doable action this week, never a field that ends on inadequacy with no next step."*

The field as written:

> "...લંડનવાળા દીકરાની જેમ સાવ છોડી દેવાની વાત નથી, પણ ફેર ધીરે ધીરે પડતો જ જાય છે. ગુજરાતી
> વાંચવા-લખવામાં તમને પોતાને ક્યાં સૌથી વધારે અટકવું પડે છે — બોલવામાં, વાંચવામાં કે લખવામાં ?"

This closes by asking the reading child, directly, where *they themselves* stall most in Gujarati
— exactly the "own weaker Gujarati" self-diagnosis the check forbids ending on — and offers no
action for the child to take. Compare the same chapter's own `M2.S2.T3`, which the same class of
check ("must land on one specific, doable, non-blaming action") *does* satisfy: "...હવે પછી ઘરમાં
કોઈ વડીલ ગુજરાતીમાં વાત કરે ત્યારે તમે એક વાર થોભીને, ધ્યાનથી સાંભળશો — શું સંભળાય છે ?" — a named
future action (pause and listen next time), not a self-assessment of where the child is weak.
`M3.S3.T7` needed the same shape and does not have it.

This is a content defect, not a merge defect — `13_merged.json` correctly carries
`12_authoring.json`'s text unchanged (re-verified field-by-field, zero drift). **Owner: A12**
(`agents/12_runtime_authoring.md`) — rewrite `M3.S3.T7.real_life_example` to close on one small,
doable, non-blaming action the child can take this week (in the register this chapter already
uses at `M2.S2.T3`/`M2.S2.T5` — e.g. asking a parent or elder to correct one written word, or
reading one Gujarati sentence aloud slowly this week), keeping the anchor Indian, single, and
inside the 55–90 word band. The orchestrator should re-run the minimal set (A12 → this gate) once
that field is rewritten.

Every other hard `avoid_check` in `07_pitfalls.json` (24 of 25 items across the other 12 topics,
including the two hardest — `M3.S5.T11`'s hypothetical-objector attribution and `M4.S6.T13`'s G2
second-person-imperative gate) was re-checked individually against the current authored text and
holds. All three `08_sensitivity.json` hard items (`M2.S2.T5`, `M3.S5.T10`, `M3.S5.T12`, all area
ધર્મ) hold. No other Section-D or Section-B/C item failed.

## A–D (blocking), item by item

**A — Diagnosis and lens: PASS.** `04_validation.json` records `genre_fidelity.pass: true`.
Independently re-checked: the 13 content markers in `00_chapter_normalized.md`
(`[[લેખક-પરિચય]]`, `[[કૃતિ-પરિચય]]`, 3×`[[ઘટના: …]]`, 7×`[[તર્ક: …]]`, 1×`[[સંવાદ: …]]`) map 1:1,
in order, to topics `M1.S1.T1`…`M4.S6.T13`; the three `[[સ્વાધ્યાય: …]]` markers correctly became
zero topics. `explanation_unit` matches the `samvad_nibandh.md` single-voice-નિબંધ row, and this
chapter is that profile's own cited anchor per `01_meta.json`. `guiding_question` is
chapter-specific and answered by reading the 13 topics in order. Apparatus (શબ્દ-સમજૂતી,
વિદ્યાર્થી-પ્રવૃત્તિ, ભાષા-અભિવ્યક્તિ, શિક્ષકની ભૂમિકા) stayed apparatus; લેખક-પરિચય/કૃતિ-પરિચય
correctly became the two CONCEPT topics per the std-9 allowance.

**B — Verbatim and structure: PASS.** All 13 `original_chunk` fields non-empty; a codepoint sweep
of every one (bracket-stripped) finds zero Latin and zero Devanagari characters — this essay is
ગદ્ય and needs no bracketed technical terms — and zero `।`. Ids run consecutively M1–M4 / S1–S6 /
T1–T13 / C1–C13. No header furniture in any chunk; no `[[સ્વાધ્યાય: …]]` block became a topic.

**C — The teaching block: PASS.** Every topic has non-empty `explanation` and `real_life_example`;
word counts re-measured programmatically on `13_merged.json`: `explanation` 69–85 words,
`real_life_example` 65–86 words, all 13 inside the 55–90 band; `objective_text` O1–O13 run 17–26
words, inside 12–30. L2 calibration held (તત્સમ-heavy words glossed inline at first use; the
Hindi false-friend મોટો/મોટી glossed once at first occurrence per the chapter-level pitfall note).

**D — સ્વરૂપ essence: FAIL — see above.** With that one exception, no બોધ is forced onto the
essay anywhere; the author's own thesis is reported as his claim, never re-issued as an
instruction. `figures_of_speech` is `[]` on 12 of 13 topics and carries one entry on `M3.S5.T11`
(વર્ણાનુપ્રાસ), re-checked programmatically against that topic's `original_chunk` and found
verbatim. `rhyme_scheme` is `null` and module `difficult_words`/`overall_rhyme_scheme` are
empty/null throughout — correct for ગદ્ય.

**Contract — 12/12 invariants hold on `13_merged.json`.** Registry consistency verified by script
(every `objective_id` unique; every topic's `objective_ids` resolves to O1–O13; every
`home_topic_id` and `anchor[]` entry resolves to a real node; `strand_to_objective_map` covers
every `legacy_id` exactly once); inline `learning_objectives[]` mirrors match root
`objective_text` character-for-character on all 13 topics; `MEDIA_ID_RE` matches all 3 media ids,
each concept-scoped correctly; `recall_questions[]` ids are `{topic}.RQ{n}` /
`legacy_id` `{topic}.TR{n}` on all 39 recall questions, never `.SR{n}`; `concept_id`s are
chapter-continuous and equal the topic number; three-tier summaries strictly increase in word
count on all 13 topics; zero digit characters found in any authored display field this rule scopes
(`topic_name`, `explanation`, `real_life_example`, all three summaries, `concept_bullets`,
`important_points`, `concepts[].content[]` text/items, `recall_questions[].prompt`/`.answer`).
`publication_id` is `1`, non-null.

## E–G (reported)

- **E — Exercises:** `10_exercise_solutions.json.coverage_report` — `blocks_found`/`blocks_answered`
  both list all 3 inventoried blocks (MCQ×4, બે-ત્રણ વાક્યોમાં×2, છ-સાત વાક્યોમાં×2 — 8 items),
  `unanswered: []`, `unmapped: []`. EX4 (the cross-chapter MCQ naming four book titles as options)
  is answered from this chapter's own text alone, with the other titles flagged unverifiable in
  `teacher_note` rather than guessed.
- **F — Shape:** `chapter_id`/`plan_id` follow the pack's provisional VERIFY-1 form. One item did
  not hold cleanly — see Gaps §1 below (reported, not blocking: this rule sits in qc_checklist.md
  Section F, and the instance is inside `publication_chunk`, not inside any field this run's
  Contract-9 digit sweep scopes).
- **G — the seven usual mistakes:** none observed. Genre held as ચિંતનાત્મક નિબંધ throughout — no
  degeneration into સાર+બોધ+પ્રશ્નોત્તર; no ઘટના split from its setup; no biographical fact invented
  about ફાધર વાલેસ beyond `M1.S1.T1`'s own printed કૃતિ-પરિચય; the one `figures_of_speech` entry is
  verbatim-checked; no `real_life_example` set outside India or pitched off std 9 (the one D-section
  failure above is a missing "next step," not a wrong setting or standard).

## Media

`09_media.json.reuse_report`: `scenes: 3, authored: 3, reused: 0, rejected: []` — matches exactly
the 3 topics (`M2.S2.T3`, `M2.S2.T4`, `M2.S2.T5`) whose `available_content_types` carry `"image"`
in `05_with_content.json`. All 3 media nodes carry `image_url: ""` and a non-empty, self-contained
`generation_prompt`; `negative_prompt` includes `Devanagari script labels` on all three, plus a
scene-specific addition on `M2.S2.T5` ("religious idol or altar, devotional worship imagery,
temple iconography") matching that topic's ધર્મ sensitivity note. `2d_tool: null`. No fabricated
`image_url`, no `[reused frame: …]` stamp anywhere. `0/3` is the correct, expected ratio.

## Gaps

1. **`16_publication.json`'s `publication_chunk` for `M3.S4.T8` still carries the pre-fix SMS
   example (`'kem 6'`) inside its appended rewrite of `real_life_example`,** a literal digit
   character sitting in reader-facing text. Root cause, confirmed by file mtimes:
   `16_publication.json` (01:29) was generated *before* `12_authoring.json`'s later re-run (01:51)
   corrected this same example to `'kem cho' ને બદલે 'kmcho'`, and 16 was never re-run afterward,
   so its snapshot of `real_life_example` is stale on this one topic. This is **reported, not
   blocking** — it is not one of the fields Contract invariant 9's digit sweep scopes
   (`explanation`, `real_life_example`, summaries, bullets, prompts, recall answers;
   `publication_text`/`publication_chunk` are not named in that list, and the merged plan's
   `real_life_example` itself is clean) — but it is a genuine, fixable staleness, not a
   documentation footnote to leave standing indefinitely. **Owner: A16**
   (`agents/16_publication_authoring.md`) — resync `16_publication.json` against the current
   `12_authoring.json` (at minimum, regenerate `M3.S4.T8`'s `publication_text`/
   `publication_chunk`/`concept_publication` entry) once the A12 fix above has also landed, so both
   fixes go out in the same re-run rather than two.
2. **`publication_chunk` contains `original_chunk` as a byte-identical prefix, then
   `publication_text`, then a de-personalised rewrite of `real_life_example` — it is not, as a
   whole, byte-identical to `original_chunk`.** This gate's own spec text (and
   `reference/json_contract.md`) say "byte-identical"; `agents/16_publication_authoring.md`
   defines the field as "the publication-facing version of the topic's block as a whole" with
   "the verbatim `original_chunk` stays verbatim *inside* it," and `PORTING_BRIEF.md` restates the
   same containment design as the thing to keep. Checked structurally on all 13 topics this run:
   the verbatim prefix is byte-identical and untouched, the appended prose adds no fact or reading
   beyond what `explanation`/`real_life_example` already state, drops every vocative and direct
   second-person question, and `concept_publication` maps one entry per topic to the one
   `paragraph`-type content block by index, correctly skipping `list`-type blocks. This matches the
   documented, pack-wide convention (`output6`–`output10`, most chapters) and is not treated as a
   new blocking item here — but it is the same standing spec-wording conflict every other chapter
   in this pack has carried, still unresolved at the reference-file level (one chapter,
   `output7/ch15`, was previously edited the other way, to strict whole-field equality — the two
   conventions have not been reconciled and a human should pick one wording and fix
   `agents/13_assembly_validation.md`/`reference/json_contract.md` or
   `agents/16_publication_authoring.md` to match it, chapter-pack-wide, not chapter by chapter).
3. **`publication_id`/`chapter_master_id` remain unresolved server-side lookups (VERIFY-2)** — a
   standing precondition of upload shared by every chapter in the pack, not this run's blocker.
4. **Board/medium segments in `chapter_id`/`plan_id` are provisional until VERIFY-1** — standing
   note shared by every chapter.
5. **`textbook_url` is a local PDF path** — no hosted URL exists yet for the GSEB readers.
6. **`11_pages.json` confidence is `medium`** — the folio numbers themselves are legible at 150 dpi
   and cross-checked against `manifest.json`'s std-9 row, but the std-9 cover page has not been
   read/confirmed against the board profile (a standing std 8–9 gap, not specific to this chapter).
7. **`topic_number` is `null`** in `01_meta.json`/root `13_merged.json` — Agent 1 recorded no value
   for this chapter (`output9/ch02` carries the same `null`); not invented here.

## LP2 validator

Not run this pass — no network call is available to this agent. Do not submit `13_merged.json` to
`POST /api/lp2/learning-plans/validate` until the `M3.S3.T7` fix above lands and this gate re-runs
to PASS — this run's own rule is that an A–D failure makes the plan not complete, whatever the
rest of the file looks like.
## LP2 validator

**Timestamp:** 2026-08-29 21:00:15 UTC

**Result:** VALID (no validation errors)

**Response:**
```json
{
    "success": true,
    "action": "validated_only",
    "plan_id": "gseb_eng_gujarati9_ch6_v1",
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

