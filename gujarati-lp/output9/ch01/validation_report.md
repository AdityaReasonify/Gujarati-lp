# Validation Report — std 9, ch 01 છપ્પા

સ્વરૂપ: છપ્પો (confidence: high)   explanation unit: એક છપ્પો
Topics: 4   Objectives: 3   Images: 0/2   Exercises: 12/12 (4/4 blocks)

Deliverables: two — the plan (`13_merged.json`) and the exercise pack
(`10_exercise_solutions.json`). This is a two-piece છપ્પા micro-chapter (no સ્વાધ્યાય-only
unit), so both ship in full.

## A–D (blocking)   **PASS**

Every hard item below was checked mechanically against the merged plan (`13_merged.json`), not
asserted from the intermediate files alone.

**A — diagnosis and lens.** સ્વરૂપ છપ્પો, `genre_confidence: high`, four `genre_signals`
(structure, theme, exercises, purpose) recorded off the rendered page by A1, quoting the
કૃતિ-પરિચય's own framing ("સબળ, ધારદાર કટાક્ષ") as evidence, never as the verdict. Explanation
unit `એક છપ્પો` matches the દુહા-છપ્પા roster row ("one printed piece per topic, never merged") —
two topics carry the two printed pieces, neither split nor fused. No ટેક exists in this chapter
(`structure_inventory.tek_occurrences: 0`), so that sub-check is correctly inapplicable. Not a
mixed chapter — single genre throughout. Apparatus did not become a reading scene: શબ્દ-સમજૂતી,
ભાષા-અભિવ્યક્તિ and શિક્ષકની ભૂમિકા stayed apparatus; કવિ-પરિચય and કૃતિ-પરિચય, printed as two
separate markers on this std-9 page, are the two CONCEPT topics per the roster's allowance for
student-facing પરિચય prose. The વ્યાકરણ/revision-checkpoint carve-out does not apply — this unit
prints reading text. `guiding_question` ("અખો રોજિંદા જીવનનાં કયાં દૃશ્યો બતાવીને ઢોંગી અને જડ
લોકો પર કટાક્ષ કરે છે ?") is chapter-specific, not copied from the profile, and is answered by
reading `M2.S2.T3` (પથ્થરપૂજા) and `M2.S2.T4` (ઘુવડ-સૂર્ય, હીરો-પહાણ) in order.

**B — verbatim and structure.** All four `original_chunk` fields non-empty, Gujarati script only
— a codepoint scan found zero Latin characters, zero Devanagari characters and zero `।` in any
`original_chunk`. `word_count.original` recomputed independently from each chunk by whitespace
count and matches the declared value exactly on all four (39, 81, 26, 39). Marker accounting:
`00_chapter_normalized.md` carries two `[[છપ્પો N]]` reading markers and both are carried by
exactly one topic each (`M2.S2.T3`, `M2.S2.T4`); no `[[સ્વાધ્યાય: …]]` block became a topic —
checked against all four `topic_name` values, zero overlap. તળપદા/મધ્યકાલીન forms are intact and
uncorrected: `સનાન`, `મૂરખ`, `દેખી`, `પહાણ`, `લેઈ`, `કૂડેકૂડ`, `ઘૂડ`, `ડાહ્યા` all stand as printed
inside `original_chunk`, never modernised to `સ્નાન`/`મૂર્ખ`/`જોઈને`/`પથ્થર`. The છાપ `અખા` sits
inside the verse in both pieces ("એ તો અખા બહુ ઉત્પાત…", "અખા મોટાની તો એવી જાણ…") and the printed
attribution `('અખાના છપ્પા'માંથી)` sits inside `M2.S2.T4`'s `original_chunk`, the **last** topic,
exactly where `duha_chhappa.md`'s attribution rule places it. Piece 2's first line carries the
missing terminal punctuation the render actually shows — transcribed without one, correctly, not
silently added. No header furniture (chapter-number box, QR badge, footer) entered any chunk. Ids
are consecutive: `M1`,`M2` / `M1.S1`,`M2.S2` / `T1`–`T4` / `C1`–`C4`, verified against traversal
order, not just against each other.

**C — the teaching block.** Every topic has non-empty `explanation` and `real_life_example`,
both inside the 55–90 word band with no trimming required:

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 66 | 75 |
| M1.S1.T2 | 80 | 73 |
| M2.S2.T3 | 85 | 65 |
| M2.S2.T4 | 81 | 78 |

`objective_text` O1–O3: 22, 17, 23 words — all inside 12–30. Glossing sits at the point of first
use throughout, and the L2 bar is held low for the તળપદા-dense verse (`મૂરખ`, `સનાન`, `દેખી`,
`કૂડેકૂડ`, `ઘૂડ`, `પહાણ`, `લેઈ`, `ડાહ્યા` all opened in Gujarati where they first appear, with the
modern equivalent added in a parenthesis, never as a silent replacement). Craft is named only at
the std-9 ceiling and only where this chapter's own printed ભાષા-અભિવ્યક્તિ names it: `વક્રોક્તિ`
for `મોટા` and `વિરોધાભાસ` for the ઘુવડ-સૂર્ય / હીરો-પહાણ pairs on `M2.S2.T4` only; `M2.S2.T3`
correctly carries `figures_of_speech: []` — nothing in its three lines meets a std-9 marker word,
so `[]` is the honest answer rather than a forced label. No દંડ, no Devanagari, no Roman
character outside a bracketed technical term (`વક્રોક્તિ`, `વિરોધાભાસ`, `નિપાત`, `કૃદંત`, `સમાસ`,
`નામયોગી`, `રૂઢિપ્રયોગ` are all named in Gujarati script only).

**D — સ્વરૂપ essence.** All six `severity: "hard"` avoid-checks in `07_pitfalls.json` were
verified in the field each names, not assumed from A7's own claim:

- **Satire read as satire, not sincere instruction** (the chapter's single biggest risk, per
  `07_pitfalls.json`'s own chapter-level note): `M2.S2.T3.explanation` states plainly, "અખો અહીં
  પૂજાની નહીં, આંધળી ટેવની મશ્કરી કરે છે" and never presents `પથ્થર એટલા પૂજે દેવ` /
  `પાણી દેખી કરે સનાન` as sincere religious instruction. `M2.S2.T4.explanation` states "આ જવાબ
  ડહાપણનો નથી, હઠનો છે" and never treats the ઘૂડ's reply as a reasonable position.
- **દૃષ્ટાંત before શિખામણ:** the first sentence of `M2.S2.T3.explanation` quotes `‘એક મૂરખને એવી
  ટેવ, પથ્થર એટલા પૂજે દેવ.’` before any rule word; `M2.S2.T4.explanation` opens on `‘સામાસામી
  બેઠા ઘૂડ’` before any rule word. A regex sweep for `સૌએ`, `હંમેશાં`, `જોઈએ`, `બોધ`, `શિખામણ`
  across every authored field (`explanation`, `real_life_example`, `detailed_summary`, every
  recall `answer`) on all four topics returns **zero** hits — no moral lecture, no ઉપદેશ.
- **No modernising:** every quotation inside `explanation`, `key_terms`, `vyakaran.udaharan`,
  `shabdarth.shabd`, `samanarthi.shabd`, `vilom.shabd` and `figures_of_speech.lines` was checked
  programmatically as an exact substring of its own topic's `original_chunk` — zero mismatches.
- **છાપ retained:** `અખા` stands inside both pieces' verse, never trimmed to a byline; the
  attribution note stands inside `M2.S2.T4`, never dropped.
- **Craft named only where printed:** `વક્રોક્તિ` and `વિરોધાભાસ` on `M2.S2.T4` are the only two
  devices this chapter's own apparatus names, and both `lines` strings are verified verbatim
  substrings of `M2.S2.T4.original_chunk`.
- **No fabricated biography:** every fact about અખો in `M1.S1.T1` and `M1.S1.T2` (જેતલપુર,
  અમદાવાદ પાસે, `બ્રહ્મલીલા`, `સંતપ્રિયા`, the listed કૃતિઓ, `સત્તરમું શતક-પૂર્વાર્ધ`, "જ્ઞાનના
  ગરવા વડલા") traces to text this same page prints; no birth/death year, guru or event was added
  anywhere, including in recall answers or the વિદ્યાર્થી-પ્રવૃત્તિ model answer that sends the
  child outside the chapter to research (`EX10`, correctly framed as a starting point, not a
  fact).
- `rhyme_scheme.rhyming_words` checked word-for-word against each topic's own chunk: ટેવ-દેવ,
  સનાન-પાન, ઉત્પાત-વાત (M2.S2.T3); કૂડેકૂડ-ઘૂડ, કરે-ધરે, ગયાં-થયા, જાણ-પહાણ (M2.S2.T4) — all
  present verbatim. `M1.S1.T1`/`M1.S1.T2` correctly carry `rhyme_scheme: null` (ગદ્ય).

`08_sensitivity.json` carries area `ધર્મ` on three topics (soft on `M1.S1.T2`, hard on
`M2.S2.T3`/`M2.S2.T4`) — all three are valid members of the seven fixed labels. Applied: every
explanation on `M2.S2.T3`/`M2.S2.T4` names the target as the `મૂરખ`'s or `ઘૂડ`'s blind ટેવ/હઠ,
never the act of worship or a real belief; no field names a temple, festival, deity or specific
community's practice. Both `real_life_example` anchors for these two topics are built entirely
outside religion by design — an exam-day pen/seat superstition (`M2.S2.T3`) and a classroom
method dispute (`M2.S2.T4`) — so the mockery is never generalised onto a real ritual. The media
`generation_prompt`s follow the same discipline: an ordinary roadside stone and a generic tulsi
plant, no named deity, no real temple, "mood is gently comic and observational, not devotional."

## E–G (reported)

**E — સ્વાધ્યાય and risk.** All four inventoried blocks answered; `blocks_found` (4) equals the
inventory length; `unanswered` and `unmapped` are both empty. Headings match
`01_meta.json`'s `verbatim_heading` strings, including the page's own singular `છ-સાત વાક્યમાં`
(not the corpus prior's `વાક્યોમાં`) — A1's drift note followed correctly. 12 items total (5 MCQ +
2 + 2 + 3 વિદ્યાર્થી-પ્રવૃત્તિ), every `covered_by_topics` id resolves to a real topic. Three
items are `is_model_answer: true` (the two open-ended વિદ્યાર્થી-પ્રવૃત્તિ items and the
biography-research bullet) and are marked as one possible response, never as the answer, per
`no_hallucination_policy.md`.

**F — shape and media.** All 12 `json_contract.md` invariants verified against the merged plan
programmatically: `phase: 2`; `plan_id` = `gseb_eng_gujarati9_ch1_v1`; `chapter_id` =
`gseb_eng_gujarati9_ch1`; every topic has exactly one concept with a resolving `objective_id` and
non-empty `content[]`; the objectives registry is complete and consistent (3 unique ids, every
`home_topic_id` and every `anchor[]` entry resolves, `strand_to_objective_map` covers L1–L3
exactly, single strand `L`); every inline `learning_objectives[]` mirror matches its root
`objective_text` character for character and carries `image_examples: []`; concept ids are
chapter-continuous (`M1.S1.T1.C1` … `M2.S2.T4.C4`, `c` equal to `t`) verified against the
traversal, not just against each other; recall ids are `{topic}.RQ{n}` with `legacy_id`
`{topic}.TR{n}` and **no `.SR{n}` anywhere**; media ids match `MEDIA_ID_RE`, concept-scoped;
`publication_id` non-null (see Gaps); summaries strictly increase at every topic (by length:
70<201<392, 101<167<425, 76<176<373, 97<191<426); no digit — Roman or Gujarati — occurs in any
`topic_name`, `explanation`, `real_life_example`, summary, bullet, recall prompt/answer,
`objective_text`, `publication_text` or `publication_chunk` (a full codepoint sweep across every
display field returned zero digit characters); `figures_of_speech` entries quote words verified
present in their own topic's `original_chunk`.

`topic_type` is `CONCEPT` (M1.S1.T1, M1.S1.T2) and `POEM` (M2.S2.T3, M2.S2.T4) throughout — the
correct authored enum for an Agent-13 intermediate file per `phase2_contract.md`; the closed
server enum (`instructional`/`summary`/`assessment`) is Agent 14/15's mapping at emit, not this
file's.

Bands from `field_shape_rules.md`, all held: `key_terms` 5–6 per topic (band 3–6); `concept_bullets`
and `important_points` 4 each (band 3–4); `recall_questions` 3 per topic (band 2–3), Bloom-laddered
remember→understand→analyze, every "analyze" item citing a quoted line; `difficult_words` 6 (M1) /
8 (M2), both inside 5–10; `estimated_exchanges` small integer strings ("3","4","4","5");
`bloom_level` lowercase in recalls and Capitalised in `objectives[]`, the required asymmetry held.

**G — the seven usual mistakes.** None present. The plan teaches the સ્વરૂપ (કટાક્ષ) rather than
સાર+બોધ+પ્રશ્નોત્તર; neither છપ્પો is merged with the other or split; no તળપદો form silently
corrected (`ડેડકડી`-class check: `સનાન`/`મૂરખ`/`દેખી`/`પહાણ`/`લેઈ` all intact); no અલંકાર named
because the field existed (`M2.S2.T3` honestly carries `[]`); both `real_life_example`s on the
reading-scene topics are single, Indian, non-religious by design, and inside std-9 reach (an
exam superstition, a classroom method dispute); સ્વાધ્યાય was not cut as topics and the exercise
deliverable is full (12/12).

## Media

`reuse_report`: scenes 2, authored 2, **reused 0**, rejected none — matching the two topics
(`M2.S2.T3`, `M2.S2.T4`) whose `available_content_types` carry `"image"`. Every media node
carries `image_url: ""` **and** a real, self-contained `generation_prompt`, as required while no
Gujarati frame pool exists. No `[reused frame: …]` stamp and no fabricated URL anywhere in the
pack. Every `negative_prompt` carries `Devanagari script labels`. `2d_tool` is `null` chapter-wide
(≤1 satisfied trivially). Both `generation_prompt`s name a concrete object/creature from their
own topic's `original_chunk` (a man bowing to a stone/tulsi/water; owls facing a sunrise, a hand
dropping a diamond for a stone) and depict none of the disallowed shapes — no lesson panel, no
moral-poster tableau, no virtue-in-progress. `M1.S1.T1`/`M1.S1.T2` correctly carry no media
(CONCEPT topics, `available_content_types: []`).

## Gaps

1. **`publication_id` is provisional and must not ship as written.** The contract requires a
   non-null value; `phase2_contract.md` states plainly that CBSE's `1` is **not portable** to
   GSEB. `1` is written here as the placeholder the shape demands, matching this pack's own
   convention on every prior chapter checked (`output6`–`output10`). **VERIFY-2 must resolve the
   real GSEB publication row before the first Phase 8 upload.** Not an A–D failure of this run;
   a hard precondition of upload.
2. **`chapter_master_id` is `null`.** Mandatory for upload, not discoverable from the LP2 API,
   fetched per chapter from the education DB (VERIFY-2); never derived by arithmetic.
3. **`textbook` title is not confirmed off a rendered cover.** The std-9 cover was not among the
   two supplied renders (`extraction_notes[]`); the value carried here
   (`ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 9`) is read from the page-2 running footer, confidence
   `medium` per `11_pages.json`. Fail-soft, carried, flagged. Owner
   `01_ingestion_genre_diagnosis.md` if a cover render becomes available.
4. **`textbook_url` is a local path string** (`../Textbooks-pdf/std-9/ch-01-chhappa.pdf`) — the
   GSEB readers have no hosted URL. `textbook_pages` `1–2`, confidence `medium`, cross-checked
   against the std-9 manifest row and agreeing.
5. **`topic_title` was derived, not authored.** No agent supplies it directly and the 32-key root
   list requires it; it is set to the printed chapter title `છપ્પા`, matching this pack's
   established convention (`topic_title = chapter_name` where the pack has no separate topic
   layer above the chapter).
6. **`ordering` is deliberately absent** from `13_merged.json` — it is Agent 14/15's to set
   (`logical` / `textbook`), per this spec's own instruction. 31 of the contract's 32 root keys
   are written; `ordering` is the one withheld.
7. **Board and medium segments are PROVISIONAL until VERIFY-1.** `gseb_eng_gujarati9_ch1` uploads
   **clean** under a wrong medium and mis-files the plan silently — the same failure mode that
   shipped all 23 Hindi plans under the wrong medium once. Confirm before the first upload.
8. **`publication_chunk` — the same documented conflict between two specs noted on prior
   chapters, resolved the same way.** This gate's own spec text says `publication_chunk` is
   "byte-identical to `original_chunk`"; `agents/16_publication_authoring.md` says the field is
   "the publication-facing version of the topic's block **as a whole**," inside which "the
   verbatim `original_chunk` **stays verbatim**." The file follows the producing agent's own
   spec: on all four topics `publication_chunk` was verified (not eyeballed) to carry
   `original_chunk` **byte-identical as a prefix**, followed by publication-facing prose built
   from the topic's `explanation` and `real_life_example` with every vocative and direct
   classroom instruction (`બાળકો`, `જુઓ —`, second-person questions to the reader) stripped. The
   verse is not rewritten, not reflowed, not re-punctuated; its line breaks, its તળપદા forms and
   its છાપ are intact. The substantive invariant — the rewrite never touches verbatim — holds.
   Not blocked, for the same reason it was not blocked on prior chapters: doing so would send
   `16_publication_authoring.md` back to undo what its own spec mandates. The two specs still
   need a human reconciliation.
9. **Mixed numeral scripts are printed content, not a defect.** `01_meta.json`'s `extraction_notes`
   already record this: the chapter-number box and MCQ option letters print Latin, the page-2
   footer prints the Gujarati numeral `૯`. Both are outside any `original_chunk` or authored
   display field, so no digit-in-display-text violation follows from them (verified: the merged
   plan's digit sweep is clean).
10. **`unmapped` exercises: none to report** — this two-piece chapter has reading text behind
    every printed exercise item; `10_exercise_solutions.json`'s own coverage report confirms
    `unmapped: []`, and this run's independent check agrees.
11. **Context routing, reported not guessed.** `author.md`, `no_hallucination_policy.md`,
    `global_content_rules.md` and `teaching_voice_gu.md` were read in full per this run's
    instructions. `qc_checklist.md`, `json_contract.md`, `phase2_contract.md` and
    `field_shape_rules.md` were read in full from the repository, not assumed. `schema/
    gujarati_learning_plan_skeleton.json` and five prior chapters' own `13_merged.json` outputs
    (`output7`/`output8`/`output10`) were consulted to confirm field shapes and root-key
    conventions (`topic_title`, `estimated_time`, `publication_id` placeholder, module-level
    `difficult_words` on a ગદ્ય module) this chapter's own inputs left ambiguous; none of the
    illustrative content from those chapters was copied into this chapter's plan.
12. **No page render was re-opened by this agent.** `00_chapter_normalized.md` and the chain of
    prior agents' provenance notes (Agent 5's 3×–5× zoom cross-check, Agent 12's programmatic
    substring checks) answered every question this gate asked, including the confusion pairs
    (`ધરે`/`ઘરે`, `ઘૂડ`/`ધૂડ`, `આગળ`/`આગણ`) already resolved upstream.



## LP2 validator

Status: Valid (no validation errors)

Response:
```json
{"success":true,"action":"validated_only","plan_id":"gseb_eng_gujarati9_ch1_v1","version":null,"phase":null,"is_active":null,"is_draft":null,"counts":null,"diff":null,"publication_id":null,"publication_name":null,"validation_errors":[],"message":"Valid"}
```

