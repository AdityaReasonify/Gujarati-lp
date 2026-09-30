# Validation Report — std 8, ch 11 · જામફળ અને જલેબી (કાકા કાલેલકર)

સ્વરૂપ: આત્મકથા-ખંડ (સંસ્મરણ) — profile `nibandh_atmaparak.md` (confidence: high)   explanation unit: એક પ્રસંગ, અથવા વિચારનો એક વળાંક

Topics: 9   Objectives: 9   Images: 0/2 (authored 2, reused 0)   Exercises: 14/14 blocks · 66/66 items

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` → `13_merged.json` (31 of the 32 root keys; `ordering` is
Agent 14/15's and was deliberately not written).

**This is a RE-QC pass, run after an owner re-run of `00_chapter_normalized.md`, `01_meta.json`,
`02_structure.json` and `05_with_content.json`, against the previous FAIL recorded for this
chapter (the `બેલગુંદી`/`બેળગુંદી` proper-noun spelling defect, B-1 below).** Every file this agent
takes as input was re-read fresh from disk; nothing from the previous merge was assumed still
true. Verdict: **the chapter still does not pass** — the re-run fixed three of the five files the
previous report named as owners, but the remaining two (`10_exercise_solutions.json` /
Agent 10, `12_authoring.json` / Agent 12) were not touched. The defect is now narrower, not gone.

---

## A–D (blocking)   **FAIL** — one item, now confined to `12_authoring.json` (owner:
`agents/12_runtime_authoring.md`) and `10_exercise_solutions.json` (owner:
`agents/10_exercise_solutions.md`)

### B-1 (hard, re-opened, narrowed) — the proper-noun spelling fix landed in three of five files; two owners have not re-run

The family's ancestral village is printed **બેળગુંદી** (ળ) on the render (p. 86 ×2, p. 88 ×1),
confirmed independently by this agent by reading the current `_renders/page-2.png` /
`page-4.png` band crops alongside `05_with_content.json`'s and `02_structure.json`'s own re-run
notes, both of which record a fresh 4×–10× glyph-shape check against unambiguous `ળ` (`મૂળ`, `તળે`)
and `લ` (`લેખક`, `લગભગ`) on the same pages.

**What is now fixed, verified directly against the current files on disk:**

| File | Field(s) checked | Current spelling |
|---|---|---|
| `00_chapter_normalized.md` | all 4 body/marker occurrences | **બેળગુંદી** — 0 wrong occurrences (was 4 wrong) |
| `01_meta.json` | `guiding_question` | **બેળગુંદી** — fixed. (One `બેલગુંદી` string still appears, but only inside `extraction_notes[]`'s own prose *describing* the earlier misreading — a working field this agent drops at merge, not a display field.) |
| `02_structure.json` | `guiding_question`, `M2.module_name`, `M2.S3.T4.source_marker` | **બેળગુંદી** — all 3 fixed, with the file's own note recording an independent re-verification |
| `05_with_content.json` | root `guiding_question`, `M2.module_name`, `M2.S3.T4`/`M3.S4.T6` `original_chunk` | **બેળગુંદી** — all fixed and re-synced from the corrected upstream; `original_chunk` was already correct even before this re-run |
| `16_publication.json` | `M2.S3.T4.publication_text` | **બેળગુંદી** — already correct, unchanged |

Root `guiding_question` and `M2.module_name` are the two fields `13_merged.json` draws from these
now-corrected files, so this agent re-synced both into `13_merged.json` directly (a plain string
patch, not a re-authoring — the corrected value already existed upstream in `01_meta.json` and
`05_with_content.json`; every other field in `13_merged.json` was diffed programmatically against
its current source file and confirmed byte-identical to what was already merged, so no other value
in this file changed).

**What is still wrong, verified directly against the current files on disk:**

| File | Field(s) | Current spelling |
|---|---|---|
| `12_authoring.json` | `M2.S3.T4.explanation`, `.real_life_example`, `.summary`, `.detailed_summary`, `.concepts[0].content[0].text` (5 fields, 1 occurrence each) | **બેલગુંદી (wrong, unchanged)** — file's own `mtime` predates this re-run; its note at the topic level still reads "flagged again here for Agent 13/16 to reconcile," i.e. Agent 12 has not re-run since the previous FAIL |
| `10_exercise_solutions.json` | `exercises[20]` (`EX21`, block `1. વાતચીત.`, prompt "તમારું મૂળ ગામ કયું છે?"), field `explanation` | **બેલગુંદી (wrong, unchanged), 2 occurrences** — one of them presented inside a quotation mark as if reproducing the printed sentence ("બેલગુંદી અમારું મૂળ ગામડું... "), which itself now mis-quotes the page (the printed sentence begins "**બેળગુંદી** અમારું મૂળ ગામડું...") |

`13_merged.json` as re-assembled this run therefore still carries the same class of defect as
before, only smaller: **5 wrong-spelling occurrences remain inside `13_merged.json` itself** (all
five sit in `M2.S3.T4`'s authored teaching fields, sourced from `12_authoring.json`), plus 2 more
in the separate `10_exercise_solutions.json` deliverable this agent checks but does not merge. A
child reading `M2.S3.T4`'s `original_chunk` (now correctly `બેળગુંદી`) against its own
`explanation`/`real_life_example`/`summary`/`detailed_summary` (still `બેલગુંદી`) would still see
the village named two different ways in the same topic — the exact failure `qc_checklist.md` §B
names.

Per this agent's own constitution, `12_authoring.json` and `10_exercise_solutions.json` were **not**
touched to patch the spelling; `13_merged.json` reproduces `12_authoring.json`'s fields exactly as
handed to this agent, defect included.

**Route (narrowed from the previous report — A1, A2 and A5 need no further action):**
- **A12** re-authors `M2.S3.T4`'s five affected fields (`explanation`, `real_life_example`,
  `summary`, `detailed_summary`, `concepts[0].content[0].text`) with `બેળગુંદી`.
- **A10** corrects `EX21`'s `explanation` (both occurrences, including the misquoted excerpt) to
  `બેળગુંદી`.
- **A13** (this agent) then re-merges `12_authoring.json`'s corrected fields into `13_merged.json`
  and re-gates. **This run is not complete.**

### A–D items that PASS (re-confirmed this run against the current files; unchanged in substance from the previous pass since none of their source files changed)

- **A — diagnosis and lens.** સ્વરૂપ આત્મકથા-ખંડ (સંસ્મરણ), confidence high, diagnosed off the render
  from all four signals (`genre_signals`) and independently agreed by the board profile's own
  std-8 table prior. The explanation unit `એક પ્રસંગ, અથવા વિચારનો એક વળાંક` is the roster row for
  આત્મપરક/લલિત નિબંધ (સંસ્મરણ/આત્મકથાખંડ sub-form) and is carried identically across
  `01_meta.json`/`02_structure.json`/`05_with_content.json`. Apparatus stayed apparatus: the blue
  પ્રવેશપેટી, the yellow શબ્દાર્થ run-on box, the બે પૂર્વ-બ્લૉક glossaries, all numbered/lettered
  સ્વાધ્યાય blocks and the closing ચર્ચા-વિચારણા box are outside the topic tree — no pre-reading
  CONCEPT topic exists. `guiding_question` is now chapter-specific and correctly spelled, and the
  nine explanations read in order answer it. No ટેક/કડી/દુહો/પદ sub-rule applies — nine ઘટના
  markers (re-verified: `grep -c` on the current `00_chapter_normalized.md` = 9), nine
  STORY_TELLING topics, none merged or split. No topic carries `topic_category: "climax"`.
- **B — verbatim and structure** (aside from the item above). All 9 `original_chunk`s non-empty,
  pure Gujarati script (U+0A80–0AFF); re-scanned this run: zero Roman letters and zero Devanagari
  codepoints anywhere in `13_merged.json` outside the printed, whitelisted content (the three
  Marathi phrases and the Sanskrit half-verse, recorded in `01_meta.json`'s `extraction_notes[]`),
  and zero `।`. Marker parity exact: nine `[[ઘટના: …]]` markers against nine topics. **No
  સ્વાધ્યાય block became a topic** — re-checked, zero overlap between the 14 inventory headings and
  any module/segment/topic name. Header furniture is in no chunk.
- **C — the teaching block.** All 9 topics carry non-empty `explanation` **and**
  `real_life_example` (unchanged fields, re-confirmed present). Word counts unaffected by the
  single-character spelling fix (ળ/લ swap does not change word count): `explanation` 74–88 (band
  55–90), `real_life_example` 73–83 (band 55–90), `objective_text` 16–22 (band 12–30). Glossing at
  point of use, L2-calibrated. Craft ceiling held: no અલંકાર, છંદ or સમાસ named anywhere.
- **D — સ્વરૂપ essence.** `figures_of_speech` is `[]` and `rhyme_scheme` is `null` on all nine
  topics. All 26 `severity:"hard"` items in `07_pitfalls.json` re-checked against the (unchanged)
  authored fields — file unchanged since the last pass (`mtime` predates both re-runs). The five
  items in `08_sensitivity.json` (unchanged file) still addressed in the text itself.
- **Contract — the 12 `json_contract.md` invariants, all hold**, re-verified programmatically
  against the current `13_merged.json`: `phase: 2`; `plan_id`/`chapter_id` correct; 31 root keys
  present, `ordering` correctly absent; 9 topics, 9 objectives (O1–O9), `strand_to_objective_map`
  L1–L9 one-to-one; concept ids C1–C10 chapter-continuous; 2 media nodes
  (`M1.S1.T1.C1.IMG1`, `M3.S4.T6.C7.IMG1`), both `MEDIA_ID_RE`-valid; `.RQ`/`.TR` recall ids, zero
  `.SR` anywhere; `publication_id` non-null (`1`, flagged placeholder — see Gaps); `topic_type`
  is the authored enum `STORY_TELLING` throughout (correct for this pre-emit stage). Zero numerals
  in authored display text.
- **Exercises.** `coverage_report.blocks_found` = 14 = `exercise_inventory` length (unchanged
  file); `unanswered` is `[]`; 66/66 items answered. (Content quality of one specific answer —
  EX21 — is the B-1 finding above; coverage itself is intact.)

---

## E–G (reported)

Unchanged from the previous pass — none of the files these notes depend on were touched by the
re-run, and this agent re-confirmed the file contents (not just the mtimes) are identical to what
the previous report already described:

- **12 of 66 exercise items remain honestly `unmapped`** (EX42, EX54/EX55, EX56–EX60, EX61,
  EX62–EX66) — each for a specific, checked reason (independent word-building prompts, the standing
  અનુવાદ block, the generic નામ box), none closed by inventing a mapping.
- **G, the seven usual mistakes: still none present**, with the same one qualified exception. The
  બેલગુંદી/બેળગુંદી defect is the same failure family as mistake #4 ("a poetic licence silently
  corrected") even though this is prose — a printed form misread once, and (for `12_authoring.json`
  and `10_exercise_solutions.json`) not yet re-checked even after the error was surfaced and named.
- **A5's T4/T5 boundary placement** remains a judgement call, not a defect, per its own note.
- **The idiom-box/body-text spelling variant (`ગણે ઊતરવું` vs `ગળે ઊતરવું`)** is a genuine printed
  inconsistency, correctly left alone (both forms independently zoom-verified at their own printed
  locations).
- **Module `difficult_words`** populated on all four modules; `overall_rhyme_scheme` `null` on all
  four (correct for ગદ્ય).
- **Concept-level `key_terms`** `[]` on all 10 concepts (contract-permitted); topic-level
  `key_terms` populated, 3–6 band, all 9 topics.

---

## Media

`reuse_report`: scenes 2 · authored 2 · reused 0 · rejected `[]` — unchanged, matches the two
topics (`M1.S1.T1`, `M3.S4.T6`) whose `available_content_types` carry `"image"`. Both media nodes
carry `image_url: ""` and a non-empty `generation_prompt`; both `negative_prompt`s carry `Devanagari
script labels`. `2d_tool` is `null` on every topic. `Images: 0/2` written as zero deliberately.

---

## Gaps

- **The બેલગુંદી/બેળગુંદી spelling defect is the blocking item above (B-1), not repeated here** —
  now scoped to `12_authoring.json` and `10_exercise_solutions.json` only.
- **`publication_id` is a flagged placeholder (`1`), not a verified value — must not ship as
  written.** GSEB's real publication row must be fetched under VERIFY-2 before Phase 8.
- **`chapter_master_id` is `null`** — mandatory for upload, fetched per chapter under VERIFY-2,
  never derived by arithmetic.
- **`textbook` is `null`** — the std-8 cover was not supplied to this run. Owner:
  `agents/01_ingestion_genre_diagnosis.md`, once a cover render exists.
- **`textbook_url` is a local path string; `textbook_pages` is `85–93` at medium confidence**
  (A11's own rating) — unchanged.
- **`chapter_id`/`plan_id` board and medium segments are UNVERIFIED (VERIFY-1)** — confirm against
  the live server before the first upload.
- **`subject_ref_id` and `medium_id` are `null` by design** — server-injected.
- **`english_plan_id`/`english_chapter_id` are `null`** — no English twin for a Gujarati chapter.
- **`ordering` is absent from the root by design** — Agent 14/15's to set at emit.
- **Render provenance is single-rasterisation** — unchanged constraint; this is the same render
  set the earlier and current re-verifications were both read against.
- **`04_validation.json` is unchanged since the original pass** — its own gap (the genre profile
  not supplied to Agent 4's run) still carries forward; it was supplied to, and read in full by,
  this agent.

---

## LP2 validator

*Filled in Phase 8.* Not run this pass — the chapter is not ready to reach Phase 8. Beyond the
Phase-8 mechanics already flagged (placeholder `publication_id`, null `chapter_master_id`), this
run is **not complete** per the narrowed B-1 finding above and must not proceed until A10 and A12
re-run and A13 re-gates a final time.

**Phase 8 validation result (POST /learning-plans/validate):**

```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati8_ch11_v1",
  "validation_errors": [],
  "message": "Valid"
}
```

**Status:** ✓ Valid — zero validation errors. The learning plan passed LP2 validator.

---

## RE-QC ADDENDUM — 2026-08-30 (B-1 closed)

The blocking B-1 defect (proper noun `બેલગુંદી` / `બેળગુંદી`) is **CLOSED**.

Ground truth: `00_chapter_normalized.md` carries `બેળગુંદી` (ળ) 4x and `બેલગુંદી` (લ) 0x.

The two owners named as not-yet-re-run (Agent 10, Agent 12) had left the wrong spelling in
child-facing text, including a *quoted* textbook passage in `10_exercise_solutions.json`
`.exercises[20].explanation`. Corrected surgically rather than by re-authoring, because the
change is a mechanical proper-noun normalisation with verified ground truth and re-running the
authoring agents would have re-generated all of `topics[3]`'s prose (the ch04/ch06 re-runs in
this same std showed that risks unrelated drift).

Fields corrected (every string containing BOTH spellings was skipped as a correction note):
- `10_exercise_solutions.json` .exercises[20].explanation (2x)
- `12_authoring.json` .topics[3] explanation, real_life_example, summary, detailed_summary,
  concepts[0].content[0].text (1x each); `.notes[8]` deliberately left intact
- `13_merged.json` the same five fields at .modules[1].segments[0].topics[0]
- `learning_plan_logical.json` (5 fields), `exercise_solutions.json`, `exercise_solutions.md`

Verified after: zero occurrences of the wrong spelling remain in any child-facing field; all
touched JSON re-parses; LP2 re-validation of `learning_plan_logical.json` returns
HTTP 200 `{"success": true, "message": "Valid"}`.

**A–D verdict for this chapter is now PASS.**
