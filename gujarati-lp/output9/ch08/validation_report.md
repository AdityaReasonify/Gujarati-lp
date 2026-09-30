# Validation Report — std 9, ch 08 આભાર

સ્વરૂપ: સૉનેટ (confidence: high)   explanation unit: એક ભાવ-ખંડ
Topics: 5   Objectives: 5   Images: 0/4   Exercises: 11/11 (4/4 blocks)

Deliverables: two — the plan (`13_merged.json`) and the exercise pack
(`10_exercise_solutions.json`). This is a standard numbered teaching chapter (no સ્વાધ્યાય-only
unit, no revision checkpoint, no વ્યાકરણ એકમ), so both ship in full.

## A–D (blocking)   **PASS**

Every hard item below was checked mechanically against the merged plan (`13_merged.json`), not
asserted from the intermediate files alone — a Python pass walked the full JSON tree for each
check rather than eyeballing samples.

**A — diagnosis and lens.** સ્વરૂપ સૉનેટ, `genre_confidence: high`, four `genre_signals`
(structure, theme, exercises, purpose) recorded off the rendered page by A1, quoting the
book's own કૃતિ-પરિચય definition of સોનેટ as evidence, never as the verdict — corroborated
independently by the chapter's own MCQ (4), which tests સાહિત્યપ્રકાર against ગઝલ/ઊર્મિકાવ્ય/પદ
as distractors. Explanation unit `એક ભાવ-ખંડ` matches the સૉનેટ roster row ("one ભાવ-ખંડ, the ચોટ
never split, never cut couplet-wise"): four ભાવ-ખંડ topics cut at the poem's own three-times-
repeated "હજી/હજુ…સારું છે" clause plus the turn to "ભલું કે" — sits at the profile's stated
ceiling of four, not over it, and `04_validation.json`'s own line-by-line reconstruction (verified
independently here) confirms the four spans concatenate to all fourteen printed lines with no gap,
no overlap, and no cut mid-sentence. The ચોટ (last two printed lines) is kept whole inside the
last verse topic (`M2.S2.T5`), never split. No ટેક, છાપ or રદીફ-કાફિયા exists in this chapter
(`structure_inventory` confirms), so those sub-checks are correctly inapplicable; not a mixed
chapter. Apparatus did not become a reading scene: શબ્દ-સમજૂતી, ભાષા-અભિવ્યક્તિ, શિક્ષકની ભૂમિકા
and the three સ્વાધ્યાય blocks plus વિદ્યાર્થી-પ્રવૃત્તિ all stayed out of the topic tree; the
poet-bio + કૃતિ-પરિચય, printed under one marker, is the one CONCEPT topic the std-9 roster allows
for student-facing પરિચય prose. No revision-checkpoint/વ્યાકરણ-એકમ carve-out applies — this unit
prints reading text throughout. `guiding_question` ("કવિ 'હજી સારું છે' કહી કહીને પ્રકૃતિનું કયું
ઋણ ગણાવે છે…") is chapter-specific, not copied from the profile, and reading `M2.S2.T2` →
`M2.S2.T5` in order answers it precisely — the poem's premise, its three "સારું છે" answers, and
the ચોટ.

**B — verbatim and structure.** All five `original_chunk` fields non-empty; a full codepoint sweep
of the merged plan found zero Devanagari characters and zero Roman characters outside bracketed
technical terms, and zero `।` anywhere. `word_count.original` recomputed independently by
whitespace count from each `original_chunk` and matches the declared value on all five (256, 46,
29, 18, 15). `00_chapter_normalized.md` prints zero `[[ભાવ-ખંડ]]`/`[[કડી]]`/`[[દુહો]]`/`[[પદ]]`
markers for the fourteen-line verse (`structure_inventory.stanza_breaks: 0`) — consistent with a
સૉનેટ printed as one unbroken block, not a defect; the four verse-topic boundaries are Agent 2's
own syntactic cut, sanctioned by the profile for exactly this case, and no `[[સ્વાધ્યાય: …]]`
block became a topic (checked against all five `topic_name` values — zero overlap). Archaic/
તળપદું/ઘડેલા forms stand exactly as printed and uncorrected throughout: `કરી'તી`, `ટ્હૌકા` (kept
distinct from the કૃતિ-પરિચય paraphrase's plainer `ટહુકા`), `પરણ`, `ગાછ્યા`, `ફુક્ક`, `મિટ્ટી`,
`તણાં`, `ભણી`, and `મૂળો` with ળ (independently cross-checked by A1 against MCQ item 3's own
printed spelling — the rendered page's spelling stands over `profiles/genres/sonnet.md`'s own
illustrative quote, which the pack has already flagged as a likely transcription slip in the
reference file, per `reference/gujarati_verbatim.md`'s rendered-page authority). The printed
attribution `('અશ્વત્થ'માંથી)` sits inside `M2.S2.T5`'s `original_chunk`, the **last** topic. No
header furniture (chapter-number box, QR badge, running footer) entered any chunk. Ids are
consecutive and chapter-continuous: `M1`→`M2` / `M1.S1`,`M2.S2` / `T1`–`T5` / `C1`–`C5`, and the
concept-number-equals-topic-number rule holds on all five.

**C — the teaching block.** Every topic has non-empty `explanation` and `real_life_example`, both
inside the 55–90 word band (recomputed independently, no trimming required):

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 82 | 71 |
| M2.S2.T2 | 85 | 79 |
| M2.S2.T3 | 81 | 76 |
| M2.S2.T4 | 77 | 75 |
| M2.S2.T5 | 85 | 77 |

`objective_text` O1–O5: 21, 29, 24, 22, 29 words — all inside 12–30. L2 glossing sits at the point
of first use throughout and the bar is held low for this chapter's dense verse (`ભણી`, `ટ્હૌકા`,
`પરીકથા`, `પરણ`, `ગાછ્યા`, `ફુક્ક`, `તરડ`, `મિષ`, `ઋણી`, `આદિમ` are all opened in simple Gujarati
where they first appear, in `શબ્દ — અર્થ` shape, never a Hindi stand-in). `real_life_example` is
single, Indian, and inside std-9's reach on every topic — five different concrete domains (a
school word-limit essay, a stray kitten on the ઓટલો, a distant bird-call recalling a
grandparent's village, ants finding a way into a sealed tin, an old neighbourhood tree still
standing) so no anchor repeats the poem's own literal image as its noun, and none needs its own
extra gloss. Craft is named only where std-9's ceiling and this chapter's own printed apparatus
allow: `figures_of_speech: []` on all five topics is the honest answer — the ભાષા-અભિવ્યક્તિ box
names only the "હજી" repetition-pattern and the "ફુક્ક" sound-word (both handled as `vyakaran`
દ્વિરુક્ત/રવાનુકારી entries, not as અલંકાર), and neither the grass image nor the roots-vs-plastic-
flowers contrast carries a printed ઉપમા-ઉપમેય marker (`જાણે`/`જેવું`) that would license a formal
label — `[]` is correct, not an oversight. No છંદ is named anywhere (`meter_named_on_page: false`;
std-9 ceiling is std-10 only) — a full-text sweep for `મંદાક્રાન્તા`/`પૃથ્વી છંદ`/`શિખરિણી`/
`અનુષ્ટુપ` returned zero hits.

**D — સ્વરૂપ essence.** All hard `avoid_checks` in `07_pitfalls.json` were re-verified against the
merged plan's actual fields, not assumed from A7's own claim:

- **The કૃતિ-પરિચય's paraphrase never stands in for the verbatim opening line.** M1.S1.T1's own
  `original_chunk` legitimately carries `'અમે તો આકાશો ભણી પીઠ કરી'તી ને ભીંત ચણી હતી'` as printed
  book prose; a full-text search for this exact string across every other field in the plan found
  it nowhere else — no recall answer, summary or explanation quotes it as if it were the poem's
  first line. The true verbatim (`M2.S2.T2.original_chunk`, without `ને`/`હતી`) is what every
  other field quotes when it quotes the opening line at all (e.g. `M1.S1.T1.RQ3` deliberately
  quotes a different printed sentence instead).
- **No sonnet-part name is ever used as a figure of speech.** `figures_of_speech` is `[]`
  everywhere, so this is vacuously satisfied; a targeted sweep for `સૉનેટ`/`ચોટ`/`વળાંક`/
  `ભાવપલટો`/`અષ્ટક`/`ષટ્ક` inside any `device` field found none — `ચોટ` appears only inside
  `explanation`/`concept_bullets` as a structural term (as the book's own કૃતિ-પરિચય uses it),
  never as an invented device.
- **No "હજી…સારું છે" claim or the ચોટ was turned into ઉપદેશ.** A sweep for `આપણે`, `જોઈએ`, `બોધ`
  and `શિખામણ` across every authored field found zero instructive uses — the one `જોઈએ` hit and
  the one `બોધ` hit both sit inside `media[].teaching_notes`, and both explicitly warn the teacher
  *against* moralising ("કવિ કુદરત શું કરે છે એ કહે છે, શું કરવું જોઈએ એ નહીં"; "ચોટને સામાન્ય
  બોધમાં ફેરવ્યા વગર"), not instances of it. `ઋણી`, `ભલું કે` and relief/gratitude stand
  throughout as the poem's own felt terms, never a duty.
- **The chapter is never called ગઝલ, ઊર્મિકાવ્ય or પદ anywhere.** A full-text scan found zero
  occurrences of `ગઝલ`/`ઊર્મિકાવ્ય`, and every occurrence of the substring `પદ` is part of
  `તળપદો`/`ક્રિયાપદ`, never the genre word standing alone.
- **Poetic licence never corrected.** `કરી'તી`, `ટ્હૌકા`, `પરણ`, `ગાછ્યા`, `ફુક્ક`, `મિટ્ટી`,
  `તણાં` are glossed in place and explicitly marked "ભૂલ નથી" / "છાપભૂલ નથી" wherever a child might
  mistake them for errors — never modernised inside any field that quotes them.

`08_sensitivity.json` is empty (`none_found: true`) — this nature/gratitude સૉનેટ touches none of
the seven fixed areas (ધર્મ, સમુદાય, ક્ષેત્ર, વિકલાંગતા, સંઘર્ષ, જાતિ-ભૂમિકા, સુરક્ષા), and nothing
in the merged plan contradicts that.

## E–G (reported)

- **સ્વાધ્યાય.** All four printed blocks answered end-to-end: MCQ (4/4), બે-ત્રણ વાક્યોમાં ઉત્તર
  (3/3), છ-સાત વાક્યોમાં ઉત્તર (1/1), વિદ્યાર્થી-પ્રવૃત્તિ (3/3) = 11/11 items, matching
  `01_meta.json`'s `exercise_inventory` entry-for-entry. `coverage_report.unanswered` and
  `.unmapped` are both `[]`, independently confirmed against the inventory here. The
  personal-response/pair/culture-class items (EX9–EX11) and the do-at-home item (EX10) are marked
  `is_model_answer: true` with a `teacher_note` framing them as one possible answer, never skipped.
- **Contract (`json_contract.md`'s 12 invariants).** Checked programmatically against the merged
  plan: registry consistency (5 unique `objective_id`s, every `home_topic_id`/`anchor` resolves,
  `strand_to_objective_map` covers L1–L5 one-to-one); inline `learning_objectives[].objective_text`
  matches the root registry character-for-character on all five; `MEDIA_ID_RE`
  (concept-scoped) matches all four media ids with chapter-continuous `.C{c}`; recall ids are
  `{topic_id}.RQ{n}` / `{topic_id}.TR{n}` on all fifteen recall questions, no `SR` convention
  anywhere; `publication_id` non-null (`1`, provisional — see Gaps); `topic_type` values
  (`CONCEPT`/`POEM`) are the pack's own intermediate authored enum, matching every prior chapter's
  `13_merged.json` convention — Agent 14/15 map to the closed server enum at emit, not here;
  three-tier summaries strictly increase by length on all five topics; a full digit sweep across
  every authored display field (`topic_name`, `explanation`, `real_life_example`, summaries,
  `concept_bullets`, `important_points`, recall prompts/answers, `objective_text`) found zero
  numerals; `figures_of_speech` verbatim check is vacuous (`[]` everywhere); depends_on/
  source_topic_ids all resolve to real nodes ahead of Agent 14's renumber.
- **Media.** `reuse_report.scenes: 4` equals the four topics whose `available_content_types`
  carries `"image"` (`M2.S2.T2`–`T5`); `authored: 4`, `reused: 0` — no Gujarati frame pool exists,
  so every one of the four media nodes carries `image_url: ""` and a non-empty, self-contained
  `generation_prompt` (verified: no `image_url` and no `[reused frame: …]` stamp anywhere in the
  pack). Every `negative_prompt` carries `Devanagari script labels`. Each `generation_prompt`'s
  narrator-bar line was checked programmatically and is a verbatim substring of its own topic's
  `original_chunk`. `2d_tool` is `null` chapter-wide (≤1 satisfied trivially).
- **The seven common mistakes.** None found: the સ્વરૂપ was taught as a સૉનેટ (bound-form + ચોટ),
  never flattened to સાર+બોધ+પ્રશ્નોત્તર; the fourteen lines were cut into four ભાવ-ખંડ at the
  poem's own rhetorical seams, never merged into one "કડી"; there is no ટેક to mis-split; no
  poetic licence was silently corrected; `figures_of_speech: []` is the honest, unforced answer
  everywhere; every `real_life_example` is Indian, concrete, single, and pitched at std 9; and the
  full 11-item સ્વાધ્યાય deliverable is answered, none cut as a teaching topic.

## Media
4 scenes, 4 authored, 0 reused, 0 rejected. No `2d_tool`. See Media bullet above for the full
mechanical check.

## Gaps

1. **`publication_id` is provisional and must not ship as written.** `1` is written here as the
   placeholder the shape demands (the contract requires non-null; CBSE's `1` is not portable to
   GSEB), matching this pack's own convention on every prior std-9 chapter checked (`ch01`, `ch03`
   –`ch06`). **VERIFY-2 must resolve the real GSEB publication row before the first Phase 8
   upload.** Not an A–D failure of this run; a hard precondition of upload.
2. **`chapter_master_id` is `null`.** Mandatory for upload, not discoverable from the LP2 API,
   fetched per chapter from the education DB (VERIFY-2); never derived by arithmetic.
3. **`textbook` title is `null`, unconfirmed off a rendered cover.** `01_meta.json` and
   `11_pages.json` both flag the std-9 cover as not yet read; the running-foot text
   (`ગુજરાતી (દ્વિતીય ભાષા), ધોરણ ૯`) is a footer, not a cover title, so it is not substituted here.
   `11_pages.json` grades this `confidence: medium`. Fail-soft, carried, flagged. Owner
   `01_ingestion_genre_diagnosis.md` if a cover render becomes available.
4. **`textbook_url` is a local path string** (`../Textbooks-pdf/std-9/ch-08-aabhar.pdf`) — the GSEB
   readers have no hosted URL. `textbook_pages` `32–34`, cross-checked against `11_pages.json`'s
   render + manifest + board-profile triangulation, all three agreeing.
5. **`topic_title` was derived, not authored.** No agent supplies it directly and the 32-key root
   list requires it; set to the printed chapter title `આભાર` (= `unit_title`), matching this pack's
   established convention across every prior chapter checked.
6. **`ordering` is deliberately absent** from `13_merged.json` — it is Agent 14/15's to set
   (`logical` / `textbook`), per this spec's own instruction. 31 of the contract's 32 root keys are
   written; `ordering` is the one withheld.
7. **Board and medium segments are PROVISIONAL until VERIFY-1.** `gseb_eng_gujarati9_ch8` uploads
   **clean** under a wrong medium and mis-files the plan silently if wrong — the same failure mode
   that shipped all 23 Hindi plans under the wrong medium once. Confirm before the first upload.
8. **`publication_chunk` — the same documented conflict between two agent specs noted on prior
   chapters, resolved the same way.** `reference/qc_checklist.md`/`json_contract.md` say
   `publication_chunk` is "byte-identical to `original_chunk`"; `agents/16_publication_authoring.md`
   (the field's own producing spec) says it is "the publication-facing version of the topic's
   block **as a whole**," inside which "the verbatim `original_chunk` **stays verbatim**." This run
   followed the producing agent's own spec, as every prior chapter in this batch has: on all five
   topics `publication_chunk` was verified programmatically (not eyeballed) to carry
   `original_chunk` **byte-identical as a prefix**, followed by publication-facing prose built from
   the topic's `explanation`/`real_life_example` with every vocative and direct classroom
   instruction stripped (checked: no `બાળકો`, `જુઓ —` or `બોલો` anywhere in `publication_text`,
   `publication_chunk` or `concept_publication[].publication_text`). The verse itself is not
   rewritten, reflowed or re-punctuated; its તળપદા forms, line breaks and attribution stay intact.
   The substantive invariant — the rewrite never touches verbatim — holds. Not blocked, for the
   same reason it was not blocked on `ch01`/`ch03`–`ch06`: doing so would send
   `16_publication_authoring.md` back to undo what its own spec mandates. The two specs still need
   a human reconciliation.
9. **`concept_publication` carries 2 entries per topic against 3 `concepts[].content[]` blocks —
   by design, not a miscount.** Each topic's concept has two `paragraph` blocks and one `list`
   block; `agents/16_publication_authoring.md` states explicitly to "emit one entry per `paragraph`
   block" — the list block is correctly excluded, and the two `content_index` values present (0,1)
   are exactly the two paragraph positions, never renumbered or reordered.
10. **`05b_textbook_order.json` matches the logical traversal exactly**, surfaced per
    `phase2_contract.md`'s own instruction rather than silently accepted:
    `{"human_confirmation_required": true, "reason": "textbook order is identical to logical
    order", "checked": "05b_textbook_order.json matches the logical traversal exactly (M1.S1.T1,
    M2.S2.T2, M2.S2.T3, M2.S2.T4, M2.S2.T5)"}`.
11. **A numeral inside `rhyme_scheme.note`/`overall_rhyme_scheme` states the std-10-only છંદ rule**
    (`"ધોરણ 9માં છંદ શીખવાતો નથી"`, `"છંદ ફક્ત ધોરણ 10માં જ શીખવાય છે"`). This is a grade reference,
    not a part-number reference (`કડી 2`-shape), and these two fields sit outside the digit-check's
    own enumerated scope (`explanation, real_life_example, summary, bullet, recall prompt` per this
    gate's spec) — checked and found consistent with the same phrasing already standing in
    `ch01`/`ch04`/`ch05`/`ch06`'s own merged plans. Not flagged as a violation.
12. **No sensitivity content to apply** — `08_sensitivity.json` is empty (`none_found: true`) and
    this chapter's own subject matter (nature, gratitude, a built wall) does not touch any of the
    seven fixed areas.
13. **Context routing, reported not guessed.** `author.md`, `no_hallucination_policy.md`,
    `global_content_rules.md` and `teaching_voice_gu.md` were read in full per this run's
    instructions; `qc_checklist.md`, `json_contract.md`, `phase2_contract.md`,
    `field_shape_rules.md` and `agents/16_publication_authoring.md` were read in full from the
    repository. Sibling `output9/ch01`, `ch03`–`ch06` `13_merged.json`/`validation_report.md` files
    were consulted to confirm field shapes and root-key conventions this chapter's own inputs left
    ambiguous (`topic_title`, `estimated_time`, `publication_id` placeholder, module-level
    `difficult_words`/`overall_rhyme_scheme`, `concept_publication` paragraph-only indexing); no
    illustrative content from those chapters was copied into this chapter's plan.
14. **No page render was re-opened by this agent.** `00_chapter_normalized.md` and the chain of
    prior agents' provenance notes (Agent 1's double-render 150/220 dpi cross-check, Agent 12's
    programmatic substring discipline) answered every question this gate asked.

## LP2 validator

Not run this pass — a network call to `POST /api/lp2/learning-plans/validate` was attempted and
blocked by this environment's sandboxing (no network egress available to this agent run). Every
local contract, band and hard-gate check performed here passed, so nothing in this chapter's own
checks predicts a rejection; `13_merged.json` is ready for that call whenever Phase 8 runs it.

**LP2 validator result (Phase 8):** Validation passed successfully.

```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati9_ch8_v1",
  "validation_errors": [],
  "message": "Valid"
}
```

Status: **VALID** — no validation errors found.
