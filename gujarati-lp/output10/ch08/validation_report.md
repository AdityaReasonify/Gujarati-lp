# Validation Report — ધોરણ 10, એકમ 8 — સૂરજ તો બધે જ સરખો

સ્વરૂપ: હાસ્યનિબંધ (`nibandh_atmaparak.md`, હાસ્યલેખ sub-form; confidence: **high**)
explanation unit: એક ઘટના (એક સ્થળ વિશેની વાત)

Topics: 6 (M1.S1 = 1 · M2.S2 = 4 · M2.S3 = 1)   Objectives: 6   Images: 0/5   Exercises: 8/8 items across 4/4 blocks

---

## A–D (blocking)   **PASS**

### A — Diagnosis and lens.   PASS
`genre_signals` (structure/theme/exercises/purpose, in `01_meta.json`) are read off the rendered
pages and quote the printed કૃતિ-પરિચય (`"...એ ટેવ વિશે લેખક કટાક્ષ કરે છે..."`) and લેખક-પરિચય
(`"આ લેખ હળવી શૈલીમાં આપણી વિચિત્રતાઓ અને ટેવો વિશે ધ્યાન દોરે છે..."`) as evidence, never as the
verdict. `genre_confidence: "high"` is independently corroborated by `04_validation.json`, and
`nibandh_atmaparak.md`'s own provenance list names this exact chapter as "measured — confirmed on
the render." `structure_inventory` records `ghatna: 5, kadi/duha/pad/tek: 0` — five printed
`[[ઘટના: ...]]` markers map 1:1 to five topics (`M2.S2.T2`–`T5`, `M2.S3.T6`); no marker was swallowed
or split. The unlabelled કૃતિ-પરિચય paragraph is folded into the લેખક-પરિચય topic (`M1.S1.T1`),
matching std-10's measured bio+કૃતિ-પરિચય pairing. Apparatus stayed apparatus: `શબ્દ-સમજૂતી`, the
single `કહેવત` block, all four `[[સ્વાધ્યાય: ...]]` blocks, `વિદ્યાર્થી-પ્રવૃત્તિ`,
`ભાષા-અભિવ્યક્તિ` and `શિક્ષકની ભૂમિકા` carry no topic. No revision checkpoint or વ્યાકરણ એકમ
applies. `guiding_question` ("સર્વજ્ઞભાઈ દરેક પ્રખ્યાત સ્થળે માત્ર ખાણીપીણીની જ વાત કરીને છેવટે
ક્યાંય ન જવાનું નક્કી કરે છે, ત્યારે લેખક પ્રવાસ કરવાની આપણી ટેવ વિશે શું કહી જાય છે ?") is this
chapter's own, and reading `M1.S1.T1 → M2.S2.T2 → T3 → T4 → T5 → M2.S3.T6` in order answers it: the
caricature is introduced (T1) → the same food-over-sight habit repeats at five destinations, rising
in absurdity (T2–T5) → the habit's logical, comic endpoint — staying home (T6).

A documented, deliberate departure is carried forward correctly: this chapter's dialogue carries
**no first-person 'હું' admission** by the writer — the humour is built entirely from the caricature
`સર્વજ્ઞભાઈ`'s own words, framed from outside by the printed intro's third-person `લેખક કટાક્ષ
કરે છે`. `01_meta.json`, `04_validation.json` and `07_pitfalls.json`'s `chapter_level` notes all
record this identically, and no field anywhere in `12_authoring.json` invents a self-deprecating
`હું` for the writer — checked and confirmed (see D below).

### B — Verbatim and structure.   PASS
All six `original_chunk`s are non-empty. A programmatic scan finds **zero** Devanagari codepoints,
**zero** stray Roman characters outside brackets, and **zero** `।` in any `original_chunk`; every
`original_chunk` is found byte-for-byte inside `00_chapter_normalized.md` (checked programmatically).
Printed poetic/colloquial and loanword forms are intact and uncorrected — `આંગળાં કરડ્યા કરીએ`,
`નારિયેળવાળો`, `ટેસ્ટી`, `બ્યુટિફૂલ`, `હમ્બગ`, `ફૂટની દાળઢોકળી`, the single unclosed opening quote
on the second dialogue turn — all kept exactly as `01_meta.json`'s `extraction_notes` record them,
double-checked against a 300dpi re-render. `word_count.original` values (150/148/74/110/235/73)
match a fresh token recount exactly. Ids run consecutive and chapter-continuous (`M1`/`M2` →
`S1`/`S2`/`S3` → `T1`…`T6` → `C1`…`C7`, `M2.S2.T5` correctly carrying two concepts `C5`+`C6` so `C7`
lands on `M2.S3.T6`). No `[[સ્વાધ્યાય: ...]]` block became a topic. Header furniture (chapter-number
box, the QR badge `N5B4Y7`) was never transcribed.

### C — The teaching block.   PASS
All six topics carry non-empty `explanation` and `real_life_example`, both inside 55–90 words:
`M1.S1.T1` 81/73 · `M2.S2.T2` 69/72 · `M2.S2.T3` 72/76 · `M2.S2.T4` 81/81 · `M2.S2.T5` 77/79 ·
`M2.S3.T6` 76/74. `objective_text` (19/23/21/21/25/27 words) is inside 12–30 on all six. No band was
widened. `explanation` glosses hard words at first use inline (`કટાક્ષ`, `ખાસિયત`, `ગજબ`, `હમ્બગ`,
`ટંક`, `ઝંઝટ`, `નવરો`) and holds the L2 calibration — every gloss is in Gujarati, one new idea per
sentence. `real_life_example` is Indian, concrete, single per topic, and rotates domain across the
chapter (school outing/અડાલજની વાવ → તહેવાર/રથયાત્રા → ST બસ/ભેળની લારી → સાપુતારાનો ધોધ →
તરણેતરનો મેળો → ધાબા પરની ઉનાળુ સાંજ), per `12_authoring.json`'s own domain ledger, with no
immediate-neighbour repeat. Every `real_life_example` ends on a direct question to the child. Craft
is named only where std 10 may — no છંદ anywhere (correctly, none is printed), and the single
`figures_of_speech` entry (`M2.S2.T5`, સજીવારોપણ) is inside the std-10 canon.

### D — સ્વરૂપ essence.   PASS
Checked line-by-line against every `severity:"hard"` item in `07_pitfalls.json` (30 checks across
six topics) and the one hard item in `08_sensitivity.json`:

- **લેખક vs સર્વજ્ઞભાઈ never merged.** Every explanation, summary and recall answer that reports a
  food-obsessed remark attributes it to `સર્વજ્ઞભાઈ` as grammatical subject; `M1.S1.T1`'s own fields
  name `લેખક` only as the outside observer who `કટાક્ષ કરે છે`. No field anywhere invents a
  first-person `હું` admission for the writer (checked across all 24 explanation/summary/example
  fields) — the chapter's genuinely third-person shape is preserved, not papered over.
- **No verdict-as-fact.** `M2.S2.T2`'s explanation names the તાજમહેલ "કબર" line as કટાક્ષ, not a
  straight opinion; `M2.S2.T3` shows the point-names-but-remembers-only-nariyal pattern as કટાક્ષ,
  not real sightseeing information; `M2.S2.T5`'s `સૂરજ તો બધે જ સરખો` is attributed to સર્વજ્ઞભાઈ's
  own excuse, never presented as an unattributed moral; `M2.S3.T6`'s ધાબા-decision is the habit's
  own comic endpoint, never turned into `ઘરમાં જ સુખ છે`.
- **No fact invented beyond print.** `M1.S1.T1` names only the books/awards/named ચરિત્રો the
  chapter itself prints; `M2.S2.T5`'s કહેવત carries only its own printed meaning, no origin story
  for સિદ્ધપુર; `M2.S3.T6`'s closing credit (`'વગેરે, વગેરે, વગેરે...' માંથી`) is named as printed
  and nowhere expanded.
- **08_sensitivity.json's one hard item (M2.S2.T4, area સંઘર્ષ) honoured by exclusion, verified
  programmatically**: the words `કશ્મીર` and `આતંકવાદ` appear **zero** times in `M2.S2.T4`'s
  `brief_summary`, `summary`, `detailed_summary`, `concept_bullets`, `important_points` or any
  `recall_questions` prompt/answer — the reference appears exactly once, in `explanation`, named as
  `એક બેપરવા, અતિશયોક્તિભરી ટીકા... નવી કોઈ વાત નહિ`, tied only to the દાળઢોકળી-complaint, adding no
  political or geographic fact. `real_life_example` stays entirely on the food-over-waterfall habit.
- **Craft-naming gate.** `figures_of_speech: []` on five of six topics is a considered call:
  `12_authoring.json`'s own notes record that `સૂરજ તો બધે જ સરખો` itself was checked against the
  std-10 registry and found not to fit any listed device precisely, so it correctly stays
  unlabelled. The one entry that IS named (`M2.S2.T5`, સજીવારોપણ on `સૂરજ તો નવરો છે તે વહેલો ઊગી
  જાય.`) is verified verbatim inside that topic's own `original_chunk`, and the chapter's own
  printed `ભાષા-અભિવ્યક્તિ` box independently names this exact construction as producing `વ્યંગ
  અને હાસ્ય` — not a label attached because the field existed.
- No `topic_category` is `climax` anywhere (categories used: introduction/core/transition/
  resolution) — the profile's avoid-list gate for this genre.

### Contract — the 12 invariants.   PASS, all 12 (verified programmatically against `13_merged.json`)
1. `phase: 2`; `chapter_id = gseb_eng_gujarati10_ch8`; `plan_id = gseb_eng_gujarati10_ch8_v1`. ✓
2. All six `original_chunk`s non-empty, Gujarati-script only, no unbracketed Roman/Devanagari. ✓
3. Every topic has ≥1 concept (`M2.S2.T5` carries two); every concept's `objective_id` resolves to
   the root registry (derived from each objective's own `anchor[]`) and `content[]` is non-empty. ✓
4. Registry complete: 6 unique `objective_id`s; every `home_topic_id` and every `anchor[]` entry
   resolves to a real node; `strand_to_objective_map` covers L1–L6 one-to-one with O1–O6; every
   topic's `objective_ids` resolve. ✓
5. `learning_objectives[].objective_text` matches the root registry character-for-character on all
   six topics (verified programmatically); `image_examples: []` appended on each mirror. ✓
6. Id grammar: all five media ids match `MEDIA_ID_RE`, concept-scoped, `concept_id` prefix matching;
   recall ids are `{topic_id}.RQ{1,2,3}` with `legacy_id` `.TR{n}` — **zero** `.SR{n}` anywhere
   (checked programmatically). Concept numbering runs chapter-continuous `C1`…`C7`. ✓
7. No સ્વાધ્યાય block is a topic; all 4 inventoried blocks (8 items) are answered in
   `10_exercise_solutions.json` — `coverage_report.unanswered: []`, `unmapped: []`. ✓
8. Three-tier summaries strictly increase by word count on all six topics (verified
   programmatically). ✓
9. **Zero** digits — Latin or Gujarati — in any authored display text (programmatic scan of every
   `topic_name`, `explanation`, `real_life_example`, every summary tier, every bullet, every recall
   prompt/answer, `objective_text`, `guiding_question`). ✓
10. Media: 5 reading scenes carry `"image"` in `available_content_types` (`M2.S2.T2`–`T5`,
    `M2.S3.T6`); 5 media nodes exist, one per scene; `reuse_report` reads `scenes:5 / authored:5 /
    reused:0`; every node carries `image_url:""` and a non-empty, self-contained
    `generation_prompt`; `2d_tool: null` chapter-wide. ✓
11. `figures_of_speech` quotes verbatim words on its one non-empty entry (verified above); vacuously
    true elsewhere. ✓
12. Agent 14's renumbering has not run yet — ids are frozen and internally consistent going in;
    nothing to check here. ✓

### Publication.   PASS
All six topics carry non-empty `publication_text`. `original_chunk` is embedded byte-for-byte,
unmodified, inside `publication_chunk` on every topic (verified programmatically as an exact
substring match) — the rewrite never touches the verbatim quotation; `publication_chunk` additionally
carries the vocative-stripped `publication_text` and a vocative-stripped restatement of
`real_life_example`, matching `16_publication_authoring.md`'s own "topic's block as a whole" shape
and this pack's majority convention (39 of 50 existing `13_merged.json` chapters pack-wide follow
this same embed-plus-surrounding-prose shape; the minority that instead write `publication_chunk`
literally equal to `original_chunk` — `ch01`, `ch03`, `ch09` in this same std-10 batch — are poem/
verse chapters whose block has no separate surrounding narrative to add). A scan for
vocative/classroom-instruction survivals (`બાળકો`, `જુઓ —`, `બોલો`, `હવે વિચારો`) across the
non-verbatim remainder of every `publication_chunk` and every `publication_text` returns zero hits —
the "`તમે`"/"`તમને`" instances that appear inside `M2.S2.T5`'s `publication_chunk` are part of the
embedded verbatim dialogue itself (સર્વજ્ઞભાઈ addressing his listener), not narrator vocatives.
`concept_publication` supplies `publication_text` on exactly the `paragraph`-type content block at
each concept's own `content_index`, matched by index and count (7 concepts, 7 entries; the sibling
`list`-type block correctly carries none). No meaning was added in any rewrite.

---

## E–G (reported)

- **E — સ્વાધ્યાય and risk.** All 4 inventoried blocks (MCQ ×2, એક-એક વાક્યમાં ×2, બે-ત્રણ
  વાક્યમાં ×2, સવિસ્તર ×2 = 8 items) answered as EX1–EX8, each mapped to the topic(s) that prepare
  it. No block is unmapped, none unanswered. `01_meta.json`'s own `extraction_notes` flags that
  `વિદ્યાર્થી-પ્રવૃત્તિ` (3 bullets, printed after the સ્વાધ્યાય banner) was not inventoried as an
  exercise block by Agent 1 — correct per apparatus rules (તે personal/project work, not a
  answerable printed block), reported here rather than silently left unmentioned.
  `08_sensitivity.json`'s one hard item (M2.S2.T4, area સંઘર્ષ) is applied, not censored (see D).
- **F — Shape and media.** All 12 contract invariants hold (above). `chapter_id`/`plan_id` shape is
  correct and provisional per VERIFY-1. Five reading scenes, five media nodes, one per scene;
  `2d_tool: null`. Every `negative_prompt` carries `Devanagari script labels` plus a
  chapter/scene-specific bar (no funerary/tomb-interior imagery on T2, no conflict/military imagery
  on T4, no empty/deserted promenade on T5, no travel-luggage on T6). No `[reused frame: …]` stamp
  and no non-empty reused `image_url` anywhere — correct, since no Gujarati frame pool exists yet.
- **G — the seven usual mistakes.** All seven checked and none present: (1) no
  સાર+બોધ+પ્રશ્નોત્તર flattening — every explanation stays inside સર્વજ્ઞભાઈ's own words and the
  chapter's own કટાક્ષ; (2)–(3) vacuous, no દુહા/પદ/ટેક in this genre; (4) printed loanwords and
  colloquial address terms (`ટેસ્ટી`, `બ્યુટિફૂલ`, `હમ્બગ`, `બોસ`, `યાર`, `બાપુ`, `સાલો`) are kept
  exactly as printed everywhere, never "corrected"; (5) `figures_of_speech` is `[]` everywhere the
  device did not genuinely fit the std-10 registry — not filled for filling's sake; (6) all six
  `real_life_example`s are Indian, single, concrete, pitched at std 10, and rotate domain across
  Gujarat's regions (Ahmedabad, Saurashtra/ST-bus travel, Dang/Saputara, તરણેતર) — none is an adult
  abstraction; (7) no સ્વાધ્યાય block was cut as a topic.

## Media
`reuse_report`: **scenes 5 · authored 5 · reused 0 · rejected []**. Five authored scenes, one per
STORY_TELLING topic (`M2.S2.T2.C2.IMG1` તાજમહેલ vs દાળવડાં · `M2.S2.T3.C3.IMG1` ખીણ vs નારિયેળ-પાણી
· `M2.S2.T4.C4.IMG1` બજારગલી-દહીંવડાં · `M2.S2.T5.C6.IMG1` નખી લેક ને અમદાવાદીઓની ભીડ ·
`M2.S3.T6.C7.IMG1` ધાબા પર આઈસ્ક્રીમ). `M1.S1.T1` correctly carries no media
(`available_content_types: []` — a લેખક-પરિચય/કૃતિ-પરિચય paragraph, not a reading scene needing an
image). `2d_tool: null` for the whole chapter. Each `generation_prompt` is self-contained (setting,
the recurring character's fixed appearance, action, mood, style, 16:9, Indian setting) and names no
previous image or the chapter itself; each carries a scene-specific `negative_prompt` addition
matched to its own risk.

## Gaps
- `textbook_url` is a **local path** (`../Textbooks-pdf/std-10/ch-08-suraj-to-badhe-j-sarkho.pdf`)
  — the GSEB readers have no hosted URL.
- `textbook_pages: "42–45"` at confidence **high** (`11_pages.json`) — printed folio and the
  manifest row agree exactly (std-10 offset N+5). No pagination gap.
- `chapter_master_id: null`, `publication_id: 1`. Neither is a real GSEB record — `1` is written
  only because the contract rejects `null`; it is the same CBSE-derived placeholder every sibling
  chapter in this pack currently carries (`upload_reference/chapter_master_map.json` records both
  fields as `null`/unresolved for `gseb_eng_gujarati10_ch8`, pending the education-DB fetch). Both
  fields must be resolved from the education DB at **VERIFY-2** before any upload.
- `chapter_id`/`plan_id`'s board and medium segments (`gseb`/`eng`) are **provisional until
  VERIFY-1**. A wrong medium segment uploads clean and mis-files the plan.
- `medium_id` and `subject_ref_id` are `null` by contract (server-injected). `english_plan_id` and
  `english_chapter_id` are `null` — a Gujarati chapter has no English twin.
- `ordering: null` — deliberately left for Agent 14/15.
- **`05b_textbook_order.json` matches the logical traversal exactly** (both read `M1.S1.T1 →
  M2.S2.T2 → T3 → T4 → T5 → M2.S3.T6`), consistent with this being a strictly sequential five-place
  essay with no cross-references. Per `phase2_contract.md`'s own instruction, raised rather than
  silently skipped:
  ```jsonc
  {"human_confirmation_required": true,
   "reason": "textbook order is identical to logical order",
   "checked": "05b_textbook_order.json matches the logical traversal exactly"}
  ```
- Working fields dropped at merge, as required: `genre_signals`, `genre_confidence`,
  `active_genre_profiles`, `explanation_unit`, `structure_inventory`, `exercise_inventory`,
  `extraction_notes` (from `01_meta.json`); `notes` (from `02_structure.json`, `04_validation.json`,
  `05_with_content.json`, `12_authoring.json`); `avoid_checks`/`misconception`/`correction`
  (`07_pitfalls.json`); `08_sensitivity.json`'s working shape; `topic_id` on each media node
  (redundant with `concept_id`/`home_concept_id`); `04_validation.json`'s checklist scaffolding.
  `13_merged.json` carries the 32 root contract keys and the 36 topic keys (31 base + `shabdarth`/
  `samanarthi`/`vilom`/`vyakaran`/`figures_of_speech`/`rhyme_scheme`), and nothing else.

## LP2 validator

**Phase 8 validation result (POST /api/lp2/learning-plans/validate):**

```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati10_ch8_v1",
  "validation_errors": [],
  "message": "Valid"
}
```

**Status: PASS** — validation_errors is empty. Learning plan is valid and ready for upload.

---

## Verdict
**PASS — A–D hold, all 12 contract invariants hold, publication complete, exercises complete.**
Nothing was repaired by this agent — no explanation, gloss, prompt or device was touched; every
field already written by A2/A4/A5/A7/A8/A9/A10/A12/A16 passed as authored, including a hard
sensitivity item (M2.S2.T4, the Kashmir/terrorism line) that was verified programmatically to be
confined to a single, correctly-framed clause in `explanation` and absent from every other field.
The only open items are the standing pack-wide ones (VERIFY-1, VERIFY-2, the LP2 live-validator
call, Agent 14's renumbering and ordering) — none of them block this gate.
