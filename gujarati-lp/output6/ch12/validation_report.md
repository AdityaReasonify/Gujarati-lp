# Validation Report — std 6, ch 12 · અજબગજબનો મેળો

સ્વરૂપ: `mahitiprad_gadya` — માહિતીપ્રદ / સાંસ્કૃતિક ગદ્ય (confidence: high)   explanation unit: એક માહિતી-ખંડ
Topics: 9   Objectives: 9   Images: 0/4   Exercises: 17/17 blocks (54 items, 0 unanswered)

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` → `13_merged.json` (31 root keys; `ordering` deliberately left
for Agent 14/15). Modules 2, segments 5, topics 9, concepts 11 (chapter-continuous C1–C11),
media 4, `2d_tool` 1.

## A–D (blocking)   **PASS**

**A — diagnosis and lens.** `genre_signals` records the four signals off the rendered page and the
blue intro box is quoted as evidence, not as the verdict; `genre_confidence: high`; one profile
loaded (`mahitiprad_gadya.md`), not a mixed chapter. Explanation unit is **એક માહિતી-ખંડ**, which is
this profile's unit. The five printed માહિતી-ખંડ markers map to nine topics, with the long second
ખંડ cut at its **fact-steps** (T2–T6), not at the paragraph — the profile's own rule and its hard
gate #3. Apparatus stayed out: the blue પ્રવેશપેટી, the two real photographs on folio 79, the
શબ્દાર્થ box and the un-numbered `જોડો :` picture box are all recorded in `marker_map.not_topics`.
`guiding_question` is derived from this chapter's own થાંભલો and ગોળની પોટલી and could fit no other
unit.

**B — verbatim and structure.** All 9 `original_chunk`s non-empty, Gujarati script (U+0A80–0AFF),
**no Roman letters, no Devanagari, no `।`** anywhere in the plan. Marker accounting is exact:
`00_chapter_normalized.md` prints 5 `[[માહિતી-ખંડ …]]` reading markers and 17 `[[સ્વાધ્યાય: …]]`
blocks; `marker_map` covers all 9 topics and **no સ્વાધ્યાય block became a topic**. Topic ids run
T1–T9 consecutively, segments S1–S5 across both modules, concepts C1–C11 chapter-continuous.
The printed Roman numerals `20 થી 25 ફૂટ` survive inside T3's `original_chunk` as provenance —
correct, and the only numerals in the reading text.

**C — the teaching block.** Every topic carries a non-empty `explanation` **and**
`real_life_example`. All 18 fields land inside the 55–90 band (explanations 57–78, examples 57–67);
all 9 `objective_text` inside 12–30 (18–23). Summaries strictly increase in every topic. No craft
label above the std-6 ceiling — no અલંકાર or છંદ named anywhere. Anchors are Indian, single and
inside a std-6 child's reach (નિશાળનો પહેલો દિવસ, નવરાત્રિના ચોકના ગરબા, શેરીની લખોટી, દાદીની
બાંધણી, ગામનો મેળો).

**D — સ્વરૂપ essence.** All twelve `mahitiprad_gadya` hard gates checked against the merged fields:

- #1 no topic carries `topic_category: "climax"` (introduction / core×7 / resolution) and no field
  names a વળાંક or a character's choice.
- #4 every proper noun in the teaching fields (અમદાવાદ, ગુજરાત, જેસાવાડા, દાહોદ, ગરબાડા, હોળી)
  traces to this chapter's own `original_chunk`. No other મેળો is named anywhere.
- #5 no scientific or technical term the chapter does not print; no correction of the chapter's
  account.
- #6 every topic carries at least one printed practice-word in `key_terms` in `શબ્દ — અર્થ` form
  (વીંધ·ફટકા·ટોચ·પોટલી, સોટી·વાંસ, હાટ·આભૂષણ·ઘરવખરી, ધજા·પ્રથા·સ્વયંવર, લોકમેળા; T1's own
  defining word મેળાપ).
- #7 no પછાત / અભણ / જંગલી / "આ લોકો" anywhere; **આદિવાસી પ્રજા** used exactly as printed in
  M2.S5.T8, inside the chapter's own ગૌરવ register.
- #8 the સ્વયંવર mention and the chapter's own correction
  `પરંતુ હવે મેળાનો હેતુ કન્યા પસંદગીનો રહ્યો નથી.` sit **in the same topic** (M2.S4.T7), in the
  chunk, in the explanation and in a recall answer.
- #10 no tacked-on બોધ; T8 and T9 quote the chapter's own ગૌરવની વાત and its closing appeal and
  teach them as the writer's move.
- #12 `figures_of_speech: []` and `rhyme_scheme: null` on all 9 topics; `overall_rhyme_scheme: null`
  on both modules. Expository ગદ્ય — `[]` is the complete answer, and nothing was invented to fill
  the field.

All **28 hard `avoid_checks`** from `07_pitfalls.json` and all **3 hard items** from
`08_sensitivity.json` are addressed:

| Hard sensitivity item | area | how it is met |
|---|---|---|
| M1.S3.T4 — સોટીઓ / pole-climbing must not become a re-enactable game | સુરક્ષા | example is the નવરાત્રિ ગરબા circle (watching, not doing); the apply recall asks the child to *describe* the circle at home |
| M1.S3.T5 — 20–25-foot climb and sudden jump must not be a dare | સુરક્ષા | example is turn-taking in a શેરી લખોટી game; the apply recall asks for onomatopoeic words, never "have you climbed" |
| M2.S5.T8 — named community must not be flattened or exoticised | સમુદાય | `આદિવાસી પ્રજા` printed form kept; explanation and all three recalls stay inside the chapter's ગૌરવ register |

The 8 sensitivity `areas[]` values are all drawn from the seven fixed labels (સુરક્ષા ×2,
જાતિ-ભૂમિકા, સમુદાય).

## E–G (reported)

- **Contract (F).** All 12 `json_contract.md` invariants hold on `13_merged.json`: registry
  complete and consistent (9 unique `objective_id`, every `home_topic_id`/`anchor[]` resolving,
  `strand_to_objective_map` covering L1–L9); every topic ≥1 concept with a resolving `objective_id`
  and non-empty `content[]`; `MEDIA_ID_RE` concept-scoped and matching `.C{c}`; recall ids `RQ{n}`
  with `legacy_id` `TR{n}` — **no `.SR{n}` anywhere**; `publication_id` non-null; summaries
  strictly increasing; **no digits in any display text** (names, explanations, examples,
  summaries, bullets, recall prompts and answers, concept names, `publication_text`, ભાષા-બોધ
  values, `difficult_words`).
- **`learning_objectives[]` built at merge.** Agent 2 left the inline mirror unset (04's own note).
  It is derived here mechanically — the root registry entry copied whole plus `"image_examples": []`
  — and verified character-for-character against the registry for all 9 topics. No authoring
  judgment was applied.
- **`topic_type` stays the authored enum.** All 9 topics are `CONCEPT`, per
  `phase2_contract.md` ("intermediate files, Agents 02–13, carry POEM | STORY_TELLING | CONCEPT |
  REVIEW"). The map to the closed server enum (`CONCEPT → instructional`) is Agent 14/15's at emit.
- **`genre` carries the slug.** `13_merged.json` writes `mahitiprad_gadya`, not `01_meta.json`'s
  Gujarati display name — 04's note flagged this and the merge honours it.
- **`ordering` not written**, per spec: Agent 14/15 sets it.
- **Exercises (E).** All 17 inventoried blocks appear in `10_exercise_solutions.json`;
  `blocks_found` = 17 = inventory length; `unanswered` is empty; 54 exercise entries, 23 marked
  `is_model_answer`. **`unmapped` is reported, not closed**: 10 items across 3 blocks
  (સમાનાર્થી ×5, વિશેષણ ×4, અંતાક્ષરી પ્રવૃત્તિ ×1) whose words occur nowhere in the reading text
  or the printed શબ્દાર્થ box, so no reading scene prepares them. No mapping was invented.
- **Agent 4's notes (reported, never blocking).** Thin segments — M1.S1 and M2.S4 hold one topic
  each; both are their own fact-cluster and the profile's "a definition and its consequence stay
  together" argues against fusing them. Uneven length — M2.S5.T9 is one printed sentence
  (18 words); the profile names this chapter and grants exactly this licence
  ("that is its own small topic, `topic_category: "resolution"`").
- **Whitelisted non-Gujarati.** No printed non-Gujarati content exists in this chapter, so no
  `extraction_notes[]` whitelist is in play. The only Roman text in the plan is machine-facing by
  design and is **not** a script failure: `generation_prompt` / `negative_prompt` (read by an image
  model with no context, per `field_shape_rules.md`), the `2d_tool` spec, and the romanized
  ભાષા-બોધ **key names** (`shabdarth`, `samanarthi`, `vilom`, `vyakaran`, and `shabd`/`arth`/
  `prakar` inside them), which `phase2_contract.md` requires be kept romanized. Every ભાષા-બોધ
  and `difficult_words` **value** is Gujarati script with no digits.
- **`vilom: []` on M1.S1.T1, M1.S2.T2, M1.S3.T4, M2.S5.T8.** A legitimate empty, not a gap.

## Media

`reuse_report`: **scenes 4, authored 4, reused 0, rejected []** — matching exactly the 4 topics
whose `available_content_types` carry `"image"` (T1, T4, T7, T8). Every media node carries
`image_url: ""` **and** a substantial authored `generation_prompt` (1.5–1.9 KB each); no
`[reused frame: …]` stamp and no fabricated URL anywhere. `negative_prompt` carries
`Devanagari script labels` on all four. Exactly **one `2d_tool`** in the chapter, on M1.S2.T3 —
a stage-builder assembled only from stages this chapter prints, in printed order, with no digits
in any child-facing label and no bride-choice element. `Images: 0/4` is the true count: no Gujarati
frame pool exists.

## Gaps

Honest absences, surfaced rather than filled:

1. **`textbook_url` is a local PDF path** (`../Textbooks-pdf/std-6/ch-12-ajabgajabno-melo.pdf`) —
   the GSEB readers have no hosted URL. Recorded by Agent 11 as its one gap.
2. **`chapter_master_id: null`** — the GSEB row is fetched from the education DB (VERIFY-2) and is
   never invented or derived. `upload_reference/chapter_master_map.json` is still a provisional
   all-null file. **Blocks upload, not this gate.**
3. **`publication_id: 1` is provisional.** The server rejects null, so the pack-wide provisional
   value is written (identical to ch01–ch11 of this grade), but `1` is **CBSE's publication row**
   and does not transfer. It must be replaced with the verified GSEB row at VERIFY-2 before the
   first Phase 8 run.
4. **`chapter_id` / `plan_id` board and medium segments are provisional until VERIFY-1.** A wrong
   medium uploads clean and mis-files the plan; `gseb_eng_gujarati6_ch12` was not reasoned out and
   must be confirmed against the live server.
5. **`subject_ref_id` and `medium_id` are `null`** — server-injected. No GSEB subject record is
   confirmed; null is the only correct value.
6. **Three unmapped exercise blocks** (10 items) — see E above. Reported, not mapped.
7. **`publication_chunk` is not byte-identical to `original_chunk`** — surfaced as a documented
   **contradiction between two policy files, not as an authoring defect.**
   `agents/13_assembly_validation.md` says "`publication_chunk` is byte-identical to
   `original_chunk`"; `agents/16_publication_authoring.md` says "The publication-facing version of
   the topic's block as a whole. The verbatim `original_chunk` stays verbatim **inside** it … only
   its surrounding prose" is rewritten. Agent 16 followed its own spec. The substantive invariant
   both files protect was verified mechanically on all 9 topics: **`original_chunk` appears
   byte-for-byte, unaltered, at the head of every `publication_chunk`** (no reflow, no re-spacing,
   no re-punctuation; the printed double spaces and the `.` full stops survive). Not blocked, and
   routing it to A16 would ask A16 to violate its own spec. The two files should be reconciled by
   whoever owns them.
8. **Four words in the printed શબ્દાર્થ box (પહેરવેશ, મરદ, મુછાળો, અવકાશ) appear nowhere in the
   chapter's reading text** — a printed fact of the page, recorded by Agent 1 and carried
   unchanged, not a transcription gap.
9. No `2d_tool` verification is possible at this stage; the spec is authored text and no tool was
   built.

## LP2 validator

*Filled in Phase 8.* Not run: `POST /api/lp2/learning-plans/validate` requires
`chapter_master_id` and a verified `publication_id` (gaps 2–3), both pending VERIFY-1/VERIFY-2.

---

**Verdict: A–D PASS. This run is complete at Agent 13** and hands `13_merged.json` to Agent 14 for
renumbering, `ordering`, and the `CONCEPT → instructional` enum mapping. Upload remains blocked on
VERIFY-1 / VERIFY-2, which is a provenance gate, not a content failure.

## LP2 validator

- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: output6/ch12/learning_plan_logical.json
- HTTP 200, validation_errors: [] (none)
- Result: PASS
