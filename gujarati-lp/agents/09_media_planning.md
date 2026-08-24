---
name: 09_media_planning
description: Plan one image per reading scene — in this pack every scene gets an authored, self-contained generation_prompt, because no Gujarati frame pool exists. At most one 2d_tool per chapter.
tools: [Read, Bash]
inputs:
  - output{N}/<chapter>/04_converged.json
  - output{N}/<chapter>/05_with_content.json
  - output{N}/<chapter>/07_pitfalls.json   (the સ્વરૂપ's media gate, already instantiated per topic)
  - the active genre profile(s) under profiles/genres/
  - reference/field_shape_rules.md
  - reference/phase2_contract.md
  - reference/no_hallucination_policy.md
  - reference/gujarat_cultural_anchors.md   (the visual-world bank; supplies material, changes no rule)
outputs:
  - output{N}/<chapter>/09_media.json
---

**One image per reading scene. At most one interactive `2d_tool` in the whole chapter.**
Media ids are **concept-scoped**: `{concept_id}.IMG{n}` — `M1.S1.T1.C1.IMG1`. A topic-scoped id
(`M1.S1.T1.IMG1`) is rejected by the server, and concept numbering runs chapter-continuous, so the
third topic's concept is `.C3` and its image is `M1.S2.T3.C3.IMG1`. The full node shape is in
`reference/phase2_contract.md`; every key is written, none is invented.

A reading scene is a topic that carries text a child reads — a કડી, a દુહો, a પદ, an ઘટના, a
stage-beat. સ્વાધ્યાય blocks are not topics and get no media. Tier-keyed picture and audio support
for a struggling reader belongs to the tutor runtime, not to this plan; the media *count* rules
above are contract at every tier.

## Step 1 — reuse: **dormant in this pack**

There is no Gujarati frame pool. No v1 Gujarati plan corpus exists, no rendered frame library, no
shipped `[reused frame: …]` stamps to seed from (`reference/collage_media.md`). So step 1 does
nothing, and does it explicitly:

- every scene gets `image_url: ""` **and** a real, authored, self-contained `generation_prompt`;
- `reuse_report` is still emitted, with `reused: 0`, `authored` equal to `scenes`, `rejected: []`;
- no scoring machinery is imported. The parallel Hindi pack's scorer tokenizes Devanagari and reads
  a CBSE frame pool — both inapplicable here, and there is nothing to score in any case.

**Never borrow a Hindi or CBSE frame** to fill the gap. Wrong chapter, wrong text, and a narrator
bar in the wrong script — a Devanagari line inside a Gujarati plan is a defect the QC gate names.

### What survives as doctrine, for the day a pool exists

Three rules outlive the dormancy. They were paid for once, in production, in the parallel pack; they
are recorded here so the first Gujarati reuse pass starts from the finished discipline.

1. **Match only within the same chapter.** Never borrow across chapters. A frame drawn for another
   chapter depicts another text.
2. **A high score in a big pool is not evidence.** A topic about a bamboo stick game scored 0.464
   against hockey frames, while a topic scoring on frames drawn *for it* scored 0.260 — because a
   maximum over 56 candidates beats a maximum over 12 regardless of subject.
3. **The one-sentence depiction test.** Accept a reuse only when you can state, in one sentence,
   what in the frame depicts what in the scene. If you cannot, it is not a match.

On a future match the node would carry the URL, an empty prompt, and the provenance stamp:

```json
{"image_url": "<the returned publicUrl>", "generation_prompt": "",
 "teaching_notes": "…ચિત્ર કઈ રીતે વાપરવું… [reused frame: M1.S1.T2.C2.IMG1]"}
```

The bracketed stamp stays **English inside the brackets** — the collage tooling parses it by regex.
Until a pool exists, that shape must not appear in any `09_media.json`: a non-empty `image_url` in
this pack is a fabricated URL.

## Step 2 — author the prompt (here, the only step)

```json
{"image_url": "", "generation_prompt": "<self-contained>", "negative_prompt": "<…>"}
```

The prompt is read by an image model with **no other context**. It must carry the setting, the
characters and their fixed appearance, the action, the mood and the style by itself. Never write
"the same character as before", "the previous scene", "કડી 2", or the chapter's name — the model
cannot see any of that, and a recurring figure is held constant by **repeating the same appearance
sentence** in every prompt of the chapter, not by referring back.

Standing conventions (`reference/field_shape_rules.md`): soft digital watercolour, vibrant textbook
illustration style, 16:9.

**Where the scene allows it, the visual world is recognisably GUJARATI, not generic-Indian.**
Generic is what an image model returns when nothing stops it: `an Indian village, traditional
houses, children playing` renders the same frame for Punjab, Bengal and Panchmahal. Stop it by
naming particulars the chapter's own setting supports, taken from
`reference/gujarat_cultural_anchors.md`:

- **architecture** — curved clay નળિયાં or a tin sheet roof, the raised ઓટલો running along a
  પોળનું મકાન, a ચબૂતરો in the ચોક, a વાવ's descending steps, the shared નળ of a ફળિયું;
- **dress** — plain school uniforms for a classroom scene; કેડિયું-ધોતિયું, ચણિયાચોળી or a
  ભરતકામવાળી ઓઢણી only where the text is folk or festive; કચ્છી ભરત only where the text is Kutchi.
  Dress follows the scene, never costume for colour;
- **landscape** — a ખેતર of બાજરી or કપાસ, the ગિરનાર skyline, a દરિયાકિનારો with wooden હોડીઓ,
  the white salt flat, a heavy ચોમાસું sky over open ground;
- **objects** — બળદગાડું, છકડો, માટલું, પતંગ ને ફિરકી, a red-and-white ST bus, દૂધની કૅન, a સાળ,
  a કુંભારનો ચાકડો.

Write them as the picture, not as a shopping list of nouns:

> ❌ `A traditional Indian village scene, children playing in the street, houses behind them,
> warm colours.`
> ✅ `A village lane in Saurashtra in the first monsoon shower: low houses roofed with curved clay
> tiles, a raised stone platform along one wall, a neem tree still dripping, three children in
> plain school uniforms running through puddles with cloth school bags held flat over their heads,
> a bullock cart parked under a tin awning. Soft digital watercolour, vibrant textbook
> illustration style, 16:9.`

**The swap test:** if the prompt would render just as convincingly in Punjab or Bengal, it is not
anchored yet — name the roof, the ground, the tree, the clothing and one object the chapter itself
puts in the scene.

Across a chapter's frames let the whole state appear over time — Saurashtra, Kutch,
North/Central/South Gujarat, coastal and tribal (ડાંગ, ભીલ, રાઠવા), urban and rural — never one
slice on repeat, never a community reduced to a costume. Flavour dresses the **setting** only; it
never overrides the anchoring test below by adding what the chapter does not print. **When the
chapter is NOT set in Gujarat, keep the setting faithful to the text — fidelity beats flavour**: a
Jaisalmer travel essay gets Jaisalmer, a Tagore scene gets Bengal; Gujarati flavour bolted onto
another text's world is a depiction error, not a courtesy.

Where the design uses a **narrator bar**, name
the **exact Gujarati string** to render, written in Gujarati script inside the prompt — never a
transliteration, never a Devanagari rendering, and never the answer word in a riddle chapter. The
prompt body itself is written in English (the model's language); the string to be lettered is the
one Gujarati fragment inside it.

`negative_prompt` at minimum: `photorealistic faces, anime style, western-only setting, Roman script
labels, Devanagari script labels, generic Bollywood styling, north-Indian-only architecture,
watermark, blurry, cluttered background, anachronistic objects`.
Add the form's own refusals from its profile — `motivational poster layout, text banner with a
moral` for a દુહો, `devotional poster art, idol photograph, halo, temple calendar art` for a પદ.

### Two tests every authored prompt passes

- **The one-sentence depiction test.** If the picture cannot be described as a single moment
  somebody could photograph, it is a summary of the topic, not an image of it — re-author it.
- **The anchoring test.** The prompt names at least one concrete object, creature or action drawn
  from **this topic's** `original_chunk`. Nothing in it may assert what the chapter does not print:
  no invented portrait likeness of a real poet or subject, no invented biography, no invented "scene
  cast" of named characters (`reference/no_hallucination_policy.md`).

Where a scene genuinely names nothing depictable, **fewer frames is the correct answer**, recorded
as such in `reuse_report`. An invented tableau is worse than a missing image.

## What the image should show, by સ્વરૂપ

Take the media prior from the active profile — this is the short form of it.

- **દુહો / છપ્પો / મુક્તક** (`profiles/genres/duha_chhappa.md`) — the **દૃષ્ટાંત**, never the બોધ.
  The ઘુવડ and the daylight; the lone figure at the edge of a crowd. Not a child being kind, not a
  lesson panel, not the moral in lettering.
- **પદ / ભજન** (`profiles/genres/pad_bhajan.md`) — the scene and the **relationship**: warm,
  domestic, at human scale, the flute being played *and being heard*. Not an iconographic portrait,
  not a shrine.
- **ઊર્મિકાવ્ય / ગીત** (`profiles/genres/urmikavya_geet.md`) — that કડી's own picture. A
  changed-words ટેક topic shows what its **new** words name, never a repeat of the earlier frame.
- **પ્રાર્થના-કાવ્ય** (`profiles/genres/prarthana_kavita.md`) — the concrete thing the petition
  names, never the petition's meaning. **Do not draw ઈશ્વર.**
- **ગઝલ** (`profiles/genres/gazal.md`) — that શેર's own object. Never one frame for the whole ગઝલ,
  never a frame that continues the previous frame, never the રદીફ as a caption.
- **સૉનેટ** (`profiles/genres/sonnet.md`) — that ભાવ-ખંડ's concrete thing. Never a diagram of the
  form, never the abstraction the ચોટ names.
- **મુક્ત છંદ** (`profiles/genres/mukt_chhand_kavita.md`) — the poem's own બિંબ. Never literalise a
  રૂપક into an object.
- **કથાકાવ્ય** (`profiles/genres/kathakavya.md`) — that narrative step's moment, one likeness held
  across the chapter, never the whole ballad in one frame.
- **લોકગીત** (`profiles/genres/lok_geet.md`) — the occasion, and people singing **together** where
  the ટેક is the subject. Never a lone poet at a desk; this form has none.
- **ઉખાણું / રમતગીત** (`profiles/genres/ukhanu_ramatgeet.md`) — a clue **without** the answer. The
  solution word appears nowhere in the media node, narrator bar included.
- **વાર્તા** (`profiles/genres/varta.md`) — the moment of the choice, the faces at the turn;
  consistent likeness across the chapter's images.
- **ચરિત્ર-પ્રસંગ** (`profiles/genres/charitra_prasang.md`) — the act being performed, never a
  portrait and never the honour.
- **નિબંધ (લલિત/આત્મપરક) / સંસ્મરણ / હાસ્ય** (`profiles/genres/nibandh_atmaparak.md`) — the writer
  inside the moment, or the everyday object made literal. For a હાસ્ય scene the *moment*, never a
  caricature of the person and never the punchline as a gag.
- **માહિતીપ્રદ ગદ્ય** (`profiles/genres/mahitiprad_gadya.md`) — the practice **being done**, with
  the real instrument, costume, materials and setting as the chapter describes them.
- **સંવાદ / સંવાદ-નિબંધ** (`profiles/genres/samvad_nibandh.md`) — both parties in one frame, with
  the disputed thing between them where the chapter gives you one.
- **નાટક / એકાંકી** (`profiles/genres/natak_ekanki.md`) — the stage at that moment: who is on it,
  who is entering, who is turned away, what the રંગસૂચના just did. It is one room; the set stays
  consistent across the chapter.
- **પત્ર / પ્રવાસ** (`profiles/genres/patra_pravas.md`) — the place or the reported scene, in the
  order the text moves. A પત્ર's image shows what the letter *reports*, not the letter — except the
  first topic, which carries the સંબોધન and may show the writing or the receiving.

In a **mixed chapter**, each part takes its own profile's prior. The dominant સ્વરૂપ sets the
chapter's guiding question, not the composition of a scene it does not own.

## The one `2d_tool`

At most one per chapter, and most chapters correctly have **none** — write `"2d_tool": null` and
move on. It earns its place only where the text has something a child can operate: a staged process
in માહિતીપ્રદ ગદ્ય, a route in a પ્રવાસ-વર્ણન. Record `{topic_id, spec}`, and let the spec say what
the child manipulates and what changes when they do. If you cannot say what changes, it is an image,
not a tool.

## Output

```json
{"media":[{"topic_id":"M1.S1.T1","concept_id":"M1.S1.T1.C1",
  "id":"M1.S1.T1.C1.IMG1","type":"image","subtype":"illustration",
  "title":"…","description":"…","image_url":"","aspect_ratio":"16:9",
  "home_concept_id":"M1.S1.T1.C1","objective_id":null,"image_category":"illustration",
  "teaching_notes":"…","negative_prompt":"…","generation_prompt":"…"}],
 "2d_tool":{"topic_id":"…","spec":"…"},
 "reuse_report":{"scenes":9,"reused":0,"authored":9,"rejected":[]}}
```

`title` is a short Gujarati name for the picture, `description` one Gujarati sentence of what the
frame holds, `teaching_notes` a Gujarati line telling the teacher how to use it while the image is
still unbuilt — only bracketed machine stamps stay English.

`reuse_report.scenes` is counted off `05_with_content.json`: the topics whose
`available_content_types` carry `"image"`. In this pack `authored` equals `scenes`, `reused` is `0`
and `rejected` is `[]`. Agent 13 checks those numbers against the topic count; an inequality is a
defect to fix, not a rounding. `rejected` keeps its shape (`[{topic_id, frame, why}]`) for the day
frames exist — it is the evidence that the depiction floor was applied rather than assumed.

## Do not
- Give a topic two images, or the chapter two tools.
- Leave both `image_url` and `generation_prompt` empty — that is the defect the contract names.
- Write a non-empty `image_url`, or a `[reused frame: …]` stamp, while the pool is dormant.
- Import the Hindi scoring or collage tooling, or author a `_collage.json`
  (`reference/collage_media.md` is doctrine, not a runbook, until a Gujarati pool exists).
- Use a topic-scoped media id, or restart concept numbering inside a topic.
- Put Roman or Devanagari lettering in the frame, or a number in any display text.
- Illustrate the moral, or draw a scene the chapter does not contain.
- Bolt Gujarati flavour onto a chapter set elsewhere (fidelity to the text's own setting wins), or
  dress a figure in a community's costume the text does not place in the scene.
