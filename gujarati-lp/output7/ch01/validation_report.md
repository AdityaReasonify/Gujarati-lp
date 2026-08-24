# Validation Report — std 7, ch 01 · સુંદર સુંદર
સ્વરૂપ: ઊર્મિકાવ્ય-ગીત (confidence: high)   explanation unit: એક કડી
Topics: 5   Objectives: 5   Images: 0/5   Exercises: 49/49 (14/14 blocks)

## A–D (blocking)   **PASS**

**A — diagnosis and lens.** ઊર્મિકાવ્ય-ગીત diagnosed off the render from all four signals
(`01_meta.json` `genre_signals`), confidence high. The roster's unit for this profile is **one કડી**
and the cut is one કડી per topic: four printed કડી → four topics, plus the three flush-left
આરંભની પંક્તિઓ carrying the first refrain as M1.S1.T1. The blue પ્રવેશપેટી is quoted as evidence of
form, never as the verdict. **ટેક handled as content:** the refrain
`વિભુ હશે તો કેવા સુંદર, એવું થાતું મુજ મનમાં` is printed in full five times with no word changed
(`tek_words_changed: false`), so it is taught once in M1.S1.T1 and carried by `depends_on` on the
other four — not re-taught, not lifted out as a topic of its own. Apparatus stayed apparatus: the
teacher-addressed પ્રવેશપેટી, the શબ્દાર્થ box and the fourteen સ્વાધ્યાય blocks are in no topic.
`guiding_question` is derived from this chapter's own arc and the topics answer it in order.

**B — verbatim and structure.** All five `original_chunk`s non-empty, Gujarati only
(U+0A80–0AFF), no Roman, no Devanagari, no `।` introduced, line breaks preserved, single-column
verse so no read-down hazard. Marker accounting: `[[કડી 1–4]]` = 4 markers → 4 topics carrying
them; `[[આરંભની પંક્તિઓ]]` ×1 → M1.S1.T1; `[[ટેક]]` ×5 → 1 topic per the identical-refrain gate;
**zero of the fourteen `[[સ્વાધ્યાય: …]]` blocks became a topic.** `મુજ` and `થાતું` survive
unmodernised everywhere they are quoted. Ids consecutive (M1, M2; M1.S1, M1.S2, M2.S3; T1–T5;
C1–C5 chapter-continuous); every cross-reference resolves.

**C — the teaching block.** Every topic has non-empty `explanation` and `real_life_example`.
Word counts, all inside band: explanations 85 / 87 / 85 / 84 / 89; examples 70 / 77 / 73 / 70 / 68
(band 55–90). `objective_text` 27 / 26 / 24 / 25 / 26 (band 12–30). No band was widened and no
prose needed trimming. Craft is named at the std-7 ceiling only — sound described in the child's
words, **no** device label anywhere (`પુનરાવર્તન`, `ધ્રુવપંક્તિ`, `ટેક`, `પ્રાસ`, `અલંકાર`, `છંદ`
all absent from every child-facing field). Summaries strictly increase on all five topics
(25<42<108, 23<51<96, 19<41<83, 23<46<102, 20<38<109 words).

**D — સ્વરૂપ essence.** All 19 `severity: "hard"` items in `07_pitfalls.json` verified addressed:
the slogan gate holds (`જોઈએ` occurs in no child-facing field of any topic); "feeling before
picture" holds — every explanation's first substantive clause names a word printed in that topic's
own chunk (સૂરજ / ઉષા / માછલી / તારા-આભ / ભાષા-હૈયું); the mandatory craft limb is present on all
five; the over-scientifying word lists are absent in full. `08_sensitivity.json` carries **no hard
item** — its single soft ધર્મ item (`areas: ["ધર્મ"]`, a valid label from the seven) is applied:
`વિભુ` is glossed as the everyday word for ઈશ્વર, the refrain is presented as the poet wondering
rather than as a claim, and T1's anchor is a courtyard sunrise, not a temple. `figures_of_speech`
is `[]` on all five topics per the std-7 craft ceiling — **no device was invented**, so the
lines-found-verbatim check passes vacuously.

**Contract (12 invariants).** All hold except the one recorded under Gaps. `phase: 2`;
`plan_id = {chapter_id}_v{version}`; every topic ≥1 concept with a resolving `objective_id` and
non-empty `content[]`; registry complete, `strand_to_objective_map` covers L1–L5; inline
`learning_objectives[]` mirrors match the root `objective_text` character for character;
`MEDIA_ID_RE` matches all five media ids, concept-scoped, `.C1`–`.C5` chapter-continuous; recalls
are `RQ{n}` with `legacy_id` `TR{n}` — **no `.SR{n}` anywhere**; no numbers in any display text
(digits appear only in ids, `word_count`, `textbook_pages` and `estimated_exchanges`, which is a
provenance/contract field, not display).

## E–G (reported)
- **E — સ્વાધ્યાય.** All 14 inventoried blocks answered, 49/49 items, item counts matching the
  inventory exactly (10+2+4+2+1+4+4+1+4+5+1+1+1+9). 21 items are flagged `is_model_answer` and 19
  carry `values_filled_for_teaching`; the પ્રવૃત્તિ, વાતચીત and personal-opinion blocks are
  answered as model answers rather than skipped. 12 items are **reported unmapped** — the three
  non-poem rows of શબ્દરચના and the nine શબ્દગમ્મત sentences — each with a stated reason; no
  mapping was invented to empty the list. Every `covered_by_topics` id resolves.
- **E — whitelisted script.** The five અનુવાદ answers (EX33–EX37) are written in Roman-script
  English on purpose, as the medium of instruction, and each says so in `teacher_note`. A
  script-purity flag against them would be a false positive; none was raised.
- **F — shape.** `topic_type` is `POEM` throughout, which is correct for an intermediate file;
  Agent 14 owes the `POEM → instructional` mapping at emit. `ordering` is deliberately **not**
  written here — it is Agent 14/15's. `chapter_id`/`plan_id` are frozen in PROVISIONAL form
  (`gseb_eng_gujarati7_ch1` / `_v1`) pending VERIFY-1; the medium slot is the medium of
  instruction, and a wrong value uploads clean.
- **F — root `genre` is the Gujarati display name, not the roster slug.** The plan carries
  `"genre": "ઊર્મિકાવ્ય-ગીત"`; `phase2_contract.md` shows a slug (`urmikavya_geet`, the form used
  in `active_genre_profiles`). Reported, not repaired — root fields are A1's
  (`agents/01_ingestion_genre_diagnosis.md`). Non-blocking: not one of the 12 invariants.
- **F — `teaching_lens` is `ચિત્ર + ભાવ + લય`**, where `urmikavya_geet.md` prints
  `ચિત્ર + ભાવ + અલંકાર`. This is a deliberate std-7 adaptation (the અલંકાર canon starts at std 9),
  it is consistent across A1, A4, A7 and A12, and the sung third is actually carried in the
  explanations. Recorded, not flagged.
- **G — the seven usual mistakes.** None present: no સાર+બોધ+પ્રશ્નોત્તર substitution, no merged
  કડી, no split પદ or lifted ટેક, no silently corrected licence (`મુજ`, `થાતું` intact), no
  invented અલંકાર, no adult or non-Indian anchor, no સ્વાધ્યાય cut as a topic.

## Media
`reuse_report`: **scenes 5, authored 5, reused 0, rejected []** — equal to the five topics whose
`available_content_types` carry `"image"`. Every node carries `image_url: ""` **and** a
self-contained `generation_prompt` (1111–1324 chars), as required while no Gujarati frame pool
exists; there is no `[reused frame: …]` stamp and no fabricated URL anywhere. Every
`negative_prompt` carries `Devanagari script labels`. `2d_tool` is `null` for the whole chapter
(≤1 satisfied). Media ids are concept-scoped `…C{n}.IMG1`; the routing-only `topic_id` key was
dropped at merge.

## Publication
All five topics carry `publication_text`; all five `publication_chunk`s **open with the topic's
`original_chunk` byte-identical** — the verbatim is untouched by the rewrite.
`concept_publication` matches `concepts[].content[]` by index and by count (2 paragraph blocks per
topic, indices [0,1], 10/10 landed). The classroom address is gone from every publication field
(`બાળકો`, `જુઓ —`, `બોલો`, `તમારા` all absent) while the glosses and readings survive; no meaning
was added.

*One reconciled spec conflict, recorded rather than hidden:* this agent's spec says
`publication_chunk` is "byte-identical to `original_chunk`", while `agents/16_publication_authoring.md`
— which owns the field — defines it as the topic's whole block **with the verbatim intact inside
it**. A16 followed its owning spec, and the binding intent ("the rewrite never touches verbatim")
is satisfied exactly. Treated as PASS; the two spec texts should be reconciled in one direction.

## Gaps
1. **`publication_id` is `null`, and it must not be for upload.** `upload_reference/chapter_master_map.json`
   holds `null` for `gseb_eng_gujarati7_ch1` — the GSEB publication row has never been fetched
   (VERIFY-2). This agent's spec asks for a non-null provisional value; the no-hallucination policy
   and the map's own `_verify_2` note forbid inventing one, and CBSE's `1` does not transfer. `null`
   is written and the gap is surfaced here. **Blocks Phase 8 upload, not this run.**
2. **`chapter_master_id` is `null`** for the same reason (VERIFY-2, fetched from the education DB,
   never derived by arithmetic). Also required for upload.
3. **`chapter_id` / `plan_id` board and medium segments are unverified** (VERIFY-1). A wrong medium
   uploads clean and mis-files the plan. A correction changes those two strings only.
4. **`textbook_url` is a local path**, not a hosted URL — the GSEB readers have none. Carried from
   `11_pages.json` as recorded, with the gap noted there too. Page range `1–4` is `confidence:
   high` (printed folios read off pp. 1 and 4 of the render, cross-checked against the board
   profile's std-7 row and manifest.json).
5. **The poet's byline is in the plan nowhere.** `- ધર્મેન્દ્ર માસ્તર 'મધુરમ્'` is printed in the
   **title zone above** the poem, not as an end-of-poem attribution, so A5 correctly declined to
   append it to the last topic's `original_chunk` (that would falsify the printed order) and
   recorded it in `00_chapter_normalized.md` and `01_meta.json`'s `extraction_notes[]`. The
   32-key root contract has no field for a poet's name, so it currently does not travel. Surfaced
   for whoever owns emit; not repaired here.
6. **`topic_title` was not authored.** No agent produced one and the root contract requires it; it
   is filled from `chapter_name` (`સુંદર સુંદર`), the same string `unit_title` already carries.
   Recorded so it is a decision, not a silent default.
7. **Render method gap, carried from A1.** The renders were supplied pre-rasterised and
   re-rendering was forbidden, so the spec's double-render cross-check was performed as a 3x–12x
   LANCZOS upscale pass on the same PNGs. That verifies glyph shape but cannot add optical detail
   a higher-dpi re-render would have. A1 recorded it as a method gap, not a clean double-render.
8. **One printed-glyph mismatch on record (A10).** Block 4's heading prints `ખરું (√)` on the page
   while `00_chapter_normalized.md` and `01_meta.json` record `ખરું (✓)`. `blocks_found` keeps the
   inventory string so the two files match. Cosmetic; reported.
9. **Non-blocking notes from A4, carried here as instructed.** Uneven topic length (M1.S1.T1 has
   four printed lines, the rest two each — permitted by the profile); lens thinness in the
   objectives, since resolved in the explanations; `bloom_level: "Evaluate"` on O5 sits above the
   std-7 recall ceiling but is justified by the chapter's own printed exercise
   (`કવિએ છેલ્લે … શા માટે કહ્યું હશે ?`) and applies to the objective label, not to a recall
   question — A12's recalls stop at `analyze`.
10. **Context routing.** The run context routed `no_hallucination_policy.md` and
    `global_content_rules.md` only, while this spec's inputs also name `qc_checklist.md`,
    `json_contract.md`, `phase2_contract.md` and `field_shape_rules.md`. All four were present on
    disk under `reference/` and were read in full. Nothing was inferred from an unread document.

## LP2 validator
Not run — filled in Phase 8. Expect one blocking server error until VERIFY-2 lands:
`publication_id` must not be null (`json_contract.md` rule 1). `chapter_master_id` is required by
the upload endpoint and is likewise null.

---
**Verdict: A–D PASS. `13_merged.json` written (31 root keys, 37 topic keys, 5 topics, 5
objectives, 5 media nodes).** No authoring was repaired by this agent, no band was widened, no id
was renumbered, no gap was closed by invention. The run is complete as a Phase-2 assembly; it is
**not yet uploadable** — items 1–3 under Gaps are Phase-8 blockers owned by VERIFY-1/VERIFY-2, not
by any authoring agent.

## LP2 validator

- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- Result: HTTP 200, success=false, action=validated_only, plan_id=gseb_eng_gujarati7_ch1_v1
- validation_errors (1):
  1. root: 'publication_id' is required and must not be null
