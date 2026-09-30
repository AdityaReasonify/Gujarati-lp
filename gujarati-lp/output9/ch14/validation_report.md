# Validation Report — std 9, ch 14 મારું તારું !

સ્વરૂપ: ગઝલ (confidence: high)   explanation unit: એક શેર
Topics: 9   Objectives: 8   Images: 0/7   Exercises: 12/12 (4/4 blocks)

Deliverables: two — the plan (`13_merged.json`) and the exercise pack
(`10_exercise_solutions.json`). This is a nine-topic ગઝલ chapter (no સ્વાધ્યાય-only unit), so both
ship in full.

## A–D (blocking)   **PASS**

Every hard item below was checked mechanically against the merged plan (`13_merged.json`),
programmatically where a check could be automated, not asserted from the intermediate files alone.

**A — diagnosis and lens.** સ્વરૂપ ગઝલ, `genre_confidence: high` in `01_meta.json`, four
`genre_signals` (structure, theme, exercises, purpose) recorded off the rendered page, quoting the
કૃતિ-પરિચય's own framing ("આ રચના ગઝલ સ્વરૂપની છે") as evidence, never as the verdict — this
chapter is one of `gazal.md`'s own two founding measured examples, so profile and page agree by
construction. Explanation unit `એક શેર` matches the ગઝલ roster row ("one શેર") — seven POEM topics
(M2.S2.T3–T9) carry the seven printed શેર, one per topic, none merged or split; marker count
verified programmatically: seven `[[શેર N]]` markers in `00_chapter_normalized.md` = seven POEM
topics. No `[[ટેક]]` marker exists on the page and none was invented (`structure_inventory.tek_
occurrences: 0`) — a codepoint scan of the whole merged plan found the bare word `ટેક` only inside
sentences correctly *denying* one ("કોઈ ટેક નથી"), never asserting one. Not a mixed chapter —
single genre throughout. Apparatus did not become a reading scene: શબ્દ-સમજૂતી, ભાષા-અભિવ્યક્તિ
and શિક્ષકની ભૂમિકા stayed apparatus; કવિ-પરિચય and કૃતિ-પરિચય, printed as two separate markers on
this std-9 page, are the two CONCEPT topics per the roster's allowance for student-facing પરિચય
prose. The વ્યાકરણ/revision-checkpoint carve-out does not apply — this unit prints reading text.
`guiding_question` ("કવિ પોતાનું ગમેલું બીજાને 'તારું' કરી દેવા અને વારે વારે હારવાનું પસંદ કરવા
કેમ કહે છે…") is chapter-specific, not copied from the profile, and is answered by reading the
seven શેર topics in order (M2.S2.T3 → T9).

**B — verbatim and structure.** All nine `original_chunk` fields non-empty, Gujarati script only —
a codepoint scan found zero Latin characters outside bracketed technical terms, zero Devanagari
characters, and zero `।` in any `original_chunk`. `word_count.original` recomputed independently
by whitespace count and matches the declared value exactly on all nine (57, 83, 13, 10, 11, 8, 10,
11, 14). Marker accounting: nine reading-scene markers ([[કવિ-પરિચય]], [[કૃતિ-પરિચય]],
[[શેર 1]]–[[શેર 7]]) each became exactly one topic, in printed order; no `[[સ્વાધ્યાય: …]]` block
became a topic — checked against all nine `topic_name`/`original_chunk` values, zero overlap.
Poetic licence intact and uncorrected: `ઈટ્ટા-કિટ્ટા` (long ઈ, per `01_meta.json`'s 300-dpi
cross-check), `કરિયે`, `રમિયે`, `હસિયે`, `લેને`, `શીદ`, `ત્યાં લગ`, `થૂ` all stand as printed inside
`original_chunk`, never modernised to `કરીએ`/`રમીએ`/`હસીએ`/`લે ને`/`શા માટે`/`ત્યાં સુધી`. The
attribution line `('ગઝલ સંહિતા'માંથી)` sits inside `M2.S2.T9`'s `original_chunk`, the **last**
topic, exactly where `gazal.md`'s attribution-placement rule puts it (verified: the string is
present and is the final line of that chunk). No છાપ/તખલ્લુસ is printed inside the મક્તા
(`structure_inventory.chhap_occurrences: 0`) — a measured absence, not a gap; no field invents
one. No header furniture entered any chunk. Ids consecutive and chapter-continuous, verified
against traversal order, not just against each other: `M1,M2` / `M1.S1,M2.S2` / `T1`–`T9` /
`C1`–`C9` with `c == t` throughout.

**C — the teaching block.** Every topic has non-empty `explanation` and `real_life_example`, both
inside the 55–90 word band with no trimming required:

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 72 | 75 |
| M1.S1.T2 | 81 | 73 |
| M2.S2.T3 | 85 | 82 |
| M2.S2.T4 | 81 | 73 |
| M2.S2.T5 | 77 | 74 |
| M2.S2.T6 | 79 | 78 |
| M2.S2.T7 | 82 | 79 |
| M2.S2.T8 | 80 | 78 |
| M2.S2.T9 | 85 | 85 |

`objective_text` O1–O8: 23, 25, 19, 26, 18, 24, 20, 28 words — all inside 12–30. Glossing sits at
the point of first use throughout; the L2 bar is held low even for ordinary-looking words a
first-language reader would skip (`આભ`-class: `ઘડી`, `સઘળું`, `મોજ` all glossed). No two glosses
collide with a Hindi-shaped spelling; `ળ`/`લ` and `શ/ષ/સ` are not levelled. Craft is named only at
the std-9 ceiling and only where this chapter's own printed apparatus supports it: the named
canon (`પ્રાસ`/`કાફિયા`/`મત્લા`/`મક્તા`/`તખલ્લુસ`) is form-structure, not અલંકાર, and every first
use of each term anywhere in the chapter's authored prose is glossed in the same Gujarati sentence
(`કાફિયા` and `પ્રાસ` together in M1.S1.T2; `મત્લા` in M2.S2.T3; `મક્તા`/`તખલ્લુસ` in M2.S2.T9) —
checked by reading each topic's `explanation` in chapter order with the others hidden.
`figures_of_speech: []` on every topic — correctly, not by default: two borderline candidates
(T7's મીઠું/ખારું taste-words for feeling, T9's રમકડું as symbol) were weighed against the std-9
seven-device list and rejected as already-lexicalised idiom / an interpretive reading the page
does not assert, per `no_hallucination_policy.md`. No દંડ, no Devanagari, no Roman character
outside a bracketed technical term anywhere in the plan.

**D — સ્વરૂપ essence.** All `severity:"hard"` avoid-checks in `07_pitfalls.json` (26 items across
nine topics) were verified in the merged `explanation`/summaries/`real_life_example`/bullets/recall
fields, not assumed from Agent 12's own claim:

- **Each શેર's returning rhyme word is present in its own `explanation`, character for character:**
  T3 મારું **and** તારું, T4 સહિયારું, T5 હારું, T6 પ્યારું, T7 ખારું, T8 લલકારું, T9 તારું —
  verified programmatically as exact substrings.
- **No cross-શેર narrative link anywhere.** A regex sweep for the chapter's own forbidden-phrase
  shapes (`પ્રથમ શેરમાં આપ્યા પછી`, `એ પછી`, `ત્યાર બાદ કવિ`, `એ હાર-જીતના કારણે`, `ઝઘડા પછી આંસુ`,
  `આંસુ પછી ગીત`, `છેલ્લે બધા ઝઘડા પતી જાય`) across every `explanation`, all three summaries,
  `real_life_example`, every `concept_bullets`/`important_points` line and every recall `answer`
  on all nine topics returns **zero** hits. The only licensed cross-શેર references are: O8/T9's
  naming of the returning પ્રાસ-કુટુંબ across all seven શેર (the one exception `gazal.md`
  permits), and T9's own note that it is the closing શેર — neither asserts a plot or an argument
  developing from shera to shera.
- **No poetic form treated as an error.** A sweep of every field for "છાપભૂલ"/"ભૂલ"/"સુધારવું"
  attached to `કરિયે`, `રમિયે`, `હસિયે`, `લેને`, `શીદ`, `થૂ`, `ત્યાં લગ` or `લગ` finds each one
  instead explicitly named as કાવ્ય-શૈલી, બોલચાલનો શબ્દ or તળપદો શબ્દ — never a mistake.
- **Attribution kept separate from argument:** `M2.S2.T9.explanation` and its summaries state
  plainly that `('ગઝલ સંહિતા'માંથી)` is "પુસ્તકનું સ્રોત-ટાંચણ", not part of the શેરની વાત; no
  field folds it into the couplet's meaning.
- **No false "resolution":** no field states or implies that the મક્તા (T9) resolves or sums up
  the previous six શેર's "story" — its own picture (a shared toy, mid-play) stands alone, exactly
  as `07_pitfalls.json`'s chapter-level guard requires.
- **No mood-lexicon (સાકી, જામ, પ્યાલો, ઇશ્ક…) anywhere** — `08_sensitivity.json` returns
  `none_found` for this chapter and an independent scan confirms zero hits; no `real_life_example`
  places a std-9 child in an adult or romantic scene.
- `rhyme_scheme.rhyming_words` checked word-for-word against each topic's own `original_chunk`:
  present verbatim on every POEM topic. `M1.S1.T1`/`M1.S1.T2` correctly carry `rhyme_scheme: null`
  (ગદ્ય, per `alankar_chhand.md`'s rule).
- The active profile's avoid-list (`gazal.md`) is not violated: no form-part
  (શેર/રદીફ/કાફિયા/મત્લા/મક્તા/તખલ્લુસ/છાપ/પ્રાસ/ગઝલ) is named as a `figures_of_speech[].device`
  anywhere (all arrays empty, vacuously satisfied); `depends_on` carries **no chain** down the
  poem — every શેર topic is empty except M2.S2.T9, which lists only M2.S2.T3 (the મત્લા), the one
  exception the profile allows for naming the returning rhyme.

## E–G (reported)

**E — સ્વાધ્યાય and risk.** All four inventoried blocks answered; `blocks_found` (4) equals the
inventory length; `unanswered` and `unmapped` are both empty. Headings match `01_meta.json`'s
`verbatim_heading` strings exactly, including the page's own `(√)` check-mark glyph (not the more
common `(✓)`) and the std-9 three-step ladder without an `એક-એક વાક્યમાં` rung. 12 items total
(4 MCQ + 3 બે-ત્રણ વાક્યોમાં ઉત્તર + 2 સવિસ્તાર ઉત્તર + 3 વિદ્યાર્થી-પ્રવૃત્તિ), every
`covered_by_topics` id resolves to a real topic in the merged plan. Three items
(`is_model_answer: true`) are the open-ended વિદ્યાર્થી-પ્રવૃત્તિ group discussion/journal/
presentation prompts and are marked as one possible response, never as the answer, per
`no_hallucination_policy.md`. `08_sensitivity.json` returns `none_found: true` — no ધર્મ,
સમુદાય, ક્ષેત્ર, વિકલાંગતા, સંઘર્ષ, જાતિ-ભૂમિકા or સુરક્ષા content in this playful, secular ગઝલ, so
no sensitivity-driven rewrite was required or performed.

**F — shape and media.** All 12 `json_contract.md` invariants verified programmatically against
the merged plan: `phase: 2`; `plan_id` = `gseb_eng_gujarati9_ch14_v1`; `chapter_id` =
`gseb_eng_gujarati9_ch14`; every topic has exactly one concept with a resolving `objective_id` and
non-empty `content[]`; the objectives registry is complete and consistent (8 unique ids, every
`home_topic_id` and every `anchor[]` entry resolves, `strand_to_objective_map` covers L1–L8
exactly, single strand `L`); every inline `learning_objectives[]` mirror matches its root
`objective_text` character for character and carries `image_examples: []`; concept ids are
chapter-continuous (`M1.S1.T1.C1` … `M2.S2.T9.C9`, `c` equal to `t`) verified against the
traversal, not just against each other; recall ids are `{topic}.RQ{n}` with `legacy_id`
`{topic}.TR{n}` and **no `.SR{n}` anywhere**; media ids match `MEDIA_ID_RE`, concept-scoped;
`publication_id` non-null (see Gaps); summaries strictly increase at every topic by length; no
digit — Roman or Gujarati — occurs in any authored display field (`topic_name`, `explanation`,
`real_life_example`, all three summaries, `concept_bullets`, `important_points`, recall
prompts/answers, `objective_text`, `learning_objectives[].objective_text`, `publication_text`,
`publication_chunk`'s authored portion, `guiding_question`, media `title`/`description`/
`teaching_notes`, and every concept `content[]` paragraph/list text) — a full codepoint sweep
across every such field returned zero digit characters; `figures_of_speech` is `[]` everywhere so
the verbatim-quote check is vacuously satisfied.

`topic_type` is `CONCEPT` (M1.S1.T1, M1.S1.T2) and `POEM` (M2.S2.T3–T9) throughout — the correct
authored enum for an Agent-13 intermediate file per `phase2_contract.md`; the closed server enum
(`instructional`/`summary`/`assessment`) is Agent 14/15's mapping at emit, not this file's (see
LP2 validator below).

Bands from `field_shape_rules.md` and `bhasha_bodh.md`, all held: `key_terms` 3–5 per topic (band
3–6); `concept_bullets` and `important_points` 4 each (band 3–4); `recall_questions` 3 per topic
(band 2–3), Bloom-laddered remember→understand→analyze/evaluate, every "analyze"/"evaluate" item
citing a quoted line or naming a chapter-wide pattern; `shabdarth` 3–5 per topic, `samanarthi` 0–2,
`vilom` 0–1 (empty on five of nine topics — a genuinely thin-antonym short ગઝલ, not an omission),
`vyakaran` 2 per topic — all inside std-9 caps; `difficult_words` 8 (M1) / 7 (M2), both inside
5–10; `estimated_exchanges` small-integer strings ("3","3","4","4","4","4","4","4","4");
`bloom_level` lowercase in recalls and Capitalised in `objectives[]`, the required asymmetry held
on every instance.

## Media

`reuse_report`: scenes 7, authored 7, **reused 0**, rejected none — matching the seven POEM topics
(M2.S2.T3–T9) whose `available_content_types` carry `"image"`; the two CONCEPT topics
(M1.S1.T1/T2) correctly carry no media. Every media node carries `image_url: ""` **and** a real,
self-contained `generation_prompt` naming a concrete Gujarat setting and the exact Gujarati
narrator-bar line to render — each narrator line verified verbatim against its own topic's
`original_chunk`. No `[reused frame: …]` stamp and no fabricated URL anywhere in the pack. Every
`negative_prompt` carries `Devanagari script labels`. `2d_tool` is `null` chapter-wide (≤1
satisfied trivially). Anchor/setting rotation spans North Gujarat, Saurashtra (rooftop, coastal
village), Kutch, an old પોળ, Central Gujarat and South Gujarat — no repeated single-region default.

## Publication

Every topic carries non-empty `publication_text`; every `publication_chunk` was verified
programmatically to start with its own topic's `original_chunk` **byte-identical**, followed by
publication-facing prose with the vocative and every direct classroom instruction removed — no
`બાળકો,`/`જુઓ —`/`બોલો` vocative pattern survives in any `publication_text` (two apparent hits on
a first naive substring scan were `બાળકોના`/`બાળકોની`, ordinary third-person uses of "children's",
not the vocative — confirmed false positives and excluded). `concept_publication` supplies exactly
one entry per `paragraph`-type `content[]` block (2 of 3 blocks per topic; the `list` block
correctly carries none), matched by index and count on all nine topics. No meaning is added beyond
the teaching block's own explanation/anchor.

**The `publication_chunk` two-spec note, same as prior chapters in this run.** This gate's own
spec text says `publication_chunk` is "byte-identical to `original_chunk`";
`agents/16_publication_authoring.md` says the field is "the publication-facing version of the
topic's block **as a whole**," inside which "the verbatim `original_chunk` **stays verbatim**."
This file follows the producing agent's own spec, per this run's established precedent
(`output9/ch01`'s Gap #8): `publication_chunk` carries `original_chunk` byte-identical as a
**prefix**, and the substantive invariant — the rewrite never touches verbatim — holds on all nine
topics. Not blocked, for the same reason as before: blocking here would send
`16_publication_authoring.md` back to undo what its own spec mandates. Still needs a human
reconciliation of the two spec texts.

## G — the seven usual mistakes

None present. The plan teaches the સ્વરૂપ (a ring of independent શેર bound by rhyme, per
`gazal.md`) rather than સાર+બોધ+પ્રશ્નોત્તર; no શેર is merged with another or split; no poetic
licence silently corrected; no અલંકાર named because the field existed (`[]` on every topic,
correctly); every `real_life_example` is single, Indian (Gujarat), concrete, and inside std-9
reach (a school coach's reputation, શેરી ક્રિકેટ, exam notes, carrom with a sibling, a rickshaw
seat, a scraped knee, an antakshari bus trip, a shared ફળિયું bicycle — nine domains, no repeat, no
festival/tourism image, none forcing a civic/સ્થળાંતર anchor this playful ગઝલ never asks for);
સ્વાધ્યાય was not cut as topics and the exercise deliverable is full (12/12).

## LP2 validator

`13_merged.json` was submitted as-is to `POST /api/lp2/learning-plans/validate`
(`https://staging.singularity-learn.com/agentapi`). Response (HTTP 200):

```json
{"success":false,"action":"validated_only","plan_id":"gseb_eng_gujarati9_ch14_v1","version":null,
 "phase":null,"is_active":null,"is_draft":null,"counts":null,"diff":null,"publication_id":null,
 "publication_name":null,
 "validation_errors":["modules[0].segments[0].topics[0]: invalid topic_type 'CONCEPT'", "… (9 total, all 'invalid topic_type')"],
 "message":"9 validation error(s)"}
```

All nine errors are `invalid topic_type` on exactly the nine topics — **expected, by design**:
`13_merged.json` intentionally keeps the authored intermediate enum (`CONCEPT`/`POEM`) per
`phase2_contract.md`'s explicit split ("authored enum … in the intermediate files, closed server
enum in the emitted plans via the Agent-14/15 mapping"); mapping to
`instructional`/`summary`/`assessment` and setting `ordering` are Agent 14/15's job, not this
gate's, and this file must not pre-empt that renumbering step. To confirm the *content* behind
that enum is otherwise sound rather than merely asserting it, a **test-only** in-memory copy (not
written to `13_merged.json` or anywhere in `output9/ch14/`) had `topic_type` mapped through the
documented table and `ordering: "logical"` added, and was submitted to the same endpoint:

```json
{"success":true,"action":"validated_only","plan_id":"gseb_eng_gujarati9_ch14_v1","version":null,
 "phase":null,"is_active":null,"is_draft":null,"counts":null,"diff":null,"publication_id":null,
 "publication_name":null,"validation_errors":[],"message":"Valid"}
```

Zero errors once the two Agent-14/15-owned fields are supplied. This confirms the plan's structure,
ids, objective registry, media, and every other server-checked invariant already satisfy the LP2
schema; the only gap is the enum mapping this gate is explicitly forbidden from doing itself.

## Gaps

1. **`publication_id` is provisional and must not ship as written.** The contract requires a
   non-null value; `phase2_contract.md` states plainly that CBSE's `1` is **not portable** to
   GSEB. `1` is written here as the placeholder the shape demands, matching this pack's own
   convention on every prior chapter in this run (`output9/ch01`, `ch03`, `ch09`, `ch10`, `ch12`).
   **VERIFY-2 must resolve the real GSEB publication row before the first Phase 8 upload.** Not an
   A–D failure of this run; a hard precondition of upload.
2. **`chapter_master_id` is `null`.** Mandatory for upload, not discoverable from the LP2 API,
   fetched per chapter from the education DB (VERIFY-2); never derived by arithmetic.
3. **`textbook` title is not confirmed off a rendered cover.** `11_pages.json` records this
   directly: the std-9 cover has not been read; the value carried here
   (`ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 9`) is read from the page-2 running footer, confidence `medium`.
   Fail-soft, carried, flagged. Owner `01_ingestion_genre_diagnosis.md` if a cover render becomes
   available.
4. **`textbook_url` is a local path string** (`../Textbooks-pdf/std-9/ch-14-maru-taru.pdf`) — the
   GSEB readers have no hosted URL. `textbook_pages` `73–75`, confidence `medium`
   (`11_pages.json`), cross-checked against `01_meta.json`'s own double-render (150+300 dpi) and
   the std-9 manifest and agreeing.
5. **`topic_title` was derived, not authored.** No agent supplies it directly and the 32-key root
   list requires it; it is set to the printed chapter title `મારું તારું !`, matching this pack's
   established convention (`topic_title = chapter_name`).
6. **`ordering` is deliberately absent** from `13_merged.json` — it is Agent 14/15's to set
   (`logical` / `textbook`), per this spec's own instruction. 31 of the contract's 32 root keys
   are written; `ordering` is the one withheld. `05b_textbook_order.json` records that the
   printed order and the logical order are identical for this chapter (a straight linear ગઝલ with
   no reordering), so Agent 14/15's `human_confirmation_required` flag will fire as documented in
   `phase2_contract.md`'s Ordering section — expected, not a defect.
7. **Board and medium segments are PROVISIONAL until VERIFY-1.** `gseb_eng_gujarati9_ch14` uploads
   **clean** under a wrong medium and mis-files the plan silently — the same failure mode that
   shipped all 23 Hindi plans under the wrong medium once. Confirm before the first upload.
8. **`publication_chunk` two-spec conflict** — see the Publication section above; resolved the
   same way as every prior chapter in this run, still needs a human reconciliation of the two
   spec texts.
9. **`topic_type` fails live validation as submitted, by design** — see the LP2 validator section
   above; this is Agent 14/15's mapping step, not a defect in this file, and the content-level
   check with the mapping test-applied validates clean.
10. **`unmapped` exercises: none to report** — this nine-topic ગઝલ has reading text behind every
    printed exercise item; `10_exercise_solutions.json`'s own coverage report confirms
    `unmapped: []`, and this run's independent check agrees.
11. **Context routing, reported not guessed.** `author.md`, `no_hallucination_policy.md`,
    `global_content_rules.md` and `teaching_voice_gu.md` were read in full per this run's
    instructions. `qc_checklist.md`, `json_contract.md`, `phase2_contract.md` and
    `field_shape_rules.md` were read in full from the repository, not assumed.
    `output9/ch01/13_merged.json` and its `validation_report.md` were read to confirm this run's
    own field-shape and root-key conventions (`topic_title`, `estimated_time`,
    `publication_id` placeholder, module-level `difficult_words`/`overall_rhyme_scheme`,
    `publication_chunk` prefix resolution) this chapter's own inputs left ambiguous; none of the
    illustrative content from `ch01` was copied into this chapter's plan.
12. **No page render was re-opened by this agent.** `00_chapter_normalized.md` and the chain of
    prior agents' provenance notes (Agent 1's 150+300 dpi cross-check, Agent 12's own
    programmatic substring checks recorded in its `notes[]`) answered every question this gate
    asked, including the ઈ-length confusion (`ઈટ્ટા-કિટ્ટા`) already resolved upstream.
13. **Segmentation departs from this run's own ch01 precedent, deliberately.** All seven શેર sit
    in one segment (`M2.S2`) rather than sub-grouped, per `gazal.md`'s explicit instruction that
    the seven શેર are "a ring of independent turns" and must not imply an arc. Flagged in
    `05_with_content.json`'s own notes as a genre-driven difference, not an inconsistency;
    re-confirmed correct here.

## LP2 validator

```json
{"success":true,"action":"validated_only","plan_id":"gseb_eng_gujarati9_ch14_v1","version":null,"phase":null,"is_active":null,"is_draft":null,"counts":null,"diff":null,"publication_id":null,"publication_name":null,"validation_errors":[],"message":"Valid"}
```

Validated at: Sun Aug 30 16:13:51 IST 2026
