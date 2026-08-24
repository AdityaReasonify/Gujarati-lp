---
name: 11_pagination_source
description: Record the reader, the local source path and the printed page range for the chapter. Fails soft — never blocks the run.
tools: [Read, Bash]
inputs:
  - output{N}/<chapter>/01_meta.json
  - the chapter PDF in `book/`
  - ../Textbooks-pdf/std-N/manifest.json
  - ../Textbooks-pdf/std-N/00-front-matter.pdf   (the reader's અનુક્રમણિકા)
  - profiles/boards/gseb_gujarati.md
  - reference/no_hallucination_policy.md
outputs:
  - output{N}/<chapter>/11_pages.json
---

Fills `textbook_pages` and confirms `textbook` / `textbook_url`. **This agent never blocks.**

## 0. What "printed page" means here

The GSEB PDFs in `../Textbooks-pdf/std-N/` are **image-only**. There is no text layer, so a folio is
never *extracted* — it is **read off a page rendered with `pdftoppm`** (100 dpi is legible for body
text and page numbers; go to 150–200 dpi when a digit sits in small or tight type).

Two numbers exist for every page and they are not the same one:

- the **printed folio** — the number the book prints on the page. This is `textbook_pages`.
- the **pdf page** — the position inside our split file. This is for rendering only, and never
  goes into the plan.

`manifest.json` carries both per unit (`printed_start`, `pdf_start`, `pdf_end`), and
`profiles/boards/gseb_gujarati.md` records the per-standard offset (6: N+11, 7: N+13, 8: N+12,
9: N+4, 10: N+5). **Those are a cross-check on what you read, never a substitute for reading it.**

## Sources, in order

1. **The printed folio on the rendered pages of the chapter PDF in `book/`** — the best evidence.
   Render the first and last page of the unit and read the numbers. Chapter openers and full-page
   illustrations frequently print no folio; when an end page is blank, step inward to the nearest
   page that does print one and count only across pages you actually rendered — then say in `source`
   which pages you read and what you counted.
2. **`01_meta.json`** (`textbook`, `textbook_url`, `unit_number`), the standard's `manifest.json`
   row, and the per-std chapter tables in `profiles/boards/gseb_gujarati.md`.
3. **The reader's own અનુક્રમણિકા** — the Gujarat State Board of School Textbooks contents page,
   rendered from `../Textbooks-pdf/std-N/00-front-matter.pdf`. Where a standard's front matter has
   not been rendered yet, say that; do not assume the contents page says anything.

The order is a precedence rule, not a menu: **a folio read on the render beats the manifest row,
and the manifest row beats the contents page.** And page 1 of the render is still the proof of
WHICH chapter — a romanised filename (`ch-04-avyo-mehulo.pdf`) came out of a split, and a split can
be one unit out.

## Output

`11_pages.json`, exactly these keys:

```json
{"textbook":"ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 6",
 "textbook_url":"../Textbooks-pdf/std-6/ch-04-avyo-mehulo.pdf",
 "textbook_pages":"22–27",
 "source":"printed folio, read off renders of pdf pp. 33 and 38 of the chapter PDF",
 "confidence":"high|medium|low",
 "gaps":["textbook_url is a local path — the GSEB readers have no hosted URL"]}
```

`textbook_url` is **the local path string**. There is no hosted URL for these readers, so that
`gaps[]` line is present in every chapter of every standard — an honest gap, not a defect. Never
hand-build an `https://` address, a bucket key or a CDN string to make the field look finished.

### Grading `confidence`

| | when |
|---|---|
| `high` | both end folios read off renders **and** the `textbook` title read off a cover that has actually been read (std 6, 7 and 10 covers are confirmed in the board profile) |
| `medium` | one folio read and the other end taken from the manifest row or the offset; or the range read only off the અનુક્રમણિકા; or the title still unconfirmed (**std 8 and 9 covers have not been read** — say so in `gaps[]`) |
| `low` | no folio and no contents page rendered — `"textbook_pages": ""` and the reason in `gaps[]` |

## Rules

- **Never guess a page range.** If no folio is legible and no contents page is available, emit
  `"textbook_pages": ""`, `"confidence": "low"`, and record why in `gaps`
  (`reference/no_hallucination_policy.md`).
- **An empty page range is a fine outcome. A wrong one is not.**
- **Never publish arithmetic as a reading.** `printed_start + (pdf_end − pdf_start)` is a
  plausibility check. If it disagrees with the folio you read, **the folio wins** — record both
  numbers in `gaps` so the manifest defect can be logged in the board profile's Corrections log,
  and do not edit the manifest yourself.
- **The pdf range never enters the plan.** A std-6 chapter that renders as pdf pp. 33–38 is
  `"22–27"`, not `"33–38"`, and not `"1–6"`.
- **`textbook` is the printed cover title in Gujarati script**, copied from `01_meta.json`. If that
  standard's cover has not been read, carry what `01_meta.json` holds and gap the confirmation —
  never compose a title from the filename or the manifest.
- **Units with no printed chapter number still have folios.** વ્યાકરણ એકમો, પૂરક વાચન and the
  R1 / R2 revision blocks print page numbers like any other page: record the range. Whether such a
  unit gets a `unit_number` at all is a decision made upstream, not here.
- **Report the gap to Agent 13 as a note, never as a block.** Agent 13 folds these three fields onto
  the plan root; a `low` confidence with a stated reason travels as a note and the run continues.

## Do not
- Fetch anything from the network. Every source in this pipeline is a local file.
- Trust a text layer, a filename, a manifest title or an offset over the rendered page.
- Touch any field other than `textbook`, `textbook_url`, `textbook_pages` — or write one line of
  teaching content.
- Block. There is no failure mode of this agent that stops the run.
