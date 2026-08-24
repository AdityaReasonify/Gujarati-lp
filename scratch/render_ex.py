#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render exercise_solutions.json -> exercise_solutions.md (GSEB Gujarati LP pack).

Format reverse-engineered from output6/ch04/exercise_solutions.md and verified
byte-for-byte against it before use.
"""
import json
import sys


def blockquote(text):
    return "\n".join("> " + ln if ln.strip() else ">" for ln in text.split("\n"))


def render(d):
    out = []
    A = out.append

    A("# સ્વાધ્યાય — ઉકેલ")
    A("")
    A("**પાઠ:** %s  " % d["chapter_name"])
    A("**વિષય:** %s · **ધોરણ:** %s  " % (d["subject"], d["grade"]))
    A("**chapter_id:** `%s` · **plan_id:** `%s`" % (d["chapter_id"], d["plan_id"]))
    A("")
    A("> આ પાઠના છાપેલા દરેક સ્વાધ્યાય-બ્લોકના ઉકેલ અહીં જ છે. સ્વાધ્યાય કદી teaching topic નથી —")
    A("> `learning_plan_logical.json` તેને ભણાવતું નથી, આ ફાઇલ તેને ઉકેલે છે.")
    A("")

    exercises = d["exercises"]
    cr = d["coverage_report"]

    # groups in printed order, taken from the exercise list itself
    groups = list(dict.fromkeys(e["exercise_group"] for e in exercises))
    counts = {g: sum(1 for e in exercises if e["exercise_group"] == g) for g in groups}

    A("## અનુક્રમ")
    A("")
    for g in groups:
        A("- %s — %d" % (g, counts[g]))
    A("")

    for g in groups:
        A("---")
        A("")
        A("## %s" % g)
        A("")
        for e in [x for x in exercises if x["exercise_group"] == g]:
            A("### `%s` · %s" % (e["exercise_id"], e["skill"]))
            A("")
            A("**પ્રશ્ન (છપાયેલો):**")
            A("")
            A(blockquote(e["prompt_verbatim"]))
            A("")
            A("**ઉત્તર:**")
            A("")
            A(e["answer"])
            A("")
            if e.get("values_filled_for_teaching"):
                A("**ભરેલી જગ્યાઓ / કોષ્ટક:**")
                A("")
                A(e["values_filled_for_teaching"])
                A("")
            if e.get("explanation"):
                A("**સમજૂતી:** %s" % e["explanation"])
                A("")
            if e.get("acceptable_alternatives"):
                A("**બીજા સ્વીકાર્ય ઉત્તર:**")
                A("")
                for alt in e["acceptable_alternatives"]:
                    A("- %s" % alt)
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
    A("## Coverage report")
    A("")
    A("| | |")
    A("|---|---|")
    A("| છપાયેલા બ્લોક મળ્યા | %d |" % len(cr["blocks_found"]))
    A("| ઉકેલાયેલા બ્લોક | %d |" % len(cr["blocks_answered"]))
    A("| કુલ entries | %d |" % len(exercises))
    unanswered = cr.get("unanswered") or []
    A("| બાકી (unanswered) | %s |"
      % ("—" if not unanswered else ", ".join(unanswered)))
    A("| મેપ ન થયેલા (unmapped) | %d |" % len(cr.get("unmapped") or []))
    A("")
    A("**છપાયેલા બ્લોક, છપાયેલા ક્રમમાં:**")
    A("")
    for b in cr["blocks_found"]:
        A("- %s" % b)
    A("")
    if cr.get("unmapped"):
        A("**કોઈ topic સાથે મેપ ન થયેલા entries:**")
        A("")
        for u in cr["unmapped"]:
            A("- %s · %s"
              % (", ".join("`%s`" % i for i in u["exercise_ids"]), u["exercise_group"]))
            A("")
            A("  %s" % u["reason"])
            A("")
    if cr.get("_note"):
        A("**નોંધ:** %s" % cr["_note"])

    return "\n".join(out) + "\n"


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as fh:
        data = json.load(fh)
    with open(dst, "w", encoding="utf-8") as fh:
        fh.write(render(data))
    print("wrote", dst)
