# Validation Report — std 8, ch 12 · ક્ષિતિ (ધીરુબેન પટેલ)

સ્વરૂપ: નાટક (એકાંકી) — profile `natak_ekanki.md` (confidence: **high**)   explanation unit: એક સ્ટેજ-બીટ (સંવાદ-ખંડ)

Topics: 10   Objectives: 10   Images: 0/10   Exercises: 15/15 blocks · 68 items (35 mapped, 33 reported unmapped)

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` → `13_merged.json` (31 of the 32 root keys; `ordering` is
Agent 14/15's and was deliberately not written). 3 modules / 6 segments / 10 topics / 15 concepts /
10 media nodes / 0 `2d_tool`.

---

## A–D (blocking)   **PASS**

**A — diagnosis and lens.** સ્વરૂપ diagnosed off the render on all four signals
(`genre_signals.structure/theme/exercises/purpose` in `01_meta.json`), `genre_confidence: "high"`,
with no signal conflict recorded. The intro box's own line — `"આ એક નાટક છે…"` — and the
performance-task tell (block 10, `આ એકાંકીના સંવાદો વર્ગખંડમાં હાવભાવ સાથે રજૂ કરો.`) are quoted as
*evidence* in `genre_signals`, never copied in as the verdict. `explanation_unit`
(`એક સ્ટેજ-બીટ (સંવાદ-ખંડ)`) matches the profile's નાટક/એકાંકી row identically across
`01_meta.json` and `05_with_content.json`. The chapter carries exactly one `[[પાત્રો]]` marker and
one continuous `[[સંવાદ: …]]` marker in `00_chapter_normalized.md` (no `પ્રવેશ`/`દૃશ્ય` numbering —
`structure_inventory.drushya_count: 1, ank_pravesh_count: 0`); per the profile's explicit rule that
the explanation unit is the stage-beat, not the printed marker, the two markers were correctly cut
into 10 stage-beat topics at entrances/exits/object-arrivals/knowledge-or-want changes —
`05_with_content.json`'s own notes record the marker-to-topic reasoning and count roughly 14
stage-changes against the 10 topics cut, under the profile's inflation ceiling. **The header topic
is its own topic** (`M1.S1.T1` bundles the `પાત્રો` cast list with the opening room-direction, per
the profile's std-8 header-signal row). Apparatus stayed apparatus: the blue પરિચય-બોક્સ, the
રૂઢિપ્રયોગ pre-block, the ચર્ચા-વિચારણા box and the ચેપ્ટર-ફાઈનલ કહેવત box are none of them topics —
all feed `01_meta.json`/exercises only. **The embedded historical `સ્થળ : પાટણ` (રાજા વિશળદેવ–જગડુશા)
play-excerpt inside સ્વાધ્યાય block 3 was correctly kept out of the topic chain entirely** — it is
comprehension apparatus, not part of ક્ષિતિ, and no topic's `original_chunk` contains any of its
lines (checked). `guiding_question` is derived from this chapter's own two-hinge plot (the false
મિલકતનો કાગળ → સંતોષની લાગણી) and the ten topics read in order visibly answer it.

**B — verbatim and structure.** All 10 `original_chunk`s non-empty, pure Gujarati-script
(U+0A80–0AFF); a full-document scan (every `original_chunk`, `modified_chunk`, `explanation`,
summaries, `concept_bullets`, `important_points`, `key_terms`, concept `content[]`,
`shabdarth`/`samanarthi`/`vilom`/`vyakaran`, recall prompts/answers, names, `objective_text`) finds
**0 unbracketed Roman characters, 0 Devanagari codepoints, 0 `।`** (the one Roman substring, `ST`
inside `M2.S3.T6.real_life_example`'s `ST બસ ડેપોમાં`, is the same std-6–8 real-life-anchor
abbreviation `field_shape_rules.md`/`qc_checklist.md` themselves name as a valid middle-standard
anchor — not a script-purity defect). રંગસૂચના survive character-for-character, including the
render-verified correction `બળ્યું` (retroflex ળ) in `M1.S1.T3` — `05_with_content.json`'s notes
record this was cross-checked against `_renders/page-02.png` against `00_chapter_normalized.md`'s
`બલ્વું` and surfaced loudly rather than silently patched upstream. Speaker labels and their words
match the printed order in every beat. No `[[સ્વાધ્યાય: …]]` block became a topic (checked against
all 15 inventoried group names and all 10 `topic_name`/`concept_name` values — no overlap). Ids run
consecutively M1–M3 / S1–S6 / T1–T10 / C1–C15 (chapter-continuous, verified against traversal
position programmatically) and every cross-reference resolves (see Contract).

**C — the teaching block.** All 10 topics carry non-empty `explanation` **and** `real_life_example`.
Word counts, all inside `field_shape_rules.md` bands, no band widened: `explanation` 74–88 words
(band 55–90), `real_life_example` 70–85 words (band 55–90), `objective_text` 18–27 words
(band 12–30). Glossing is inline, in Gujarati, at first use, calibrated for L2 (`આતુરતાપૂર્વક`,
`પંચાત`, `તંગ`, `કડાકૂટ` glossed though ordinary L1 vocabulary). Each `real_life_example` is one
concrete, Indian, std-8-reach anchor (a fisherman's family waiting on the shore, a rasoda pestering,
housework shared, an ST-bus-depot first meeting, a friend's slow build-up to bad news, a festival
sweet-exchange, a grandparent's kept secret) — `12_authoring.json`'s own domain ledger records the
rotation and no two adjacent topics repeat a domain. Std-8 craft ceiling held: `figures_of_speech`
is `[]` and `rhyme_scheme` is `null` on all 10 topics — correct for prose drama, not an omission
(std-8's own gate: named-device identification starts std 9).

**D — સ્વરૂપ essence.** All **20 `severity: "hard"` avoid-checks in `07_pitfalls.json`** (2 per
topic) plus its 4 chapter-level items were checked against the merged `explanation`/summaries/recall
answers and hold: no topic completes a trailing `ત્રણ ટપકાં` line (`ખબર પડત કે...`,
`એવી ઈચ્છા હતી કે એ...`, ક્ષિતિની ચિંતાનો જવાબ withheld till `M2.S3.T6`, her private-request reason
withheld till `M3.S5.T8`, the letter's falsity withheld till `M3.S6.T10`); no topic states a general
life-rule from a character's line (`M1.S1.T2`'s `દાસી` complaint, `M1.S2.T4`'s ખોટું-બોલવું line,
`M3.S6.T9`'s generosity all stay this-beat-specific); every રંગસૂચના named in a pitfall check
survives character-for-character in its topic's `original_chunk`, quoted rather than narrated-around
in `explanation`; nicknames (કિટી/કેતકી, સંતુ/સંતોષ, ચારુ/ચારુબાલા) are never treated as separate
people; `કડાકૂટ` (topic) vs `કડાફૂટ` (exercise word-bank) both stand exactly as printed in their own
location. No topic ends on બોધ/સંદેશ/શિખામણ/ઉપદેશ — the resolution stays with ક્ષિતિની ક્રિયા (કાગળ
ફાડવી, રહેવાનો નિર્ણય, ગુપ્તતાની શરત), not the blue box's printed line, which no field paraphrases.
The four **soft** `08_sensitivity.json` items (all જાતિ-ભૂમિકા) are followed as guidance, not
censorship: `M1.S1.T2`/`M1.S1.T3`'s real-life anchors show shared housework rather than normalising
one person carrying it alone; `M2.S3.T6` presents ક્ષિતિની appearance as her own choice, adding no
comment that a doctor/20-years-abroad woman "should" look different; `M3.S5.T8` keeps સંતોષની
`પરણ્યા વગર નહીં ખબર પડે` line as his own banter, never restated as a claim about unmarried women.
`figures_of_speech: []` is correct and vacuous — no device is asserted anywhere.

## Contract (the 12 `json_contract.md` invariants)   PASS

1. `phase: 2`; `chapter_id: gseb_eng_gujarati8_ch12`; `plan_id: gseb_eng_gujarati8_ch12_v1`. ✔
2. Every topic carries a non-empty Gujarati-script `original_chunk`, no unbracketed Roman/Devanagari. ✔
3. Every topic has ≥1 concept (15 total across 10 topics), each a valid `concept_id`, an
   `objective_id` resolving to the root registry, and non-empty `content[]`. ✔
4. Registry complete: 10 unique `objective_id`s (O1–O10); every `home_topic_id` and every `anchor[]`
   entry resolves to a real node; `strand_to_objective_map` covers L1–L10 one-to-one; every topic's
   `objective_ids` resolves. ✔ (programmatic check against the merged tree)
5. Inline mirrors: `learning_objectives[]` built at merge from the root registry, compared character
   for character — 10/10 identical, each carrying `image_examples: []`. ✔
6. Id grammar: M1–M3 / S1–S6 / T1–T10 match traversal position exactly; concepts run
   chapter-continuous C1…C15 (e.g. `M1.S2.T4.C4`, `M1.S2.T4.C5`); media match `MEDIA_ID_RE`
   (concept-scoped, `{concept_id}.IMG1`); recalls are `{topic}.RQ{n}` / `legacy_id` `{topic}.TR{n}`.
   **Zero `.SR{n}` anywhere** (this chapter authors no segment-level recalls). ✔
7. No સ્વાધ્યાય block is a topic; all 15 inventoried blocks are answered in
   `10_exercise_solutions.json` (`unanswered: []`, 68/68 items non-empty). ✔
8. Three-tier summaries strictly increase on all 10 topics by word count (verified programmatically,
   e.g. 17 < 35 < 95). ✔
9. No numbers in display text — a digit scan (Arabic and Gujarati numerals) over every `topic_name`,
   `explanation`, `real_life_example`, summary, `concept_bullets`, `important_points`, `key_terms`,
   recall prompt/answer, `objective_text` and concept `content[]`/`publication_text` returns **zero**
   hits. Digits survive only in ids, `word_count` and `textbook_pages`, and inside `original_chunk` /
   `publication_chunk`, where the page's own numerals belong. ✔
10. Media — see below. ✔
11. `figures_of_speech` is `[]` on all 10 topics, so no device is asserted that the lines do not
    carry (vacuously satisfied for this prose-drama chapter). ✔
12. Every reference resolves in the merged, still-frozen id set (renumbering is Agent 14's). ✔

`topic_type` is `CONCEPT`/`STORY_TELLING` — the intermediate-file authored enum; Agents 14/15 map it
to the closed server enum `instructional` at emit. `publication_id` is non-null (see **Gaps**).

## Exercises

All **15/15** inventoried સ્વાધ્યાય groups appear in `10_exercise_solutions.json`
(`coverage_report.blocks_found` = the inventory, exact string match on every `verbatim_heading`).
**68 item-level entries, all with a non-empty `answer`; `unanswered: []`.** **33 reported
`unmapped`**, never closed by inventing a mapping — and each carries a real reason: the six embedded
`સ્થળ: પાટણ` comprehension questions (a second, unrelated historical play-excerpt, correctly never
pulled into any topic's `original_chunk`); the generic grammar/vocabulary furniture (agentive-suffix
grid, વાક્યગમ્મત, વાક્ય-પુનર્લેખન, વાક્યચક, the x-mark MCQ set, the translation paragraph, the
કહેવત list) built from stock example sentences (વલ્લભભાઈ, દાદાજી/મોન્ટુ, ગીરનો પ્રવાસ) that never
occur in ક્ષિતિ's own dialogue. This is not a missed scene — the play's own 10 topics are otherwise
well covered by the રૂઢિપ્રયોગ, વાતચીત, comprehension and શબ્દજૂથ blocks (35 mapped items).

## Media

`reuse_report: {scenes: 10, reused: 0, authored: 10, rejected: []}` — matches the plan exactly: all
10 topics carry `"image"` in `available_content_types` and each has exactly one media node, on the
concept it belongs to. **Every node carries `image_url: ""` and a non-empty, self-contained
`generation_prompt`** — correct, since no Gujarati frame pool exists; a filled `image_url` here
would be fabricated. No `[reused frame: …]` stamp anywhere. Every `negative_prompt` carries
`Devanagari script labels`. `2d_tool` is `null` for the whole chapter (≤1 satisfied — this સ્વરૂપ
rarely earns one). Media titles/descriptions stage the room as a consistent single set across all
10 images, per the profile's own priors for drama.

## Publication

All 10 topics carry a non-empty `publication_text`; `concept_publication` matches the **paragraph**
content blocks by index and by count on every one of the 15 concepts (the one `list` block, in
`M1.S1.T1.C1` index 2, correctly carries no `publication_text` — the contract's node shape gives
`list` blocks none). A word-level diff confirms `publication_text` is `explanation` with only the
vocative `બાળકો, જુઓ — ` removed, on all 10 topics — no fact, gloss or reading added or dropped.

**Convention note, reported not blocking — the same reconciliation this pack has recorded before**
(`output6/ch11`, `ch13`, `output7/ch01`, `ch09`, `output6/ch10`). This agent's own spec text says
`publication_chunk` is "byte-identical to `original_chunk`". `agents/16_publication_authoring.md` —
the agent that owns the field — instead defines `publication_chunk` as the topic's whole
reader-facing block, with the verbatim `original_chunk` kept intact **inside** it, followed by
`publication_text` and a de-personalised, question-dropped version of `real_life_example`. A16
built this chapter to its own owning spec, matching the pack-wide convention exactly. The gate that
actually matters was run as **containment**, and it passes on all 10 topics: `original_chunk` occurs
as an exact, unmodified prefix of `publication_chunk` — no reflow, no re-spacing, no re-punctuation.
A vocative sweep (`બાળકો`, `જુઓ —`, `બોલો`) across every publication field returns two `બાળકો` hits,
both false positives (`નાનાં બાળકોને ભણાવવાનું` = Santosh considering teaching children, a plot fact,
not classroom address). The appended real-life passages differ from the authored
`real_life_example` only by dropping the closing question to the child and, on three topics
(`M2.S3.T6`, `M3.S5.T8`, `M3.S6.T10`), a second-person → impersonal rewording — no new fact
anywhere. Treated as **PASS**, consistent with every other chapter in this corpus that has reached
this gate; the two spec texts should be reconciled in one direction.

## E–G (reported)

- **E — સ્વાધ્યાય and risk.** See **Exercises** above. Sensitivity: all four soft `08_sensitivity.json`
  items followed (see D above); `areas[]` uses only the fixed seven labels (જાતિ-ભૂમિકા here). No
  hard sensitivity item exists in this chapter.
- **F — shape and media.** All 12 contract invariants hold (above). `chapter_id`/`plan_id` follow
  `naming_conventions.md`'s provisional form; **board/medium segments remain PROVISIONAL until
  VERIFY-1**. Media and summaries both hold (above).
- **G — the seven usual mistakes.** None present: not સાર+બોધ+પ્રશ્નોત્તર (1); no દુહા/પદ concern
  applies to drama (2–3); no poetic licence silently corrected — `બળ્યું` was render-verified and
  surfaced, not silently patched, and the printed `કડાકૂટ`/`કડાફૂટ` inconsistency stands as printed
  in each of its own locations (4); `figures_of_speech: []` throughout, nothing invented (5); every
  `real_life_example` is a std-8, Indian, single anchor (6); the સ્વાધ્યાય deliverable is complete,
  nothing cut as a teaching topic (7).

## Gaps

- **`genre` root field.** `01_meta.json` and `05_with_content.json` both write the Gujarati
  descriptive form `નાટક (એકાંકી)`, not a roster slug; `phase2_contract.md`'s own worked example
  uses a slug (`"urmikavya_geet"`). Unlike the std-6 pack (documented split, `output6/ch13` Gap 2),
  **every one of this book's 13 already-merged sibling chapters (`output8/ch01`–`ch15`) writes the
  Gujarati descriptive form**, with no `genre_slug` field anywhere in any of their `05_with_content.json`
  files either. The merge here follows that unanimous std-8 convention and carries `નાટક (એકાંકી)`
  forward unchanged, rather than deriving a slug from `active_genre_profiles[0]` as an earlier pass
  of this file briefly did. Owner **A1**, for a pack-wide decision, not a per-chapter one.
- **`publication_id` is written as `1` and is PROVISIONAL.** `upload_reference/chapter_master_map.json`
  holds `publication_id: null` for `gseb_eng_gujarati8_ch12` with an explicit `_comment` that it must
  be fetched from the education DB (**VERIFY-2**) and never invented; CBSE's `1` does not transfer.
  `1` is written here only because (a) the server rejects `null` outright and (b) it is what every
  one of this book's 13 merged sibling chapters already carries — a pack-wide placeholder, not a
  claim that `1` is this chapter's real GSEB row. Do not treat this value as verified; it blocks
  Phase-8 upload, not this run.
- **`chapter_master_id` is `null`.** Same map, same reason — required for upload, fetched from the
  education DB (VERIFY-2), never derived by arithmetic. `subject_ref_id` / `medium_id` are
  server-injected and correctly left `null`.
- **`chapter_id`/`plan_id` board and medium segments are PROVISIONAL until VERIFY-1** — a wrong
  medium uploads clean and mis-files the plan.
- **`textbook` is filled, not left `null`, unlike this book's `ch05`/`ch09` siblings.** This
  chapter's `11_pages.json` fills `textbook: "ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 8"` from
  `profiles/boards/gseb_gujarati.md`'s standard std-8 format, explicitly flagged there as
  cover-unverified (`01_meta.json.extraction_notes[0]`); `ch05`/`ch09`'s own `11_pages.json` instead
  left the field `null` for the identical unread-cover reason. Both are Agent-11 judgement calls on
  the same known gap, not a defect in either — carried here exactly as this chapter's `11_pages.json`
  states, per this agent's fail-soft instruction for pagination/edition gaps. Worth one pack-wide
  convention, not a per-chapter fix.
- **`textbook_url` is a local path** (`../Textbooks-pdf/std-8/ch-12-kshiti.pdf`) — the GSEB readers
  have no hosted URL. `textbook_pages: "94-107"` is `confidence: "medium"` (folios 94 and 107 read
  off the first/last renders, cross-checked against the manifest and the board profile's std-8 row).
- **QR badge code (page 94) was not transcribed**, per policy.
- **`05b_textbook_order.json` matches the logical traversal exactly** — per `phase2_contract.md`
  §Ordering this is raised for human confirmation at emit; `ordering` is correctly not written here
  (Agent 14/15's field).
- **Two thin, non-blocking notes carried from `04_validation.json`:** `M1.S1.T1` and `M1.S1.T2` are
  both `topic_category: "introduction"` (two consecutive introduction beats before the first
  `"core"` beat) — a thin categorisation choice, not a coverage defect. `O1`'s `objective_text` is
  the thinnest of the ten (names no individual character the way O2–O10 do) — reported, not blocking.
- **Context-routing gaps surfaced by earlier agents, passed on so the orchestrator can widen the
  bundles:** A5 was not given `profiles/genres/natak_ekanki.md` in its own read list (it proceeded
  on `no_hallucination_policy.md`/`global_content_rules.md`/`author.md`/`gujarati_verbatim.md`/
  `shabd_gloss.md` and flagged the gap rather than guessing); A12 was not given
  `teaching_block_format.md`, `alankar_chhand.md`, `shabd_gloss.md`, `bhasha_bodh.md` or
  `profiles/students/std-8.md` (it located and read all five from disk, since `profiles/students/std-8.md`
  was independently in this run's own RUN CONTEXT). This agent (A13) was given every document its own
  spec cites.

## LP2 validator

Not run — filled in Phase 8. `POST /api/lp2/learning-plans/validate` must return zero
`validation_errors`, and must not be attempted before VERIFY-1 (board/medium) and VERIFY-2
(`publication_id`, `chapter_master_id`) land, since both remain provisional above.

---

**Verdict: PASS on A–D, Contract, Exercises, Media and Publication.** No hard item blocks. Every
provisional value above (`publication_id`, `chapter_master_id`, the `chapter_id`/`plan_id` board and
medium segments) is a recorded, pack-wide placeholder awaiting VERIFY-1/VERIFY-2 — a Phase-8 upload
gate, not a defect in this plan. This chapter ships one deliverable pair (learning plan +
`10_exercise_solutions.json`), both complete.
## LP2 validator

**Status:** Empty validation_errors

**Response:**
```json
{"success":true,"action":"validated_only","plan_id":"gseb_eng_gujarati8_ch12_v1","version":null,"phase":null,"is_active":null,"is_draft":null,"counts":null,"diff":null,"publication_id":null,"publication_name":null,"validation_errors":[],"message":"Valid"}
```

## LP2 validator

**Status:** Empty validation_errors

**Response:**
```json
{"success":true,"action":"validated_only","plan_id":"gseb_eng_gujarati8_ch12_v1","version":null,"phase":null,"is_active":null,"is_draft":null,"counts":null,"diff":null,"publication_id":null,"publication_name":null,"validation_errors":[],"message":"Valid"}
```

