# Validation Report — ધોરણ 10, એકમ 5 — શ્વેતકાંતિના પ્રણેતાઓ

સ્વરૂપ: ચરિત્ર-પ્રસંગ (રેખાચિત્ર) (`charitra_prasang.md`, confidence: **high**)
explanation unit: એક જીવન-પ્રસંગ, અથવા છપાયેલ વ્યક્તિ-વિભાગ (તથ્ય-ઝૂમખું)

Topics: 12   Objectives: 12   Images: 0/5   Exercises: 9/9 items across 3/3 inventoried blocks

## A–D (blocking)   **FAIL** — two independent hard failures, both outside sections A–D's own
mechanical checks but explicitly gated by this agent's own spec: Contract invariant 9 (no numbers
in display text) and the Publication check (`publication_chunk` byte-identity / concept-level
`publication_text`). **`13_merged.json` is withheld this run** — see below.

### A — Diagnosis and lens.   PASS
`genre_signals` (structure/theme/exercises/purpose) are recorded in `01_meta.json` off the
rendered pages, `genre_confidence: "high"`. `explanation_unit` matches `charitra_prasang.md`'s own
roster line exactly ("The printed part-head is the cut… within a section, episodes cut further"
plus "A dated facts-cluster is a legitimate topic where the chapter is built of facts") — both
halves used correctly: the two printed person-heads `(1) ત્રિભુવનદાસ પટેલ` / `(2) ડૉ. વર્ગીસ
કુરિયન` open modules M2/M3, the five `[[ઘટના: …]]` markers land in five distinct STORY_TELLING
topics, and the remaining seven topics are dated-facts-clusters within each person-section — not
invented topics. No `[[સ્વાધ્યાય: …]]` block became a topic (all three exercise groups and all
nine item texts cross-checked against all 12 `topic_name` values in `04_validation.json` — zero
overlap). Apparatus correctly excluded: શબ્દ-સમજૂતી, વિદ્યાર્થી-પ્રવૃત્તિ, ભાષા-અભિવ્યક્તિ,
શિક્ષક ભૂમિકા. Single genre throughout, not mixed. `guiding_question` is chapter-derived (names
both men, the "અમૂલ બ્રાન્ડ" and the "ચાર દાયકા" partnership) and the topic sequence in printed
order answers it.

### B — Verbatim and structure.   PASS
All 12 `original_chunk` fields non-empty, Gujarati-script only. Programmatic scan of every
`original_chunk`, `modified_chunk` and `topic_name`: **zero** Devanagari codepoints, **zero** `।`,
and the one Roman-script hit (`ST બસ` inside `M1.S1.T1.real_life_example`) is the pack's own
approved cultural-anchor abbreviation (`teaching_voice_gu.md`'s bank uses the identical form
`ST બસનું ડેપો`), not a violation. `word_count.original` independently recomputed on all 12 topics
by whitespace count and matches the declared value exactly (112, 109, 221, 156, 83, 212, 161, 274,
146, 70, 253, 72). Marker accounting: five `[[ઘટના: …]]` markers land in exactly five topics, two
printed person-heads open exactly two modules, no double-claim, no gap — re-confirmed against
`04_validation.json`'s own line-range table. Poetic/dialect licence is inapplicable (ગદ્ય ચરિત્ર,
no verse), but the chapter's own printed variance is honoured, not harmonised: the four differing
forms of the Kheda cooperative's name each stay inside the topic that actually prints that form
(spot-checked `M2.S3.T3` → `ખેડા જિલ્લા દૂધ ઉત્પાદક સહકારી મંડળી લિમિટેડ`, `M3.S4.T7` → `ખેડા
ડિસ્ટ્રિક્ટ મિલ્ક પ્રોડ્યુસર્સ યુનિયન લિમિટેડ`, matching each topic's own `original_chunk`, never
borrowed from a neighbour). No header furniture (chapter-number box, QR badge, footer) entered any
chunk. Ids consecutive: M1–M3 / S1–S7 / T1–T12 / C1–C17, chapter-continuous, no restart at any
topic boundary.

### C — The teaching block.   PASS on shape and voice
Every topic carries non-empty `explanation` and `real_life_example`, both inside the 55–90 word
band on all 12 topics (explanation: 76–87; real_life_example: 71–78). `objective_text` O1–O12: 18,
21, 21, 20, 26, 20, 19, 21, 26, 18, 21, 22 words — all inside 12–30. Voice is second-person, spoken
શિષ્ટ ગુજરાતી, glossing at point of first use (`કાર્યદક્ષતા`, `સ્વપ્નદૃષ્ટા`, `સંગઠનક્ષમતા` etc.
glossed inline in `explanation` and again as module `difficult_words`). `real_life_example`
anchors are Indian, single, and rotate domain scene-to-scene per `12_authoring.json`'s own ledger
(ST બસ → શેરી ક્રિકેટ → ખેડૂત-વેપારી → ઉનાળાની પરબ → કારીગરનો ભત્રીજો → સાયકલ → વર્કશોપ-માર્ગદર્શક
→ દૂધમંડળી → કેન્ટીન → રથયાત્રા → વાવ → પોતાની આવડત) — no repeated domain, no adult abstraction, no
anchor needing its own glossary. **But the field-shape pass does not clear Contract invariant 9 —
see below.**

### D — સ્વરૂપ essence.   PASS
`figures_of_speech: []` and `rhyme_scheme: null` on all 12 topics, correct for ગદ્ય ચરિત્ર-પ્રસંગ
(no કડી, પ્રાસ or છંદ anywhere in the source). All 17 `severity:"hard"` avoid-checks in
`07_pitfalls.json` spot-checked against actual authored text, not merely asserted against
`12_authoring.json`'s own notes:
- `M1.S1.T1` — qualities (કાર્યદક્ષતા, સંગઠનક્ષમતા…) named only as a preview the "coming પ્રસંગો
  will show," never as a settled verdict in the first sentence. Confirmed in `explanation`.
- `M2.S3.T3` — situation → act → result order held exactly: પોલસનનો ત્રાસ (situation) →
  ખેડૂતોએ મંડળી સ્થાપી (act) → કુરિયનનો સાથ, ડેરીનો વિકાસ (result); no bare year-list; this
  topic's own printed cooperative name used, not another topic's form. Confirmed verbatim in
  `explanation`.
- `M3.S4.T6` — the hard **sensitivity** item (severity: hard, ધર્મ/સમુદાય): the community fact
  "એક સિરિયન ખ્રિસ્તી પરિવારમાં" is carried, named exactly as printed, with no elaboration on
  belief, at the same neutral weight as the other birth-family facts — present in
  `concepts[M3.S4.T6.C8].content[0].text`. (It is absent from `explanation` itself, which leads
  instead with the age/self-reliance thread the pitfalls file also sanctions; since the fact is
  carried correctly in the topic's other authored teaching field, the hard item is satisfied.)
- Marriage/spouse check: `પત્ની` appears 5× across `12_authoring.json`, all five referring to
  ત્રિભુવનદાસ's printed wife `મણિબહેન` (`M2.S3.T4`, matching the source); zero fabricated
  reference to Kurien's marital status, which the chapter never prints (chapter-level pitfall).
  Death-age `91 વર્ષની વયે` is carried as printed on both men, never silently recomputed to `90`.
- No topic-count-based "Kurien is the main hero" framing found in any `explanation`.

## Two hard failures found this pass

### 1 — Contract invariant 9: numbers in authored display text (owner: **A12**, `agents/12_runtime_authoring.md`)

`json_contract.md` invariant 9 / `global_content_rules.md` item 4 / `qc_checklist.md` §F all require
**zero** digits (Arabic or Gujarati) in authored display text — `explanation`, summaries,
`concept_bullets`, `important_points`, `concepts[].content[]`, recall prompts and answers. This
pack enforces it strictly even for factual/biographical content: the already-passed sibling
`output10/ch06` (a memoir, equally date/fact-dense) shows **zero** digit hits across every authored
field, and its own validation report records the check explicitly ("No digit — Latin or Gujarati —
in any authored display field").

`output10/ch05/12_authoring.json` fails this on **7 of 12 topics, 34 field-level occurrences**:

| Topic | Fields carrying a digit |
|---|---|
| `M2.S3.T3` | `detailed_summary` (`22-10-1903`, `1940-41`, `3 જૂન 1994`, `91`) |
| `M2.S3.T4` | `explanation`, `summary`, `detailed_summary` (`1971`, `1964`), `concept_bullets` ×2, `recall_questions[].prompt` |
| `M3.S4.T5` | `detailed_summary` (`1944`) |
| `M3.S4.T6` | `explanation`, `brief_summary`, `summary`, `detailed_summary` (`1948`, `26-10-1921`) |
| `M3.S4.T7` | `detailed_summary`, `concept_bullets` (`13-5-1949`) |
| `M3.S5.T8` | `explanation`, `brief_summary`, `summary`, `detailed_summary`, `concept_bullets` ×2, `recall_questions[].answer` (`33`, `60`, `24`) |
| `M3.S7.T11` | `explanation`, `brief_summary`, `summary`, `detailed_summary`, `concept_bullets` ×2 (`2012`, `9-9-2012`, `26 નવેમ્બર`) |

Every one of these dates/counts is genuinely printed in the chapter — nothing is fabricated — but
the rule requires them spelled out in Gujarati words in *authored* fields exactly the way
`ST બસ`-style rewrites elsewhere in the pack already do it (`original_chunk`/`prompt_verbatim` are
the only fields licensed to keep printed numerals). This is a mechanical, chapter-wide rewrite, not
a judgment call — A12 needs to re-render every digit above into words (`ઓગણીસસો અડતાળીસ`, `તેત્રીસ
વર્ષ`, `તા. તેવીસમી ઓક્ટોબર, ઓગણીસસો ત્રણ` or an equivalent qualitative phrasing) across the 7
affected topics.

### 2 — Publication: `publication_chunk` not byte-identical to `original_chunk`, and `concepts[].content[].publication_text` entirely absent (owner: **A16**, `agents/16_publication_authoring.md`)

Checked programmatically on all 12 topics: **`publication_chunk` matches `original_chunk` on 0 of
12 topics.** `16_publication.json`'s `publication_chunk` is not a clean copy — it is
`original_chunk` + `publication_text` + a third block that reads like a rewritten
`real_life_example` (e.g. `M1.S1.T1`'s chunk ends with an ST-bus driver/conductor analogy never
printed anywhere in the source; `M3.S6.T10`'s ends with a રથયાત્રા-દોરડું analogy). Lengths roughly
double to triple the original on every topic (112→224 words-equivalent range up to 274→~550). This
is exactly the failure this agent's own spec names as a defect, not a style choice: "Meaning
**added** in the rewrite is a defect." The rewrite additionally never touches verbatim per the
spec's own "Do not" list — concatenating onto it is the same violation from the other direction.

Separately and independently: **`concepts` is `null` on all 12 topics in `16_publication.json`.**
The merge instructions require `concepts[].content[].publication_text` matched by index against
`12_authoring.json`'s `concepts[].content[]` (which has 1–2 concepts per topic, non-empty
`content[]` on every one) — Agent 16 produced no concept-level publication text at all, so this
half of the required deliverable does not exist to merge.

Both defects were re-confirmed by direct field comparison (not asserted from either file's own
notes) on every one of the 12 topics.

## `13_merged.json` is not emitted this run

Diagnosis, verbatim, media, exercises and the sensitivity/pitfall hard items all check out clean
and are ready to fold (see below). But folding `16_publication.json` as it stands would ship
`publication_chunk` fields that fail the byte-identity gate on **every** topic and
`concepts[].content[].publication_text` that is silently absent on **every** topic — a
known-broken artifact — while the digit violations in `12_authoring.json` would carry the same
problem into `explanation`/summaries/bullets. Per this agent's own instructions ("do not fix
authoring yourself… name the owner and stop"), the merge is withheld. **Re-run this agent once
`12_authoring.json`'s 34 digit occurrences are re-rendered in words and `16_publication.json` is
re-authored as a clean `original_chunk` copy plus separately-stored `publication_text` and a
populated `concepts[].content[].publication_text` — nothing else is blocking.**

## E–G (reported)

- **E — Exercises: clean on what was inventoried,** but the inventory itself is worth a second
  look. `10_exercise_solutions.json.coverage_report`: all 3 inventoried blocks (MCQ×3,
  એક-એક વાક્યમાં ઉત્તર×3, સવિસ્તર ઉત્તર×3 — 9 items, EX1–EX9) answered; `unanswered: []`,
  `unmapped: []`; matches `01_meta.json`'s `exercise_inventory` exactly (3 blocks, matching
  `reference/exercise_alignment.md`'s own measured note that "ch 5 prints a 3-tier ladder with no
  બે-ત્રણ વાક્ય tier"). **However**, `01_meta.json`'s `extraction_notes` classify this chapter's
  printed વિદ્યાર્થી-પ્રવૃત્તિ block (4 bullets: વક્તૃત્વસ્પર્ધા, સહકારી મંડળીની મુલાકાત,
  ઈન્ટરનેટ-માહિતી, ગામની દૂધમંડળીની મુલાકાત) as apparatus, outside `exercise_inventory` —
  while `reference/exercise_alignment.md`'s own std-10 table lists વિદ્યાર્થી-પ્રવૃત્તિ as part of
  the printed ladder to be answered (rule 4: "every વિદ્યાર્થી-પ્રવૃત્તિ bullet" gets a model
  answer), and this run's own sibling chapters `output10/ch01` and `output10/ch04` both carry a
  `પ્રવૃત્તિ` group in their `exercise_inventory` and answer it. `10_exercise_solutions.json`'s own
  `coverage_report._note` flags this exact inconsistency and declines to invent a block the
  inventory does not record — correctly, per its own agent's scope. This is not a block on its own
  (E is reported, not gating), but it means the true exercise deliverable may be 9/13 rather than
  9/9 complete. **Recommend a QC pass on `01_meta.json`'s `exercise_inventory` (owner A1), and a
  re-run of `agents/10_exercise_solutions.md` to answer the activity block if the inventory is
  amended.**
- **E — Sensitivity:** the three `severity:"soft"` items (`M1.S1.T1` જાતિ-ભૂમિકા, `M2.S2.T2` ધર્મ,
  `M2.S3.T3` સંઘર્ષ) all hold on direct reading — women's organising stated as the chapter states
  it with no generic sermon added, the Hanuman temple kept as incidental meeting-place, the
  Satyagrah/jail terms framed as courage-for-a-cause with no partisan commentary and the Polson
  episode kept to the plain economic fact. The one hard item (`M3.S4.T6`) is addressed — see D
  above.
- **F — Shape:** the 12 `json_contract.md` invariants checked independently of the two failures
  above: registry consistency (12 unique `objective_id`s, every `home_topic_id`/`anchor` resolves,
  `strand_to_objective_map` covers all 12 `legacy_id`s), `MEDIA_ID_RE` holds on all 5 media ids
  (concept-scoped, e.g. `M2.S2.T2.C2.IMG1`), `recall_questions[]` ids are `{topic}.RQ{n}` /
  `{topic}.TR{n}` on all 36 recall items (3 per topic × 12) — never `.SR{n}` — `key_terms` runs
  exactly 5 per topic (inside 3–6), `concept_bullets`/`important_points` run exactly 4 per topic
  (inside 3–4), three-tier summaries strictly increase in length on all 12 topics,
  `figures_of_speech` verbatim-check is vacuous (`[]` everywhere, correctly). **Invariant 9 fails —
  see above.**
- **G — usual failure modes:** none of the other six observed. Genre kept as ચરિત્ર-પ્રસંગ
  throughout; the two person-sections' unequal topic count (3 vs 8) is the page's own imbalance,
  not a cut defect, and no `explanation` frames Kurien as the "main" figure; no biographical fact
  invented anywhere (every date/institution/quote traced to that topic's own `original_chunk`); no
  poetic licence issue (ગદ્ય, none applies); `real_life_example` never pitched at an adult or set
  outside India; સ્વાધ્યાય not cut as teaching topics.

## Media

`09_media.json.reuse_report`: `scenes: 5`, `authored: 5`, `reused: 0`, `rejected: []` — matches
exactly the 5 topics whose `available_content_types` carries `"image"`
(`M2.S2.T2`, `M3.S4.T5`, `M3.S4.T7`, `M3.S6.T9`, `M3.S6.T10`). All 5 media nodes individually
checked: `image_url: ""`, non-empty self-contained `generation_prompt` (701–869 chars, no reference
to "the previous image" or the chapter by name), `negative_prompt` containing "Devanagari script
labels" on all 5. `2d_tool: null`. Structurally clean and ready to fold once the two failures above
are cleared.

## Gaps

- `11_pages.json`: `textbook_pages: "23–28"`, confidence **high** (both end-page renders read
  directly, cross-checked against `manifest.json`). `textbook_url` is a local PDF path — no hosted
  URL exists for this source (recorded, not a defect).
- `01_meta.json`'s own `extraction_notes` flag several verbatim-fidelity facts Agent 5 already
  carried forward correctly and which must survive any A12 rewrite unchanged: the book's own
  spelling `શ્વેતકાંતિ` (not `શ્વેતક્રાંતિ`); the four Kheda-society name variants (not reconciled);
  mixed Arabic/Gujarati numerals for 1950/૧૯૫૦ inside `original_chunk` only (untouched by the
  digit rule, which applies to authored fields, not verbatim); both subjects' printed death-age of
  91 despite the dates arithmetically giving 90. None of these block; all are load-bearing for the
  A12 re-author pass.
- A minor footer-punctuation variant (`ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 10` with a comma, against the
  board profile's uncomma'd table rendering) — noted by Agent 1, not blocking.
- `chapter_master_id`, `subject_ref_id`, `medium_id`, `publication_id` remain `null`/unset pending
  VERIFY-1/VERIFY-2 (no GSEB DB record fetched yet) — pack-wide convention, not a chapter defect,
  and moot until the merge itself can run.
- Exercise-inventory completeness question (વિદ્યાર્થી-પ્રવૃત્તિ) — see E above.

## LP2 validator

Not attempted this pass — `13_merged.json` does not exist to validate. `learning_plan_logical.json`
generation and server validation are downstream of a clean merge, which is blocked on A12 and A16
as detailed above.

**Phase 8 validation attempt (2026-08-30 05:35 UTC):**

File status: `learning_plan_logical.json` does not exist at expected path. 

Reason: Merge was blocked by failing conditions in A12 (Contract invariant 9: 34 digit occurrences in authored fields) and A16 (`publication_chunk` byte-identity check and missing `concepts[].content[].publication_text`). Per the validation report above, the merge (`13_merged.json`) was not emitted, therefore downstream `learning_plan_logical.json` generation did not occur.

**Result:** UNREACHABLE (file prerequisite does not exist)

**Next steps:** 
1. A12 must re-render 34 digit occurrences as Gujarati words across 7 topics in `12_authoring.json`
2. A16 must re-author `16_publication.json` as a clean copy of `original_chunk` with separately-stored `publication_text` and populated `concepts[].content[].publication_text`
3. Re-run merge to generate `13_merged.json`
4. Re-run Phase 8 validation once `learning_plan_logical.json` is generated
