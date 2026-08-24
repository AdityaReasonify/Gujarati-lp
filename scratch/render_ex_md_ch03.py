#!/usr/bin/env python3
# Render exercise_solutions.json -> exercise_solutions.md (format mirrors output8/ch01)
import json, os

OUT = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output8/ch03"
d = json.load(open(os.path.join(OUT, "exercise_solutions.json"), encoding="utf-8"))
ex = d["exercises"]
cr = d["coverage_report"]

L = []
w = L.append

w("# સ્વાધ્યાય — ઉકેલ")
w("")
w("**પાઠ:** %s  " % d["chapter_name"])
w("**વિષય:** %s · **ધોરણ:** %s  " % (d["subject"], d["grade"]))
w("**chapter_id:** `%s` · **plan_id:** `%s`" % (d["chapter_id"], d["plan_id"]))
w("")
w("> આ પાઠના છાપેલા દરેક સ્વાધ્યાય-બ્લોકના ઉકેલ અહીં જ છે. સ્વાધ્યાય કદી teaching topic નથી —")
w("> `learning_plan_logical.json` તેને ભણાવતું નથી, આ ફાઇલ તેને ઉકેલે છે.")
w("")
w("## અનુક્રમ")
w("")
for b in cr["blocks_found"]:
    n = sum(1 for e in ex if e["exercise_group"] == b)
    w("- %s — %d" % (b, n))
w("")

cur = None
for e in ex:
    if e["exercise_group"] != cur:
        cur = e["exercise_group"]
        w("---")
        w("")
        w("## %s" % cur)
        w("")
    w("### `%s` · %s" % (e["exercise_id"], e["skill"]))
    w("")
    w("**પ્રશ્ન (છપાયેલો):**")
    w("")
    for ln in e["prompt_verbatim"].split("\n"):
        w("> %s" % ln if ln.strip() else ">")
    w("")
    w("**ઉત્તર:**")
    w("")
    ans = e["answer"]
    if isinstance(ans, list):
        for a in ans:
            w("- %s" % a)
    else:
        for i, ln in enumerate(str(ans).split("\n")):
            w(ln)
    w("")
    vft = e.get("values_filled_for_teaching")
    if vft:
        w("**ભરેલી જગ્યાઓ / કોષ્ટક:**")
        w("")
        if isinstance(vft, list):
            for v in vft:
                w("- %s" % v)
        elif isinstance(vft, dict):
            for k, v in vft.items():
                w("- **%s** — %s" % (k, v))
        else:
            for ln in str(vft).split("\n"):
                w(ln)
        w("")
    if e.get("explanation"):
        w("**સમજૂતી:** %s" % e["explanation"].replace("\n", " "))
        w("")
    alts = e.get("acceptable_alternatives") or []
    if alts:
        w("**બીજા સ્વીકાર્ય ઉત્તર:**")
        w("")
        for a in alts:
            w("- %s" % str(a).replace("\n", " "))
        w("")
    if e.get("is_model_answer"):
        w("*(નમૂનારૂપ ઉત્તર — એક શક્ય જવાબ, એકમાત્ર જવાબ નહિ.)*")
        w("")
    if e.get("teacher_note"):
        w("**શિક્ષક માટે:** %s" % e["teacher_note"].replace("\n", " "))
        w("")
    tops = e.get("covered_by_topics") or []
    w("**તૈયારી કરાવતાં topics:** %s" % (", ".join("`%s`" % t for t in tops) if tops else "—"))
    w("")

w("---")
w("")
w("## Coverage report")
w("")
w("| | |")
w("|---|---|")
w("| છપાયેલા બ્લોક મળ્યા | %d |" % len(cr["blocks_found"]))
w("| ઉકેલાયેલા બ્લોક | %d |" % len(cr["blocks_answered"]))
w("| કુલ entries | %d |" % len(ex))
w("| બાકી (unanswered) | %s |" % (", ".join(cr["unanswered"]) if cr.get("unanswered") else "—"))
w("| મેપ ન થયેલા (unmapped) | %d |" % len(cr.get("unmapped") or []))
w("")
w("**છપાયેલા બ્લોક, છપાયેલા ક્રમમાં:**")
w("")
for b in cr["blocks_found"]:
    w("- %s" % b)
w("")
um = cr.get("unmapped") or []
if um:
    w("**કોઈ topic સાથે મેપ ન થયેલા entries:**")
    w("")
    for u in um:
        if isinstance(u, dict):
            w("- `%s` · %s" % (u.get("exercise_id", "?"), u.get("exercise_group", "")))
            w("")
            w("  %s" % str(u.get("reason", "")).replace("\n", " "))
            w("")
        else:
            w("- %s" % u)
            w("")
if cr.get("_note"):
    w("**નોંધ:** %s" % cr["_note"].replace("\n", " "))
    w("")

open(os.path.join(OUT, "exercise_solutions.md"), "w", encoding="utf-8").write("\n".join(L).rstrip() + "\n")
print("wrote exercise_solutions.md  lines=%d entries=%d" % (len(L), len(ex)))
