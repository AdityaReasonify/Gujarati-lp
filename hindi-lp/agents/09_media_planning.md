---
name: 09_media_planning
description: Plan one image per reading scene — reuse an existing chapter frame where it genuinely matches, author a self-contained prompt where it does not. At most one 2d_tool per chapter.
tools: [Read, Bash]
inputs:
  - output/<chapter>/04_converged.json
  - output/<chapter>/05_with_content.json
  - the active genre profile(s) (media priors)
  - reference/field_shape_rules.md
  - reference/phase2_contract.md
outputs:
  - output/<chapter>/09_media.json
---

**One image per reading scene. At most one interactive `2d_tool` in the whole chapter.**
Media ids are **concept-scoped**: `{concept_id}.IMG{n}` — `M1.S1.T1.C1.IMG1`. A topic-scoped id is
rejected by the server.

## Step 1 — try to reuse an existing frame

Class-6 Hindi already has ~680 generated frames, one chapter's worth per chapter, in the v1 plans
at `imagebyGPT/data/cbse/cbse/english/class_6/hindi/ch_{N}/hindi6_ch{N}_standard_v1.json`. Each
carries `image_url`, `title`, `description` and `generation_prompt`.

Score this chapter's frames against the scene using the machinery already written for it:

```python
from prune_plan_images import score_media, deva, jaccard, eng   # imagebyGPT/
```

Score the frame's Devanagari tokens against the topic's `topic_name`, `key_terms` and
`original_chunk` tokens.

**Match only within the same chapter.** Never borrow across chapters, and never take the
best-scoring frame from a large pool as if that meant relevance. This has already failed once in
production: a topic about a bamboo stick game scored 0.464 against hockey frames while a topic
scoring on frames drawn *for it* scored 0.260 — because a maximum over 56 candidates beats a
maximum over 12 regardless of subject. **A high score in a big pool is not evidence.**

Accept a reuse only when you can state, in one sentence, what in the frame depicts what in the
scene. If you cannot, it is not a match.

On a match:
```json
{"image_url": "<the CDN url>", "generation_prompt": "",
 "teaching_notes": "…how to use it… [reused frame: M1.S1.T1.O1.E3]"}
```
Record the source frame id in `teaching_notes` — that is the provenance trail.

## Step 2 — otherwise, author a prompt

```json
{"image_url": "", "generation_prompt": "<self-contained>", "negative_prompt": "<…>"}
```

The prompt is read with **no other context**. It must carry the setting, the characters and their
fixed appearance, the action, the mood and the style by itself. Never write "the same character as
before", "the previous scene", or the chapter's name.

Standing conventions (`reference/field_shape_rules.md`): soft digital watercolour, vibrant textbook
illustration style, 16:9, Indian setting by default, and where the design uses a narrator bar, name
the exact Devanagari string to render. `negative_prompt` at minimum: photorealistic faces, anime
style, western-only setting, Roman script labels, watermark, blurry, cluttered background,
anachronistic objects.

## What the image should show, by विधा

Take the media prior from the profile. In short:
- **दोहा** — the **दृष्टांत**, not the moral. Water and a thread, not a child being kind.
- **पद** — the scene and the relationship; domestic and warm, not an iconographic portrait.
- **प्रकृति/देशभक्ति छंद** — that छंद's picture. A टेक topic shows what its *new* words name.
- **वीर-रस** — motion and posture; never gore.
- **कहानी / संस्मरण** — the moment of the choice or the remembered detail; consistent likeness
  across the chapter.
- **सूचनात्मक** — the practice being done, with the real instrument, costume and setting.
- **संवाद** — both parties in one frame.

## Output

```json
{"media":[{"topic_id":"M1.S1.T1","concept_id":"M1.S1.T1.C1",
  "id":"M1.S1.T1.C1.IMG1","type":"image","subtype":"illustration",
  "title":"…","description":"…","image_url":"…or empty…","aspect_ratio":"16:9",
  "home_concept_id":"M1.S1.T1.C1","objective_id":null,"image_category":"illustration",
  "teaching_notes":"…","negative_prompt":"…","generation_prompt":"…or empty if reused…"}],
 "2d_tool":{"topic_id":"…","spec":"…"} ,
 "reuse_report":{"scenes":9,"reused":4,"authored":5,
   "rejected":[{"topic_id":"…","frame":"…","why":"…"}]}}
```

`reuse_report.rejected` records frames that scored well but did not depict the scene. That list is
the evidence that the floor was applied rather than assumed.

## Do not
- Give a topic two images, or the chapter two tools.
- Reuse a frame you cannot justify in one sentence.
- Leave both `image_url` and `generation_prompt` empty.
- Use a topic-scoped media id.
