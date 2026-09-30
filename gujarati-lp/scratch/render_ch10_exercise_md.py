import json

BASE = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output8/ch10"

d = json.load(open(f"{BASE}/exercise_solutions.json", encoding="utf-8"))
exs = d["exercises"]
cr = d["coverage_report"]

# --- group exercises into contiguous blocks by exercise_group, paired
# positionally with coverage_report.blocks_found (the verbatim printed
# heading), since exercise_group here is a short internal label and
# blocks_found carries the exact printed text, both in printed order. ---
blocks = []  # list of (heading, [exercises])
seen_groups = []
for ex in exs:
    g = ex["exercise_group"]
    if not blocks or seen_groups[-1] != g:
        seen_groups.append(g)
        blocks.append([g, []])
    blocks[-1][1].append(ex)

if len(blocks) != len(cr["blocks_found"]):
    raise SystemExit(f"block count mismatch: {len(blocks)} contiguous groups vs "
                      f"{len(cr['blocks_found'])} blocks_found entries")

for (g, items), heading in zip(blocks, cr["blocks_found"]):
    pass  # positional pairing only; heading comes from blocks_found

lines = []
lines.append("# સ્વાધ્યાય — ઉકેલ")
lines.append("")
lines.append(f"**પાઠ:** {d['chapter_name']}  ")
lines.append(f"**વિષય:** {d['subject']} · **ધોરણ:** {d['grade']}  ")
lines.append(f"**chapter_id:** `{d['chapter_id']}` · **plan_id:** `{d['plan_id']}`")
lines.append("")
lines.append("> આ પાઠના છાપેલા દરેક સ્વાધ્યાય-બ્લોકના ઉકેલ અહીં જ છે. સ્વાધ્યાય કદી teaching topic નથી —")
lines.append("> `learning_plan_logical.json` તેને ભણાવતું નથી, આ ફાઇલ તેને ઉકેલે છે.")
lines.append("")
lines.append("## અનુક્રમ")
lines.append("")
for (g, items), heading in zip(blocks, cr["blocks_found"]):
    lines.append(f"- {heading} — {len(items)}")
lines.append("")
lines.append("---")

for (g, items), heading in zip(blocks, cr["blocks_found"]):
    lines.append("")
    lines.append(f"## {heading}")
    for ex in items:
        lines.append("")
        lines.append(f"### `{ex['exercise_id']}` · {ex['skill']}")
        lines.append("")
        lines.append("**પ્રશ્ન (છપાયેલો):**")
        lines.append("")
        lines.append(f"> {ex['prompt_verbatim']}")
        lines.append("")
        lines.append("**ઉત્તર:**")
        lines.append("")
        lines.append(ex["answer"])

        vft = ex.get("values_filled_for_teaching")
        if vft:
            lines.append("")
            lines.append("**ભરેલી જગ્યાઓ / કોષ્ટક:**")
            lines.append("")
            lines.append(str(vft))

        lines.append("")
        lines.append(f"**સમજૂતી:** {ex['explanation']}")

        if ex.get("is_model_answer"):
            lines.append("")
            lines.append("*(નમૂનારૂપ ઉત્તર — એક શક્ય જવાબ, એકમાત્ર જવાબ નહિ.)*")

        alts = ex.get("acceptable_alternatives") or []
        if alts:
            lines.append("")
            lines.append("**બીજા સ્વીકાર્ય ઉત્તર:**")
            lines.append("")
            for a in alts:
                lines.append(f"- {a}")

        tn = ex.get("teacher_note")
        if tn:
            lines.append("")
            lines.append(f"**શિક્ષક માટે:** {tn}")

        cbt = ex.get("covered_by_topics") or []
        if cbt:
            lines.append("")
            ids_str = ", ".join(f"`{t}`" for t in cbt)
            lines.append(f"**તૈયારી કરાવતાં topics:** {ids_str}")
    lines.append("")
    lines.append("---")

# ---------- Coverage report ----------
lines.append("")
lines.append("## Coverage report")
lines.append("")
lines.append("| | |")
lines.append("|---|---|")
lines.append(f"| છપાયેલા બ્લોક મળ્યા | {len(cr['blocks_found'])} |")
lines.append(f"| ઉકેલાયેલા બ્લોક | {len(cr['blocks_answered'])} |")
lines.append(f"| કુલ entries | {len(exs)} |")
unanswered = cr.get("unanswered") or []
lines.append(f"| બાકી (unanswered) | {len(unanswered) if unanswered else '—'} |")
unmapped = cr.get("unmapped") or []
lines.append(f"| મેપ ન થયેલા (unmapped) | {len(unmapped)} |")
lines.append("")
lines.append("**છપાયેલા બ્લોક, છપાયેલા ક્રમમાં:**")
lines.append("")
for b in cr["blocks_found"]:
    lines.append(f"- {b}")
lines.append("")

if unanswered:
    lines.append("**Unanswered:**")
    lines.append("")
    for u in unanswered:
        lines.append(f"- {u}")
    lines.append("")

lines.append("**મેપ ન થયેલા items — નોંધ્યા છે, બનાવટી મેપિંગ કર્યું નથી:**")
lines.append("")
for u in unmapped:
    if isinstance(u, dict):
        lines.append(f"- `{u['exercise_id']}` ({u.get('exercise_group','')}) — {u.get('reason','')}")
    else:
        lines.append(f"- {u}")
lines.append("")

note = cr.get("_note")
if note:
    lines.append(f"**નોંધ:** {note}")

out = "\n".join(lines) + "\n"
open(f"{BASE}/exercise_solutions.md", "w", encoding="utf-8").write(out)
print("wrote exercise_solutions.md,", len(out), "chars")
