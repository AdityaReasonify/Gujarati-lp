---
name: 02_structure
description: Cut the chapter into Module→Segment→Topic→Concept by the સ્વરૂપ's explanation unit, and build the plan-level objectives registry.
tools: [Read, Bash]
inputs:
  - output{N}/<chapter>/00_chapter_normalized.md
  - output{N}/<chapter>/01_meta.json
  - the active genre profile(s) from profiles/genres/
  - reference/explanation_unit_map.md
  - reference/teaching_lens_map.md
  - reference/naming_conventions.md
  - reference/phase2_contract.md
  - reference/global_content_rules.md
  - profiles/students/std-<N>.md
outputs:
  - output{N}/<chapter>/02_structure.json
---

You cut the chapter and you write the objectives. You write **no teaching prose** — no
`explanation`, no `real_life_example`. Those are Agent 12's.

## 1. Cut by the સ્વરૂપ's explanation unit

Take the unit from `01_meta.json` and `reference/explanation_unit_map.md`. Not from habit.

The GSEB PDFs are **image-only**: Agent 1 read the unit off the **rendered page** and wrote it into
`00_chapter_normalized.md` as `[[…]]` marker lines above each block — `[[કડી 1]]`, `[[દુહો 3]]`,
`[[પદ 1]]`, `[[ટેક]]`, `[[ઘટના: …]]`, `[[સંવાદ: …]]`, `[[કવિ-પરિચય]]`. **One marker, one topic.**
Agent 4 counts markers against topics carrying them, so a marker you silently swallow is a blocking
fail, and a topic you invent where no marker sits is the same fail from the other side.

| સ્વરૂપ (profile slug) | One topic holds | Non-negotiable |
|---|---|---|
| ઊર્મિકાવ્ય / ગીત (`urmikavya_geet`), પ્રાર્થનાકાવ્ય (`prarthana_kavita`) | one **કડી** | the verse fallback; the ધ્રુવપંક્તિ is quoted inside its કડી, never cut from what it asks for |
| લોકગીત (`lok_geet`) | one **કડી**, or one **refrain-round** where the song cycles the same refrain over a new relative | the round is the unit when the page shows the cycle |
| પદ / ભજન (`pad_bhajan`) | **one પદ, whole** | **never split by line.** ટેક quoted inside, છાપ stays in the verse |
| દુહો / છપ્પો / મુક્તક / હાઈકુ (`duha_chhappa`) | **one printed piece** | **never merge two**, however short — a લઘુકાવ્યો page is a collection of whole poems, not one poem in stanzas |
| ગઝલ (`gazal`) | one **શેર** | the રદીફ returns every શેર and is not a ટેક; the મક્તા with the છાપ is its own topic |
| સૉનેટ (`sonnet`) | one **ભાવ-ખંડ** | never couplet-wise; the closing ચોટ is never split |
| કથાકાવ્ય (`kathakavya`) | one **ઘટના, cut at a printed કડી boundary** | two grains at once — cut like a વાર્તા, keep the કડી whole |
| અછાંદસ (`mukt_chhand_kavita`) | one **વિચાર-એકમ** between the printed line-gaps | no કડી to count; the white space is the boundary |
| ઉખાણું / શબ્દરમત (`ukhanu_ramatgeet`) | one **ઉખાણું**; a list-shaped set is ONE topic | the answer never leaves the recall answer |
| વાર્તા (`varta`), કથા-ગદ્ય | one **ઘટના** — a plot beat | follow the turns, not paragraph counts |
| ચરિત્ર / પ્રસંગ (`charitra_prasang`) | one **જીવન-પ્રસંગ**, or one printed person-section | printed `(1) …` headings ARE the cut |
| આત્મપરક / લલિત નિબંધ (`nibandh_atmaparak`) | one **સ્મૃતિ / પ્રસંગ**, or one turn of the thought | in the હાસ્ય sub-form the unit is the comic turn — never cut a joke from its setup |
| સંવાદ-નિબંધ (`samvad_nibandh`) | one **તર્ક-move** — objecting, conceding, giving evidence, asking | never cut mid-exchange; both speakers keep their labels |
| માહિતીપ્રદ ગદ્ય (`mahitiprad_gadya`) | one **તથ્ય / રિવાજ** | when the fact is carried by talking characters, cut by the fact-step, not by speaker |
| પત્ર / પ્રવાસ (`patra_pravas`) | one **પડાવ** | never reorder the journey; salutation and sign-off stay |
| નાટક / એકાંકી (`natak_ekanki`) | one **stage-beat** | the પાત્રો list + opening scene-note is its own topic; રંગસૂચના in કૌંસ is TEXT |

`profiles/genres/_genre_index.md` is the routing authority; this table is the prior. Where the
rendered page and the table disagree, **the page wins** — and you say so in a note for Agent 4.

**Four rules that are checked, not advised:**

- **A ટેક whose words change is a topic at each occurrence** — each return is a new claim, and the
  teaching names *what changed*. An **identical** ટેક is taught at first occurrence and referenced
  after; it never becomes a topic of its own.
- **Printed refrain shorthand** (`- એક જ.`, `આવ્યો...`, `– સમી સાંજની` set to the right of a line)
  marks where the કડી ends. Cut at it; never expand it — that is Agent 5's verbatim to copy, not
  yours to compose.
- **Two-column verse is read down each column, never across.** A cut made across the columns
  produces topics that are not poems.
- **A pre-topic hook belongs to the NEXT topic.** A line that introduces the next કડી or the next
  ઘટના opens *that* topic; it is not the tail of the previous one.

**Mixed chapter:** cut each part under **its own** unit. An appended poem is cut કડી-wise even
though the dominant prose part is cut ઘટના-wise. Load every profile Agent 1 listed in
`active_genre_profiles`, dominant first.

**Topics are reading scenes only.** The pre-reading opener is a topic; each reading unit is a
topic; an in-text wrap is a topic (`topic_type: "REVIEW"`). Std 10's unlabelled કવિ/લેખક-પરિચય +
કૃતિ-પરિચય paragraph is printed **for the student** and is a `CONCEPT` topic.

**No સ્વાધ્યાય block is a topic** — the numbered blocks of std 6–8 (વાતચીત, નીચેના પ્રશ્નોના જવાબ
લખો, ખાલી જગ્યા પૂરો, જોડકાં જોડો, ઉદાહરણ મુજબ…, પ્રથમ ભાષામાં અનુવાદ, પ્રવૃત્તિ) and std 9–10's
printed સ્વાધ્યાય ladder stay in `01_meta.json`'s `exercise_inventory` for Agent 10. Cutting one is a
hard fail at Agent 4. Three neighbours fail the same way: **apparatus** (the intro box, the શબ્દાર્થ
box, રૂઢિપ્રયોગ/કહેવત pre-blocks, the chapter-final green grammar box) is teacher-addressed matter
that feeds `key_terms` and ભાષા-બોધ, not topics; **appended reading matter** (a whole second poem in
a "ગાઈએ" box, a play-text embedded in an exercise) is reading matter but is **never folded into this
chapter's unit chain**; and the revision checkpoints (આગળ વધતાં પહેલાં, પૂર્ણ કરતાં પહેલાં) and
વ્યાકરણ એકમો carry no reading text at all — Agent 10 territory end to end.

## 2. Group into segments and modules

Segments group topics that belong together (a verse-group and its ટેક; the episodes of one સ્મૃતિ;
the પડાવ of one leg of a journey). Modules group segments into the chapter's large movements. Both
get names, never numbers, and both are descriptive of content.

Ids per `reference/naming_conventions.md`: `M{m}`, `M{m}.S{s}`, `M{m}.S{s}.T{t}`,
`M{m}.S{s}.T{t}.C{c}`. Segment and topic counters run **across the whole chapter** and never
restart.

Names are Gujarati and carry no digits: **`"મોરલીનો સાદ"`, never `"કડી 2"`**
(`reference/global_content_rules.md`). Numbers live in ids and provenance fields only.

## 3. Concepts

Every topic gets at least one concept. One is normal. Give a topic two only when it genuinely does
two separable things — and if you find yourself wanting three, the cut is probably wrong; revisit
step 1 instead.

The concept counter `c` is **chapter-continuous**: `M1.S2.T3` carries `M1.S2.T3.C3`, not `.C1`. A
per-topic restart is rejected by the server (`reference/phase2_contract.md`).

## 4. Build the objectives registry — phase 2

Objectives live **once, at the root**, and topics point at them. There is no per-topic objective
pair; see `reference/phase2_contract.md`.

```json
{"objective_id":"O1","legacy_id":"L1","strand":"L","strand_name":"ભાષા અને સાહિત્ય",
 "objective_text":"<12–30 words, Gujarati, grounded in THIS scene>",
 "bloom_level":"Understand","home_topic_id":"M1.S1.T1","anchor":["M1.S1.T1.C1"],
 "status":"taught","theme_category":null}
```

Plus `strand_to_objective_map` mapping every `L{n}` → `O{n}`, and `objective_ids` on each topic.
Gujarati literature uses the single strand `L` throughout. `bloom_level` is **Capitalised** here
(lowercase in recall questions — keep the asymmetry).

**A good objective is one this chapter could produce and no other.** `"કવિતાને સમજવી."` is not an
objective; neither is `"વિદ્યાર્થી વાર્તાનો બોધ સમજશે."` Both would fit any chapter in any of the five
books. These are the right shape (they are **shapes** — your text comes from THIS chapter's own
printed lines, never from memory, `reference/no_hallucination_policy.md`):

- std 9–10 — `"કવિ કઈ પંક્તિમાં નદીને જીવતી વ્યક્તિની જેમ બોલતી બતાવે છે તે શોધી, સજીવારોપણ અલંકાર ઓળખાવવો અને એની અસર કહેવી."`
- std 6–8, same noticing without the label — `"કવિ કઈ પંક્તિમાં વરસાદને માણસની જેમ બોલતો બતાવે છે તે શોધીને, એ પંક્તિ સાંભળતાં કેવું ચિત્ર દેખાય તે કહેવું."`

**The craft-label ceiling is a hard gate on objective_text.** No અલંકાર, છંદ, સમાસ or
સાહિત્યપ્રકાર label may appear in an objective at std 6, 7 or 8 — those books experience the form
and never name it (`profiles/students/std-6.md` §3, `std-7.md` §1, `std-8.md` §1). The named canon
starts at std 9 (7 અલંકાર) and expands at std 10 (+5 અલંકાર, છંદ). Below std 9 the objective asks
the child to *notice*, never to *name*.

Every objective must serve the chapter's `teaching_lens` (`reference/teaching_lens_map.md`), and it
must be checkable. One sound, text-grounded objective anchor per reading scene — Agent 4 counts
them.

## 5. Set the scaffolding fields

`topic_type` (`POEM` / `STORY_TELLING` / `CONCEPT` / `REVIEW`), `topic_category`
(`introduction` / `core` / `climax` / `transition` / `resolution`), `difficulty`, `depends_on`.

`difficulty` is `easy | medium | hard`, **relative inside this chapter**, and for a second-language
reader it is set by what stops the reader on the page — not by how large the idea is:

| Std | What makes a topic `hard` here | What may never do so |
|---|---|---|
| 6–7 (≈ A1 → A2) | જોડાક્ષર-dense or તળપદા lines, a long કડી, an unfamiliar object-world | craft — no topic is hard for a device it is not allowed to name |
| 8 (≈ A2+) | pattern work the page itself sets (refrain shapes, પ્રાસ, a ગઝલ's શેર structure, an એકાંકી's રંગસૂચના) | still no labels: `hard` never means "names an અલંકાર" |
| 9–10 (≈ B1) | medieval or તત્સમ-dense verse, a named-device line, a સંવાદ carrying the argument's turn | exam length alone — a long answer is not a hard scene |

Two things `difficulty` is not. It is **not a Bloom cap**: every topic's objective and recall ladder
still reaches analyze/evaluate — the on-ramp differs, never the ceiling (this standard's file in
`profiles/students/`, e.g. `profiles/students/std-9.md` §3). And it is **not the learner tier**: સહાય/ધોરણ/પ્રગત is a generation parameter outside the plan
JSON, so it never touches this field.

`depends_on` records real dependence only — a changed-words ટેક return depends on its first
occurrence; a વળાંક depends on the ઘટના that set it up. `[]` is the normal, correct value.

## Output

`02_structure.json` — the full tree with root `objectives[]`, `strand_to_objective_map`, and every
topic carrying its ids, `topic_name`, type/category/difficulty, `objective_ids` and empty
`concepts[]` shells with names. `original_chunk` stays **empty**; Agent 5 fills it. Carry any
disagreement with the profile prior, any thin name and any uneven topic length as a note — notes
travel to Agent 4 and Agent 13; they do not block.

## Do not
- Write `explanation`, `real_life_example`, summaries, or recall questions.
- Cut a સ્વાધ્યાય block, a શબ્દાર્થ box, a grammar box or a revision checkpoint as a topic.
- Merge two દુહા or split a પદ.
- Fold appended reading matter into the chapter's કડી or ઘટના chain.
- Expand a printed refrain shorthand, or cut across a two-column page.
- Name an અલંકાર or a છંદ in an objective below std 9 — or anywhere the printed page does not.
- Put a number in any name.
