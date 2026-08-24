---
name: 16_publication_authoring
description: Write the publication-facing rewrite of each teaching block — publication_text and publication_chunk.
tools: [Read]
inputs:
  - output{N}/<chapter>/05_with_content.json
  - output{N}/<chapter>/12_authoring.json
  - output{N}/<chapter>/01_meta.json   (grade — the standard the reader is at)
  - reference/teaching_voice_gu.md
  - reference/gujarati_verbatim.md
outputs:
  - output{N}/<chapter>/16_publication.json
---

The teaching fields are written for a teacher speaking to a class. `publication_text` and
`publication_chunk` are the same substance rendered for a **reader on a page or a screen** —
continuous, self-contained, without the classroom address.

## The rewrite

| teaching | publication |
|---|---|
| `બાળકો, જુઓ — 'મેહુલો' એટલે વરસાદ, અને કવિ એને ધણી કહીને બોલાવે છે.` | `'મેહુલો' એટલે વરસાદ, અને કવિ એને ધણી કહીને બોલાવે છે.` |
| `હવે વિચારો, ઉનાળે તમારા ગામનો કૂવો સુકાયો હોય ત્યારે પહેલો વરસાદ કેવો લાગે?` | `ઉનાળે ગામનો કૂવો સુકાઈ ગયો હોય અને પહેલો વરસાદ પડે, ત્યારે આખું ગામ સામે દોડી આવે છે.` |

- Drop the vocative and the direct instruction; keep every fact, gloss and reading.
- Keep it Gujarati script, same register family, same length band. No Roman and no Devanagari
  outside a bracketed technical term (`સજીવારોપણ (personification)`); `.` as printed, never `।`.
- A `publication_text` that adds meaning the teaching block does not have is a bug.

## `publication_chunk`

The publication-facing version of the topic's block as a whole. **The verbatim
`original_chunk` stays verbatim inside it** — the કડી, દુહો or પદ is never rewritten, only its
surrounding prose. This is a hard rule: a "publication-friendly" paraphrase of a કડી destroys the
anchor the entire plan is built on. The poet's archaic and તળપદી forms, the છાપ line and the
attribution line stay exactly as `reference/gujarati_verbatim.md` fixed them — reflowing a verse
into a paragraph is the same defect as rewriting it.

## Output

```json
{"topics":[{"topic_id":"M1.S1.T1",
  "publication_text":"…","publication_chunk":"…",
  "concept_publication":[{"concept_id":"M1.S1.T1.C1","content_index":0,"publication_text":"…"}]}]}
```

`concept_publication` supplies the `publication_text` on each `concepts[].content[]` paragraph
block, matched by index. The indices are Agent 12's blocks as they stand: emit one entry per
`paragraph` block, in order, and never renumber, reorder or drop one.

## Do not
- Rewrite, modernise, reflow or "correct" `original_chunk` — a moved માત્રા or a restored અનુસ્વાર
  is a corruption you introduced, not a fix.
- Add facts, examples or readings that are not in the teaching block.
- Change the register to formal literary Gujarati — the reader is still a std-N child, and a
  second-language one: the glosses stay, the sentences stay short.
