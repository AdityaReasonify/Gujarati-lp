# एकांकी

> Written twice, independently — once from मल्हार 8 (नए मेहमान) and गंगा 9 (रीढ़ की हड्डी), once
> from स्पर्श 10 (कारतूस) — and merged. Where the two books differ the difference is marked by
> series; everything unmarked held in all three chapters.

## Diagnosis signals

A **cast-and-setting header** before the text, then unbroken dialogue: speaker's name on the left,
their words on the right, with **stage directions in parentheses** both between and inside the
speeches — `(हँसकर)`, `(दरवाज़े की ओर देखते हुए)`, `(प्रवेश)`, *(खिड़की के पास जाकर)*.

The header's fields differ by series, and the field list is itself a diagnosis signal:

| series | header fields |
|---|---|
| मल्हार / गंगा | **पात्र-परिचय** — each character named with one phrase saying who they are (`विश्वनाथ — गृहपति`, `रेवती — विश्वनाथ की पत्नी`) — then a **स्थान** line, then a block of parenthesised prose setting the room, the hour and the weather |
| स्पर्श | **पात्र**, plus some or all of **अवधि**, **ज़माना**, **समय**, **स्थान**. `अवधि` is given in *minutes* — the text is meant to be performed, not read |

One act. No chapter breaks, no narrator, no descriptive passage that is not a stage direction.
**Everything the reader learns, they learn because a character said it aloud or because a direction
told the stage to do something.**

**Tested before `sakshatkar`, `samvad_nibandh` and `kahani`.** All four have named speakers or a
plot. The discriminators:

- **`sakshatkar`** — an interview has questions and a single answering voice, an interviewer
  eliciting testimony, and no stage. If there are stage directions, it is not an interview.
- **`samvad_nibandh`** — an essay-dialogue has two *positions* being argued. A play has
  **characters who want things and a room they are standing in**.
- **`kahani`** — a कहानी also has a plot and a turn, but it has a narrator who can tell you what a
  character felt. An एकांकी cannot. **That inability is the form.**

## Lens

**संवाद + रंग-संकेत + मोड़** — what is said, what the stage is told to do, and the turn the two
produce between them.

## Guiding question

*जो मंच पर दिखाया नहीं जा सकता, वह संवाद और रंग-संकेत से दर्शक तक कैसे पहुँचता है?*

A second form, where the chapter turns on motive rather than on staging:
*इस दृश्य में कौन क्या चाहता है, और वह किस बात से बदल जाता है?*

## Explanation unit — **one stage-beat** (दृश्य-प्रसंग / संवाद-खंड)

A beat is a stretch of the एकांकी held together by one situation, and **it ends when the stage
changes.** The stage directions are therefore the cut marks — that is what makes the unit
decidable, and it matters because many एकांकी (कारतूस among them) carry **no formal दृश्य numbering
at all**. Reading such a chapter as one undivided lump, or cutting it by page, both destroy the
shape.

In practice the boundary is almost always one of:

- **an entrance or an exit** — someone new is on stage and what can be said changes,
- **a sound or an object arriving** — hooves stop outside, a lamp is noticed, a telegram comes,
- **a change in what a character knows** — a name is heard, a mistake is realised,
- **a change in what a character wants** — patience turns to anger, hospitality to a plea.

Four rules follow, and they are the ones a generic pipeline gets wrong:

- **The header is its own topic.** पात्र / अवधि / ज़माना / समय / स्थान, plus the opening stage
  direction, go together. This is not front matter to be skipped — it is the audience's entire
  orientation delivered in six lines, and reading it is a skill. The room, the heat and the broken
  fan are the play's whole pressure, established before anyone speaks. Teach `अवधि — 5 मिनट` as
  information: this is a play short enough to perform in class.
- **Never cut mid-exchange, and never separate a speech from the direction that governs it.** If A
  asks and B answers, that pair is inside one beat; *(चिल्लाकर)* बहुत खूब। is one thing. Cutting
  between them does to a play what splitting a प्रश्न from its उत्तर does to an interview.
- **A long expository exchange stays one topic.** Two officers talking for two pages about a man
  neither has met is one beat, because nothing on the stage changes. Use the `concepts[]` layer for
  its internal turns — who the man is, what he did, why he matters — exactly as a long interview
  answer or a long पद is handled. **Do not cut it into five topics because five facts arrived.** A
  play does not get more topics for being talkative.
- **A single line can be its own topic** when a direction makes it the turn. The line that names
  the visitor, delivered as he walks out, is a beat by itself.

Do **not** cut by page, by speech count, or by character. Cut by what changes on the stage.

## Emphasise

- **रंग-संकेत are text, not formatting or stage furniture.** They carry the plot: `(पसीना पोंछते
  हुए)` carries the heat, `(प्रवेश)` is the turn itself, *(टापों की आवाज़ बहुत करीब आकर रुक जाती
  है)* is the arrival, *(दबी ज़बान से अपने आप से कहता है)* is the whole ending. Keep them inside
  `original_chunk` exactly as printed — brackets, italics and all — and say in the explanation what
  the direction tells the audience that the dialogue does not. **A plan that keeps only the spoken
  lines has deleted half the play.**
- **The exposition problem.** An एकांकी has no narrator, so everything must be spoken by someone
  who has a reason to speak it. Show the child the device: a junior officer asks *"कौन शमसुद्दौला?"*
  and the senior answers — the question exists so the audience can be told. Naming this is the
  single most transferable thing in the form.
- **Subtext — what is said versus what is meant.** A host saying `आइए, बैठिए` while wishing the
  guest would leave is the form's central pleasure. Name the gap; do not flatten it to politeness.
- **Dramatic irony — what the audience knows and a character does not.** Where the text lets the
  reader see past a character, say so plainly and let the child feel the gap. Do not spoil it
  early; teach it at the beat where it lands.
- **The closing line.** एकांकी endings are short and usually **repeat an earlier line with its
  meaning reversed**. Where a phrase returns, put the two occurrences side by side and ask what
  changed between them — the words did not.
- **The stage as a real constraint.** One room, one tent, one night, real time. Everything must
  happen in front of the audience — that is why a letter has to be read aloud and a telegram has to
  arrive. The unity is what lets five minutes hold a war.
- **Register belongs to the character.** Urdu-inflected Hindi (`अफ़साने`, `हुक्म`, `जाँबाज़`,
  `हमगोश`), a soldier's clipped speech, an officer's formality. Gloss it; never neutralise it.
- **Comic timing where it exists.** Misunderstanding, an entrance at the worst moment, a repeated
  phrase coming back. Say why it is funny; a joke explained flatly stops being one.
- **Performability.** The child is going to be asked to act this. Where a line is hard to say
  aloud, or a direction hard to stage, that is worth pointing at.

## Avoid (hard gate)

- **Supplying a narrator.** No "लेखक बताते हैं कि", no "फिर विश्वनाथ ने सोचा…", no interior states
  the text does not speak. If a character's feeling is not said aloud or shown in a direction, the
  plan does not know it.
- **Dropping the रंग-संकेत**, or paraphrasing them into narration ("then a soldier came in"). The
  commonest failure, and the one that turns the form into prose.
- **Retelling the plot in place of teaching the scene.** A summary of an एकांकी is
  indistinguishable from a summary of a कहानी — which is exactly the evidence that the form was
  lost.
- **Cutting by speech, by page, or by character** instead of by beat.
- **Attaching a शिक्षा or a tacked-on संदेश to the ending.** A play argues by putting two people in
  a tent; it resolves a situation, it does not issue a moral.
- **Treating the header as metadata** and skipping it.
- **Reassigning a line to the wrong speaker.** Names are the only cue the reader has; an error here
  corrupts the whole scene.
- **Inventing what happens offstage**, or resolving an ending the playwright left open.
- **"Correcting" the text.** A cast list that omits a speaker who appears, or a name spelled two
  ways on one page, is what the book prints — record it in `07_pitfalls.json` and keep the verbatim
  as printed (`reference/devanagari_verbatim.md`).

## Priors

**Media** — one image per beat, composed as **the stage at that moment**: who is on it, where they
are, who is entering, who is turned away, what the direction just did. Prefer the moment a
direction describes over a portrait of a speaker. The set stays consistent across the chapter's
images, because it is one room — a frame showing a different room is a wrong match no matter how
well the action fits. A collage suits this form unusually well, because entries and exits give the
panels their own order: panel १ the tent before, panel २ the arrival, panel ३ the two men alone.
Existing chapter art for an एकांकी tends to be plentiful and beat-by-beat; match on
`generation_prompt` before authoring anything.

**अभ्यास** — expect comprehension per beat and character-motive questions in both series, and
reliably a **staging task**. The block names differ:

| series | blocks to expect |
|---|---|
| मल्हार | `मिलकर करें मिलान` on character-to-trait · `अभिनय की बारी` (perform a scene) · `एकांकी की रचना` (write your own short scene) · भाषा की बात on मुहावरे and on **बल देने वाले शब्द** — emphasis words, which only exist because the text is meant to be spoken |
| स्पर्श | `योग्यता विस्तार` usually asks the class to stage it; `भाषा अध्ययन` carries real grammar, not vocabulary noticing |

Where a topic prepares the acting task, its explanation should name what an actor would need from
the line: what the character wants in that beat, who is being addressed, at what volume, moving
where.

**Language** — everyday spoken Hindi, often mid-20th-century urban, and in स्पर्श a good deal of
Urdu. Period objects (तार, आने, गज, अँगीठी) need glossing and are frequently the subject of the
chapter's own side-boxes. Gloss inside the explanation; the textbook's own bracketed glosses
(*दावत (आमंत्रण)*) are part of `original_chunk` and stay.

## Recall priors

One `remember` (who is on stage, who said it, what the direction did), one `understand` (why that
line had to be spoken aloud at all), one `analyze`, `apply` or `evaluate` (what the direction adds;
what the audience knew that the character did not; how you would play the line).
