# Validation Report — std 8, ch 8 · જીવતી દીવાદાંડી (હરીશ નાયક)

સ્વરૂપ: સાહસકથા (ચરિત્ર-પ્રસંગ) — profile `charitra_prasang.md` (confidence: high)   explanation unit: એક જીવન-પ્રસંગ

Topics: 3   Objectives: 3   Images: 0/3   Exercises: 14/14 blocks · 63 items (39 mapped, 24 reported unmapped)

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` → `13_merged.json` (31 of the 32 root keys; `ordering` is
Agent 14/15's and was deliberately not written).

---

## A–D (blocking)   **PASS**

No blocking item failed. What was actually checked, and what the check measured:

**A — diagnosis and lens.** સ્વરૂપ સાહસકથા (ચરિત્ર-પ્રસંગ), confidence high, agreed independently by
`01_meta.json`'s four-signal `genre_signals` block and `profiles/genres/_genre_index.md`'s own Forms
table, which lists "સાહસકથા built on a real life" as a named sub-form of `charitra_prasang.md`. The
intro box's own line — `આ એક અદ્ભુત સાહસકથા છે જે ઘણી જ પ્રેરક છે` — is quoted in `genre_signals` as
evidence, never copied in as the verdict. `explanation_unit` (`એક જીવન-પ્રસંગ`) matches the roster row
for ચરિત્ર/રેખાચિત્ર/પ્રસંગકથા identically across `01_meta.json` and `05_with_content.json`. All three
`[[ઘટના: …]]` markers in `00_chapter_normalized.md` (grep-verified: lines 9, 37, 57) became exactly
three topics, one per marker, in printed order — matching `01_meta.json`'s own
`structure_inventory.ghatna: 3` and `04_validation.json`'s independent structural pass. No ટેક exists
(`tek_occurrences: 0`), so that rule does not apply; this is not a mixed chapter. Apparatus stayed out
of the topic tree: `[[પરિચય-પેટી]]` (teacher-addressed per `01_meta.json`'s own extraction note —
this chapter carries no student-facing કવિ/લેખક-પરિચય box), `[[શબ્દાર્થ]]` and `[[ચર્ચા-વિચારણા]]` feed
`key_terms`/exercises only, never a topic; the two `[[ચિત્ર: …]]` lines (14, 62) are not chapter text
and appear in no `original_chunk`. The connecting biographical material between rescue acts (family
background, the honours paragraphs, Ida's closing quoted reflection) carries no marker of its own and
is correctly folded as each topic's *second* concept rather than spun into an unmarked fourth topic —
`charitra_prasang.md`'s own "a dated facts-cluster is a legitimate topic … two concepts, never a
third" precedent, applied identically to all three topics. `guiding_question` is derived from this
chapter's own repeated how-and-why pattern across all three rescues, and the three topics'
explanations, read in order, do answer it (skill and decisiveness for "how"; duty without seeking
fame, and Ida's own words on the joy of responsibility, for "why").

**B — verbatim and structure.** All 3 `original_chunk` non-empty and Gujarati-script (U+0A80–0AFF).
Programmatic scan of every `original_chunk`: **0 Roman characters, 0 Devanagari codepoints, 0 `।`**
(U+0964). The chapter's own printed Arabic numerals (1858, 1869, 218, 37, 21, 64, 50, 69, 23, 27)
are preserved as printed in `original_chunk` — provenance, not display. Ida's own two-paragraph
quoted reflection (lines 71–73, opening `''ક્યારેક તો મોજાંની ઝાપટો…`) is transcribed character-for-
character inside `M3.S3.T3`'s chunk, including the doubled single-quote convention. The QR badge code
(`M5P7W8`) is not transcribed, per policy. Zero of the 14 inventoried સ્વાધ્યાય `verbatim_heading`s
overlap any module/segment/topic name — no સ્વાધ્યાય block became a topic. `publication_chunk` is
confirmed **byte-identical** to `original_chunk` on all 3 topics (programmatic string-equality check).

**C — the teaching block.** All 3 topics carry non-empty `explanation` **and** `real_life_example`.
Measured word counts, all inside `field_shape_rules.md`'s bands, no band widened: `explanation`
72–87 words (band 55–90), `real_life_example` 74–80 words (band 55–90), `objective_text` 18–21
words (band 12–30); no trimming was required. Glossing is inline and in Gujarati at first use
(`કાબેલિયત`, `ડગમગેલી`, `સહીસલામત`, `બેશુદ્ધ`, `નિઃસ્વાર્થ` glossed the moment they appear). Each
`real_life_example` is one concrete, Indian, std-8-reach anchor addressed in second person (ઘરનું
કામ, માછીમારનું ઘર, દાદી/બાનું રોજિંદું ધ્યાન) — the American setting (ન્યૂપોર્ટ, લાઈમ રોક, ફોર્ટ એડમ)
stays in the reading itself, never Indianised, per `charitra_prasang.md`'s one measured
foreign-setting exception; the anchor lands the *feeling* in the child's own world instead. Std-8
craft ceiling held: a programmatic scan of the whole merged plan for `અલંકાર`, `છંદ`, `સમાસ`,
`ઉપમા`, `સજીવારોપણ`, `પ્રાસ`, `રૂપક` returns **zero** hits — `figures_of_speech: []` and
`rhyme_scheme: null` on all three topics, correct-by-absence for this prose form.

**D — સ્વરૂપ essence.** All **13 `severity:"hard"` avoid-checks in `07_pitfalls.json`** (5 on
M1.S1.T1, 4 on M2.S2.T2, 4 on M3.S3.T3) were checked against the authored fields and hold:
- Cross-topic number bleed (gates 2/5, this chapter's single likeliest trip) — checked every
  authored field of all three topics against each topic's own licensed number/name set. **Zero**
  numbers crossed topic boundaries: M1 uses only 1858/16 (ન્યૂપોર્ટ, લાઈમ રોક, આઈડા લ્યૂસ), M2 only
  1869/27/218/37/21 (ફોર્ટ એડમ, રાષ્ટ્રપતિ ગ્રાન્ટ), M3 only 64/50/69/23/ત્રણ. M2's explanation carries
  exactly one calendar year (1869), satisfying the year-ceiling gate.
- Hagiography, act-first (gate 4) — M1's explanation states the rescue verbs (`ખેંચીને…પહોંચાડ્યા`)
  before the evaluative `સીધી-સાદી છોકરી હતી` line; M2's explanation builds the plank/unconscious-
  friend rescue detail before naming the honours as `આ પછી જ… બહાદુરીના કામ પછીનું ફળ` (consequence,
  not subject).
- Dramatised interiority (gate 3, M1) — the only interior state used is the licensed one
  (`ચારેયની જિંદગી બચાવવાનો આનંદ તેના મોં પર વર્તાતો હતો`), kept as an observed facial expression, not
  rewritten as an unstated thought.
- Invented dialogue (gate 1, all three) — M1 uses only the licensed `'બચાવો, બચાવો'`; M2's chunk
  carries no quotation at all and none was added; M3's every quotation-marked span
  (`'તેમ છતાં હું ખૂબ જ ખુશ રહેતી.'`, `'આ બધા લોકો સહીસલામત…મને આનંદ થતો.'`) matches Ida's own printed
  reflection character-for-character; the narrator's closing line quoted in M3's concept content is
  correctly attributed `પાઠના જ શબ્દોમાં`, never as Ida's own words.
- First-person slippage (gate 7, M3) — every `હું`/`મારા`/`મને` sits inside a quotation attributed to
  આઈડા; no field claims the writer witnessed her words directly.
- Tacked-on બોધ (gate 12, M3) — no field closes on an added `આપણે પણ… જોઈએ`-type line; the chapter's
  own closing statements are used only as its own attributed lines.
- Disability language (gate 10, M1) — no pity word (`બિચારું`/`લાચાર`/`ખોડખાંપણ`) appears anywhere,
  and every field's sentence subject stays on the family's responsibility or Ida's work, never on
  pity for the father; see the reported note below on a partial, non-blocking word-choice gap.

Both `severity:"soft"` items in `08_sensitivity.json` (જાતિ-ભૂમિકા, M2 and M3) are addressed with
the chapter's own two-part framing (`'આવા જોખમી કાર્ય માટે મહિલાની પસંદગી થતી ન હતી'`;
`'મહિલાને અધિકાર ન જ મળ્યો'…`), no added grievance or stereotype. The chapter-level સુરક્ષા guidance
(frame the rescues as Ida's trained, lifelong duty — never something for a child to attempt) is woven
into M1.S1.T1's concept content (`આવા સંજોગોમાં બાળકોનું કામ મોટેરાંને તરત બોલાવવાનું છે, જાતે પાણીમાં
ઊતરવાનું નહિ`) rather than repeated three times, a reasonable choice given all three rescues share
the same real-world danger.

**Contract — the 12 `json_contract.md` invariants, all hold** (verified programmatically against
`13_merged.json`, zero errors). `phase: 2`; `plan_id` = `chapter_id` + `_v1`; `chapter_id` =
`gseb_eng_gujarati8_ch8`. Objectives registry O1–O3 unique, every `home_topic_id` and every
`anchor[]` id resolves, `strand_to_objective_map` covers L1–L3 one-to-one with O1–O3. Inline
`learning_objectives[]` mirrors match root `objective_text` **character for character** (string-
equality check) and each carries `image_examples: []`. Concept ids run chapter-continuous
(C1,C2 | C3,C4 | C5,C6 — two concepts per topic throughout, verified against
`naming_conventions.md`'s worked example for this exact non-1:1 case). All 3 media ids match
`MEDIA_ID_RE` (concept-scoped: `M1.S1.T1.C1.IMG1`, `M2.S2.T2.C3.IMG1`, `M3.S3.T3.C5.IMG1`). Recalls
are `.RQ{n}` with `legacy_id` `.TR{n}`, sequential per topic (RQ1–RQ3 on every topic); **the string
`.SR` does not occur anywhere** in the merged plan. `publication_id` is non-null (see Gaps — a
flagged placeholder). `topic_type` is the authored enum `STORY_TELLING` throughout, which Agent
14/15 maps to the closed server enum `instructional` at emit. Summaries strictly increase in length
on all 3 topics (checked programmatically). No craft-device label anywhere below std 9. Every
`figures_of_speech` is `[]` (no device to verify verbatim — correct by absence for this prose form).

**Exercises.** `coverage_report.blocks_found` = 14 = `exercise_inventory` length; every inventory
`verbatim_heading` present in `blocks_answered`; `unanswered` is `[]`; all 63 `EX` items carry a
non-empty answer. The two un-numbered, pre-answered શબ્દસમૂહ/રૂઢિપ્રયોગ pre-blocks are answered from
the printed page's own filled-in answers, per `01_meta.json`'s extraction note, not solved fresh.
The standing `અનુવાદ` block (EX63) is answered in the medium of instruction, teacher-noted as such.

**Media.** `reuse_report` `scenes: 3` equals the 3 topics whose `available_content_types` carry
`"image"`; `authored: 3`; `reused: 0`; `rejected: []`. Every node has `image_url: ""` **and** a
non-empty, self-contained `generation_prompt` (each independently names the setting, Ida's age-
appropriate appearance, period clothing, and the specific rescue moment — no prompt refers to "the
same character as before" or the chapter by name). Every `negative_prompt` carries `Devanagari
script labels` alongside scene-specific exclusions (no life jacket/motorboat anachronism, no
halo/saintly framing, no medal-ceremony framing for M2). `2d_tool` is `null` at chapter level and on
every topic — 0 of the permitted 1.

**Publication.** `publication_text` on 3/3. `publication_chunk` is **byte-identical** to
`original_chunk` on 3/3 (programmatic check). `concept_publication` blocks match `concepts[].
content[]` by index and by count on every **paragraph**-type content item; the one **list**-type
item (`M2.S2.T2.C4`, content index 0 — the honours list) correctly carries no `publication_text`,
matching the contract's own worked example shape (only `{"type": "paragraph", ...}` items carry
`publication_text`). A scan for `બાળકો,`/`જુઓ —`/`બોલો` across every `publication_text` and
`concept_publication` block returns zero vocative-address hits (the one substring hit, `બાળકોનું
કામ` inside M1.S1.T1.C1's safety-framing sentence, is the third-person noun "the children's task",
not a vocative address, and is correctly retained — the classroom-voice opener `બાળકો, જુઓ —` that
opens every `explanation` correctly does **not** survive into any `publication_text`, holding the
teacher-voice/publication-voice split). No meaning was added in any rewrite beyond the verbatim.

---

## E–G (reported)

- **24 of 63 exercise items are reported `unmapped`, and that is the honest number.** Every reason is
  stated in `coverage_report.unmapped`: one વાતચીત general-knowledge packing question (EX8); the open
  wrapper-based પ્રવૃત્તિ (EX23); three સંયુક્તાક્ષર drill items whose target ligature does not occur in
  any topic's chunk (EX25, EX28, EX32); the ten-blank Galapagos/Darwin cloze paragraph printed inside
  block 6, which is apparatus text, not chapter narrative (EX39–48); the five-blank sea-expedition
  cloze paragraph inside block 8, same reason (EX55–59); three external-research પ્રવૃત્તિ items
  (hokayantra/submarine, Navy Day, aquarium — EX60–62); and the standing અનુવાદ block's own printed
  whale passage (EX63), which is not part of Ida's narrative. No mapping was invented to close any of
  these.
- **A partial, non-blocking word-choice gap on gate 10 (M1, disability language).** The pitfall's
  literal text asks that any authored field mentioning the father's illness use the chapter's own
  word `અપંગ`. `detailed_summary`, `concept_bullets`, and `M1.S1.T1.C2`'s concept content all do so
  correctly. `real_life_example`, `brief_summary`, `summary`, and `important_points` instead say
  `પિતા બીમાર પડતાં` / `પિતાની બીમારી` — a paraphrase drawn from the same source clause
  (`…બીમારીને કારણે અપંગ બની ગયા`), not an invented or softened synonym. In every one of these fields
  the sentence subject stays on the family's responsibility or Ida's work, never on pity for the
  father, and no banned pity word (`બિચારું`/`લાચાર`/`ખોડખાંપણ`) appears anywhere — the gate's actual
  purpose (no pathos framing) is met throughout. Reported here as a literal-wording observation, not
  escalated to a block, since the substantive check passes. If a future pass wants the exact word
  everywhere, owner is `12_runtime_authoring.md`.
- **G, the seven usual mistakes: none present.** No સાર+બોધ+પ્રશ્નોત્તર substitution (each of the
  three rescues is taught through its own act, not summarised into a moral); nothing merged that
  should stay separate and nothing split that should stay whole (three ઘટના markers, three topics,
  1:1); no ટેક issue (none exists in this prose form); no poetic licence to silently correct (the one
  genuine transcription fix, `અધા રસ્તે`→`અડધા રસ્તે` on page 65, was caught and corrected by Agent 1
  on a closer read of the same render, per its own `extraction_notes`, not a licence overwritten); no
  અલંકાર named because the field existed (`figures_of_speech` is `[]` throughout, correctly — this is
  ગદ્ય); no `real_life_example` written for an adult, set outside India, or pitched off-standard (all
  three stay concrete, Indian, std-8-reach, and correctly keep the American *setting* of the reading
  itself un-Indianised per the chapter's own measured exception); no સ્વાધ્યાય cut as a teaching topic
  (all 14 inventoried blocks stay exclusively in `10_exercise_solutions.json`).
- **Two-concept-per-topic cut on all three topics, confirmed deliberate, not padding.** Each ઘટના
  block genuinely does two separable things — the rescue act itself, then a dated facts-cluster or
  Ida's own closing reflection — matching `charitra_prasang.md`'s own "a dated facts-cluster is a
  legitimate topic … two concepts, never a third" precedent, already checked structurally by
  `04_validation.json` and re-confirmed here against the fully authored content.
- **PITFALL CORRECTIONS APPLIED, confirmed present in the authored fields, not just noted as intent.**
  M1's `પરંતુ`-contrast (boys could have helped but told no one) is its own clause in `explanation`
  and re-tested in RQ2. M2's explanation and RQ1/RQ2 keep act-before-honour order throughout. M3's
  `હંગામી`/`કામચલાઉ` double meaning is addressed directly in RQ3, exactly where `07_pitfalls.json`
  suggested.

---

## Media

`reuse_report`: **scenes 3 · authored 3 · reused 0 · rejected []** — no frame was rejected because no
Gujarati frame pool exists to draw from. One illustration per reading scene, each concept-scoped
(`M1.S1.T1.C1.IMG1`, `M2.S2.T2.C3.IMG1`, `M3.S3.T3.C5.IMG1`), all `image_url: ""` with a real,
self-contained `generation_prompt` — each independently sets the period (mid-to-late 1800s New
England), Ida's age at that point in her life (sixteen / late-twenties / sixties, each described
fresh rather than cross-referenced), and the specific rescue action. Every `negative_prompt` carries
`Devanagari script labels` alongside scene-specific exclusions (M2 additionally excludes
"medal close-up, president's visit" to keep the honours out of the illustrated moment; M3 excludes
"young girl, teenage appearance" to keep Ida's age correct at 64). `2d_tool` is `null` for the whole
chapter — 0 of the permitted 1. `Images: 0/3` is written as zero deliberately: nothing is reused,
nothing is generated yet.

---

## Gaps

- **`publication_id` is a flagged placeholder, not a verified value — it must not ship as written.**
  The Agent-13 spec requires the key non-null, so `1` is written, matching this pack's other std-8
  chapters; `phase2_contract.md` rule 1 states plainly that `1` is **CBSE's publication row and is
  not portable to GSEB**. The real GSEB publication row must be fetched from the education DB under
  **VERIFY-2** and substituted before any Phase 8 upload.
- **`chapter_master_id` is `null`.** Mandatory for upload, not discoverable from the LP2 API, fetched
  per chapter from the education DB (VERIFY-2). Never derived by arithmetic.
- **`textbook` is written as `"ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 8"`, from `11_pages.json`, even though the
  std-8 cover has still not been read in this run** (`01_meta.json`'s own extraction note flags this
  explicitly, and `profiles/boards/gseb_gujarati.md` itself carries the same "cover not confirmed"
  caveat for std 8). Unlike sibling chapters `ch04`/`ch05`, where Agent 11 left `textbook: null` for
  the identical unconfirmed-cover reason, Agent 11 here wrote the provisional profile string anyway.
  Per the merge table this agent's job is to carry Agent 11's value forward, not to second-guess it —
  written as supplied, flagged here as an inconsistency across this run's own std-8 chapters for the
  orchestrator to reconcile once a cover render exists. Owner: `01_ingestion_genre_diagnosis.md` /
  `11_page_pagination.md`.
- **`textbook_url` is a local path string** (`../Textbooks-pdf/std-8/ch-08-jivti-divadandi.pdf`). The
  GSEB readers have no hosted URL. `textbook_pages` is `64-71` at **medium** confidence — printed
  folios read off page-1 and page-8 renders, cross-checked against the manifest row (`printed_start:
  64`, 8 pages). A11 fails soft; this never blocks.
- **`chapter_id` / `plan_id` board and medium segments are UNVERIFIED (VERIFY-1).**
  `gseb_eng_gujarati8_ch8` follows `naming_conventions.md`, but a wrong medium slot **uploads clean**
  and mis-files the plan under the wrong medium column. Confirm both segments against the live
  server before the first upload.
- **`subject_ref_id` and `medium_id` are `null` by design** — server-injected, in
  `VOLATILE_TOP_LEVEL_KEYS`. No GSEB subject record is confirmed.
- **`english_plan_id` / `english_chapter_id` are `null`** — a Gujarati chapter has no English twin.
  Not a gap to be closed.
- **`ordering` is absent from the root by design** — it is Agent 14/15's to set at emit, so 31 of the
  32 contract root keys are written here. `topic_title` is set to the printed chapter name `જીવતી
  દીવાદાંડી`, mirroring `unit_title`; it is derived from `chapter_name`, not authored.
- **`05b_textbook_order.json` was not re-opened for this pass** — Agent 5's own logical cut already
  runs the three rescues in their printed, chronological order (1858 → 1869 → the final rescue at
  64), and nothing in this chapter's authored content suggests a reordering; if the two orders turn
  out identical, Agent 14/15 raises `human_confirmation_required` per `phase2_contract.md`, as this
  agent does not own that comparison.
- **Renders were not re-opened for this pass.** `00_chapter_normalized.md`, `01_meta.json`,
  `07_pitfalls.json` and `08_sensitivity.json` answered every question this validation needed —
  marker positions and counts, script purity, the exercise inventory, and every hard avoid-check.
  Agent 1's own `extraction_notes` records one genuine transcription correction on a second, closer
  read of the same page-65 render (`અધા રસ્તે` → `અડધા રસ્તે`), which is not a fresh gap to re-open
  here.

---

## LP2 validator

**Validation Status: PASS (validation_errors: [])**

Endpoint: `https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate`  
Timestamp: Phase 8  
HTTP Status: 200 OK  
Response:
```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati8_ch8_v1",
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

The learning plan passed the server's structural validation with zero errors. One value is already
known to fail if submitted for upload: the placeholder `publication_id: 1` (CBSE's row, not GSEB's
— see Gaps). The non-null `chapter_master_id` required by the upload endpoint is also still
missing. Both need VERIFY-2 to land before the first upload attempt. The twelve local contract
invariants above were verified programmatically against `13_merged.json` and hold; this is a
deployment-readiness note, not a data-integrity finding inside the chapter itself.
---

**Verdict: A–D PASS.** `13_merged.json` written (31 of 32 root keys; 37 topic keys; 3 topics, 6
concepts, 3 objectives, 3 media nodes). No item was repaired by this agent; the one lexical
observation on gate 10 (see E–G) is reported, not escalated, because the pitfall's substantive
purpose — no pity-framing, subject stays on duty — holds in every field it touches.
