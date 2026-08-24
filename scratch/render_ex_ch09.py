#!/usr/bin/env python3
# Render exercise_solutions.json -> exercise_solutions.md (format follows output6/ch07, ch08).
import json, collections, os

OUT = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch09"
with open(os.path.join(OUT, "exercise_solutions.json"), encoding="utf-8") as f:
    d = json.load(f, object_pairs_hook=collections.OrderedDict)

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

# group runs, in printed order
runs = []
for e in d["exercises"]:
    if not runs or runs[-1][0] != e["exercise_group"]:
        runs.append([e["exercise_group"], []])
    runs[-1][1].append(e)

A("## અનુક્રમ")
A("")
for g, items in runs:
    A("- %s — %d" % (g, len(items)))
A("")

for g, items in runs:
    A("---")
    A("")
    A("## %s" % g)
    A("")
    for e in items:
        A("### `%s` · %s" % (e["exercise_id"], e["skill"]))
        A("")
        A("**પ્રશ્ન (છપાયેલો):**")
        A("")
        for line in e["prompt_verbatim"].split("\n"):
            A("> %s" % line if line.strip() else ">")
        A("")
        A("**ઉત્તર:**")
        A("")
        for line in e["answer"].split("\n"):
            A(line)
        A("")
        if e.get("values_filled_for_teaching"):
            A("**ભરેલી જગ્યાઓ / કોષ્ટક:**")
            A("")
            for line in e["values_filled_for_teaching"].split("\n"):
                A(line)
            A("")
        if e.get("explanation"):
            A("**સમજૂતી:** %s" % e["explanation"])
            A("")
        if e.get("acceptable_alternatives"):
            A("**બીજા સ્વીકાર્ય ઉત્તર:**")
            A("")
            for alt in e["acceptable_alternatives"]:
                A("- %s" % alt.replace("\n", " "))
            A("")
        if e.get("is_model_answer"):
            A("*(નમૂનારૂપ ઉત્તર — એક શક્ય જવાબ, એકમાત્ર જવાબ નહિ.)*")
            A("")
        if e.get("teacher_note"):
            A("**શિક્ષક માટે:** %s" % e["teacher_note"])
            A("")
        if e.get("covered_by_topics"):
            A("**તૈયારી કરાવતાં topics:** %s" % ", ".join("`%s`" % t for t in e["covered_by_topics"]))
        else:
            A("**તૈયારી કરાવતાં topics:** —")
        A("")

cr = d["coverage_report"]
unanswered = cr.get("unanswered") or []
unmapped = cr.get("unmapped") or []
A("---")
A("")
A("## Coverage report")
A("")
A("| | |")
A("|---|---|")
A("| છપાયેલા બ્લોક મળ્યા | %d |" % len(cr["blocks_found"]))
A("| ઉકેલાયેલા બ્લોક | %d |" % len(cr["blocks_answered"]))
A("| કુલ entries | %d |" % len(d["exercises"]))
A("| બાકી (unanswered) | %s |" % (len(unanswered) if unanswered else "—"))
A("| મેપ ન થયેલા (unmapped) | %s |" % (len(unmapped) if unmapped else "—"))
A("")
A("**છપાયેલા બ્લોક, છપાયેલા ક્રમમાં:**")
A("")
for b in cr["blocks_found"]:
    A("- %s" % b)
A("")
if unanswered:
    A("**ઉકેલ વગરના બ્લોક:**")
    A("")
    for u in unanswered:
        A("- %s" % (u if isinstance(u, str) else json.dumps(u, ensure_ascii=False)))
    A("")
if unmapped:
    A("**કોઈ topic સાથે મેપ ન થયેલા entries:**")
    A("")
    for u in unmapped:
        A("- `%s` · %s — %s" % (u["exercise_id"], u["exercise_group"],
                                u["prompt_verbatim"].replace("\n", " / ")))
        A("")
        A("  %s" % u["reason"])
        A("")
if cr.get("_note"):
    A("**નોંધ:** %s" % cr["_note"])
    A("")

with open(os.path.join(OUT, "exercise_solutions.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(L).rstrip() + "\n")
print("wrote exercise_solutions.md  lines=%d groups=%d entries=%d" % (len(L), len(runs), len(d["exercises"])))
