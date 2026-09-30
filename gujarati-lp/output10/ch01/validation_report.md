# Validation Report — ધોરણ 10, એકમ 1 — મોરલી

સ્વરૂપ: ભક્તિ-પદ (`pad_bhajan.md`, confidence: **high**)
explanation unit: એક પદ — સમગ્ર રચના એક જ એકમ

Topics: 2 (M1.S1 = 1 · M1.S2 = 1)   Objectives: 2   Images: 0/1   Exercises: 10/10 items across 5/5
blocks

**This is a RE-QC pass.** The prior gate (this same agent, earlier run) FAILED because
`12_authoring.json` and `16_publication.json` did not exist yet. The owner has since re-run
`agents/12_runtime_authoring.md` and `agents/16_publication_authoring.md`. Both now exist and are
folded into a fresh `13_merged.json`. Everything upstream of them (A1/A2/A4/A5/A7/A8/A9/A10/A11) is
unchanged and is re-confirmed below, not re-derived.

---

## A–D (blocking)   **PASS**

### A — Diagnosis and lens.   PASS
`genre_signals` (structure/theme/exercises/purpose) and `genre_confidence: "high"` sit in
`01_meta.json`, read off the rendered pages; the printed કૃતિ-પરિચય's own words are quoted **as
evidence** inside `genre_signals.purpose`, never as the verdict. `explanation_unit`
(`એક પદ — સમગ્ર રચના એક જ એકમ`) matches the actual cut: the single `[[પદ 1]]` block — `[[ટેક]]`,
`[[કડી 1]]`–`[[કડી 3]]` all nested inside it, plus the trailing `[[સ્રોત-નિર્દેશ]]` line — is one
topic, `M1.S2.T2`, never split કડી-wise. Std 10's unlabeled કવિ-પરિચય + કૃતિ-પરિચય pair is folded
into one CONCEPT topic (`M1.S1.T1`), per the std-10 apparatus exception. Apparatus stayed
apparatus: `[[શબ્દ-સમજૂતી]]` (and its three sub-heads), `[[સ્વાધ્યાય-બૅનર]]`,
`[[ભાષા-અભિવ્યક્તિ]]` and `[[શિક્ષકની ભૂમિકા]]` carry no topic. No revision checkpoint or
વ્યાકરણ એકમ applies. `guiding_question` is this chapter's own (quotes `દર્શન થકી દુઃખ ભાંગે છે`,
names મોરલી and મીરાં) and `M1.S1.T1` → `M1.S2.T2` in order answers it.

### B — Verbatim and structure.   PASS
Both `original_chunk`s are non-empty, Gujarati-script only — a programmatic scan finds **zero**
Devanagari codepoints, **zero** stray Roman characters outside the chapter's own bracketed forms,
and **zero** `।` anywhere. Both `original_chunk`s are found **verbatim, whitespace-collapsed,
inside `00_chapter_normalized.md`** (checked programmatically). Poetic licence is intact and
uncorrected: `થૈ` (not `થઈ`), `મારગ` (not `માર્ગ`); the છાપ line
`બાઈ મીરાં કે પ્રભુ ગિરિધરના ગુણ, દર્શન થકી દુઃખ ભાંગે છે.` sits character-for-character inside
`M1.S2.T2.original_chunk`; the refrain shorthand `વૃંદાવન.` is kept tab-separated and unexpanded
on every occurrence. `word_count.original` matches a fresh recount on both topics (155, 84). Ids
run consecutively and chapter-continuous (`M1` → `M1.S1`/`M1.S2` → `M1.S1.T1`/`M1.S2.T2` →
`.C1`/`.C2`, `c` = `t` on both). No `[[સ્વાધ્યાય: …]]` block became a topic. Marker arithmetic
(`[[પદ]]` = 1 = topics carrying a પદ) was fixed at Agent 4's gate and nothing since has touched
structure — not re-litigated here.

### C — The teaching block.   PASS
Both topics carry non-empty `explanation` and `real_life_example`. Word counts: `M1.S1.T1`
explanation 79 / example 75; `M1.S2.T2` explanation 84 / example 73 — all four inside the 55–90
band. `objective_text`: O1 = 15 words, O2 = 25 words, inside 12–30. No band was widened; all four
measured inside the band as written. `explanation` glosses hard words at first use inline
(`સત્સંગ`, `ભાવવાહી`, `કુંજગલી`, `ગિરિધર`, and the point-of-use `(કે = કહે)` gloss beside every
quotation of the છાપ line, answering the chapter-level L2 false-friend note in `07_pitfalls.json`).
`real_life_example` is Indian, concrete, single, inside std-10's reach, and both end on a question
to the child (`તમારા ફળિયામાં કોઈને... ?`, `તમારી શેરીમાં એવો કયો અવાજ છે... ?`). Craft is named
only where std 10 may: no અલંકાર or છંદ label appears anywhere; `rhyme_scheme` and
`overall_rhyme_scheme` describe the ટેક-કડી પ્રાસ pattern honestly (near-rhyme called out as such,
no છંદ asserted because none is printed).

### D — સ્વરૂપ essence.   PASS
Checked field-by-field against every `severity:"hard"` item in `07_pitfalls.json` and the one
`hard` item in `08_sensitivity.json`:

- **M1.S1.T1** (3 hard avoid-checks): the closing sentence of `explanation`/`detailed_summary` and
  every `recall_questions[].answer` names a concrete person/place/act from `original_chunk`
  (મીરાંબાઈ, કૃષ્ણ, વૃંદાવન, ગોપીઓ, દર્શન, મોરલી), never a general moral clause. No field states
  religion-as-fact or ranks traditions; the source's own hedge `એમ મનાય છે` is kept verbatim
  (matches `08_sensitivity.json`'s soft guidance exactly). No biographical claim beyond what the
  page prints (`original_chunk`'s સંવત 1498/કુડકી/મેડતા/રાજકુટુંબ, plus the title-block era line
  `ઈ.સ. સોળમી સદી` that `07_pitfalls.json`'s own chapter-level note whitelists as a second legitimate
  source) — no guru named, no award or movement invented. `real_life_example` is a secular anchor
  (a village દાયરો-કલાકાર known by voice), not a devotional claim.
- **M1.S2.T2** (7 hard avoid-checks): the ટેક stays inside this topic's single `original_chunk`/
  concept and is quoted verbatim in `explanation` (`વાગે છે રે વાગે છે, વૃંદાવન મોરલી વાગે છે, /
  તેનો નાદ ગગનમાં ગાજે છે.` — the same "/"-for-linebreak convention already used chapter to chapter
  in this pack for inline verse quotation); the છાપ line is quoted verbatim, as verse, with its
  `(કે = કહે)` gloss sitting **outside** the quoted span; every quoted span matches
  `original_chunk` character for character (`થૈ`, `મારગ` unmodernised); no field states what a
  religion teaches or what કૃષ્ણ is/did beyond the પદ's own reported imagery; the one media node
  names concrete elements (a flute, a tree-lined lane) and a human relationship (a listener stopped
  mid-step), and explicitly rules out an idol/પૂજા framing in its own `teaching_notes`; zero
  sentences of `explanation` name the emotion abstractly (all of it works through મોરલી, રાસ,
  પીતાંબર, કુંજગલી, નાચ, દર્શન) — the profile allows up to one, so this exceeds the bar cleanly.
  The chapter's one **hard** sensitivity item (`08_sensitivity.json`, ધર્મ) asked for a real-life
  anchor that is "a tune or a call heard across a શેરી that stops someone mid-step, never a temple
  instruction" — `real_life_example` (a ભરવાડની મોરલી heard at dusk, ફળિયાનાં છોકરાં થંભી જાય છે)
  matches this guidance almost to the word.
- `figures_of_speech: []` on both topics is a considered `[]`, not a placeholder: `12_authoring.json`'s
  own notes work through the std-9/10 canon (`વર્ણાનુપ્રાસ`, `યમક`) and correctly find neither
  settles the printed `'વાગે છે'`-repetition / `'છે'`-ending pattern — per `alankar_chhand.md`'s own
  rule ("if two labels are both arguable and the page does not settle it, write `[]`"), the
  repetition is taught unlabelled in `explanation`/`vyakaran`/`overall_rhyme_scheme` instead. No
  છંદ is named anywhere, correctly — none is printed in this chapter.

### Contract — the 12 invariants.   PASS, all 12
1. `phase: 2`; `chapter_id` = `gseb_eng_gujarati10_ch1`; `plan_id` = `{chapter_id}_v{version}`. ✓
2. Both `original_chunk`s non-empty, Gujarati-script only (checked programmatically). ✓
3. Every topic has ≥1 concept; both concepts now carry a valid `objective_id` (O1/O2, resolving to
   the registry) and **non-empty `content[]`** (2 blocks each — the blocker from the earlier FAIL
   is closed). ✓
4. Registry complete: 2 unique `objective_id`s; both `home_topic_id`s and both `anchor[]` entries
   resolve to real nodes; `strand_to_objective_map` covers L1/L2; both topics' `objective_ids`
   resolve. ✓
5. Inline `learning_objectives[].objective_text` matches the root registry character for character
   on both topics (verified programmatically; `image_examples: []` appended). ✓
6. Id grammar: media id `M1.S2.T2.C2.IMG1` matches `MEDIA_ID_RE`, concept-scoped; recall ids are
   `M1.S1.T1.RQ{1,2,3}` / `M1.S2.T2.RQ{1,2,3}` with `legacy_id` `.TR{n}` — no `.SR{n}` anywhere
   (checked programmatically). ✓
7. No સ્વાધ્યાય block is a topic; all 5 inventoried blocks (10 items) are answered in
   `10_exercise_solutions.json` — `coverage_report.unanswered: []`, `unmapped: []`. ✓
8. Three-tier summaries strictly increase on both topics, by sentence count and by word count
   (M1.S1.T1: 12 → 46 → 78 words; M1.S2.T2: 19 → 55 → 105 words). ✓
9. No digit — Latin or Gujarati — in any authored display text: scanned `objective_text`,
   `guiding_question`, `teaching_lens`, every `topic_name`, `explanation`, `real_life_example`,
   every summary tier, every bullet, every recall prompt/answer — zero hits. `1498` inside
   `original_chunk`/`publication_chunk` and `10` inside `textbook` are provenance/printed text, not
   display text, and are correctly exempt. ✓
10. Media: one reading scene needs an image (`M1.S2.T2`, `available_content_types` carries
    `"image"`), one media node exists, `reuse_report` reads `scenes:1 / authored:1 / reused:0`; the
    node carries `image_url:""` and a non-empty, self-contained `generation_prompt`; at most one
    `2d_tool` in the chapter (`null`). ✓
11. `figures_of_speech` is `[]` on both topics — vacuously true, nothing to verify against
    `original_chunk`; the emptiness itself is examined under D above and is a considered call, not
    an omission. ✓
12. Renumbering (Agent 14) has not run yet — nothing to check here; ids are frozen and internally
    consistent going in. ✓

### Publication.   PASS
Both topics carry non-empty `publication_text`. `publication_chunk` is **byte-identical** to
`original_chunk` on both topics (verified programmatically — the verse was never touched).
`concept_publication` supplies `publication_text` on exactly the `paragraph`-type content block at
`content_index: 0` on each concept, matching `16_publication_authoring.md`'s own rule ("emit one
entry per `paragraph` block... never renumber, reorder or drop one") — the sibling `list`-type block
correctly carries no `publication_text`, which is the spec, not a gap. No vocative or classroom
instruction survives in any `publication_text` (`બાળકો`, `જુઓ —`, `બોલો` all scanned for, zero
hits). `M1.S1.T1`'s `publication_text` names the printed title-block era line (`સોળમી સદીમાં`) in
place of `explanation`'s omitted date — this is a fact drawn from the same printed page
(`01_meta.json`'s `genre_signals` quotes `મીરાંબાઈ (જન્મ : ઈ.સ. સોળમી સદી)` verbatim, and
`07_pitfalls.json`'s chapter-level biography note explicitly names this era line as the second
legitimate printed source alongside `original_chunk`), not an invented one — noted here as a minor
editorial observation, not a defect.

---

## E–G (reported)

- **E — સ્વાધ્યાય and risk.** All 5 inventoried blocks (MCQ ×2, એક-એક વાક્યમાં ×2, બે-ત્રણ વાક્યમાં
  ×2, સવિસ્તર ×1, વિદ્યાર્થી પ્રવૃત્તિ ×3 = 10 items) answered as EX1–EX10, all mapped to
  `M1.S2.T2` (the whole પદ is the chapter's one reading scene). The three વિદ્યાર્થી પ્રવૃત્તિ items
  and both MCQ-adjacent explanations are correctly flagged `is_model_answer: true`/model-style
  where the task is personal/creative (drawing, singing, instrument survey) rather than skipped.
  `08_sensitivity.json`'s one **soft** item (`M1.S1.T1`, ધર્મ) and one **hard** item (`M1.S2.T2`,
  ધર્મ) are both addressed, per D above. No block is unmapped.
- **F — Shape and media.** All 12 contract invariants hold (above). `chapter_id`/`plan_id` shape is
  correct and provisional per VERIFY-1. One reading scene, one media node, one per scene;
  `2d_tool: null`. `negative_prompt` carries `Devanagari script labels` (and more). No
  `[reused frame: …]` stamp and no non-empty reused `image_url` anywhere — correct, since no
  Gujarati frame pool exists yet.
- **G — the seven usual mistakes.** All seven checked and none present: (1) no સાર+બોધ+પ્રશ્નોત્તર
  flattening — the પદ's own images carry the explanation throughout; (2) no દુહા merged (vacuous,
  `structure_inventory.duha` = 0); (3) the પદ is not split કડી-wise and its ટેક is not lifted out
  as its own topic; (4) printed licence (`થૈ`, `મારગ`) is uncorrected everywhere it is quoted,
  including inside `explanation`/summaries/recall answers; (5) no અલંકાર named because a field
  existed — `[]` is a reasoned call (see D); (6) both `real_life_example`s are Indian, single,
  concrete, and pitched at std 10, not an adult abstraction; (7) no સ્વાધ્યાય block was cut as a
  topic — the exercise deliverable is complete, not half-empty.

## Media

`reuse_report`: **scenes 1 · authored 1 · reused 0 · rejected []**. The one authored scene sits on
`M1.S2.T2.C2` (`M1.S2.T2.C2.IMG1`, "વૃંદાવનની કુંજગલીમાં મોરલી") — a flute-player and a listener
stopped mid-step in a tree-lined lane at dusk, no idol or પૂજા framing (`teaching_notes` says so
explicitly). `M1.S1.T1` correctly carries no media (`available_content_types: []`). `2d_tool: null`
for the whole chapter. `generation_prompt` is self-contained (setting, both figures' fixed
appearance, action, mood, style, 16:9, Indian village setting) and names no previous image or the
chapter itself.

## Gaps

- `textbook_url` is a **local path** (`../Textbooks-pdf/std-10/ch-01-morli.pdf`) — the GSEB readers
  have no hosted URL.
- `textbook_pages: "1–3"` at confidence **high** (`11_pages.json`) — printed folio and
  `Textbooks-pdf/std-10/manifest.json`'s row agree. No pagination gap.
- `chapter_master_id: null`, `publication_id: 1`. Neither is a real GSEB record —
  `upload_reference/chapter_master_map.json` carries `null`/`null` for this chapter. `1` is written
  only because the contract rejects `null`; it is the same CBSE-derived placeholder every sibling
  chapter in this pack currently carries (kept for pack-wide consistency, not derived or invented
  fresh). Both fields must be resolved from the education DB at **VERIFY-2** before any upload.
- `chapter_id`/`plan_id`'s board and medium segments (`gseb`/`eng`) are **provisional until
  VERIFY-1**. A wrong medium segment uploads clean and mis-files the plan.
- `medium_id` and `subject_ref_id` are `null` by contract (server-injected). `english_plan_id` and
  `english_chapter_id` are `null` — a Gujarati chapter has no English twin.
- `ordering: null` — Agent 14/15's field, deliberately not set here.
- **`05b_textbook_order.json` is identical to the logical traversal** (`M1.S1.T1`, `M1.S2.T2` in
  both). Per `phase2_contract.md`'s own instruction, raised rather than silently skipped:
  ```jsonc
  {"human_confirmation_required": true,
   "reason": "textbook order is identical to logical order",
   "checked": "05b_textbook_order.json matches the logical traversal exactly"}
  ```
- `M1.S1.T1.publication_text` names the title-block era line (`સોળમી સદીમાં`) — see the Publication
  note above; flagged here too as the one place this pass exercised judgment rather than a
  mechanical check, so a human reviewer can confirm the call.
- Working fields dropped at merge, as required: `genre_signals`, `genre_confidence`,
  `active_genre_profiles`, `explanation_unit`, `structure_inventory`, `exercise_inventory`,
  `extraction_notes` (all from `01_meta.json`); `notes` (from `05_with_content.json`,
  `02_structure.json`, `12_authoring.json`); `topic_id` on each media node (redundant with
  `concept_id`/`home_concept_id`); `04_validation.json`'s checklist scaffolding. `13_merged.json`
  carries the 32 root contract keys, the 31 topic keys plus the poem/ભાષા-બોધ extras, and nothing
  else.

## LP2 validator

**PASS** — Live server validation completed successfully.

Request to `POST /api/lp2/learning-plans/validate` (staging.singularity-learn.com) at 2026-08-29:

```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati10_ch1_v1",
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

**Result:** Zero validation errors. Plan is valid for deployment.

---

## Verdict

**PASS — A–D hold, all 12 contract invariants hold, publication complete, exercises complete.**
`12_authoring.json` and `16_publication.json` closed every gap the prior gate found: both concepts
now carry non-empty `content[]`, every hard `avoid_checks`/sensitivity item is addressed exactly as
the pitfalls file asked, and the publication layer rewrites cleanly with no added meaning worth
blocking on. Nothing was repaired by this agent — no explanation, gloss, prompt or device was
touched; the fields already written by A5/A7/A8/A9/A10/A11/A12/A16 passed as authored. The only
open items are the standing pack-wide ones (VERIFY-1, VERIFY-2, the LP2 live-validator call) and the
one minor editorial note above (era line in `M1.S1.T1.publication_text`) — none of them block this
gate.
