# ઉખાણાં / શબ્દરમત

> Provenance: written from GSEB std-6 પૂરકવાચન 1, item 4 **ચતુર કરો વિચાર !** (printed pp. 113–118)
> — the one unit in the measured std 6–10 corpus that is printed as a *reading text* of this form —
> together with the palindrome box closing the same page (`જો જો પાછળથી ન વાંચતાં હો !`), std-6
> ch 13's `શબ્દોની ફેરકૂદરડી` box, the ઉખાણું boxes at std-6 ch 10 and std-7 ch 7, and the measured
> word-play blocks inside other chapters' સ્વાધ્યાય: std-6 ch 1 (block 12), ch 2 (block 10), ch 4
> (block 6), R1 (block 16), R2 (block 16); std-7 ch 10 (block 8), ch 14 (block 4), and the
> tongue-twister blocks at std-7 ch 2, ch 8, ch 11; std-8 ch 10 (block 9) and ch 12 (block 7). All
> quoted strings are transcriptions from rendered pages — the GSEB PDFs carry no text layer. See
> `reference/corpus/std-{6,7,8}_inventory.md`.

> ⚠ **Provisional — VERIFY-3.** Three things here are not measurement.
>
> 1. **One unit, not a form-wide sample.** In the whole measured corpus exactly one piece of this
>    form is printed as reading matter: the seven-riddle set inside std-6 P1. All five inventories are recorded
>    COMPLETE (std-10's included, every સ્વાધ્યાય read) and contain no other. Everything below that is not tied to a cited page is a
>    prior, not a measurement, and is re-checked when a second unit is confirmed.
> 2. **Routing files do not yet carry this form.** `reference/genre_diagnosis.md`'s verse branch has
>    no ઉખાણાં node — every riddle currently falls through it to `urmikavya_geet.md`, the verse
>    fallback, which is exactly the failure this profile exists to prevent. That file, plus
>    `reference/teaching_lens_map.md`, `reference/explanation_unit_map.md` and
>    `profiles/genres/_genre_index.md` (tree AND master table — `check_pack.py` enforces both
>    directions), need a row for `ukhanu_ramatgeet` when this profile is indexed.
> 3. **A boundary that must be narrowed at the same time.** `reference/genre_diagnosis.md` lists the
>    fun boxes — "humour, ઉખાણું, ગાઈએ" — under **not a genre, never diagnose these**. That is
>    correct for an appended box and stays correct. It is *not* correct for a numbered piece printed
>    as the chapter's reading text. The narrowing is stated as a hard gate below, and the two
>    statements must be made to agree in one edit, not left to contradict each other.

## Diagnosis signals

**Verse whose point is the puzzle or the sound — not a feeling, not a picture, not a story.**

Three things land here: **ઉખાણાં** (riddles, the only sub-form measured as a reading text),
**શબ્દરમત** (word-play — palindromes, syllable swaps, segmentation puns, letter-ladders,
tongue-twisters), and **તુકબંદી** (verse held together by rhyme alone, with no ભાવ and no ઘટના
underneath it — *unmeasured in this corpus; a piece diagnosed as તુકબંદી is a first, and Agent 1
should say so in `extraction_notes[]`*).

- **A blank answer-box under each piece.** This is the decisive tell and the one the whole profile
  turns on. std-6 P1 item 4 prints seven short verse-riddles, each closed by an empty box where the
  answer would go — *the page is asking the child, not telling the reader.* No other verse form in
  this corpus leaves a hole in itself.
- **The speaker is an "I" that is not a person.** `નાક ઉપર બેસે છે`, `ભેજામાં બેસે છે`,
  `રોજ રાતે આવું છું`, `પાળ્યું પંખી એક` — first-person or third-person self-description by a thing
  that never names itself. Compare a ગીત, where the "હું" is a child, a poet, or the whole class.
- **A clue that deliberately closes a door.** `વૃક્ષ ઉપર હોઉં પણ પક્ષી નથી` — the negation is not
  decoration, it is the craft: it exists to rule out the guess the earlier lines invited.
- **No author line at all.** ચતુર કરો વિચાર ! prints none, no era line, no source attribution, no
  કવિ-પરિચય. Contrast: ઊર્મિકાવ્ય-ગીત names a living or modern poet; લોકગીત prints `- લોકગીત` in the
  author slot; a પદ carries a છાપ inside the verse. An empty author slot with nothing in it at all
  is this form's normal state.
- **No ટેક, no ધ્રુવપંક્તિ, nothing that returns.** There is no refrain to track, so the whole ટેક
  machinery of `urmikavya_geet.md` — teach what the ટેક changed, or teach it once and reference it —
  has no object to act on.
- **The pieces are freely reorderable.** Nothing in the set requires the `નાક ઉપર બેસે છે` riddle to
  stand before the `રોજ રાતે આવું છું` one, or either of them to stand where it does. Shuffle them and
  the page loses nothing. This is the exact negative of `kathakavya.md`'s decisive test, where કડી four
  cannot precede કડી three because the story has already moved. **If the order matters, this is the
  wrong profile.**
- **The title addresses a solver.** `ચતુર કરો વિચાર !` is an instruction to the reader; so is
  `જો જો પાછળથી ન વાંચતાં હો !`. A ગીત's title names its subject.
- **Everyday vocabulary, with the difficulty placed nowhere.** P1 item 4's શબ્દાર્થ box is short and
  plain — શાન, અભિમાન, લાચાર, પેરી, ફૂલ, જબરું, ભેજું, તેલીબિયાં, મધુર, નકામું, ચતુર, સંદેશો, દિ.
  Nothing there is hard for its own sake; the piece hides a noun, not a vocabulary.
- **સ્વાધ્યાય tell, where the unit has one at all: solve, then make one of your own.** The measured
  reading unit has **no સ્વાધ્યાય whatsoever** (પૂરકવાચન pattern). The book's instinct is visible
  instead in the blocks that surround other chapters: std-6 ch 1 block 12
  `વિદ્યાર્થીઓનાં જૂથ પાડી, પશુ-પંખીઓનાં ઉખાણાં બનાવવાની પ્રવૃત્તિ કરાવો. (જૂથકાર્ય)` with its own
  worked example `સૌથી સુંદર પંખી છું... જવાબ - મોર`; std-6 R1 block 16
  `ઉદાહરણ મુજબ શબ્દરમત બનાવો.`; std-7 ch 14 block 4 `મને ઓળખો :`. The task is always *do it
  yourself*, never *explain the feeling*.

### Near misses — route on the tell, not on the feel

| Looks like | But is | Tell |
|---|---|---|
| **`urmikavya_geet`** — **the nearest miss, and the default landing** | short rhymed lines in a child's vocabulary, no poet's argument, printed among poems | its lens is **ચિત્ર + ભાવ + અલંકાર** and it will send the explanation hunting a ભાવ that is not in the piece. Ask: **is something being withheld?** A ગીત hides nothing — it shows you the branch, the rain, the swept શેરી. An ઉખાણું keeps its noun off the page and prints a box where the noun should be. Its ટેક rule has nothing to act on either |
| `lok_geet` | anonymity looks the same — no named poet | the author slot of a લોકગીત *prints* `- લોકગીત`, the piece is tied to an occasion (વર્ષા, લગ્ન, ગરબો, હાલરડું) and is sung in company. A riddle has no ઢાળ and no occasion; it has a solver |
| `kathakavya` | rhymed short units, animals and objects doing things, a child's world | its decisive test is order — its કડી cannot be shuffled. These pieces can, and nothing is lost. Nobody speaks to anybody; there is no ઘટના to hand from one piece to the next |
| `duha_chhappa` | two to four self-contained lines, complete on their own, no refrain | a દુહો's second line turns the first line's picture into a rule — it hands you a **conclusion**. A riddle hands you a **question** and withholds the noun. If the piece closes on a શિખામણ, route there and use that profile's hard gates |
| `duha_chhappa` (હાઈકુ) | three short lines, one image, no argument, no પ્રાસ | a હાઈકુ **shows**; an ઉખાણું **hides**. And a હાઈકુ never asks the reader for anything |
| `nibandh_atmaparak` (હાસ્યનિબંધ) | both are funny, both play with words | હાસ્ય is prose with a persona and a ટકોર aimed at somebody — a dumb habit, a pretension, the writer himself. The joke here is structural: a hidden noun, a sentence that reads the same backwards, two syllables changing places. It is aimed at nobody |

### The boundary — printed as the reading text, or printed as a fun box

The same form appears in this corpus in two completely different places, and only one of them is
ever a topic.

**Reading text → this profile.** A numbered piece inside the reading sequence, carrying the page's
own શબ્દાર્થ box: std-6 P1 item 4.

**Appended fun matter → not a topic, in this profile or any other.** The chapter-final riddle box at
std-6 ch 10 (the ગોલુ relationship puzzle) and std-7 ch 7 (the kinship ઉખાણું
`એમના સસરા અને મારા સસરા સગા બાપ-દીકરો થાય`); std-6 ch 13's `શબ્દોની ફેરકૂદરડી` pun box; the P1
palindrome box; std-7's `શબ્દસીડી` board-game page; the humour and name-game boxes. These sit beside
a *different* reading text and belong to it as apparatus. Record them in `extraction_notes[]`; where
one asks the child to do something, it goes to Agent 10 as an exercise
(`reference/exercise_alignment.md`). Never cut one as a topic and never let one change the chapter's
diagnosed સ્વરૂપ. This is the narrowing that `reference/genre_diagnosis.md`'s "not a genre" list
needs when this profile is indexed — the list stays true of boxes and stops being true of the
reading text.

## Lens

**સંકેત + રમત + અનુમાન** — the clue, the play, and the child's guess.

For a શબ્દરમત piece the middle term is the sound or the shape of the word itself; for an ઉખાણું it
is the disguise. The third term is never dropped: a topic of this form that leaves the child nothing
to do has taught the wrong thing.

## Guiding question

*આ ઉખાણું શું છુપાવે છે, અને કઈ ચાવી આપણને એની નજીક લઈ જાય છે ?*

A shape, not a text. Each chapter derives its own from its own page — what the speaker pretends to
be; which line closes the easy door; what happens to the sentence when you read it from the other
end. The derived question goes in `01_meta.json`, never copied from this file. In a mixed chapter
the guiding question belongs to the **dominant** part (`profiles/genres/_genre_index.md`, step 4),
which for std-6 P1 will not be this one.

## Explanation unit — **one ઉખાણું / one piece**

One riddle with its answer-box is one topic. Seven riddles under one printed title are **seven
topics** — each hides a different thing, and merging two because they are short destroys the only
thing either of them does. A unit may never split: a riddle's clue lines are the same puzzle and a
cut between them leaves the first half unanswerable.

**A list-shaped word-play piece is the exception, and it goes the other way.** Eight palindrome
sentences under one heading are **one** topic, because they are one trick demonstrated eight times —
`સીમા રીમા મારી માસી.`, `જો પસા સાપ જો.`, `ખારા મમરા ખા.`, `લે મનીષ નીમ લે.` teach the child exactly
one thing, and eight topics would teach it eight times. Same for a syllable-swap set (દયા/યાદ,
જગા/ગાજ, વાદ/દવા, ભલા/લાભ). The test is: **does the next item hide something new, or repeat the same
move?** New thing → own topic. Same move → same topic, with the extra items inside
`concepts[].content[]` as a `list` block.

Two pieces join **only** when the page prints them as one numbered piece — a riddle whose second
half completes a call the first half began. The merge is recorded in `extraction_notes[]` with the
printed evidence.

**Reading order is printed order.** Because the pieces are freely reorderable there is no logical
sequence to derive, so Agent 14's order is the page's order and `05b_textbook_order.json` will match
the logical traversal exactly. That is the expected outcome here, and Agent 15 raises
`{human_confirmation_required: true, …}` per `reference/phase2_contract.md` — a correct report, not a
defect. Never invent a "better" order to avoid the flag.

Markers in `00_chapter_normalized.md` follow `reference/gujarati_verbatim.md`'s scheme, one line
above the block they label: `[[ઉખાણું 1]]` … `[[ઉખાણું 7]]`, `[[શબ્દરમત: <exact printed heading>]]`.
The printed answer-box is structure: record its presence and its emptiness in `extraction_notes[]`.

## How an ઉખાણું is built, and therefore how it is taught

Four moves, in this order, on every riddle in the measured set:

1. **The disguise** — a speaker that is not a person and does not name itself (`રોજ રાતે આવું છું`).
2. **Clues that fit more than one thing** — the invitation to guess wrong.
3. **One clue that closes the door** — a negation, a contradiction or an impossible pairing
   (`વૃક્ષ ઉપર હોઉં પણ પક્ષી નથી`).
4. **The blank box** — the piece stops without its noun, on purpose.

The `explanation` follows exactly that shape and fits it comfortably inside the 55–90 word band:
name the disguise, walk one clue, name the clue that closes the door, hand the question back. There
is no fifth move, and **there is no second, deeper meaning underneath** — pretending there is one is
this profile's characteristic failure, the same one `urmikavya_geet.md` would produce by asking what
feeling the poet built. An explanation that spends its words on what the answer-object is for has
explained the play away.

`modified_chunk` (Agent 5's plain "what is happening" seed) is under the same discipline: it says
that something is describing itself without giving its name, and it does not supply the name.

## શબ્દરમત — when the play is in the word, not in the puzzle

The sound sub-form. Nothing is hidden; the pleasure is that the language does something twice.
Measured varieties, all of them in this corpus:

- **Palindromes** — `જો જો પાછળથી ન વાંચતાં હો !` (std-6 P1): the sentence reads the same from
  either end.
- **Syllable swaps** — `શબ્દોની ફેરકૂદરડી` (std-6 ch 13): દયા/યાદ, જગા/ગાજ, વાદ/દવા, ભલા/લાભ.
- **Segmentation puns** — std-8 ch 10 block 9 `નીચેનાં વાક્યો વાંચો અને વાક્ય ગમ્મત માણો.`:
  `તે મને આપો.` / `તેમને આપો.`; `આ તોરણ લીલાં છે.` / `આ તો રણ લીલાં છે.` The space is the joke.
- **Letter-building and letter-ladders** — std-6 ch 2 block 10 `શબ્દરમત :` (ક મ ળ પુ ર → કમળ, પુર,
  રકમ), ch 4 block 6 (ઉમરગામ → ગામ, રમ, ઉર, ઉમર, ગાર), R1 block 16 (ચા → ચાર → રમત → તલવાર →
  રમતિયાળ), std-7 ch 10 block 8.
- **Tongue-twisters** — std-7 ch 2 block 8 `ચાલો, થોડી જીભની કસરત કરી લઈએ...`, ch 8, ch 11.

Almost all of these are printed as exercise blocks or fun boxes, and are therefore **Agent 10's or
`extraction_notes[]`', not topics** — the boundary rule above governs, without exception. The
sub-form is documented here so that a piece printed as reading matter is taught correctly if one
appears, and so that a topic which *prepares* one of these blocks can name the play in its
`explanation`.

Where a શબ્દરમત piece is the reading text, the teaching move is: **say it aloud, both ways, before
naming anything.** The reversal is heard before the word ઊલટ is used; the swap is heard before
અક્ષર-ફેર is used. The child who has heard `ખારા મમરા ખા.` come back at them has had the lesson.

## Emphasise

- **The clue, quoted, first.** The explanation's first sentence points at a word that is actually on
  this page. `નાક ઉપર બેસે છે` — start there, not at what the answer might be.
- **The disguise, named as a disguise.** Something is speaking as though it were alive, or as though
  it were a bird, and it is not. That is the whole of the ચિત્ર this form has, and it is enough.
- **The one clue that closes the door.** `પણ પક્ષી નથી` is where the craft is. Ask the child which
  guess that line has just ruled out, and let them answer.
- **The blank box, pointed at.** The page's empty answer-space is content. A sentence of the
  explanation should say that the page is not going to tell us.
- **The sound, heard before it is named.** પ્રાસ in a તુકબંદી line, the reversal in a palindrome, the
  swap in દયા/યાદ. Say them together aloud; then — and only then — the word પ્રાસ.
- **What the child does with it.** The guess out loud, the second guess after the door-closing clue,
  the class split in two, and — the form's own closing task — one riddle of their own about
  something in this classroom.

## Avoid (hard gate)

Agent 7 instantiates each of these as a testable per-topic check in `07_pitfalls.json`; Agent 13
blocks on `severity: "hard"`; the structural ones are checked at Agent 4.

- **The answer is never given away.** Agent 7 records this topic's solution word — or `null` where
  the page prints none — as the check's subject string. That string must not appear in `topic_name`,
  `concepts[].concept_name`, `objective_text` (registry and inline mirror), `brief_summary`,
  `summary`, `key_terms`, `concept_bullets`, `important_points`, `modified_chunk`,
  `recall_questions[].prompt`, `media[].title`, `media[].description`, `media[].teaching_notes`,
  `media[].generation_prompt`, or in the **first sentence** of `explanation`. A topic that prints the
  answer in its own title has removed the piece's method and is re-authored, not patched.
- **Never state an answer the page does not print.** ચતુર કરો વિચાર ! prints an empty box after
  every riddle. Where no answer is printed, no `explanation`, `summary`, `brief_summary`,
  `detailed_summary`, `concept_bullets`, `important_points`, `real_life_example` or
  `publication_text` sentence asserts one as fact. A candidate may appear only in
  `recall_questions[].answer` or in `10_exercise_solutions.json`'s `teacher_note`, always beside the
  clue that supports it and always carrying the printed fact that the page withholds the answer
  (`is_model_answer: true`). Inventing certainty is a `reference/no_hallucination_policy.md` hard
  fail; `[]` and "the page does not say" are correct answers.
- **The guess stays with the child.** Every topic of this form has an `explanation` containing at
  least one `?`, and its **last sentence is interrogative**. An explanation that supplies the answer
  and stops has converted a puzzle into a fact.
- **No straight-faced description.** The `explanation` must (a) contain at least one word occurring
  character-for-character in this topic's `original_chunk`, and (b) name the play — at least one of
  ઉખાણું / કોયડો / રમત / ગમ્મત / છુપાવે / છેતરે / ઊંધું appears in it. An `explanation` that reads as
  an encyclopedia entry for the answer-object — what it is made of, what it is used for, how it grows
  or how it works — has failed even when every fact in it is true.
- **No બોધ, no શિખામણ.** No sentence of any prose field is an exhortation of the shape
  "આપણે … જોઈએ" or states a life lesson, unless those exact words are quoted from this topic's
  `original_chunk`. A riddle teaches nothing except its own answer; a palindrome teaches nothing at
  all. Where the chapter itself states a lesson, teach that as the book's move — nowhere else.
- **No science or general-knowledge lesson about the answer.** No fact absent from this chapter's
  printed text and its printed શબ્દાર્થ box appears in `explanation` or `real_life_example`. Where
  the likely guess is a modern object, that object's history, working, or usefulness is not this
  topic (`reference/no_hallucination_policy.md`).
- **One piece, one topic — checked at Agent 4.** The number of topics carrying an `[[ઉખાણું n]]`
  marker equals the number of pieces the page prints; no topic carries two markers and no marker is
  split across two topics. A list-shaped શબ્દરમત piece carries exactly one `[[શબ્દરમત: …]]` marker and
  exactly one topic.
- **No અલંકાર named for the field.** `[]` is a correct and complete `figures_of_speech` value for
  most topics of this form. Where the play *is* the device — a શ્લેષ, a યમક, a વર્ણાનુપ્રાસ that is
  the piece's whole point — it may be named only if `figures_of_speech[].lines` reproduces the words
  character-for-character from this topic's `original_chunk` **and** the device sits on GSEB's own
  taught ladder for this standard (`reference/alankar_chhand.md`). An invented device is a hard fail;
  hearing વર્ણાનુપ્રાસ in a tongue-twister at std 6 and not naming it is correct.
- **No author and no provenance the page does not print.** ચતુર કરો વિચાર ! prints no author line and
  no source attribution. `01_meta.json` records the absence; no topic, no `publication_text` and no
  `11_pages.json` note supplies a poet, a collector, `સંકલિત`, or the word લોકસાહિત્ય unless the page
  prints it.
- **A fun box is never a topic.** No topic's `original_chunk` may be drawn from a chapter-final
  riddle, palindrome, pun, humour, name-game or board-game box, in this profile or any other. They
  go to `extraction_notes[]`, or to Agent 10 where they ask the child something.
- **No numbers in display text.** `"પહેલા ઉખાણામાં"`, never `"ઉખાણું 1માં"` — numbers live in ids and
  provenance fields only.

## Priors

**Media** — one image per piece, and its single job is to **show a clue without showing the answer**.
Two compositions work: the misleading surface the riddle paints (the thing on the tree that is not a
bird, drawn so the guess stays open), or the guessing itself — a std-6 classroom, hands up, one
child at the board, the page's empty box visible. Never the solution object, never a composite frame
holding all the pieces at once, never a "clever child" trope standing in for the puzzle. The narrator
bar carries one exact Gujarati line **from the piece** and never the answer word; the solution string
must not appear anywhere in the media node (hard gate above). For a palindrome topic the frame shows
the sentence read from both ends — two children, one line, arrows both ways. Soft digital
watercolour, vibrant textbook illustration style, 16:9, Indian setting, `image_url: ""` with an
authored `generation_prompt` (Agent 9's reuse step is dormant — there is no Gujarati frame pool).
≤1 `2d_tool` per chapter, and this form rarely earns one.

**સ્વાધ્યાય** — the measured reading unit has **none at all**: std-6 P1 carries no exercise
apparatus of any kind. Record the empty `exercise_inventory` and say so in `extraction_notes[]`; do
not borrow blocks from a neighbouring chapter to fill it, and do not invent a "typical" set. Where a
piece of this form sits inside a chapter that does have exercises, the blocks to expect — measured,
per the inventories — are: ઉખાણાં-making and શબ્દરમત-making activities (std-6 ch 1 block 12, R1 block
16); letter-grid and letter-ladder word building (std-6 ch 2 block 10, ch 4 block 6; std-7 ch 10
block 8); `મને ઓળખો :` who-am-I items (std-7 ch 14 block 4); વાક્ય-ગમ્મત segmentation puns (std-8
ch 10 block 9, ch 12 block 7); tongue-twister reading blocks (std-7 chs 2, 8, 11; std-6 R2 block 16);
and, at std 6–7, the standing first-language translation block. A topic of this form prepares exactly
two skills and should name them in its `explanation`: **guessing from a clue**, and **making one of
your own**. Exercises are never topics — Agent 10 owns every one of them
(`reference/exercise_alignment.md`).

**Language** — plain everyday Gujarati. The piece hides a noun, not a vocabulary, so the general L2
rule that the glossing bar sits **lower** here meets its one principled exception
(`reference/shabd_gloss.md`): gloss every word that genuinely stops the child **except the word that
is the riddle's hinge**. For that word, give the printed શબ્દાર્થ gloss and nothing further, at the
point the page gives it — after the piece, not before — because a fuller gloss hands over the
answer. Elided and તળપદા forms in the measured set (`પેરી` for પહેરી, `દિ` for દિવસ) stay exactly as
printed and are explained as લય and બોલી, never corrected toward માનક ગુજરાતી
(`reference/gujarati_verbatim.md`). Sound-syllables in a nonsense or tongue-twister line are sound,
not vocabulary: do not define them and do not claim they mean anything — rhyming is their whole job.
The printed answer-box, the `!` in `ચતુર કરો વિચાર !` and the book's spaced question-mark convention
are transcribed as printed; punctuation is `.`, never `।`.

**Sensitivity** — small but real, and it lives in the guessing rather than in the content. Where the
page prints no answer, a child's alternative reading is a move in the game, not an error: no
`recall_questions[].answer`, `teacher_note` or `real_life_example` may frame a plausible guess as
wrong, and none may frame the child who does not get it as slow — the title's word ચતુર describes
the puzzle's invitation, not a sorting of the class. Riddles whose answer is a body part or a person
are read as riddles and never used to laugh at a body or at a named child
(`agents/08_sensitivity_safety.md`, `reference/global_content_rules.md`).

## Recall priors

Two to three per topic, Bloom-laddered, each with a real model answer that obeys the
never-invent-an-answer gate:

- one **remember** — which words the piece hands you (the clues, in the page's own words), or which
  sentence in the box reads the same from both ends;
- one **understand** — which guess the door-closing clue rules out, and how you can tell
  (`વૃક્ષ ઉપર હોઉં પણ પક્ષી નથી` is the model case); or what changes between દયા and યાદ;
- one **apply** or **create** — make one of your own, two lines, about something in this classroom,
  with the name hidden; or say the palindrome backwards and check whether it held. This is the form's
  own printed task (std-6 ch 1 block 12), so the third question is the point of the ladder, not
  decoration.

Every model answer names clues and reasoning. Where the page withholds the answer, the model answer
says that the page withholds it and then gives the class's best-supported guess as a guess — a real
answer, honestly bounded, which is what `reference/field_shape_rules.md` asks for and what
`reference/no_hallucination_policy.md` requires.
