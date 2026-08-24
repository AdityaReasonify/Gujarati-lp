---
name: 15_textbook_plan
description: Re-derive the same renumbered nodes in printed (textbook) order. Ids stay, sequence changes.
tools: [Read, Bash]
inputs:
  - output{N}/<chapter>/learning_plan_logical.json
  - output{N}/<chapter>/05b_textbook_order.json
  - output{N}/<chapter>/11_pages.json
  - reference/phase2_contract.md
outputs:
  - output{N}/<chapter>/learning_plan_textbook.json
---

Same nodes, same ids, **printed order**.

## What you do

Take the finished logical plan and re-sequence its topics into the order they appear in the
printed chapter, using `05b_textbook_order.json` (and `11_pages.json` where it helps).

**Ids do not change.** You are reordering, not renumbering — a topic keeps the id Agent 14 gave
it. Every reference stays valid because nothing was renamed.

Set `ordering: "textbook"`.

## LP2 makes this a formality — read this first

The LP2 validator ties ids to traversal position (`expected segment_id='M1.S1', got 'M1.S2'`), so
a re-sequenced plan only validates if it is renumbered, and renumbering breaks the "ids stay"
rule. **In practice the textbook plan is always emitted with the same sequence as the logical
plan**, and the real printed order is recorded in the flag below. This is a platform limit, not a
diagnosis failure — say so plainly rather than pretending the orders were compared and matched.

## When the two orders are identical

For most GSEB Gujarati chapters, the teaching order **is** the printed order — the poem is taught
કડી by કડી in the order it is printed. That is expected and correct.

When it happens, emit the file anyway and raise `human_confirmation_required` in the run report:

```json
{"human_confirmation_required": true,
 "reason": "textbook order is identical to logical order",
 "checked": "05b_textbook_order.json matches the logical traversal exactly"}
```

This is **not a failure and not a silent pass.** It is a flag saying "the two deliverables are the
same file; confirm that is intended for this chapter." A chapter whose reading order genuinely
differs — a pre-reading box printed after the poem, an appended piece taught earlier — will not
raise it.

## Do not
- Renumber anything.
- Drop or add a node.
- Suppress the flag when the orders match.
