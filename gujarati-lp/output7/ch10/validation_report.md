# Validation Report — std 7, ch 10 · ભાઈબંધી

સ્વરૂપ: `varta` — sub-form **પ્રાણીકથા (અનુવાદિત વાર્તા)** (confidence: high)   explanation unit: **એક ઘટના**
Topics: 7   Objectives: 7   Images: 0/3   Exercises: 12/12 blocks (62/62 printed items answered)

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` → `13_merged.json` (31 root keys, 37 topic keys, 3 modules,
5 segments, 7 topics, 13 concepts, 3 media nodes, 0 `2d_tool`). `ordering` is deliberately absent —
Agent 14/15 sets it. No working field survived the merge: `markers`, `source_lines_00_normalized`,
`genre_signals`, `cut_summary`, `not_cut_as_topics`, pitfall notes, `reuse_report`, sensitivity
severities, coverage reports and every agent's `notes[]` were all dropped. Only contract keys ship.

---

## A–D (blocking)   **PASS**

### A — diagnosis and lens

`01_meta.json` records all four signals off the rendered page: prose with named પાત્રો (દગડુ,
શાંતા, ગોલુ, ચંદેરી, ગોરિયો, ઢોરના ડૉક્ટર), an ઘટના-chain, dialogue inside `''…''` set within the
narration, and a વળાંક. The blue પ્રવેશપેટી's own line is quoted as **evidence, not verdict** —
"માણસ અને પ્રાણી વચ્ચે બંધાતા સ્નેહસંબંધની આ વાર્તા છે." Signal C fires twice on the સ્વાધ્યાય page:
the speaker-attribution block ("આપેલાં વાક્યો વાંચો, વિચારો અને તે કોણ બોલે છે તે લખો.") and the
counterfactual inside વાતચીત ("જો ગોલુએ ગોરિયાને શરીરે પોતાં ન મૂક્યાં હોત તો શું થાત ?") — both
listed in `varta.md` as વાર્તા tells for this exact chapter.

પ્રાણીકથા and અનુવાદિત વાર્તા are **sub-forms folded onto `varta.md`**, not profiles, so the
roster's વાર્તા row governs: **one ઘટના per topic**. All seven topics are cut on a printed ઘટના
boundary; `04_validation.json` passes `genre_fidelity`, `coverage` and `objectives`.

Apparatus stayed out of the plan — the teacher-addressed blue પ્રવેશપેટી (p. 63), the eleven-entry
શબ્દાર્થ box and the four-idiom રૂઢિપ્રયોગ box (p. 66), the twelve numbered સ્વાધ્યાય blocks
(pp. 66–69) and the chapter-final વ્યાકરણપેટી "વાક્યના પ્રકારો" (p. 70). This unit prints **no
student-facing કવિ/લેખક-પરિચય**, so it correctly has no CONCEPT opener; A4 recorded that the
"pre-reading opener is a topic" clause is vacuous here rather than manufacturing one.

`guiding_question` is derived from this chapter and from nothing else — "ગોરિયો સાજો થયો એ ચમત્કાર
દાક્તરની ગોળીએ કર્યો કે ગોલુની ભાઈબંધીએ ?" — it is the chapter's own closing sentence turned into a
question, and reading the seven explanations in order actually walks to it.

### B — verbatim and structure

All 7 `original_chunk`s are non-empty and **byte-identical** to their
`source_lines_00_normalized` ranges in `00_chapter_normalized.md` — checked mechanically, character
for character, all seven EXACT with no reflow, no re-spacing, no re-punctuation:

| topic | lines | orig words |
|---|---|---|
| M1.S1.T1 | 14–18 | 84 |
| M1.S1.T2 | 21–25 | 88 |
| M2.S2.T3 | 28–32 | 109 |
| M2.S2.T4 | 35–37 | 77 |
| M2.S3.T5 | 40–44 | 109 |
| M3.S4.T6 | 47–51 | 144 |
| M3.S5.T7 | 54–58 | 138 |

`word_count.original` on every topic equals the recomputed count of its own chunk.

**Script.** Base script Gujarati (U+0A80–0AFF) throughout. The whole merged file was walked and
every non-provenance string scanned: **zero** Devanagari characters, **zero** Roman characters and
**zero** `।` anywhere — in `original_chunk`, teaching prose, publication prose, concept content,
bullets, recall prompts and answers, `key_terms`, `shabdarth`/`samanarthi`/`vilom`/`vyakaran` and
module `difficult_words`. `01_meta.json`'s `extraction_notes[]` record no whitelisted non-Gujarati
printed matter for this chapter, and none was needed: nothing had to be excused. (The only Roman
letters in the file are inside ids — `M1.S1.T1.C1.IMG1`, `O1`, `L1` — and inside `image_url`,
`aspect_ratio`, `negative_prompt` and `generation_prompt`, which are machine fields addressed to an
image model, not child-facing display text.)

**Printed licence intact, not "corrected".** તળપદી and printed forms stand exactly as rendered
inside the chunks and are quoted in the same shape wherever the teaching repeats them: `કોઈ દી'`,
`ધરવ્યા`, `હા ભઈ હા`, `મૂઓ`, `દો'વાની`, `ભઈસા'બ`, `આઈ`, `બાબા`, `આકળ-વિકળ`, `સુધ્ધાં`. The
`''…''` double-quote convention is copied as printed. Two printed inconsistencies A1 recorded were
carried through unharmonised: `ભૂક્કો` (story, p. 65) against `ભુક્કો` (exercise reprint, p. 67),
and the ઉ/ઊ alternation in `ઉતરવો`/`ઊતર્યો`.

**Header furniture never entered the text.** The chunks begin at line 14; the number box + title
line `# 10 ભાઈબંધી`, the author/translator line `- શિરીષ પદ્માકર, અનુ. આશા વીરેન્દ્ર` and the QR
badge on p. 63 are all above it. In this chapter the credit is printed **under the title, not at the
end**, so the qc rule placing an attribution line inside the last topic's `original_chunk` does not
apply — A2 and A4 both held it as printed header matter, and nothing was invented to satisfy the
rule's usual shape.

**Marker arithmetic.** `00_chapter_normalized.md` carries **7 `[[ઘટના: …]]` markers = 7 topics**,
1:1 and in printed order. `[[કડી]]`, `[[દુહો]]`, `[[પદ]]` are **0 by measurement** and 0 topics
carry them — this unit is ગદ્ય throughout, with no verse quoted anywhere inside it, so the
verse-side rules are vacuous and verified vacuous rather than skipped. **12 `[[સ્વાધ્યાય: …]]`
blocks, 0 of which became a topic.** No topic in `02_structure.json` carries a સ્વાધ્યાય marker.

### C — the teaching block

Every topic has non-empty `explanation` **and** `real_life_example`. Bands hold:

| topic | explanation | real_life_example | publication_text | objective |
|---|---|---|---|---|
| M1.S1.T1 | 78 | 70 | 78 | O1 · 23 |
| M1.S1.T2 | 82 | 73 | 80 | O2 · 21 |
| M2.S2.T3 | 78 | 68 | 78 | O3 · 21 |
| M2.S2.T4 | 84 | 68 | 82 | O4 · 20 |
| M2.S3.T5 | 80 | 83 | 78 | O5 · 23 |
| M3.S4.T6 | 85 | 84 | 83 | O6 · 25 |
| M3.S5.T7 | 81 | 69 | 80 | O7 · 24 |

All fourteen teaching fields inside **55–90**; all seven `objective_text` inside **12–30**.
**No band was widened and no prose was trimmed by this agent.** See the word-count note in E–G:
two explanations sit at 91 under a naive whitespace split and at 84/85 under a lexical count, and
the difference is reported there rather than buried.

**L2 calibration.** Glossing is at the point of first use and in Gujarati, at the L2 density the
pack asks for — ordinary-looking words are glossed anyway: `ધાવવું` ("માનું દૂધ પીવું"), `ધરવ્યા`
("પેટ ભરી દીધા"), `કૂખ`, `ભીંસ`, `ગરવી`, `ભારેખમ`, `ધખધખવું`, `કંતાનના` ("જાડા ખરબચડા કાપડના"),
`આઈ` ("માએ"), `સૂમસામ`, `આકળ-વિકળ`, `ચિંતામાં ડૂબી જવું`. No Hindi word stands in for a Gujarati
one; each explanation carries 2–3 glosses and at most one subordinate clause per sentence.

**Anchors** are Indian, concrete, single, and inside std-7 reach — one domain per topic, no picture
repeated: the school પંગત waiting until the last row is served; the ઉત્તરાયણ પતંગ ને ફિરકી; the
ફળિયાનો ભાઈબંધ missing for two days; the ચીમળાયેલો રોપો and માળીકાકા's "કાલ સવારે જોઈએ"; the
શાકવાળો still calling with an unsold લારી; the hand that held the cycle, now yours; the hand let go
in the મેળાની ભીડ and found again by the ઢોલ. Not one is an adult's example and not one needs its
own glossary.

**Craft-label ceiling (std 7) holds.** No અલંકાર, છંદ, સમાસ or સાહિત્યપ્રકાર is named anywhere —
including over the chapter's two invited labels, `મંદિરના ઘંટારવ જેવો` and
`તું પણ ગોરિયાની મા જેવો જ છે`, which are taught by ear and eye inside the prose, unnamed.
`figures_of_speech: []` and `rhyme_scheme: null` on all seven topics; `overall_rhyme_scheme: null`
on all three modules. **Correct and complete, not a gap.**

### D — સ્વરૂપ essence

`varta.md`'s avoid list was run mechanically against every `explanation`, `real_life_example`,
summary tier, `concept_bullets`, `important_points`, `concepts[].content[]` and
`recall_questions[].prompt`/`answer`:

- **Gate 1 (summary-only teaching).** Every `explanation` adds what `modified_chunk` does not —
  motive, craft or consequence. Token-overlap check: 31–44 of each explanation's word types appear
  in that explanation and **not** in the topic's `modified_chunk`. Concretely: T1 reads the two
  standing questions as a daily habit asked *before the humans eat*; T4 reads the doctor's line as a
  fear, not a fact, and leaves it hanging; T5 says why શાંતાની યુક્તિ was needed at all
  (ગોરિયો "મોઢું ખોલવાય તૈયાર નથી થતો") and what "કોઈના ગળે કોળિયો ન ઊતર્યો" shows about the house;
  T7 names the writer's move of ending on a question.
- **Gate 2 (tacked-on બોધ).** Scanned for `શીખવે છે` / `બોધ એ છે` / `આપણે પણ … જોઈએ` / `શિખામણ` /
  `ઉપદેશ` / `આ વાર્તા આપણને`: **zero hits** in every field of every topic. દગડુ's ready-made rule
  ("ચંદેરીના દૂધ પર પહેલો હક્ક એના વાછરડાનો") — the likeliest place in this chapter for a moral to be
  appended — is taught as this one household's own નિયમ, in દગડુ's mouth.
- **Gate 3 (judging a sympathetic character).** Scanned for `અંધશ્રદ્ધાળુ` / `વહેમી` / `મૂરખ` /
  `ગાંડો` / `ગુનેગાર` / `બેદરકાર` / `બેજવાબદાર` / `આળસુ` / `બડાઈખોર` / `દુષ્ટ` / `ક્રૂર`:
  **zero hits**. શાંતાનું રાઈ-મીઠું and દગડુના જાપ are reported as what this house did, with no
  verdict either way; the doctor's "કેમ આટલું મોડું કર્યું ?" is answered as what happened (ઘરે
  પહેલાં પોતાના ઉપાય કર્યા), not as a charge; and the returning doctor's "દવાએ બરાબર અસર કરી" is
  never framed as credit he has not earned. One string hit on `ખોટો` was examined and cleared —
  it is `ખોટો શબ્દ છેકીને`, the printed heading of સ્વાધ્યાય block 2, not a label on a character.
- **Gate 4 (spoiling the turn).** `topic_category: "climax"` sits **once**, on `M3.S4.T6`. The
  five topics before it were scanned for the forbidden lists `07_pitfalls.json` instantiated
  (`ભીના કોથળા`, `કંતાનના કોથળા`, `પોતાં`, `બાલદી`, `ચમત્કાર`, `સાજો`, `તાવ ઊતર્યો`,
  `તાવ ઊતરી ગયો`, `સાજો થઈ ગયો`): **zero hits on M1.S1.T1, M1.S1.T2, M2.S2.T4 and M2.S3.T5.**
  One hit on M2.S2.T3 — `સાજો` — was read in place and cleared: it is that topic's own printed line
  restated ("દગડુ એ જલદી સાજો થાય એ માટે જાપ કરવા માંડે છે", p. 64, inside T3's own
  `original_chunk`), a wish before the doctor is even called, not the outcome. M2.S2.T4 ends
  unanswered on "હવે શું થશે ?" and M2.S3.T5 ends on the medicine showing no effect.
- **Gate 6 (standardising the household's register).** Every printed spoken form is quoted in its
  printed shape and glossed beside — `કોઈ દી'` and `ધરવ્યા` on T1, `ધરવ્યા` again on T5, `આઈ` and
  `બાબા` inside ગોલુ's own words on T6. Scanned for the forbidden substitutions `કોઈ દિવસ` and
  `ધરાવ્યા`: **zero hits**; `પિતા` / `મા` never appear inside ગોલુ's quoted speech.
- **Gates 5 and 7 do not engage** — this is not a પૌરાણિક કથા and not an excerpt; every topic is
  bounded by a marker and a line range and no field narrates an event outside lines 14–58.
- **Gate 8 is soft and is reported**, not blocked — see Gaps 6.
- **`figures_of_speech[].lines` verbatim check** is vacuous by measurement: the array is `[]` on all
  seven topics, so there is no device to fail the check and none was invented to fill the field.

**07 pitfalls / 08 sensitivity — every `severity: "hard"` item is addressed.** All twelve hard
`avoid_checks` in `07_pitfalls.json` map to the six gates scanned above and every one passes.
`08_sensitivity.json` raises **no hard item** (three soft topic items and one soft chapter item);
its `areas[]` use only the seven fixed labels — સમુદાય, ક્ષેત્ર, સુરક્ષા — verified as strings.
The soft guidance is honoured anyway: `આહીર` is kept exactly where the page names it and T1's
weight stays on the family's ઉલ્લાસ; T6 shows the night-time wet-sack care as ગોલુની ચિંતા and says
in the explanation that such a night-time task is done with a grown-up
("રાતે આવું કામ ઘરના મોટા કોઈને સાથે રાખીને કરાય"), never as an instruction to imitate alone; and T7
keeps both voices — the doctor's દવા and ગોલુની કાળજી — without adjudicating between them.

### Contract — all 12 invariants hold

`phase: 2`; `chapter_id = gseb_eng_gujarati7_ch10`; `plan_id = gseb_eng_gujarati7_ch10_v1`.
Every topic has ≥1 concept, each with a resolving `objective_id` and **non-empty `content[]`**
(13/13). Root `objectives[]` O1–O7 unique; every `home_topic_id` and every `anchor[]` id resolves to
a real node; `strand_to_objective_map` covers L1–L7 exactly. **Every inline `learning_objectives[]`
mirror is character-for-character identical to its root registry entry** — built at merge from the
registry itself plus `image_examples: []`, so drift is structurally impossible. Id traversal checked
against position: M1–M3, S1–S5, T1–T7 and **chapter-continuous C1–C13** (five topics carry two
concepts, so the concept counter deliberately runs ahead of the topic counter — `M2.S2.T4.C7`,
`M3.S5.T7.C13`). All 3 media ids match `MEDIA_ID_RE` **concept-scoped**. Recall ids are
`{topic_id}.RQ{n}` with `legacy_id` `{topic_id}.TR{n}` on all 19 questions — **no `.SR{n}`
anywhere**; `bloom_level` lowercase in recalls and Capitalised in `objectives[]`, as the accepted
reference plan has it. All three summary tiers strictly increase on all seven topics.
**No digit — Roman or Gujarati — in any display text**: topic/segment/module/concept names,
explanations, examples, all three summary tiers, bullets, important points, recall prompts and
answers, concept content and objective texts were each scanned. `original_chunk`, `word_count`,
`textbook_pages` and ids keep their provenance numerals untouched.
`topic_type` is the **authored** enum `STORY_TELLING` on all seven — correct for an intermediate
file; Agents 14/15 map it to `instructional`. `publication_id` is `null` — see Gaps 3.

### Exercises

`coverage_report.blocks_found` = **12** = the length of `01_meta.json`'s `exercise_inventory`,
entry for entry in printed order (blocks 1–12, folios 66–69); matched fuzzily and all twelve
matched exactly. `blocks_answered` mirrors it entry for entry. **`unanswered` is empty**, and all
**62** printed items carry a non-empty `answer` (7+5+6+5+5+5+4+1+5+10+4+5). Every
`covered_by_topics` id resolves to a real node; none is invented.

### Media

`reuse_report`: `scenes: 3`, `authored: 3`, `reused: 0`, `rejected: []` — and 3 is exactly the count
of topics whose `available_content_types` carry `"image"` (M1.S1.T1, M2.S2.T4, M3.S4.T6). Every node
carries `image_url: ""` **and** a non-empty self-contained `generation_prompt`; no `[reused frame: …]`
stamp anywhere; every `negative_prompt` carries `Devanagari script labels`; `2d_tool` is `null`
chapter-wide and on every topic. **The one-image-per-reading-scene count is 3 of 7 — reported under
§F, not blocking. See Gaps 7.**

### Publication

All 7 topics carry `publication_text` and `publication_chunk`. Each `publication_chunk` contains its
topic's `original_chunk` **byte-identical**, unreflowed and unrepunctuated, as its opening block —
the rewrite did not touch the verbatim. `concept_publication` matches `concepts[].content[]` **by
index and by count** on every topic: the emitted `(concept_id, content_index)` sequence equals the
paragraph-block index sequence exactly for all 13 concepts (22 entries), in order, none renumbered,
reordered or dropped, and every `list` block correctly carries no `publication_text`. The classroom
address is gone — `બાળકો`, `જુઓ —`, `બોલો`: **zero hits** in any `publication_text`. Spot-read
against the teaching blocks: the rewrites drop the vocative and the direct instruction, turn second
person impersonal (`બેસો → બેસાય`, `આવશે → આવે છે`), and **add no fact, gloss or reading** the
teaching block does not have.

> **Note on the checklist wording.** Agent 13's spec says "`publication_chunk` is byte-identical to
> `original_chunk`". Read literally that contradicts `agents/16_publication_authoring.md`, which
> defines `publication_chunk` as the whole publication-facing block **with the verbatim
> `original_chunk` kept verbatim inside it**. The check was run in the sense the rule protects —
> the `original_chunk` substring inside `publication_chunk` is byte-identical on all seven topics.
> Flagged so the spec text can be reconciled with 16's, not treated as a defect in this chapter.
> (The same note stands in `output7/ch08/validation_report.md`.)

---

## E–G (reported)

- **Word-count method.** Bands are counted on *words*: tokens carrying at least one letter. Gujarati
  typography spaces `:` `?` `!` `—` off as free-standing tokens, so a naive whitespace split inflates
  the count. Under the lexical count every field is inside band (explanation 78–85, example 68–84,
  `objective_text` 20–25). Under a naive whitespace split **two explanations would read 91** —
  `M2.S2.T4` and `M3.S4.T6`, one word over the ceiling; the other five run 82–86. **No band was
  widened**: the two are reported here so the margin is visible rather than buried, and the method
  is the one this pack already fixed in `output7/ch02/validation_report.md`. If VERIFY-4 settles on
  naive tokenisation, those two want a one-word trim from A12 and nothing else in the chapter moves.
- **E — સ્વાધ્યાય and risk.** All 12 printed blocks answered and skill-tagged (grammar 25, reading
  comprehension 20, vocabulary 11, speaking 6). **7 of 62 items are flagged `is_model_answer`** —
  the personal-opinion and open વાતચીત prompts are answered with teaching values, not skipped as
  "not answerable"; **35 items carry `values_filled_for_teaching`**, which is how the two printed
  કોઠા (વાક્યપ્રકાર, આજ્ઞાર્થ↔વિધ્યર્થ) and the શબ્દરમત grid were filled rather than left empty.
  **19 items are reported `unmapped`** across three blocks and **no mapping was invented to shrink
  that list**: blocks 10, 11 and 12 are the chapter's વાક્યના પ્રકારો drill, and every sentence in
  them is supplied from outside the વાર્તા (નદી, ગંગા, નર્મદા, બસ, બૅન્ક, કૌશિક; the કોઠો rows
  વાહન, કસરત, રોજનીશી, વર્ગ; the four ભાવ labels). They are fed by the chapter-final વ્યાકરણપેટી,
  which is printed apparatus and correctly not a topic — so `covered_by_topics` is empty by
  construction. That is a fact about the page, not a signal the cut missed a scene. All nine
  literature blocks map to the seven ઘટના topics. Sensitivity notes are applied, not censored:
  the નજર / રાઈ-મીઠું / જાપ material and the open ચમત્કાર ending are both taught, neither resolved.
- **F — shape and media.** Three of the four server-rejection shapes are correct in this file
  (`.RQ{n}` not `.SR{n}`, chapter-continuous concept numbers, `topic_type` mapped to the closed enum
  by Agent 14); the fourth, `publication_id` non-null, is **not** satisfied — see Gaps 3.
  `chapter_id` / `plan_id` follow `naming_conventions.md` and stay **provisional until VERIFY-1**.
  ≤1 `2d_tool` holds (zero). **One image per reading scene does not hold: 3 of 7** — Gaps 7.
  Summaries increase; no numbers in display text.
- **F — invariant 8 at segment and module level** has nothing to check: this chapter's segments and
  modules carry no summary fields (only `segment_name` / `module_name`, plus `difficult_words` and
  `overall_rhyme_scheme` on modules). Verified at topic level only.
- **F — `ordering`** is deliberately absent; root key count is therefore 31 of the contract's 32.
- **G — none of the seven usual mistakes is present.** The teaching is not સાર+બોધ+પ્રશ્નોત્તર
  (gate 1 measured above); there is no verse anywhere to merge or split, so mistakes 2 and 3 cannot
  arise; no licence was silently corrected (`કોઈ દી'`, `મૂઓ`, `દો'વાની`, `ભઈસા'બ`, `આઈ`, `બાબા`,
  `આકળ-વિકળ` all intact, and the printed ભૂક્કો/ભુક્કો and ઉ/ઊ inconsistencies were left
  unharmonised); no અલંકાર was named to fill a field; every anchor is a std-7 Indian one; and all
  twelve સ્વાધ્યાય blocks live in the exercise deliverable, none as a topic.
- **Module `difficult_words`** run 8 per module, 24 chapter-wide, each `{word, meaning, example}`
  with a std-7 Indian example sentence — inside the 5–10 band.
- **ભાષા-બોધ extras** ride on every topic with the romanized keys the server stores
  (`shabdarth` 5 each, `samanarthi` 2 each, `vilom` 0–1, `vyakaran` 1 each).

---

## Media

`scenes 3 / authored 3 / reused 0 / rejected 0`. No Gujarati frame pool exists, so `Images` reads
**0/3** by design — the zero is written, not omitted. The three frames are hung on the concept each
actually depicts, not on the topic: `M1.S1.T1.C1.IMG1` (the yard before anyone eats — દગડુ asking,
ગોલુ holding ચંદેરીની રાશ, ગોરિયો suckling), `M2.S2.T4.C7.IMG1` (the doctor's examination), and
`M3.S4.T6.C10.IMG1` (the midnight work with કોથળા, બાલદી અને લોટો, hung on C10 rather than C11
because C10 is the concept that carries the act). Each prompt is a **single photographable moment**,
not a summary, and each is self-contained — setting, fixed character appearance, action, mood,
style, and a named Gujarati narrator-bar string. Character appearance is held constant across the
three so they read as one chapter. `negative_prompt` blocks Roman **and** Devanagari script labels,
humanised cartoon animals, veterinary diagrams, temple imagery and moral caption banners — the last
of which also serves `08_sensitivity.json`'s guidance on T6 and T7. No `2d_tool`: a story does not
need one here. `rejected: []` — no frame was scored or refused, because reuse is dormant in this pack.

---

## Gaps

Honest absences, all reported, none blocking:

1. **`textbook_url` is a local path** — `../Textbooks-pdf/std-7/ch-10-bhaibandhi.pdf`. The GSEB
   readers have no hosted URL (`11_pages.json` `gaps[]`).
2. **`chapter_master_id` is `null`.** Required for upload; the GSEB row must be fetched from the
   education DB (VERIFY-2). `upload_reference/chapter_master_map.json` is still the provisional
   all-null file. Never derived by arithmetic — the Hindi pack's `355 − chapter number` is CBSE
   provenance and does not transfer.
3. **`publication_id` is `null`, and the server rejects null.** Agent 13's spec asks for a non-null
   provisional value; `upload_reference/chapter_master_map.json` holds no GSEB publication row, and
   inventing one is a `no_hallucination_policy.md` violation. `null` is written to match the sibling
   chapters that face the same absence (`ch01`, `ch09`). **This must be filled with the verified
   GSEB publication row before the first Phase 8 upload (VERIFY-2)** — it is an upload blocker, not
   a content one, and it is deliberately visible here rather than papered over with CBSE's `1`.
   Note the pack is currently inconsistent about this: `ch03` and `ch08` wrote `1`, `ch01` and
   `ch09` wrote `null`. Whichever VERIFY-2 lands, all fifteen chapters need the same value.
4. **`chapter_id` / `plan_id` board and medium segments are provisional (VERIFY-1).** A wrong medium
   slot uploads clean and mis-files the plan.
5. **`subject_ref_id` and `medium_id` are `null`** — server-injected; no confirmed GSEB subject
   record exists.
6. **Translator credit (`varta.md` avoid 8, soft).** The page prints `- શિરીષ પદ્માકર,
   અનુ. આશા વીરેન્દ્ર` under the title. The phase-2 contract has **no author or translator field**,
   so the credit cannot ride in the plan; it is preserved verbatim in `00_chapter_normalized.md`
   (line 8) and in `01_meta.json`'s `extraction_notes[]`, and no field of `13_merged.json` credits
   the translator as the author. Reported as the soft item it is.
7. **One image per reading scene is 3 of 7 — the chapter's real shape gap.** A9 flagged this for
   this agent explicitly and correctly refused to fix it from its own file. `05_with_content.json`
   records `primary_content_type: null` and `available_content_types: []` on `M1.S1.T2`,
   `M2.S2.T3`, `M2.S3.T5` and `M3.S5.T7`, following A2's mapping of the chapter's **three printed
   colour illustrations** (pp. 63, 64, 65). A media node on a topic declaring no image would be a
   contract inconsistency at Agents 14/15, so A9 wrote none. Every mechanical media assertion in
   this agent's spec therefore passes (`scenes == image-declaring topics`, `authored == scenes`,
   `reused == 0`) and §F's editorial "one per reading scene" does not — which is **reported, not
   blocking.** All four text-only topics do hold a depictable moment (દફતરનો ઘા કરીને ગોરિયા પાસે
   પહોંચતો ગોલુ; સૂમસામ ઘર અને આકળ-વિકળ ચંદેરી; બાટલીનું દવાવાળું પાણી; માના આંચળે વળગેલો ગોરિયો),
   so this is a content-type gap, not a "nothing depictable" finding. **If it is to be closed, the
   fix belongs upstream: A5 sets the content-type fields, then A9 authors four more prompts.**
   Nothing was invented here to close it.
8. **`ordering` is absent from `13_merged.json` by design** — Agent 14 sets `"logical"` and
   Agent 15 `"textbook"`.
9. **`05b_textbook_order.json` matches the logical traversal exactly** (T1 → T7, read off printed
   pp. 63–66). Per `phase2_contract.md` §Ordering this must be raised for human confirmation at
   emit: `{"human_confirmation_required": true, "reason": "textbook order is identical to logical
   order", "checked": "05b_textbook_order.json matches the logical traversal exactly"}`.
10. **Root `genre` records the slug `varta`, not `01_meta.json`'s `"વાર્તા"`.** A4 ruled explicitly
    that the root value is the roster slug with the sub-form carried separately
    (`genre_subform: "પ્રાણીકથા (અનુવાદિત વાર્તા)"`), and `phase2_contract.md` requires a slug.
    Reported for A1 to align `01_meta.json`; not a blocker, and the sub-form is preserved in this
    report and in `05_with_content.json`.
11. **Root `topic_number` is `1`, taken from `01_meta.json`.** Some sibling std-7 chapters set
    `topic_number = unit_number` (ch 3 → 3). Reported for A1; the value was not overridden here.
12. **A4's non-blocking notes travel here.** (a) Topic length is uneven — `M2.S2.T4` is three
    sentences of dialogue plus one narrative line while `M2.S2.T3` and `M3.S5.T7` each run five
    paragraphs. The unit is the ઘટના; splitting T4 would separate the doctor's warning from the
    visit that carries it. (b) `00_chapter_normalized.md` carries **no `[[ચિત્ર: …]]` markers**,
    so A2's mapping of the three printed illustrations to T1, T4 and T6 is reasoned from
    `01_meta.json`'s description rather than read off a marker — A9 treated it that way and opened
    the renders to confirm. Reported, not blocking.
13. **Printed peculiarities carried through, each with the repair noted rather than applied:**
    block 9 item 1 opens a single quote that never closes; block 11's કોઠો is headed `અજ્ઞાર્થ વાક્ય`
    where the chapter-final વ્યાકરણપેટી prints `આજ્ઞાર્થ વાક્ય` (both verified at 5×); block 7's
    reprinted ફકરો differs from the story in two places (`દગડુએ` for the story's `એણે`, and
    `ભુક્કો` for `ભૂક્કો`) and EX37 answers the paragraph **as printed**, with the discrepancy in its
    `teacher_note`; the doctor's speech on p. 66 is introduced with a semicolon; the grammar box
    prints `ઉદેશ` three times. None was levelled to the other.
14. **Re-rendering was forbidden for this run**, so A1's spec'd double-render cross-check at a higher
    dpi could not be performed. The substitute actually run — every text block cropped from the
    supplied 1300×1831 px renders (≈156 dpi) and up-sampled 2×–5× with Lanczos, then read a second
    time — is recorded in `01_meta.json`'s `extraction_notes[]`. **No transcription defect was found**
    by A5 or A10 against the renders; nothing was repaired.
15. **`concepts[].key_terms` is `[]` on all 13 concepts.** The glosses live at topic level
    (`key_terms`, 5–6 per topic, `શબ્દ — અર્થ`) and in `shabdarth`. The contract does not require
    the concept-level array to be non-empty; noted so its emptiness reads as a choice, not a loss.
16. **No page render was opened by this agent.** Every question this gate asked was answerable from
    `00_chapter_normalized.md` and the upstream JSON; the byte-exact line-range check against the
    transcription was the stronger test.

---

## LP2 validator

Not run — filled in Phase 8. `POST /api/lp2/learning-plans/validate` must return zero
`validation_errors`, and `chapter_master_id` plus the real GSEB `publication_id` (Gaps 2 and 3) must
be in place before that call.

---

**Verdict: A–D PASS. No blocking failure. `13_merged.json` is complete and ready for Agent 14.**

## LP2 validator

- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json
- Result: FAILED (validation_errors present)
- validation_errors:
  - root: 'publication_id' is required and must not be null
