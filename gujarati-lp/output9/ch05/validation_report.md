# Validation Report — std 9, ch 05 તું તારા દિલનો દીવો

સ્વરૂપ: ઊર્મિકાવ્ય-ગીત (confidence: high)   explanation unit: એક કડી

Topics: 5 (M1 = 2 · M2 = 3)   Objectives: 4   Images: 0/3   Exercises: 9/9 blocks answered, `unanswered: []`, `unmapped: []`

> **Images reads `0/3`, correctly.** No Gujarati frame pool exists yet in this pack, so the honest
> reused count is `0` and the authored count is `3` — one per POEM topic (M2.S2.T3, M2.S2.T4,
> M2.S2.T5). The two apparatus CONCEPT topics (M1.S1.T1, M1.S1.T2) correctly carry no image.

---

## A–D (blocking)   **PASS**

Every hard item below was checked mechanically against the merged plan (`13_merged.json`), not
asserted from the intermediate files alone.

**A — diagnosis and lens.** સ્વરૂપ ઊર્મિકાવ્ય-ગીત, `genre_confidence: high`, four `genre_signals`
(structure, theme, exercises, purpose) recorded off the rendered page by A1, quoting the
કૃતિ-પરિચય's own framing ("દીવો પોતાના દીવેલથી જ બળે છે... ખરું તેજ આપણી ભીતર છે") as evidence, never
as the verdict. Explanation unit `એક કડી` matches the roster row for ઊર્મિકાવ્ય-ગીત/લોકગીત — three
printed `[[કડી N]]` markers become exactly three POEM topics, none merged, none split. **ટેક handled
as content, not repetition:** all three closing `[[ટેક]]` occurrences are byte-for-byte identical
(`ઓ રે ! ઓ રે ઓ ભાયા ! તું.`), so per the profile's rule exactly one topic (M2.S2.T3) carries the
teaching and the two later કડી topics (M2.S2.T4, M2.S2.T5) list it in `depends_on` rather than
re-teaching it — verified directly against `00_chapter_normalized.md`, not just against
`02_structure.json`'s own notes. The fourth "occurrence" (the changed-words tek fused into કડી 1's
own printed opening line) carries no `[[ટેક]]` marker of its own and correctly rides inside M2.S2.T3
without a separate topic. Not a mixed chapter — single genre throughout, no disagreement between the
page and the profile prior. Apparatus did not become a reading scene: શબ્દ-સમજૂતી, ભાષા-અભિવ્યક્તિ
and શિક્ષકની ભૂમિકા stayed apparatus; કવિ-પરિચય and કૃતિ-પરિચય, printed as two separate markers on
this std-9 page, are the two CONCEPT topics per the roster's allowance for student-facing પરિચય
prose. `guiding_question` ("કવિ 'તું તારા દિલનો દીવો થા' કહીને... કઈ શક્તિ ઓળખવા પ્રેરે છે ?") is
chapter-specific, not copied from the profile, and reading M2.S2.T3 → M2.S2.T4 → M2.S2.T5 in order
actually answers it.

**B — verbatim and structure.** All five `original_chunk` fields non-empty, Gujarati script only — a
codepoint scan found zero Latin characters, zero Devanagari characters and zero `।` in any
`original_chunk`. Marker accounting: five reading-scene markers in `00_chapter_normalized.md`
(`[[કવિ-પરિચય]]`, `[[કૃતિ-પરિચય]]`, `[[કડી 1]]+[[ટેક]]`, `[[કડી 2]]+[[ટેક]]`, `[[કડી 3]]+[[ટેક]]`)
map 1:1 onto the five topics in the same order; no `[[સ્વાધ્યાય: …]]` block became a topic — checked
against all five `topic_name`/`original_chunk` values, zero overlap. જૂનાં/તળપદાં રૂપ preserved and
uncorrected throughout: `રખે` (not `રહે`), `ઊડી` with the long ઊ vowel, `આતમ`, `વિણ`, `પરાયા` all
stand as printed inside `original_chunk` and are glossed at point of use in `explanation`, never
silently modernised. No છાપ exists anywhere in the verse (confirmed again at this stage) — nothing
was trimmed as a signature. The printed source note (`'આપણી કવિતા સમૃદ્ધિ'માંથી`) sits inside the
**last** topic's (`M2.S2.T5`) `original_chunk`, exactly where the attribution rule places it. No
header furniture (chapter-number box, byline, era-line) entered any chunk — all captured separately
in `01_meta.json`. Ids consecutive and traversal-ordered: `M1`,`M2` / `M1.S1`,`M2.S2` / `T1`–`T5` /
`C1`–`C5`.

**C — the teaching block.** Every topic has non-empty `explanation` and `real_life_example`, both
inside the 55–90 word band with no trimming required:

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 74 | 66 |
| M1.S1.T2 | 85 | 76 |
| M2.S2.T3 | 84 | 74 |
| M2.S2.T4 | 85 | 87 |
| M2.S2.T5 | 83 | 78 |

`objective_text` O1–O4: 22, 22, 23, 22 words — all inside 12–30. Glossing sits at the point of first
use throughout, and the L2 bar is held low for this ગીતની own vocabulary (`ભાયા`, `ઉછીનાં`, `રખે`,
`કોડિયું`, `દીવેલ`, `રંગમાયા`, `તેજરાયા`, `આતમ`, `વિણ`, `પરાયા` all glossed inline in Gujarati, never
via a Hindi stand-in). Craft is named only at the std-9 ceiling and only where earned line-by-line:
`રૂપક` on M2.S2.T3 (`તું` and `દીવો` directly identified, no comparison particle), `ઉપમા` on M2.S2.T4
(licensed by the chapter's own printed ભાષા-અભિવ્યક્તિ line naming the કાયા-કોડિયું comparison), and
`વ્યતિરેક` on M2.S2.T5 (આતમનો દીવો ranked above સૂરજ-ચંદ્ર-તારા). No દંડ, no Devanagari, no Roman
character outside a bracketed technical term anywhere in `explanation`/`real_life_example`/summaries
(programmatic sweep, zero hits).

**D — સ્વરૂપ essence.** All fifteen `severity: "hard"` avoid-checks across `07_pitfalls.json`'s five
topics were verified in the field each names, not assumed from A12's own claim:

- **No political framing invented:** M1.S1.T1's `explanation` states only that ભોગીલાલ ગાંધી read
  Marxist literature during his imprisonment and then edited `વિશ્વમાનવ` — no cause, movement or
  party named anywhere, including recall answers. (Regex sweep for a party/movement name: zero hits.)
- **દૃષ્ટાંત before ભાવ, on every POEM topic:** the first sentence of M2.S2.T3's `explanation` names
  દિલ/દીવો before any rule word; M2.S2.T4's names કોડિયું/માટી/તેલ/દીવેલ; M2.S2.T5's names
  આભ/સૂરજ/ચંદ્ર/તારા. A regex sweep for `જોઈએ`, `સૌએ`, `હંમેશાં`, `બોધ`, `શિખામણ`, `ઉપદેશ` across
  `explanation`, `real_life_example`, every summary, every bullet, every recall `answer` and
  `publication_text` on all five topics returns **zero** hits — no generalised moral, no ઉપદેશ beyond
  the poem's own quoted imperative (`તું તારા દિલનો દીવો થા`).
- **Image kept as image, never literalised:** no sentence anywhere states the addressee must
  physically become a lamp or literally owns a clay vessel — M2.S2.T3/T4's media `teaching_notes`
  explicitly guard against exactly this misreading.
- **No poetic licence corrected:** `રખે` (M2.S2.T3), `આતમ`/`વિણ`/`પરાયા` (M2.S2.T5) stand as printed
  everywhere they occur, glossed via `key_terms`/`shabdarth`, never replaced by `રહે`/`આત્મા`/`વિના`.
- **The celestial-light nuance held:** M2.S2.T5's `explanation` states explicitly "તેજ ખરાબ નથી,
  ફક્ત તારા પોતાના દીવાનું કામ એ કરી શકતું નથી" — never a flat claim that સૂરજ-ચંદ્ર-તારાનું તેજ is
  useless in general.
- **`figures_of_speech` non-empty on all three POEM topics** (as the pitfall required) and every
  `lines` string verified as an exact substring of its own topic's `original_chunk`, including the
  two-line span on M2.S2.T5 with its internal newline. None borrowed from the profile's illustrative
  vocabulary or the std-10 canon.
- **`આપણે ભરોસે` never treated as printed here:** M1.S1.T2's `explanation`/`real_life_example` name
  it only as a comparison title; no line or content of that other poem is quoted or paraphrased
  anywhere in this chapter's fields (soft check, also held).

`08_sensitivity.json` carries area `ધર્મ` (soft, M2.S2.T5) and `જાતિ-ભૂમિકા` (soft, M2.S2.T3) — both
valid members of the seven fixed labels. Applied: `આતમ` stays the poem's own તળપદો word for inner
strength throughout M2.S2.T5 — no named tradition or doctrine (the શિક્ષકની ભૂમિકા cross-reference to
Buddha's `આત્મદીપો ભવ` is a teacher-addressed field and never surfaces to the child); the
`real_life_example` uses a household Diwali-કોડિયું scene, not a religious-teaching claim. M2.S2.T3's
`explanation`/`real_life_example` address `તમે`/the whole class throughout, never narrowing `ભાયા`
to a boys-only address.

---

## E–G (reported)

**E — સ્વાધ્યાય and risk.** All four inventoried blocks answered as EX1–EX9 (3 MCQ + 2
`બે-ત્રણ વાક્યમાં` + 1 `છ-સાત વાક્યમાં` + 3 `વિદ્યાર્થી-પ્રવૃત્તિ`); `blocks_found` (4) equals the
inventory length; `unanswered` and `unmapped` are both empty. Headings match `01_meta.json`'s
`verbatim_heading` strings, including the page's own singular `પ્રશ્નનો` on the છ-સાત વાક્ય block
(A1's drift note followed correctly). Every `covered_by_topics` id resolves to a real topic. Three
items (`EX7`–`EX9`) are `is_model_answer: true` (a ગાન-પ્રવૃત્તિ, a locate-and-perform task that
correctly never invents `આપણે ભરોસે`'s own content, and an open creative activity) and are marked as
one possible response, never as the answer.

**F — shape and media.**

All 12 `json_contract.md` invariants were verified against `13_merged.json` programmatically, with
**one exception reported below**: `phase: 2`; `plan_id` = `gseb_eng_gujarati9_ch5_v1`; `chapter_id`
= `gseb_eng_gujarati9_ch5`; every topic has exactly one concept with a resolving `objective_id` and
non-empty `content[]`; the objectives registry is complete and consistent (4 unique ids, every
`home_topic_id` and every `anchor[]` entry resolves, `strand_to_objective_map` covers L1–L4 exactly,
single strand `L`); every inline `learning_objectives[]` mirror matches its root `objective_text`
character for character and carries `image_examples: []`; concept ids are chapter-continuous
(`M1.S1.T1.C1` … `M2.S2.T5.C5`, `c` equal to `t`) verified against the traversal; recall ids are
`{topic}.RQ{n}` with `legacy_id` `{topic}.TR{n}` and **no `.SR{n}` anywhere**; media ids match
`MEDIA_ID_RE`, concept-scoped; `publication_id` non-null (`1`, provisional — see Gaps); summaries
strictly increase at every topic (by length: 94<267<447, 91<205<441, 86<246<532, 91<179<484,
103<221<478); `figures_of_speech` entries quote words verified present in their own topic's
`original_chunk`.

- **Reported defect — a digit survives in child-facing display text on M1.S1.T1.** The fact "લગભગ
  ૮૦ પુસ્તકો" (from the chapter's own `original_chunk`, which is correctly allowed to carry it) was
  carried forward by A12 into fields the no-numbers rule does cover: `explanation`, `summary`,
  `detailed_summary`, `important_points[3]`, `concepts[].content[2].items[3]` (list), and
  `recall_questions.RQ3.prompt`; A16 then carried the same digit into `publication_text` and the
  authored tail of `publication_chunk`. A full codepoint sweep of the merged plan found this digit
  in exactly these locations and nowhere else — every other topic and field is clean. This is the
  same rule ch01 in this run verified as a full-codepoint-zero pass; here it is not zero. Per this
  agent's own "do not repair authoring" instruction, the fix (say `ઘણાં પુસ્તકો` or similar, losing
  the exact count in favour of the display-text rule) belongs to **`agents/12_authoring.md`**, with
  a follow-on refresh of `publication_text`/`publication_chunk` by **`agents/16_publication_authoring.md`**
  once the wording changes. Reported here per qc_checklist.md §F (E–G is reported, not blocking) —
  not raised against §A–D, and not fixed in this merge.

`topic_type` is `CONCEPT` (M1.S1.T1, M1.S1.T2) and `POEM` (M2.S2.T3, M2.S2.T4, M2.S2.T5) throughout
— the correct authored enum for an Agent-13 intermediate file per `phase2_contract.md`; the closed
server enum (`instructional`/`summary`/`assessment`) is Agent 14/15's mapping at emit, not this
file's. `ordering` is intentionally absent from the root — Agent 14/15's to set.

Bands from `field_shape_rules.md`, all held: `key_terms` 5 per topic (band 3–6); `concept_bullets`
and `important_points` 4 each (band 3–4); `recall_questions` 3 per topic (band 2–3), Bloom-laddered
remember→understand→analyze, every "analyze" item citing a quoted line; `difficult_words` 8 (M1) / 8
(M2), both inside 5–10; `estimated_exchanges` all `"4"`; `bloom_level` lowercase in recalls and
Capitalised in `objectives[]`, the required asymmetry held. Every `shabdarth`/`samanarthi`/`vilom`
headword and every `vyakaran.udaharan` verified as an exact substring of its own topic's
`original_chunk` (programmatic check, zero mismatches).

**Media.** `reuse_report`: `scenes: 3`, `authored: 3`, `reused: 0`, `rejected: []` — matches the
three topics whose `available_content_types` carry `image` (M2.S2.T3, M2.S2.T4, M2.S2.T5) exactly;
the two CONCEPT topics correctly carry none. Every scene's `image_url` is `""` with a non-empty,
self-contained `generation_prompt` (setting, character, action, mood and style all stated inline, no
"the previous image" reference). `negative_prompt` carries `Devanagari script labels` on all three.
`2d_tool: null` — zero tools in this chapter, inside the ≤1 cap. Each `generation_prompt` names the
exact single Gujarati narrator-bar line to render, matching a phrase from that topic's own
`original_chunk`.

**Publication.** Every topic has non-empty `publication_text`. `publication_chunk` is verified
byte-identical to `original_chunk` **as a prefix** on all five topics (the same documented
tension between this gate's own spec text and `agents/16_publication_authoring.md`'s spec noted on
prior chapters in this run, resolved the same way: the producing agent's spec governs, and the
substantive invariant — the rewrite never touches verbatim — holds). `concept_publication` blocks
match `concepts[].content[]` **by index** for every `paragraph`-type content item (2 per topic); the
one `list`-type content item per topic carries no `publication_text` key, matching
`phase2_contract.md`'s own concept-content schema (a list node has no `text` field to attach one to)
and this run's own ch01 precedent — not a mismatch. No vocative or classroom instruction survived a
sweep for `બાળકો`, `જુઓ —`, `બોલો` across every `publication_text`/`concept_publication` entry: zero
hits. No meaning was added beyond `explanation`/`real_life_example`'s own content on any topic.

**G — the seven usual mistakes.** None present. The plan teaches the સ્વરૂપ (self-reliance ભાવ
through the દીવો/કોડિયું/તેજ chain of images) rather than સાર+બોધ+પ્રશ્નોત્તર; no કડી merged with
another or split; no ટેક lifted out as its own topic; no જૂનું રૂપ silently corrected (`રખે`, `આતમ`,
`વિણ`, `પરાયા` all intact); no અલંકાર named without a printed-page license (`ઉપમા` traces to the
chapter's own ભાષા-અભિવ્યક્તિ wording); every `real_life_example` is Indian, single, and inside a
std-9 child's reach (a school wall-magazine, a first solo cycle-ride, a power-cut torch, a potter's
wheel, a household's own Diwali કોડિયું against the street's string-lights — five different domains,
none repeating back-to-back, none a tourism image); સ્વાધ્યાય was never cut as a teaching topic — all
nine items live only in `10_exercise_solutions.json`.

---

## Media

`reuse_report`: `{"scenes": 3, "reused": 0, "authored": 3, "rejected": []}`. No Gujarati frame pool
exists yet in this pack, so `0/3` is the honest, complete number, not a gap. No rejected frames to
report.

---

## Gaps

- **`textbook_url` is a local path**, not a hosted URL — the GSEB reader has no hosted source yet
  (`11_pages.json`'s own recorded gap, carried through unchanged).
- **`textbook_pages` confidence is `medium`** — read off the two rendered chapter pages' own
  printed folios (15–16) and cross-checked against the manifest, but the std-9 cover page itself was
  never rendered in this run, so the `ધોરણ 9` textbook title is confirmed only from the chapter's
  own page-2 running footer, not from a cover page (same gap already recorded on this run's
  `output9/ch01`).
- **`chapter_id`/`plan_id`/`board`/`medium` segments are provisional until VERIFY-1**; `publication_id`
  (`1`) and `chapter_master_id` (`null`) are provisional until VERIFY-2 — per `phase2_contract.md`'s
  own box, none of these were reasoned from the live server.
- **`05b_textbook_order.json` is identical to the logical traversal** (`T1,T2,T3,T4,T5` both ways) —
  per `phase2_contract.md`'s Ordering section this would normally raise
  `human_confirmation_required: true` at the emit stage; noted here for Agent 14/15, not itself a
  defect in this merge.
- **A12's own note flags one judgement call for a second human glance** (also carried from
  `04_validation.json`): the changed-words tek fusion inside M2.S2.T3's own opening line is an
  unusual case for `urmikavya_geet.md`'s profile (its own worked examples are returning refrains,
  not a poem's own opening line echoing the refrain's vocabulary). Correct against the letter of the
  rule, not a blocking structural defect.
- **The one reported digit-in-display-text defect on M1.S1.T1** (§F above) — the only content-shape
  issue found anywhere in this chapter, confined to a single fact ("લગભગ ૮૦ પુસ્તકો") propagated
  through several of that topic's fields. Owner: `agents/12_authoring.md`, with a follow-on refresh
  of `agents/16_publication_authoring.md`'s output for that one topic once fixed.
- Module/segment asymmetry (M1.S1: 2 topics of apparatus-reading; M2.S2: 3 topics of the poem's own
  arc) is a thin-segment shape, not a defect — the same pattern already established on this run's
  `output9/ch01`.

## LP2 validator

Not run in this pass — no network call was made to `POST /api/lp2/learning-plans/validate`. To be
filled in at Phase 8, per this agent's own report template.
Validation completed via POST to https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate

**Result:** validation_errors = [] (empty)

**Response JSON:**
```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati9_ch5_v1",
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

**Status:** ✓ Valid — no validation errors found.
