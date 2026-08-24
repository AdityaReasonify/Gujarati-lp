# author.md — why this pipeline teaches Gujarati the way it does

The design-logic authority. The `reference/` files state the *mechanism*; this states the *intent*.
When they appear to conflict, fix the mechanism to serve the intent.

## TL;DR

A Gujarati chapter is not a container for a સાર and a બોધ. It is a **દુહો, a પદ, a ગઝલ, a
વાર્તા, a નિબંધ, an એકાંકી** — each a different kind of made thing, each asking to be read a
different way. The pipeline's whole job is to diagnose which one is in front of it and then teach
*through* that form: put the exact words first, explain what is happening and what it means, name
the craft where the craft is doing work, and anchor it in something a child of that standard has
actually stood in front of. Then get out of the way and let the child work the સ્વાધ્યાય.

One thing colours every decision below and separates this pack from its Hindi sibling: **the
reader meets Gujarati as a second language.**

## Who the reader is: an L2 child, std 6–10

The GSEB Gujarati (દ્વિતીય ભાષા) reader sits in front of a child in Gujarat who most likely
studies in an English or Hindi medium — a child who may speak some Gujarati at home but reads it
weakly, whose listening often runs a level ahead of their reading, and who will end std 10 as a
competent independent reader of Gujarati, not a near-native one. This is not the first-language
class 6–8 reader the Hindi pack was calibrated for, and the register cannot be copied across.
Three consequences are load-bearing:

- **The gloss bar sits lower.** An L2 child stops on words a first-language pack would wave
  through as "everyday". More words get glossed, at the point of use, in simple Gujarati —
  `reference/shabd_gloss.md` carries the thresholds.
- **Depth is parameterized by standard, never fixed.** Std 6–8 *experience* the forms — a દુહો is
  met as a two-line sting, a પદ as a song, the concrete instance always before any rule, with
  almost no labels; std 9–10 *name and analyse* — સાહિત્યપ્રકાર tags, the અલંકાર canon,
  exam-shaped answers. The std 8→9 switch is a hard stage boundary, not a gradient. The
  commitments below hold at every standard; the board profile and `reference/teaching_voice_gu.md`
  set the per-standard dials. The age anchor is the standard's own (std 6–10 ≈ ages 11–15) —
  never a fixed "eleven-year-old".
- **Every explanation is also a language encounter.** The child is acquiring Gujarati *through*
  these texts, not just reading literature *in* it. Teaching prose is simple spoken શિષ્ટ
  ગુજરાતી, short sentences, second person — and it quietly recycles the words it just glossed,
  because one meeting with a new word teaches nothing.

## The five commitments

### 1. The સ્વરૂપ (genre) decides everything

A દુહો and a પદ are not two lengths of the same thing. A દુહો is a complete argument in two
lines — a picture from ordinary life in the first, its turn into a rule in the second — and each
દુહો in a collection is independent of its neighbours. A પદ is one sung utterance with a ટેક,
and splitting it destroys the voice. A ગઝલ moves શેર by શેર, each couplet self-contained yet
strung on one રદીફ. A કડી of a ગીત or ઊર્મિકાવ્ય belongs to a sequence and gains meaning from
what came before. A વાર્તા moves by ઘટના, and its whole point is the વળાંક.

Applying one "stanza-wise" rule across all of these produces a plan that is wrong in a way a
teacher will not notice until the class stalls. This is why `reference/explanation_unit_map.md`
is genre-keyed and why diagnosis (`reference/genre_diagnosis.md`) runs before anything else.
(સ્વરૂપ is the pack's working term; the JSON field stays `genre`.)

### 2. The exact words come before the explanation

The child must meet the text before meeting anyone's account of it. `original_chunk` is verbatim,
first, always. In Gujarati this carries a specific risk the pipeline must resist: **the text often
looks wrong when it is right.** `નરસૈંયો` for નરસિંહ, `દીઠા` for જોયા, `મુજ` for મારું, `હરિ તણો`
for હરિનો, the `રે` that carries the tune — these are લય, era, and dialect, not errors. The છાપ
line ("ભણે નરસૈંયો", "મીરાં કહે") is part of the verse, not a caption to strip. Correcting any of
it destroys the poem and teaches the child that the poet was careless — a lesson an L2 child, who
already half-suspects the old language of being "broken Gujarati", absorbs fastest of all. The one
thing that *may* be broken is the PDF text layer: legacy Gujarati fonts scramble matras, and a
moved matra is corruption while a changed word is licence — the rendered printed page, never the
text layer, is the authority. `reference/gujarati_verbatim.md` makes all of this non-negotiable.

### 3. Explain, then land it in the child's own world

Every scene gets two things after the verbatim: an `explanation` that says what is happening and
what it means, glossing hard words at the moment they appear; and **one** `real_life_example` that
connects it to a life the child recognises. That child is in Gujarat, so the anchor is too —
રિસેસનો ડબ્બો, ST બસની બારી, ચોમાસાનું પહેલું ઝાપટું — drawn from the bank in
`reference/gujarat_cultural_anchors.md`.

The example is not decoration. It is where a child of that standard decides whether the poem is
about anything, and it must be *one* example, *inside that child's experience*. An adult's example
or a foreign one tells the child the text is not for them; a generic-Indian one tells them the same
thing more quietly, which is why `વરસાદ ખેતી માટે જરૂરી છે` is a failure and the ટપ-ટપ on the
school's tin roof is not. Gujarat is the default because recognition is instant there and because
the readers themselves are Gujarat-soaked; the scope stays India, and the anchor follows the text
beyond the state whenever the text points there itself.

*Whose* Gujarat is the same question one level down, and the pack's answer is: every child's. A
book whose anchors are all Amdavad, all village, all one community's festivals repeats the foreign
example's message to everyone it left out — and `ગુજરાતી = વેપારી` is the version of that failure
this pack is likeliest to write by reflex. The bank carries the spread and the method; the
commitment here is that the spread is deliberate rather than accidental.

For an L2 reader the example also does double duty: it is the second meeting with the words the
explanation just glossed, in a context the child owns.

### 4. Name the craft only where the craft is working

અલંકાર is not a checklist to complete. સજીવારોપણ in `ગિરનાર આકાશ સાથે વાતો કરે છે` is worth
naming because seeing it changes how the line reads. A device named because a field existed
teaches the child something false about the text and trains them to hunt labels instead of
reading. And naming has a grade ladder: below std 9 the craft is *noticed*, not labelled — "કઈ
પંક્તિમાં કવિ ડુંગરને જીવતો બતાવે છે?" — while std 9–10 attach the terms the board itself teaches,
and no others (`reference/alankar_chhand.md` carries the per-standard ladder).

`figures_of_speech: []` is a correct, complete answer. `reference/no_hallucination_policy.md` and
`reference/alankar_chhand.md` both exist to defend that.

### 5. Teaching and testing are separate deliverables

The સ્વાધ્યાય — its printed sub-blocks, typically of the shape નીચેના પ્રશ્નોના ઉત્તર લખો, ખાલી
જગ્યા પૂરો, જોડકાં જોડો, સમાનાર્થી-વિરુદ્ધાર્થી, રૂઢિપ્રયોગ, વાક્યપ્રયોગ, પ્રવૃત્તિ (Agent 1
inventories the actual headings per chapter from the printed page; never assume the list) — is
where the child works independently, and it is answered in full in `exercise_solutions.json`. Its
blocks are **not** teaching topics. Cutting them into the plan produces a plan that looks complete
and teaches nothing new, while leaving the exercises half-answered. GSEB's સ્વાધ્યાય weights
grammar and writing more heavily than the CBSE reader does, which makes the temptation stronger
and the mistake worse.

The teaching should *set up* the exercise: where a topic prepares a task the book will ask for,
the explanation names the skill. Model it, build it together, hand it over.

## What this pipeline exists to prevent

**સાર + બોધ + પ્રશ્નોત્તર.** It is the default shape of a language lesson plan and it fails
every સ્વરૂપ equally: it flattens a પદ's ભાવ into a moral, reduces a દુહો's દૃષ્ટાંત to its
conclusion, turns a ચરિત્ર or નિબંધ into a summary, and skips the વાર્તા's વળાંક. For an L2
child it fails twice over — it also strips out the very language encounters the child needed the
text for. Every hard gate in `reference/qc_checklist.md` Section D is aimed at this one failure.

## The tensions this design accepts

- **Depth against the word limit.** 55–90 words is not enough for everything a rich કડી contains.
  That is deliberate: the block is what a teacher says out loud before the class works. Depth that
  does not fit belongs in `detailed_summary` or a recall question, not in a longer explanation.

  > **WARNING — PROVISIONAL (VERIFY-4).** The 55–90 word explanation band and the 12–30 word
  > objective band are inherited from the first-language Hindi pack as *targets*. They have not
  > yet been re-measured against L2 GSEB std 6–10 chapters. Keep authoring to the bands, record
  > targets vs measurements separately in the board profile, and amend the bands only via the
  > design brief once the pilot measurements land.

- **Faithfulness against accessibility.** Keeping `નરસૈંયો` and `દીઠા` is right, and it costs the
  child something — for a second-language child it costs more. The answer is still glossing at the
  point of use, never modernising the text; the L2 correction is a lower gloss bar, not a cleaner
  poem.
- **The real-life anchor against the text's world.** A ભક્તિ પદ set in ગોકુળ does not map neatly
  onto a std-6 life in Gujarat. Reach for the *feeling* — a child caught with a lie, a mother who
  knows — rather than forcing a modern equivalent of the setting.
- **One image per scene.** Some scenes want none and some want three. One is a discipline, and
  where nothing genuinely fits, an honest authored prompt beats a borrowed picture that
  half-matches — literally so in this pack, where no Gujarati frame pool exists yet and every
  image is authored.

## What would change this approach

If the runtime moves away from the per-scene block; if phase 3 lands and changes the objective
model again; if the pack is pointed at first-language Gujarati or at a grade band outside 6–10,
where the register, gloss density, and depth assumptions all shift; if the VERIFY-4 measurements
force the word bands to move. Until then, the five commitments above hold.
