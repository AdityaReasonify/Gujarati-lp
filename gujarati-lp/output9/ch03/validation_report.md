# Validation Report — std 9, ch 03 જ્યાં જ્યાં વસે એક ગુજરાતી

સ્વરૂપ: ઊર્મિકાવ્ય-ગીત (confidence: high)   explanation unit: એક કડી
Topics: 7   Objectives: 7   Images: 0/6   Exercises: 7/7 (3/3 blocks)

Deliverables: two — the plan (`13_merged.json`) and the exercise pack
(`10_exercise_solutions.json`). This unit prints a full reading text plus a printed સ્વાધ્યાય, so
both ship in full (not the revision-checkpoint / વ્યાકરણ-એકમ single-deliverable case).

## A–D (blocking)   **PASS**

Every hard item below was checked mechanically against the merged plan (`13_merged.json`), not
asserted from the intermediate files alone.

**A — diagnosis and lens.** સ્વરૂપ ઊર્મિકાવ્ય-ગીત, `genre_confidence: high`, four `genre_signals`
(structure, theme, exercises, purpose) recorded off the rendered page by A1, quoting the
કૃતિ-પરિચય's own framing ("ગુજરાતનો મહિમાગાન કરતું…") as evidence, never as the verdict.
Explanation unit `એક કડી` matches the ઊર્મિકાવ્ય-ગીત roster row. `structure_inventory` (kadi 5,
tek_occurrences 5) matches a grep of `00_chapter_normalized.md` exactly (5 `[[કડી n]]`, 5
`[[ટેક]]` markers). **ટેક handling verified against the profile's changed-words rule**, which
this exact chapter is the profile's own worked example for: only the opening occurrence carries
changed words (ટેક couplet + `જ્યાં જ્યાં બોલાતી ગુજરાતી…`) and is cut as its own topic
(`M2.S2.T2`); the four later identical occurrences are correctly **not** re-cut as topics — each
is referenced via `depends_on` on the કડી topic it closes (T3, T4, T5, T7 all carry `M2.S2.T2` in
`depends_on`), matching "where the ટેક returns identical, teach it once and reference it after."
Apparatus did not become a reading scene: શબ્દ-સમજૂતી (3 sub-blocks), વિદ્યાર્થી-પ્રવૃત્તિ,
ભાષા-અભિવ્યક્તિ and શિક્ષકની ભૂમિકા stayed apparatus (cross-checked against all 7 `topic_name`
values — zero overlap); કવિ-પરિચય + કૃતિ-પરિચય, printed as two markers, are combined into one
CONCEPT topic (`M1.S1.T1`) per the roster's allowance for student-facing પરિચય prose — a
documented content judgement, not a coverage gap. The વ્યાકરણ/revision-checkpoint carve-out does
not apply — this chapter prints reading text. `guiding_question` ("ગુજરાતી માણસ જ્યાં જાય ત્યાં
ગુજરાત સાથે લઈ જાય છે — કવિ કયાં કયાં ચિત્રો મૂકીને આ વાત આપણી આંખ સામે ઊભી કરે છે ?") is
chapter-specific, not copied from the profile, and reading `M2.S3.T3` → `M2.S3.T4` → `M2.S3.T5` →
`M2.S4.T6` → `M2.S4.T7` in order does answer it — each is one more ચિત્ર (સૂર્ય-ઉષા, ગુર્જર
વાણી-લહાણી, પુણ્યભૂમિ-ભરતી, કોડ-રાસ) building to the closing જયઘોષ.

**B — verbatim and structure.** All 7 `original_chunk` fields non-empty, Gujarati script only — a
codepoint scan found zero Latin characters, zero Devanagari characters and zero `।` in any
`original_chunk`. Marker accounting: 5 `[[કડી n]]` + 5 `[[ટેક]]` markers in
`00_chapter_normalized.md`; the 5 `[[કડી n]]` markers are each carried by exactly one topic
(T3–T7, one marker note per topic); the printed fusion (a કડી's own lines followed, same
printed block, by its closing ટેક) is preserved inside `original_chunk` — T3, T4, T5, T7 each
carry their કડી's lines plus the identical closing ટેક couplet, and T6 carries only its two lines
because no ટેક follows it before કડી 5. No `[[સ્વાધ્યાય: …]]` block became a topic — checked
against all 7 `topic_name` and `original_chunk` values, zero overlap. Archaic/તળપદા/કાવ્ય-રૂપ
forms stand uncorrected throughout: `તણાં`, `હેલાતી`, `ભોમ`, `મિરાત`, `અદલ`, `કેરી`, `ઝૂઝે`,
`ગરજી`, `હુલાતી` all appear exactly as printed. No comparison text ("ne", "તણા" with the extra
commas ભાષા-અભિવ્યક્તિ prints) was substituted for the verse's own wording in `M2.S4.T6`'s
`original_chunk` — the verse line, not the apparatus quotation, is what stands, per
`01_meta.json`'s own extraction note. No header furniture entered any chunk. Ids consecutive and
resolve after traversal: `M1`,`M2` / `M1.S1`,`M2.S2`,`M2.S3`,`M2.S4` / `T1`–`T7` / `C1`–`C7`.

**C — the teaching block.** Every topic has non-empty `explanation` and `real_life_example`, both
inside the 55–90 word band with no trimming required:

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 84 | 78 |
| M2.S2.T2 | 84 | 79 |
| M2.S3.T3 | 80 | 77 |
| M2.S3.T4 | 84 | 75 |
| M2.S3.T5 | 84 | 79 |
| M2.S4.T6 | 85 | 81 |
| M2.S4.T7 | 86 | 70 |

`objective_text` O1–O7: 20, 27, 23, 21, 22, 24, 24 words — all inside 12–30. Glossing sits at the
point of first use throughout (`ઓતર`-class L2 bar held: `તણાં`, `હેલાતી`, `ઉર`, `ભોમ`, `મિરાત`,
`ખંડ`, `ગરજી` all opened in Gujarati where they first appear). Craft named only at the std-9
ceiling and only where the lines carry it: `પ્રાસસાંકળી` on `M2.S3.T4` (વાણી-લહાણી-શાણી),
`રૂપક` on `M2.S3.T5` (ગુર્જર ભરતી ઊછળે છાતી) and `M2.S4.T6` (ઉર વૈભવ રાસ રચાય) — all three inside
the std-9 seven-device canon (`reference/alankar_chhand.md`). `M2.S3.T3` correctly carries
`figures_of_speech: []`: the personifying `દોડે`/`હસે` picture is real but its label
(સજીવારોપણ) is **std-10 canon, not std-9** per the measured placement table — so the honest move
is `[]` plus a પ્રાસ sentence in `explanation` ("'વાસ', 'પ્રકાશ' અને 'પ્રભાત' — ત્રણેય પંક્તિના
છેડા…"), which satisfies the profile's "figures_of_speech OR a craft sentence" gate without
naming a device above this standard's ceiling. No `છંદ` named anywhere (std-10-only); module
`M2.overall_rhyme_scheme` states this explicitly. No Devanagari, no Roman outside a bracketed
technical term, no `।`.

**D — સ્વરૂપ essence.** All `severity: "hard"` avoid-checks in `07_pitfalls.json` (23 across 7
topics) were verified in the field each names, not assumed from A7's own claim — and this
chapter is one of only two the profile itself names as most tempted toward slogan/political
framing (the other being std-6 ch 7), so this check was run literally, not summarised:

- **No slogan anywhere.** A regex sweep for `જોઈએ`, `રાખવી જોઈએ`, `કરવો જોઈએ`, `આપણે સૌએ`,
  `આપણે બધાએ` across every authored field (`explanation`, `real_life_example`, three summaries,
  `concept_bullets`, `important_points`, every recall `answer`) on all 7 topics returns **zero**
  hits. The poem's own જયઘોષ (`M2.S4.T7`) is quoted/echoed, never extended into reader
  instruction.
- **No political framing.** A sweep for `સરકાર`, `પક્ષ`, `યોજના`, `સીમા`, `સરહદ`, `ચૂંટણી` across
  the same fields returns zero hits. `M2.S3.T5`'s naming of કૃષ્ણ, દયાનંદ, દાદા stays inside the
  book's own `'મહામાનવો'` framing — no state, army or border invoked.
- **Feeling before picture**, checked topic by topic: every POEM topic's `explanation` opens on a
  concrete noun from that topic's own `original_chunk` (`M2.S2.T2` → `ગુજરાતી`/`ગુજરાત`;
  `M2.S3.T3` → the four directions; `M2.S3.T4` → `ગુર્જર વાણી`; `M2.S3.T5` → `કૃષ્ણ, દયાનંદ ને
  દાદા`; `M2.S4.T6` → `કોડ`; `M2.S4.T7` → `જય જય`) — never the abstract ભાવ first.
- **Literal reading of a figurative line never asserted**: `M2.S3.T3.explanation` states plainly
  "ખરેખર સૂરજ દોડતો નથી; આ કવિનું ચિત્ર છે"; `M2.S3.T5.explanation` marks `ગુર્જર ભરતી`/
  `ગુર્જર માત` as "બંને ચિત્રો છે, હકીકત નહીં"; `M2.S4.T6.explanation` marks the રાસ line the
  same way.
- **ટેકનું ચલિત named, not skipped**: `M2.S2.T2.explanation` states in its own words what changed
  between `વસે` and `બોલાતી` (વસવાટ → ભાષા બોલવી), satisfying objective O2 directly.
- **Respect the text's world (M2.S3.T5, hard sensitivity item)**: `explanation` names કૃષ્ણ,
  દયાનંદ (સરસ્વતી), દાદા (દાદાભાઈ નવરોજી) exactly as the book's own શબ્દ-સમજૂતી does, as
  `'મહામાનવો'`, with no added religious, theological or biographical claim.
- **Never invent a poet's intention (`M2.S4.T7`, hard item)**: `explanation` gives `અદલ`'s
  printed meaning (`બરાબર, ખરું`) as the settled reading and names the ઉપનામ resemblance only as
  "એક રસપ્રદ યોગાનુયોગ… નિશ્ચિત દાવો નહીં" — never asserted as a છાપ, matching the fact that this
  is a ગીત, not a પદ.
- **No modernising:** every quotation inside `explanation`, `key_terms`, `vyakaran.udaharan`,
  `shabdarth.shabd`, `samanarthi.shabd`, `vilom.shabd` and `figures_of_speech.lines` was checked
  programmatically as an exact substring of its own topic's `original_chunk` — zero mismatches.
- **No fabricated biography**: every fact about ખબરદાર in `M1.S1.T1` (જન્મસ્થળ દમણ, પારસી,
  વેપારી, the listed કાવ્યસંગ્રહો) traces to text this same page prints; no birth/death year
  beyond the printed dates, no guru, no award was added anywhere, including in recall answers.

`08_sensitivity.json` carries area `સમુદાય` (soft, `M1.S1.T1` and `M2.S2.T2`) and `ધર્મ` (hard,
`M2.S3.T5`) — all valid members of the seven fixed labels. Applied: `M1.S1.T1.explanation` states
the Parsi fact plainly, once, with no comment on Parsi traits; `M2.S2.T2`'s real_life_example
stays inside a Gujarati family's own world (a son working in Dubai) and never raises borders or
citizenship; `M2.S3.T5` handled as above.

## E–G (reported)

**E — સ્વાધ્યાય and risk.** All 3 inventoried blocks answered as EX1–EX7 (5 MCQ + 1 બે-ત્રણ
વાક્યોમાં + 1 પાંચ-છ વાક્યોમાં); `coverage_report.blocks_found` (3) equals the inventory length;
`unanswered` and `unmapped` are both empty. Every `covered_by_topics` id resolves to a real topic;
EX7 (the પાંચ-છ વાક્ય synthesis question) correctly spans all six POEM topics rather than being
pinned to one. `teacher_note` on EX3 explicitly reiterates the hard sensitivity handling for
કૃષ્ણ/દયાનંદ/દાદા. No personal-opinion or પ્રવૃત્તિ block exists in this chapter's own
`exercise_inventory` to mark as a model answer — વિદ્યાર્થી-પ્રવૃત્તિ was correctly excluded
as apparatus for this specific chapter (01_meta.json's own inventory carries only 3 groups), not
assumed present from the corpus prior.

**F — shape and media.** All 12 `json_contract.md` invariants verified against the merged plan
programmatically: `phase: 2`; `chapter_id` = `gseb_eng_gujarati9_ch3`; `plan_id` =
`gseb_eng_gujarati9_ch3_v1`; every topic has exactly one concept with a resolving `objective_id`
and non-empty `content[]`; the objectives registry is complete and consistent (O1–O7 unique,
every `home_topic_id` and every `anchor[]` entry resolves, `strand_to_objective_map` covers
L1–L7 exactly, single strand `L`); every inline `learning_objectives[]` mirror matches its root
`objective_text` character for character and carries `image_examples: []`; concept ids are
chapter-continuous (`C1`…`C7`, `c` equal to `t` throughout, one concept per topic) verified
against the traversal; recall ids are `{topic}.RQ{n}` with `legacy_id` `{topic}.TR{n}` and **no
`.SR{n}` anywhere**; media ids match `MEDIA_ID_RE`, concept-scoped; `publication_id` non-null
(see Gaps); summaries strictly increase at every topic (checked by word count, all 7 topics);
no digit — Roman or Gujarati — occurs in any `topic_name`, `explanation`, `real_life_example`,
summary, bullet, recall prompt/answer, `objective_text`, `publication_text` or
`publication_chunk` (full sweep, zero hits); `figures_of_speech` entries (3 total, on T4/T5/T6)
quote words verified present in their own topic's `original_chunk`.

`topic_type` is `CONCEPT` (M1.S1.T1) and `POEM` (the other 6) throughout — the correct authored
enum for an Agent-13 intermediate file; the closed server enum
(`instructional`/`summary`/`assessment`) is Agent 14/15's mapping at emit, not this file's.

Bands from `field_shape_rules.md`, all held: `key_terms` 4–5 per topic (band 3–6);
`concept_bullets` and `important_points` 4 each (band 3–4); `recall_questions` 3 per topic (band
2–3), Bloom-laddered remember→understand→analyze/evaluate, the "analyze" items on T3–T6 and the
"evaluate" item on T7 all citing or building on a quoted line; module `difficult_words` 6 (M1) /
8 (M2), both inside 5–10; `estimated_exchanges` small integer strings (`"4"` ×6, `"5"` once, on
T5); `bloom_level` lowercase in recalls and Capitalised in `objectives[]`, the required asymmetry
held. ભાષા-બોધ extras (`shabdarth` 4–6, `samanarthi` 2, `vilom` 0–2, `vyakaran` 2–3 per topic;
`figures_of_speech` 0–2 from the std-9 canon) all sit inside `bhasha_bodh.md`'s std-9 working caps,
and every `shabdarth`/`samanarthi`/`vilom` word was verified present in its own topic's
`original_chunk`.

**G — the seven usual mistakes.** None present. The plan teaches the સ્વરૂપ (ચિત્ર-દર-ચિત્ર
ગૌરવ) rather than સાર+બોધ+પ્રશ્નોત્તર; no કડી merged with another, none split; the changed-words
ટેક is a topic once and the four identical repeats are `depends_on`, not five re-teachings of the
same lines; no તળપદો/કાવ્ય-રૂપ form silently corrected; no અલંકાર named because the field
existed (`M2.S3.T3` honestly carries `[]` for exactly this reason); every `real_life_example` is
single, Indian, inside std-9 reach (ST બસ કન્ડક્ટર, Dubai-working neighbour, ST બસ પ્રવાસ, લહાણીની
વાટકી, બીજા રાજ્યમાં મજૂરી, નવરાત્રિનો ગરબો, શેરી ક્રિકેટ) and never an adult abstraction; સ્વાધ્યાય
was not cut as topics and the exercise deliverable is full (7/7).

## Media

`reuse_report`: scenes 6, authored 6, **reused 0**, rejected none — matching the 6 topics whose
`available_content_types` carry `"image"` (all POEM topics; the CONCEPT pre-reading topic
correctly carries none). Every media node carries `image_url: ""` **and** a real, self-contained
`generation_prompt` naming setting, figures, action, mood and style with no reference to "the
previous image" or the chapter by name. No `[reused frame: …]` stamp and no fabricated URL
anywhere. Every `negative_prompt` carries `Devanagari script labels`. `2d_tool` is `null`
chapter-wide (≤1 satisfied trivially). `M2.S3.T5`'s prompt deliberately draws no named historical
or mythological figure (a young traveller touching the shore before departure) — the teaching_notes
say so explicitly, matching the hard sensitivity item on that topic.

## Gaps

1. **`publication_id` is provisional and must not ship as written.** The contract requires a
   non-null value; `phase2_contract.md` states CBSE's `1` is not portable to GSEB. `1` is written
   here as the placeholder the shape demands, matching this pack's own established convention on
   every prior std-9/std-10 chapter checked (`output9/ch01`, `output10/ch01`, `output10/ch03`).
   **VERIFY-2 must resolve the real GSEB publication row before the first Phase 8 upload.** Not
   an A–D failure of this run; a hard precondition of upload.
2. **`chapter_master_id` is `null`.** Mandatory for upload, not discoverable from the LP2 API,
   fetched per chapter from the education DB (VERIFY-2); never derived by arithmetic.
3. **`textbook` is `null`.** `01_meta.json` and `11_pages.json` both record the std-9 cover as not
   yet read anywhere in this pipeline; the running foot on this chapter's own pages
   (`ગુજરાતી (દ્વિતીય ભાષા), ધોરણ ૯`) is a running foot, not a cover, and is correctly not
   asserted as the `textbook` title. Owner `01_ingestion_genre_diagnosis.md` if a cover render
   becomes available.
4. **`textbook_url` is a local path string** (`../Textbooks-pdf/std-9/ch-03-jyan-jyan-vase-ek-gujarati.pdf`)
   — no hosted URL exists. `textbook_pages` `8–10`, confidence `medium` per `11_pages.json`,
   cross-checked against the std-9 manifest offset (`N+4`) and the printed folios on the renders,
   both agreeing.
5. **`estimated_time` set to `1.5`**, matching this pack's established convention on every prior
   std-9/std-10 chapter, even though `profiles/boards/gseb_gujarati.md` flags `2` as plausible and
   under review for std 9–10. Kept at `1.5` for corpus consistency; not re-decided here.
6. **`topic_title` was derived, not authored** — set to the printed chapter title
   (`જ્યાં જ્યાં વસે એક ગુજરાતી`), matching `chapter_name`, per this pack's established
   convention where there is no separate topic layer above the chapter.
7. **`ordering` is deliberately absent** from `13_merged.json` — Agent 14/15's to set. 31 of the
   contract's 32 root keys are written; `ordering` is the one withheld.
8. **Board and medium segments are PROVISIONAL until VERIFY-1.** `gseb_eng_gujarati9_ch3` uploads
   clean under a wrong medium and mis-files the plan silently if VERIFY-1 turns up a different
   segment — confirm before the first upload.
9. **`publication_chunk` — the same documented conflict between two agent specs noted on prior
   chapters, resolved the same way.** This gate's own spec text says `publication_chunk` is
   "byte-identical to `original_chunk`"; `agents/16_publication_authoring.md` says the field is
   "the publication-facing version of the topic's block **as a whole**," inside which "the
   verbatim `original_chunk` **stays verbatim**." This run followed the producing agent's own
   spec: on all 7 topics `publication_chunk` was verified (not eyeballed) to carry
   `original_chunk` byte-identical as a prefix, followed by publication-facing prose built from
   `explanation`/`real_life_example` with every vocative and direct classroom instruction stripped
   (checked programmatically for `બાળકો`, `જુઓ —`, `બોલો` — zero hits). The verse is never
   rewritten, reflowed or re-punctuated. Not blocked, for the same reason it was not blocked on
   prior chapters — the two specs still need a human reconciliation.
10. **`તણાં`/`કેરી`/archaic-form glosses are recorded as કાવ્ય-રૂપ, never corrected** — matching
    `gujarati_verbatim.md`'s rule and this pack's own established handling on this exact word
    class.
11. **`vyakaran` bindu placement against the std-9 વ્યાકરણ-એકમ sequence** — `M1.S1.T1` names
    `સમાસ` and `M2.S3.T5` names `સંધિ`, both drawn correctly from `bhasha_bodh.md`'s canonical
    bindu list and both demonstrated from this chapter's own text (વિગ્રહ shown for `સમાસ`; the
    vowel-merge shown for `સંધિ`). `bhasha_bodh.md` separately notes these terms are first
    **boxed** in std-9's એકમ 4 (after ch 23) and એકમ 2 (after ch 11) respectively — this is
    chapter 3. Read as descriptive placement of the textbook's own grammar boxes, not as a
    "never use before" gate (no A–D item or contract invariant states the latter), and each entry
    is self-contained enough to teach the point from the chunk without assuming prior in-class
    exposure. Recorded here as a reviewable judgement call, not resolved unilaterally.
12. **Context routing, reported not guessed.** `author.md`, `no_hallucination_policy.md`,
    `global_content_rules.md` and `teaching_voice_gu.md` were read in full per this run's
    instructions, plus `reference/alankar_chhand.md`, `reference/bhasha_bodh.md` and
    `profiles/genres/urmikavya_geet.md` for the craft-naming and grammar-band checks above.
    `qc_checklist.md`, `json_contract.md`, `phase2_contract.md` and `field_shape_rules.md` were
    read in full from the repository. `output9/ch01/13_merged.json` and
    `output9/ch01/validation_report.md` (same standard, already passed) were consulted to confirm
    field shapes and root-key conventions (`topic_title`, `estimated_time`, `publication_id`
    placeholder, module-level `difficult_words`/`overall_rhyme_scheme`, `media[]` retaining
    `topic_id`) this chapter's own inputs left ambiguous; no content from that chapter was copied
    into this chapter's plan.
13. **No page render was re-opened by this agent.** `00_chapter_normalized.md`, `01_meta.json`'s
    `extraction_notes[]` (14 entries, including the ટેક-fusion, the `રહ્યા`/`રમ્યા` conjunct
    correction, and the verse-vs-apparatus wording discrepancy on `M2.S4.T6`) and the chain of
    prior agents' provenance notes answered every question this gate asked.

## LP2 validator

```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati9_ch3_v1",
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

**Result:** PASSED — no validation errors. The LP2 API confirmed the learning plan is valid.
