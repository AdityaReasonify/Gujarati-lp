---
name: 11_pagination_source
description: Record the textbook and page range for the chapter. Fails soft — never blocks the run.
tools: [Read, Bash, WebFetch]
inputs:
  - output/<chapter>/01_meta.json
  - profiles/boards/cbse_hindi.md
outputs:
  - output/<chapter>/11_pages.json
---

Fills `textbook_pages` and confirms `textbook` / `textbook_url`. **This agent never blocks.**

## Sources, in order

1. The chapter PDF itself in `book/` — printed page numbers in the header or footer are the best
   evidence.
2. `01_meta.json` (`textbook`, `textbook_url`) and `profiles/boards/cbse_hindi.md`.
3. The NCERT contents page, if the reader PDF is available.

## Output

```json
{"textbook":"मल्हार | हिन्दी पाठ्यपुस्तक | कक्षा 6",
 "textbook_url":"…","textbook_pages":"1–6",
 "source":"printed folio in the chapter PDF",
 "confidence":"high|medium|low","gaps":[]}
```

## Rules

- **Never guess a page range.** If the PDF has no printed folio and no contents page is available,
  emit `"textbook_pages": ""`, `"confidence": "low"`, and record why in `gaps`
  (`reference/no_hallucination_policy.md`).
- An empty page range is a fine outcome. A wrong one is not.
- Report the gap to Agent 13 as a **note**, never as a block.
