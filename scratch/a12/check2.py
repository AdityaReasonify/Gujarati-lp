# -*- coding: utf-8 -*-
import json, re
D = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch12/"
plan = json.load(open(D + "12_authoring.json"))
src = json.load(open(D + "05_with_content.json"))
chunks = {}
for m in src["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            chunks[t["topic_id"]] = t["original_chunk"]
allchunk = " ".join(chunks.values())

def display_strings(t):
    out = []
    for f in ("explanation","real_life_example","brief_summary","summary","detailed_summary"):
        out.append((f, t[f]))
    for f in ("concept_bullets","important_points"):
        for i,x in enumerate(t[f]): out.append(("%s[%d]"%(f,i), x))
    for c in t["concepts"]:
        for j,b in enumerate(c["content"]):
            if b["type"]=="paragraph": out.append(("%s.c%d.text"%(c["concept_id"],j), b["text"]))
            else:
                for k,it in enumerate(b["items"]): out.append(("%s.c%d.item%d"%(c["concept_id"],j,k), it))
    for q in t["recall_questions"]:
        out.append((q["id"]+".prompt", q["prompt"]))
        out.append((q["id"]+".answer", q["answer"]))
    for e in t["shabdarth"]: out.append(("shabdarth:"+e["shabd"], e["arth"]))
    for e in t["vyakaran"]:
        out.append(("vyakaran.udaharan", e["udaharan"])); out.append(("vyakaran.note", e["note"]))
    return out

problems = []
DIGITS = re.compile(r"[0-9०-९૦-૯]")
ROMAN = re.compile(r"[A-Za-z]")
DEVA = re.compile(r"[ऀ-ॿ]")

for t in plan["topics"]:
    tid = t["topic_id"]
    for name, s in display_strings(t):
        if DIGITS.search(s): problems.append("DIGIT %s %s :: %s" % (tid, name, s[:90]))
        if ROMAN.search(s): problems.append("ROMAN %s %s :: %s" % (tid, name, s[:90]))
        if DEVA.search(s): problems.append("DEVA %s %s :: %s" % (tid, name, s[:90]))
        if "।" in s: problems.append("DANDA %s %s" % (tid, name))
    # shabdarth headword present in this topic's chunk
    ch = chunks[tid]
    for e in t["shabdarth"]:
        w = e["shabd"]
        stem = w.split()[0]
        if stem not in ch:
            # try trimming trailing inflection
            ok = any(ch.find(stem[:i]) >= 0 and len(stem[:i]) >= 3 for i in range(len(stem), 2, -1) if stem[:i] in ch)
            problems.append("SHABDARTH-NOT-IN-CHUNK %s %s (loose=%s)" % (tid, w, ok))
    for e in t["samanarthi"]:
        if e["shabd"] not in ch and e["shabd"][:4] not in ch:
            problems.append("SAMANARTHI-HEAD-NOT-IN-CHUNK %s %s" % (tid, e["shabd"]))
    for e in t["vilom"]:
        if e["shabd"] not in ch and e["shabd"][:3] not in ch:
            problems.append("VILOM-HEAD-NOT-IN-CHUNK %s %s" % (tid, e["shabd"]))

# module difficult_words
for m in plan["modules"]:
    for dw in m["difficult_words"]:
        if dw["word"] not in allchunk and dw["word"][:4] not in allchunk:
            problems.append("DW-NOT-IN-CHAPTER %s %s" % (m["module_id"], dw["word"]))
        for k in ("meaning","example"):
            if DIGITS.search(dw[k]) or ROMAN.search(dw[k]) or DEVA.search(dw[k]) or "।" in dw[k]:
                problems.append("DW-SCRIPT %s %s %s" % (m["module_id"], dw["word"], k))
        if dw["example"] in allchunk:
            problems.append("DW-EXAMPLE-FROM-TEXT %s %s" % (m["module_id"], dw["word"]))
    if not (5 <= len(m["difficult_words"]) <= 10):
        problems.append("DW-COUNT %s %d" % (m["module_id"], len(m["difficult_words"])))

# banned vocabulary
BANNED = ["પછાત","જંગલી","અસભ્ય","અભણ","આ લોકો","એ લોકોની","વિચિત્ર રિવાજ","મૂરખ","નકામો","આળસુ"]
BOD = ["આપણે આપણી સંસ્કૃતિ જાળવવી જોઈએ","આ પાઠ આપણને શીખવે છે"]
for t in plan["topics"]:
    for name, s in display_strings(t):
        for b in BANNED + BOD:
            if b in s: problems.append("BANNED '%s' %s %s" % (b, t["topic_id"], name))

# T3 must not contain the word માર anywhere
t3 = [t for t in plan["topics"] if t["topic_id"] == "M1.S2.T3"][0]
for name, s in display_strings(t3):
    if re.search(r"(?<![\u0A80-\u0AFF])માર(?![\u0A80-\u0AFF])", s): problems.append("T3-CONTAINS-માર %s :: %s" % (name, s[:80]))

# T8 forbidden added-fact words
t8 = [t for t in plan["topics"] if t["topic_id"] == "M2.S5.T8"][0]
for name, s in display_strings(t8):
    for b in ["ચકડોળ","રમકડાં","ભજિયાં","જલેબી","ફજર"]:
        if b in s: problems.append("T8-ADDED '%s' %s" % (b, name))

# T7 correction sentence must travel with the સ્વયંવર mention, per field-group
CORR = "હવે મેળાનો હેતુ કન્યા પસંદગીનો રહ્યો નથી"
t7 = [t for t in plan["topics"] if t["topic_id"] == "M2.S4.T7"][0]
for f in ("explanation","detailed_summary"):
    if "સ્વયંવર" in t7[f] and CORR not in t7[f]:
        problems.append("T7-NO-CORRECTION in %s" % f)
for q in t7["recall_questions"]:
    if ("પરણી" in q["answer"] or "કન્યા પસંદગી" in q["answer"]) and CORR not in q["answer"]:
        problems.append("T7-NO-CORRECTION in %s" % q["id"])

# "જોઈએ" appears only where allowed
for t in plan["topics"]:
    for name, s in display_strings(t):
        for mt in re.finditer("જોઈએ", s):
            seg = s[max(0,mt.start()-60):mt.end()+5]
            if t["topic_id"] != "M2.S5.T9":
                problems.append("JOIYE %s %s :: %s" % (t["topic_id"], name, seg))

print("PROBLEMS:", len(problems))
for p in problems: print("  -", p)
