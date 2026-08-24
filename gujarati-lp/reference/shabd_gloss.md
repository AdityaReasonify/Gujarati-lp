# શબ્દ-gloss — which words to explain, and how

Drives `key_terms`, the inline glossing inside `explanation`, `concept_bullets`, and the module's
`difficult_words`.

This is a **second-language** pack. The stopping-point criterion is the same mechanism as a
first-language pack, but the threshold sits **lower**: a std 6–10 GSEB learner of Gujarati as
દ્વિતીય ભાષા stops on many ordinary words a first-language reader walks past. Recalibrating that
bar — not translating a Hindi word list — is the whole job of this file.

## Which words earn a gloss

Gloss a word when the std-N child reading it **stops**. In Gujarati that happens for five reasons,
and each needs a different kind of gloss:

| Kind | Why it stops the child | Gloss with |
|---|---|---|
| **તત્સમ** — unchanged Sanskrit (`સ્તબ્ધ`, `પ્રોત્સાહન`, `નિરંતર`, `પ્રતિષ્ઠા`, `સ્થાપત્ય`) | formal register, rarely spoken at home; often જોડાક્ષર-heavy to decode | the everyday તદ્ભવ or spoken equivalent |
| **તદ્ભવ** in an old or worn shape (`ચરિતર` = ચરિત્ર, `જમના` = યમુના, `મલ્લક` = મલક, `આલને` = આપને) | familiar root, unfamiliar shape | the current માનક ગુજરાતી form |
| **દેશ્ય / તળપદું** — regional and folk words (`ઓતર` = ઉત્તર, `મેહુલો` = વરસાદ, `ધોરી` = બળદ, `અસતરી` = સ્ત્રી, `ભે` = ભય, `ઢાંઢા`, `સાંતીડું`) | never met in a textbook register; the child's own dialect may not be this one | the standard word, and name it as a તળપદો શબ્દ, not an error |
| **આગત** — ફારસી-અરબી (`મશગૂલ`, `બખ્તર`, `નસીબ`, `હકીકત`, `ફરમાન`) and અંગ્રેજી/પોર્ટુગીઝ (`ઇસ્પિતાલ`, `બાલદી`, `ગોડાઉન`, `પાવરહાઉસ`, `ગ્રિડ`) | usually known by ear, often not on the page | plain Gujarati; spell it exactly as GSEB prints it |
| **કાવ્ય-રૂપ** — poetic licence and જૂનાં રૂપો (`મોજારે` = મોજાં વચ્ચે, `તણો/તણું` = -નો/-નું, `જ્યાંહીં`, `વસીજે`, `છાંડો`, `સુણો`, `જીવન કેરા`) | looks like a spelling mistake | say it is લય, not a mistake |

Lead with words the child will **meet again** — `ઉત્સાહ`, `કુતૂહલ`, `જવાબદારી`, `પ્રતિષ્ઠા`,
`સંસ્કૃતિ`, `જિજ્ઞાસા` — over one-off ornamental words. A word that appears once in one કાવ્ય and
nowhere else in the child's reading life is a lower priority than one that will return in every
નિબંધ. For an L2 learner this rule is stronger, not weaker: their reading time is short, so every
glossed word must earn its slot.

**Skip** the words the child certainly owns — `પાણી`, `ઝાડ`, `ઘર`, `છોકરો`. Glossing those wastes
attention and signals that you are filling a field.

## The second-language recalibration

The GSEB books assume L2 themselves — a std-8 સ્વાધ્યાય item reads
"આપેલા ફકરાનો તમારી પ્રથમ ભાષામાં અનુવાદ કરો.", and every measured chapter of std 6, 7 and 8
prints a શબ્દાર્થ box. Author to that reality with a **two-ring** model:

- **Ring 1 — never gloss.** Core everyday Gujarati the std-6 L2 child has from speech: પાણી, ઘર,
  માતા, દોડવું, મોટું.
- **Ring 2 — gloss, even though a first-language pack would not.** Ordinary but bookish or
  household-specific words: `ભાથું`, `પરસાળ`, `છાપરું`, `પાથરણું`, `ટંક`, `ચાકડો`, `નેવાં`,
  `વઢવું`, `પગી`, `સગડ`. These are the words that separate this pack from its first-language
  source. When in doubt at std 6–7, gloss.
- **Ring 3 — always gloss**, with the kind of gloss its row in the table above prescribes:
  તત્સમ, તદ્ભવ-in-old-shape, દેશ્ય, આગત, કાવ્ય-રૂપ.

Gloss density by learner tier (from `PEDAGOGY.md` §2): **સહાય** — every low-frequency word gets an
inline appositive gloss plus an English equivalent; **ધોરણ** — તળપદા and new Tier-2 words glossed
inline in Gujarati, English on request; **પ્રગત** — infer-from-context first, confirm after, then
extend into the word family. **The plan is authored at the ધોરણ level**; tier adaptation is the
runtime's job, not a second set of `key_terms`.

## How many words — per-standard thresholds

> **Provisional (VERIFY-4).** The per-standard rows below are set from the measured શબ્દાર્થ boxes
> of std 6, 7 and 8 plus the PEDAGOGY vocabulary-load findings. The std-9 and std-10 rows were set
> **before** those inventories were completed; both are complete now
> (`reference/corpus/std-9_inventory.md`, `std-10_inventory.md` — every chapter's
> શબ્દ-સમજૂતી apparatus read) and the rows have **not yet been recalibrated** against them. Treat
> every number here as a target awaiting measurement, record targets and measurements separately,
> and reconcile through the board profile — never by silently editing this table. The contract bands (`key_terms` 3–6 per topic, `difficult_words` 5–10 per module) are
> fixed by `reference/field_shape_rules.md` and are NOT provisional; these rows only say where
> inside those bands each standard sits.

| Std | `key_terms` per topic (band 3–6) | module `difficult_words` (band 5–10) | taught in depth per topic | inline glosses inside `explanation` |
|---|---|---|---|---|
| 6 | 4–6 — sit high in the band | 6–8 | 2 | 2–3, appositive form |
| 7 | 4–6 | 6–8 | 2–3 | 2–3 |
| 8 | 4–6 | 7–9 | 2–3 | 2–3 |
| 9 | 3–5 | 7–10 | 2–3 | 2, infer-first on about half |
| 10 | 3–5 | 8–10 | 2–3 | 2, infer-first; તત્સમ/જોડાક્ષર words pre-broken (સ્ + ત = સ્ત) |

Two numbers, not one: `key_terms` is a **recognition** list the child can lean on; only **2–3** of
them get the full teaching routine (meaning, example, use, revisit) in any one topic. Listing six
and teaching six is the failure mode.

Measured basis, for honesty about how thin it is: where the corpus inventories transcribe the box
contents, std-6 શબ્દાર્થ boxes carry roughly 8–17 entries (typically ≈9–13) and std-7 boxes
roughly 6–40 (typically ≈14, with the medieval કથાકાવ્ય an outlier at ~35–40). Std-8 boxes are
transcribed for a subset only (≈10–24). **The book glosses a chapter; a topic is smaller than a
chapter** — never inherit the box size as the topic count.

## Script-level stopping points — ળ/લ, શ/ષ/સ, અનુસ્વાર

Gujarati has **no nukta** in normal use; there is no nukta-dot distinction of the kind Hindi
preserves in its Perso-Arabic loans, so no such pair survives the port. The
distinctions that actually stop an L2 child — and that a careless author actually breaks — are
these three. All of them are verbatim-fidelity matters first (`reference/gujarati_verbatim.md`),
gloss matters second:

- **ળ vs લ** is lexical, never optional: `કાળ` (સમય) ≠ `કાલ` (આવતીકાલ/ગઈકાલ), `મૂળ` (જડ) ≠ `મૂલ`
  (કિંમત), `વાળ` (કેશ) ≠ `વાલ` (કઠોળ). GSEB's own dictionary-order box states the rule that helps
  a child: "ળ થી શરૂ થતા કોઈ શબ્દો નથી" — ળ never opens a word. If a text-layer extraction turns
  ળ into લ, that is a corruption to fix against the rendered page, not a variant to gloss.
- **શ / ષ / સ** — `શેર` (વજનનું માપ) ≠ `સેર` (ધાર), `શાલ` ≠ `સાલ`, `કેશ` ≠ `કેસ`. Rule of thumb
  worth giving the child once: **ષ lives almost only in તત્સમ words** (પુરુષ, વર્ષ, ભાષા, દોષ), so
  a ષ on the page is usually a signal that the word is a Sanskrit borrowing — which is also the
  clue to how it should be glossed.
- **અનુસ્વાર is content, not decoration**: `મા` (માતા) ≠ `માં` (અંદર), `કઈ` (which) ≠ `કંઈ`
  (something), and it carries grammar — `બહેનો આવ્યાં` vs `ભાઈઓ આવ્યા`. Never add an અનુસ્વાર to
  regularise a poet's line and never drop one the page prints. Same discipline for ચંદ્રબિંદુ.
- Related, and a real L2 stumble: `ઇ/ઈ` and `ઉ/ઊ` length in જોડણી. GSEB teaches જોડણી as its own
  વ્યાકરણ unit at std 9–10, so a gloss may **note** the spelling but the correction drill belongs
  to `reference/bhasha_bodh.md` and Agent 10, not to `key_terms`.

The standard-form target throughout is **માનક / શિષ્ટ ગુજરાતી** — the register the child is being
taught to write. Glossing towards it is teaching; rewriting the text towards it is a defect.

## How to write the gloss

- **Student-friendly and concrete, never dictionary-style.**
  `સુકાન — વહાણની દિશા બદલવાનું સાધન; અહીં જીવન પોતાના હાથે ચલાવવાની વાત છે.` — good.
  `સુકાન — નૌકાસંચાલનનું દિશાનિર્ધારક ઉપકરણ.` — useless to a std-7 L2 child.
- **Gloss at the point of use** inside `explanation`, the moment the word appears — not in a list
  the child must scroll back to.
- Follow the book's own best habit: GSEB boxes mark sense-in-context with `(અહીં)` —
  `શિક્ષા ((અહીં) સજા)`, `સેર ((અહીં) ધાર)`, `ગિરિવર — પર્વત; અહીં હિમાલય.` Gloss the sense **this
  passage** uses, not the word's full range.
- `key_terms` entries use the form `શબ્દ — અર્થ`, em dash, 3–6 per topic.
- `concept_bullets` / `important_points` lead with the keyword, e.g.
  `તળપદો શબ્દ — રોજિંદી બોલીનો શબ્દ, જે ગામ પ્રમાણે બદલાય.`
- For an **આગત** word, name the source only when it helps the child hold it —
  `ઇસ્પિતાલ — દવાખાનું` is enough at std 6; the etymology is not the lesson.
- For a **કાવ્ય-રૂપ**, say what happened and why:
  `'મોજારે' અહીં 'મોજાં વચ્ચે' માટે આવ્યું છે — કવિએ લય સાચવવા શબ્દનું રૂપ થોડું બદલ્યું છે.`
  The same sentence shape serves જૂનાં રૂપો — `તણો` = `-નો`, `જ્યાંહીં` = `જ્યાં` — which the
  GSEB books explicitly ask the class to notice ("જૂના શબ્દો તરફ ધ્યાન દોરવું").
- Never gloss by "fixing" the poet, and never mark a દેશ્ય or medieval form as wrong. See
  `reference/gujarati_verbatim.md`; voice and sentence length per `reference/teaching_voice_gu.md`.

## The trap

A GSEB chapter almost always prints its own **શબ્દાર્થ** box — and often a boxed રૂઢિપ્રયોગ or
કહેવત block beside it. Use the box as evidence of what the book thinks is hard, but:

- **Do not copy it in place of glossing at point of use.** It sits at the chapter's end (or top),
  after the child has already stopped.
- **Do not assume it is complete.** It is written for a class that already speaks the language; the
  Ring-2 words that stop an L2 reader are exactly the ones it leaves out.
- **Do not empty it into `key_terms`.** A 35-entry box does not become a 35-item field; pick per
  topic, inside the band.
- **રૂઢિપ્રયોગ / કહેવત / સમાનાર્થી-વિરુદ્ધાર્થી blocks are not `key_terms`.** They belong to
  `reference/bhasha_bodh.md` (`shabdarth`, `samanarthi`, `vilom`, `vyakaran`) and to Agent 10's
  સ્વાધ્યાય answers.

The child's stopping point, not the printed list, decides.
