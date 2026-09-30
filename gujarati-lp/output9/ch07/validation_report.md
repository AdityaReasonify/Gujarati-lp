# Validation Report — std 9, ch 07 નવસર્જનની વાટે

સ્વરૂપ: ઊર્મિકાવ્ય-ગીત (confidence: high)   explanation unit: એક કડી
Topics: 5   Objectives: 4   Images: 0/3   Exercises: 6/8 (3/3 inventoried blocks; **2 printed
વિદ્યાર્થી-પ્રવૃત્તિ bullets are outside the inventory and unanswered**)

Deliverables: two — the plan (`13_merged.json`) and the exercise pack
(`10_exercise_solutions.json`). This chapter has reading text throughout (no સ્વાધ્યાય-only unit),
so both deliverables are expected in full; the second one currently ships short by one block.

## A–D (blocking)   **FAIL — exercise coverage** (see detail below; all other A–D items pass clean)

Every item below was checked mechanically against the merged plan (`13_merged.json`) and, for the
one failing item, against `00_chapter_normalized.md` and `reference/exercise_alignment.md`, not
asserted from the intermediate files alone.

**A — diagnosis and lens.** સ્વરૂપ ઊર્મિકાવ્ય-ગીત, `genre_confidence: high`, all four
`genre_signals` (structure, theme, exercises, purpose) recorded off the rendered page by A1, and
the કૃતિ-પરિચય's own framing ("આ પૃથ્વી ઉપર કશુંક નવું, ચિરસ્થાયી રચી જવાનો ઉત્સાહ") is quoted as
evidence, never as the verdict. Explanation unit `એક કડી` matches the ઊર્મિકાવ્ય-ગીત roster row —
three printed કડી map to three POEM topics, none split, none merged. The identical ટેક
'અમે નૂતન યુગના પ્રવાસી.' (3 occurrences, no wording change) is taught in full once, at its first
occurrence (`M2.S2.T3`), and only referenced via `depends_on` at `M2.S2.T4`/`M2.S3.T5` — the
correct handling for an unchanged refrain, and the chapter's own note that no separate `[[ટેક]]`
marker exists on this page (the refrain is printed as each કડી's own closing line) was confirmed
against `00_chapter_normalized.md` and does not read as a swallowed marker. Not a mixed chapter —
single genre throughout (`active_genre_profiles: ["urmikavya_geet.md"]`). Apparatus stayed
apparatus: શબ્દ-સમજૂતી, ભાષા-અભિવ્યક્તિ and શિક્ષકની ભૂમિકા never became a topic; કવિ-પરિચય and
કૃતિ-પરિચય, printed as two separate std-9 markers, are the two CONCEPT topics per the roster's
allowance. `guiding_question` ("'નૂતન યુગના પ્રવાસી' બનવા માટે કવિ કઈ કઈ વસ્તુઓ છોડી દેવાનું અને
શું નવું સર્જવાનું કહે છે ?") is chapter-specific, not copied from the profile, and reading
`M2.S2.T3` → `M2.S2.T4` → `M2.S3.T5` in order does answer it (identity → what is shed → what is
built).

**B — verbatim and structure.** All five `original_chunk` fields non-empty, Gujarati script only —
a codepoint scan found zero Latin characters, zero Devanagari characters and zero `।` in any
`original_chunk`. `word_count.original` recomputed independently by whitespace count and matches
the declared value on all five (39, 58, 16, 16, 29). Marker accounting: `00_chapter_normalized.md`
carries five reading-scene markers (`[[કવિ-પરિચય]]`, `[[કૃતિ-પરિચય]]`, `[[કડી 1]]`, `[[કડી 2]]`,
`[[કડી 3]]`) and all five are carried by exactly one topic each, in order; no `[[સ્વાધ્યાય: …]]`
block became a topic — checked against all five `topic_name` values, zero overlap. તળપદો and
period-modern forms are intact and uncorrected: `વાટ` (the chapter's one printed તળપદો શબ્દ) is
glossed at point of use as `રસ્તો`, never silently replaced. No attribution line follows `કડી 3`
(the page prints none — correctly nothing was appended). Indentation of the alternating printed
lines is preserved inside every કડી's `original_chunk`. No header furniture entered any chunk. Ids
are consecutive and chapter-continuous: `M1`,`M2` / `M1.S1`,`M2.S2`,`M2.S3` / `T1`–`T5` /
`C1`–`C5` (`c` equal to `t` throughout), verified against the traversal order.

**C — the teaching block.** Every topic has non-empty `explanation` and `real_life_example`, both
inside the 55–90 word band with no trimming required:

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 71 | 78 |
| M1.S1.T2 | 82 | 76 |
| M2.S2.T3 | 79 | 62 |
| M2.S2.T4 | 73 | 67 |
| M2.S3.T5 | 83 | 74 |

`objective_text` O1–O4: 21, 21, 25, 29 words — all inside 12–30. Glossing sits at the point of
first use throughout (`પ્રૂફરીડર`, `આખ્યાન`, `મોહમાયા`, `ચિરસ્થાયી`, `નેમ`, `વાટ`, `પંથ`, `વગડો`,
`મિથ્યા`, `ફંદ`, `ભૂત`, `ઉદાસી`, `ધરા` all opened where they first appear); the L2 bar is held low
for this ગીતની તત્સમ-ભારે diction, not only the printed શબ્દાર્થ box's own five entries. Craft is
named only at the std-9 ceiling and only where the chapter's own printed ભાષા-અભિવ્યક્તિ block
names it: `વર્ણાનુપ્રાસ` on `M2.S2.T3` (two entries: `વ`-sound in 'નવસર્જનની વાટે વિહરતા', `પ`-sound
in 'અમે પ્રગતિના પંથના પ્રવાસી,'), continuing on `M2.S2.T4` ('અમે વિચરતા વગડાના વાસી,') and
`M2.S3.T5` ('અજબ આશાનાં સ્વપ્ન સજાવશું,'). The single adjective `રંગીન` (M2.S3.T5) — which the
page's own apparatus glosses as "અલ્પમાં અધિકનું સૂચન" — was correctly left unlabelled rather than
forced into one of the seven std-9 canon devices; `explanation` and `RQ3` name the effect in
prose instead, which `07_pitfalls.json`'s own avoid-check for this topic explicitly accepts as an
alternative to a `figures_of_speech` entry. No દંડ, no Devanagari, no Roman character outside a
bracketed technical term anywhere (none of this chapter's authored craft terms even needed one —
all are named in Gujarati script, per std-9's own canon).

**D — સ્વરૂપ essence.** All hard `avoid_checks` in `07_pitfalls.json` (four per topic, one topic
carries four) were verified in the field each names, not assumed from A7's own claim:

- **No `આપણે … જોઈએ` exhortation anywhere.** A programmatic sweep for `જોઈએ` across every
  `explanation`, `real_life_example`, `brief_summary`, `summary`, `detailed_summary`,
  `concept_bullets`, `important_points` and `recall_questions[].{prompt,answer}` on all five
  topics returns **zero** hits. The poet's biography (`M1.S1.T1`), the ગીતનો ભાવ (`M1.S1.T2`) and
  every પ્રવાસી first-person વચન (`હટાવશું`, `મિટાવશું`, `ફગાવશું`, `ભગાડશું`, `ઉતારશું`) stay
  first-person self-description, never recast as advice to the child.
- **No political/campaign framing on `નવસર્જન`/`નૂતન યુગ`/`પ્રગતિ`.** No explanation, example or
  recall answer on any of the five topics names a government, party, scheme, campaign, army or
  border; every anchor stays personal or familial.
- **`વાટ` never treated as an error.** Glossed in `M2.S2.T3.explanation` explicitly as "તળપદો
  શબ્દ, રસ્તો", matching the chapter's own શબ્દ-સમજૂતી entry.
- **`ભૂત` and `સ્વર્ગ` never read literally.** `M2.S3.T5.explanation`, `summary` and `RQ2` all
  gloss `ભૂત` as "ખોટી કીર્તિની ઘેલછા" (not a literal ghost) and `સ્વર્ગ` as this-worldly, રંગીન
  ધરતી (not an afterlife) — checked against the topic's own `key_terms`, which carry the same
  gloss.
- **No invented કવિ-fact.** `M1.S1.T1`/`M1.S1.T2` state only the facts printed in their own
  `original_chunk` (વડોદરા જિલ્લાનું મસ્તુપુરા, 'નવજીવન'માં પ્રૂફરીડર, the seven named કૃતિઓ). The
  poet's birth/death dates (7-3-1916 / 28-2-1993), printed only in `01_meta.json`'s
  `genre_signals` and never inside either topic's own `original_chunk`, do **not** appear
  anywhere in the merged plan (a full-text search of `13_merged.json` for `1916`, `1993`, `7-3`,
  `28-2` returns zero hits).
- **`figures_of_speech` entries quote words that actually appear** in their own topic's
  `original_chunk` — all four entries (`M2.S2.T3` ×2, `M2.S2.T4` ×1, `M2.S3.T5` ×1) verified as
  exact substrings, re-checked independently on the merged file, not only trusted from A12's own
  claim.

`08_sensitivity.json` returned `none_found` for this chapter — correctly: the ગીત stays with
મોહમાયા/આળસ/નિરાશા/વેરઝેર/જૂઠી કીર્તિ as universal traits and uses "સ્વર્ગ" as a this-worldly
metaphor, never a theological claim, so no ધર્મ/સમુદાય/ક્ષેત્ર/વિકલાંગતા/સંઘર્ષ/જાતિ-ભૂમિકા/સુરક્ષા
flag applies.

### The one failing item — exercise coverage

`00_chapter_normalized.md` (lines 63–65) prints a `[[વિદ્યાર્થી-પ્રવૃત્તિ]]` block with 2
child-addressed bullets ("તમારી શાળામાં શું શું નવું કરી શકો તેનાં સૂચનોની યાદી તૈયાર કરો…",
"તમારા ગામ/શહેરમાં શાનું નવસર્જન કરવા જેવું છે તેની યાદી તૈયાર કરી…") on printed page 31,
immediately after the three-tier ladder and before ભાષા-અભિવ્યક્તિ. `reference/exercise_alignment.md`'s
own measured std-9 corpus table records વિદ્યાર્થી-પ્રવૃત્તિ as a real, inventoried સ્વાધ્યાય block
in 22/23 std-9 literature chapters, explicitly distinct from the apparatus items (ભાષા-અભિવ્યક્તિ,
શિક્ષકની ભૂમિકા) that are **not** exercise blocks, and states plainly: "Agent 13 checks none went
unanswered (a skipped block is a hard fail)." `global_content_rules.md` rule 7 names `પ્રવૃત્તિ`
among the સ્વાધ્યાય sub-blocks belonging to `exercise_solutions.json` alone. Three sibling
chapters in this same run (`output9/ch01`, `ch04`, `ch05`) all inventory and answer their own
વિદ્યાર્થી-પ્રવૃત્તિ block as `is_model_answer: true` items.

`01_meta.json`'s `exercise_inventory` for this chapter records only 3 blocks (MCQ,
બે-ત્રણ વાક્યોમાં ઉત્તર, છ-સાત વાક્યોમાં ઉત્તર) — the વિદ્યાર્થી-પ્રવૃત્તિ block is missing from it.
`10_exercise_solutions.json`'s own `coverage_report._note` already caught and flagged this exact
gap ("This looks like an inventory omission in THIS chapter's 01_meta.json, not a genuine
absence"), and correctly did not invent an answer for a block its own inventory did not record.
Measured against `01_meta.json`'s inventory as written, `blocks_found` (3) equals the inventory
length and `unanswered`/`unmapped` are both empty — but measured against the rendered page (which
this agent's own inputs include `00_chapter_normalized.md` for exactly this purpose), one printed,
student-facing exercise block ships with **zero** answered items. This is the single hard gate
this run fails.

**Owner:** `agents/01_ingestion_genre_diagnosis.md` — add a `વિદ્યાર્થી-પ્રવૃત્તિ` entry
(2 items, `verbatim_heading` transcribed from the render) to `01_meta.json`'s
`exercise_inventory`. Then `agents/10_exercise_solutions.md` — re-run to answer the 2 bullets as
`is_model_answer: true` items (open, student-directed tasks; no single correct answer), mapped to
no reading topic (`covered_by_topics: []`, matching the sibling chapters' treatment of their own
open-ended વિદ્યાર્થી-પ્રવૃત્તિ items). No other agent's output is implicated — the poem plan
itself, the media, and the publication rewrite are unaffected by this gap and are not blocked.

## E–G (reported)

**E — સ્વાધ્યાય and risk (beyond the one failing item above).** The three inventoried blocks that
were answered are answered well: all 4 MCQ items give a distractor-by-distractor rationale
(including the negative-stem item, `EX4`, correctly flagged by A1 as a trap format and handled
with the "નથી" emphasis called out in `teacher_note`); the બે-ત્રણ-વાક્ય and છ-સાત-વાક્ય items stay
inside their own length tier and are built entirely from the poem's own first-person વચનો, never
padded with outside content. No personal-opinion/model-answer item needed flagging among the 3
answered blocks (the gap is the unanswered 4th block, above). `values_filled_for_teaching` is
correctly `null` throughout — this chapter prints no empty table or grid.

**F — shape and media.** All 12 `json_contract.md` invariants verified against the merged plan
programmatically: `phase: 2`; `chapter_id` = `gseb_eng_gujarati9_ch7`; `plan_id` =
`gseb_eng_gujarati9_ch7_v1`; every topic has exactly one concept with a resolving `objective_id`
and non-empty `content[]`; the objectives registry is complete and consistent (4 unique ids, every
`home_topic_id` and every `anchor[]` entry resolves — including `O1` anchoring both `C1` and `C2`
for the paired pre-reading topics — `strand_to_objective_map` covers L1–L4 exactly, single strand
`L`); every inline `learning_objectives[]` mirror matches its root `objective_text` character for
character and carries `image_examples: []`; concept ids are chapter-continuous (`M1.S1.T1.C1` …
`M2.S3.T5.C5`, `c` equal to `t`, no restart across the M1→M2 module boundary) verified against the
traversal, not just against each other; recall ids are `{topic}.RQ{n}` with `legacy_id`
`{topic}.TR{n}` and **no `.SR{n}` anywhere**; media ids match `MEDIA_ID_RE`, concept-scoped
(`M2.S2.T3.C3.IMG1`, `M2.S2.T4.C4.IMG1`, `M2.S3.T5.C5.IMG1`); `publication_chunk` verified
byte-identical-as-a-prefix to `original_chunk` on all five topics; `concept_publication` blocks
match `concepts[].content[]` by index for the two paragraph-type items on every topic (the
established, already-accepted convention in this run — see `output9/ch01`'s own passed report —
that `publication_text` is authored for paragraph content only, not for list-type bullets); no
digit — Roman or Gujarati — occurs in any `topic_name`, `explanation`, `real_life_example`,
summary, bullet, recall prompt/answer, `objective_text`, `publication_text` or `publication_chunk`
(a full codepoint sweep returned zero digit characters); summaries strictly increase at every
topic by word count (17<32<46, 16<33<66, 14<28<60, 17<27<62, 21<35<91); `figures_of_speech`
entries quote words verified present in their own topic's `original_chunk`.

`topic_type` is `CONCEPT` (`M1.S1.T1`, `M1.S1.T2`) and `POEM` (`M2.S2.T3`, `M2.S2.T4`,
`M2.S3.T5`) throughout — the correct authored enum for an Agent-13 intermediate file; the closed
server enum (`instructional`/`summary`/`assessment`) is Agent 14/15's mapping at emit.

Bands from `field_shape_rules.md`, all held: `key_terms` 5–6 per topic (band 3–6);
`concept_bullets` and `important_points` 4 each (band 3–4); `recall_questions` 3 per topic
(band 2–3), Bloom-laddered remember→understand→analyze/evaluate, every "analyze"/"evaluate" item
citing a quoted line or naming a specific device; `difficult_words` 7 (M1) / 8 (M2), both inside
5–10; `estimated_exchanges` small integer strings ("3","4","4","4","5"); `bloom_level` lowercase
in recalls and Capitalised in `objectives[]`, the required asymmetry held; `shabdarth` 5–6,
`samanarthi` 2, `vilom` 0–1, `vyakaran` 2–3 per topic, all inside `bhasha_bodh.md`'s std-9 caps.

**Minor, non-blocking note on `vyakaran.udaharan`.** `12_authoring.json`'s own notes claim every
`vyakaran`/`figures_of_speech` quotation was checked as an exact substring of its own topic's
`original_chunk`. Two `vyakaran.udaharan` strings on `M1.S1.T1` and `M1.S1.T2` are trimmed
paraphrases of their source sentence (drop the leading `તેમણે` / restate a clause) rather than
exact substrings — a minor inconsistency with that claim and with this run's own precedent
(`output9/ch01`, `ch03`, `ch04` all use byte-exact `udaharan` quotations throughout). Neither
`json_contract.md`'s 12 invariants nor `qc_checklist.md` Section D require `vyakaran.udaharan` to
be byte-exact (only `figures_of_speech.lines` carries that explicit hard requirement, and all four
of this chapter's entries pass it) — so this is reported, not blocked. Owner if corrected:
`agents/12_runtime_authoring.md`.

**G — the seven usual mistakes.** None of the six that apply to a poem chapter are present: the
plan teaches the સ્વરૂપ (ઉત્સાહ-ગીત) rather than સાર+બોધ+પ્રશ્નોત્તર; the three કડી are not fused
into one topic, and none is split; the ટેક is taught once and referenced, never re-taught or
lifted out as its own topic; no તળપદો form was silently corrected (`વાટ` stays `વાટ`); no
અલંકાર was named because the field existed (`M1.S1.T1`/`M1.S1.T2` correctly carry `[]`, being
ગદ્ય); every `real_life_example` is single, Indian, and inside std-9 reach (a neighbourhood
કાકા's varied talents, a family tree-planting, a first day of school, a maldhari family's dawn
departure, a Diwali rangoli — no domain repeats between adjacent topics). The seventh mistake —
"સ્વાધ્યાય cut as teaching topics, leaving the exercise deliverable half-empty" — is present in a
different shape than the classic form: no exercise was cut into a topic, but the exercise
deliverable does ship half-empty for one block, per the failing item above.

## Media

`reuse_report`: scenes 3, authored 3, **reused 0**, rejected none — matching the three POEM topics
(`M2.S2.T3`, `M2.S2.T4`, `M2.S3.T5`) whose `available_content_types` carry `"image"`. Every media
node carries `image_url: ""` **and** a real, self-contained `generation_prompt`, as required while
no Gujarati frame pool exists. No `[reused frame: …]` stamp and no fabricated URL anywhere in the
pack. Every `negative_prompt` carries `Devanagari script labels`. `2d_tool` is `null` chapter-wide
(≤1 satisfied trivially). All three `generation_prompt`s name a concrete scene from their own
topic's `original_chunk` (a road at dawn for `M2.S2.T3`; open scrubland at first light for
`M2.S2.T4`; a colourful hillside with a discarded net for `M2.S3.T5`) and each carries a narrator
bar naming the exact Gujarati line to render. `M1.S1.T1`/`M1.S1.T2` correctly carry no media
(CONCEPT topics, `available_content_types: []`).

## Gaps

1. **The exercise coverage gap above is the run's one hard blocker.** Not a pagination or
   extraction gap — an inventory omission. Recorded here again for visibility: `01_meta.json`
   needs a `વિદ્યાર્થી-પ્રવૃત્તિ` `exercise_inventory` entry, then `10_exercise_solutions.json`
   needs re-running to answer its 2 bullets.
2. **`publication_id` is provisional and must not ship as written.** Written here as `1`, the
   placeholder this pack's own convention uses on every prior chapter checked (`output9/ch01`
   through `ch06`), pending **VERIFY-2**'s real GSEB publication row. Not an A–D failure of this
   run; a hard precondition of upload.
3. **`chapter_master_id` is `null`.** Mandatory for upload, not discoverable from the LP2 API,
   fetched per chapter from the education DB (VERIFY-2); never derived by arithmetic.
4. **`textbook` title is not confirmed off a rendered cover.** `11_pages.json` records this
   explicitly (confidence `medium`) — the value (`ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 9`) is read from
   this chapter's own page-footer, not the std-9 front-cover spread, which this unit's render does
   not include. Owner `agents/01_ingestion_genre_diagnosis.md` if a cover render becomes
   available.
5. **`textbook_url` is a local path string** (`../Textbooks-pdf/std-9/ch-07-navsarjanni-vate.pdf`)
   — the GSEB readers have no hosted URL. `textbook_pages` `30-31`, confidence `medium` per
   `11_pages.json`, cross-checked against the std-9 manifest row and agreeing.
6. **`topic_title`/`topic_number` are derived, not authored.** No agent supplies `topic_title`
   directly; it is set to the printed chapter title `નવસર્જનની વાટે`, matching this pack's
   established convention (`topic_title = chapter_name`). `topic_number` is carried through as
   `null` from `01_meta.json`, matching the `output9/ch06` precedent for the same field.
7. **`ordering` is deliberately absent** from `13_merged.json` — it is Agent 14/15's to set
   (`logical` / `textbook`), per this spec's own instruction. 31 of the contract's 32 root keys
   are written; `ordering` is the one withheld.
8. **Board and medium segments are PROVISIONAL until VERIFY-1.** `gseb_eng_gujarati9_ch7` uploads
   **clean** under a wrong medium and mis-files the plan silently. Confirm before the first
   upload.
9. **`publication_chunk`** — the same documented, already-resolved tension noted on every prior
   chapter in this run: this gate's own text calls for byte-identical `original_chunk`, while
   `agents/16_publication_authoring.md` treats `publication_chunk` as the topic's whole
   publication-facing block with the verbatim kept intact as a prefix. Followed the producing
   agent's own spec, as this run's precedent does: verified `original_chunk` sits
   byte-identical as a **prefix** of `publication_chunk` on all five topics, with no vocative or
   second-person classroom question surviving in the appended prose. Not blocked, for the same
   reason it was not blocked on prior chapters.
10. **No page render was re-opened by this agent.** `05_with_content.json`'s `original_chunk` for
    all five topics carries Agent 5's own render-verified provenance (cross-checked at 150/250/400
    dpi, including the measured 4/4/7 line-count correction against a prior inventory's 4/4/8);
    this agent authors and merges on top of that frozen verbatim. `00_chapter_normalized.md` was
    read directly (not re-rendered) to confirm the `[[વિદ્યાર્થી-પ્રવૃત્તિ]]` marker for the one
    failing item above.

## LP2 validator

Validation endpoint: POST to https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate

Response (HTTP 200):
- success: false
- action: validated_only
- plan_id: gseb_eng_gujarati9_ch7_v1

Validation errors (5):
- modules[0].segments[0].topics[0]: invalid topic_type 'CONCEPT'
- modules[0].segments[0].topics[1]: invalid topic_type 'CONCEPT'
- modules[1].segments[0].topics[0]: invalid topic_type 'POEM'
- modules[1].segments[0].topics[1]: invalid topic_type 'POEM'
- modules[1].segments[1].topics[0]: invalid topic_type 'POEM'

Message: 5 validation error(s)

**Analysis:** The validation errors indicate that topic_type values use the authored enum (CONCEPT/POEM) rather than the server enum (instructional/summary/assessment). This is expected because the `learning_plan_logical.json` submitted is the raw authored version (Agent-13 output). The mapping to the closed server enum happens at Agent 14/15 emit time. These errors do not represent a failure of the chapter itself, but rather reflect the staged transformation from authored form to server-compatible form.

**Status:** Validation indicates the need for Agent 14/15 transformation before upload.
