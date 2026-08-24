#!/usr/bin/env python3
"""Phase-7 deliverable render: 10_exercise_solutions.json -> exercise_solutions.json + .md"""
import json, pathlib, shutil

OUT = pathlib.Path("/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch07")
src = OUT / "10_exercise_solutions.json"
dst = OUT / "exercise_solutions.json"
shutil.copyfile(src, dst)

d = json.loads(dst.read_text())
ex = d["exercises"]
cov = d.get("coverage_report", {})

groups = []
for e in ex:
    if e["exercise_group"] not in groups:
        groups.append(e["exercise_group"])

L = []
L.append("# સ્વાધ્યાય — ઉકેલ")
L.append("")
L.append(f'**પાઠ:** {d["chapter_name"]}  ')
L.append(f'**વિષય:** {d["subject"]} · **ધોરણ:** {d["grade"]}  ')
L.append(f'**chapter_id:** `{d["chapter_id"]}` · **plan_id:** `{d["plan_id"]}`')
L.append("")
L.append("> આ પાઠના છાપેલા દરેક સ્વાધ્યાય-બ્લોકના ઉકેલ અહીં જ છે. સ્વાધ્યાય કદી teaching topic નથી —")
L.append("> `learning_plan_logical.json` તેને ભણાવતું નથી, આ ફાઇલ તેને ઉકેલે છે.")
L.append("")
L.append("## અનુક્રમ")
L.append("")
for g in groups:
    L.append(f"- {g} — {sum(1 for e in ex if e['exercise_group'] == g)}")
L.append("")

for g in groups:
    L.append("---")
    L.append("")
    L.append(f"## {g}")
    L.append("")
    for e in [x for x in ex if x["exercise_group"] == g]:
        L.append(f'### `{e["exercise_id"]}` · {e["skill"]}')
        L.append("")
        L.append("**પ્રશ્ન (છપાયેલો):**")
        L.append("")
        for ln in e["prompt_verbatim"].split("\n"):
            L.append(f"> {ln}" if ln else ">")
        L.append("")
        L.append("**ઉત્તર:**")
        L.append("")
        L.extend(e["answer"].split("\n"))
        L.append("")
        v = e.get("values_filled_for_teaching")
        if v:
            L.append("**ભરેલી જગ્યાઓ / કોષ્ટક:**")
            L.append("")
            if isinstance(v, list):
                L.extend(f"- {x}" for x in v)
            else:
                L.extend(str(v).split("\n"))
            L.append("")
        if e.get("explanation"):
            L.append(f'**સમજૂતી:** {e["explanation"]}')
            L.append("")
        alts = e.get("acceptable_alternatives") or []
        if alts:
            L.append("**બીજા સ્વીકાર્ય ઉત્તર:**")
            L.append("")
            L.extend(f"- {a}" for a in alts)
            L.append("")
        if e.get("is_model_answer"):
            L.append("*(નમૂનારૂપ ઉત્તર — એક શક્ય જવાબ, એકમાત્ર જવાબ નહિ.)*")
            L.append("")
        if e.get("teacher_note"):
            L.append(f'**શિક્ષક માટે:** {e["teacher_note"]}')
            L.append("")
        cbt = e.get("covered_by_topics") or []
        if cbt:
            L.append("**તૈયારી કરાવતાં topics:** " + ", ".join(f"`{t}`" for t in cbt))
        else:
            L.append("**તૈયારી કરાવતાં topics:** — "
                     "(કોઈ વાચન-દૃશ્ય તૈયારી કરાવતું નથી; Coverage report જુઓ.)")
        L.append("")

L.append("---")
L.append("")
L.append("## Coverage report")
L.append("")
L.append("| | |")
L.append("|---|---|")
L.append(f'| છપાયેલા બ્લોક મળ્યા | {len(cov.get("blocks_found", []))} |')
L.append(f'| ઉકેલાયેલા બ્લોક | {len(cov.get("blocks_answered", []))} |')
L.append(f"| કુલ entries | {len(ex)} |")
L.append(f'| બાકી (unanswered) | {len(cov.get("unanswered") or []) or "—"} |')
L.append(f'| મેપ ન થયેલા (unmapped) | {len(cov.get("unmapped") or []) or "—"} |')
L.append("")
L.append("**છપાયેલા બ્લોક, છપાયેલા ક્રમમાં:**")
L.append("")
for b in cov.get("blocks_found", []):
    L.append(f"- {b}")
L.append("")
if cov.get("unanswered"):
    L.append("**ઉકેલ વગરના બ્લોક:**")
    L.append("")
    for b in cov["unanswered"]:
        L.append(f"- {b}")
    L.append("")
if cov.get("unmapped"):
    L.append("**કોઈ topic સાથે મેપ ન થયેલા entries:**")
    L.append("")
    for u in cov["unmapped"]:
        L.append(f'- `{u["exercise_id"]}` · {u["prompt_verbatim_short"]}')
        L.append("")
        L.append(f'  {u["reason"]}')
        L.append("")
if cov.get("_note"):
    L.append(f'**નોંધ:** {cov["_note"]}')
    L.append("")

(OUT / "exercise_solutions.md").write_text("\n".join(L))
print("wrote exercise_solutions.json + exercise_solutions.md  lines=%d" % len(L))
