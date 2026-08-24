# સ્વાધ્યાય Alignment (Step 7) — the second deliverable

Two deliverables ship together: the teaching plan **and** complete સ્વાધ્યાય solutions. Never one
without the other.

## સ્વાધ્યાય is not a topic

Every GSEB ગુજરાતી (દ્વિતીય ભાષા) chapter ends with an exercise apparatus. None of it is cut into
the teaching plan.

The apparatus comes in **two regimes**, measured off rendered pages (the PDFs are image-only):

- **Std 6–8 — no printed banner.** No chapter in these three readers prints the word સ્વાધ્યાય as a
  heading. Numbered pink headings begin directly under the શબ્દાર્થ box; block 1 is always
  **વાતચીત**. The intro boxes call the block સ્વાધ્યાય, so that is the series' own name for it —
  but a pipeline that keys on a "સ્વાધ્યાય" heading finds nothing. Key on the numbered headings.
  Headings are re-worded per chapter; there is no fixed printed formula.
- **Std 9–10 — printed સ્વાધ્યાય banner, fixed ladder.** A word-apparatus block (શબ્દ-સમજૂતી and its
  sub-heads) precedes it, a fixed 3–4 tier question ladder follows it, and three named blocks come
  after it (વિદ્યાર્થી-પ્રવૃત્તિ, ભાષા-અભિવ્યક્તિ, શિક્ષકની ભૂમિકા).

Agent 1 inventories every block into `01_meta.json` as
`exercise_inventory[{group, items, verbatim_heading}]` — from the rendered page of THIS chapter,
never from the tables below. Agent 10 answers **every one**. Agent 4 checks none was cut as a topic;
Agent 13 checks none went unanswered (a skipped block is a hard fail).

### Std 6 — measured across chs 1–15 (+ R1, R2)

| Block family (typical printed heading) | Frequency | Default `skill` |
|---|---|---|
| **વાતચીત** (always block 1; 5–10 oral prompts + the standing bullet "…ચર્ચા વર્ગખંડમાં કરો.") | 15/15 | speaking |
| **નીચેના પ્રશ્નોના ઉત્તર / જવાબ લખો.** | 15/15 + R1 + R2 | reading comprehension |
| **નીચેનાં વાક્યોનો તમારી પ્રથમ ભાષામાં અનુવાદ કરો.** (5 sentences; the L2 signature block) | 15/15 | writing |
| **ઉદાહરણ મુજબ…** — derivation / pattern blocks, the workhorse ભાષા-પ્રવૃત્તિ frame | every chapter, 2–5 each | grammar or vocabulary, per item |
| **ખાલી જગ્યા પૂરો** (word-bank or paragraph cloze) | 12 chapters + R1, R2 | vocabulary |
| **વાક્યો બનાવો** (given words / word-pairs) | 10 chapters | vocabulary |
| **ખરું/ખોટું · ✓ કરો · યોગ્ય/અયોગ્ય** judgement | 8 chapters | reading comprehension |
| **જોડકાં જોડો / બે ભાગ જોડીને વાક્ય બનાવો** (અ/બ) | chs 3, 8, 9, 13, 14, 15 + R2 | reading comprehension |
| **શબ્દો આડાઅવળા → વાક્ય ફરીથી લખો** | chs 5, 6, 8, 9, 12 | grammar |
| **ઘટનાક્રમ મુજબ ગોઠવો** | chs 2, 13, 15 + R2 | reading comprehension |
| **કોણ બોલી શકે ?** (speaker attribution) | chs 6, 8, 14 | reading comprehension |
| **રેખાંકિત શબ્દને સ્થાને … જરૂરી ફેરફાર કરી ફરીથી લખો** | chs 1, 2, 3, 4 | grammar |
| **અંગ્રેજી શબ્દો શોધો** (loanword hunt) | chs 5, 9, 14 + R2 | vocabulary |
| **ચિત્રવર્ણન / ચિત્ર પરથી વાક્યો** | chs 4, 9, 14 + R1 | writing |
| **નિબંધ / ફકરો / પત્ર / સંવાદ લખો** | chs 3, 7, 8, 10, 12, 14, 15 | writing |
| **સમૂહગાન / મુખરવાચન / નાટ્યીકરણ / અભિનય** | chs 1, 2, 3, 6, 7, 10, 12, 13, 14, 15 | speaking |
| **(જૂથકાર્ય) / (જોડીકાર્ય)** tagged activities | chs 1, 4, 6, 8, 11, 12 + R1 | speaking or values, per item |
| **પુસ્તકાલય / શબ્દકોશ**-આધારિત blocks | chs 3, 6, 13 + R2 | vocabulary |
| **શ્રુતલેખન / સુલેખન** | chs 5, 6, 8 | listening / writing |

Chapter-final **grammar teaching boxes** (chs 2, 3, 4, 5, 7, 9) and **fun boxes** (ch 4's "ગાઈએ"
second poem, ch 5's humour box, ch 7's name game) are printed matter, not exercises — see
*What is not an exercise block*.

### Std 7 — measured across the 15 teaching chapters

| Block family (typical printed heading) | Frequency | Default `skill` |
|---|---|---|
| **વાતચીત** (always block 1) | 15/15 | speaking |
| **નીચેના પ્રશ્નોના ઉત્તર / જવાબ લખો.** | 15/15 | reading comprehension |
| **…તમારી પ્રથમ ભાષામાં અનુવાદ કરો.** | 10/15 (chs 1, 2, 4–9, 12, 13) | writing |
| **કૌંસમાં આપેલા શબ્દથી પ્રશ્ન બનાવો** (કોણ/ક્યારે/ક્યાં…) | 8/15 | grammar |
| **ખાલી જગ્યા પૂરો** / cloze with word bank | ~9/15 + rev | vocabulary |
| **જોડકાં જોડો.** (અ/બ; printed કોષ્ટક or કોઠા) | 5/15 | reading comprehension |
| **ઘટનાક્રમમાં ગોઠવો** (often with checkboxes) | 5/15 | reading comprehension |
| **કોણ બોલ્યું / કોણ બોલી શકે ?** | 5/15 | reading comprehension |
| **સૌથી નજીકના અર્થ સામે ખરું (✓) કરો** / વિકલ્પ પસંદ કરો ((અ)/(બ)/(ક)) | 5/15 | reading comprehension |
| **"જો … હોત તો ?"** counterfactual questions — a std-7 signature | chs 3, 6, 7, 8, 10, 12 | reading comprehension |
| **ચિત્રવર્ણન** (drawing or real photograph) | 6/15 | writing |
| **વાક્યનો વિસ્તાર કરો** (expansion ladder) | 4/15 + R2 | grammar |
| **શબ્દકોશના ક્રમમાં ગોઠવો** | 3/15 | vocabulary |
| **તળપદા શબ્દોની યાદી બનાવો** | chs 8, 9 | vocabulary |
| tongue-twisters / **સાંભળો અને બોલો** | chs 2, 8, 11 | listening |
| **નિબંધ / પત્ર / જાહેરાત / પ્રવાસ-લેખન** | chs 5, 12, 15 | writing |
| document literacy (લાઇટ બિલ, જાહેરાત, કૅલેન્ડર) | chs 13, 15 + R1, R2 | reading comprehension |
| **પ્રવૃત્તિ / જોડીકાર્ય / જૂથકાર્ય** tags | ~10/15 | speaking or values, per item |

### Std 8 — measured across the 15 regular chapters

| Block family (verbatim core wording) | Frequency | Default `skill` |
|---|---|---|
| **વાતચીત.** | 15/15, always item 1 | speaking |
| **નીચેના પ્રશ્નોના જવાબ લખો.** (chs 2, 12 split into 2.(અ) ટૂંકમાં / 2.(બ) સવિસ્તાર) | 15/15 | reading comprehension |
| **આપેલા ફકરાનું તમારી પ્રથમ ભાષામાં ભાષાંતર / અનુવાદ કરો.** — ALWAYS the last numbered item | 15/15 | writing |
| **ચર્ચા-વિચારણા** (yellow chapter-final box, 1–3 bullets) | 15/15 | speaking or values |
| **ખાલી જગ્યા પૂરો** (word-bank / option-bank) | ~10/15 | vocabulary |
| MCQ with ✓/☑ (અ/બ/ક or અ/બ/ક/ડ; ch 9 uses 〇/△, ch 12 §11 uses ✗) | chs 1, 3, 4, 6, 11, 12, 13, 15 | reading comprehension |
| **ઉદાહરણ મુજબ/પ્રમાણે વાક્યમાં ફેરફાર કરો** (પ્રયોગ, rhetorical→plain, re-expression) | chs 4, 6, 7, 9, 12 | grammar |
| **પ્રશ્નવાક્ય બનાવો** (કૌંસના શબ્દથી) | chs 3, 7, 8, 13 | grammar |
| Realia comprehension (જાહેરાત, બિલ, કંકોતરી, હેલ્પલાઇન, ટ્રાફિક ચિહ્નો) | chs 3, 6, 7, 14 | reading comprehension |
| **પાત્ર/વિષય પર મુક્ત લેખન**; ch 13 અહેવાલ 100–150 શબ્દ | chs 8, 9, 11, 13, 15 | writing |
| **અધૂરી વાર્તા પૂર્ણ કરો / મુદ્દા પરથી વાર્તા બનાવો** | chs 3, 10, 11 | writing |
| Timed reading-fluency (જોડી કાર્ય, સમય table) | chs 2, 5, 15 | speaking |
| **પ્રવૃત્તિ** | ch 1 (un-numbered), ch 7 (numbered "14.") | values or writing |

Pre-blocks under the શબ્દાર્થ box — **• રૂઢિપ્રયોગ.** (11/15), **• શબ્દસમૂહ માટે એક શબ્દ.** (8/15),
**• કહેવત.** (ch 15 only) — are glossaries, not tasks. They are apparatus (see below), and they are
where the chapter's vocabulary items get their printed answers.

### Std 9 — measured across all 31 units (inventory complete)

> The std-9 inventory is complete — `reference/corpus/std-9_inventory.md`, 31 of 31 units read off
> rendered pages, every સ્વાધ્યાય page included. The ladder below is remarkably uniform across all
> 23 literature chapters. Agent 1's per-chapter inventory is still the authority: `prompt_verbatim`
> copies what THIS chapter prints, micro-variants and all.

Printed **સ્વાધ્યાય** banner, then a near-fixed ladder:

| Printed heading (verbatim; micro-variants exist) | Frequency | Items | Default `skill` |
|---|---|---|---|
| **પ્રશ્નની નીચે આપેલા વિકલ્પોમાંથી સાચો વિકલ્પ પસંદ કરી ખરાની (✓) નિશાની કરો :** — options (A)–(D); ch 14 prints (√) | 23/23, always block 1 | 2–6 | reading comprehension |
| **કારણ આપો :** (ch 2 only) | 1/23 | 1 | reading comprehension |
| **નીચેના પ્રશ્નોના બે-ત્રણ વાક્યોમાં ઉત્તર લખો :** (ch 3 prints singular "પ્રશ્નનો"; ch 6 drops the "નીચેના પ્રશ્નોના" prefix; chs 21, 23 end "." not ":") | 23/23, always block 2 | 1–4 | reading comprehension |
| **નીચેના પ્રશ્નોના છ-સાત વાક્યોમાં ઉત્તર લખો :** (ch 2 prints "પાંચ-છ") — the long-answer form of chs 1–8 | 7/23 | 1–2 | writing |
| **નીચેના પ્રશ્નોના સવિસ્તાર ઉત્તર લખો / આપો :** — replaces છ-સાત from ch 9 onward; stems include પાત્રાલેખન કરો, રસદર્શન કરાવો, શીર્ષકની યથાર્થતા ચર્ચો | 12/23 | 1–3 | writing |
| **વિદ્યાર્થી-પ્રવૃત્તિ** — 1–4 child-addressed bullets (absent in ch 2) | 22/23 | 1–4 | speaking, writing or values |

Chs 22 and 23 print blocks 1–2 only. Before the banner: **શબ્દ-સમજૂતી** (23/23) with sub-heads
**સમાનાર્થી/શબ્દાર્થ** (23), **વિરુદ્ધાર્થી** (22; absent ch 20), **તળપદા શબ્દો** (~12),
**રૂઢિપ્રયોગ** (8), **શબ્દસમૂહ માટે એક શબ્દ** (7), **કહેવત** (chs 9, 13) — only those the chapter
needs; ch 6, pure શિષ્ટ ગદ્ય, prints no તળપદા block. After it: **ભાષા-અભિવ્યક્તિ** and
**શિક્ષકની ભૂમિકા** — neither is an exercise.

The four **વ્યાકરણ એકમો** (V1–V4) are grammar units with no literature text: their practice is woven
into the exposition and the book prints its own answers ("કેટલાક સ્વાધ્યાય કરીએ ?" … "ઉત્તર જોઈએ :").
Record the item AND the book's printed answer; never cut such a unit into topics.

### Std 10 — measured across all 29 units (inventory complete)

> The std-10 inventory is complete — `reference/corpus/std-10_inventory.md`, 29 of 29 units read
> off rendered pages, every chapter's સ્વાધ્યાય included. The banner set below held in all 18
> literature chapters with measured deviations: **ch 5 prints a 3-tier ladder with no બે-ત્રણ વાક્ય
> tier**, chs 12 and 14 print the MCQ heading as "નીચેના પ્રશ્નોમાં…", and the લખો/આપો ·
> વાક્યમાં/વાક્યોમાં · સવિસ્તર/સવિસ્તાર drift runs throughout. Agent 1's per-chapter inventory is
> still the authority.

Fixed banner set per chapter, in printed order:
**શબ્દ-સમજૂતી** · **સમાનાર્થી શબ્દો/શબ્દાર્થ** · [**તળપદા શબ્દો** | **વિરુદ્ધાર્થી શબ્દો** |
**રૂઢિપ્રયોગો** | **કહેવત** | **શબ્દસમૂહ માટે એક શબ્દ**] · **સ્વાધ્યાય** · **વિદ્યાર્થી(-)પ્રવૃત્તિ** ·
**ભાષા-અભિવ્યક્તિ** · **શિક્ષકની ભૂમિકા**.

The સ્વાધ્યાય itself is a four-tier ladder:

| Tier (verbatim; wording micro-varies) | Items | Default `skill` |
|---|---|---|
| 1. **નીચેના પ્રશ્નો સાથે આપેલા વિકલ્પોમાંથી સાચો વિકલ્પ પસંદ કરી ખરાની (✓) નિશાની કરો.** — options (a)–(d) | 2 (ch-16: 3) | reading comprehension |
| 2. **નીચેના પ્રશ્નોના એક-એક વાક્યમાં ઉત્તર લખો / આપો :** | 2 | reading comprehension |
| 3. **નીચેના પ્રશ્નોના બે-ત્રણ વાક્યમાં ઉત્તર લખો / આપો.** | 2 | reading comprehension |
| 4. **નીચેના પ્રશ્નનો સવિસ્તર / સવિસ્તાર ઉત્તર લખો.** | 1–2 | writing |
| **વિદ્યાર્થી-પ્રવૃત્તિ** — 3–4 bullets (ચિત્ર દોરો, ગાન કરો, ઇન્ટરનેટ પરથી લોકગીતો મેળવો…) | 3–4 | speaking, writing or values |

Six **વ્યાકરણ એકમો** (સમાનાર્થી-વિરુદ્ધાર્થી-જોડણી; સંધિ-સમાસ; રૂઢિપ્રયોગ-કહેવત; વાક્યપ્રકાર
કર્તરિ/કર્મણિ/ભાવે/પ્રેરક + વિશેષણ; વિરામચિહ્નો + વાર્તાલેખન; અહેવાલલેખન-સંક્ષેપીકરણ-અર્થવિસ્તાર-નિબંધલેખન)
sit between the literature chapters and follow the std-9 rule above. **SSC weighting:** the std-10
ladder is shaped like the board paper — keep each answer inside the tier's own length (one sentence
/ two-three sentences / સવિસ્તર), so a child can use it as written.

### Grammar rows — what the સ્વાધ્યાય actually drills, per standard

Language-study items are answered by Agent 10 like any other block; this ladder tells you what a
given standard's items can legitimately assume the child already has.

| Std | Grammar taught in the reader (measured, in teaching order) |
|---|---|
| 6 | જોડાક્ષર (ch 2 anchor) · સંજ્ઞા: વ્યક્તિવાચક/જાતિવાચક/સમૂહવાચક + લિંગ પ્રત્યય (ch 3) · વિશેષણ: વિકારી/અવિકારી (ch 4) · ક્રિયાપદ + ત્રણ કાળ (ch 5) · વાક્યના પ્રકારો: વિધાન/પ્રશ્નાર્થ/ઉદ્ગાર (ch 7) · વિરામચિહ્નો: અલ્પવિરામ, અવતરણચિહ્ન (ch 9) · ઉચ્ચારભેદ શ/ષ/સ, ર/ળ, ળ/ડ + વિસર્ગ (chs 4, 6) · બહુવચન · derivational suffixes (-આઈ, -ખોર, -પૂર્વક, -નાર…) · દ્વિરુક્ત અને રવાનુકારી શબ્દો · સમાનાર્થી/વિરુદ્ધાર્થી · તળપદા vs માનક · રૂઢિપ્રયોગ (chs 5–15) · શબ્દકોશ ક્રમ · પત્રલેખન. **સંધિ, સમાસ, કૃદંત, નિપાત do NOT appear at std 6.** |
| 7 | વિરામચિહ્નો, six kinds (ch 2) · સંજ્ઞા, all six types (ch 3) · લિંગ-વચન-વિભક્તિ, નામ vs નામપદ (ch 4) · સર્વનામ (ch 6) · ક્રિયાવિશેષણ (ch 8) · વાક્યના પ્રકારો, six (ch 10) · કાળ + સહાયકારક રૂપો (ch 11) · હકારવાચક-નકારવાચક રચના (ch 12) · ઉપસર્ગ-પ્રત્યય, તળપદા શબ્દો, જોડાક્ષર-hunt, દ્વિરુક્ત-રવાનુકારી, શબ્દકોશ. The spiral is explicit ("ગયા વર્ષે… શીખી ગયા છીએ") — do not re-teach std-6 ground. |
| 8 | કાળ (સંયુક્ત ક્રિયાપદ) · પ્રયોગ / voice (-થી, દ્વારા) · સંયોજક · અનુસ્વાર minimal pairs (ભાંગી/ભાગી, જંગ/જગ) · જોડાક્ષર expansion · વચન અને agreement · પ્રશ્નવાચક શબ્દો · વાક્યપ્રકાર wheel · શબ્દરચના (ઉપસર્ગ મહા-, agentive -જ્ઞ/-ક/-ચર/-પાલ) · સમાનાર્થી/વિરુદ્ધાર્થી/polysemy · વાક્યવિસ્તાર અને redundancy deletion · રૂઢિપ્રયોગ, કહેવત, શબ્દસમૂહ માટે એક શબ્દ · પ્રાસ hunts · ભાવસૂચક શબ્દો, ભાવાર્થ. |
| 9 | Grammar moves into standalone વ્યાકરણ એકમો. Measured: **એકમ 1** — સમાનાર્થી, વિરુદ્ધાર્થી, સ્વર-વ્યંજન, જોડણી (hrasva-dirgha અર્થભેદ, અનુસ્વાર minimal pairs, કોશક્રમ) · **એકમ 2** — લિંગ, વચન, અનુગ, નામયોગી, સંધિ · **એકમ 3** — વિશેષણ, ક્રિયાવિશેષણ, સંયોજક, વિરામચિહ્નો · **એકમ 4** — સમાસ, શબ્દસમૂહ માટે એક શબ્દ, રૂઢિપ્રયોગ, કહેવત. The units quote the literature chapters' own sentences as examples — cross-references for topic-mapping. |
| 10 | **એકમ 1** સમાનાર્થી, વિરુદ્ધાર્થી, જોડણી · **એકમ 2** સંધિ, સમાસ · **એકમ 3** રૂઢિપ્રયોગ, કહેવત · **એકમ 4** વાક્યપ્રકાર (કર્તરિ, કર્મણિ, ભાવે, પ્રેરક) અને વિશેષણ · **એકમ 5** વિરામચિહ્નો, વાર્તાલેખન · **એકમ 6** અહેવાલલેખન, સંક્ષેપીકરણ, અર્થવિસ્તાર, નિબંધલેખન. |

### What is not an exercise block

These are printed apparatus. They never enter `exercise_inventory`, so Agent 13 never demands an
answer for them; record them in `extraction_notes[]` so nobody hunts them twice.

- **Blue intro box** (std 6–8) and the **લેખક/કવિ-પરિચય** paragraphs (std 9–10) — teacher-addressed
  or biographical; the intro box is the best genre signal on the page, so Agent 1 reads it, but it
  is not a task.
- **શિક્ષકની ભૂમિકા** (std 9–10) — teacher imperatives (કરાવવું, વંચાવવી, રજૂ કરવા કહેવું).
- **ભાષા-અભિવ્યક્તિ** (std 9–10) — printed craft commentary with no task. It is *evidence* for
  Agent 12's craft fields, never an exercise item, and never a substitute for reading the lines.
- **શબ્દાર્થ / શબ્દ-સમજૂતી** boxes and their pre-blocks — glossaries. They feed `key_terms` and give
  vocabulary items their printed answers; see `reference/shabd_gloss.md` on the printed-glossary trap.
- **Chapter-final fun and reference boxes** — std 6 ch 4's "ગાઈએ" second poem, ch 5's humour box,
  ch 6's "ગુજરાતી શબ્દકોશ ક્રમ" chart, ch 7's name game. The "ગાઈએ" poem is appended reading matter:
  neither an exercise nor part of the main લોકગીત.
- **Chapter-final green grammar boxes** (std 6–8, e.g. "સંજ્ઞા વિશે જાણીએ") — teaching text, not
  tasks. The exercises that drill them are separate numbered blocks and ARE inventoried.

**Exercise-only units.** Std 6–8 R1 "આગળ વધતાં પહેલાં" and R2 "પૂર્ણ કરતાં પહેલાં", and the std 9–10
વ્યાકરણ એકમો, carry no reading text at all. They route to Agent 10 end-to-end. They produce no
reading scenes, so `covered_by_topics` is empty by construction — record every such item in
`coverage_report.unmapped` with the reason, and cross-reference the chapters a revision unit revises
(R1 questions cite chs 1–7 by content). Never manufacture a topic to give them a mapping.

## Per-item shape

```json
{"exercise_id": "EX1", "exercise_group": "વાતચીત",
 "skill": "reading comprehension|vocabulary|grammar|literary device|speaking|listening|writing|values",
 "prompt_verbatim": "…exact printed Gujarati wording, options included…",
 "answer": "…", "explanation": "…why this answer…",
 "acceptable_alternatives": ["…"],
 "values_filled_for_teaching": "…filled table/grid/blank values where the book leaves them empty…",
 "teacher_note": "…", "is_model_answer": false,
 "covered_by_topics": ["M1.S1.T1"]}
```

plus a `coverage_report` — `{blocks_found, blocks_answered, unanswered, unmapped}` — mapping every
block to the reading scenes that prepare it.

`EX{n}` is **our** counter, consecutive in printed order across the whole chapter. It is not the
book's number, which is unreliable: std-8 ch-14 jumps 5 → 7, std-8 chs 2 and 12 print two blocks
both numbered "2.", std-7 ch-6 prints "10." twice, std-6 ch-1 leaves the final activity un-numbered.
Keep the printed number inside `exercise_group` or `teacher_note` when it matters; never renumber
the book to make it tidy.

## Rules

1. **`prompt_verbatim` is verbatim** — the book's exact Gujarati wording, options included, punctuation
   as printed: the spaced question mark (`તમે ઓળખી બતાવશો ?`), the `(અ)/(બ)/(ક)` or `(A)–(D)` option
   letters, the colon after `…ઉત્તર લખો :`, the std-10 micro-variants (લખો vs આપો, વાક્યમાં vs
   વાક્યોમાં, સવિસ્તર vs સવિસ્તાર). Full stop `.` exactly as the readers print it — never the Devanagari danda. And where the book prints wrong forms
   **on purpose** — std-6 ch 6's child-speech passage (મરવા for મળવા), R1's misspelled conjuncts
   (સહસ્ત્ર, વિધ્યાર્થી) — the prompt keeps them exactly as printed; the repair goes in `answer`.
2. **Answer from the chapter.** The answer to `'મેહુલે માંડ્યાં મંડાણ' - એટલે શું ?` is in the
   લોકગીત's own lines, not in general knowledge about the monsoon. A તળપદો શબ્દ is glossed from the
   book's own શબ્દાર્થ box plus the line it stands in, not from a dictionary elsewhere.
3. **Explain the choice, not just the choice.** For a ✓-MCQ say why the right option is right *and*
   why the tempting wrong one is wrong. Std-9 ch 4 asks the સાહિત્યપ્રકાર of "સિંહનું મૃત્યુ"
   (નવલકથાખંડ / નવલિકા / નિબંધ / નાટક): નવલકથાખંડ is right because the intro names it an extract
   from the novel 'અકૂપાર'; નવલિકા tempts because the extract reads as a complete small story.
4. **A personal-opinion item gets a model answer, clearly marked** — `is_model_answer: true`, and the
   answer text says it is one possible response. This covers most of વાતચીત, every
   વિદ્યાર્થી-પ્રવૃત્તિ bullet, and open tasks like `તમારા વિસ્તારમાં બોલાતા તળપદા શબ્દોની યાદી બનાવો.`
   Never present such an answer as *the* answer.
5. **Fill the grids.** Where the book prints an empty table, matching grid or cloze,
   `values_filled_for_teaching` carries the correct values so a teacher can use it directly: std-6
   ch 2's જોડાક્ષર colouring table (દ્વ, દ્ધ, દ્ર, દ્દ, દ્ય, સ્ર — three words against each), ch 5's
   three-column પહેલાં/અત્યારે/હવે પછી tense table, ch 4's word-bank cloze, the std-7 અ/બ કોષ્ટક.
6. **Map to topics.** `covered_by_topics` names the reading scenes that prepare the item. An exercise
   that maps to nothing — in a chapter that HAS reading text — is a signal the cut missed a scene:
   report it in `coverage_report.unmapped`, do not invent a mapping.
7. **Language-study items still map.** A જોડાક્ષર block maps to the ઘટના topics whose text carries
   those words (તલ્લીન, અધ્ધર, મસ્તી in std-6 ch 2); a તળપદા-શબ્દ block maps to the કડી that prints
   ઓતર and દખ્ખણ; a રૂઢિપ્રયોગ item maps to the scene where the idiom is used. Only a unit with no
   reading text at all (R1/R2, વ્યાકરણ એકમો) maps to nothing, and that is recorded, not invented.

Blocks also obey Agent 7's avoid-list: an exercise answer that flattens the genre — a બોધ appended
to a દુહો, a ભક્તિ-પદ turned into a morality lesson — is as wrong in the solutions file as in the
explanation.
