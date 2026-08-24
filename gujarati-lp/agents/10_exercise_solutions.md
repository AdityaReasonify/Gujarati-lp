---
name: 10_exercise_solutions
description: The sole home of the textbook સ્વાધ્યાય — answer every block, skill-tag it, and map it to the reading scenes that prepare it.
tools: [Read, Bash]
inputs:
  - output{N}/<chapter>/00_chapter_normalized.md
  - output{N}/<chapter>/01_meta.json   (exercise_inventory)
  - output{N}/<chapter>/04_converged.json
  - output{N}/<chapter>/07_pitfalls.json
  - reference/exercise_alignment.md
  - reference/bhasha_bodh.md
  - the exercise-solutions skeleton under `schema/` (root shape restated under **Output**)
outputs:
  - output{N}/<chapter>/10_exercise_solutions.json
---

The સ્વાધ્યાય blocks are **never** teaching topics. They are answered here, in full, and nowhere
else. This is the second of the two deliverables — the run is not complete without it.

## 0. Where the prompts come from

The GSEB PDFs in `../Textbooks-pdf/std-N/` are **image-only**. There is no text layer to copy from:
every printed word in this pipeline is Agent 1's **transcription of a rendered page**, written into
`00_chapter_normalized.md` under `[[સ્વાધ્યાય: <exact printed sub-heading>]]` markers, and
inventoried into `01_meta.json`.

- Copy the prompt from `00_chapter_normalized.md`; **verify it against the render** before you write
  it down — option letters `(અ)/(બ)/(ક)` vs `(A)–(D)`, the spaced question mark
  (`તમે ઓળખી બતાવશો ?`), the colon in `…ઉત્તર લખો :`, ✓/☑/〇/△/✗ glyphs and the shape of every
  printed grid are exactly the details a transcription loses.
- A mismatch between the transcription and the page is **Agent 1's defect**. Note it in
  `teacher_note`, say so, and do not silently repair it.
- Where a std 9–10 વ્યાકરણ એકમ prints its own answer ("કેટલાક સ્વાધ્યાય કરીએ ?" … "ઉત્તર જોઈએ :"),
  record the item **and** the book's printed answer. The book outranks you.

## Cover everything

Take `exercise_inventory` from `01_meta.json` and answer **every block and every item**. The block
names are whatever THIS chapter printed — read them off the inventory, never off a remembered list:

- **Std 6–8** print no સ્વાધ્યાય banner at all. Numbered pink headings begin directly under the
  શબ્દાર્થ box; block 1 is always **વાતચીત**; the last numbered block is almost always
  **નીચેનાં વાક્યોનો તમારી પ્રથમ ભાષામાં અનુવાદ કરો.** Headings are re-worded per chapter.
- **Std 9–10** print the **સ્વાધ્યાય** banner and a fixed 3–4 tier ladder, with
  **વિદ્યાર્થી-પ્રવૃત્તિ** after it.

`reference/exercise_alignment.md` carries the measured block families per standard and the default
`skill` for each. It is a map of what to expect, **not** a substitute for the inventory: a block the
inventory records and the table does not is still answered; a block the table lists and this chapter
did not print does not exist.

Do not answer what is not a task: the blue intro box, લેખક/કવિ-પરિચય, **ભાષા-અભિવ્યક્તિ**,
**શિક્ષકની ભૂમિકા**, the શબ્દાર્થ / શબ્દ-સમજૂતી boxes and their રૂઢિપ્રયોગ / શબ્દસમૂહ માટે એક શબ્દ /
કહેવત pre-blocks, and the chapter-final green grammar boxes are printed apparatus. Agent 1 keeps them
out of `exercise_inventory`; you keep them out of `exercises[]`.

A block you skip is a hard fail at Agent 13.

## Per item

```json
{"exercise_id":"EX1","exercise_group":"વાતચીત",
 "skill":"reading comprehension|vocabulary|grammar|literary device|speaking|listening|writing|values",
 "prompt_verbatim":"<the book's EXACT Gujarati wording, options included>",
 "answer":"…","explanation":"…","acceptable_alternatives":["…"],
 "values_filled_for_teaching":"…","teacher_note":"…","is_model_answer":false,
 "covered_by_topics":["M1.S1.T1"]}
```

`EX{n}` is **our** counter, consecutive in printed order across the whole chapter — not the book's
number, which is unreliable (std-8 ch-14 jumps 5 → 7; std-8 chs 2 and 12 print two blocks numbered
"2."; std-6 ch-1 leaves its final activity un-numbered). Keep the printed number inside
`exercise_group` or `teacher_note` where it matters; never renumber the book to make it tidy.

## Rules

1. **`prompt_verbatim` is verbatim** — the exact Gujarati, including all options, exactly as
   printed: option letters, the spaced `?`, the trailing `:`, the std-10 micro-variants (લખો vs
   આપો, વાક્યમાં vs વાક્યોમાં, સવિસ્તર vs સવિસ્તાર). Full stop `.` as the readers print it — never
   a Devanagari danda. Where the book prints a wrong form **on purpose** (std-6 ch 6's child-speech
   મરવા for મળવા; R1's સહસ્ત્ર, વિધ્યાર્થી), the prompt keeps it and the repair goes in `answer`.
2. **Answer from the chapter.** `'મેહુલે માંડ્યાં મંડાણ' - એટલે શું ?` is answered by the લોકગીત's
   own lines, not by general knowledge about the monsoon. A તળપદો શબ્દ is glossed from the book's
   own શબ્દાર્થ box plus the line it stands in — see `reference/bhasha_bodh.md` on the
   printed-glossary trap.
3. **Explain the choice.** For a ✓-MCQ say why the right option is right **and** why the tempting
   wrong one is wrong — the book itself asks the child for reasons. Std-9 ch 4 asks the સાહિત્યપ્રકાર
   of 'સિંહનું મૃત્યુ': નવલકથાખંડ is right because the intro names it an extract from the novel
   'અકૂપાર'; નવલિકા tempts because the extract reads as a complete small story.
4. **Personal-opinion items get a model answer**, `is_model_answer: true`, clearly framed as one
   possible response. Never as *the* answer. This covers most of વાતચીત, every વિદ્યાર્થી-પ્રવૃત્તિ
   bullet, and open tasks like `તમારા વિસ્તારમાં બોલાતા તળપદા શબ્દોની યાદી બનાવો.`
5. **Fill the grids.** Where the book prints an empty table, matching grid or cloze,
   `values_filled_for_teaching` carries the correct values so a teacher can use the page directly:
   std-6 ch 2's જોડાક્ષર colouring table (દ્વ, દ્ધ, દ્ર, દ્દ, દ્ય, સ્ર — three words against each),
   ch 5's પહેલાં/અત્યારે/હવે પછી tense table, ch 1's word-bank ફકરો, the std-7 અ/બ કોષ્ટક.
6. **Map to topics.** `covered_by_topics` names the reading scenes that prepare the item. An
   exercise that maps to nothing — in a chapter that HAS reading text — goes in
   `coverage_report.unmapped`: **report it, do not invent a mapping.** An unmapped exercise usually
   means the cut missed a scene. Ids come from `04_converged.json` and are frozen; Agent 14
   translates them when it renumbers.
7. **Language-study items still map** — a જોડાક્ષર block maps to the ઘટના topics whose text carries
   તલ્લીન, અધ્ધર, મસ્તી; a તળપદા-શબ્દ block maps to the કડી that prints ઓતર and દખ્ખણ; a
   રૂઢિપ્રયોગ item maps to the scene where the idiom is used. Only a unit with **no reading text at
   all** maps to nothing: std 6–8 R1 "આગળ વધતાં પહેલાં" / R2 "પૂર્ણ કરતાં પહેલાં" and the std 9–10
   વ્યાકરણ એકમો route here end-to-end, produce no scenes, and every item is recorded in
   `coverage_report.unmapped` with that reason plus the chapters a revision unit revises.
8. **Respect the pitfalls.** `07_pitfalls.json` applies here too: an answer must not violate the
   સ્વરૂપ's avoid-list any more than an explanation may. A બોધ appended to a દુહો, a ભક્તિ-પદ turned
   into a morality lesson, an invented અલંકાર offered as the answer to a craft question — all as
   wrong in the solutions file as in the plan. `08_sensitivity.json` guides how a sensitive item is
   answered, never whether.

## Grammar items — answer at the standard's own level

`skill: "grammar"` items are drilled hard in these readers. Answer them in the categories GSEB
actually teaches — સંધિ, સમાસ, કૃદંત, નિપાત, રૂઢિપ્રયોગ, કહેવત, શબ્દસમૂહ માટે એક શબ્દ, પ્રયોગ
(કર્તરિ / કર્મણિ / ભાવે / પ્રેરક), સંજ્ઞા-સર્વનામ-વિશેષણ-ક્રિયાપદ, કાળ, લિંગ-વચન-વિભક્તિ,
જોડાક્ષર-જોડણી-અનુસ્વાર, વિરામચિહ્નો — and only where that standard has reached them. The measured
ladder is in `reference/exercise_alignment.md`: **સંધિ, સમાસ, કૃદંત and નિપાત do not appear at std
6**; સંધિ-સમાસ is std-10 વ્યાકરણ એકમ 2; રૂઢિપ્રયોગ-કહેવત is એકમ 3. Naming a category the child has
not been taught is the same defect as answering from outside the chapter.

Two standing calibrations:

- **The અનુવાદ block** (std 6 and 8, 15/15 chapters) asks for the child's **પ્રથમ ભાષા**, which
  varies by school. Give the model translation in the medium of instruction recorded in
  `chapter_id`, set `is_model_answer: true`, and say in `teacher_note` that a school with another
  first language substitutes it. Non-Gujarati script inside such an `answer` is expected here and
  nowhere else — flag it in `teacher_note` so Agent 13 reads it as intended, not as a script defect.
- **Std 10 answers stay inside their tier's length** — one sentence, two-three sentences, સવિસ્તર —
  because the ladder is shaped like the SSC paper and the child uses the answer as written.

The word blocks and the plan are complements, not competitors: Agent 12's `shabdarth`, `samanarthi`,
`vilom`, `vyakaran` fields **prepare** these items (`reference/bhasha_bodh.md`); you **answer** them.
Neither replaces the other, and neither may contradict the other.

## Output

`10_exercise_solutions.json`, on the exercise-solutions skeleton under `schema/`: root
`_comment`, `plan_id`, `chapter_id`, `subject`, `grade`, `chapter_name` (from `01_meta.json`),
`exercises[]` in the per-item shape above, and a `coverage_report` with `blocks_found`,
`blocks_answered`, `unanswered`, `unmapped`. `blocks_found` must equal the number of entries in
`exercise_inventory`; `unanswered` must be empty.

The orchestrator copies this file to `exercise_solutions.json` and renders the `.md` at Phase 7.

## Do not
- Create topics.
- Paraphrase a prompt, tidy its punctuation, or translate a heading into Hindi-pack wording.
- Answer from general knowledge where the chapter has the answer.
- Assume a block the inventory does not record, or skip one it does.
- Leave a વાતચીત or વિદ્યાર્થી-પ્રવૃત્તિ item unanswered because it is subjective — model it.
