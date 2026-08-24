#!/usr/bin/env python3
"""Render exercise_solutions.json -> exercise_solutions.md (ch07/ch05 house format)."""
import json, os
from collections import Counter

D = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch08"
d = json.load(open(os.path.join(D, "exercise_solutions.json"), encoding="utf-8"))

L = []
L.append("# સ્વાધ્યાય — ઉકેલ")
L.append("")
L.append("**પાઠ:** %s  " % d["chapter_name"])
L.append("**વિષય:** %s · **ધોરણ:** %s  " % (d["subject"], d["grade"]))
L.append("**chapter_id:** `%s` · **plan_id:** `%s`" % (d["chapter_id"], d["plan_id"]))
L.append("")
L.append("> આ પાઠના છાપેલા દરેક સ્વાધ્યાય-બ્લોકના ઉકેલ અહીં જ છે. સ્વાધ્યાય કદી teaching topic નથી —")
L.append("> `learning_plan_logical.json` તેને ભણાવતું નથી, આ ફાઇલ તેને ઉકેલે છે.")
L.append("")

groups = []
for e in d["exercises"]:
    if e["exercise_group"] not in groups:
        groups.append(e["exercise_group"])
counts = Counter(e["exercise_group"] for e in d["exercises"])

L.append("## અનુક્રમ")
L.append("")
for g in groups:
    L.append("- %s — %d" % (g, counts[g]))
L.append("")

for g in groups:
    L.append("---")
    L.append("")
    L.append("## %s" % g)
    L.append("")
    for e in [x for x in d["exercises"] if x["exercise_group"] == g]:
        L.append("### `%s` · %s" % (e["exercise_id"], e.get("skill") or ""))
        L.append("")
        L.append("**પ્રશ્ન (છપાયેલો):**")
        L.append("")
        for ln in e["prompt_verbatim"].split("\n"):
            L.append(("> " + ln).rstrip())
        L.append("")
        L.append("**ઉત્તર:**")
        L.append("")
        L.append(e["answer"])
        L.append("")
        if e.get("values_filled_for_teaching"):
            L.append("**ભરેલી જગ્યાઓ / કોષ્ટક:**")
            L.append("")
            L.append(e["values_filled_for_teaching"])
            L.append("")
        if e.get("explanation"):
            L.append("**સમજૂતી:** %s" % e["explanation"])
            L.append("")
        if e.get("acceptable_alternatives"):
            L.append("**બીજા સ્વીકાર્ય ઉત્તર:**")
            L.append("")
            for a in e["acceptable_alternatives"]:
                L.append("- %s" % a)
            L.append("")
        if e.get("is_model_answer"):
            L.append("*(નમૂનારૂપ ઉત્તર — એક શક્ય જવાબ, એકમાત્ર જવાબ નહિ.)*")
            L.append("")
        if e.get("teacher_note"):
            L.append("**શિક્ષક માટે:** %s" % e["teacher_note"])
            L.append("")
        if e.get("covered_by_topics"):
            L.append("**તૈયારી કરાવતાં topics:** %s"
                     % ", ".join("`%s`" % t for t in e["covered_by_topics"]))
            L.append("")

cr = d["coverage_report"]
unanswered = cr.get("unanswered") or []
unmapped = cr.get("unmapped") or []
L.append("---")
L.append("")
L.append("## Coverage report")
L.append("")
L.append("| | |")
L.append("|---|---|")
L.append("| છપાયેલા બ્લોક મળ્યા | %d |" % len(cr.get("blocks_found") or []))
L.append("| ઉકેલાયેલા બ્લોક | %d |" % len(cr.get("blocks_answered") or []))
L.append("| કુલ entries | %d |" % len(d["exercises"]))
L.append("| બાકી (unanswered) | %s |" % (len(unanswered) if unanswered else "—"))
L.append("| મેપ ન થયેલા (unmapped) | %s |" % (len(unmapped) if unmapped else "—"))
L.append("")
L.append("**છપાયેલા બ્લોક, છપાયેલા ક્રમમાં:**")
L.append("")
for b in cr.get("blocks_found") or []:
    L.append("- %s" % b)
L.append("")
if unanswered:
    L.append("**ઉકેલ વગરના બ્લોક:**")
    L.append("")
    for b in unanswered:
        L.append("- %s" % (b if isinstance(b, str) else json.dumps(b, ensure_ascii=False)))
    L.append("")
if unmapped:
    L.append("**કોઈ topic સાથે મેપ ન થયેલા entries:**")
    L.append("")
    for u in unmapped:
        L.append("- `%s` · %s" % (u["exercise_id"], u.get("prompt_verbatim_short", "")))
        L.append("")
        L.append("  %s" % u.get("reason", ""))
        L.append("")
if cr.get("_note"):
    L.append("**નોંધ:** %s" % cr["_note"])
    L.append("")

out = os.path.join(D, "exercise_solutions.md")
open(out, "w", encoding="utf-8").write("\n".join(L).rstrip("\n") + "\n")
print("wrote", out, len(L), "lines")
