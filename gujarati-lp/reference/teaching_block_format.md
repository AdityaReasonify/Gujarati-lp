# Teaching Block Format (Step 4) — exact text first, then one linear explanation

Every topic is **one કડી / દુહો / પદ / ઘટના**, anchored to verbatim Gujarati script, then taught
through a single **linear** block — not a fan of multi-angle perspectives.

This block is for the **reading scenes only**. The textbook સ્વાધ્યાય blocks are a separate
deliverable (Agent 10), never teaching blocks.

## The anchor: verbatim before anything

`original_chunk` — the exact passage, word for word, line breaks and માત્રા/અનુસ્વાર intact
(`gujarati_verbatim.md`). The GSEB PDFs carry no text layer: the verbatim is **transcribed from the
rendered page**, and the rendered page is the only authority. Punctuation exactly as printed — GSEB
Gujarati readers use `.` (પૂર્ણવિરામ); never introduce `।`. Only once the passage is in place does
explanation happen.

## The three parts, in order

1. **`original_chunk`** — the verbatim passage. *The anchor; never paraphrased, never transliterated.*
2. **`explanation`** — the plain teaching explanation, carrying **both layers in one field**:
   (a) **શું થઈ રહ્યું છે + the plain meaning**, with vocabulary **glossed inline the moment it
   appears** (`shabd_gloss.md`; this is a **second-language** reader, so the glossing bar sits lower
   — more everyday Gujarati words genuinely stop the child); and (b) **the deeper reading** — the
   અલંકાર, the ભાવ, the why-behind-the-behaviour, the વળાંક — woven in **where the passage genuinely
   calls for it**.
3. **`real_life_example`** — **one** Indian, concrete anchor inside the child's own world, pitched at
   the standard being authored (`teaching_voice_gu.md`).

### Age is a parameter, not a constant

The pack runs std 6–10. The anchor's reach moves with the standard — never write to a fixed
"eleven-year-old":

| Standard | Reader is about | Anchor reaches |
|---|---|---|
| 6 | 11 | ઘર, વર્ગખંડ, શેરી, રમત |
| 7 | 12 | શાળા, મહોલ્લો, તહેવાર (ઉત્તરાયણ, નવરાત્રિ), બજાર |
| 8 | 13 | ગામ/શહેર, ખેતર-કૂવો, ST બસ, મેળો |
| 9 | 14 | કામ કરતા મોટેરાં, સમાચાર, જવાબદારી |
| 10 | 15 | પોતાના નિર્ણય, ભવિષ્યની પસંદગી, સમાજ |

Gujarat-flavoured anchors are natural; the scope stays India, and it stays **one** anchor.

### This is where the old two-objective spine lives now

Earlier work in this pipeline used O1 વ્યાખ્યા + O2 દૃષ્ટિકોણ per topic. Phase 2 has no per-topic
objective pair — objectives are a plan-level registry (`phase2_contract.md`). The teaching is
unchanged; it simply lives in the right fields:

| old | now |
|---|---|
| O1 વ્યાખ્યા | **`explanation`** |
| O2 દૃષ્ટિકોણ | **`real_life_example`** |

Do not attempt two objectives per topic. It fails validation, and the teaching value was always in
these two fields.

### When `explanation` carries a deeper layer, and when it stays plain

Add the deeper layer when the passage carries meaning beyond the literal —
an **અલંકાર doing work** (the ટીપાં that introduce themselves and argue are સજીવારોપણ, not a science
note), a **figurative line** (`કડવા હોય લીમડા, પણ શીતલ એની છાંય`), a **why** behind a choice
(*why* જોગીદાસ ખુમાણ walks unarmed into his enemy's શોકસભા), the **વળાંક** where the meaning pivots
(`ચક્રવ્યૂહ તૂટ્યો પણ આપણો ભડવીર ખૂટ્યો !`).

Keep it plain when the passage is a plain beat — a dated biographical line, a scene that only moves
the party from one place to the next — or a pre-reading topic. **Over-reading a plain scene flattens
it** just as surely as under-reading a rich one.

A form's own forms are content, not errors: હાલીએ, ભેરુ, મોજારે, છઈએ get **explained where they
stand**, never corrected (`gujarati_verbatim.md`).

## Field-by-field

| Part | Lives in |
|---|---|
| verbatim | `original_chunk` |
| what happens + gloss seed | `modified_chunk` (Agent 5) |
| explanation + deeper reading | `explanation` |
| the Indian anchor | `real_life_example` |
| the goal | root `objectives[]` → mirrored in `learning_objectives[0].objective_text` |
| the check | `recall_questions[]` (`RQ{n}`, Bloom-laddered, each with an answer) |
| supporting | `key_terms`, `concept_bullets`, `important_points`, three-tier summaries |
| craft (કાવ્ય) | `figures_of_speech[]`, `rhyme_scheme` (`alankar_chhand.md`) |
| concept blocks | `concepts[].content[]` — `paragraph` / `list` |

Three-tier summaries **strictly increase in length**: `brief_summary` < `summary` <
`detailed_summary`.

## Gradual release

`original_chunk` + `explanation` are modelled by the teacher; `real_life_example` is built jointly
with the child; `recall_questions` hand the work over. Where a topic prepares a સ્વાધ્યાય task
(શબ્દજોડકાં, ઘટનાક્રમમાં ગોઠવો, રૂઢિપ્રયોગનો વાક્યપ્રયોગ, વાક્ય વિસ્તારો, પ્રથમ ભાષામાં અનુવાદ), its
`explanation` should **name the skill the exercise will ask for** — the exercise is the independent
step the teaching set up. Take those names from this chapter's `exercise_inventory` in
`01_meta.json`, never from an assumed list.
