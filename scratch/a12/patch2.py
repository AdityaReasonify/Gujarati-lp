# -*- coding: utf-8 -*-
import json
P = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch12/12_authoring.json"
plan = json.load(open(P))
byid = {t["topic_id"]: t for t in plan["topics"]}

def rep(tid, old, new):
    t = byid[tid]
    assert old in t["explanation"], (tid, old)
    t["explanation"] = t["explanation"].replace(old, new)

# genre gate #3 — the fact/step must stand in the FIRST sentence, not the second
rep("M1.S2.T2",
    "બાળકો, જુઓ — હવે પાઠ એક ચોક્કસ મેળા પાસે લઈ જાય છે. દાહોદ જિલ્લાના",
    "બાળકો, જુઓ — દાહોદ જિલ્લાના")
rep("M1.S2.T3",
    "બાળકો, જુઓ — મેળાના દિવસે પહેલું કામ મેદાનની બરાબર વચ્ચે થાય છે. ત્યાં લાકડાનો",
    "બાળકો, જુઓ — મેળાના દિવસે મેદાનની બરાબર વચ્ચે લાકડાનો")
rep("M1.S3.T4",
    "હવે થાંભલાની ચારે બાજુ ચિત્ર ગોઠવાય છે.",
    "હવે થાંભલાની ચારે બાજુ કન્યાઓનું કૂંડાળું ગોઠવાય છે.")
rep("M2.S5.T9",
    "પાઠ છેલ્લે એક વાત મૂકીને પૂરો થાય છે :",
    "પાઠ છેલ્લે લેખકનું નિમંત્રણ મૂકે છે :")
rep("M2.S5.T9",
    "આ લેખકનું નિમંત્રણ છે.",
    "એટલે કે લેખક આપણને મેળામાં જવા બોલાવે છે.")

json.dump(plan, open(P, "w"), ensure_ascii=False, indent=1)
for tid in ("M1.S2.T2", "M1.S2.T3", "M1.S3.T4", "M2.S5.T9"):
    print(tid, len(byid[tid]["explanation"].split()), "|", byid[tid]["explanation"][:95])
