# -*- coding: utf-8 -*-
import json, sys, collections

def bq(text):
    return "\n".join((("> " + ln) if ln else ">") for ln in str(text).split("\n"))

def render(d):
    L = []; A = L.append
    cov = d["coverage_report"]
    blocks = cov["blocks_found"]; answered = cov["blocks_answered"]
    unanswered = cov.get("unanswered") or []; unmapped = cov.get("unmapped") or []
    ex = d["exercises"]
    counts = collections.Counter(e["exercise_group"] for e in ex)
    A("# સ્વાધ્યાય — ઉકેલ"); A("")
    A("**પાઠ:** %s  " % d["chapter_name"])
    A("**વિષય:** %s · **ધોરણ:** %s  " % (d["subject"], d["grade"]))
    A("**chapter_id:** `%s` · **plan_id:** `%s`" % (d["chapter_id"], d["plan_id"])); A("")
    A("> આ પાઠના છાપેલા દરેક સ્વાધ્યાય-બ્લોકના ઉકેલ અહીં જ છે. સ્વાધ્યાય કદી teaching topic નથી —")
    A("> `learning_plan_logical.json` તેને ભણાવતું નથી, આ ફાઇલ તેને ઉકેલે છે."); A("")
    A("## અનુક્રમ"); A("")
    seen = []
    for e in ex:
        if e["exercise_group"] not in seen: seen.append(e["exercise_group"])
    for g in seen: A("- %s — %d" % (g, counts[g]))
    A("")
    cur = None
    for e in ex:
        g = e["exercise_group"]
        if g != cur:
            cur = g; A("---"); A(""); A("## %s" % g); A("")
        A("### `%s` · %s" % (e["exercise_id"], e["skill"])); A("")
        A("**પ્રશ્ન (છપાયેલો):**"); A(""); A(bq(e["prompt_verbatim"])); A("")
        A("**ઉત્તર:**"); A(""); A(e["answer"]); A("")
        if e.get("values_filled_for_teaching"):
            A("**ભરેલી જગ્યાઓ / કોષ્ટક:**"); A(""); A(e["values_filled_for_teaching"]); A("")
        A("**સમજૂતી:** %s" % e["explanation"]); A("")
        if e.get("acceptable_alternatives"):
            A("**બીજા સ્વીકાર્ય ઉત્તર:**"); A("")
            for alt in e["acceptable_alternatives"]: A("- %s" % alt)
            A("")
        if e.get("is_model_answer"):
            A("*(નમૂનારૂપ ઉત્તર — એક શક્ય જવાબ, એકમાત્ર જવાબ નહિ.)*"); A("")
        if e.get("teacher_note"):
            A("**શિક્ષક માટે:** %s" % e["teacher_note"]); A("")
        tp = e.get("covered_by_topics") or []
        if tp:
            A("**તૈયારી કરાવતાં topics:** %s" % ", ".join("`%s`" % t for t in tp))
        else:
            A("**તૈયારી કરાવતાં topics:** —")
        A("")
    A("---"); A(""); A("## Coverage report"); A("")
    A("| | |"); A("|---|---|")
    A("| છપાયેલા બ્લોક મળ્યા | %d |" % len(blocks))
    A("| ઉકેલાયેલા બ્લોક | %d |" % len(answered))
    A("| કુલ entries | %d |" % len(ex))
    A("| બાકી (unanswered) | %s |" % ("—" if not unanswered else str(len(unanswered))))
    A("| મેપ ન થયેલા (unmapped) | %s |" % ("—" if not unmapped else str(len(unmapped)))); A("")
    A("**છપાયેલા બ્લોક, છપાયેલા ક્રમમાં:**"); A("")
    for b in blocks: A("- %s" % b)
    A("")
    if unanswered:
        A("**વણઉકેલ્યા બ્લોક:**"); A("")
        for b in unanswered: A("- %s" % b)
        A("")
    if unmapped:
        A("**કોઈ topic સાથે મેપ ન થયેલા entries:**"); A("")
        for u in unmapped:
            head = "- `%s` · %s" % (u["exercise_id"], u.get("exercise_group", ""))
            if u.get("prompt_verbatim"):
                head += " — %s" % u["prompt_verbatim"]
            A(head); A("")
            A("  %s" % u["reason"]); A("")
    if cov.get("_note"):
        A("**નોંધ:** %s" % cov["_note"]); A("")
    return "\n".join(L).rstrip("\n") + "\n"

if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f: d = json.load(f)
    with open(dst, "w", encoding="utf-8") as f: f.write(render(d))
    print("wrote", dst)
