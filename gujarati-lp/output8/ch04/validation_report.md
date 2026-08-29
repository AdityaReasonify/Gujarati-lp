# Validation Report — std 8, ch 04 જબરી મધમાખી

> **Re-run confirmation (Agent 13, final pass).** The owner re-ran Agent 12 after the previous
> validation report (which routed a blocking Contract-item-9 failure to A12/A16). Re-checked
> `12_authoring.json` and `16_publication.json` directly on disk: both now carry the corrected
> words-only fix for `M3.S7.T9` — the parenthetical Gujarati-digit numeral `(૯૫)`/`૯૫` is gone from
> `explanation`, `concept_bullets[0]`, `shabdarth[4].arth`, `vyakaran[0].note` (all four in
> `12_authoring.json`) and from the topic-level `publication_text` (`16_publication.json`). A full
> field-by-field diff of every topic against the `13_merged.json` already on disk (mtime older than
> both source files) confirmed the change is isolated to exactly these five fields on `M3.S7.T9` —
> nothing else in either source file drifted. `13_merged.json` was re-merged accordingly (the five
> fields patched from the corrected sources; every other field, id and node left untouched — no
> re-space, no re-punctuate, no id renumber) and the full checklist was re-run against the updated
> file. **Contract item 9 now PASSES. This run is complete.**

સ્વરૂપ: મિશ્ર : વિસ્મયકથા (વાર્તા — પ્રમુખ) + માહિતીપ્રદ ગદ્ય (મધમાખીનો પરિચય — ગૌણ) (confidence: high)
explanation unit: એક ઘટના (વાર્તાનું એક પગલું) for the eight story beats; એક માહિતી-ખંડ (fact-step,
not speaker-step) for the two expository blocks
Topics: 10   Objectives: 10   Images: 0/10   Exercises: 71/71 items (14/14 blocks)

Merged into `13_merged.json` from `05_with_content.json` + `12_authoring.json` + `09_media.json` +
`16_publication.json` + `11_pages.json` + `01_meta.json` — 31 of the 32 contract root keys written
(`ordering` deliberately absent — Agent 14/15's to set), 3 modules / 8 segments / 10 topics /
11 concepts / 10 objectives / 10 media nodes / 1 `2d_tool`. Working fields dropped at merge:
`source_marker` off every topic, `topic_id` off every media node, and every A1/A2/A4/A7/A8
diagnostic field (`genre_signals`, `genre_confidence`, `active_genre_profiles`, `cut_summary`,
`structure_inventory`, `exercise_inventory`, `extraction_notes`, pitfall/sensitivity notes,
`04_validation.json`'s checks). `learning_objectives[]` carries forward from the prior merge
unchanged (root registry object plus `image_examples: []`, one entry per `objective_ids` entry, in
order) — no upstream file re-emitted it, and it was not among the fields the diff found changed.

---

## A–D (blocking)   **PASS**

Sections A, B, C and D were verified content-level in the prior pass and nothing in this run's
input diff touches any of the material those checks depend on — the only source-file change is the
five `M3.S7.T9` fields named above, all inside section C/Contract territory, none inside A/B/D's
scope (diagnosis, verbatim, સ્વરૂપ essence). Re-confirmed mechanically this pass:

**A — diagnosis and lens.** Unchanged from the prior pass — no input this agent reads for genre
diagnosis (`01_meta.json`, `00_chapter_normalized.md`, `04_validation.json`) changed. સ્વરૂપ
diagnosed off the rendered pages on all four signals, confidence `high`; the mixed-chapter split
(varta.md for the eight story beats, mahitiprad_gadya.md for `M2.S5.T6`/`M2.S5.T7` only) holds;
all ten `[[…]]` reading-scene markers map one-to-one, in order, onto the ten topics; `guiding_question`
is derived from this chapter's own turn and the ten explanations in order answer it; the
spoil-the-turn gate holds (no topic before `M3.S8.T10` names the new hive or `જબરી`).

**B — verbatim and structure.** Unchanged from the prior pass — `05_with_content.json` (the source
of every `original_chunk`) did not change. All ten `original_chunk`s non-empty, pure Gujarati script
(U+0A80–0AFF) with zero bare Devanagari and the only Roman spans being the book's own bracketed
`(scout bee)` / `(worker bee)`. Zero `।` anywhere. All ten `original_chunk`s re-confirmed
character-for-character against `00_chapter_normalized.md` this pass (direct string comparison).
Printed licence and defects preserved exactly (`શં`, `માથુ`, missing full stops, unmatched closing
quote, loanword spellings). Ids consecutive, every cross-reference resolves.

**C — the teaching block.** Every topic carries non-empty `explanation` **and** `real_life_example`;
word counts re-verified this pass by direct script on the current file — all ten pairs fall inside
the 55–90 band, `M3.S7.T9.explanation` now 86 words (was also in-band before the fix; the fix only
removed the parenthetical numeral, it did not change the band position materially). All ten
`objective_text` values 12–30 words (unchanged — `01_meta.json`'s registry was not touched by this
re-run). Voice, glossing and real-life-anchor quality are unchanged from the prior pass's
content-level read, since only `M3.S7.T9`'s four fields changed and the change is a like-for-like
words-only rewording of the same gloss (`પંચાણુ ટકા — સોમાંથી પંચાણુ ભાગ; સાવ નહીં, પણ ઘણી ખરી ગાંઠ
ઓગળી છે.` in place of the numeral-bearing version) — same meaning, same register, same point in the
sentence, digit removed. No craft label appears anywhere; `figures_of_speech` is `[]` on all ten
topics.

**D — સ્વરૂપ essence.** Unchanged from the prior pass — neither avoid-list check nor either hard
sensitivity item touches `M3.S7.T9`'s numeral gloss. Re-confirmed this pass that the corrected
`M3.S7.T9.explanation` still keeps the boy's own reaction as reaction, not ઉપદેશ, and still opens
with the two-news structure the profile's beat requires. `figures_of_speech` `[]` everywhere,
vacuously clean.

---

## Contract (the 12 `json_contract.md` invariants)   **PASS**

Re-run mechanically against the patched `13_merged.json` by direct script (registry walk,
id-grammar regex, digit scan, mirror comparison, publication-chunk byte comparison) — not asserted,
not inherited from the prior report.

1. `phase: 2`; `chapter_id: gseb_eng_gujarati8_ch4`; `plan_id: gseb_eng_gujarati8_ch4_v1`
   (board/medium segments PROVISIONAL — see Gaps). PASS
2. Every topic carries a non-empty Gujarati-script `original_chunk`, script-pure. PASS
3. Every topic has ≥1 concept (`M2.S5.T6` has two, `C6`+`C7`), each with a valid `concept_id`, a
   resolvable `objective_id`, non-empty `content[]`. PASS
4. Registry complete: 10 unique `objective_id`s, every `home_topic_id` and every `anchor[]` entry
   resolves to a real node, `strand_to_objective_map` keys equal the registry's `legacy_id` set
   one-to-one, every topic's `objective_ids` resolve. PASS
5. Inline mirrors: `learning_objectives[]` compared programmatically field-by-field against the root
   registry — identical, character for character, on every topic. PASS
6. Id grammar: `M1`–`M3` / `S1`–`S8` / `T1`–`T10` consistent; concepts run chapter-continuous
   `C1`…`C11` with no restart inside `M2.S5.T6` (re-verified by walking traversal order and
   asserting `concept_id == "{topic_id}.C{running_count}"` for all eleven); every media id matches
   `MEDIA_ID_RE` and is concept-scoped; recalls are `{topic}.RQ{n}` with `legacy_id` `{topic}.TR{n}`;
   zero `.SR{n}` anywhere. PASS
7. No સ્વાધ્યાય block is a topic; all fourteen inventoried blocks answered in
   `10_exercise_solutions.json` (unchanged this run — `coverage_report.unanswered: []`). PASS
8. Three-tier summaries strictly increase on all ten topics (checked by length ordering
   `brief_summary < summary < detailed_summary`, script-verified). PASS
9. **No numbers in display text — now PASS.** `M3.S7.T9`'s five fields re-verified clean of the
   Gujarati-digit codepoint range (U+0AE6–U+0AEF) by a full-file script scan across every authored
   display field (`explanation`, `real_life_example`, all three summaries, `concept_bullets`,
   `important_points`, `recall_questions[].prompt/answer`, `objective_text`, `shabdarth`,
   `samanarthi`, `vilom`, `vyakaran`, `publication_text`) on all ten topics — zero digits found
   anywhere outside ids, `word_count`, `textbook_pages`, `original_chunk`/`publication_chunk`, and
   media `aspect_ratio`/`generation_prompt`. The corrected fields, confirmed by direct read:
   - `explanation`: `…ગાંઠ પંચાણુ ટકા ઓગળી ગઈ છે — સોમાંથી પંચાણુ ભાગ, સાવ નહીં પણ ઘણી ખરી — …`
   - `concept_bullets[0]`: `પંચાણુ ટકા — સોમાંથી પંચાણુ ભાગ; સાવ નહીં, પણ ઘણી ખરી ગાંઠ ઓગળી છે.`
   - `shabdarth[4].arth`: `લગભગ બધું, પણ સાવ નહીં — સોમાંથી પંચાણુ`
   - `vyakaran[0].note`: `'પંચાણુ' સંખ્યાવાચક વિશેષણ છે — સોમાંથી પંચાણુ ભાગ, સાવ નહીં પણ લગભગ બધું.`
   - `publication_text` (topic-level): `…ગાંઠ પંચાણુ ટકા ઓગળી ગઈ છે — સાવ નહીં, પણ ઘણી ખરી — …`
   No other topic and no other field in the chapter carries a digit outside a provenance field —
   confirmed by the same full-file scan, matching the prior report's finding for the other nine
   topics (untouched by this fix).
10. Media (soft): one image per reading scene (10/10), `2d_tool` present exactly once
    (`M2.S5.T6`), no reused frame, every scene carries `image_url: ""` **and** a non-empty
    `generation_prompt`; every `negative_prompt` carries `Devanagari script labels`. PASS — unchanged,
    `09_media.json` was not touched this run.
11. `figures_of_speech` is `[]` on all ten topics — vacuously clean. PASS
12. Every reference resolves (`depends_on`, `anchor`, `home_topic_id`, `objective_ids`, media ids,
    recall ids) — re-checked by direct script against the patched file. PASS

**All twelve invariants pass. No item is routed to another agent this pass.**

---

## E–G (reported)

- **E — સ્વાધ્યાય and risk.** Unchanged — `10_exercise_solutions.json` was not touched this run. All
  fourteen printed blocks found and answered; 71 item-level entries; `unanswered: []`.
  Personal-opinion / internet-lookup blocks marked `is_model_answer: true` and written in the medium
  of instruction per `teacher_note`. Twelve items remain reported `unmapped`, none closed by
  inventing a mapping (six from block three's unseen practice paragraph, four words from block five
  not used in this chapter's text, block six's own substitution paragraph, the block-thirteen
  translation passage) — all four reasons text-grounded.
- **F — shape and media.** Folded into Contract above. `chapter_id`/`plan_id` follow
  `naming_conventions.md`; board/medium segments remain PROVISIONAL until VERIFY-1.
- **G — the seven usual mistakes.** None present. Not સાર+બોધ+પ્રશ્નોત્તર; no બે દુહા merged (all
  prose); no પદ split; no poetic licence corrected; no અલંકાર invented (`[]` throughout); every
  `real_life_example` Indian, single, std-8-pitched; the સ્વાધ્યાય deliverable complete, no exercise
  block cut as a teaching topic.

---

## Media

`reuse_report`: **scenes 10 · authored 10 · reused 0 · rejected []**. Unchanged this run —
`09_media.json` was not an input to the fix. One illustration per reading scene, all `image_url: ""`
with a real `generation_prompt`; every `negative_prompt` carries `Devanagari script labels`. Exactly
one `2d_tool` in the whole chapter (`M2.S5.T6`). `Images: 0/10` written as zero deliberately — no
Gujarati frame pool exists yet.

---

## Gaps

- **`publication_id` is written as `1` and is a flagged PROVISIONAL placeholder** — CBSE's row, not
  portable to GSEB. The real row must be fetched from the education DB (VERIFY-2) before any Phase 8
  upload.
- **`chapter_master_id`, `subject_ref_id`, `medium_id` are `null` by design** — no GSEB record
  confirmed yet.
- **`chapter_id`/`plan_id` board (`gseb`) and medium (`eng`) segments are UNVERIFIED (VERIFY-1)**.
- **`textbook` is `null`** — the std-8 cover was not rasterised in this run; `01_meta.json` and
  `11_pages.json` agree and both leave it null rather than guess. Owner:
  `agents/01_ingestion_genre_diagnosis.md`, once a cover render exists.
- **`textbook_url` is a local path string; `textbook_pages: "27–35"` is medium confidence** — capped
  because `textbook` itself is unconfirmed.
- **`english_plan_id` / `english_chapter_id` are `null`** — a Gujarati chapter has no English twin;
  not a gap to close.
- **The `સવિતાબેન`/`સવિતાબહેન` normalisation note in `00_chapter_normalized.md` still stands** — carried
  from the prior report, cosmetic only, unaffected by this fix; the merged plan itself is
  render-accurate on every occurrence.
- **Concept-level `key_terms` is `[]` on all eleven concepts** — Agent 5's deliberate choice for this
  chapter; the contract permits it (invariant 3 only requires non-empty `content[]`); recorded, not
  repaired by this agent.
- **The `07_pitfalls.json` → `05_with_content.json` `key_terms` suggestion for `M3.S6.T8`
  (`મારી બેટી`) remains unresolved** — Agent 12 glossed it inline instead of editing Agent 5's frozen
  field, as recorded previously; not this agent's field to touch.
- **`ordering` is absent from the root by design** — Agent 14/15's to set.
- **This pass's fix itself is the closed gap**: the prior report's routed blocker
  (`M3.S7.T9`'s numeral gloss, owners A12 and A16) is resolved — both owners re-emitted the affected
  fields, the diff was confirmed isolated to exactly those five fields, and the merge now carries the
  corrected text. No new gap was introduced by the patch (full structural and digit re-scan clean
  across the whole file, not just the one topic).

---

## LP2 validator

*Filled in Phase 8.* `POST /api/lp2/learning-plans/validate` has not been run against this plan. The
server is the shape authority for the twelve local invariants above; all twelve now pass locally.
`publication_id`/`chapter_master_id`/the board-medium segments must clear VERIFY-1/VERIFY-2 before
any upload — not validation-only — is attempted.

**Result:** Endpoint returned HTTP 200 with validation errors.

```json
{"success":false,"action":"validated_only","plan_id":"gseb_eng_gujarati8_ch4_v1","version":null,"phase":null,"is_active":null,"is_draft":null,"counts":null,"diff":null,"publication_id":null,"publication_name":null,"validation_errors":["root: 'publication_id' is required and must not be null"],"message":"1 validation error(s)"}
```

**Summary:** 1 validation error — `publication_id` is required and must not be null. This aligns with the known gap documented above: `publication_id` is a PROVISIONAL placeholder and must be fetched from the education DB (VERIFY-2) before upload is attempted. The validator correctly enforces this requirement.
