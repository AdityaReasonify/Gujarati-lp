# Validation Report — std 6, ch 10 · સાથી મારે બાર (રમણલાલ સોની)
સ્વરૂપ: kathakavya — કથાકાવ્ય / કથાગીત (confidence: high)   explanation unit: એક વાર્તા-પગલું (ઘટના), boundary always at a printed કડી (પ્રાસ-જોડ) end
Topics: 12   Objectives: 12   Images: 0/12   Exercises: 13/13

**VERDICT: PASS.** Sections A–D pass with zero blocking items. This is the second Agent-13 pass on
this chapter: the first (superseded, kept at `_invalid/`) blocked because `16_publication.json` had
never been written. Agent 16 has since run, the publication layer is complete on all 12 topics and
all 24 concept content blocks, and the block is cleared. `13_merged.json` is rewritten from the
current layers.

Two things are **reported and must be read before this ships** (neither is an A–D failure): the
publication-chunk convention note under **Publication**, and the stale Agent-14/15 deliverables under
**Gaps** item 1.

---

## A–D (blocking)   PASS

### A — Diagnosis and lens   PASS
- સ્વરૂપ diagnosed off the rendered page with `genre_signals` (structure / theme / exercises) and
  `genre_confidence: high`. The book names the form itself twice and never settles on one label —
  the blue intro box prints "આ કથાકાવ્યની બાળકો પાસે નાટ્યાત્મક રજૂઆત કરાવવી." and સ્વાધ્યાય blocks
  2 and 13 print "આ એક કથાગીત છે…" / "આ કથાગીતનું ગાન વર્ગમાં કરો." — quoted as evidence, not as the
  verdict; `01_meta.json` records both and picks no winner, as `kathakavya.md` instructs.
- Explanation unit matches the roster line for કથાકાવ્ય: **one વાર્તા-પગલું cut at a printed કડી
  boundary**. Measured this run: 12 `[[ઘટના: …]]` markers → 12 instructional topics, one-to-one; 15
  `[[કડી n]]` markers, each carried whole by exactly one topic (mechanically confirmed, zero splits,
  zero double-carries); 12 < 15, so `kathakavya.md` hard gates 1 and 2 both hold.
- ટેક: **zero** — a measured fact, not an empty box. No line recurs and no refrain shorthand is
  printed; that absence is what pushes the diagnosis off the ગીત branch.
- Not a mixed chapter. Apparatus did not become a reading scene: the blue પ્રવેશક-પેટી, the green
  શબ્દાર્થ box, the • રૂઢિપ્રયોગ pre-block and the chapter-final ઉખાણા-પેટી carry no topic.
- `guiding_question` is derived from this poem — "એકલો ધૂળો ચાર ચોર સામે કઈ રીતે ટકી ગયો, અને એના
  'બાર સાથી' ખરેખર કોણ નીકળ્યા ?" — and reading the twelve explanations in printed order answers it.
- `topic_category` runs introduction → core → … → climax (M3.S5.T9) → resolution (M3.S6.T12), free
  text per the contract.

### B — Verbatim and structure   PASS
- 12/12 topics carry a non-empty `original_chunk`; **every line of every chunk matched a line of
  `00_chapter_normalized.md` character for character** (mechanical check, zero misses).
- Script: Gujarati (U+0A80–0AFF) throughout. **Zero** Roman and **zero** Devanagari characters in any
  `original_chunk`, and zero in any authored display text outside brackets. No `।` anywhere.
- Printed poetic licence intact and unmodernised: `ચડિયો`, `અલ્યા`, `કાંક`, `નહિ`, `વારતા`, `દશ`,
  `પાય`, `બી ગયા`, `સબોસબ`, `ધબોધબ`, `આઘુંપાછું`, and the apostrophe-elision `જાવું'તું`. A sweep
  for the માનક replacements (ચડ્યો, અરે, કંઈક, નહીં, જવું હતું) inside quoted spans returned seven
  hits and **all seven are glosses, not repairs** — the printed form is the headword and the standard
  form is the meaning given beside it (`ચડિયો — 'ચડ્યો'; ગાનારો આમ બોલે છે, એ ભૂલ નથી.`), which is
  what avoid-gate 11 asks for. M3.S5.T10's recall answer explains the `જાવું'તું` elision outright
  and states it is not a misprint.
- Two-column p. 63 read **down each column**; the પ્રાસ pair સાથ/હાથ that breaks across the
  p. 63 → p. 64 boundary is held whole inside M3.S5.T9 — no કડી split at the page break.
- Attribution `- રમણલાલ સોની` sits inside the **last** topic's `original_chunk` (M3.S6.T12).
- Marker accounting: કડી 15 · ઘટના 12 · સ્વાધ્યાય 13 · topics 12. **No `[[સ્વાધ્યાય: …]]` block
  became a topic** (all 13 live in `10_exercise_solutions.json` alone).
- Header furniture kept out: the pink `10` number box, the QR badge and its Latin code string, and
  the running folios are absent from every chunk.
- Ids match traversal position exactly (M1.S1.T1 → M3.S6.T12); concept numbers chapter-continuous
  C1…C12.

### C — The teaching block   PASS
- 12/12 topics carry a non-empty `explanation` **and** `real_life_example`.
- Every band holds with no trimming needed: `explanation` **68–78** words, `real_life_example`
  **61–71** words (band 55–90); `objective_text` **15–23** words (band 12–30). Bands applied as
  written — ⚠ provisional until VERIFY-4, and not widened.
- Three-tier summaries strictly increase on all 12 topics (chapter ranges 11–18 / 23–41 / 53–81
  words).
- L2 calibration held: ordinary-but-hesitable words are glossed at the point of use — `વાણિયો`,
  `સમી સાંજ`, `ઉચાટ`, `વીંઝે`, `સબોસબ`, `ખાળે`, `પાય`, `વારતા`, `નાઠા` — in Gujarati, in the
  chapter's own શબ્દાર્થ / રૂઢિપ્રયોગ wording, with no Hindi word standing in for a Gujarati one.
- `real_life_example` is Indian, single and inside std-6 reach throughout — ઘર, શેરી, દીવાબત્તીનું
  ટાણું, નવરાત્રિનો રાસ, વર્ગખંડ. No adult framing, no abstraction, no three-examples-in-one.
- Craft is at the std-6 ceiling: પ્રાસ is **heard**, never named as a device. Zero અલંકાર labels and
  zero છંદ labels anywhere. No explanation opens its first sentence on craft terminology, and no
  topic carries more than one craft sentence (both checked mechanically; zero hits).
- No digit — Latin or Gujarati — appears in any name, explanation, example, summary, bullet, key
  term, concept text, recall prompt or recall answer.

### D — સ્વરૂપ essence   PASS
- `kathakavya.md`'s fourteen **avoid** items checked item by item; no violation found. The
  structural gates 1–3 re-confirmed here from the merged file rather than inherited from Agent 4.
- **Gate 7 / contract 11:** `figures_of_speech` is `[]` on all 12 topics — the honest answer for this
  ballad at std 6, and the one `no_hallucination_policy.md` §3 asks for. Nothing to verify verbatim
  because nothing was claimed. Every `rhyme_scheme.rhyming_words` pair is two words printed in this
  chapter (નામ—ગામ, વાટ—ઉચાટ, વિચાર—બાર, ચાર—વાર, એક—વિવેક, માલ—વિકરાળ, સબોસબ—ધબોધબ, ઘાવ—દાવ,
  જંગ—રંગ, જોર—ઘોર, સાથ—હાથ, ગામ—કામ, તમામ—નામ, પાય—થાય, વિશ્વાસ—ખાસ) — mechanically confirmed
  against `00_chapter_normalized.md`.
- **Gate 5:** no tacked-on બોધ — zero occurrences of "આ કાવ્ય આપણને શીખવે", "બોધ એ છે કે",
  "આપણે પણ" in any explanation, summary, bullet, important point or recall answer.
- **Gate 9:** the turn is not spoiled early. The closing tally's words (`કાટલાં`, `દશ થાય`,
  `હિંમત અને વિશ્વાસ`, `બે હાથ`, `બે પાય`) appear in no topic before the reveal, in no summary and in
  no recall answer. Two apparent hits at M1.S2.T3 are the opposite of a spoiler — they say in so many
  words that who the બાર સાથી are **has not yet been told** ("એ બાર સાથી કોણ છે તે આ ઘડીએ કાવ્યમાં
  કહેવાયું નથી").
- **Gate 10:** every speaker named in an explanation, summary or recall answer is ધૂળો, ચોરો or a
  pronoun — all printed in this or an earlier chunk. No speaker invented.
- **Gate 12/32:** no ગ્રામ / કિલો value is stated for the ચાર કાટલાં anywhere.
- **Chapter-level pitfalls:** the intro box's own words (`વણિક`, `ઝઝૂમી`, `બુદ્ધિપૂર્વક`) appear in
  no field — zero hits. `રોકાણ`, printed in the શબ્દાર્થ box but in no line of the poem, is quoted
  as a poem word nowhere — zero hits. The term `કાવ્યસ્વાતંત્ર્ય` (above std-6 reach) is used
  nowhere — zero hits.
- **Community dignity:** `વાણિયો` is glossed as ધૂળાનું કામ (વેપાર કરનાર) and never as a caste label;
  zero occurrences of `વાણિયાઓ`, `વેપારીઓ`, `કંજૂસ`, `બીકણ`, `હિસાબી` in any field.
- **Hard pitfalls / sensitivity:** 32 hard `avoid_checks` from `07_pitfalls.json` across the 12
  topics — none left unaddressed. The one **hard** item in `08_sensitivity.json` (M2.S4.T7 —
  સુરક્ષા + સંઘર્ષ) is addressed in both places it had to be: the explanation stays on ધૂળાની ચતુરાઈ
  and on `ખાળે ઘાવ` rather than on the blows, and the EX12 નાટ્યીકરણ answer prints the mime
  instruction outright — "કોથળો હાથમાં લેવાનો નથી — માત્ર હાથનો હલનચલન". All `areas[]` values
  (સમુદાય, સુરક્ષા, સંઘર્ષ) are inside the seven fixed labels.

---

## E–G (reported)

**E — સ્વાધ્યાય and risk.** All 13 inventoried blocks answered, skill-tagged and mapped:
`coverage_report.blocks_found` = 13 = `01_meta.json` inventory length, `unanswered` = `[]`,
`unmapped` = `[]`, and every `covered_by_topics` id resolves to a real topic (zero unresolved). The
13 headings match the inventory one-for-one in printed order. The seven personal-opinion / પ્રવૃત્તિ
/ teacher-addressed blocks (વાતચીત, વાર્તાલેખન, પ્રાસ-જાળી, શબ્દો-આપીને-વાર્તા, અનુવાદ, નાટ્યીકરણ,
સમૂહગાન) carry `is_model_answer: true` and are labelled as one possible response in the answer text
itself. The printed પ્રાસ grid and the ખરું-ખોટું table are filled with teaching values. The
chapter-level સુરક્ષા note reaches both activity blocks (EX12, EX13).

**F — Shape and media.** All 12 `json_contract.md` invariants hold, re-run from scratch on the new
merge: `phase: 2`; `chapter_id: gseb_eng_gujarati6_ch10`, `plan_id: …_v1`; 12/12 topics with a
non-empty Gujarati `original_chunk`; 12/12 topics with ≥1 concept, each with non-empty `content[]`
and a resolving `objective_id`; 12 unique objectives, every `home_topic_id` and every `anchor[]` id
resolving, `strand_to_objective_map` covering all twelve `legacy_id`s; inline `learning_objectives[]`
`objective_text` identical to the registry character for character on all 12 topics; 12 media ids
concept-scoped and matching `MEDIA_ID_RE`; 36 recalls, all `.RQ{n}` with `legacy_id` `.TR{n}` and
lowercase `bloom_level` — **no `.SR` anywhere**; registry `bloom_level` Capitalised; `publication_id`
non-null; summaries strictly increasing; no digits in display text. Root keys are exactly the 32 of
the contract minus `ordering`, which is deliberately left to Agents 14/15. Topic keys are exactly the
contract's 31 plus the કાવ્ય extras `figures_of_speech` / `rhyme_scheme` and the four romanized
ભાષા-બોધ extras (`shabdarth`, `samanarthi`, `vilom`, `vyakaran`); module level carries
`difficult_words` (7 / 8 / 8) and `overall_rhyme_scheme`. A sweep for working fields (pitfall notes,
media scores, validation flags, transcription notes) found **none** carried into `13_merged.json`.
`topic_type` is the authored enum `POEM` on all 12, correct for an intermediate file — Agents 14/15
map it to `instructional` at emit. ⚠ `chapter_id`'s board/medium segments remain provisional until
VERIFY-1.

**G — the seven usual mistakes.** None present. Not a સાર+બોધ+પ્રશ્નોત્તર plan; no couplets merged
or fused; nothing split line by line and no ટેક lifted out (there is no ટેક); no poetic licence
silently corrected; no અલંકાર named to fill a field; no adult or non-Indian `real_life_example`; no
સ્વાધ્યાય cut as a topic — the exercise deliverable is complete at 13/13.

---

## Media
`reuse_report`: **scenes 12 · authored 12 · reused 0 · rejected []** — and exactly 12 topics carry
`"image"` in `available_content_types`, so `scenes` matches the reading scenes. Every one of the 12
media nodes carries `image_url: ""` **and** a non-empty, self-contained `generation_prompt`; no
`[reused frame: …]` stamp appears anywhere and no fabricated URL. `reused: 0` is correct — no
Gujarati frame pool exists, so `Images` reads **0/12**. Every `negative_prompt` carries
`Devanagari script labels`; the prompts additionally exclude weapons, blood and any counted tally of
twelve companions, which keeps the reveal out of the artwork — the right call for this ballad.
`2d_tool` is `null` on every topic and for the chapter (0 ≤ 1); `kathakavya.md` would allow an
event-order strip only where the chapter's own સ્વાધ્યાય prints an ordering block, and this chapter
prints none.

---

## Publication   PASS (with one convention note)

- `publication_text` present on **12/12** topics; `publication_chunk` present on **12/12**;
  `concepts[].content[].publication_text` present on **all 24** paragraph blocks and on no `list`
  block.
- **Index and count match:** `concept_publication` entries equal the paragraph-block count on every
  topic, every `content_index` points at a real paragraph block, and every entry's string is
  byte-identical to the one landed at `concepts[].content[i].publication_text`. Zero mismatches.
- **No meaning added.** Diffed field by field against `12_authoring.json`: ten of twelve
  `publication_text` values are the Agent-12 `explanation` unchanged; M1.S1.T1 drops "બાળકો, જુઓ —"
  and makes the સ્વાધ્યાય sentence declarative; M3.S6.T12 drops "જુઓ,"; M3.S6.T11 swaps બાળકોને →
  બાળ તમામને and બાળકો → છોકરાં. All twelve appended real-life passages differ from the authored
  `real_life_example` only by second-person → impersonal verb forms and by dropping the closing
  question to the child. **No fact, gloss or reading was added, dropped or reworded anywhere.**
- **Vocative sweep** (`બાળકો`, `જુઓ —`, `બોલો`) across topic `publication_text`, the appended chunk
  tail and every concept `publication_text`: two hits, both at M3.S6.T11, both **false positives** —
  `બધાં બાળકો ધૂળાને પૂછે છે` (nominative subject) and `બાળકોને પણ … કુતૂહલ થાય છે` (dative). Both
  name the poem's own `પૂછે બાળ તમામ` as characters; neither is an address to the class, and a
  vocative cannot be in the dative. Not a defect.

**Convention note — read this, it needs one decision.** `13_assembly_validation.md` says
`publication_chunk` is *byte-identical* to `original_chunk`. It is not, on any of the 12 topics —
and it is not on **any of the 84 topics across ch01–ch09 either**. The pack-wide Agent-16 convention,
stated in `16_publication.json`'s own `notes[]`, is: the verbatim `original_chunk` first,
character-for-character and line-break-for-line-break, then a blank line, then `publication_text`,
then a blank line, then the publication-facing real-life passage. Verified this run: **all 12 chunks
open with a byte-identical `original_chunk` prefix** — the verbatim is untouched, which is what the
spec's own parenthetical ("the rewrite never touches verbatim") is protecting. Reported rather than
blocked because the spec's routing table blocks publication only on *missing*, *index-mismatched* or
*added-meaning*, and none of those applies. **A1/A16/A13 should reconcile the wording in one commit**
so this is not re-raised every chapter; if the byte-identity reading is the intended one, it is a
pack-wide re-run of Agent 16, not a ch10 defect.

---

## Gaps

1. **The emitted deliverables in this directory are STALE and must be regenerated.**
   `learning_plan_logical.json` (08:28), `learning_plan_textbook.json` (08:33) and
   `exercise_solutions.json` (08:28) were built from the *superseded* merge now at `_invalid/`, i.e.
   before the publication layer landed at 08:36. Both plans carry `publication_text` and
   `publication_chunk` **empty on 12/12 topics**. Agents 14 and 15 must re-run against the
   `13_merged.json` written by this pass. Not an authoring defect and not routed as a failure —
   but nothing should ship until they do.
2. **The `## LP2 validator` result now in this directory was run against that stale plan.** It is
   carried forward below for provenance only and does **not** certify the current merge. Re-run the
   validator after Agents 14/15 re-emit.
3. **`textbook_url` is a local path**, `../Textbooks-pdf/std-6/ch-10-sathi-mare-bar.pdf`. The GSEB
   readers have no hosted URL; recorded in `11_pages.json` `gaps[]`, carried here unchanged. Page
   range `63–67` is `confidence: high` (printed folio read off renders of pp. 1 and 5, agreeing with
   the manifest row and the std-6 N+11 offset).
4. **`chapter_master_id` is `null`** — the GSEB row is fetched from the education DB (VERIFY-2),
   never derived and never invented. It was not invented here.
5. **`publication_id` is `1`** — the pack's standing provisional value (a CBSE row carried over from
   the Hindi run), matching ch01–ch09. It is **not** a verified GSEB publication row. VERIFY-2 owns
   the real value; the contract's "must not be null" is satisfied only nominally until then.
6. **`subject_ref_id` and `medium_id` are `null`** — server-injected, correct as written.
   `english_plan_id` / `english_chapter_id` are `null` — a Gujarati chapter has no English twin.
7. **`ordering` is not set** — Agent 14/15's field, deliberately not written here.
8. **Root `genre` disagreement, resolved toward the contract.** `01_meta.json` records the printed
   label `કથાકાવ્ય / કથાગીત`; `02/04/05` carry the slug `kathakavya`; `13_merged.json` emits the
   **slug**, per `phase2_contract.md` and ch01's precedent. Note that ch05 and ch09 of this same pack
   emit a Gujarati *label* in root `genre` — the pack is inconsistent chapter to chapter. Not
   blocking, but A1 should settle it pack-wide.
9. **`teaching_lens` contains the numeral `6`** ("ધો. 6 — પ્રાસ 'સંભળાવવો'…"). A root
   pipeline/lens field, not child-facing display text, so the no-numbers rule does not bite. Noted so
   it is not re-raised each run.
10. **Single-render transcription.** `01_meta.json` `extraction_notes[]` (18 entries) records that
    only 150-dpi renders were available; A1 cross-checked doubtful glyphs by 3×–14× PIL crop-zoom
    from the same PNGs and by pango-view reference rendering (`કૂદ્યો` vs `કૂધ્યો`) rather than by an
    independent second render. Whether that substitutes for a true double-render is the
    orchestrator's call; A1 says so plainly rather than claiming a second pass.
11. **Printed inconsistencies preserved, not corrected** — all recorded in `extraction_notes[]`: the
    શબ્દાર્થ box's scrambled `વિકરાળ … ભયાનક` ordering with its double space; the entry
    `રોકાણ - વાર, વિલંબ` for a word that appears in **no** line of the poem; and સ્વાધ્યાય block 7
    reprinting two poem lines in altered form (`જાવું'તું જે ઠામ` for the poem's `જે ગામ,`). Each is
    carried as printed, and the teaching quotes `રોકાણ` nowhere.
12. **Naive quote-balance false positive at M3.S5.T10.** A mechanical run of `kathakavya.md` hard
    gate 3 reports an odd single-quote count in that chunk. The mark is the elision apostrophe in
    `જાવું'તું`, which is content, not a speech quote — A2 and A4 both warned of exactly this. The
    gate genuinely passes; every real speech opens and closes inside one topic.
13. **Climax placement — a recorded disagreement, not an error.** `kathakavya.md` §Emphasise names
    this ballad's turn as the bluff `'નથી કદી હું એકલો, સાથી મારે બાર !'`; `01_meta.json`, read off
    the page, names the વળાંક as the thieves' flight. A2 preferred the chapter-measured reading and
    set `topic_category: "climax"` on M3.S5.T9, stating the disagreement openly. `topic_category` is
    free text; avoid-gate 9 holds under this placement (verified above). Reported, not blocked.
14. **O5's `objective_text` quotes a joined string** — `'નથી હું એક, બાર જણા લઈ નીકળ્યો'` joins the
    end of printed line 9 to the start of line 10 and drops the vocative `અલ્યા,`. `objective_text`
    is not a verbatim field so nothing is blocked, but where the teaching quotes this speech it
    should quote a printed line whole. A4 raised it; carried forward here still unresolved.
15. **Nine of twelve topics carry exactly one કડી**, which reads close to a કડી-wise cut. It is not
    one: the count gate holds (12 topics vs 12 ઘટના vs 15 કડી) and the grouping is the source's own
    marker grouping. A4's note is reported here rather than re-litigated.
16. **The અનુવાદ block (EX11)** is answered in the medium of instruction on purpose and marked as
    such in its `teacher_note` — the script check correctly does not fire on it, and a script
    failure raised against it would be a false positive.

## LP2 validator
⚠ **Run against the stale plan, not against this merge — see Gaps 1–2.**

- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json (built 08:28, before the publication layer landed)
- Result: HTTP 200, success=true, plan_id=gseb_eng_gujarati6_ch10_v1
- validation_errors: [] (none)
- message: "Valid"

Shape is therefore known good; the run must be repeated after Agents 14/15 re-emit from the current
`13_merged.json`, and the re-run result recorded here in Phase 8.

---

### Route
No A–D failure. No agent is routed for re-authoring.

| Item | Owner | Blocking? |
|---|---|---|
| Re-emit `learning_plan_logical.json` / `learning_plan_textbook.json` / `exercise_solutions.json` from the current `13_merged.json` | `14_*` / `15_*` | not an A–D block, but nothing ships until done |
| Re-run the LP2 validator on the re-emitted plan | Phase 8 | — |
| Reconcile `publication_chunk` byte-identity wording across `13_assembly_validation.md` and the pack-wide Agent-16 convention | `16_publication_authoring.md` + spec owner | no |
| `publication_id`, `chapter_master_id`, `chapter_id` board/medium segments | VERIFY-1 / VERIFY-2 | no (pre-upload) |

## LP2 validator

- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json
- HTTP status: 200
- plan_id: gseb_eng_gujarati6_ch10_v1
- validation_errors: [] (none)
- message: Valid

