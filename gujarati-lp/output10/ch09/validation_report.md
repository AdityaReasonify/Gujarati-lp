# Validation Report — ધોરણ 10, એકમ 9 — હાથ મેળવીએ

સ્વરૂપ: ઊર્મિકાવ્ય (`urmikavya_geet.md`, confidence: **high**)
explanation unit: કડી-વિભાજન છપાયેલ નથી — સંબોધન/ચિત્રના વળાંક પ્રમાણે ચાર ભાગમાં જજમેન્ટ-કટ (પ્રોફાઇલ પોતે આ જ ચેપ્ટરને પોતાનું ઉદાહરણ ગણાવે છે) + એક પરિચય-ટોપિક

Topics: 5 (M1.S1 = 1 · M1.S2 = 4)   Objectives: 5   Images: 0/4   Exercises: 8/8 items across 4/4 blocks

---

## A–D (blocking)   **PASS**

### A — Diagnosis and lens.   PASS
`genre_signals` (structure/theme/exercises/purpose, in `01_meta.json`) are read off the rendered
pages; the printed કૃતિ-પરિચય line `"કવિએ આ નાનકડા ઊર્મિકાવ્યમાં ભાવસંવેદનનું મહત્ત્વ સ્થાપ્યું છે."`
is quoted **as evidence**, never as the verdict. `genre_confidence: "high"` is independently
corroborated by `04_validation.json`: `urmikavya_geet.md` names **this exact chapter** (std-10 ch 9
હાથ મેળવીએ) as its own worked precedent for "a poem printed with no કડી breaks at all… is cut on
its turns of address or image, and the cut is recorded in `extraction_notes[]` as a judgement,
never presented as printed structure." `structure_inventory` confirms `kadi:0, duha:0, pad:0,
tek_occurrences:0, lines:16` — the કડી/દુહો/પદ/ટેક marker-count sub-rules are correctly
inapplicable. The judgement-cut arithmetic (T2 lines 1–5, T3 lines 6–9, T4 lines 10–13, T5 lines
14–16 = 16, matching `structure_inventory.lines` exactly) was fixed at Agent 4 and is re-confirmed,
not re-derived. Std-10's unlabelled કવિ-પરિચય + કૃતિ-પરિચય pair is folded into one CONCEPT topic
(`M1.S1.T1`), per the std-10 apparatus exception and this pack's own ch01/ch03/ch04 precedent.
Apparatus stayed apparatus: `શબ્દ-સમજૂતી` (સમાનાર્થી/વિરુદ્ધાર્થી only — the shortest in the book,
per `extraction_notes`), all four `[[સ્વાધ્યાય: …]]` blocks, વિદ્યાર્થી-પ્રવૃત્તિ, ભાષા-અભિવ્યક્તિ and
શિક્ષકની ભૂમિકા carry no topic. No revision checkpoint or વ્યાકરણ એકમ applies. `guiding_question`
("કવિ 'ખાલી હાથ'ને પણ મૈત્રી અને હૃદયના ભાવથી ભરેલો કઈ રીતે બતાવે છે ?") is this chapter's own, and
reading `M1.S1.T1 → M1.S2.T2 → T3 → T4 → T5` in order answers it: invitation and the question of
what's in your hand (T2) → rejection and the "ખાલી છતાં કેટલું છે" turn (T3) → the reveal, ઉષ્મા
and થડકો, ભાવ ભેળવવો (T4) → the circle closing on a stranger (T5).

### B — Verbatim and structure.   PASS
All five `original_chunk`s are non-empty. A programmatic scan finds **zero** Devanagari codepoints
and **zero** `।` anywhere in any `original_chunk`; the one stray-Roman scan (`ST` — not present in
`original_chunk`, only in one `real_life_example`, see the Gaps note below) is not a verbatim
defect. Every `original_chunk` is found verbatim inside `00_chapter_normalized.md` (checked
programmatically, whitespace preserved). Poetic/colloquial forms are intact and uncorrected —
`કેટલુંયે`, `બેય`, `હાથમાંયે`, `તોયે`, `નિ:સ્વાર્થ`'s colon-style visarga — all kept exactly as
printed, per `extraction_notes`. The trailing source-line `('છંદોલય'માંથી)` sits, spacing intact,
inside `M1.S2.T5`'s `original_chunk` on the same printed line as the closing verse — correctly
identified as provenance, not a છાપ (this ઊર્મિકાવ્ય prints no છાપ; `structure_inventory.
tek_occurrences: 0` confirms no ટેક either, and the near-identical opening/closing line is
correctly named a **વર્તુળાકાર સમાપ્તિ**, never "ટેક," in every field that touches it). `word_count.
original` values (133/34/21/28/18) were spot-checked against a fresh token count and match. Ids run
consecutive and chapter-continuous (`M1` → `S1`/`S2` → `T1`…`T5` → `C1`…`C5`, `c = t` throughout —
the 1-marker-to-4-topic judgement cut on `[[કાવ્ય]]` is Agent 4-confirmed against the profile's
explicit precedent, not re-litigated here). No `[[સ્વાધ્યાય: …]]` block became a topic. Header
furniture (the QR string `S8T8A7`) was never transcribed.

### C — The teaching block.   PASS
All five topics carry non-empty `explanation` and `real_life_example`. Word counts (all inside
55–90): `M1.S1.T1` 72/75 · `M1.S2.T2` 72/78 · `M1.S2.T3` 84/77 · `M1.S2.T4` 83/86 · `M1.S2.T5`
84/82. `objective_text`: O1 23 · O2 29 · O3 27 · O4 27 · O5 29 words — all inside 12–30. No band was
widened; every value measured inside the band as written. `explanation` glosses hard words at
first use inline (`ઊર્મિકાવ્ય`, `પ્રતીક`, `હૃદયૈક્ય`, `નિ:સ્વાર્થ`, `ઉષ્મા`, `થડકો`, `બિનઆવડત`,
`પરસ્પર`, `અજાણ્યા`, `તોયે`) and holds the L2 calibration — an L2 hesitation-word like `કેટલુંયે`,
`બેય` is glossed even though it is colloquially ordinary. `real_life_example` is Indian, concrete,
single per topic, and rotates domain across the chapter (school/નવો સહાધ્યાયી → ST-bus મુસાફરી →
બીમારીમાં ખાલી હાથે આવતો મિત્ર → શાળાનું વૃક્ષારોપણ → ગામનો મેળો; ledger confirmed in `12_authoring.
json`'s own notes, no immediate-neighbour repeats). Four of five end on a direct question to the
child; `M1.S1.T1` ends on a question too. Craft is named only where std 10 may: no અલંકાર label and
no છંદ name appears anywhere (correctly — none is printed), and `rhyme_scheme.pattern` reads
`અછાંદસ` on every POEM topic, honestly noting the near-rhyme/repetition pattern rather than
asserting a metrical scheme.

### D — સ્વરૂપ essence.   PASS
Checked line-by-line against every item in `07_pitfalls.json` (all `severity:"hard"` except one
explicitly-marked `soft` on M1.S1.T1) — `08_sensitivity.json` reports `none_found: true`, so no
sensitivity item applies:

- **Slogans (profile's own hard gate).** A programmatic scan for `આપણે … જોઈએ`-shaped exhortations
  across every `explanation`/`real_life_example`/summary/bullet/recall-answer field on all five
  topics returns **zero** unlicensed hits — every occurrence of `જોઈએ` either reports the poet's
  own want (`કવિને … જોઈએ છે`) or restates the poem's own `કેળવીએ`/`મેળવીએ` in plain indicative
  prose without the word `જોઈએ`. This is the chapter-level risk `07_pitfalls.json` flags hardest
  (its own note: "ખાસ કરીને M1.S2.T3 અને M1.S2.T4માં") and it holds on both.
- **Feeling before picture.** The first sentence of every poem topic's `explanation` names a
  concrete word from that topic's own `original_chunk` — T2: `હાથ`, `ધન`, `સત્તા`, `કીર્તિ`; T3:
  `હાથ`, `ખાલી`; T4: `ઉષ્મા`, `થડકો`, `હાથ`; T5: `અજાણ્યા` — verified programmatically, never opening
  on the abstract ભાવ.
- **M1.S2.T2**'s `હશે` (સંભાવના, not a claim) is glossed explicitly, no real government/party/leader
  is named while discussing `સત્તા` (checked against `explanation`, `real_life_example` and the
  media `generation_prompt`/`negative_prompt`, which additionally bars political symbols,
  government emblems and currency branding).
- **M1.S2.T3** keeps "કેટલું છે" unanswered — no content named for the empty hands — so `M1.S2.T4`'s
  reveal (ઉષ્મા, થડકો) stays fresh, exactly as `07_pitfalls.json`'s misconception note asks.
- **M1.S2.T4**: no scientific/medical word (તાપમાન, રક્તાભિસરણ, નાડી, BPM) appears anywhere in
  `explanation`/`real_life_example`; the inverted printed syntax
  (`બિનઆવડત સારું નઠારું કેટલુંયે કામ કરતા આપણા આ હાથ કેળવીએ`) is explicitly reordered into plain
  sequence in `explanation`, and ઉષ્મા-થડકો are named as `હૃદયનું જીવંત જોડાણ`/`પ્રેમની હૂંફ` before
  any literal reading could land — the misconception (reading `બિનઆવડત`/`નઠારું` as a confession of
  fault) is headed off directly.
- **M1.S2.T5** marks `('છંદોલયમાંથી')` as a source-note in both `explanation` and `key_terms`, never
  a છાપ, and the media `teaching_notes` shows no mockery of the stranger's unfamiliar dress.
- **Craft-naming gate** (a non-empty `figures_of_speech[]` **or** an explanation sentence naming
  the topic's own પુનરાવર્તન/જોડિયા-શબ્દ/લય): T2 names `હશે`'s three-fold repetition and its લય; T3
  names `ખાલી તમારો હાથ`'s statement-to-question echo; T4 names the `સારું નઠારું` જોડિયા-શબ્દ; T5
  names the opening line's return and calls it a **વર્તુળાકાર સમાપ્તિ** (in `explanation` and, more
  explicitly, `rhyme_scheme.note`) rather than a ટેક — correctly, since the return is not
  કડી-કડીએ repeated.
- **No fact about નિરંજન ભગત beyond what M1.S1.T1's own `original_chunk` prints.** `explanation`
  names only `અમદાવાદ`, `'છંદોલય'` and `રણજિતરામ સુવર્ણચંદ્રક` — the soft check in `07_pitfalls.json`
  and the chapter-level note (the five-book, two-award roster is apparatus, not a memorisation
  list for an L2 std-10 reader) are both honoured; no unprinted biographical fact (a university
  post, a specific year) appears anywhere.
- `figures_of_speech: []` on all five topics is a considered call, not a placeholder:
  `12_authoring.json`'s own notes record that this ઊર્મિકાવ્ય is અછાંદસ and none of its repetitions
  settles into a named std-9/10 canon device — per `alankar_chhand.md`'s rule, an unsettled label
  is written `[]` and the effect is taught unlabelled instead. Vacuously true against invariant 11
  (no `lines` string to check).

### Contract — the 12 invariants.   PASS, all 12 (verified programmatically against `13_merged.json`)
1. `phase: 2`; `chapter_id = gseb_eng_gujarati10_ch9`; `plan_id = gseb_eng_gujarati10_ch9_v1`. ✓
2. All five `original_chunk`s non-empty, Gujarati-script only outside the one bracketed technical
   shape pattern (none needed here). ✓
3. Every topic has ≥1 concept; all five concepts carry a valid `objective_id` resolving to the root
   registry and non-empty `content[]` (2 blocks each). ✓
4. Registry complete: 5 unique `objective_id`s; every `home_topic_id` and `anchor[]` entry resolves;
   `strand_to_objective_map` covers L1–L5 one-to-one with O1–O5; every topic's `objective_ids`
   resolve. ✓
5. `learning_objectives[].objective_text` matches the root registry character-for-character on all
   five topics (verified programmatically); `image_examples: []` appended on each. ✓
6. Id grammar: all four media ids match `MEDIA_ID_RE`, concept-scoped, with `concept_id ==
   home_concept_id`; recall ids are `M1.S{s}.T{t}.RQ{1,2,3}` with `legacy_id` `.TR{n}` — **zero**
   `.SR{n}` anywhere (checked programmatically). ✓
7. No સ્વાધ્યાય block is a topic; all 4 inventoried blocks (8 items) are answered in
   `10_exercise_solutions.json` — `coverage_report.unanswered: []`, `unmapped: []`. ✓
8. Three-tier summaries strictly increase by word count on all five topics (e.g. `M1.S1.T1` 20 → 44
   → 104; `M1.S2.T3` 20 → 47 → 87). ✓
9. **Zero** digits — Latin or Gujarati — in any authored display text (programmatic scan of every
   `topic_name`, `explanation`, `real_life_example`, every summary tier, every bullet, every recall
   prompt/answer, `objective_text`, `guiding_question`, `teaching_lens`). The dates inside
   `M1.S1.T1.original_chunk`/`publication_chunk` (`18-05-1926`, `01-02-2018`) are provenance/printed
   text, correctly exempt. ✓
10. Media: 4 reading scenes carry `"image"` in `available_content_types` (T2–T5); 4 media nodes
    exist, one per scene; `reuse_report` reads `scenes:4 / authored:4 / reused:0`; every node
    carries `image_url:""` and a non-empty, self-contained `generation_prompt`; `2d_tool: null`
    chapter-wide. ✓
11. `figures_of_speech` is `[]` on all five topics — vacuously true; the emptiness itself is a
    reasoned call examined under D above. ✓
12. Agent 14's renumbering has not run yet — ids are frozen and internally consistent going in;
    nothing to check here. ✓

### Publication.   PASS
All five topics carry non-empty `publication_text`. `publication_chunk` is **byte-identical** to
`original_chunk` on all five topics (verified programmatically, byte-for-byte, including the
tail-spacing before `('છંદોલય'માંથી)`). `concept_publication` supplies `publication_text` on exactly
the `paragraph`-type content block at `content_index: 0` on each of the five concepts — the sibling
`list`-type block correctly carries no `publication_text`, matching `16_publication_authoring.md`'s
rule. A scan for vocative/classroom-instruction survivals (`બાળકો`, `જુઓ —`, `બોલો`) across all five
`publication_text` fields returns zero hits. No meaning was added in any rewrite — each
`publication_text` is a same-facts, vocative-stripped restatement of its `explanation`.

---

## E–G (reported)

- **E — સ્વાધ્યાય and risk.** All 4 inventoried blocks (MCQ ×2, એક-એક વાક્યમાં ×2, બે-ત્રણ વાક્યમાં
  ×2, સવિસ્તાર ×2 = 8 items) answered as EX1–EX8, each mapped to the topic(s) that prepare it (e.g.
  EX7's central-turn question maps to both `M1.S2.T3` and `M1.S2.T4`). No block is unmapped, none
  is unanswered. This chapter's શબ્દ-સમજૂતી prints only સમાનાર્થી/વિરુદ્ધાર્થી sub-blocks (the
  book's shortest — no તળપદા/રૂઢિપ્રયોગ block), correctly excluded from `exercise_inventory`
  per `01_meta.json`'s own `extraction_notes`. `08_sensitivity.json` reports `none_found: true` —
  no sensitivity item to apply.
- **F — Shape and media.** All 12 contract invariants hold (above). `chapter_id`/`plan_id` shape is
  correct and provisional per VERIFY-1. Four reading scenes, four media nodes, one per scene;
  `2d_tool: null`. `negative_prompt` carries `Devanagari script labels` (and more, including
  chapter-specific bars: no political symbols on T2, no scientific/anatomical overlay on T4, no
  mocking depiction of unfamiliar dress on T5). No `[reused frame: …]` stamp and no non-empty reused
  `image_url` anywhere — correct, since no Gujarati frame pool exists yet.
- **G — the seven usual mistakes.** All seven checked and none present: (1) no
  સાર+બોધ+પ્રશ્નોત્તર flattening — every topic's explanation stays inside the poem's own images and
  question-answer turns; (2) no દુહા merged (vacuous — `structure_inventory.duha = 0`); (3) there
  is no printed ટેક to split out, and none was invented; (4) printed colloquial forms
  (`કેટલુંયે`, `બેય`, `હાથમાંયે`, `તોયે`) are uncorrected everywhere they are quoted; (5) no અલંકાર
  named because a field existed — `[]` is a reasoned call (see D); (6) all five
  `real_life_example`s are Indian, single, concrete, pitched at std 10, and rotate domain — none is
  an adult abstraction; (7) no સ્વાધ્યાય block was cut as a topic — the exercise deliverable is
  complete.

## Media

`reuse_report`: **scenes 4 · authored 4 · reused 0 · rejected []**. Four authored scenes, one per
poem topic (`M1.S2.T2.C2.IMG1` ખાલી હાથ vs ભરેલો હાથ · `M1.S2.T3.C3.IMG1` બંને ખાલી હાથ, ઢગલો બાજુ
પર · `M1.S2.T4.C4.IMG1` હાથ મળે ને રોપો રોપાય · `M1.S2.T5.C5.IMG1` અજાણી વ્યક્તિ તરફ લંબાયેલો હાથ).
`M1.S1.T1` correctly carries no media (`available_content_types: []`, a પરિચય paragraph, not a
reading scene needing an image). `2d_tool: null` for the whole chapter. Each `generation_prompt` is
self-contained (setting, both figures' fixed appearance, action, mood, style, 16:9, Indian setting)
and names no previous image or the chapter itself; each carries a chapter-specific
`negative_prompt` addition matched to its own risk (political symbols on T2, alms-giving imagery on
T3, medical/biological overlay on T4, ethnic-mockery on T5).

## Gaps

- `textbook_url` is a **local path** (`../Textbooks-pdf/std-10/ch-09-hath-melvie.pdf`) — the GSEB
  readers have no hosted URL.
- `textbook_pages: "46–48"` at confidence **high** (`11_pages.json`) — printed folio and the
  manifest row agree (std-10 offset N+5). No pagination gap.
- `chapter_master_id: null`, `publication_id: 1`. Neither is a real GSEB record —
  `1` is written only because the contract rejects `null`; it is the same CBSE-derived placeholder
  every sibling chapter in this pack currently carries (kept for pack-wide consistency, not derived
  or invented fresh). Both fields must be resolved from the education DB at **VERIFY-2** before any
  upload.
- `chapter_id`/`plan_id`'s board and medium segments (`gseb`/`eng`) are **provisional until
  VERIFY-1**. A wrong medium segment uploads clean and mis-files the plan.
- `medium_id` and `subject_ref_id` are `null` by contract (server-injected). `english_plan_id` and
  `english_chapter_id` are `null` — a Gujarati chapter has no English twin.
- `ordering: null` — deliberately left for Agent 14/15.
- **`05b_textbook_order.json` matches the logical traversal exactly** (both read `M1.S1.T1 →
  M1.S2.T2 → T3 → T4 → T5`). Per `phase2_contract.md`'s own instruction, raised rather than
  silently skipped:
  ```jsonc
  {"human_confirmation_required": true,
   "reason": "textbook order is identical to logical order",
   "checked": "05b_textbook_order.json matches the logical traversal exactly"}
  ```
- `M1.S2.T2`'s `real_life_example` uses the unbracketed Roman abbreviation **`ST`** (`ST બસમાં લાંબી
  મુસાફરીમાં…`) — reviewed, not flagged as a script-purity defect. `ST બસ` is this pack's own
  established, unbracketed idiom for "State Transport bus," used exactly this way, un-bracketed,
  throughout the standing reference corpus itself — `teaching_voice_gu.md`'s own anchor bank
  (`ST બસનું ડેપો ને ટિકિટબારી`) and calibration example, `gujarat_cultural_anchors.md`'s ✅ example,
  and `qc_checklist.md`'s own std-8 register-table row all print it exactly this way. Flagged here
  for a human reviewer's visibility, not blocked — the `original_chunk`/`publication_chunk`
  script-purity checks (which do block) contain no such instance on any topic.
- Working fields dropped at merge, as required: `genre_signals`, `genre_confidence`,
  `active_genre_profiles`, `explanation_unit`, `structure_inventory`, `exercise_inventory`,
  `extraction_notes` (from `01_meta.json`); `notes` (from `05_with_content.json`, `02_structure.
  json`, `12_authoring.json`); `topic_id` on each media node (redundant with `concept_id`/
  `home_concept_id`); `04_validation.json`'s checklist scaffolding. `13_merged.json` carries the 32
  root contract keys, the 31 topic keys plus the poem/ભાષા-બોધ extras, and nothing else.

## LP2 validator

**Phase 8 validation: PASS**

Validation endpoint: `POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate`
HTTP Status: 200
Response:
```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati10_ch9_v1",
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

**Verdict:** ✓ No validation errors. Learning plan is valid for LP2 schema.

---

## Verdict

**PASS — A–D hold, all 12 contract invariants hold, publication complete, exercises complete.**
Nothing was repaired by this agent — no explanation, gloss, prompt or device was touched; every
field already written by A2/A4/A5/A7/A8/A9/A10/A12/A16 passed as authored. The only open items are
the standing pack-wide ones (VERIFY-1, VERIFY-2, the LP2 live-validator call) and the one reviewed,
non-blocking editorial note above (the `ST` abbreviation, which matches this pack's own established
usage) — none of them block this gate.
