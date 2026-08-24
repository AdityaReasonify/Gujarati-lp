# Validation Report — std 6, ch 10 · સાથી મારે બાર (રમણલાલ સોની)
સ્વરૂપ: kathakavya — કથાકાવ્ય / કથાગીત (confidence: high)   explanation unit: એક વાર્તા-પગલું (ઘટના), boundary always at a printed કડી (પ્રાસ-જોડ) end
Topics: 12   Objectives: 12   Images: 0/12   Exercises: 13/13

**VERDICT: NOT COMPLETE.** Sections A–D pass. The run is blocked by a missing pipeline layer:
`16_publication.json` was never written, so every `publication_text` / `publication_chunk` in
`13_merged.json` is empty. Owner: **`16_publication_authoring.md`**. This is a real block, not a
cosmetic gap — the plan cannot be emitted by Agent 14/15 with an empty publication layer, and Agent
13 does not author publication text to close it.

---

## A–D (blocking)   PASS

### A — Diagnosis and lens   PASS
- સ્વરૂપ diagnosed off the rendered page with `genre_signals` (structure / theme / exercises) and
  `genre_confidence: high`. The book names the form itself twice and never settles on one label —
  the blue intro box prints "આ કથાકાવ્યની બાળકો પાસે નાટ્યાત્મક રજૂઆત કરાવવી." and સ્વાધ્યાય blocks
  2 and 13 print "આ એક કથાગીત છે…" / "આ કથાગીતનું ગાન વર્ગમાં કરો." — quoted as evidence, not as the
  verdict; `01_meta.json` records both.
- Explanation unit matches the roster line for કથાકાવ્ય: **one વાર્તા-પગલું cut at a printed કડી
  boundary**. Measured: 12 `[[ઘટના: …]]` markers → 12 instructional topics, one-to-one; 15
  `[[કડી n]]` markers, each carried whole by exactly one topic; 12 < 15, so `kathakavya.md` hard
  gates 1 and 2 both hold. All 30 printed lines are covered contiguously, 1–30, no gap, no overlap.
- ટેક: **zero** — a measured fact, not an empty box. No line recurs and no refrain shorthand is
  printed; that absence is what pushes the diagnosis off the ગીત branch.
- Not a mixed chapter. Apparatus did not become a reading scene: the blue પ્રવેશક-પેટી, the green
  શબ્દાર્થ box, the • રૂઢિપ્રયોગ pre-block and the chapter-final ઉખાણા-પેટી carry no topic —
  verified by scanning every `original_chunk` for their strings (zero hits).
- `guiding_question` is derived from this poem — "એકલો ધૂળો ચાર ચોર સામે કઈ રીતે ટકી ગયો, અને એના
  'બાર સાથી' ખરેખર કોણ નીકળ્યા ?" — and reading the twelve explanations in printed order answers it.

### B — Verbatim and structure   PASS
- 12/12 topics carry a non-empty `original_chunk`; every line of every chunk matches a line of
  `00_chapter_normalized.md` character for character (mechanical check, zero misses).
- Script: Gujarati (U+0A80–0AFF) throughout. **Zero** Roman and **zero** Devanagari characters
  anywhere in `original_chunk`, and zero in authored display text outside brackets. No `।` anywhere.
- Printed poetic licence intact and unmodernised: `ચડિયો`, `અલ્યા`, `કાંક`, `નહિ`, `વારતા`, `દશ`,
  `પાય`, `બી ગયા`, `સબોસબ`, `ધબોધબ`, `આઘુંપાછું`, and the apostrophe-elision `જાવું'તું`.
- Two-column p. 63 read **down each column**, and the પ્રાસ pair સાથ/હાથ that breaks across the
  p. 63 → p. 64 boundary is held whole inside M3.S5.T9 — no કડી split at the page break.
- Attribution `- રમણલાલ સોની` sits inside the **last** topic's `original_chunk` (M3.S6.T12), as the
  profile requires, even though the poet slot is printed at the head of p. 63.
- Marker accounting: કડી 15 · ઘટના 12 · સ્વાધ્યાય 13 · topics 12. **No `[[સ્વાધ્યાય: …]]` block
  became a topic** (all 13 live in `10_exercise_solutions.json` alone).
- Header furniture kept out: the pink `10` number box, the QR badge and its Latin code string, and
  the running folios are absent from every chunk.

### C — The teaching block   PASS
- 12/12 topics carry a non-empty `explanation` **and** `real_life_example`.
- Every band holds with no trimming needed: `explanation` 68–78 words, `real_life_example` 61–71
  words (band 55–90); `objective_text` 15–23 words (band 12–30). Bands applied as written —
  ⚠ provisional until VERIFY-4, and not widened.
- Three-tier summaries strictly increase on all 12 topics (e.g. 11 / 23 / 53 words at M1.S1.T1).
- L2 calibration held: ordinary-but-hesitable words are glossed at the point of use — `વાણિયો`,
  `સમી સાંજ`, `ઉચાટ`, `વીંઝે`, `સબોસબ`, `ખાળે`, `પાય`, `વારતા`, `નાઠા` — in Gujarati, in the
  chapter's own શબ્દાર્થ wording, with no Hindi word standing in for a Gujarati one.
- `real_life_example` is Indian, single and inside std-6 reach throughout — ઘર, શેરી, દીવાબત્તીનું
  ટાણું, નવરાત્રિનો રાસ, વર્ગખંડ. No adult framing, no abstraction, no three-examples-in-one.
- Craft is at std-6 ceiling: પ્રાસ is **heard**, never named. Zero અલંકાર labels and zero છંદ
  labels anywhere in the pack — correct for this standard.

### D — સ્વરૂપ essence   PASS
- `kathakavya.md` **avoid** list checked item by item; no violation found.
- `figures_of_speech` is `[]` on all 12 topics — the honest answer for this ballad at std 6, and the
  one `no_hallucination_policy.md` §3 asks for. Nothing to verify verbatim because nothing was
  claimed.
- `rhyme_scheme.rhyming_words` pairs are all words printed in this chapter (નામ—ગામ, વાટ—ઉચાટ,
  વિચાર—બાર, ચાર—વાર, એક—વિવેક, માલ—વિકરાળ, સબોસબ—ધબોધબ, ઘાવ—દાવ, જંગ—રંગ, જોર—ઘોર, સાથ—હાથ,
  ગામ—કામ, તમામ—નામ, પાય—થાય, વિશ્વાસ—ખાસ) — mechanically confirmed against
  `00_chapter_normalized.md`.
- No tacked-on બોધ: zero occurrences of "આ કાવ્ય આપણને શીખવે…", "બોધ એ છે કે…", "આપણે પણ … જોઈએ" in
  any explanation, summary, bullet or recall answer.
- Craft never displaces the story: every `explanation` opens on a character or an action from its own
  chunk, and no topic carries more than one craft sentence.
- Turn not spoiled early: the closing tally's words (`ચાર કાટલાં`, `દશ થાય`, `હિંમત અને વિશ્વાસ`)
  appear in **no** topic before the reveal, in no summary and in no recall answer.
- Community dignity held: `વાણિયો` is glossed as ધૂળાનું કામ (વેપાર કરનાર) and never as a caste
  label; zero occurrences of `વાણિયાઓ`, `વેપારીઓ`, `કંજૂસ`, `બીકણ` in any field. The intro box's
  own words (`વણિક`, `ઝઝૂમી`, `બુદ્ધિપૂર્વક`) were correctly kept out of the teaching.
- The one **hard** sensitivity item (M2.S4.T7 — સુરક્ષા + સંઘર્ષ) is addressed in both places it
  had to be: the explanation stays on ધૂળાની ચતુરાઈ and on `ખાળે ઘાવ` rather than on the blows, and
  the block-12 નાટ્યીકરણ answer prints the mime instruction outright — "કોથળો હાથમાં લેવાનો નથી —
  માત્ર હાથનું હલનચલન". `areas[]` values (સમુદાય, સુરક્ષા, સંઘર્ષ) are all inside the seven fixed
  labels. 32 hard `avoid_checks` from `07_pitfalls.json` across the 12 topics: none left unaddressed.

---

## Publication   **FAIL — BLOCKING**   owner: `16_publication_authoring.md`

`16_publication.json` does not exist in `output6/ch10/`. Every other std-6 chapter (ch01–ch09) has
one; Agent 16 has not run for this chapter. Consequences now visible in `13_merged.json`:

| Field | State |
|---|---|
| `publication_text` (topic) | empty on **12/12** topics |
| `publication_chunk` (topic) | empty on **12/12** topics |
| `concepts[].content[].publication_text` | empty on **12/12** paragraph blocks |

Nothing was invented to fill these. Empty strings are written so the shape matches the contract and
the absence is visible; Agent 16 fills them, Agent 13 does not. Once 16 lands, re-run this agent —
the byte-identity check (`publication_chunk` == `original_chunk`), the index-and-count match against
`concepts[].content[]`, and the vocative sweep (`બાળકો`, `જુઓ —`, `બોલો` — note M1.S1.T1's
`explanation` opens "બાળકો, જુઓ —", which is fine in the teacher-voice field and must **not** survive
the rewrite) are wired and will run automatically.

---

## E–G (reported)

**E — સ્વાધ્યાય and risk.** All 13 inventoried blocks answered, skill-tagged and mapped:
`blocks_found` = 13 = inventory length, `unanswered` = `[]`, `unmapped` = `[]`, every
`covered_by_topics` id resolves to a real topic. The seven personal-opinion / પ્રવૃત્તિ /
teacher-addressed blocks (વાતચીત, વાર્તાલેખન, પ્રાસ-જાળી, શબ્દો-આપીને-વાર્તા, અનુવાદ, નાટ્યીકરણ,
સમૂહગાન) carry `is_model_answer: true` and are labelled as one possible response in the answer text
itself. The printed પ્રાસ grid and the ખરું-ખોટું table are filled with teaching values
(`values_filled_for_teaching`). The chapter-level સુરક્ષા note reaches both activity blocks.

**F — Shape and media.** All 12 `json_contract.md` invariants hold:
`phase: 2`; `chapter_id: gseb_eng_gujarati6_ch10`, `plan_id: …_v1`; 12/12 topics with a non-empty
Gujarati `original_chunk`; 12/12 topics with ≥1 concept, each with non-empty `content[]` and a
resolving `objective_id`; 12 unique objectives, every `home_topic_id` and `anchor[]` resolving,
`strand_to_objective_map` covering all twelve `legacy_id`s; inline `learning_objectives[]`
`objective_text` identical to the registry character for character on all 12 topics; media ids
concept-scoped and matching `MEDIA_ID_RE`; recalls `.RQ{n}` with `legacy_id` `.TR{n}` — **no `.SR`
anywhere**; `publication_id` non-null; summaries strictly increasing; no digits in display text.
Concept numbers are chapter-continuous C1…C12 and ids match traversal position exactly (M1.S1.T1 →
M3.S6.T12). `topic_type` is the authored enum `POEM` on all 12, which is correct for an intermediate
file — Agents 14/15 map it to `instructional` at emit. ⚠ `chapter_id`'s board/medium segments remain
provisional until VERIFY-1.

**G — the seven usual mistakes.** None present. Not a સાર+બોધ+પ્રશ્નોત્તર plan; no couplets merged
or fused; nothing split line by line and no ટેક lifted out (there is no ટેક); no poetic licence
silently corrected; no અલંકાર named to fill a field; no adult or non-Indian `real_life_example`; no
સ્વાધ્યાય cut as a topic — the exercise deliverable is complete at 13/13.

---

## Media
`reuse_report`: **scenes 12 · authored 12 · reused 0 · rejected []** — and 12 topics carry `"image"`
in `available_content_types`, so scenes matches the reading scenes exactly. Every one of the 12 media
nodes carries `image_url: ""` **and** a non-empty, self-contained `generation_prompt`; no
`[reused frame: …]` stamp appears anywhere, and no fabricated URL. `reused: 0` is correct — no
Gujarati frame pool exists, so `Images` reads **0/12**. Every `negative_prompt` carries
`Devanagari script labels`, and the prompts additionally exclude weapons, blood and any counted
tally of twelve companions — the latter keeping the reveal out of the artwork, which is the right
call for this ballad. `2d_tool` is `null` for the whole chapter (0 ≤ 1).

## Gaps

1. **`16_publication.json` absent** — the blocker above. Owner `16_publication_authoring.md`.
2. **`textbook_url` is a local path**, `../Textbooks-pdf/std-6/ch-10-sathi-mare-bar.pdf`. The GSEB
   readers have no hosted URL; recorded in `11_pages.json` `gaps[]`, carried here unchanged.
3. **`chapter_master_id` is `null`** — the GSEB row is fetched from the education DB (VERIFY-2),
   never derived and never invented. It was not invented here.
4. **`publication_id` is `1`** — this is the pack's standing provisional value (a CBSE row carried
   over from the Hindi run) and matches ch01–ch09. It is **not** a verified GSEB publication row.
   VERIFY-2 owns the real value; the contract's "must not be null" is satisfied only nominally until
   then.
5. **`subject_ref_id` and `medium_id` are `null`** — server-injected, correct as written.
6. **`ordering` is not set** — Agent 14/15's field, deliberately not written here.
7. **Root `genre` disagreement, resolved toward the contract.** `01_meta.json` records the printed
   label `કથાકાવ્ય / કથાગીત`; `02/04/05` carry the slug `kathakavya`. `13_merged.json` emits the
   **slug**, per `phase2_contract.md` ("slug from the Gujarati genre roster") and per ch01's
   precedent. Agent 4 flagged this for reconciliation; the printed label stays available in
   `01_meta.json`. Not blocking — but A1 should settle whether `01_meta.genre` holds the slug or the
   label pack-wide.
8. **`teaching_lens` contains the numeral `6`** ("ધો. 6 — પ્રાસ 'સંભળાવવો'…"). This is a root
   pipeline/lens field, not child-facing display text, so the no-numbers rule does not bite. Noted so
   it is not re-raised each run.
9. **Single-render transcription.** `01_meta.json` `extraction_notes[]` records that only 150-dpi
   renders were available; A1 cross-checked doubtful glyphs by 3×–14× PIL crop-zoom from the same
   PNGs and by pango-view reference rendering (`કૂદ્યો` vs `કૂધ્યો`) rather than by an independent
   second render. Whether that substitutes for a true double-render is the orchestrator's call, and
   A1 says so plainly rather than claiming a second pass.
10. **Printed inconsistencies preserved, not corrected** — all recorded in `extraction_notes[]`: the
    શબ્દાર્થ box's scrambled `વિકરાળ … ભયાનક` ordering with its double space; the entry
    `રોકાણ - વાર, વિલંબ` for a word that appears in **no** line of the poem; and સ્વાધ્યાય block 7
    reprinting two poem lines in altered form (`જાવું'તું જે ઠામ` for the poem's `જે ગામ,`). Each is
    carried as printed. The teaching correctly does not quote `રોકાણ` as a word of the poem.
11. **Naive quote-balance false positive at M3.S5.T10.** A mechanical run of `kathakavya.md` hard
    gate 3 reports an odd single-quote count in that chunk. The mark is the elision apostrophe in
    `જાવું'તું`, which is content, not a speech quote — A2 and A4 both warned of exactly this. The
    gate genuinely passes; every real speech opens and closes inside one topic.
12. **Climax placement — a recorded disagreement, not an error.** `kathakavya.md` §Emphasise names
    this ballad's turn as the bluff `'નથી કદી હું એકલો, સાથી મારે બાર !'`; `01_meta.json`, read off
    the page, names the વળાંક as the thieves' flight. A2 preferred the chapter-measured reading and
    set `topic_category: "climax"` on M3.S5.T9, stating the disagreement openly. `topic_category` is
    free text; avoid-gate 9 holds under this placement (verified above). Reported, not blocked.
13. **O5's `objective_text` quotes a joined string** — `'નથી હું એક, બાર જણા લઈ નીકળ્યો'` joins the
    end of printed line 9 to the start of line 10 and drops the vocative `અલ્યા,`. `objective_text`
    is not a verbatim field so nothing is blocked, but where the teaching quotes this speech it
    should quote a printed line whole. A4 raised it; it is carried forward here unresolved.
14. **Nine of twelve topics carry exactly one કડી**, which reads close to a કડી-wise cut. It is not
    one: the count gate holds (12 topics vs 12 ઘટના vs 15 કડી) and the grouping is the source's own
    marker grouping. A4's note is reported here rather than re-litigated.

## LP2 validator
Not run. `POST /api/lp2/learning-plans/validate` is Phase 8 and must return zero
`validation_errors` before upload. It should not be run against this plan until the publication
layer lands.

---

### Route
| Failure | owner |
|---|---|
| `publication_text` / `publication_chunk` / concept `publication_text` missing on all 12 topics because `16_publication.json` was never written | **`16_publication_authoring.md`** |

Re-run Agent 16 for std 6 ch 10, then re-run Agent 13. No other agent needs re-running: A1, A2, A4,
A5, A7, A8, A9, A10, A11 and A12 all pass every check this gate runs.
