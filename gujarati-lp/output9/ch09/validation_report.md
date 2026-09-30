# Validation Report — std9/ch09 (પારખું)

સ્વરૂપ: હળવું એકાંકી (natak_ekanki) (confidence: high)   explanation unit: એક દૃશ્ય-પ્રસંગ (સંવાદ-ખંડ)
Topics: 9   Objectives: 8   Images: 0/7   Exercises: 12/12 items (4/4 blocks)

**Final-pass re-QC note.** This is a fresh Agent 13 run against the chapter as it now stands on
disk — every input layer (`05_with_content.json`, `07_pitfalls.json`, `08_sensitivity.json`,
`09_media.json`, `10_exercise_solutions.json`, `11_pages.json`, `12_authoring.json`,
`16_publication.json`, `01_meta.json`, `04_validation.json`) was re-read from scratch and
cross-checked programmatically rather than assumed from the previous pass. No upstream file has
changed since the last merge (`12_authoring.json` and `16_publication.json` are unchanged; every
`explanation`, summary, `publication_text` and `publication_chunk` in the merged plan was verified
character-for-character against these two source files). `13_merged.json` was rebuilt field-by-field
from the nine input layers and diffed against the file already on disk: the only differences found
were the intentional drop of the working `topic_id` key from each media node (not part of the
`phase2_contract.md` media-node schema) — everything else matched exactly. The verdict below is a
full re-run of every mechanical check, not a copy-forward of the prior report.

## A–D (blocking)   **PASS**

### A — Diagnosis and lens.   PASS
`01_meta.json.genre_signals` records the પાત્રો box, the single `(સ્થળ : દવાખાનું  સમય : સવારના
દસ)` opening direction, colon-led speaker tags, 41 counted રંગસૂચના brackets, 4 entrances/4 exits
and no scene-numbering — `genre_confidence: "high"`, and `natak_ekanki.md`'s own provenance note
names this exact chapter as one of the four that fixed the profile. `explanation_unit` ("એક
દૃશ્ય-પ્રસંગ (સંવાદ-ખંડ)") matches the નાટક/એકાંકી roster line ("one stage-beat") exactly. Marker
accounting re-walked against `00_chapter_normalized.md` directly (`grep '^\[\['`): `[[લેખક-પરિચય]]`
→ `M1.S1.T1`, `[[કૃતિ-પરિચય]]` → `M1.S1.T2`, `[[પાત્રો]]` → header `M1.S2.T3` plus six stage-beats
`M2.S3.T4`…`M2.S6.T9` — 9 topics, no gap, no double-claim. All three `[[સ્વાધ્યાય: …]]` markers plus
`[[શબ્દ-સમજૂતી]]`, `[[વિદ્યાર્થી-પ્રવૃત્તિ]]`, `[[ભાષા-અભિવ્યક્તિ]]` and `[[શિક્ષકની ભૂમિકા]]`
correctly carry no topic. `guiding_question` is chapter-derived, and reading the nine topics'
`explanation`s in printed order answers it: T4–T5 set up the doctor's English-laced bragging and the
unseen સસરો's costume; T6 shows him garbling that same costume; T7 shows the first ચોટ
(મનમોહનદાસ); T8–T9 show the second (નરરત્નમણિરાવ) unraveling the same boasts one by one.

### B — Verbatim and structure.   PASS
All 9 `original_chunk` fields non-empty (checked programmatically against `05_with_content.json`);
zero Devanagari codepoints (U+0900–U+097F) anywhere, zero `।` anywhere. Roman-script hits (T4
Say/staff/Humbug/Nonsense, T5 strange/Rascal/fatel, T7 Mixture/research/allopathy/surcharge
collector/Swindle, T8 absolutely painless process/Hard facts) are the exact printed-content
exception this agent's own spec and `qc_checklist.md` name by chapter and number ("the Roman
dialogue lines in std-9 ch 9"), confirmed against `01_meta.json.extraction_notes` — not a
script-purity violation. Ids consecutive and chapter-continuous (M1–M2 / S1–S6 / T1–T9 / C1–C10),
`M2.S5.T7` correctly carrying two concepts (C7, C8) for its double beat, and the following topic
`M2.S6.T8` correctly continuing at `C9` (not restarting) — media id `M2.S6.T8.C9.IMG1` matches.
`original_chunk` is verified to sit as an exact, untouched substring inside `publication_chunk` on
every one of the 9 topics — the rewrite in Agent 16's file surrounds the verbatim with fresh prose
but never re-touches it, matching `agents/16_publication_authoring.md`'s own definition of
`publication_chunk` ("the publication-facing version of the topic's block as a whole… the verbatim
`original_chunk` stays verbatim inside it").

### C — The teaching block.   PASS
`12_authoring.json` supplies non-empty `explanation` and `real_life_example` on all 9 topics.
Word counts (whitespace split, programmatic):

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 75 | 73 |
| M1.S1.T2 | 82 | 81 |
| M1.S2.T3 | 79 | 85 |
| M2.S3.T4 | 83 | 77 |
| M2.S3.T5 | 77 | 74 |
| M2.S4.T6 | 81 | 77 |
| M2.S5.T7 | 85 | 82 |
| M2.S6.T8 | 84 | 82 |
| M2.S6.T9 | 85 | 89 |

All 18 values land inside 55–90; `objective_text` on O1–O8 runs 23–29 words, inside 12–30. Glossing
sits at the point of first use throughout (`વતન (જન્મ-સ્થળ)`, `પ્રયોગશીલ (નવી નવી રીતો
અજમાવનારા)`, `સવાર` explicitly disambiguated from ઘોડેસવાર in T3) and holds the L2 bar low for the
Roman-English code-switching that is this chapter's own hard-comprehension load. `real_life_example`
anchors are Indian, single, and inside std 9's reach (કામ કરતાં મોટેરાં, સમાચાર, જવાબદારી): a
multi-skilled neighbour (T1), a school prize-function mix-up (T2), an empty snack stall at recess
(T3), a classmate's English-laced showing-off (T4), an ST-બસ-સ્ટૅન્ડ pickup by description alone
(T5), a memorised poem line garbled under pressure (T6), a boasted cricket score punctured by the
coach himself (T7), a kite-flying boast unwound by follow-up questions (T8), a friend's hollow
boasting exposed by one plain question (T9) — none adult-only, none outside India, none needing its
own glossary, no domain repeated back-to-back. Craft naming stays inside the std-9 ceiling:
`સાહિત્યપ્રકાર` (હળવું એકાંકી) is named directly from the chapter's own printed કૃતિ-પરિચય in T2's
explanation and O1; no અલંકાર, છंद, સંધિ or સમાસ label is asserted anywhere this prose page does not
support, and `figures_of_speech: []` / `rhyme_scheme: null` hold on all 9 topics (ગદ્ય, confirmed
against `01_meta.json.structure_inventory`'s own kadi=duha=pad=ghatna=tek_occurrences=0). Three-tier
summaries strictly increase by word count on every topic (verified programmatically, e.g. M2.S6.T9:
19 < 37 < 80).

### D — સ્વરૂપ essence.   PASS
All 7 `severity:"hard"` avoid-checks in `07_pitfalls.json` were read directly against the authored
text this pass (`explanation`, both summaries, `concept_bullets`, and every `recall_questions[]`
prompt/answer), not assumed from the pitfalls file's own wording:

- **M1.S1.T1** — `explanation`/summaries/recall state only વતન અમદાવાદ, the four roles, and the
  named titles; no birth/death year, award or movement appears anywhere. The `'પ્રવેશ બીજો'`
  misconception is corrected explicitly: "'પ્રવેશ બીજો' પુસ્તકનું નામ છે, 'પારખું'નો કોઈ
  દૃશ્ય-ક્રમાંક નહીં," repeated in RQ2.
- **M1.S1.T2** — no field ends on બોધ/ઉપદેશ; `explanation` and RQ2 state plainly that the doctor
  does not discover either identity himself — "બીજાં પાત્રો જ પોતાની ઓળખ ખોલે છે... ડૉકટર જાતે
  શોધી કાઢતો નથી."
- **M2.S3.T4** — the doctor's Roman-script lines stand exactly as printed wherever cited: `'Say.'`,
  `'You don't understand.'` (detailed_summary), `staff` (explanation, both concept paragraphs, RQ1
  and RQ2 answers), `'Humbug !'`, `'Nonsense !'` (explanation, detailed_summary, RQ3) — none
  translated, softened or dropped; `'ધીરજનાં ફળ મીઠાં'` and the register word `compounder` are kept
  intact alongside them.
- **M2.S4.T6** — the doctor's jumbled costume lines are quoted exactly as printed everywhere they
  appear (`'કાશ્મીરી ધોતિયું'`, `'ચાર પાટલીની ટોપી'`, `'લાંબું કાળું ધોતિયું, ચાર પાટલીનો કોટ'`,
  `'કાશ્મીરી કોટ'`), never silently rearranged into the correct combination — checked as exact
  substrings of `original_chunk` in both `explanation` and RQ2/RQ3's answers.
- **M2.S5.T7** — every doctor claim is framed as his own boast, never as fact: "આ ડૉકટરનો પોતાનો
  દાવો છે, હકીકત નહીં" (explanation), "આ બધા ડૉકટરના પોતાના દાવા છે, પુરાવો નથી" (concept C7), RQ2's
  answer states outright that the claim should not be taken as fact and cites the later puncture
  ("પીયૂષ-ડ્રોપ્સ પીગળી ગયાં").
- **M2.S6.T8** — no interior motive is invented for the doctor's honesty; `explanation` says so
  explicitly — "કોઈ પણ પંક્તિ ડૉકટરના મનની વાત કહેતી નથી, ફક્ત આ ટૂંકા જવાબો જ છપાયા છે" — echoed
  again in `detailed_summary`. Only the printed deflating answers (`'ભાડૂતી... ભાડૂતી !'`,
  `'પીગળી ગયાં, બુઝુર્ગ મિત્ર'`) are used.
- **M2.S6.T9** — no field ends on બોધ/સંદેશ/શિખામણ/ઉપદેશ; the closing line and title pay-off
  (`'પારખું કરવા નીકળ્યો. પારખું થઈ ગયું.'`) are read as the play's own irony, RQ3's answer stating
  the shift in the word's weight rather than moralising. નરરત્નની દીકરી regret is kept as this one
  father's private matter ("પોતાની દીકરીનું ઘર બગડ્યું એ સમજતાં નરરત્ન રડી પડે છે") with no editorial
  on arranged marriage in general — the soft sensitivity item is honoured too.

`08_sensitivity.json`'s two soft items (no hard items exist in this file) are also honoured in the
field: **M2.S6.T9**'s slap is framed as "પોતાની જ છેતરપિંડી પકડાયેલા ડૉકટરની ફૂટેલી, બાલિશ
પ્રતિક્રિયા છે, ન્યાય નહીં" — the fraud's own foolish reaction, explicitly not justice, never
something to imitate. **M2.S6.T8**'s doctor line about chanting versus painless treatment is not
quoted at all in the authored text, so the ધર્મ caution's risk never arises. `figures_of_speech` is
`[]` and `rhyme_scheme` is `null` on every topic — correct for a prose/drama chapter — so the
"quoted verbatim" invention-check has nothing to trip on.

## E–G (reported)

- **E — Exercises: clean.** `10_exercise_solutions.json.coverage_report`: all 4 inventoried blocks
  (MCQ×4, બે-ત્રણ વાક્યમાં ઉત્તર×3, સવિસ્તાર ઉત્તર×3, વિદ્યાર્થી-પ્રવૃત્તિ×2 — 12 items, EX1–EX12)
  match `01_meta.json.exercise_inventory` exactly; `unanswered: []`, `unmapped: []`.
- **E — Sensitivity: no hard items**, both soft items applied — see D above.
- **F — Shape: the 12 `json_contract.md` invariants hold**, checked against the rebuilt
  `13_merged.json` programmatically. `phase: 2`; `chapter_id`/`plan_id` =
  `gseb_eng_gujarati9_ch9`/`_v1`; every topic carries `objective_ids` resolving to the root registry;
  8 unique `objective_id`s, every `home_topic_id` and `anchor[]` entry resolves against the 10 real
  concept ids; `strand_to_objective_map` covers L1–L8 exactly, single strand `L`; every inline
  `learning_objectives[]` entry matches its root `objective_text` character for character; concept
  ids chapter-continuous `M1.S1.T1.C1`…`M2.S6.T9.C10`; recall ids `{topic}.RQ{n}` with `legacy_id`
  `{topic}.TR{n}`, **zero** `.SR{n}` anywhere, `bloom_level` lowercase in every recall item; media
  ids match `MEDIA_ID_RE`, concept-scoped, resolving to a real concept in every case; `publication_id`
  non-null (`1`, provisional — see Gaps); `topic_type` is the authored enum
  (`CONCEPT`/`STORY_TELLING`) throughout, correct for this intermediate file; three-tier summaries
  strictly increase by word count on all 9 topics; `concept_publication` blocks match
  `concepts[].content[]` by index and by count on all 9 topics (verified programmatically, including
  the two-concept M2.S5.T7).
- **F — one reported (non-blocking) item, carried forward: a numeral in authored display text.**
  `M2.S5.T7`'s `explanation`, `detailed_summary`, and concept `M2.S5.T7.C7`'s second paragraph each
  carry the Gujarati numeral `૫૦૦-૬૦૦` ("મહિને ૫૦૦-૬૦૦ દાંત") — the doctor's own printed boast,
  correctly preserved verbatim inside `original_chunk`, but also echoed with the same digit-string
  inside freely-composed teaching prose. `qc_checklist.md` places "no numbers in display text" under
  Section F (reported), not B, C or D, so this does not block the run — but it is real and is named
  here again, owner **Agent 12** (`agents/12_runtime_authoring.md`); fix is mechanical: spell the
  quantity as `પાંચસો-છસો`, matching how the same fact is already spelled correctly elsewhere in this
  very topic (`પચાસેક ઓપરેશન્સ`, `હજાર-બારસોની average`) and matching how `16_publication.json`'s own
  `publication_text` for this topic already spells it (`પાંચસો-છસો`) — so the merged plan's
  `publication_text` and `concepts[].content[].publication_text` are clean; only the
  `explanation`/`detailed_summary`/one concept-paragraph `text` field carry the digit. No other digit
  or numeral (Arabic or Gujarati) was found anywhere else in any authored display field across all 9
  topics, `objective_text` included — re-checked this pass programmatically against `topic_name`,
  `explanation`, `real_life_example`, all three summaries, `concept_bullets`, `important_points`,
  every `recall_questions[].prompt`/`.answer`, `publication_text`, and every concept
  `content[].text`/`.publication_text`.
- **F — a second observation, also non-blocking (not a `qc_checklist.md` gate at all): the
  ભાષા-બોધ per-topic counts in `reference/bhasha_bodh.md`.** Its own std-9 row targets `samanarthi`
  at 2–4 per topic; `12_authoring.json` runs at 0–1 on most topics, and `M2.S4.T6`'s `shabdarth` runs
  at 3, one below the 4–6 target. This table is not named anywhere in `qc_checklist.md`'s A–D or E–G
  sections, so it does not gate this run; recorded here only because `bhasha_bodh.md` calls it "the
  contract band."
- **G — usual failure modes: none observed.** Genre taught as હળવું એકાંકી throughout, not flattened
  to સાર+બોધ+પ્રશ્નોત્તર; neither ચોટ resolved early (the second, નરરત્નમણિરાવ, stays confined to
  `M2.S6.T8`/`T9`); no Roman-script line mistranslated, softened or dropped (see D); no અલંકાર named
  anywhere on this ગદ્ય page; all 9 `real_life_example`s are single, Indian, in-standard, and none
  reaches for an adult-only domain (ઓફિસ/હપતા/વીમો); સ્વાધ્યાય was not cut as teaching topics and the
  exercise deliverable is complete (12/12).

## Media

`09_media.json.reuse_report`: `scenes: 7`, `authored: 7`, `reused: 0`, `rejected: []` — matches
exactly the 7 topics whose `available_content_types` carries `"image"` (`M1.S2.T3`, `M2.S3.T4`,
`M2.S3.T5`, `M2.S4.T6`, `M2.S5.T7`, `M2.S6.T8`, `M2.S6.T9`; the two પરિચય topics `M1.S1.T1`/`T2`
correctly carry none). All 7 media nodes re-verified against the rebuilt merged plan: `image_url: ""`
on every one, non-empty self-contained `generation_prompt`, `negative_prompt` containing "Devanagari
script labels" on all 7, media ids concept-scoped and matching `MEDIA_ID_RE` exactly
(`M2.S6.T8.C9.IMG1` correctly resolves to T8's actual concept `C9`, not a mis-numbered `C8`).
`2d_tool: null` chapter-wide, trivially ≤1.

## Gaps

1. **`publication_id` is provisional and must not ship as written.** Written here as `1`, matching
   this pack's own established std-9 convention (checked against `output9/ch01` and `ch03`, both of
   which also write `1`) — not CBSE's row, a placeholder the shape demands.
   `phase2_contract.md`'s own rule stands: the real GSEB publication row must be resolved (VERIFY-2)
   before the first Phase 8 upload.
2. **`chapter_master_id`/`subject_ref_id` remain `null`** — unresolved server-side lookups pending
   VERIFY-2, unrelated to this run.
3. **`chapter_id`/`plan_id`'s `gseb`/`eng` segments remain provisional** pending VERIFY-1.
4. **`textbook` title is not confirmed off a rendered cover** — carried from the page-2 running
   footer per `11_pages.json`, confidence medium; the std-9 cover was not among this chapter's own
   renders.
5. **`textbook_url` is a local path string** (`../Textbooks-pdf/std-9/ch-09-parkhu.pdf`); no hosted
   URL exists for this pack.
6. **`ordering` is deliberately absent** from `13_merged.json` — Agent 14/15's to set, per this
   agent's own instruction. 31 of the contract's 32 root keys are written; `ordering` is the one
   withheld.
7. **The two F-level items above** (`M2.S5.T7`'s numeral, and the ભાષા-બોધ `samanarthi` shortfall)
   are recorded here again for visibility: neither blocks this PASS, both are cheap for a future
   authoring touch to close.
8. **The T7→T8 bracket-split note from `04_validation.json`'s genre_fidelity check** travels here:
   one printed line holds two stage directions back to back
   (`(આંટા મારે છે. નરરત્નમણિરાવ દાખલ થાય છે.)`) — the doctor's own continued pacing was correctly
   kept with T7 and the entrance direction correctly opens T8; Agent 4 flagged this as a
   transcription instruction, not a topic-boundary defect, and this pass confirms the cut followed
   it.
9. **`unmapped` exercises: none to report** — `10_exercise_solutions.json`'s own coverage report
   confirms `unmapped: []`, and this pass's independent check agrees.
10. **Mixed numeral scripts inside `original_chunk` are printed content, not a defect** — the
    Gujarati numeral `૫૦૦-૬૦૦` printed on the page (M2.S5.T7's own dialogue) is correctly preserved
    verbatim inside `original_chunk` and inside `publication_chunk`'s verbatim portion; the Gap item
    above is about the *separate* copy of that same digit-string that leaked into freely-composed
    `explanation`/`detailed_summary` prose, which is the display-text rule this checklist actually
    gates.
11. **No upstream deltas found this pass.** `12_authoring.json` and `16_publication.json` — the two
    files a prior pass on this chapter had to wait for — are unchanged since that pass produced the
    merge; this run is a genuine independent re-verification (every check above re-run from the
    source files, not carried forward from the prior report's prose), and it reaches the same PASS.

## LP2 validator
Not attempted this pass — no server call was made. Filled in at Phase 8, once VERIFY-1/VERIFY-2
resolve the provisional board/medium segments and the real `publication_id`/`chapter_master_id`.

## LP2 validator

**Validation Timestamp:** 2026-08-30T02:52:35Z

**HTTP Status:** 200

**Response:**
\`\`\`json
{"success":true,"action":"validated_only","plan_id":"gseb_eng_gujarati9_ch9_v1","version":null,"phase":null,"is_active":null,"is_draft":null,"counts":null,"diff":null,"publication_id":null,"publication_name":null,"validation_errors":[],"message":"Valid"}
\`\`\`

**Validation Errors:** None

**Status:** ✓ VALID
