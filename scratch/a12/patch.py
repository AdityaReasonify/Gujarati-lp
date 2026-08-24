# -*- coding: utf-8 -*-
import json
P = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch12/12_authoring.json"
plan = json.load(open(P))
byid = {t["topic_id"]: t for t in plan["topics"]}

# 1. keep the printed form of ઘેરો as the shabdarth headword
t7 = byid["M2.S4.T7"]
for e in t7["shabdarth"]:
    if e["shabd"] == "ઘેરો":
        e["shabd"] = "ઘેરામાંથી"
        e["arth"] = "ઘેરો એટલે ચારે બાજુથી ઘેરીને ઊભેલું ટોળું; અહીં કન્યાઓના કૂંડાળામાંથી."

# 2. remove the '... જોઈએ' shaped rubric clause from a recall answer
t4 = byid["M1.S3.T4"]
q = t4["recall_questions"][2]
assert "આવવી જોઈએ" in q["answer"], q["answer"]
q["answer"] = q["answer"].replace(
    "પાઠ પ્રમાણે બે વાત આવવી જોઈએ :",
    "પાઠ પ્રમાણે બે વાત આવે :")

json.dump(plan, open(P, "w"), ensure_ascii=False, indent=1)
print("patched")
