# Validation Report — std 8, પૂરક01 · ભુલભુલામણી (`gseb_eng_gujarati8_ch16`)
સ્વરૂપ: ઊર્મિકાવ્ય-ગીત (બાળકાવ્ય) (confidence: high)   explanation unit: એક કડી

Topics: 6   Objectives: 6   Images: 0/0 (`09_media.json` is absent, so nothing is authored on disk; 6 scenes are waiting for it)   Exercises: 0/0 blocks (none printed — see Gaps)

Deliverables: this unit prints a reading scene, so two ship — the plan (`13_merged.json`) and the exercise pack (`10_exercise_solutions.json`). The exercise pack is correctly **empty** (measured: `exercise_inventory: []`), but the file itself is missing.

**VERDICT: NOT COMPLETE. Six hard blockers (B-1, B-2, B-3, D-1, D-2, D-3). This is a failing run and is not presented as a pass.**

> **Where this file is.** This report could not be written to its declared path. This agent's own Write to `output8/purak01/validation_report.md` was refused by the harness guard ("this subagent's parent bg session hasn't isolated yet, so writes to the shared checkout are blocked"), the same guard that stopped A7, A9 and A10. The guard was not routed around (no Bash write into the checkout, no settings change). The report is staged at `/tmp/gujarati-lp-staging/purak01/validation_report.md` (beside A9's staged `09_media.json`). Anyone with write access can copy it to `/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output8/purak01/validation_report.md`. Until then `output8/purak01/` holds no report; the existing `13_merged.json` there is current (below).

**RE-QC (final pass).** No `validation_report.md` from an earlier pass was on disk when this pass began, only a `13_merged.json`. The merge was therefore re-derived from scratch from the layers now on disk and compared leaf by leaf with that file: **no leaf differs** (all 31 root keys, 6 topics, 6 objectives, 12 recall questions, 12 `concept_publication` entries), so `13_merged.json` needed no rewrite and was left in place untouched. It is **not shippable**: `media` is `[]` on all six topics because `09_media.json` does not exist, and it carries the B-2 and B-3 defects exactly as found. A13 merges; it does not repair.

Why three layers are missing is infrastructure, not authoring. A7, A9 and A10 each ran to completion on 2026-10-06 between 00:37 and 00:44 and each reported `ok=false` with the same cause: their Write to the shared checkout was refused by the guard quoted above, and each declined to route around it. This pass did not route around it either: the staged copies were **read** for information (below) and **not** copied into place, because they are other agents' declared files.

---

## A–D (blocking)   **FAIL** — six items, named below

### B-1 (hard) — `guiding_question` misspells the poem's first word (owner: A1)

Root `guiding_question` opens `ઘરુવાડિયાં` (ઘ). The verse in `M1.S1.T1`'s `original_chunk` and the printed શબ્દાર્થ box both print `ધરુવાડિયાં` (ધ). A1's own `extraction_notes[]` records the ધ/ઘ resolution to ધ, and the shipped field still carries ઘ. Not a word in Gujarati. A7 (staged copy) and A9 noted it independently.

Where it lives: `01_meta.json` (`guiding_question`, and the working field `genre_signals.theme`), copied into `02_structure.json` and `05_with_content.json`; `13_merged.json` takes it from `01_meta.json`. No teaching field carries it — checked: zero occurrences of ઘરુવાડિયા in `12_authoring.json` and `16_publication.json`.

Minimal remedy: one character (ઘ → ધ) in `guiding_question`. This is **not** a reason to re-diagnose the chapter: if A1 is re-run it should be told to change only that field, and the copies in 02/05 need the same character fixed.

### B-2 (hard) — M1.S2.T3: `સવાર` is read upstream as "the morning", which contradicts the authored layer (owners: A2 → A4 → A5)

The printed line is `થશું સવાર જ્યાં ધૂમકેતુની ઘોડો દેતો હાવળ !`. `થશું` is the first-person-plural future of *becoming*, and the same line prints `ઘોડો` and `હાવળ` (the box glosses હાવળ as ઘોડાનો હણહણાટ). So `સવાર` is the rider: "we shall become riders where the comet's horse neighs". It cannot be "until morning comes" (that would need `થશે સવાર`). A12 (authoring), A16 (publication), A7 (staged) and `08_sensitivity.json` all read it as a rider.

Upstream still reads it as dawn. Verified occurrences in the current files:
- root `objectives[2].objective_text` (O3): "…કવિ **સવાર સુધીની** ઊડાનની કલ્પના કઈ રીતે બાંધે છે…", and its inline mirror `M1.S2.T3.learning_objectives[0].objective_text`;
- `M1.S2.T3.modified_chunk`: "…ઊડતાં-ઊડતાં **સવાર પડે ત્યાં સુધી** જવું છે…";
- the module-grouping note in `02_structure.json` / `05_with_content.json` ("reaching સવાર at the end of કડી 3").

Effect: the merged plan states a goal and a seed paraphrase that say the opposite of its own explanation, which tells the child "સવાર એટલે સવારનો સમય નહિ". The authored fields are right and need no change for this item.

Order matters. A2 rewrites O3 (and the grouping note), A4 re-validates (ids stay frozen — text only), then A5 re-attaches the registry and re-derives `modified_chunk`. Run concurrently, A5 would copy the stale registry from `02_structure.json`.

### B-3 (hard) — an unsourced botanical gloss in A5's `key_terms` / `modified_chunk` (owner: A5)

`M2.S3.T4` glosses `આવળ-બાવળ — બે જાતનાં કાંટાળાં ઝાડવાં` in the topic `key_terms`, the concept `key_terms`, and `modified_chunk` ("કાંટાળાં ઝાડવાં"). The printed શબ્દાર્થ box glosses neither word. A12, A7 and A9 each could not confirm it, and this pass cannot confirm it from the page either. To this QC's knowledge આવળ is a yellow-flowered shrub, not a thorny one, so the gloss is both unsourced and probably wrong, and it sits in a child-facing field. A12 avoided it in prose (it says only that they are friends beside પારિજાત and ગુલાબ), which is why only A5's layer needs the fix.

Remedy: a neutral gloss (e.g. `બે જાતનાં ઝાડવાં`) or a printed source — never an assertion the page does not carry (`no_hallucination_policy.md`). Other A5 readings that are *not* printed but are plausible, and are reported in E–G rather than blocked: `બીજ` as બીજનો ચાંદ, `પતંગ-પાંખો` as moth/butterfly wings, `નંદ-યશોદા` / `શામળ` as Krishna's household.

### D-1 (hard) — `07_pitfalls.json` is absent, so D's "every `severity:"hard"` item is addressed" cannot be certified (owner: A7)

A7 (`s8purak01:07`) finished a complete, validated file but could only write it to a linked worktree: `.claude/worktrees/purak01-a07-pitfalls/gujarati-lp/output8/purak01/07_pitfalls.json` (34 KB). A12 authored without it (A12's own note, "ROUTING GAP 2": it applied the profile's Avoid list itself and asked A13 to re-check once A7 lands). `08_sensitivity.json` is present and has three items, all `soft` (ધર્મ ×2, સુરક્ષા — all three are labels from the fixed seven); each was checked against the authored fields and is honoured (no ઉત્તરાયણ / kite, wings or leaping in T3; no ભક્તિ કરવી / Krishna episodes in T5; no કૃષ્ણ / શામળ / નંદ / યશોદા read back into T4).

**Informational pre-check of the staged copy against the authored layer — not a gate, because the file is not at its declared path.** Its `hard` items, run mechanically wherever they can be:
- Passing on all six: no `જોઈએ` exhortation anywhere; the first sentence of every explanation names a word printed in that કડી; every explanation carries a પ્રાસ/પુનરાવર્તન/ધ્વનિ sentence quoting the line-end words; `figures_of_speech: []` with no device label; no science, astronomy, ecology, kohl-making or eclipse vocabulary; no `કડી <n>`; printed `કો'નું`, `તણી`, `અમ...` kept.
- **Probable hits, if the staged items are confirmed once it lands** (all in `12_authoring.json`, so owner A12, then A16 re-derives publication):
  - T1, hard item "every sentence that states the pictures also carries an imagining word (જાણે / કલ્પના / કવિને લાગે છે)": the first and third sentences of `explanation` state the pictures without one (the fourth sentence has "કવિની કલ્પનામાં").
  - T6, hard item "each sentence that says the line carries જાણે / કલ્પના": the first and second sentences of `explanation` (and the summaries) say `કવિ અંધારાનું કાજળ … આંજે છે` / `અંધારાને જ કાજળ બનાવી દે છે` with none.
  - T3, hard item "never `ધૂમકેતુનો ઘોડો` in any field": it appears in `summary`, `detailed_summary`, `important_points[0]`, a recall answer, and the `vyakaran` note. The `vyakaran` use is a grammar note naming the rule-form beside the printed one and keeping the printed one, which is defensible; the prose uses are what the item targets.

  These are judgement calls on strict wording, so they are reported as probable, not as findings.

### D-2 (hard) — `09_media.json` is absent; no topic carries media (owner: A9)

All six topics carry `available_content_types: ["image"]`, so `reuse_report.scenes` must be 6; on disk there is no `reuse_report`, authored is 0, and merged `media` is `[]` on all six. A9 (`s8purak01:09`) staged a finished file at `/tmp/gujarati-lp-staging/purak01/09_media.json`. Read-only pre-check of that copy against the Media gate: 6 nodes, ids match `MEDIA_ID_RE` and the plan's six concept ids, `image_url: ""` on every node, a non-empty `generation_prompt` (984–1165 chars) on every node, `Devanagari script labels` in every `negative_prompt`, one narrator-bar line per prompt that is a verbatim substring of that topic's `original_chunk`, `2d_tool: null`, `reuse_report {scenes 6, reused 0, authored 6, rejected []}`. It would pass as read. It is not in place, and a gate cannot merge a layer that is not at its declared path.

### D-3 (hard) — `10_exercise_solutions.json` is absent (owner: A10)

The inventory is empty and that is a measured fact (A1 recorded it; A10 independently re-read the render and found only the number box, title, author line, પ્રવેશપેટી, six કડી, one શબ્દાર્થ box and folio 138). The correct content is therefore `exercises: []`, `coverage_report.blocks_found` equal to the inventory length (0), `unanswered: []`, `unmapped: []` — identical to the precedents `output6/purak02` and `output7/purak04`. A10 (`s8purak01:10`) was blocked by the same guard and left its intended JSON in its notes only; nothing is staged on disk. A14 copies this file to `exercise_solutions.json`, so the missing file would fail there.

---

### What was checked and passed (mechanically, from the layers on disk)

**A.** સ્વરૂપ ઊર્મિકાવ્ય-ગીત (બાળકાવ્ય), `genre_confidence: high`, four `genre_signals` recorded; the blue પ્રવેશપેટી names no form and A1 says so openly rather than inventing a quote. Explanation unit `એક કડી` matches the profile. Six `[[કડી n]]` markers, six topics. પ્રવેશપેટી and શબ્દાર્થ are apparatus (`markers_deliberately_not_cut_as_topics`), none became a topic. No `[[ટેક]]` marker, so the ટેક rules have nothing to bite on, and `depends_on: []` throughout is correct for a cumulative list poem. The six explanations in order do answer the guiding question (apart from the B-1 typo).

**B.** All six `original_chunk` equal the corresponding block of `00_chapter_normalized.md` **byte for byte** (T1 with the printed byline `- યોગેન્દ્ર વી. ભટ્ટ` at its head); non-empty; every character is U+0A80–0AFF, whitespace or punctuation; zero Roman, zero Devanagari, zero `।`. `word_count.original` recomputed for all six and agrees (17, 14, 13, 17, 11, 11). Printed forms intact and uncorrected: `ધૂમકેતુની ઘોડો`, `કો'નું`, `તણી`, `અમ...`, `માગીશું...`, `ધરુવાડિયાં`, `કાસળ`, `બંસી`. QR code string absent. Ids consecutive. No `[[સ્વાધ્યાય…]]` marker exists and none became a topic.

**C.** Every topic has non-empty `explanation` and `real_life_example`, all inside 55–90, nothing trimmed or widened:

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 73 | 69 |
| M1.S2.T2 | 67 | 64 |
| M1.S2.T3 | 74 | 64 |
| M2.S3.T4 | 70 | 63 |
| M2.S3.T5 | 70 | 64 |
| M2.S4.T6 | 68 | 62 |

`objective_text` O1–O6: 22, 23, 20, 28, 22, 21 words (12–30). Craft at the std-8 ceiling: a scan for અલંકાર, છંદ, સમાસ, સંધિ, રૂપક, ઉપમા, ઉત્પ્રેક્ષા, સજીવારોપણ, અનુપ્રાસ, યમક, શ્લેષ, અતિશયોક્તિ and the rest returns zero hits in every authored field.

**D.** Zero `જોઈએ`/`જોઈશે`/`ફરજ`/`ઉપદેશ` in any authored field (the profile's slogan gate). Zero scientific-mechanism or political words. First sentence of every explanation names something in that કડી that is in its `original_chunk` (ધરુવાડિયાં; ફૂલનું / આગિયા; પતંગ-પાંખો / તમરાં; ભેરુ / પારિજાત / ગુલાબ; મોરપીંછ / બંસી; કાજળ / સૂર્ય-ચંદ્રની). `figures_of_speech` is `[]` on all six, so invariant 11 holds vacuously and nothing was invented; every `rhyme_scheme.rhyming_words` pair (વાદળ–ઝાકળ, પાછળ–આગળ, સાંકળ–હાવળ, બાવળ–કાસળ, આવળ–બાવળ, કામળ–શામળ, કાજળ–કાગળ) is found verbatim in its chunk, and every note says honestly that the consonant before ળ differs, so the rhyme is a shared sound-ending and not letter-for-letter. T3's visible traps are handled: `સવાર` taught as the rider, and the flight kept in કલ્પના.

**Contract (12 invariants).** (1) `phase: 2`, `plan_id` = `{chapter_id}_v1`, `chapter_id` `gseb_eng_gujarati8_ch16`, `unit_number` 16, `topic_number` 16. (2) as B. (3) six concepts `C1`–`C6`, chapter-continuous, each with a registry-resolving `objective_id` and non-empty `content[]`. (4) registry: unique ids, every `home_topic_id` and `anchor` resolves, `strand_to_objective_map` covers L1–L6, every topic's `objective_ids` resolve. (5) all six inline mirrors match the registry character for character. (6) recall ids `{topic}.RQ{n}` with `legacy_id` `.TR{n}`, three per topic, lowercase `bloom_level`, every one with an answer; no `.SR` anywhere; `publication_id` is 1 (non-null, provisional until VERIFY-2); `topic_type` is the authored `POEM`, which A14 maps to `instructional`. (7) no સ્વાધ્યાય topic. (8) summaries strictly increase: 1 / 3 / 5 sentences, 97–123 / 171–219 / 306–413 characters in every topic. (9) zero digits or `કડી <n>` in any display field, in module `difficult_words` or `overall_rhyme_scheme`. (10) not satisfiable — see D-2. (11) vacuous, as above. (12) `depends_on` and `source_topic_ids` are empty, so nothing can dangle after renumbering.

**Publication.** Every topic has `publication_text`. `publication_chunk` begins with `original_chunk` **byte for byte** on all six, then the rewritten explanation, then the rewritten example. `concept_publication` has 12 entries, matching the 12 paragraph blocks by index and count. No `બાળકો`, `જુઓ —`, `બોલો`, `જુઓ`, `વિચારો` survives in any publication field. Added meaning: none found — `publication_text` equals the explanation minus its vocative opener on five topics, and on T3 differs by exactly one word (`વાંચો` → `રાખ્યું છે`, which A12's own paragraph already says); the example rewrites differ from `real_life_example` only by dropped second-person questions and the two sentence rewrites A16 declared.

---

## E–G (reported)

- **E — exercises and risk.** No સ્વાધ્યાય block is printed on this પૂરક page; `exercise_inventory: []` is a measurement, not a gap, and `profiles/genres/urmikavya_geet.md` says પૂરકવાચન poems carry none. The three soft sensitivity items (ધર્મ on the prayer in the fourth કડી and the Krishna names in the fifth; સુરક્ષા on the wings and the horse in the third) are applied in the authored layer as guided, not censored.
- **F — shape.** The invariants above hold except media (D-2). `chapter_id` is the synthetic ch16 required by the run context and is provisional; the provenance (પૂરક lesson 1 continuing after std-8's 15 numbered chapters) is recorded in `01_meta.json`'s `extraction_notes[]`. `ordering` is not written here (A14's key). `05b_textbook_order.json` equals the logical traversal exactly, so A14/A15 should raise `human_confirmation_required`.
- **G — the seven mistakes.** None is present: not a સાર + બોધ + પ્રશ્નોત્તર (the explanations are pictures first, and no બોધ is forced); no દુહા merged and no પદ split; no ટેક lifted out (there is none); no poetic licence corrected in the verbatim (`ધૂમકેતુની ઘોડો` is kept and flagged, never repaired); no અલંકાર named because a field existed (all six `[]`); no adult or foreign `real_life_example` (a village-field lunch, an Eid-evening crescent, a night ST bus, a પોળ ઓટલો, a lullaby, a recess word-chain — all inside std-8's reach, none needing its own glossary); no સ્વાધ્યાય cut as a topic.
- **Spec conflict — `publication_chunk`, decided against the literal text, flagged for the orchestrator.** Agent 13's spec says `publication_chunk` must be "byte-identical to `original_chunk`". Agent 16's spec, which owns the field, says the verbatim "stays verbatim **inside** it" with the rewritten prose around it, and the shipped corpus follows that: `output8/ch01`, `output7/purak04` and the three passing chapters measured in `output6/purak02`'s waiver all have 0 byte-identical and all begin with the verbatim. This pass verified the property that protects the verse (a byte-exact prefix on all six) and did **not** raise the literal reading as a blocker, because routing it to A16 would loop against A16's own spec. If the orchestrator wants the literal reading enforced it should say so, and spec 16 would have to change first.
- **Attribution placement.** The byline `- યોગેન્દ્ર વી. ભટ્ટ` sits at the head of `M1.S1.T1`, not in the last topic as the checklist assumes. The page prints it above the poem, so this is page-faithful; same ruling as `output8/ch01`. Reported so it is not later mistaken for a misplacement.
- **A5 readings that are not printed and were not blocked** (all flagged by A7/A9/A12 independently): `બીજ` = the thin crescent (contextual, and the natural reading of `બીજ તણી બંકિમ હોડી`, but no gloss is printed); `પતંગ-પાંખો` = moth/butterfly wings in A5's `key_terms` (a paper kite is the other everyday reading; A12's prose stays neutral); `નંદ-યશોદા` and `શામળ` as Krishna's household. A5's `modified_chunk` for T1 and T6 states images and a reading flatly ("…તડકા-લચકા મળે છે", "કવિતા પોતે જ … ભુલભુલામણી બની રહે છે"); A12 did not echo either.

## Media

`reuse_report` does not exist on disk (D-2). `Images: 0/0` is the truth of what is landed. Expected once A9's file lands: 6 scenes, 0 reused, 6 authored, 0 rejected, no Gujarati frame pool, every `image_url: ""`. The staged copy's own note adds that no human figures are drawn (the poem has no cast), the sixth-કડી sun and moon are plain discs, the fifth-કડી image shows only objects and doorways with no deity, and the third-કડી narrator bar keeps the printed `ધૂમકેતુની ઘોડો`. Its only open flag is the same B-3 question about `આવળ` (it drew a yellow-flowered shrub beside a thorny acacia).

## Gaps

- **Harness write guard (infrastructure).** `07_pitfalls.json`, `09_media.json` and `10_exercise_solutions.json` were not landed because the parent session had not isolated when A7, A9 and A10 ran, and this A13 pass hit the same refusal on its own `validation_report.md`. A12, A16 and the earlier A13 pass did write into `output8/purak01/` successfully earlier the same night, so the guard is intermittent or session-dependent. Staged: `.claude/worktrees/purak01-a07-pitfalls/…/07_pitfalls.json` (A7), `/tmp/gujarati-lp-staging/purak01/09_media.json` (A9), `/tmp/gujarati-lp-staging/purak01/validation_report.md` (this file). A10 has nothing staged (content known: an empty exercise pack). A7, A9 and A10 need to re-run or have their files landed by someone with write access; A7's worktree and branch also need removing afterwards. `/tmp` is cleared on reboot, so copy the staged files soon.
- **`textbook` is `null`.** `profiles/boards/gseb_gujarati.md` still records the std-8 cover as unread, and A11 declined to guess. Sibling chapters `output8/ch01` and `ch02` carry `ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 8` from the profile's convention while `ch03` carries `null`; the corpus is not consistent and this unit follows `ch03`. Not invented here.
- **`textbook_url` is a local path** (`../Textbooks-pdf/std-8/purak-01-bhulbhulamani.pdf`); the readers have no hosted URL.
- **`textbook_pages: "138"`, confidence medium.** One printed page, read once (not at both ends of a range); agrees with the manifest and the board profile.
- **`chapter_master_id: null`** by design: no real GSEB master row exists for a પૂરક unit under the synthetic ch16 identity. **`publication_id: 1`** is provisional until VERIFY-2.
- **Only one render exists** for this single-page unit, so A5's usual "render low, re-render high, compare" cross-check could not run; A1 and A5 substituted enlarged crops. No render was opened in this pass: `00_chapter_normalized.md` answered every question.
- **Routing gaps reported by earlier agents** (documents the run context did not hand over): A2, A4, A12 and A16 each read the missing document from the repository. A9 did not read `phase2_contract.md` or `field_shape_rules.md` and asked QC to verify; this pass checked the staged media node shape and conventions against both (see D-2).
- **A4's notes:** none blocking. `04_validation.json` (`status: pass`) and `04_converged.json` (`sha256` matches the current `02_structure.json`) are intact; B-2 is a content error in text A4 does not check.

## Routing

| blocker | owner | note |
|---|---|---|
| B-1 | A1 (one character; do not re-diagnose) | fix the copies in `02_structure.json` and `05_with_content.json` too |
| B-2 | A2 → A4 → **then** A5 | sequential; A5 copies the registry from `02_structure.json` |
| B-3 | A5 | in the same A5 pass as B-2 |
| D-1 | A7 (land the file) | then re-gate; if the three probable hits stand, A12 → A16 |
| D-2 | A9 (land the file) | staged copy looks clean |
| D-3 | A10 (land the file) | `exercises: []`, as above |

The in-run owner loop takes at most three owners and runs them concurrently, so it cannot carry the B-2 chain. A second, sequential round is needed: A7, A9, A10 can run together; A1; then A2 → A4 → A5.

## LP2 validator

_Filled in Phase 8. Not run on this plan: it is not shippable until the blockers above are closed._
