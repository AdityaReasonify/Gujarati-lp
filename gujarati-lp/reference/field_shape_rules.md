# Field Shape Rules — lengths, types and the shape of each authored field

| Field | Type | Shape |
|---|---|---|
| `objective_text` | string | **12–30 words**, a goal, Gujarati. Not a teaching paragraph. |
| `explanation` | string | **55–90 words**, teacher voice, inline glosses, deeper layer where earned |
| `real_life_example` | string | **55–90 words**, one Indian anchor, may end on a question |
| `brief_summary` | string | 1 sentence |
| `summary` | string | 2–3 sentences |
| `detailed_summary` | string | 4–6 sentences; strictly longer than `summary` |
| `key_terms` | string[] | `શબ્દ — અર્થ`, 3–6 per topic |
| `concept_bullets` / `important_points` | string[] | `કીવર્ડ — gloss`, 3–4 lines |
| `recall_questions[]` | object[] | 2–3 per topic, Bloom-laddered, each with a real answer |
| `figures_of_speech[]` | object[] | `{device, lines, note}`; `[]` when none |
| `rhyme_scheme` | object\|null | `{pattern, rhyming_words[], note}`; `null` for ગદ્ય |
| `difficult_words[]` | object[] | module level, 5–10, `{word, meaning, example}` |
| `word_count` | object | `{"original": <int>}` computed from `original_chunk` |
| `estimated_exchanges` | string | small integer as a string, e.g. `"4"` |
| `2d_tool` | string\|null | at most one per chapter |

**L2 re-validation flag (VERIFY-4).** The word-count bands above (55–90 / 12–30) are carried
over from the first-language source pack and are the binding targets until VERIFY-4 completes:
they must be re-validated against measured GSEB second-language chapters, with targets and
measurements recorded separately. Do not change the bands here; a confirmed mismatch is
reconciled through the board profile, not by silently editing this table.

## Media `generation_prompt` — self-contained

A prompt is read by an image model with **no other context**. It must therefore carry, in itself:
the setting, the characters with their fixed appearance, the action, the mood, and the style. Add
the standing Gujarati-pack conventions:

- Soft digital watercolour, vibrant textbook illustration style, 16:9.
- **Indian setting by default** — clothing, architecture, landscape, faces.
- A **narrator bar** at the bottom carrying one line of Gujarati in Gujarati script where the
  design uses one; name the exact string to render.
- `negative_prompt` at minimum: photorealistic faces, anime style, western-only setting, Roman
  script labels, Devanagari script labels, watermark, blurry, cluttered background, anachronistic
  objects.

Never write a prompt that refers to "the previous image", "the same character as before", or the
chapter by name — the model cannot see any of that.

## Recall question

```json
{"id": "M1.S1.T1.RQ1", "legacy_id": "M1.S1.T1.TR1",
 "prompt": "…", "answer": "…", "difficulty": "easy|medium|hard",
 "bloom_level": "remember|understand|apply|analyze|evaluate|create"}
```

`bloom_level` is lowercase here and Capitalised in `objectives[]` — that asymmetry is in the
accepted reference plan; keep it.

## Empty is a legitimate value

`[]` and `null` are correct answers when the text gives nothing. Filling a field to avoid an empty
one is a `no_hallucination_policy.md` violation, not diligence.
