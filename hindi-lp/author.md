# author.md — why this pipeline teaches Hindi the way it does

The design-logic authority. The `reference/` files state the *mechanism*; this states the *intent*.
When they appear to conflict, fix the mechanism to serve the intent.

## TL;DR

A Hindi chapter is not a container for a सारांश and a शिक्षा. It is a **कविता, a दोहा, a पद, a
संस्मरण, a कहानी** — each a different kind of made thing, each asking to be read a different way.
The pipeline's whole job is to diagnose which one is in front of it and then teach *through* that
form: put the exact words first, explain what is happening and what it means, name the craft where
the craft is doing work, and anchor it in something an Indian eleven-year-old has actually stood
in front of. Then get out of the way and let the child answer questions.

## The five commitments

### 1. The विधा decides everything

A दोहा and a पद are not two lengths of the same thing. A दोहा is a complete argument in two lines —
a picture in the first, its turn in the second — and each दोहा in a collection is independent of
its neighbours. A पद is one sung utterance with a टेक, and splitting it destroys the voice. A छंद
of a देशभक्ति कविता belongs to a sequence and gains meaning from what came before.

Applying one "stanza-wise" rule across all three produces a plan that is wrong in a way a teacher
will not notice until the class stalls. This is why `reference/explanation_unit_map.md` is
genre-keyed and why diagnosis (`reference/genre_diagnosis.md`) runs before anything else.

### 2. The exact words come before the explanation

The child must meet the text before meeting anyone's account of it. `original_chunk` is verbatim,
first, always. In Hindi this carries a specific risk the pipeline must resist: **the text often
looks wrong when it is right.** `यमुन` for `यमुना`, `मातुभूमि`, `नहिं`, `खायो`, `रघुपित` — these
are लय and dialect, not errors. Correcting them destroys the poem and teaches the child that the
poet was careless. `reference/devanagari_verbatim.md` makes this non-negotiable.

### 3. Explain, then land it in the child's own world

Every scene gets two things after the verbatim: an `explanation` that says what is happening and
what it means, glossing hard words at the moment they appear; and **one** `real_life_example` that
connects it to a life the child recognises — गली का क्रिकेट, आम की छाँव, स्टेशन का बोर्ड,
तिरंगे का चक्र.

The example is not decoration. It is where an eleven-year-old decides whether the poem is about
anything. But it must be *one* example, *Indian*, and *inside the child's experience* — an adult's
example or a foreign one silently tells the child the text is not for them.

### 4. Name the craft only where the craft is working

अलंकार is not a checklist to complete. `मानवीकरण` in `हिमालय आकाश चूमता है` is worth naming because
seeing it changes how the line reads. A device named because a field existed teaches the child
something false about the text and trains them to hunt labels instead of reading.

`figures_of_speech: []` is a correct, complete answer. `reference/no_hallucination_policy.md` and
`reference/alankar_chhand.md` both exist to defend that.

### 5. Teaching and testing are separate deliverables

मेरी समझ से, सोच-विचार के लिए, भाषा की बात, कविता की रचना — these are where the child works
independently, and they are answered in full in `exercise_solutions.json`. They are **not** teaching
topics. Cutting them into the plan produces a plan that looks complete and teaches nothing new,
while leaving the exercises half-answered.

The teaching should *set up* the exercise: where a topic prepares a task the book will ask for,
the explanation names the skill. Model it, build it together, hand it over.

## What this pipeline exists to prevent

**सारांश + शिक्षा + प्रश्न-उत्तर.** It is the default shape of a Hindi lesson plan and it fails
every विधा equally: it flattens a पद's भाव into a moral, reduces a दोहा's दृष्टांत to its
conclusion, turns a संस्मरण into a summary, and skips the कहानी's turn. Every hard gate in
`reference/qc_checklist.md` Section D is aimed at this one failure.

## The tensions this design accepts

- **Depth against the word limit.** 55–90 words is not enough for everything a rich छंद contains.
  That is deliberate: the block is what a teacher says out loud before the class works. Depth that
  does not fit belongs in `detailed_summary` or a recall question, not in a longer explanation.
- **Faithfulness against accessibility.** Keeping `नहिं` and `माखन` is right, and it costs the
  child something. The answer is glossing at the point of use, not modernising the text.
- **The real-life anchor against the text's world.** A भक्ति पद set in ब्रज does not map neatly
  onto a class-6 life. Reach for the *feeling* — a child caught with a lie, a mother who knows —
  rather than forcing a modern equivalent of the setting.
- **One image per scene.** Some scenes want none and some want three. One is a discipline, and
  where nothing genuinely fits, an honest prompt beats a borrowed picture that half-matches.

## What would change this approach

If the runtime moves away from the per-scene block; if phase 3 lands and changes the objective
model again; if a grade band below 6 or above 8 is targeted, where the register and the depth
assumptions both shift. Until then, the five commitments above hold.
