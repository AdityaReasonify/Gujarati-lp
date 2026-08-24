# Devanagari Verbatim — what `original_chunk` must preserve

The verbatim passage is the anchor of every topic. In Hindi it carries risks an English pipeline
never faces, because a plausible-looking "correction" silently destroys the poet's work.

## Absolute rules

1. **No transliteration, anywhere.** `original_chunk`, `topic_name`, `key_terms`, `explanation`,
   `real_life_example`, recall prompts — all Devanagari. Roman appears only inside brackets for a
   technical term: `मानवीकरण (personification)`. A Romanised line is a hard fail.

2. **Never "fix" the poet.** Old and dialectal forms are the text:
   - `यमुन` for `यमुना`, `मातुभूमि` for `मातृभूमि`, `रघुपित` for `रघुपति` — कवि shortens or bends a
     word for **लय**. Keep it exactly, then explain it in `explanation` or `key_terms`.
   - ब्रज / अवधी / राजस्थानी forms — `नहिं`, `माखन`, `खायो`, `जिन`, `कहुँ`, `तउ` — are correct as
     printed. Do not modernise to खड़ी बोली.
   - `रहिमन`, `सूरदास` in the last line of a दोहा/पद is the poet's छाप (signature). It is part of
     the verse; never trim it.

3. **मात्राएँ, नुक़्ते, हलंत, अनुस्वार/चंद्रबिंदु are content.** `हँस` ≠ `हंस`. `ज़` ≠ `ज`.
   `क़लम` ≠ `कलम`. Copy the characters as they appear in the source, including
   `ॉ` in loanwords and `ऽ` where printed.

4. **Line breaks are structure.** A छंद's four lines are four lines. A दोहा's two lines are two
   lines with the caesura where printed. Never reflow verse into a paragraph.

5. **Keep the attribution line.** `— सोहनलाल द्विवेदी` at the end of a poem belongs to the last
   topic's `original_chunk`, not to a metadata field only.

6. **Punctuation as printed** — the `।` (पूर्ण विराम), the `?`, the quotation marks the textbook
   uses, and the `—`. Do not substitute `.` for `।`.

## Extraction from a PDF

The मल्हार PDFs are text-layer PDFs. After extraction, **check before trusting**:

- **Conjuncts and मात्राएँ survive?** Look for `क्ष त्र ज्ञ श्र द्व ट्ट` and reordered vowel signs
  (`िक` where `कि` was meant). A broken conjunct means the extraction is wrong — re-extract or
  read the page as an image; do not hand-repair one word and assume the rest is fine.
- **Verse line breaks survive?** PDF extraction often joins verse lines. Restore them from the
  page layout, not from guesswork about where a line "should" end.
- **The printed page is the only authority.** Not the text layer, and not any existing plan.
  **Both can be corrupt, and in class-6 Hindi both are.** Render the page and read it.

  This is not hypothetical. The मल्हार PDFs use a legacy font mapping whose text layer produces
  `आकाश च ूमता िै` for `आकाश चूमता है`. The v1 plans were built from that same broken layer and
  inherited its corruptions — `रघुपित` for **`रघुपति`**, `मातुभूमि` for **`मातृभूमि`**, `सुनाईं`
  for **`सुनाई`**. Each is the reordered-vowel-sign failure described above. A downstream plan
  then taught two of them to children as काव्य-रूप, which is worse than a typo: it tells a child
  the poet wrote something the poet did not write.

- **Cross-check, in the right direction.** Comparing your extraction against
  `imagebyGPT/data/.../hindi6_ch{N}_standard_v1.json` is still worth doing — a mismatch means
  **one of the two is wrong and you must go to the rendered page to find out which.** Never
  resolve a mismatch by assuming either side is right.

- **The tell.** A "poetic licence" that is really a corruption always looks like a moved or
  swapped mātrā: `ति`→`ित`, `ृ`→`ु`, `है`→`िै`. A genuine licence changes the *word*, not the
  glyph order — `यमुन` for `यमुना` drops a syllable and scans differently. If the only difference
  is where a vowel sign sits, it is an extraction bug, not the poet.

## Structural markers in `00_chapter_normalized.md`

Mark structure without altering text, one marker per line, above the block it labels:

```
[[छंद 1]]
[[दोहा 3]]
[[पद 1]]
[[घटना: पहला मैच]]
[[संवाद: पेड़ और लड़का]]
[[टेक]]
[[लेखक-परिचय]]
[[अभ्यास: मेरी समझ से]]
```

Everything under `[[अभ्यास: …]]` is inventoried for Agent 10 and **never cut as a topic**.
