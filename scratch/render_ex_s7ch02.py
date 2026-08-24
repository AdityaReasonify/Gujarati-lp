#!/usr/bin/env python3
# Phase 7: copy 10_exercise_solutions.json -> exercise_solutions.json and render the .md
# Format mirrors output7/ch01/exercise_solutions.md exactly.
import json, shutil
from pathlib import Path

OUT = Path("/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output7/ch02")
src = OUT / "10_exercise_solutions.json"
dst = OUT / "exercise_solutions.json"
shutil.copyfile(src, dst)

d = json.loads(dst.read_text(encoding="utf-8"))
ex = d["exercises"]
cov = d["coverage_report"]


def quote(text):
    return "\n".join("> " + ln if ln.strip() else ">" for ln in str(text).split("\n"))


L = []
L.append("# સ્વાધ્યાય — ઉકેલ")
L.append("")
L.append(f"**{d['chapter_name']}** · ધોરણ {d['grade']} · {d['subject']}")
L.append("")
L.append("| | |")
L.append("|---|---|")
L.append(f"| `chapter_id` | `{d['chapter_id']}` |")
L.append(f"| `plan_id` | `{d['plan_id']}` |")
L.append(f"| છપાયેલા સ્વાધ્યાય-બ્લૉક | {len(cov['blocks_found'])} |")
L.append(f"| ઉત્તર અપાયેલા બ્લૉક | {len(cov['blocks_answered'])} |")
L.append(f"| કુલ પ્રશ્ન-એકમ | {len(ex)} |")
L.append("")
L.append("> સ્વાધ્યાય કદી શીખવવાનો ટૉપિક નથી. છપાયેલો દરેક સ્વાધ્યાય-બ્લૉક ફક્ત આ જ ફાઇલમાં ઉકેલાયો છે.")
L.append("")
L.append("---")

groups = []
for e in ex:
    if e["exercise_group"] not in groups:
        groups.append(e["exercise_group"])

for g in groups:
    L.append("")
    L.append(f"## {g}")
    for e in [x for x in ex if x["exercise_group"] == g]:
        L.append("")
        L.append(f"### `{e['exercise_id']}`")
        L.append("")
        L.append("**પ્રશ્ન (છપાયેલો)**")
        L.append("")
        L.append(quote(e["prompt_verbatim"]))
        L.append("")
        head = "**ઉત્તર**"
        if e.get("is_model_answer"):
            head += " · *એક શક્ય ઉત્તર (નમૂનારૂપ)*"
        L.append(head)
        L.append("")
        L.append(quote(e["answer"]))
        if e.get("values_filled_for_teaching"):
            L.append("")
            L.append("**ભરેલા રૂપે (વર્ગમાં બતાવવા)**")
            L.append("")
            L.append(quote(e["values_filled_for_teaching"]))
        if e.get("acceptable_alternatives"):
            L.append("")
            L.append("**સ્વીકાર્ય બીજાં રૂપ**")
            L.append("")
            for a in e["acceptable_alternatives"]:
                L.append("- " + str(a).replace("\n", " / "))
        if e.get("explanation"):
            L.append("")
            L.append(f"**સમજૂતી** — {e['explanation']}")
        if e.get("teacher_note"):
            L.append("")
            L.append(f"**શિક્ષક-નોંધ** — {e['teacher_note']}")
        L.append("")
        cb = e.get("covered_by_topics") or []
        cbs = ", ".join(f"`{c}`" for c in cb) if cb else "—"
        L.append(f"**કૌશલ્ય** `{e['skill']}` · **તૈયારી કરાવતાં વાચન-દૃશ્યો** {cbs}")

L.append("")
L.append("---")
L.append("")
L.append("## કવરેજ-અહેવાલ")
L.append("")
n_found = len(cov["blocks_found"])
answered = set(cov["blocks_answered"])
if not cov["unanswered"]:
    L.append(f"### છપાયેલા બ્લૉક ({n_found}) — બધા ઉકેલાયા")
else:
    L.append(f"### છપાયેલા બ્લૉક ({n_found})")
L.append("")
for i, b in enumerate(cov["blocks_found"], 1):
    L.append(f"{i}. {b}" + (" ✓" if b in answered else ""))
L.append("")
L.append("### વણઉકેલ્યા બ્લૉક")
L.append("")
if not cov["unanswered"]:
    L.append("કોઈ નહીં — છપાયેલો દરેક બ્લૉક ઉકેલાયો છે.")
else:
    for b in cov["unanswered"]:
        L.append(f"- {b}")
L.append("")
L.append(f"### વાચન-દૃશ્ય સાથે ન જોડાયેલા એકમ ({len(cov['unmapped'])})")
L.append("")
L.append("આ એકમોને કોઈ વાચન-દૃશ્ય તૈયાર કરતું નથી, એટલે એમનું જોડાણ ઉપજાવ્યું નથી.")
L.append("")
for u in cov["unmapped"]:
    L.append(f"- **`{u['exercise_id']}`** ({u['exercise_group']}) — {u['reason']}")
L.append("")
L.append("### નોંધ")
L.append("")
L.append(cov["_note"])
L.append("")

(OUT / "exercise_solutions.md").write_text("\n".join(L), encoding="utf-8")
print("wrote exercise_solutions.json (verbatim copy) and exercise_solutions.md")
print("exercises:", len(ex), "groups:", len(groups), "unmapped:", len(cov["unmapped"]))
