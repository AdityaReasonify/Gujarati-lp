# अभ्यास Alignment (Step 7) — the second deliverable

Two deliverables ship together: the teaching plan **and** complete अभ्यास solutions. Never one
without the other.

## अभ्यास is not a topic

Every मल्हार chapter ends with exercise blocks. None of them is cut into the teaching plan:

| Block | What it asks |
|---|---|
| **मेरी समझ से** | बहुविकल्पीय — comprehension with reasoning |
| **सोच-विचार के लिए** | short answers found by re-reading the text |
| **भाषा की बात** | शब्द-युग्म, विलोम, पर्यायवाची, मुहावरे, निपात, संज्ञा/सर्वनाम |
| **कविता की रचना** | काव्य-कला — तुक, लय, poetic licence |
| **आपकी बात** | the child's own opinion or experience |
| **मिलकर करें मिलान** | matching |
| **कहानी से आगे / रचनात्मक** | imagination, writing, discussion |

Agent 1 inventories every block into `01_meta.json`. Agent 10 answers **every one**. Agent 4
checks none was cut as a topic; Agent 13 checks none went unanswered.

## Per-item shape

```json
{"exercise_id": "…", "exercise_group": "मेरी समझ से",
 "skill": "reading comprehension|vocabulary|grammar|literary device|speaking|listening|writing|values",
 "prompt_verbatim": "…exact wording from the book…",
 "answer": "…", "explanation": "…why this answer…",
 "acceptable_alternatives": ["…"],
 "values_filled_for_teaching": "…filled table/blank values where the book leaves them empty…",
 "teacher_note": "…", "covered_by_topics": ["M1.S1.T1"]}
```

plus a `coverage_report` mapping every block to the reading scenes that prepare it.

## Rules

1. **`prompt_verbatim` is verbatim** — the book's exact Hindi wording, options included.
2. **Answer from the chapter.** The answer to `कोयल कहाँ रहती है?` is in the पद, not in general
   knowledge about koels.
3. **Explain the choice, not just the choice.** For a बहुविकल्पीय item say why the right option is
   right *and* why the tempting wrong one is wrong — the book itself asks the child to give
   reasons.
4. **A personal-opinion item gets a model answer, clearly marked as one possible response.** Never
   present it as *the* answer.
5. **Fill the tables.** Where the book prints an empty matching or fill-in grid,
   `values_filled_for_teaching` carries the correct values so a teacher can use it directly.
6. **Map to topics.** `covered_by_topics` names the reading scenes that prepare the item. An
   exercise that maps to nothing is a signal the cut missed a scene — report it, do not invent a
   mapping.
7. **`भाषा की बात` still maps.** A शब्द-युग्म exercise maps to the topics whose text contains those
   pairs.
