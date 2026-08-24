---
name: 05_verbatim_attachment
description: Attach each topic's exact Gujarati-script original_chunk, draft modified_chunk, set key_terms and content types, and emit the textbook-order index.
tools: [Read, Bash]
inputs:
  - output{N}/<chapter>/04_converged.json
  - output{N}/<chapter>/00_chapter_normalized.md
  - output{N}/<chapter>/01_meta.json
  - the active genre profile(s) under profiles/genres/
  - reference/gujarati_verbatim.md
  - reference/shabd_gloss.md
outputs:
  - output{N}/<chapter>/05_with_content.json
  - output{N}/<chapter>/05b_textbook_order.json
---

You attach the text. This is the anchor everything else is built on, so it is copied — never
composed, never remembered, never tidied.

## 0. Where the text comes from

The GSEB PDFs in `../Textbooks-pdf/std-N/` are **image-only**: they carry no usable text layer, so
there is nothing to copy-paste and nothing to "extract". The verbatim in this pipeline is the
**transcription Agent 1 read off the rendered pages** and wrote into
`00_chapter_normalized.md`. That file is your source; you do not re-transcribe and you do not
improve it.

Because the transcription is a human-and-model reading of a picture, it can be wrong in ways a text
layer cannot: a dropped અનુસ્વાર, a ળ read as લ, a joined verse line. So:

- **Copy from `00_chapter_normalized.md`, verify against the render.** Before you attach a verse
  topic, open the page image for that passage and read the lines you are about to copy. Prose: spot
  check the first and last line of every chunk plus any line carrying an unusual form.
- **A mismatch is Agent 1's defect, not yours to patch.** Note it, stop, and say so. Silently
  repairing one word tells everyone downstream the transcription is trustworthy when it is not.
- The printed page is the only authority. There is **no v1 Gujarati plan and no second corpus** to
  cross-check against — do not invent a second opinion.

## 1. `original_chunk` — exact

For each topic in `04_converged.json`, copy its passage from `00_chapter_normalized.md` exactly:

- **Verse line breaks are structure.** A કડી of three lines is three lines; a દુહો's two lines are
  two lines with the caesura where printed; a ગઝલનો શેર is its two lines. Never reflow verse into a
  paragraph, never join a run-on line the page breaks.
- **માત્રા, અનુસ્વાર, ચંદ્રબિંદુ, હલંત/જોડાક્ષર as printed.** Conjuncts (`ક્ષ જ્ઞ ત્ર શ્ર દ્વ`)
  survive intact. The load-bearing distinctions here are not Hindi's — **Gujarati has no nukta**;
  what breaks a word is `ળ` ≠ `લ` (`કાળ` ≠ `કાલ`, `મૂળ` ≠ `મૂલ`), `શ`/`ષ`/`સ` (`શેર` ≠ `સેર`), and
  the presence or absence of an અનુસ્વાર (`મા` ≠ `માં`, `કઈ` ≠ `કંઈ`, `આવ્યાં` ≠ `આવ્યા`). Copy
  `ઍ`/`ઑ` in આગત words exactly where printed.
- **Punctuation as printed: `.`, never `।`.** GSEB Gujarati readers use the full stop; the
  Devanagari daṇḍa does not belong in this pack's texts — introducing one is a hard fail. Keep the
  book's spacing habits too, including the space before a question or exclamation mark
  (`તુજ વિના ધેનમાં કોણ જાશે ?`), its quotation marks, and its `—`.
- **Never correct the poet.** Archaic, dialectal and medieval forms are the text:
  `ભણે નરસૈયો` (= કહે), `બાઈ મીરાં કે` (`કે` = કહે), `સાગર મોજારે ઝુકાવીએ`, `પરસેવે ન્હાય`,
  `લો'તાં`, `મુજ`, `કેરો`, `તણો`, `નવ`, `જ્યાંહીં`, `સુણો`. They stay, and they get **explained**
  by Agent 12 — modernising them destroys the text and teaches the child something the poet did not
  write.
- **The છાપ is verse, not a label.** `ભણે નરસૈયો એનું દર્શન કરતાં કુળ એકોતેર તાર્યાં રે!`,
  `બાઈ મીરાં કે પ્રભુ ગિરિધરના ગુણ, દર્શન થકી દુઃખ ભાંગે છે.`, the ગઝલ's મક્તા with the તખલ્લુસ —
  `તમે જાળ નાખ્યા કરો રોજ 'આદિલ', પરંતુ કદીયે ન પકડાય દરિયો.` — all stay inside the line they sit
  in. Never trim a છાપ into a byline.
- **The attribution and source lines belong to the LAST topic** of the poem or piece:
  `— કવિ/લેખકનું નામ` and the book's own source note, e.g. `('મીરાંનાં શ્રેષ્ઠ પદ'માંથી)`,
  `('હરિનાં લોચનિયાં' માંથી)`. They are printed text, not metadata to move into a field.
- **Typeset refrain cues are copied as printed, never expanded.** GSEB prints refrains three ways
  and each is copied literally: a right-aligned tag beside every line (`વૃંદાવન.` in std-10's પદ;
  `– સમી સાંજની` in the લોકગીત), a shorthand repeat marker closing a કડી (`- એક જ.`, `- હો ભેરુ.`,
  `પ્રભુ હે...`), and a full refrain line written out each time (`મારું જીવન અંજલિ થાજો !`). Do not
  silently expand a shorthand into the full ટેક and do not merge a right-aligned tag into the verse
  line — if the render is ambiguous about which it is, that is a stop, not a guess.
- **Strip the `[[…]]` marker lines** — `[[કડી 2]]`, `[[ટેક]]`, `[[ઘટના: …]]`, `[[સ્વાધ્યાય: …]]`
  are scaffolding, not text. Nothing under a `[[સ્વાધ્યાય: …]]` marker is ever a topic's chunk; it
  belongs to Agent 10.
- No transliteration anywhere — not into Roman, not into Devanagari.

Set `word_count.original` from the chunk you attached.

**If you cannot read a passage cleanly off the render, stop and say so.** Do not reconstruct it,
do not fill from memory of a famous poem, do not paraphrase the gap.

## 2. `modified_chunk` — the seed, not the teaching

A plain **"શું થઈ રહ્યું છે"** restatement in simple શિષ્ટ ગુજરાતી, with the hardest words glossed
inline. Two to four sentences. It is raw material for Agent 12's `explanation`, not the explanation
itself — do not write the deeper reading, the અલંકાર, the ભાવ, or the real-life link here.

## 3. `key_terms`

3–6 per topic, `શબ્દ — અર્થ` with an em dash, chosen by `reference/shabd_gloss.md`. The taxonomy —
which also decides what *kind* of gloss each word gets:

| Kind | Gloss with | Example |
|---|---|---|
| **તત્સમ** — unchanged Sanskrit | the everyday spoken equivalent | `નિરંતર — સતત, અટક્યા વગર` |
| **તદ્ભવ** in an old or worn shape | the current માનક ગુજરાતી form | `જમના — યમુના` |
| **દેશ્ય / તળપદું** — regional, folk | the standard word, named as તળપદો શબ્દ, never as an error | `મેહુલો — વરસાદ` |
| **આગત** — ફારસી-અરબી, અંગ્રેજી | plain Gujarati; spell it as GSEB prints it | `હકીકત — સાચી વાત` · `ઇસ્પિતાલ — દવાખાનું` |
| **કાવ્ય-રૂપ** — poetic licence, જૂનાં રૂપો | say what happened and that it is લય, not a mistake | see below |

For a **કાવ્ય-રૂપ**, name it as licence explicitly:
`મોજારે — 'મોજાં વચ્ચે' માટે; કવિએ લય સાચવવા શબ્દનું રૂપ થોડું બદલ્યું છે.`
`કે — 'કહે'; મીરાંની છાપની જૂની ભાષાનું રૂપ છે, ભૂલ નથી.`

**The L2 bar sits lower — this is the rule most likely to be got wrong by habit.** This is a
દ્વિતીય-ભાષા pack: a std 6–10 GSEB learner stops on many ordinary Gujarati words a first-language
reader walks straight past. "Skip everyday words" still holds for the core the child owns from
speech (`પાણી`, `ઘર`, `માતા`, `મોટું`), but the ring above it — bookish or household-specific words
like `ભાથું`, `પરસાળ`, `છાપરું`, `પાથરણું`, `ટંક`, `નેવાં`, `પગી`, `સગડ` — **is glossed here even
though a first-language pack would not gloss it.** When in doubt at std 6–7, gloss.

Lead with words the child will **meet again** (`ઉત્સાહ`, `જવાબદારી`, `પ્રતિષ્ઠા`, `સંસ્કૃતિ`) over
one-off ornamental words. Where inside the 3–6 band a standard sits — std 6–8 high, std 9–10 lower
— is in `reference/shabd_gloss.md`; the band itself is fixed by `reference/field_shape_rules.md`.

The chapter's printed **શબ્દાર્થ** box is evidence of what the book thinks is hard, not your list:
it is written for a class that already speaks the language, it sits at the end of the chapter after
the child has already stopped, and a 35-entry box does not become a 35-item field. Pick per topic,
inside the band. `રૂઢિપ્રયોગ`/`કહેવત`/`સમાનાર્થી-વિરુદ્ધાર્થી` blocks are **not** `key_terms` — they
belong to Agent 10 and to the ભાષા-બોધ fields.

## 4. Content types

`primary_content_type` / `secondary_content_type` / `tertiary_content_type` /
`available_content_types`. A reading scene that will carry an image is `"image"` with
`available_content_types: ["image"]`; a text-only topic sets `null` and `[]`. Secondary and
tertiary are `null` unless a second medium is genuinely planned. Follow the chapter's scene list —
one image per reading scene — not a wish to fill the field.

## 5. `05b_textbook_order.json`

The order the chapter is **printed** in, as a list of topic ids:
`{"chapter_id": "...", "textbook_order": ["M1.S1.T1", "M1.S1.T2", …], "source": "printed pages
<range> read off the render"}`. For most GSEB chapters this equals the logical order — emit it
anyway, so Agent 15 has an explicit index rather than an assumption, and so its
`human_confirmation_required` flag is raised on a comparison that actually happened.

Order is the order of the **teaching text**. The reader's વ્યાકરણ એકમો, પૂરકવાચન pieces and
`આગળ વધતાં પહેલાં` revision units sit between chapters in the book; they are not this chapter's
topics and never enter this list.

## Output

`05_with_content.json` — `04_converged.json` plus `original_chunk`, `modified_chunk`,
`word_count`, `key_terms` and the four content-type fields on every topic. Ids, names, objectives
and structure are frozen: pass them through untouched.

## Do not
- Write `explanation`, `real_life_example`, summaries, recall questions, figures_of_speech, or
  media.
- Paraphrase, modernise, reflow, or transliterate any part of `original_chunk`.
- Introduce `।`, Roman, or Devanagari characters anywhere.
- Drop the attribution line, the source note, or the છાપ.
- Repair a transcription defect quietly instead of reporting it.
- Turn a `[[સ્વાધ્યાય: …]]` block into a topic's chunk.
