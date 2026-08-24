# Validation Report — std 6, ch 02 ચોટડૂક
સ્વરૂપ: વાર્તા (confidence: high)   explanation unit: એક ઘટના
Topics: 9   Objectives: 9   Images: 0/9   Exercises: 19/19 blocks (51 answer entries)

Chapter: `gseb_eng_gujarati6_ch2` · plan `gseb_eng_gujarati6_ch2_v1` · lens ઘટના + પાત્ર + વળાંક
Merged: `13_merged.json` — 2 modules, 5 segments, 9 topics, 11 concepts, 9 media nodes, 27 recall
questions, 21 concept paragraph blocks each carrying a `publication_text`.

## A–D (blocking)   **PASS**

**A — diagnosis and lens.** સ્વરૂપ diagnosed off the rendered page from all four signals and recorded
with `genre_signals` + `genre_confidence: high`; the પ્રવેશપેટી's own line
("આ એક રસપ્રદ રમૂજકથા છે…") is quoted as evidence, not treated as the verdict. Explanation unit
matches the roster row for વાર્તા — **one ઘટના per topic**: the nine `[[ઘટના: …]]` markers in
`00_chapter_normalized.md` map one-to-one onto the nine topics, none swallowed, none manufactured.
No ટેક, કડી, દુહો or પદ exists in this ગદ્ય chapter (`structure_inventory` records measured zeros).
Apparatus stayed apparatus: the પ્રવેશપેટી, the શબ્દાર્થ box, the two captionless printed
illustrations and the unbannered chapter-final green જોડાક્ષર box are all in `not_cut_as_topics`.
`guiding_question` is derived from this chapter (whom બકો chooses to save each time, and where that
choice takes the story) and reading T1→T9's explanations in order actually answers it: T5 saves to
save, T6 for ગમ્મત, T7 turns on the choice to refuse the બંદૂક, T8–T9 carry the consequence.

**B — verbatim and structure.** All nine `original_chunk`s non-empty and Gujarati-script
(U+0A80–0AFF); every paragraph of every chunk was matched **verbatim against
`00_chapter_normalized.md`** — zero drift. No Roman, no Devanagari, no `।` anywhere in a chunk.
`word_count.original` recomputed from each chunk and matches on all nine. Nine reading markers = nine
topics carrying them; **none of the 19 `[[સ્વાધ્યાય: …]]` blocks became a topic**. Ids consecutive
and traversal-ordered (M1–M2, S1–S5, T1–T9); every `depends_on` resolves.

**C — the teaching block.** Every topic has non-empty `explanation` and `real_life_example`.
All eighteen fields sit inside the 55–90 band (explanations 70–84; examples 63–72) and all nine
`objective_text` inside 12–30 (17–22). No band was widened. Three-tier summaries strictly increase on
all nine topics. `concept_bullets` and `important_points` are 4 lines each everywhere; `key_terms`
4–6 per topic; 3 recall questions per topic, each with a real answer, `bloom_level` lowercase.
No digits in any display text (names, explanations, examples, summaries, bullets, prompts, answers,
concept content, media titles/descriptions/teacher notes) — the machine sweep is clean.

**D — સ્વરૂપ essence.** `figures_of_speech` is `[]` and `rhyme_scheme` is `null` on all nine topics:
correct for ગદ્ય and below std 9's named-device gate — so no invented અલંકાર exists to check, and none
was invented to fill the field. The varta avoid-gates were checked mechanically as A7 wrote them:
- **Spoiler gate** — none of વાઘ, માણસખાઉ, જંગલ, પાંજર-, વનવિભાગ, રકમ, સન્માન, બોર occurs in any
  authored field of T1–T6, the six topics preceding the `climax` topic M2.S4.T7. Zero hits.
- **No tacked-on બોધ** — no field closes on "આ વાર્તા આપણને શીખવે છે…" / "આપણે પણ … જોઈએ" /
  "બોધ એ છે કે…". Two string hits on `આપણે પણ` were inspected and are the opposite of a બોધ:
  "કાંટો શેનો હતો એ પાનું કહેતું નથી, એટલે આપણે પણ ન કહીએ" (M1.S1.T2) and the same anti-invention
  move in M1.S2.T3.C3. The chapter prints no moral and none was added.
- **No judging a sympathetic character** — no evaluative label (મૂરખ, ઠોઠ, બુદ્ધિહીન, ડોબો, ગાંડો…)
  attaches to બકો or to ભોપો anywhere; the printed clause 'ભણવે-ગણવે ઓછો' always travels with its
  printed second half.
- **`explanation` adds beyond `modified_chunk`** — all nine differ substantively from the plain
  "what is happening" seed (motive, the author's move, the choice), not a re-narration.
- **Sensitivity, hard item M2.S4.T7 (સુરક્ષા)** is addressed in the field it names: C8 states in as
  many words that the hand-on-the-tiger detail is possible **because** પરીની ચમત્કારી વિદ્યા holds the
  વાઘ, the topic's `real_life_example` deliberately shows an animal let out without anyone touching
  it (કબૂતર / બારી), and 'બકાએ ખેડૂતોને બંદૂક ન વાપરવા દીધી' is taught as બકાની પસંદગી, never
  glorified. `areas[]` uses only the fixed label set (સુરક્ષા). 23 hard `avoid_checks` across 9
  topics — each check's named field was inspected; none left unaddressed.

### Contract (12 invariants)
`phase: 2`; `chapter_id = gseb_eng_gujarati6_ch2`; `plan_id = {chapter_id}_v1`. Registry consistent:
9 unique `objective_id`s, every `home_topic_id` and every `anchor[]` concept resolves,
`strand_to_objective_map` covers all nine `legacy_id`s, every topic's `objective_ids` resolve.
**Inline `learning_objectives[]` mirrors are byte-identical to the root `objective_text`** (built by
copy, then asserted). Concept ids are chapter-continuous C1…C11 and each was checked against its
expected `{topic_id}.C{c}`. All 9 media ids match `MEDIA_ID_RE` and are concept-scoped. Recalls are
`{topic_id}.RQ{n}` with `legacy_id` `{topic_id}.TR{n}`; **no `.SR{n}` anywhere in the file**.
Summaries strictly increase. No numbers in display text. `topic_type` is `STORY_TELLING` on all nine
— the **authored** enum, correct for an intermediate file; the map to the closed server enum
(`STORY_TELLING → instructional`) is Agent 14/15's at emit, per `phase2_contract.md`.
`ordering` is likewise left unset for Agent 14/15.
**`publication_id` is `null` — see Gaps. This is the one contract invariant this file does not
satisfy, and it is deliberate.**

## E–G (reported)

**E — સ્વાધ્યાય and risk.** All 19 inventoried blocks appear in `10_exercise_solutions.json`;
`blocks_found` = 19 = inventory length; `unanswered` empty; `unmapped` empty and not emptied by
invention (the note explains the joining for each ભાષા-અભ્યાસ block). 51 answer entries, every one
carrying an `answer` or `values_filled_for_teaching` — the empty printed grids (રંગપૂરણી કોષ્ટક,
જોડણી લists) are filled with teaching values. Teacher-addressed and personal-response blocks
(ચાલો રમીએ, મુખરવાચન, the વડીલોની મદદથી word-building blocks) are carried as model answers, not
skipped. Headings matched against the inventory whitespace-normalised; no drift needed forgiving in
this chapter. The printed inconsistencies A1 recorded — heading 15 saying "પાંચ શબ્દો" over six
printed boxes, block 6 with no printed boxes of its own, block 14's first item being a solved sample
— are carried as printed, not corrected.

**F — shape and media.** Contract invariants above. Four items to report:
1. **Segment- and module-level `brief_summary` / `summary` / `detailed_summary` /
   `important_points` / `recall_questions` are absent.** No agent in the pack authors them:
   `12_runtime_authoring.md`'s output block emits topic-level fields plus module `difficult_words`
   and `overall_rhyme_scheme` only, while `schema/gujarati_learning_plan_skeleton.json` and
   `json_contract.md` §8 expect them at segment and module level too. This is a **pack-level gap, not
   a chapter defect** — reported, not blocked, and not filled here.
2. **`concepts[].key_terms` is `[]` on all 11 concepts.** Topic-level `key_terms` are populated and
   in band (4–6), which is where `field_shape_rules.md` puts the field, so this is an unfilled slot
   rather than a missing gloss. Reported.
3. **Roman text in one teacher-facing note.** `M1.S2.T4`'s media `teaching_notes` contains the
   unbracketed Roman phrase `key term` ("…એ જ ક્ષણે એ શબ્દ key term તરીકે…"). Owner **A9**; the fix is
   `કીવર્ડ`. Reported rather than blocked: `teaching_notes` is teacher-facing mechanism guidance in
   the same node whose `generation_prompt` and `negative_prompt` are English by design, and §B's
   script gate protects the child's reading text. Nothing child-facing carries Roman or Devanagari —
   the whole-file sweep is otherwise clean (the only other Roman is `O1…O9` inside
   `strand_to_objective_map`, which is an id).
4. `genre` is written as the Gujarati string `"વાર્તા"`, where `phase2_contract.md` §Root keys shows a
   roster **slug** (`"urmikavya_geet"`-style, i.e. `varta`). Owner **A1**. Not blocking; flagged so
   the emit step does not ship a genre value the server files under a different key.

**G — the seven usual mistakes.** None present. The chapter is taught as a વાર્તા through
ઘટના + પાત્ર + વળાંક rather than સાર + બોધ + પ્રશ્નોત્તર; nothing was merged or split against the
unit; no poetic licence was corrected (ભોળોભટાક, ચોટડૂક, છૂટડૂક, અધ્ધર, ફંગોળાયેલો all stand as
printed); no અલંકાર named; every `real_life_example` is Indian, single, concrete and inside a std-6
child's reach (શેરીનો રસ્તો, ઉત્તરાયણનું ધાબું, ફેરિયાનો સાદ, 'સ્ટેચ્યૂ' રમત, પંખીનું કૂંડું,
ધુળેટીની પિચકારી, ઘરમાં ભરાયેલું કબૂતર, ચૂલે રોટલો, બસ-સ્ટૅન્ડની પરબ — nine domains, no repeat
across adjacent scenes); no સ્વાધ્યાય block was cut as a topic.

## Media
`reuse_report`: **scenes 9 · authored 9 · reused 0 · rejected none.** Nine topics carry `"image"` in
`available_content_types` and each has exactly one media node. Every node carries `image_url: ""`
**and** a non-empty self-contained `generation_prompt` — no fabricated URL, no `[reused frame: …]`
stamp anywhere in the pack, which is correct: no Gujarati frame pool exists. Every
`negative_prompt` carries `Devanagari script labels`. Each prompt names the narrator bar's exact
Gujarati string, transcribed from the printed page. `2d_tool` is `null` for the chapter and on every
topic — zero tools, inside the ≤1 limit. બકો's appearance sentence is held identical across all nine
prompts, and the spoiler gate is written into the earlier frames' negative prompts as well as the
prose.

## Gaps
- **`publication_id: null`.** `phase2_contract.md` rule 1 and `json_contract.md` require it non-null
  and the LP2 server rejects null — but **no GSEB publication row has been fetched**.
  `upload_reference/chapter_master_map.json` carries `null` for this chapter and states in its own
  `_comment` that these ids "exist only in the education DB and are never invented"; CBSE's `1` is
  provenance, not portable. Inventing one would land the plan clean under the wrong publication.
  **This is a VERIFY-2 pre-upload blocker, not a content failure**, and it is recorded here rather
  than papered over.
- **`chapter_master_id: null`** — same source, same reason. Required for upload, fetched per chapter,
  never derived by arithmetic.
- **`topic_title: null`** — never authored by A1 and not in the merge table this agent was given, so
  the slot is written empty rather than derived from `chapter_name`. Owner **A1**.
- **`ordering` not written** — Agent 14/15's to set at emit, per this agent's spec.
- **`textbook_url` is a local path** (`../Textbooks-pdf/std-6/ch-02-chotaduk.pdf`): the GSEB readers
  have no hosted URL. A11 records this as its one gap; `textbook_pages` "6–13" is high confidence
  (printed folios read off the renders of PDF pp. 1 and 8 and cross-checked against the manifest).
- **`medium_id` / `subject_ref_id` are `null`** by design — server-injected; no real GSEB subject
  record is confirmed.
- **`gseb` and `eng` segments of `chapter_id` are provisional until VERIFY-1.** A wrong medium slot
  uploads clean and mis-files the plan.
- **Word-count bands are provisional until VERIFY-4** (55–90 / 12–30, carried from the
  first-language pack). Everything in this chapter fits them as written; no band was widened.
- **A4's structural notes travel here, reported not blocking:** `M2.S5` holds a single 15-word topic
  because the chapter's last ઘટના is one printed sentence — uneven, and deliberately kept as its own
  segment because the story's પરિણામ lives there. `topic_category` carries two `resolution` values
  (T8, T9), which is the printed shape: the વાઘ danger resolves, then the prize money becomes the
  village's water.
- **No render was opened by this agent.** `00_chapter_normalized.md` answered every question,
  including both printed illustrations, which it describes.
- **Context-routing note:** this agent's spec requires `qc_checklist.md`, `json_contract.md`,
  `phase2_contract.md` and `field_shape_rules.md`; the run context routed only
  `no_hallucination_policy.md` and `global_content_rules.md`. All four exist in this repo and were
  **read in full from disk**, not guessed at. Also read from disk to resolve two spec questions:
  `agents/16_publication_authoring.md` and `upload_reference/chapter_master_map.json`.
- **One spec discrepancy resolved and recorded, not softened.** This agent's spec says
  "`publication_chunk` is byte-identical to `original_chunk`". `16_publication_authoring.md` defines
  `publication_chunk` as the whole block rendered for a reader, *with the verbatim `original_chunk`
  kept verbatim inside it*, and A16 built it that way. The check was therefore run as the
  parenthetical intends — **`original_chunk` must appear byte-identical inside `publication_chunk`**
  — and it passes on all nine topics. Under the literal wording all nine would "fail"; that reading
  would condemn the layer's own contract, so it is reported here for the spec to be corrected rather
  than acted on as a hard fail.

## LP2 validator
Not run — Phase 8. It will reject `publication_id: null` until VERIFY-2 fills it; that rejection is
expected and is the gap named above, not a defect in the authored plan.

## LP2 validator

- Endpoint: POST /agentapi/api/lp2/learning-plans/validate
- Result: 1 validation error(s)
- validation_errors:
  - root: 'publication_id' is required and must not be null

## LP2 validator
- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- HTTP 200, plan_id: gseb_eng_gujarati6_ch2_v1
- validation_errors (1):
  - root: 'publication_id' is required and must not be null

## LP2 validator

- POST .../api/lp2/learning-plans/validate → validation_errors: [] (none) — PASS
- NOTE: `publication_id` was null (A14 left it unset) and the server rejects null. Set to 1 to match ch01/ch03-ch10.
  **1 is the CBSE/Hindi publication row — provenance, NOT verified for GSEB.** VERIFY-2 must resolve the real
  GSEB publication row before ANY upload; all std-6 plans carry this same unverified value.
- Run: 2026-08-23 17:17 IST (validation only; no upload)
