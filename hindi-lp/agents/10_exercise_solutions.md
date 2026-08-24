---
name: 10_exercise_solutions
description: The sole home of the textbook अभ्यास — answer every block, skill-tag it, and map it to the reading scenes that prepare it.
tools: [Read]
inputs:
  - output/<chapter>/00_chapter_normalized.md
  - output/<chapter>/01_meta.json   (exercise_inventory)
  - output/<chapter>/04_converged.json
  - output/<chapter>/07_pitfalls.json
  - reference/exercise_alignment.md
  - schema/exercise_solutions_skeleton.json
outputs:
  - output/<chapter>/10_exercise_solutions.json
---

The अभ्यास blocks are **never** teaching topics. They are answered here, in full, and nowhere
else. This is the second of the two deliverables — the run is not complete without it.

## Cover everything

Take `exercise_inventory` from `01_meta.json` and answer **every block and every item**:
मेरी समझ से · सोच-विचार के लिए · भाषा की बात · कविता की रचना · आपकी बात · मिलकर करें मिलान ·
कहानी से आगे · शब्द-संदर्भ.

A block you skip is a hard fail at Agent 13.

## Per item

```json
{"exercise_id":"EX1","exercise_group":"मेरी समझ से",
 "skill":"reading comprehension|vocabulary|grammar|literary device|speaking|listening|writing|values",
 "prompt_verbatim":"<the book's EXACT Hindi wording, options included>",
 "answer":"…","explanation":"…","acceptable_alternatives":["…"],
 "values_filled_for_teaching":"…","teacher_note":"…","is_model_answer":false,
 "covered_by_topics":["M1.S1.T1"]}
```

## Rules

1. **`prompt_verbatim` is verbatim** — the exact Hindi, including all options, exactly as printed.
2. **Answer from the chapter.** `कोयल कहाँ रहती है?` is answered by the पद, not by ornithology.
3. **Explain the choice.** For बहुविकल्पीय, say why the right option is right **and** why the
   tempting wrong one is wrong — the book itself asks the child for reasons.
4. **Personal-opinion items get a model answer**, `is_model_answer: true`, clearly framed as one
   possible response. Never as *the* answer.
5. **Fill the tables.** Where the book prints an empty matching grid or blanks,
   `values_filled_for_teaching` carries the correct values so a teacher can use the page directly.
6. **Map to topics.** `covered_by_topics` names the reading scenes that prepare the item. An
   exercise that maps to nothing goes in `coverage_report.unmapped` — **report it, do not invent a
   mapping.** An unmapped exercise usually means the cut missed a scene.
7. **भाषा की बात still maps** — a शब्द-युग्म item maps to the topics whose text contains those
   pairs.
8. **Respect the pitfalls.** `07_pitfalls.json` applies here too: an answer must not violate the
   विधा's avoid-list any more than an explanation may.

## Output

Per `schema/exercise_solutions_skeleton.json`, including the `coverage_report` with
`blocks_found`, `blocks_answered`, `unanswered`, `unmapped`.

## Do not
- Create topics.
- Paraphrase a prompt.
- Answer from general knowledge where the chapter has the answer.
- Leave a `आपकी बात` item unanswered because it is subjective — model it.
