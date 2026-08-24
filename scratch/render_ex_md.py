# -*- coding: utf-8 -*-
import json, sys

def bq(text):
    return "\n".join("> " + ln for ln in str(text).split("\n"))

def render(d):
    L = []
    A = L.append
    cov = d["coverage_report"]
    blocks = cov["blocks_found"]
    answered = cov["blocks_answered"]
    ex = d["exercises"]
    A("# સ્વાધ્યાય — ઉકેલ")
    A("")
    A("**%s** · ધોરણ %s · %s" % (d["chapter_name"], d["grade"], d["subject"]))
    A("")
    A("| | |")
    A("|---|---|")
    A("| `chapter_id` | `%s` |" % d["chapter_id"])
    A("| `plan_id` | `%s` |" % d["plan_id"])
    A("| છપાયેલા સ્વાધ્યાય-બ્લૉક | %d |" % len(blocks))
    A("| ઉત્તર અપાયેલા બ્લૉક | %d |" % len(answered))
    A("| કુલ પ્રશ્ન-એકમ | %d |" % len(ex))
    A("")
    A("> સ્વાધ્યાય કદી શીખવવાનો ટૉપિક નથી. છપાયેલો દરેક સ્વાધ્યાય-બ્લૉક ફક્ત આ જ ફાઇલમાં ઉકેલાયો છે.")
    A("")
    A("---")
    A("")
    cur = None
    for e in ex:
        g = e["exercise_group"]
        if g != cur:
            cur = g
            A("## %s" % g)
            A("")
        A("### `%s`" % e["exercise_id"])
        A("")
        A("**પ્રશ્ન (છપાયેલો)**")
        A("")
        A(bq(e["prompt_verbatim"]))
        A("")
        if e.get("is_model_answer"):
            A("**ઉત્તર** · *એક શક્ય ઉત્તર (નમૂનારૂપ)*")
        else:
            A("**ઉત્તર**")
        A("")
        A(bq(e["answer"]))
        A("")
        if e.get("values_filled_for_teaching"):
            A("**ભરેલા રૂપે (વર્ગમાં બતાવવા)**")
            A("")
            A(bq(e["values_filled_for_teaching"]))
            A("")
        if e.get("acceptable_alternatives"):
            A("**સ્વીકાર્ય બીજાં રૂપ**")
            A("")
            for alt in e["acceptable_alternatives"]:
                A("- %s" % alt)
            A("")
        A("**સમજૂતી** — %s" % e["explanation"])
        A("")
        if e.get("teacher_note"):
            A("**શિક્ષક-નોંધ** — %s" % e["teacher_note"])
            A("")
        topics = e.get("covered_by_topics") or []
        if topics:
            A("**કૌશલ્ય** `%s` · **તૈયારી કરાવતાં વાચન-દૃશ્યો** %s"
              % (e["skill"], ", ".join("`%s`" % t for t in topics)))
        else:
            A("**કૌશલ્ય** `%s` · **તૈયારી કરાવતાં વાચન-દૃશ્યો** —" % e["skill"])
        A("")
    A("---")
    A("")
    A("## કવરેજ-અહેવાલ")
    A("")
    unanswered = cov.get("unanswered") or []
    if not unanswered:
        A("### છપાયેલા બ્લૉક (%d) — બધા ઉકેલાયા" % len(blocks))
    else:
        A("### છપાયેલા બ્લૉક (%d)" % len(blocks))
    A("")
    for i, b in enumerate(blocks, 1):
        A("%d. %s %s" % (i, b, "✓" if b in answered else "✗"))
    A("")
    A("### વણઉકેલ્યા બ્લૉક")
    A("")
    if not unanswered:
        A("કોઈ નહીં — છપાયેલો દરેક બ્લૉક ઉકેલાયો છે.")
    else:
        for b in unanswered:
            A("- %s" % b)
    A("")
    unmapped = cov.get("unmapped") or []
    A("### વાચન-દૃશ્ય સાથે ન જોડાયેલા એકમ (%d)" % len(unmapped))
    A("")
    if not unmapped:
        A("કોઈ નહીં — દરેક એકમ ઓછામાં ઓછા એક વાચન-દૃશ્ય સાથે જોડાયેલો છે.")
    else:
        A("આ એકમોને કોઈ વાચન-દૃશ્ય તૈયાર કરતું નથી, એટલે એમનું જોડાણ ઉપજાવ્યું નથી.")
        A("")
        for u in unmapped:
            A("- **`%s`** (%s) — %s" % (u["exercise_id"], u["exercise_group"], u["reason"]))
    A("")
    if cov.get("_note"):
        A("### નોંધ")
        A("")
        A(cov["_note"])
        A("")
    return "\n".join(L).rstrip("\n") + "\n"

if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        d = json.load(f)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(render(d))
    print("wrote", dst)
