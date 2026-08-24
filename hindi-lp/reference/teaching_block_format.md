# Teaching Block Format (Step 4) — exact text first, then one linear explanation

Every topic is **one छंद / दोहा / पद / घटना**, anchored to verbatim Devanagari, then taught through
a single **linear** block — not a fan of multi-angle perspectives.

This block is for the **reading scenes only**. The textbook अभ्यास blocks are a separate
deliverable (Agent 10), never teaching blocks.

## The anchor: verbatim before anything

`original_chunk` — the exact passage, word for word, line breaks and मात्राएँ intact
(`devanagari_verbatim.md`). Only once it is in place does explanation happen.

## The three parts, in order

1. **`original_chunk`** — the verbatim passage. *The anchor; never paraphrased.*
2. **`explanation`** — the plain teaching explanation, carrying **both layers in one field**:
   (a) **क्या हो रहा है + the plain meaning**, with vocabulary **glossed inline the moment it
   appears** (`shabd_gloss.md`); and (b) **the deeper reading** — the अलंकार, the भाव, the
   why-behind-the-behaviour, the turn — woven in **where the passage genuinely calls for it**.
3. **`real_life_example`** — **one** Indian, concrete, age-11–12 anchor (`teaching_voice_hi.md`).

### This is where the old two-objective spine lives now

Earlier Hindi work used O1 व्याख्या + O2 दृष्टिकोण per topic. Phase 2 has no per-topic objective
pair — objectives are a plan-level registry (`phase2_contract.md`). The teaching is unchanged; it
simply lives in the right fields:

| old | now |
|---|---|
| O1 व्याख्या | **`explanation`** |
| O2 दृष्टिकोण | **`real_life_example`** |

Do not attempt two objectives per topic. It fails validation, and the teaching value was always in
these two fields.

### When `explanation` carries a deeper layer, and when it stays plain

Add the deeper layer when the passage carries meaning beyond the literal —
a **अलंकार doing work** (`जग को दिया दिखाया`), a **figurative line**, a **why** behind a choice
(*why* ध्यानचंद answered with goals and not with the stick), the **turn** where the meaning pivots.

Keep it plain when the passage is a plain beat (`वे मैदान से बाहर ले जाए गए`) or a pre-reading
topic. **Over-reading a plain scene flattens it** just as surely as under-reading a rich one.

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
| craft (काव्य) | `figures_of_speech[]`, `rhyme_scheme` (`alankar_chhand.md`) |
| concept blocks | `concepts[].content[]` — `paragraph` / `list` |

Three-tier summaries **strictly increase in length**: `brief_summary` < `summary` <
`detailed_summary`.

## Gradual release

`original_chunk` + `explanation` are modelled by the teacher; `real_life_example` is built jointly
with the child; `recall_questions` hand the work over. Where a topic prepares an अभ्यास task
(तुकांत शब्द, संस्मरण लेखन, शब्द-युग्म), its `explanation` should **name the skill the exercise
will ask for** — the exercise is the independent step the teaching set up.
