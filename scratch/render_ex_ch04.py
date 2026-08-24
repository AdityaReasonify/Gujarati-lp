#!/usr/bin/env python3
# Agent 14 — render exercise_solutions.md from exercise_solutions.json (std 6, ch 4).
import json

D = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch04"
d = json.load(open(f"{D}/exercise_solutions.json"))
ex = d["exercises"]
cov = d["coverage_report"]

def block(s):
    return "\n".join("> " + ln if ln.strip() else ">" for ln in s.split("\n"))

def softbreaks(s):
    return s.replace("\n", "  \n")

out = []
w = out.append

w("# સ્વાધ્યાય — ઉકેલ")
w("")
w(f"**પાઠ:** {d['chapter_name']}  ")
w(f"**વિષય:** {d['subject']} · **ધોરણ:** {d['grade']}  ")
w(f"**chapter_id:** `{d['chapter_id']}` · **plan_id:** `{d['plan_id']}`")
w("")
w("> આ પાઠના છાપેલા દરેક સ્વાધ્યાય-બ્લોકના ઉકેલ અહીં જ છે. સ્વાધ્યાય કદી teaching topic નથી —")
w("> `learning_plan_logical.json` તેને ભણાવતું નથી, આ ફાઇલ તેને ઉકેલે છે.")
w("")
w("## અનુક્રમ")
w("")

groups = []
for e in ex:
    if not groups or groups[-1][0] != e["exercise_group"]:
        groups.append([e["exercise_group"], []])
    groups[-1][1].append(e)
for g, items in groups:
    w(f"- {g} — {len(items)}")

for g, items in groups:
    w("")
    w("---")
    w("")
    w(f"## {g}")
    for e in items:
        w("")
        w(f"### `{e['exercise_id']}` · {e['skill']}")
        w("")
        w("**પ્રશ્ન (છપાયેલો):**")
        w("")
        w(block(e["prompt_verbatim"]))
        w("")
        w("**ઉત્તર:**")
        w("")
        w(softbreaks(e["answer"]))
        if e.get("values_filled_for_teaching"):
            w("")
            w("**ભરેલી જગ્યાઓ / કોષ્ટક:**")
            w("")
            w(softbreaks(e["values_filled_for_teaching"]))
        if e.get("explanation"):
            w("")
            w(f"**સમજૂતી:** {softbreaks(e['explanation'])}")
        if e.get("acceptable_alternatives"):
            w("")
            w("**બીજા સ્વીકાર્ય ઉત્તર:**")
            w("")
            for a in e["acceptable_alternatives"]:
                w(f"- {a}")
        if e.get("is_model_answer"):
            w("")
            w("*(નમૂનારૂપ ઉત્તર — એક શક્ય જવાબ, એકમાત્ર જવાબ નહિ.)*")
        if e.get("teacher_note"):
            w("")
            w(f"**શિક્ષક માટે:** {softbreaks(e['teacher_note'])}")
        if e.get("covered_by_topics"):
            w("")
            w("**તૈયારી કરાવતાં topics:** "
              + ", ".join(f"`{t}`" for t in e["covered_by_topics"]))

w("")
w("---")
w("")
w("## Coverage report")
w("")
w("| | |")
w("|---|---|")
w(f"| છપાયેલા બ્લોક મળ્યા | {len(cov['blocks_found'])} |")
w(f"| ઉકેલાયેલા બ્લોક | {len(cov['blocks_answered'])} |")
w(f"| કુલ entries | {len(ex)} |")
w(f"| બાકી (unanswered) | {len(cov['unanswered']) if cov['unanswered'] else '—'} |")
w(f"| મેપ ન થયેલા (unmapped) | {len(cov['unmapped']) if cov['unmapped'] else '—'} |")
w("")
w("**છપાયેલા બ્લોક, છપાયેલા ક્રમમાં:**")
w("")
for b in cov["blocks_found"]:
    w(f"- {b}")

if cov["unmapped"]:
    w("")
    w("**કોઈ topic સાથે મેપ ન થયેલા entries:**")
    for u in cov["unmapped"]:
        ids = u.get("exercise_ids") or [u["exercise_id"]]
        w("")
        w("- " + ", ".join(f"`{i}`" for i in ids) + f" · {u['exercise_group']}")
        w("")
        w(f"  {u['reason']}")

if cov.get("_note"):
    w("")
    w(f"**નોંધ:** {cov['_note']}")
w("")

open(f"{D}/exercise_solutions.md", "w").write("\n".join(out))
print("wrote exercise_solutions.md", len(out), "lines")
