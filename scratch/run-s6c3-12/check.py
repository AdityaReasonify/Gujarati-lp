# -*- coding: utf-8 -*-
import json, re, sys

P = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch03/12_authoring.json"
S = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch03/05_with_content.json"

d = json.load(open(P, encoding="utf-8"))
src = json.load(open(S, encoding="utf-8"))

chunks, concepts, kterms = {}, {}, {}
for m in src["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            chunks[t["topic_id"]] = t["original_chunk"]
            concepts[t["topic_id"]] = [c["concept_id"] for c in t["concepts"]]
            kterms[t["topic_id"]] = t["key_terms"]

bad = []
DEVA = re.compile(r'[ऀ-ॿ]')
ROMAN = re.compile(r'[A-Za-z]')
DIGIT = re.compile(r'[0-9૦-૯]')
BANNED = ["જોઈએ", "બોધ", "સંદેશ", "શિખામણ", "ઉપદેશ", "।"]
DISPLAY = ["explanation","real_life_example","brief_summary","summary","detailed_summary"]

def scan(tid, field, text):
    if DEVA.search(text): bad.append((tid, field, "DEVANAGARI"))
    if ROMAN.search(text): bad.append((tid, field, "ROMAN", ROMAN.findall(text)))
    if DIGIT.search(text): bad.append((tid, field, "DIGIT", DIGIT.findall(text)))
    for b in BANNED:
        if b in text: bad.append((tid, field, "BANNED:" + b))

seen_ids = set()
for t in d["topics"]:
    tid = t["topic_id"]
    ch = chunks[tid]
    for f in DISPLAY:
        scan(tid, f, t[f])
    for i, x in enumerate(t["concept_bullets"] + t["important_points"]):
        scan(tid, "bullet", x)
    for c in t["concepts"]:
        if c["concept_id"] not in concepts[tid]:
            bad.append((tid, "concept_id mismatch", c["concept_id"]))
        for blk in c["content"]:
            if blk["type"] == "paragraph": scan(tid, "para", blk["text"])
            else:
                for it in blk["items"]: scan(tid, "list", it)
    # recall
    if not (2 <= len(t["recall_questions"]) <= 3):
        bad.append((tid, "rq count", len(t["recall_questions"])))
    for n, q in enumerate(t["recall_questions"], 1):
        if q["id"] != f"{tid}.RQ{n}" or q["legacy_id"] != f"{tid}.TR{n}":
            bad.append((tid, "rq id", q["id"], q["legacy_id"]))
        if q["id"] in seen_ids: bad.append((tid, "dup rq id", q["id"]))
        seen_ids.add(q["id"])
        if q["bloom_level"] != q["bloom_level"].lower():
            bad.append((tid, "bloom case", q["bloom_level"]))
        if q["bloom_level"] not in ("remember","understand","apply","analyze","evaluate","create"):
            bad.append((tid, "bloom value", q["bloom_level"]))
        if q["difficulty"] not in ("easy","medium","hard"):
            bad.append((tid, "difficulty", q["difficulty"]))
        if not q["answer"].strip(): bad.append((tid, "empty answer", q["id"]))
        scan(tid, "rq_prompt", q["prompt"])
        scan(tid, "rq_answer", q["answer"])
    # bhasha bodh headwords in chunk
    for e in t["shabdarth"]:
        if e["shabd"] not in ch: bad.append((tid, "shabdarth not in chunk", e["shabd"]))
        if e["prakar"] not in ("તત્સમ","તદ્ભવ","દેશ્ય","આગત","કાવ્ય-રૂપ"):
            bad.append((tid, "prakar", e["prakar"]))
    for e in t["samanarthi"]:
        if e["shabd"] not in ch: bad.append((tid, "samanarthi not in chunk", e["shabd"]))
    for e in t["vilom"]:
        if e["shabd"] not in ch: bad.append((tid, "vilom not in chunk", e["shabd"]))
    for e in t["vyakaran"]:
        if e["bindu"] not in ("નામ","સર્વનામ","વિશેષણ","ક્રિયાપદ","કાળ","વચન","જાતિ","રૂઢિપ્રયોગ","કહેવત",
                              "વિરામચિહ્નો","જોડાક્ષર","ક્રિયાવિશેષણ","સંયોજક","વાક્યના પ્રકારો",
                              "ઉપસર્ગ-પ્રત્યય","દ્વિરુક્ત / રવાનુકારી શબ્દો","શબ્દસમૂહ માટે એક શબ્દ",
                              "અનુસ્વાર","શબ્દકોશ ક્રમ"):
            bad.append((tid, "bindu not canonical", e["bindu"]))
    if not (3 <= len(t["shabdarth"]) <= 5): bad.append((tid,"shabdarth band",len(t["shabdarth"])))
    if len(t["samanarthi"]) > 2: bad.append((tid,"samanarthi band",len(t["samanarthi"])))
    if len(t["vilom"]) > 1: bad.append((tid,"vilom band",len(t["vilom"])))
    if len(t["vyakaran"]) != 1: bad.append((tid,"vyakaran band",len(t["vyakaran"])))
    if t["figures_of_speech"] != []: bad.append((tid,"fos not empty"))
    if t["rhyme_scheme"] is not None: bad.append((tid,"rhyme not null"))
    if not (3 <= len(t["concept_bullets"]) <= 4): bad.append((tid,"bullets",len(t["concept_bullets"])))
    if not (3 <= len(t["important_points"]) <= 4): bad.append((tid,"points",len(t["important_points"])))
    if not t["estimated_exchanges"].isdigit(): bad.append((tid,"exchanges",t["estimated_exchanges"]))
    if not (3 <= len(kterms[tid]) <= 6): bad.append((tid,"A5 key_terms band",len(kterms[tid])))

for m in d["modules"]:
    if not (5 <= len(m["difficult_words"]) <= 10):
        bad.append((m["module_id"], "difficult_words", len(m["difficult_words"])))
    for w in m["difficult_words"]:
        scan(m["module_id"], "dw", w["meaning"]); scan(m["module_id"], "dw", w["example"])
        # example must not reuse the chapter's own line
        for tid, ch in chunks.items():
            if w["example"] in ch: bad.append((m["module_id"],"dw example from text",w["word"]))

order_src = list(chunks.keys())
order_out = [t["topic_id"] for t in d["topics"]]
if order_src != order_out: bad.append(("ORDER", order_src, order_out))

print("topics:", len(d["topics"]), "| tier:", d["tier"], "| grade:", d["grade"])
if bad:
    for b in bad: print("FAIL", b)
else:
    print("ALL CHECKS PASS")
