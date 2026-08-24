---
name: 16_publication_authoring
description: Write the publication-facing rewrite of each teaching block — publication_text and publication_chunk.
tools: [Read]
inputs:
  - output/<chapter>/05_with_content.json
  - output/<chapter>/12_authoring.json
  - reference/teaching_voice_hi.md
  - reference/devanagari_verbatim.md
outputs:
  - output/<chapter>/16_publication.json
---

The teaching fields are written for a teacher speaking to a class. `publication_text` and
`publication_chunk` are the same substance rendered for a **reader on a page or a screen** —
continuous, self-contained, without the classroom address.

## The rewrite

| teaching | publication |
|---|---|
| "बच्चों, देखो — हिमालय एक पर्वत है, पर कवि लिखते हैं…" | "हिमालय एक पर्वत है, पर कवि लिखते हैं…" |
| "अब सोचो, कभी ट्रेन से पुल पार किया है?" | "ट्रेन से किसी लंबे पुल पर नदी पार करते हुए…" |

- Drop the vocative and the direct instruction; keep every fact, gloss and reading.
- Keep it Devanagari, same register, same length band.
- A `publication_text` that adds meaning the teaching block does not have is a bug.

## `publication_chunk`

The publication-facing version of the topic's block as a whole. **The verbatim
`original_chunk` stays verbatim inside it** — the poem is never rewritten, only its surrounding
prose. This is a hard rule: a "publication-friendly" paraphrase of a छंद destroys the anchor the
entire plan is built on.

## Output

```json
{"topics":[{"topic_id":"M1.S1.T1",
  "publication_text":"…","publication_chunk":"…",
  "concept_publication":[{"concept_id":"M1.S1.T1.C1","content_index":0,"publication_text":"…"}]}]}
```

`concept_publication` supplies the `publication_text` on each `concepts[].content[]` paragraph
block, matched by index.

## Do not
- Rewrite, modernise or reflow `original_chunk`.
- Add facts, examples or readings that are not in the teaching block.
- Change the register to formal literary Hindi — the reader is still eleven.
