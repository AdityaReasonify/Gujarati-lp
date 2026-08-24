#!/usr/bin/env python3
# Render exercise_solutions.md from exercise_solutions.json, in the format the
# earlier std-6 chapters use (ch01–ch05).
import json, collections, os

D = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch06"
with open(os.path.join(D, "exercise_solutions.json"), encoding="utf-8") as f:
    d = json.load(f, object_pairs_hook=collections.OrderedDict)

def block(text):
    """multi-line body with markdown hard breaks"""
    lines = (text or "").split("\n")
    return "\n".join(l + ("  " if i < len(lines) - 1 else "")
                     for i, l in enumerate(lines))

groups = collections.OrderedDict()
for e in d["exercises"]:
    groups.setdefault(e["exercise_group"], []).append(e)

O = []
O.append("# સ્વાધ્યાય — ઉકેલ")
O.append("")
O.append("**પાઠ:** %s  " % d["chapter_name"])
O.append("**વિષય:** %s · **ધોરણ:** %s  " % (d["subject"], d["grade"]))
O.append("**chapter_id:** `%s` · **plan_id:** `%s`" % (d["chapter_id"], d["plan_id"]))
O.append("")
O.append("> આ પાઠના છાપેલા દરેક સ્વાધ્યાય-બ્લોકના ઉકેલ અહીં જ છે. સ્વાધ્યાય કદી teaching topic નથી —")
O.append("> `learning_plan_logical.json` તેને ભણાવતું નથી, આ ફાઇલ તેને ઉકેલે છે.")
O.append("")
O.append("## અનુક્રમ")
O.append("")
for g, items in groups.items():
    O.append("- %s — %d" % (g, len(items)))
O.append("")

for g, items in groups.items():
    O.append("---")
    O.append("")
    O.append("## %s" % g)
    O.append("")
    for e in items:
        O.append("### `%s` · %s" % (e["exercise_id"], e.get("skill") or "—"))
        O.append("")
        O.append("**પ્રશ્ન (છપાયેલો):**")
        O.append("")
        for line in e["prompt_verbatim"].split("\n"):
            O.append("> " + line)
        O.append("")
        O.append("**ઉત્તર:**")
        O.append("")
        O.append(block(e["answer"]))
        O.append("")
        if e.get("values_filled_for_teaching"):
            O.append("**ભરેલી જગ્યાઓ / કોષ્ટક:**")
            O.append("")
            O.append(block(e["values_filled_for_teaching"]))
            O.append("")
        if e.get("explanation"):
            O.append("**સમજૂતી:** %s" % e["explanation"].replace("\n", " "))
            O.append("")
        if e.get("acceptable_alternatives"):
            O.append("**બીજા સ્વીકાર્ય ઉત્તર:**")
            O.append("")
            for a in e["acceptable_alternatives"]:
                O.append("- %s" % a.replace("\n", " "))
            O.append("")
        if e.get("is_model_answer"):
            O.append("*(નમૂનારૂપ ઉત્તર — એક શક્ય જવાબ, એકમાત્ર જવાબ નહિ.)*")
            O.append("")
        if e.get("teacher_note"):
            O.append("**શિક્ષક માટે:** %s" % e["teacher_note"].replace("\n", " "))
            O.append("")
        cov = e.get("covered_by_topics") or []
        O.append("**તૈયારી કરાવતાં topics:** %s"
                 % (", ".join("`%s`" % c for c in cov) if cov else "—"))
        O.append("")

cr = d["coverage_report"]
O.append("---")
O.append("")
O.append("## Coverage report")
O.append("")
O.append("| | |")
O.append("|---|---|")
O.append("| છપાયેલા બ્લોક મળ્યા | %d |" % len(cr["blocks_found"]))
O.append("| ઉકેલાયેલા બ્લોક | %d |" % len(cr["blocks_answered"]))
O.append("| કુલ entries | %d |" % len(d["exercises"]))
O.append("| બાકી (unanswered) | %s |"
         % ("—" if not cr.get("unanswered") else ", ".join(map(str, cr["unanswered"]))))
O.append("| મેપ ન થયેલા (unmapped) | %d |" % len(cr.get("unmapped") or []))
O.append("")
O.append("**છપાયેલા બ્લોક, છપાયેલા ક્રમમાં:**")
O.append("")
for b in cr["blocks_found"]:
    O.append("- %s" % b)
O.append("")
if cr.get("unmapped"):
    O.append("**કોઈ topic સાથે મેપ ન થયેલા entries:**")
    O.append("")
    for u in cr["unmapped"]:
        ids = u.get("exercise_ids") or [u["exercise_id"]]
        O.append("- %s · %s" % (", ".join("`%s`" % i for i in ids), u["exercise_group"]))
        O.append("")
        O.append("  %s" % u["reason"].replace("\n", " "))
        O.append("")
O.append("**નોંધ:** %s" % cr["_note"].replace("\n", " "))
O.append("")

with open(os.path.join(D, "exercise_solutions.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(O))

print("wrote exercise_solutions.md: groups=%d entries=%d unmapped=%d"
      % (len(groups), len(d["exercises"]), len(cr.get("unmapped") or [])))
