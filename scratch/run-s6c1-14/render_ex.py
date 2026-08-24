# -*- coding: utf-8 -*-
"""Phase-7 tail: copy 10_exercise_solutions.json -> exercise_solutions.json and render the .md.

The .md is a rendering of the JSON and adds nothing to it: every line below is a field the
JSON already carries (reference/no_hallucination_policy.md).
"""
import json, os, shutil

OUT = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch01"
src = os.path.join(OUT, "10_exercise_solutions.json")
dst = os.path.join(OUT, "exercise_solutions.json")
shutil.copyfile(src, dst)

d = json.load(open(dst, encoding="utf-8"))
L = []
A = L.append

A("# સ્વાધ્યાય — ઉકેલ")
A("")
A("**પાઠ:** %s  " % d["chapter_name"])
A("**વિષય:** %s · **ધોરણ:** %s  " % (d["subject"], d["grade"]))
A("**chapter_id:** `%s` · **plan_id:** `%s`" % (d["chapter_id"], d["plan_id"]))
A("")
A("> આ પાઠના છાપેલા દરેક સ્વાધ્યાય-બ્લોકના ઉકેલ અહીં જ છે. સ્વાધ્યાય કદી teaching topic નથી —")
A("> `learning_plan_logical.json` તેને ભણાવતું નથી, આ ફાઇલ તેને ઉકેલે છે.")
A("")

groups = []
for e in d["exercises"]:
    if not groups or groups[-1][0] != e["exercise_group"]:
        groups.append((e["exercise_group"], []))
    groups[-1][1].append(e)

A("## અનુક્રમ")
A("")
for g, items in groups:
    A("- %s — %d" % (g, len(items)))
A("")
A("---")
A("")

for g, items in groups:
    A("## %s" % g)
    A("")
    for e in items:
        A("### `%s` · %s" % (e["exercise_id"], e["skill"]))
        A("")
        A("**પ્રશ્ન (છપાયેલો):**")
        A("")
        for line in e["prompt_verbatim"].split("\n"):
            A("> %s" % line)
        A("")
        A("**ઉત્તર:**")
        A("")
        alines = e["answer"].split("\n")
        for j, line in enumerate(alines):
            A(line + ("  " if j < len(alines) - 1 and line.strip() else ""))
        A("")
        if e.get("values_filled_for_teaching"):
            A("**ભરેલી જગ્યાઓ / કોષ્ટક:**")
            A("")
            v = e["values_filled_for_teaching"]
            if isinstance(v, dict):
                for k, val in v.items():
                    A("- **%s** — %s" % (k, val))
            elif isinstance(v, list):
                for val in v:
                    A("- %s" % (val if not isinstance(val, dict)
                                else " — ".join(str(x) for x in val.values())))
            else:
                A(str(v))
            A("")
        if e.get("explanation"):
            A("**સમજૂતી:** %s" % e["explanation"])
            A("")
        if e.get("acceptable_alternatives"):
            A("**બીજા સ્વીકાર્ય ઉત્તર:**")
            A("")
            for a in e["acceptable_alternatives"]:
                A("- %s" % a)
            A("")
        if e.get("is_model_answer"):
            A("*(નમૂનારૂપ ઉત્તર — એક શક્ય જવાબ, એકમાત્ર જવાબ નહિ.)*")
            A("")
        if e.get("teacher_note"):
            A("**શિક્ષક માટે:** %s" % e["teacher_note"])
            A("")
        if e.get("covered_by_topics"):
            A("**તૈયારી કરાવતાં topics:** %s"
              % ", ".join("`%s`" % t for t in e["covered_by_topics"]))
            A("")
    A("---")
    A("")

cr = d["coverage_report"]
A("## Coverage report")
A("")
A("| | |")
A("|---|---|")
A("| છપાયેલા બ્લોક મળ્યા | %d |" % len(cr["blocks_found"]))
A("| ઉકેલાયેલા બ્લોક | %d |" % len(cr["blocks_answered"]))
A("| કુલ entries | %d |" % len(d["exercises"]))
A("| બાકી (unanswered) | %s |" % (", ".join(cr["unanswered"]) if cr["unanswered"] else "—"))
A("| મેપ ન થયેલા (unmapped) | %s |" % (", ".join(cr["unmapped"]) if cr["unmapped"] else "—"))
A("")
A("**છપાયેલા બ્લોક, છપાયેલા ક્રમમાં:**")
A("")
for b in cr["blocks_found"]:
    A("- %s%s" % (b, "" if b in cr["blocks_answered"] else "  ← ઉકેલ બાકી"))
A("")
if cr.get("_note"):
    A("**નોંધ:** %s" % cr["_note"])
    A("")

open(os.path.join(OUT, "exercise_solutions.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
print("wrote exercise_solutions.json (%d exercises) and exercise_solutions.md (%d lines)"
      % (len(d["exercises"]), len(L)))
