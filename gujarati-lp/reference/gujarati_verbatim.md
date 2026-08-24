# Gujarati Verbatim — what `original_chunk` must preserve

The verbatim passage is the anchor of every topic. In Gujarati it carries risks an English pipeline
never faces, because a plausible-looking "correction" silently destroys the poet's work.

## Absolute rules

1. **No transliteration, anywhere.** `original_chunk`, `topic_name`, `key_terms`, `explanation`,
   `real_life_example`, recall prompts — all Gujarati script (Unicode U+0A80–U+0AFF). Roman appears
   only inside brackets for a technical term: `સજીવારોપણ (personification)`. Devanagari is equally
   forbidden outside such brackets — a Hindi-script or Romanised line is a hard fail.

2. **Never "fix" the poet.** Archaic, dialectal, and medieval forms are the text:
   - Old Gujarati orthography and word-forms — `મ્હારે` for `મારે`, `ત્હારે` for `તારે`, shortened
     or bent words the કવિ uses for **લય** and metre. Keep them exactly as printed, then explain
     them in `explanation` or `key_terms`.
   - સૌરાષ્ટ્રી / ચારણી / medieval forms in નરસિંહ, મીરાં, અખો and other old poets are correct as
     printed. Do not modernise them to માનક/શિષ્ટ ગુજરાતી.
   - `ભણે નરસૈંયો`, `મીરાં કહે` in the closing line of a પદ/દુહો is the poet's છાપ (signature).
     It is part of the verse; never trim it.

3. **માત્રા, અનુસ્વાર, ચંદ્રબિંદુ, હલંત/જોડાક્ષર are content.** Conjuncts like `ક્ષ જ્ઞ ત્ર શ્ર દ્વ`
   must survive intact. Gujarati has **no nukta** in normal use — the load-bearing distinctions
   are different ones: `ળ` ≠ `લ`, `શ`/`ષ`/`સ` are three different letters, and the presence or
   absence of anusvāra changes the word. Copy `ઍ`/`ઑ` in આગત (loan) words exactly where printed.

4. **Line breaks are structure.** A કડી's lines are that many lines. A દુહો's two lines are two
   lines with the caesura where printed. Never reflow verse into a paragraph.

5. **Keep the attribution line.** `— કવિ/લેખકનું નામ` at the end of a poem belongs to the last
   topic's `original_chunk`, not to a metadata field only.

6. **Punctuation as printed.** GSEB Gujarati readers use the `.` full stop — **never introduce
   `।` (the Devanagari daṇḍa); it does not belong in this pack's texts.** Keep the `?`, the
   quotation marks the textbook uses, and the `—` exactly as the page prints them.

## Extraction from a PDF

The chapter sources are **local PDFs** in `../Textbooks-pdf/std-N/` (resolved via
`profiles/boards/gseb_gujarati.md`). After extraction, **check before trusting**:

- **Conjuncts and માત્રા survive?** Look for `ક્ષ ત્ર જ્ઞ શ્ર દ્વ` and reordered vowel signs
  (`િક` where `કિ` was meant — the ઇ-માત્રા sitting after the consonant instead of before it in
  the byte stream, or detached from it entirely, e.g. `છ ે` for `છે`). A broken conjunct means
  the extraction is wrong — re-extract or read the page as an image; do not hand-repair one word
  and assume the rest is fine.
- **Verse line breaks survive?** PDF extraction often joins verse lines. Restore them from the
  page layout, not from guesswork about where a line "should" end.
- **The rendered printed page is the only authority.** Not the text layer. Gujarati textbook PDFs
  set in legacy fonts (the Shruti/Saumil/Terafont class) are known to produce reordered and
  detached vowel signs in their text layers — the same failure family that, in the Hindi pack,
  ended with a plan teaching extraction bugs to children as poetic forms, which is worse than a
  typo: it tells a child the poet wrote something the poet did not write. Render the page and
  read it.

  > **The defect catalogue is built** — from the Stage-0 inventory, recorded in
  > `profiles/boards/gseb_gujarati.md` §The text layer, never assumed from the Hindi pack's
  > catalog. Its headline finding simplifies this whole section: **all five GSEB books are
  > image-only — no text layer exists at all**, so every "extraction" in this pack is a
  > transcription from a rendered page, and the catalogue's entries are layout traps (the મેં/में
  > glyph, two-column verse, refrain shorthands, letter-spaced verse, QR intrusions), not
  > text-layer corruptions. The legacy-font warnings above still apply to any *future* source
  > that does carry a text layer; the catalogue will grow as chapters are run.

  There is **no v1 plan corpus for Gujarati** — no existing plan to cross-check against, and
  nothing to inherit corruptions from. The rendered page is the sole authority; a second opinion
  does not exist, so do not invent one.

- **The tell.** A "poetic licence" that is really a corruption always looks like a moved,
  swapped, or detached માત્રા: `કિ`→`િક`, `છે`→`છ ે`, an anusvāra jumping to the wrong letter.
  A genuine licence changes the *word* — `મ્હારે` for `મારે` is a different spelling the poet
  chose, and archaic forms change the word or its syllable count and scan differently. If the
  only difference is where a vowel sign sits, it is an extraction bug, not the poet.

## Structural markers in `00_chapter_normalized.md`

Mark structure without altering text, one marker per line, above the block it labels:

```
[[કડી 1]]
[[દુહો 3]]
[[પદ 1]]
[[ટેક]]
[[ઘટના: પહેલો મેળો]]
[[સંવાદ: વડ અને છોકરો]]
[[કવિ-પરિચય]]
[[લેખક-પરિચય]]
[[સ્વાધ્યાય: નીચેના પ્રશ્નોના ઉત્તર લખો]]
```

Markers are scaffolding — they never appear inside a text line, and they are **stripped before
anything is copied into `original_chunk`**. The `[[સ્વાધ્યાય: …]]` heading is the exact printed
sub-heading, not a normalised label. Everything under `[[સ્વાધ્યાય: …]]` is inventoried for
Agent 10 and **never cut as a topic**.
