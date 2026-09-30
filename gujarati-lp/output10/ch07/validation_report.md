# Validation Report — ધોરણ 10, એકમ 7 — જીવમાં જીવ આવ્યો

સ્વરૂપ: સૉનેટ (`sonnet.md`, confidence: **high**)
explanation unit: એક ભાવ-ખંડ — 14 પંક્તિ, જજમેન્ટ-કટ ચાર ભાવ-ખંડમાં (T2 1–4 · T3 5–8 · T4 9–12 · T5 13–14) + એક પરિચય-ટોપિક

Topics: 5 (M1.S1 = 1 · M1.S2 = 4)   Objectives: 5   Images: 0/4   Exercises: 11/11 items across 5/5 blocks

---

## RE-QC note (this pass)

This is a re-gate after an owner re-run. The prior pass (this file, before this run) **FAILED on
Publication**: `16_publication.json`'s `publication_chunk` carried the verbatim block with the
rewritten `explanation` and `real_life_example` appended after it on all five topics, instead of
being byte-identical to `original_chunk`, and `13_merged.json` was withheld per this agent's own
"name the owner and stop" rule.

**A16 has since re-run.** `16_publication.json` was re-read this pass and its `publication_chunk`
is now confirmed byte-identical to `05_with_content.json`'s `original_chunk` on all five topics
(programmatic length + character comparison, not just a visual check):

| topic | len(original_chunk) | len(publication_chunk) | match |
|---|---|---|---|
| M1.S1.T1 | 873 | 873 | ✓ |
| M1.S2.T2 | 156 | 156 | ✓ |
| M1.S2.T3 | 161 | 161 | ✓ |
| M1.S2.T4 | 183 | 183 | ✓ |
| M1.S2.T5 | 106 | 106 | ✓ |

`publication_text` and `concept_publication` were unchanged by A16's re-run (as expected — they
were never the defect) and still hold. Every other section below was independently re-verified
against this pass's own copies of the input files (not carried forward from the prior report
unchecked), since a merge is now actually being emitted.

---

## A–D (blocking)   **PASS**

### A — Diagnosis and lens.   PASS
`genre_signals` (structure/theme/exercises/purpose, in `01_meta.json`) are read off the rendered
pages; the chapter's own કૃતિ-પરિચય line naming both સ્વરૂપ and છંદ
(`"...કવિએ આ સોનેટમાં મંદાક્રાન્તા છંદમાં પ્રગટ કર્યો છે"`) is quoted **as evidence**, never as the
verdict, and `genre_confidence: "high"` is independently corroborated by `04_validation.json`.
`explanation_unit` (એક ભાવ-ખંડ) matches `sonnet.md`'s "two to four, four is the ceiling" rule — the
cut lands on sentence boundaries (પૂર્ણવિરામ/ઉદ્ગારચિહ્ન at lines 2, 4, 6, 8, 12, 14), not on the
seven printed couplets, and the last two lines (the returning title line) live together in the
final topic, `M1.S2.T5` — the ચોટ is not split. Std-10's unlabelled કવિ-પરિચય + કૃતિ-પરિચય pair is
folded into one CONCEPT topic (`M1.S1.T1`), per the std-10 apparatus exception and this pack's own
ch01/ch03/ch09 precedent. Apparatus stayed apparatus: શબ્દ-સમજૂતી (5 sub-heads), all five
`[[સ્વાધ્યાય: …]]` blocks, ભાષા-અભિવ્યક્તિ and શિક્ષકની ભૂમિકા carry no topic; no revision checkpoint
or વ્યાકરણ એકમ applies. `guiding_question` is this chapter's own (વગડો/સીમ/માણસો, quoted from the
poem's own imagery) and `M1.S1.T1 → T2 → T3 → T4 → T5` in order answers it.

### B — Verbatim and structure.   PASS
All five `original_chunk`s are non-empty, Gujarati-script only. Re-run this pass: a programmatic
scan of every authored field (explanation, real_life_example, summaries, bullets, recall Q/A,
shabdarth, samanarthi, vilom, vyakaran, figures_of_speech notes, rhyme_scheme, media title/
description/teaching_notes, publication_text) finds **zero** Devanagari codepoints and **zero**
stray Roman characters outside brackets — the one hit (`ST`, unbracketed, in
`M1.S1.T1.real_life_example`) is reviewed under Gaps, not a verbatim defect (it never touches
`original_chunk`; `ST બસ` is this pack's own established unbracketed idiom, also used unbracketed
in `reference/teaching_voice_gu.md`'s own anchor bank and in `output10/ch09/13_merged.json`).
`M1.S1.T1`'s `original_chunk` (કવિ-પરિચય + કૃતિ-પરિચય, joined `\n\n` with the `[[…]]` marker line
dropped) and all four poem topics' `original_chunk`s are each found byte-for-byte inside
`00_chapter_normalized.md`. Poetic/dialectal forms are intact and uncorrected — `થૈ`, `ટ્હૌકી`,
`લૈને`, `ફૂટું ફૂટું ફરફર` (never `ફૂટ્યું ફૂટ્યું`) — every one glossed as the poem's own કાવ્ય-રૂપ,
never flagged as a misprint, exactly matching `07_pitfalls.json`'s hard `avoid_checks` on
`M1.S2.T2`/`T3`/`T4`. The attribution line `(‘સૂરજ કદાચ ઊગે’માંથી)` sits inside `M1.S2.T5`'s
`original_chunk` on its own line, correctly identified as provenance (this સોનેટ prints no છાપ).
No `[[સ્વાધ્યાય: …]]` block became a topic. Ids run consecutive and chapter-continuous
(`M1` → `S1`/`S2` → `T1`…`T5` → `C1`…`C5`, `c = t` throughout). Header furniture (the QR code
`D2V7IZ`) was never transcribed. છंદ naming: `મંદાક્રાન્તા` appears exactly once
(`M1.S1.T1.original_chunk`, echoed once in `modules[0].overall_rhyme_scheme`) — no other છંદ name
and no માત્રા/ગણ count anywhere.

### C — The teaching block.   PASS
All five topics carry non-empty `explanation` and `real_life_example`. Word counts (all inside
55–90, recomputed programmatically this pass): `M1.S1.T1` 80/75 · `M1.S2.T2` 74/72 · `M1.S2.T3`
88/81 · `M1.S2.T4` 78/79 · `M1.S2.T5` 85/73. `objective_text`: O1 24 · O2 22 · O3 24 · O4 24 · O5
23 words, all inside 12–30. No band was widened. `explanation` glosses hard words at first use
inline (`ડમરી`, `ઠરીઠામ`, `વ્યથિત`, `નીડ`, `પરણ`, `રાફડો`, `લંગાર`, `જડિત`, `વગડો`, `સીમ`,
`ઘૂઘવવું`, `મ્હોરવું`, `નમણાં`, `છતાંયે`) and holds the L2 calibration — ordinary-but-L2-hesitant
words (`આઘે-ઓરે`, `અડખે-પડખે`) are glossed even though colloquially unremarkable. `real_life_example`
is Indian, concrete, single per topic, and rotates domain across the chapter (ST-bus/family relief
→ tin-roof monsoon → milk boiling over → village મેળો → પટોળું's two-sided truth — the last
matching `profiles/students/std-10.md`'s own named std-10 anchor for "holds two truths at once").
Four of five end on a direct question to the child. Craft is named only once (`સજીવારોપણ` on
`M1.S2.T4`, quoting lines found verbatim in that topic's own `original_chunk`, re-checked
programmatically this pass — full-string and line-by-line substring match both true) and છंદ
(`મંદાક્રાન્તા`) only where the book itself prints it — the std-10 ceiling.

### D — સ્વરૂપ essence.   PASS
Checked line-by-line against every `07_pitfalls.json` item (all hard except one soft on
`M1.S2.T2`) — `08_sensitivity.json` reports `none_found: true`:
- No field "corrects" `થૈ`, `ટ્હૌકી`, or `ફૂટું ફૂટું ફરફર` — all three verified glossed as કાવ્ય-રૂપ,
  never as misprints, on every field that touches them.
- `figures_of_speech` names `સજીવારોપણ` exactly once (`M1.S2.T4`), matching the soft avoid-check on
  `M1.S2.T2` (must stay empty there) — confirmed `[]` on T1/T2/T3/T5.
- No field converts `M1.S2.T5`'s ચોટ into an `આપણે … જોઈએ`-shaped instruction (programmatic scan of
  every field for `જોઈએ`/`બોધ`/`ઉપદેશ` returns zero hits); the closing return of the title line is
  described throughout as circular closure (`વર્તુળાકાર સમાપન`), never a ટેક or ધ્રુવપંક્તિ.
- No છंદ name beyond `મંદાક્રાન્તા`, no biographical fact about હરિકૃષ્ણ પાઠક beyond વતન/નોકરી/the six
  named books, and no content taught from the un-printed companion poem `'મેહુલા'` (named only as a
  suggested pairing inside `M1.S1.T1`'s own `original_chunk`) — all confirmed absent everywhere,
  including in the now-regenerated `publication_chunk`/`publication_text`.
- No government scheme/campaign (દા.ત. જળસંચય અભિયાન) is named anywhere; the ચોટ is never inflated
  into a water-conservation appeal — checked against `EX8`'s `teacher_note` explicitly as well.

### Contract — the 12 invariants.   PASS, all 12 (re-verified programmatically against `13_merged.json` itself)
1. `chapter_id = gseb_eng_gujarati10_ch7`; `plan_id = gseb_eng_gujarati10_ch7_v1`. ✓
2. All five `original_chunk`s non-empty, Gujarati-script only outside brackets. ✓
3. Every topic has ≥1 concept; all five concepts carry a valid `objective_id` resolving to the root
   registry and non-empty `content[]` (2 blocks each). ✓
4. Registry complete: 5 unique `objective_id`s; every `home_topic_id` and `anchor[]` entry resolves;
   `strand_to_objective_map` covers L1–L5 one-to-one with O1–O5; every topic's `objective_ids`
   resolve. ✓
5. `learning_objectives[].objective_text` matches the root registry character-for-character on all
   five topics (checked in code, not by eye). ✓
6. Id grammar: all four media ids match `MEDIA_ID_RE`, concept-scoped, with `concept_id ==
   home_concept_id`; recall ids are `M1.S{s}.T{t}.RQ{1,2,3}` with `legacy_id` `.TR{n}` — **zero**
   `.SR{n}` anywhere. ✓
7. No સ્વાધ્યાય block is a topic; all 5 inventoried blocks (11 items) are answered in
   `10_exercise_solutions.json` — `coverage_report.unanswered: []`, `unmapped: []`. ✓
8. Three-tier summaries strictly increase by word count on all five topics (`M1.S1.T1` 24→44→96 ·
   `M1.S2.T2` 13→34→76 · `M1.S2.T3` 18→31→80 · `M1.S2.T4` 20→40→90 · `M1.S2.T5` 18→31→84). ✓
9. **Zero** digits — Latin or Gujarati — in any authored display text (programmatic scan of every
   `topic_name`, `explanation`, `real_life_example`, every summary tier, every bullet, every recall
   prompt/answer, `objective_text`, `guiding_question`, `teaching_lens`). ✓
10. Media: 4 reading scenes carry `"image"`-shaped scenes; 4 media nodes exist, one per scene;
    `reuse_report` reads `scenes:4 / authored:4 / reused:0`; every node carries `image_url:""` and a
    non-empty, self-contained `generation_prompt`; `2d_tool: null` chapter-wide. ✓
11. `figures_of_speech` is `[]` on four topics and one entry on `M1.S2.T4`; that entry's `lines`
    string is found verbatim inside `M1.S2.T4.original_chunk` — both a full-substring match and a
    line-by-line match confirmed programmatically. ✓
12. Agent 14's renumbering has not run yet — ids are frozen and internally consistent going in
    (verified: every `home_topic_id`, `anchor[]`, `objective_ids`, media id and recall id in
    `13_merged.json` resolves to a real node). ✓

### Exercises.   PASS
All 5 groups in `01_meta.json`'s `exercise_inventory` (11 items: MCQ ×2, એક-એક વાક્યમાં ×2,
બે-ત્રણ વાક્યમાં ×2, સવિસ્તર ×2, વિદ્યાર્થી-પ્રવૃત્તિ ×3) appear as `EX1`–`EX11` in
`10_exercise_solutions.json`. `coverage_report.blocks_found` equals the inventory exactly;
`unanswered: []`, `unmapped: []`. The personal-opinion block (`EX8`, `તમારા શબ્દોમાં વર્ણવો`) and
the three વિદ્યાર્થી-પ્રવૃત્તિ items are marked `is_model_answer: true` and answered with teaching
values, never skipped. `EX8`'s and `EX7`'s `teacher_note`s explicitly bar a water-conservation /
જળસંચય બોધ-વાક્ય, cross-referencing `07_pitfalls.json`'s chapter-level check by name.

### Media.   PASS
`reuse_report`: **scenes 4 · authored 4 · reused 0 · rejected []**. Four authored scenes, one per
poem topic (`M1.S2.T2.C2.IMG1` ડમરી શમી/ફોરાં ઝર્યાં · `M1.S2.T3.C3.IMG1` રાફડો-તડકો-ધરાનું રૂપ ·
`M1.S2.T4.C4.IMG1` વગડો-સીમ-લોકોનું મિલન · `M1.S2.T5.C5.IMG1` બહાર એનું એ, અંદર જીવ આવ્યો).
`M1.S1.T1` correctly carries no media (પરિચય paragraph, not a reading scene). `2d_tool: null`. Every
`image_url` is `""`; every `generation_prompt` is self-contained (Saurashtra scrubland setting, a
fixed babul-tree/hut landscape recurring across all four so the four images read as one place, mood,
16:9, Indian setting) and names no previous image or the chapter by name. `negative_prompt` carries
`Devanagari script labels` plus a chapter-specific bar (`diagram of poem structure`,
`octave-sestet layout`, `motivational poster caption with a moral`) on every node.

### Publication.   **PASS** (fixed this pass — see RE-QC note above)
`publication_text` is present and well-formed on all five topics (no vocative or classroom
instruction survives — `બાળકો`/`જુઓ —`/`બોલો` scanned for, zero hits). `concept_publication`
correctly supplies exactly one entry per topic, matched to the `paragraph`-type content block at
`content_index: 0`. `publication_chunk` is now **byte-identical** to `original_chunk` on all five
topics (see the length table in the RE-QC note — character-for-character, not merely visually
similar). No meaning was added in the rewrite; `publication_text`/`concept_publication` read as the
same facts as `explanation`/`real_life_example` with vocatives and direct instruction removed, per
`agents/16_publication_authoring.md`.

---

## E–G (reported)

- **E — સ્વાધ્યાય and risk.** All 5 inventoried blocks (11 items) answered as `EX1`–`EX11`, each
  mapped to the topic(s) that prepare it. No block unmapped, none unanswered. `08_sensitivity.json`
  reports `none_found: true` — no sensitivity item to apply; this remains a public/collective-relief
  chapter (a village's relief at the first rain), and no field inflates it into a
  water-conservation appeal.
- **F — Shape and media.** All 12 contract invariants hold (above), including the
  byte-identical-`publication_chunk` requirement that was the sole blocker last pass. `chapter_id`/
  `plan_id` shape is correct and provisional per VERIFY-1. Four reading scenes, four media nodes,
  one per scene; `2d_tool: null`.
- **G — the seven usual mistakes.** Checked and none present: (1) no સાર+બોધ+પ્રશ્નોત્તર flattening;
  (2) not applicable — no દુહા in this સોનેટ; (3) no printed ટેક was invented, and the returning
  title line is correctly called circular closure, not a ટેક; (4) printed poetic forms (`થૈ`,
  `ટ્હૌકી`, `લૈને`) are uncorrected everywhere; (5) `સજીવારોપણ` is named exactly once, on lines that
  actually carry it — not a catalogue; (6) all five `real_life_example`s are Indian, single,
  concrete, pitched at std 10, and rotate domain; (7) no સ્વાધ્યાય block was cut as a topic.

## Media

`reuse_report`: **scenes 4 · authored 4 · reused 0 · rejected []** (full detail under the Media
check above). No media defect found.

## Gaps

- `textbook_url` is a **local path** (`../Textbooks-pdf/std-10/ch-07-jivma-jiv-avyo.pdf`) — the
  GSEB readers have no hosted URL.
- `textbook_pages: "39–41"` at confidence **high** (`11_pages.json`) — printed folio and the
  manifest row agree (std-10 offset N+5). No pagination gap.
- `chapter_master_id: null`, `publication_id: 1` (this pack's standing CBSE-derived placeholder,
  kept for pack-wide consistency, not derived or invented fresh — see `output10/ch01`,
  `output10/ch09` for the same value). Both fields must be resolved from the education DB at
  **VERIFY-2** before any upload.
- `chapter_id`/`plan_id`'s board and medium segments (`gseb`/`eng`) are **provisional until
  VERIFY-1**.
- `medium_id` and `subject_ref_id` are `null` by contract (server-injected). `english_plan_id` and
  `english_chapter_id` are `null` — a Gujarati chapter has no English twin.
- `ordering: null` — deliberately left for Agent 14/15.
- **`05b_textbook_order.json` matches the logical traversal exactly** (`M1.S1.T1 → M1.S2.T2 → T3 →
  T4 → T5` both ways). Per `phase2_contract.md`'s own instruction, raised rather than silently
  skipped:
  ```jsonc
  {"human_confirmation_required": true,
   "reason": "textbook order is identical to logical order",
   "checked": "05b_textbook_order.json matches the logical traversal exactly"}
  ```
- `M1.S1.T1`'s `real_life_example` uses the unbracketed Roman abbreviation **`ST`** (`તમારાં બા ST
  બસમાં પાછાં ફરવાનાં...`) — reviewed, not flagged as a script-purity defect. `ST બસ` is this pack's
  own established, unbracketed idiom for "State Transport bus," used exactly this way in
  `teaching_voice_gu.md`'s own anchor bank and in `output10/ch09`'s own already-shipped
  `13_merged.json`. Flagged for a human reviewer's visibility, not blocked — no such instance exists
  in any `original_chunk`.
- `01_meta.json`'s own `extraction_notes` records a prior corpus-file transcription of the
  કૃતિ-પરિચય's cross-reference name as `સ્વ. રામનારાયણ પાઠકનું(?)`, superseded by this chapter's own
  400dpi re-render, which reads unambiguously `સ્વપ્નસ્થનું`. Not re-litigated by this agent — Agent
  5/13 do not re-transcribe verbatim; recorded here only because it is the kind of gap this report
  exists to surface.
- Working fields dropped at this merge: `genre_signals`, `genre_confidence`,
  `active_genre_profiles`, `explanation_unit`, `structure_inventory`, `exercise_inventory`,
  `extraction_notes` (from `01_meta.json`); `notes` (from `05_with_content.json`, `02_structure.
  json`, `12_authoring.json`); `topic_id` on each media node (redundant with `concept_id`, dropped
  per this pack's own `output10/ch01`/`ch09` precedent); `04_validation.json`'s checklist
  scaffolding; `avoid_checks`/`misconception`/`correction` from `07_pitfalls.json`.

## LP2 validator

**PASS** — Server validation completed successfully.

Endpoint: `POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate`

Response:
```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati10_ch7_v1",
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

Result: **validation_errors is empty** — learning plan is structurally valid per LP2 schema.

---

## Verdict

**PASS.** All of A–D, the 12 contract invariants, Exercises, Media, and Publication pass on this
pass's own independent, programmatic re-verification. The single defect from the prior pass
(`publication_chunk` carrying appended, rewritten prose instead of being byte-identical to
`original_chunk`) is confirmed fixed by A16's re-run — verified by direct length and character
comparison against `05_with_content.json`'s `original_chunk`, not by re-reading the old report's
claim.

`13_merged.json` is emitted this pass: one phase-2 plan, 32 root keys, 5 topics (1 CONCEPT + 4
POEM) each carrying 37 topic-level keys (the 31-key contract base plus the 6 કાવ્ય extras), 5
concepts, 5 objectives, 4 media nodes, 5 recall-question sets (15 total), and `publication_text`/
`publication_chunk` on every topic. Ready for Agent 14 (renumbering / topic_type mapping to the
closed server enum) and, after that, upload.
