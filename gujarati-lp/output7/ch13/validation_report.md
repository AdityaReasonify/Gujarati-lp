# Validation Report — std 7, ch 13 · ટૅક્સીને ફૂટી પાંખો !
સ્વરૂપ: varta — વિજ્ઞાન-કલ્પનકથા sub-form (confidence: high)   explanation unit: એક ઘટના
Topics: 10   Objectives: 10   Images: 0/10   Exercises: 67/67 (13/13 printed blocks)

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` + `16_publication.json`
+ `11_pages.json` + `01_meta.json` into `13_merged.json` — 31 root keys, 37 topic keys
(the 31 contract keys plus `figures_of_speech`, `rhyme_scheme` and the four ભાષા-બોધ extras
`shabdarth` / `samanarthi` / `vilom` / `vyakaran`, romanized as the server stores them).
`ordering` is left unset — Agent 14/15 owns it. No working field, score, marker or transcription
note survived the merge (verified by a key walk over the whole tree).

## A–D (blocking)   **PASS**

**A — diagnosis and lens.** `genre_signals` (structure / theme / exercises / purpose) and
`genre_confidence: "high"` are recorded off the render in `01_meta.json`; the blue પ્રવેશપેટી is
quoted as evidence and explicitly not treated as the verdict ("પેટી 'કલ્પના' કહે છે, સ્વરૂપનું નામ
આપતી નથી"). The explanation unit **એક ઘટના** matches varta.md's roster line, and the ten topics sit
1:1 on the ten printed `[[ઘટના: …]]` markers, in printed order. Apparatus stayed apparatus: the
પ્રવેશપેટી, the શબ્દાર્થ box and the રૂઢિપ્રયોગ box are cut as non-topics in
`05_with_content.json:not_cut_as_topics`. No ટેક exists (prose chapter, `tek_occurrences: 0`).
`guiding_question` is derived from this chapter alone and the ten explanations in order do answer
it — the answer arrives at M3.S6.T10, where the daughter's foresight, not a machine, resolves the
problem.

**B — verbatim and structure.** All ten `original_chunk` values are non-empty and were checked
character-for-character against `00_chapter_normalized.md`: each is an exact substring of the
transcription once the `[[…]]` structural markers are removed (M2.S4.T6 spans the `[[પૃષ્ઠ 88]]`
page break, which is the only reason a naive substring test misses it). Script check clean:
Gujarati U+0A80–0AFF base throughout, **no Devanagari and no Roman anywhere** in
`topic_name` / `explanation` / `real_life_example` / summaries / bullets / `key_terms` / recall
prompts and answers / concept content / `objective_text` / `guiding_question` / `publication_text`.
No `।` anywhere. Marker arithmetic: 10 `[[ઘટના: …]]` = 10 topics; 0 `[[કડી]]` / `[[દુહો]]` /
`[[પદ]]` (correct — this unit is prose); **13 `[[સ્વાધ્યાય: …]]` blocks and not one of them became
a topic** — no inventoried heading appears inside any `original_chunk`. Ids run consecutively and
every cross-reference resolves.

**C — the teaching block.** Every topic carries a non-empty `explanation` **and**
`real_life_example`. Word counts, all inside the 55–90 band with nothing trimmed at this gate:

| topic | explanation | real_life_example | brief/summary/detailed |
|---|---|---|---|
| M1.S1.T1 | 88 | 68 | 16 / 50 / 99 |
| M1.S2.T2 | 90 | 68 | 21 / 43 / 126 |
| M1.S2.T3 | 88 | 70 | 20 / 52 / 111 |
| M1.S3.T4 | 86 | 68 | 20 / 48 / 87 |
| M2.S4.T5 | 87 | 69 | 21 / 55 / 107 |
| M2.S4.T6 | 90 | 72 | 20 / 54 / 133 |
| M2.S5.T7 | 87 | 73 | 16 / 43 / 97 |
| M2.S5.T8 | 79 | 66 | 16 / 60 / 112 |
| M3.S6.T9 | 84 | 65 | 20 / 50 / 122 |
| M3.S6.T10 | 82 | 67 | 23 / 58 / 128 |

`objective_text` runs 18–27 words across O1–O10, inside the 12–30 band. Summaries increase
strictly at every topic. Anchors are Indian, single and inside std-7 reach — the ten-domain ledger
(ઘરની સવાર · શાળા-રિસેસ · કરિયાણાની દુકાન · ઉત્તરાયણની આગલી સાંજ · વર્ગમાં ભાઈબંધ · શેરીની સાયકલ ·
ફળિયાની ભેંસ · ગિરનારનાં પગથિયાં · દાદીનું 'અમારા વખતે' · પ્રવાસનો ડબ્બો) repeats no domain
back-to-back. Craft is named at the std-7 bar: `figures_of_speech` is `[]` on every topic and the
સજીવારોપણ-shaped touches (the arguing ડાયરી, the crying ઓટો બ્રશ) are taught unlabelled inside
`explanation`, which is the std-7 label gate, not an omission. ⚠ The 55–90 / 12–30 bands remain
provisional until VERIFY-4; they were enforced as written and no band was widened.

**D — સ્વરૂપ essence.** All **17 `severity: "hard"` items** in `07_pitfalls.json` plus the single
chapter-level item in `08_sensitivity.json` were tested against the fields each check names:

- *Summary-only teaching* (7 topics) — no `explanation` equals its `modified_chunk`, and each of
  the seven names the beat's motive/craft/consequence the check demands (the ફ્લેશ↔તડકો link at
  T1; the one news item that starts the અશાંતિ at T2; the two-things-in-one-morning squeeze at T4;
  the face read rather than the fear spoken at T5; both stated motives plus the ડૂબતા માણસને
  તણખલાનો સહારો line at T6; the voice-recognition rule at T7; the man changing rather than the
  spec sheet at T8).
- *A tacked-on બોધ* (T1, T9, T10) — a full-text scan for `આ વાર્તા આપણને શીખવે છે`, `બોધ એ છે`,
  `આપણે પણ …` and any prescriptive `… જોઈએ` clause across every `explanation`, summary,
  `concept_bullets`, `important_points`, concept content and recall answer returns **no moral
  clause**. The ten `જોઈએ` occurrences are all the ordinary verb "is needed" inside quoted or
  reported content (`ટ્રાફિકની ખલેલ વગર … ઍરટૅક્સી જ જોઈએ`, `કમ્પ્યૂટર જોઈએ, પ્રોજેક્ટર જોઈએ`) —
  not a rule addressed to the child. The ending quotes the chapter's own last words rather than
  re-authoring their meaning.
- *Judging a sympathetic character* (T3, T6, T10) — no evaluative label (આળસુ, બેદરકાર,
  બેજવાબદાર, ડરપોક, બીકણ, જૂનવાણી, પછાત, મૂરખ, ઉદ્ધત, અસભ્ય, તોછડી) appears in any topic field.
- *Spoiling the turn early* (T3, T5, T9, and the chapter-wide gate at T10) — none of
  M1.S1.T1 … M3.S6.T9 carries પાછળની સીટ / બોક્સ / 'ગઈ કાલે જ' / 'કાલે સાંજે જ' / શ્રીમતીજી /
  હિમાલય / વહાલુડી / બેવડી ખુશી. `ભુલકણ`, `ભૂલી જવાની ટેવ` and `વિસ્મરણશીલ` appear only at
  M3.S6.T9 (the chapter's own ઝબકારો) and M3.S6.T10 (સ્નેહાનું પોતાનું વાક્ય), never at M1.S2.T3
  and never as a verdict.
- *Sensitivity — જાતિ-ભૂમિકા* — `08_sensitivity.json`'s area string is one of the seven fixed
  labels. Sneha is taught throughout as the one who reads the face, proposes and defends the
  ઍરટૅક્સી, gives the voice commands, flies the trip and had already fetched the system; Nishchal
  as the one who needed that help. No girls-vs-boys lesson was added, because the chapter states
  none.
- *Invented અલંકાર* — `figures_of_speech` is `[]` on all ten topics, so the verbatim-lines check
  has nothing to fail on and nothing was named that is not in the lines.

**Contract (the 12 invariants).** `phase: 2`; `plan_id` = `{chapter_id}_v{version}`; `chapter_id` =
`gseb_eng_gujarati7_ch13`. Every topic has ≥1 concept with a resolving `objective_id` and non-empty
`content[]`. O1–O10 unique; every `home_topic_id` and every `anchor[]` id resolves;
`strand_to_objective_map` covers L1–L10 exactly once; every topic's `objective_ids` resolve.
Inline `learning_objectives[]` mirrors match the root `objective_text` **character for character**
and each carries `image_examples: []`. Ids match traversal position at every level — M1/M2/M3,
S1…S6, T1…T10, and concepts **chapter-continuous** M1.S1.T1.C1 … M3.S6.T10.C10. Media ids match
`MEDIA_ID_RE` and are concept-scoped. Recalls are `{topic_id}.RQ{n}` with `legacy_id`
`{topic_id}.TR{n}`; a regex sweep of the whole plan finds **no `.SR{n}`**. `bloom_level` is
lowercase in recalls and capitalised in `objectives[]`. `topic_type` is the authored enum
`STORY_TELLING` on all ten, which Agent 14/15 maps to `instructional` at emit. Summaries increase
strictly. No digit — Latin or Gujarati — appears in any authored display field, media title,
description or teaching note; numerals survive only in ids, `word_count`, `textbook_pages` and
`prompt_verbatim`, which are provenance. **One invariant is not satisfiable here:
`publication_id` is `null`** — see Gaps.

**Exercises.** `coverage_report.blocks_found` has 13 entries, exactly the 13 headings in
`01_meta.json`'s `exercise_inventory`, in printed order; `blocks_answered` covers all 13;
`unanswered` is `[]`; all 67 items carry a non-empty answer, a skill tag and a
`prompt_verbatim`. 28 items are marked `is_model_answer` (વાતચીત, ચિત્રવર્ણન, લેખન, the ગૃહકાર્ય
bill block, the જોડીકાર્ય grid and the અનુવાદ paragraph), as personal-opinion and પ્રવૃત્તિ items
must be. **Publication/Verbatim.** Every topic has a `publication_text`; every topic's
`original_chunk` sits **verbatim, byte-for-byte, inside its `publication_chunk`** (the rewrite
touched only the surrounding prose, per `agents/16_publication_authoring.md`); the vocative
`બાળકો` and the classroom instructions (`જુઓ —`, `વિચારો,`) are gone from every
`publication_text`, every publication-facing anchor and every concept `publication_text`; all 20
`paragraph` blocks across the ten concepts carry a `publication_text` matched by index, none
renumbered, reordered or dropped (`list` blocks correctly carry none, as the contract's own
example shows). `16_publication.json`'s note ledger accounts for every removal and shows no
meaning added.

## E–G (reported)

- **E** — all 13 printed blocks answered and skill-tagged; the empty printed grid (block 8,
  જોડીકાર્ય) is filled with teaching values; the ગૃહકાર્ય bill block is answered as a model
  answer rather than skipped. **39 of the 67 items are reported `unmapped`**, across five blocks
  (લાઈટ બિલ, સમાનાર્થી-તારવો, ખાલી જગ્યા-કાળ, નર/નારી જાતિ, વાક્યગમ્મત) — every one of these
  batteries is built on sentences and word-pairs from **outside** this chapter, so no reading
  scene prepares them. Reported as unmapped and **not** closed with an invented mapping. That is
  the correct outcome, not a coverage hole.
- **F** — one image per reading scene, no `2d_tool` in the chapter, `negative_prompt` carries
  `Devanagari script labels` on all ten nodes, summaries increase, no digits in display text.
  `publication_id` is null (below); `chapter_id`/`plan_id` carry the provisional `gseb` / `eng`
  segments pending VERIFY-1 — a wrong medium segment uploads clean and mis-files the plan, so this
  stays an open pre-upload item, not a silent pass. `ordering` is deliberately unset for Agent 14/15.
- **G** — none of the seven habitual mistakes is present: the teaching is not સાર+બોધ+પ્રશ્નોત્તર
  (each explanation adds motive or craft); no verse-merging or verse-splitting applies (prose);
  no licence was silently corrected (see the PRINTED-AS-IS ledger below); no અલંકાર was named to
  fill a field; no anchor is adult-pitched or set outside India; no સ્વાધ્યાય block was cut as a
  teaching topic.
- **Agent 4's non-blocking notes**, carried here as they asked: (i) there is no pre-reading opener
  topic, because std 7 prints no student-facing કવિ/લેખક-પરિચય and the blue પ્રવેશપેટી is
  teacher apparatus — an absence, correctly, rather than an omission; (ii) no topic carries
  `topic_category: "resolution"` — the printed final `[[ઘટના]]` marker binds the reveal, the
  father's 'વાહ, મારી વહાલુડી દીકરી!' and the closing sentence into one block, so M3.S6.T10 is
  marked `climax` and carries both the વળાંક and the પરિણામ; splitting it would have invented an
  eleventh topic where no marker sits; (iii) topic lengths are markedly uneven (M1.S2.T2 is 218
  words of `original_chunk`, M1.S3.T4 is 46) — that follows the printed ઘટના blocks and reads as
  fidelity, not sloppiness; (iv) six of ten topics are `topic_category: "core"`, accurate to a
  story whose middle is a continuous chain of beats.

## Media
`reuse_report`: **scenes 10 · authored 10 · reused 0 · rejected []**. All ten topics carry
`available_content_types: ["image"]` and exactly one image each, so scenes matches the reading
scenes exactly. Every node carries `image_url: ""` **and** a real, self-contained
`generation_prompt` (1 177–1 668 chars) — no Gujarati frame pool exists, so reuse is dormant and
no `[reused frame: …]` stamp appears anywhere. No fabricated URL. `negative_prompt` carries
`Devanagari script labels` on all ten. `2d_tool` is `null` chapter-wide: nothing in this story is a
staged process or an operable route. Two craft points worth recording: character likeness is held
by repeating the same appearance sentence verbatim in each prompt rather than by referring back to
an earlier frame (which an image model cannot see), and the spoiler gate is enforced *in the art* —
the carton is physically in the cabin from M2.S5.T7 onward, so T7/T8/T9 frame out the rear bench
and additionally carry "any box, carton or parcel visible in the cabin" in `negative_prompt`; it is
revealed only in M3.S6.T10.C10.IMG1.

## Gaps
1. **`publication_id` is `null`.** `json_contract.md` §F and the LP2 validator both require it
   non-null, and CBSE's `1` is **not portable** to GSEB (`phase2_contract.md` rule 1). No GSEB
   publication row has been fetched, so the honest value is `null` and the invariant is blocked on
   **VERIFY-2**, not on any authoring agent. Writing a borrowed row here would be a fabricated id,
   not a fix. **This must be filled before the first Phase-8 upload.** Same for
   `chapter_master_id` (`null`; fetched from the education DB, never derived — the Hindi pack's
   `355 − chapter number` arithmetic is CBSE provenance). `subject_ref_id` and `medium_id` stay
   `null` by design; the server owns them.
2. **`chapter_id` / `plan_id` board and medium segments are unverified (VERIFY-1).**
   `gseb_eng_gujarati7_ch13` / `…_v1`. A wrong medium slot uploads clean and mis-files the plan —
   confirm against the live server before upload.
3. **No hosted `textbook_url`.** The value is the local path
   `../Textbooks-pdf/std-7/ch-13-taxine-futi-pankho.pdf`; the GSEB readers have no hosted URL.
   `11_pages.json` records this as its one gap. `textbook_pages` `85–92` is **high** confidence —
   folio boxes read off the render on pages 1 and 8, cross-checked against the std-7 manifest and
   the N+13 offset.
4. **PRINTED-AS-IS ledger — do not "fix" these downstream.** `શ્રી - ડી પ્રિન્ટર` (printed page 86,
   almost certainly meant as થ્રી-ડી, but the page prints શ્રી and the page is the authority);
   `જવાળામુખીના` without the જ્વ conjunct; `ફલેશ` and `ફ્લેશ` four words apart in the same
   paragraph; `ઍર ટૅક્સી` broken across a line end on page 88 beside `ઍરટૅક્સી` elsewhere; the
   spaced/solid pairs `ડેશ બોર્ડ`/`ડેશબોર્ડ` and `સ્માર્ટ બોર્ડ`/`સ્માર્ટબોર્ડ`;
   `ઍરટૅક્સી માંથી` with a space in the closing sentence; `રાજા રાજય` in exercise block 10;
   inconsistent spacing before terminal `?` and `!`. All transcribed as printed and taught as
   printed; the variant pairs are named once inside the teaching so a child does not read them as
   errors.
5. **Whitelisted non-Gujarati script — one instance, and it is intended.** EX67's answer (the
   standing `ફકરાનો તમારી પ્રથમ ભાષામાં અનુવાદ કરો :` block) is written in Roman English, because
   the block asks for the child's પ્રથમ ભાષા and `chapter_id` records English as the medium of
   instruction. It is marked as a model answer and flagged in its own `teacher_note`. A script
   failure raised against it would be a false positive. No other Roman or Devanagari appears
   anywhere in the pack outside bracketed technical terms.
6. **`00_chapter_normalized.md` was the sole source read for this gate.** No PNG render was
   opened: nothing in these checks turned on a layout or figure question the transcription could
   not answer — the one layout-sensitive item, M2.S4.T6's page-break span, is fully recorded by
   the transcription's own `[[પૃષ્ઠ 88]]` marker.

## LP2 validator
Not run — filled in Phase 8. It cannot pass until Gap 1 is closed: `publication_id: null` is
exactly the error the server raised on the first real Hindi run.

## Verdict
**A–D PASS.** No blocking failure, no owner to route to, nothing repaired at this gate. The four
items in Gaps 1–3 are open **verification** items owned upstream of upload (VERIFY-1 / VERIFY-2 /
VERIFY-4), not authoring defects — and none of them can be closed by inventing a value.

## LP2 validator

- Endpoint: https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- Result: FAILED (validation_errors present)
- validation_errors:
  - "root: 'publication_id' is required and must not be null"

