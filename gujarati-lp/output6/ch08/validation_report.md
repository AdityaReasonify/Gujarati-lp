# Validation Report — std-6 ch 8 મામાનો પત્ર

સ્વરૂપ: patra_pravas — પત્ર (confidence: high)   explanation unit: એક પડાવ
Topics: 6   Objectives: 6   Images: 0/6   Exercises: 14/14 blocks (42/42 items)

Merged plan: `13_merged.json` — 31 root keys, 2 modules, 3 segments, 6 topics, 8 concepts.
Layers folded: `05_with_content.json` (base) · `12_authoring.json` · `09_media.json` ·
`16_publication.json` · `11_pages.json` · `01_meta.json`.

---

## A–D (blocking)   **PASS**

### A — Diagnosis and lens
- સ્વરૂપ diagnosed off the rendered page and recorded with `genre_signals` / `genre_confidence: high`.
  The chapter prints the પત્ર furniture the profile names as the tell: sender block
  (`વિવેક ભારતીય / વિઠ્ઠલનગર સોસાયટી, રાંદેર, સુરત`), `તા. 18-10-22`, `પ્રિય પ્રાચી,` and the closing
  `- વિવેકમામાનાં આશિષ` — the salutation/signature **pair**, not a `લિ.` line.
- Explanation unit matches the સ્વરૂપ: **one પડાવ**, six of them, cut where the letter turns to a new
  matter — never at a paragraph or page break.
- Apparatus did not become a reading scene: `[[પ્રવેશપેટી]]`, `[[શબ્દાર્થ]]`, `[[રૂઢિપ્રયોગ]]`,
  `[[શીર્ષક-પટ્ટી]]`, `[[લેખક-સ્લોટ]]`, both `[[ચિત્ર: …]]` captions and the end-of-unit activity box
  are all outside the topic cut.
- `guiding_question` is derived from this chapter and could fit no other:
  *વિવેકમામા દિવાળીની શુભેચ્છા સાથે પ્રાચીને આ બે ચિત્રકારોની જ વાત કેમ લખે છે ?*

### B — Verbatim and structure
- All six `original_chunk`s non-empty; **every line of every chunk was located in
  `00_chapter_normalized.md` before the first `[[સ્વાધ્યાય:]]` marker** — i.e. all verbatim comes from
  the reading matter, none from the exercise apparatus.
- Script: base script Gujarati (U+0A80–0AFF) throughout. **Zero Roman characters, zero Devanagari
  characters, zero `।`** in any `original_chunk`, and none anywhere in `13_merged.json`.
- `word_count.original` recomputed from each chunk and matches the stated value in all six topics
  (41 / 56 / 125 / 55 / 75 / 12).
- Printed spellings and loans preserved unaltered: `જરુર`, `કાર્ડસ્`, `આર્ટસ્`, `બેંગ`,
  `ગ્રિટિંગ કાર્ડ`, `ટી-શર્ટ`, `પેઇન્ટિંગ`, the run-together `ચિત્રો,શુભેચ્છા`, the space before
  `વાત !` and its absence in `કમાલ!`, and `તા. 18-10-22`.
- Letter furniture is inside the text, not cut out as topics: the sender block, date and `પ્રિય પ્રાચી,`
  open T1's chunk **character for character**; `- વિવેકમામાનાં આશિષ` closes T6's chunk.
- **Marker count balances.** `00_chapter_normalized.md` carries **6** `[[પડાવ: …]]` markers
  (lines 32, 39, 45, 51, 54, 57) and **6** topics carry them in `source_markers`. The seventh
  occurrence, at line 9, is the legend inside the HTML transcription comment — not a marker.
  This chapter prints no `[[કડી …]]` / `[[દુહો …]]` / `[[પદ …]]` / `[[ઘટના: …]]` markers (0 each).
- **No `[[સ્વાધ્યાય: …]]` block became a topic.** All 14 printed blocks stay in
  `10_exercise_solutions.json`. Block 7 (`કૌંસમાં આપેલા શબ્દોનો ઉપયોગ કરીને પત્ર પૂર્ણ કરીને મોટેથી
  વાંચો.`) prints a second complete letter and reads like reading matter — it is correctly held as an
  exercise, which is the trap this chapter sets.
- Ids consecutive and every cross-reference resolves: S1→S3 and T1→T6 run chapter-continuous;
  all four `depends_on` targets resolve.

### C — The teaching block
- Every topic has non-empty `explanation` **and** `real_life_example`.
- Word counts, all inside the 55–90 band (⚠ provisional until VERIFY-4 — measured, not widened):

  | topic | explanation | real_life_example |
  |---|---|---|
  | M1.S1.T1 | 80 | 68 |
  | M1.S1.T2 | 81 | 73 |
  | M2.S2.T3 | 88 | 72 |
  | M2.S2.T4 | 81 | 59 |
  | M2.S3.T5 | 79 | 63 |
  | M2.S3.T6 | 81 | 71 |

  `objective_text` 20–24 words across O1–O6, inside the 12–30 band.
- L2 glossing at point of use is dense and in Gujarati throughout — `કામગીરી`, `કરોડરજ્જુ`,
  `ખબરઅંતર`, `વિશેષતા`, `શિકાર બનવું`, `ખાસિયત`, `પ્રણામ`, `આશિષ` are each glossed where they first
  stand. The letter's **furniture is glossed as content**, which is what this form requires.
- `real_life_example` anchors are Indian, concrete, single, and inside a std-6 child's reach, one
  domain each and no two adjacent alike: own-name envelope · potter's wheel at the street corner ·
  learning to cycle · garba clapping in the ફળિયું · school બાલમેળો stall · relatives leaving at dawn.
- Craft ceiling held: **no અલંકાર, છંદ or સમાસ is named anywhere** — correct for std 6. `ભાંગી પડવું`
  and `નોબત આવવી` are handled by meaning only, exactly as the printed રૂઢિપ્રયોગ box handles them.

### D — સ્વરૂપ essence
- The `patra_pravas` **avoid** list holds on all thirteen gates. Spot-verified mechanically:
  - **gate 2** — salutation and sign-off quoted inside T1/T6 `original_chunk`, neither cut as its own
    topic, neither appearing only in a summary field.
  - **gate 3** — T1's `explanation` names who writes to whom and in what relationship
    (વિવેકમામા of સુરત → his ભાણી પ્રાચી) and accounts for the register that relationship produces
    (`પ્રિય`, second-person `મજામાં હોઈશ`, the closing આશિષ).
  - **gates 4 & 5** — every proper noun in the authored display text was checked against the chapter:
    સુરત, રાજકોટ, ગુજરાત, અમદાવાદ, સી.એન. ફાઈન આર્ટસ્ કૉલેજ are all printed (અમદાવાદ on line 52).
    **No place name, date, year, price, institution or person name was introduced that the chapter
    does not print.** No route, fare, population, statistic or dynastic history anywhere.
  - **gate 6** — no topic carries `topic_category: "climax"` (introduction / transition / core ×3 /
    resolution); no `explanation` or recall `answer` asks or answers why either artist *chose* to act
    as he did, and no field adds a life-fact — no age, no accident cause, no institution name the
    letter withholds.
  - **gate 8** — no tacked-on બોધ. No field closes on `…જોઈએ` / `આપણે પણ…` / `આ પાઠ આપણને શીખવે છે`.
    The મામા's opinion sentences (`આપણા જેવા તો… ભાંગી જાય`, `છે ને ગજબની વાત !`, `છે ને કમાલ!`) are
    attributed to him in every field that carries them.
  - **gate 9 (વિકલાંગતા)** — scanned every authored, publication and media field for
    બિચારા · લાચાર · અપંગ · દયા આવે · નસીબદાર · પ્રેરણા લેવી · છતાં પણ: **zero hits.** The chapter's own
    words (કાબેલ, ખાસિયત, સંકલ્પ) carry the teaching, and `દાન નહિ, વેચાણ` is kept as the point of pride.
  - **gate 12** — `figures_of_speech: []` and `rhyme_scheme: null` on all six topics;
    `overall_rhyme_scheme: null` on both modules. This is a prose letter at std 6: **`[]` is the
    complete and correct answer**, and no device was invented to fill the field. Vacuously, no
    `figures_of_speech[].lines` string fails the verbatim-in-chunk test.
  - **gate 13** — no topic chunk overlaps any inventoried block (verified positionally against
    `00_chapter_normalized.md`); no topic opens on a printed photograph.
- Both `severity: "hard"` sensitivity items (M2.S2.T3 મૃદુલ ઘોષ, M2.S2.T4 મનોજ ભિંગારે) are addressed;
  all 21 hard `avoid_checks` from `07_pitfalls.json` were checked against the fields each one names.
  `08_sensitivity.json`'s `areas[]` use one label, **વિકલાંગતા**, drawn from the seven fixed labels.

---

## E–G (reported)

**E — સ્વાધ્યાય and risk.** All 14 inventoried blocks answered; `blocks_found` (14) equals the
inventory length and matches it entry-for-entry in printed order; `unanswered: []`, `unmapped: []`.
42 items, every one with a non-empty answer, a skill tag and a `covered_by_topics` mapping that
resolves. Personal-opinion, જૂથકાર્ય, રમત and teacher-addressed items (વાતચીત, 'પાસિંગ ધ બોલ',
શ્રુતલેખન) carry model answers with `is_model_answer` and a `teacher_note` — none skipped as
"not answerable". The અનુવાદ block's Roman-script English answers are the whitelisted case: written in
the medium of instruction on purpose and marked as such in `teacher_note`. **Not a script failure.**

**F — Shape and media.** All 12 `json_contract.md` invariants hold:
`phase: 2`; `plan_id` = `{chapter_id}_v1`; `chapter_id` = `gseb_eng_gujarati6_ch8`; six non-empty
Gujarati chunks; every topic ≥1 concept with a resolving `objective_id` and non-empty `content[]`;
objective registry complete and consistent (6 unique ids, all `home_topic_id`s and all 9 `anchor`
concept ids resolve, `strand_to_objective_map` covers L1–L6); **inline `learning_objectives[]` mirrors
match the root registry character for character**, each with `image_examples: []`; media ids match
`MEDIA_ID_RE` concept-scoped; concept numbering chapter-continuous C1…C8 with no restart inside a
topic; topic recalls `{topic_id}.RQ{n}` with `legacy_id` `.TR{n}` — **zero `.SR` ids in the file**;
`publication_id` non-null; summaries strictly increase at every topic (14<38<80, 13<39<73, 13<44<93,
13<39<68, 14<39<79, 16<39<65); and **no digit — Roman or Gujarati — appears in any display field**
(names, explanations, examples, summaries, bullets, points, prompts, answers, key terms, concept
content, objective texts, module and segment names all scanned clean).

`topic_type` is `STORY_TELLING` on all six topics. That is the **authored** enum, which
`phase2_contract.md` §topic_type specifies for intermediate files (Agents 02–13); Agents 14/15 map
`STORY_TELLING → instructional` at emit. Correct at this stage, not a defect.

**G — the seven usual mistakes.** None present. (1) The plan teaches the સ્વરૂપ — letter anatomy,
register, addressee — not સાર+બોધ+પ્રશ્નોત્તર. (2) N/A, no દુહા. (3) N/A, no પદ. (4) No printed form
was silently corrected. (5) No અલંકાર named. (6) Every anchor is std-6-sized and Indian. (7) No
સ્વાધ્યાય block was cut as a topic and the exercise deliverable is complete at 42/42.

---

## Media

`reuse_report`: **scenes 6 · authored 6 · reused 0 · rejected []** — and `available_content_types`
carries `"image"` on exactly 6 topics, so `scenes` equals the reading scenes and `authored` equals
`scenes`. Every node carries `image_url: ""` **and** a substantial self-contained
`generation_prompt` (948–1119 chars); no `[reused frame: …]` stamp and no fabricated URL anywhere.
`negative_prompt` carries `Devanagari script labels` on all six. Each prompt names an exact Gujarati
narrator-bar string in Gujarati script.

**Real named people are not depicted.** The two artist scenes (M2.S2.T3.C5.IMG1, M2.S2.T4.C6.IMG1)
carry an explicit instruction — *"Invent an ordinary anonymous face; do not depict any real,
identifiable person"* — as the profile's Media prior requires where the chapter prints captioned
photographs of real living artists.

**One `2d_tool` in the whole chapter**, on M1.S1.T1: a letter-anatomy drag-and-drop panel built only
from lines this chapter actually prints, with no `લિ.` card because the page prints none. This is one
of the two shapes the profile permits, and it is the letter shape.

---

## Gaps

Honest absences and provisional values, none of them blocking:

1. **`textbook_url` is a local PDF path**, not a hosted URL — the GSEB readers have none. Recorded in
   `11_pages.json.gaps`.
2. **`chapter_master_id` is `null`.** Mandatory for upload, fetched per chapter from the education DB
   (VERIFY-2). Never derived by arithmetic — the Hindi pack's `355 − chapter number` is CBSE
   provenance and does not transfer.
3. **`publication_id` is `1` — provisional and almost certainly wrong for GSEB.**
   `phase2_contract.md` rule 1 says outright that `1` is *CBSE's publication row, not portable*. It is
   written non-null because the server rejects null, and it matches what the rest of output6 shipped,
   but **VERIFY-2 must replace it before the first Phase 8 upload.** A wrong value here uploads clean.
4. **`chapter_id` board/medium segments are provisional until VERIFY-1.** A wrong medium slot does not
   fail loudly — it uploads clean and mis-files the plan under the wrong medium column.
5. **Root `genre` divergence, owner A1 — reported, not blocking.** `01_meta.json` carries the Gujarati
   display name `પત્ર`; `phase2_contract.md` specifies the roster **slug**, so the merged plan carries
   `patra_pravas` (unambiguous from `active_genre_profiles: ["patra_pravas.md"]`). The pack is
   inconsistent about this across std 6 — ch01 and ch07 shipped slugs, ch02/ch03/ch05 shipped Gujarati
   strings. Worth settling pack-wide rather than chapter by chapter.
6. **`ordering` is absent from the root**, by instruction: it is Agent 14/15's to set, not Agent 13's.
   The plan therefore has 31 of the contract's 32 root keys.
7. **Printed order equals logical order.** `05b_textbook_order.json` matches the logical traversal
   item for item. Agent 15 must raise `{"human_confirmation_required": true, …}`. For this form that
   flag is the **correct output, not a defect** — the profile says so explicitly.
8. **Agent 4 note carried forward (reported, not blocking):** the topic name
   `મૃદુલ ઘોષ — હવાઈ-દળથી પીંછી સુધી` has an "from X to Y" arc shape, and `પીંછી` is not in the
   letter's prose. `પીંછી` *is* on the page — in the printed photograph and in exercise block 3
   (`મને સારી પીંછી લઈ આપો`) — so it is not invented. Gate 6's check clause names `topic_category`,
   `explanation` and recall `answer`, all of which pass; `topic_name` is outside it. Reported only.
9. **Cut divergence from the profile prior, openly recorded.** `patra_pravas.md` reads this same unit
   as **four** પડાવ (શુભેચ્છા · મૃદુલ · મનોજ · મંડળ). Agent 1 read **six** off the rendered page and
   Agent 2 cut six. The two extra turns are genuine — the letter first turns toward the artists at
   `આ વર્ષે તને લખેલું શુભેચ્છા પાઠવતું કાર્ડ…` and turns home again at
   `તારાં મમ્મી અને પપ્પા મજામાં હશે.`. The page wins over the prior; the prior is evidence, not a
   verdict. Recorded in `02_structure.json` and `04_validation.json`.
10. **Agent 4's earlier snapshot superseded.** A 23:00 pair of `04_*` files described an older,
    differently numbered cut (3 modules / 5 segments). Both were rewritten at 23:14 against the
    23:02 `02_structure.json`. Ids are frozen from that point; nothing in this merge references the
    stale numbering.
11. **The unnumbered end-of-unit activity** (`પગમાં કે મોંમાં પેન્સિલ પકડી તમારું મનપસંદ ચિત્ર દોરવાનો
    પ્રયત્ન કરો.`) is printed outside the numbered list, is therefore absent from
    `exercise_inventory`, and is correctly absent from `10_exercise_solutions.json`. It is covered by
    `08_sensitivity.json`'s chapter-level guidance.
12. **Spec-vs-spec discrepancy resolved in favour of the owning agent, stated openly.**
    `agents/13_assembly_validation.md` §Publication says `publication_chunk` is *"byte-identical to
    `original_chunk`"*. `agents/16_publication_authoring.md` §`publication_chunk` — the agent that
    owns the field — says it is the publication-facing version of the topic's block **as a whole**,
    with the verbatim `original_chunk` staying verbatim *inside* it. I applied the owner's reading and
    verified the stronger thing that reading demands: **`original_chunk` is a byte-identical prefix of
    `publication_chunk` in all six topics**, followed by the rewritten teaching prose and the anchor.
    Under Agent 13's literal wording every topic would fail; under Agent 16's, every topic passes and
    the verbatim is provably untouched. One of the two spec files should be corrected.
13. **Concurrency observation.** `13_merged.json` appeared in this directory at 01:46, mid-session,
    without a companion `validation_report.md` — most likely a concurrent or aborted Agent-13 pass.
    I regenerated the merge independently from the source layers and the result is **semantically
    identical** to that file, so nothing was lost; the file now on disk is the one this run produced.

## LP2 validator

Result (Phase 8 run): `POST /api/lp2/learning-plans/validate` was called against
`learning_plan_logical.json`, succeeded on the first attempt (no retry needed), and returned
zero `validation_errors`.

- Endpoint: https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- HTTP status: 200
- validation_errors: [] (empty — PASS)
- message: Valid
- plan_id: gseb_eng_gujarati6_ch8_v1
- Raw response: `{"success":true,"action":"validated_only","plan_id":"gseb_eng_gujarati6_ch8_v1","version":null,"phase":null,"is_active":null,"is_draft":null,"counts":null,"diff":null,"publication_id":null,"publication_name":null,"validation_errors":[],"message":"Valid"}`

Note: VERIFY-1 (`chapter_id` board/medium) and VERIFY-2 (`chapter_master_id`, `publication_id`)
noted elsewhere in this report are validator-blind (the fields above are all `null` in the
response) — the schema validator passing does not close those two verification items, and
gaps 2–4 elsewhere in this report remain unresolved regardless of this PASS.

---

**Verdict: A–D PASS.** No blocking item. The run is complete at this gate and may proceed to
Agent 14. Items 1–13 under Gaps are reported, not blocking, and none of them is presented as resolved.

## LP2 validator

- POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate → validation_errors: [] (none) — PASS
- Run: 2026-08-23 17:16 IST (validation only; no upload)
