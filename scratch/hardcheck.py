import json, os
D = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch03"
m = json.load(open(os.path.join(D, "13_merged.json"), encoding="utf-8"))
T = {t["topic_id"]: t for mo in m["modules"] for s in mo["segments"] for t in s["topics"]}

def fields(t, keys=("explanation","real_life_example","brief_summary","summary","detailed_summary","publication_text")):
    out = {k: t[k] for k in keys}
    for rq in t["recall_questions"]:
        out["rq:"+rq["id"]] = rq["prompt"] + " " + rq["answer"]
    for c in t["concepts"]:
        for i, b in enumerate(c["content"]):
            out["c%s[%d]" % (c["concept_id"], i)] = json.dumps(b, ensure_ascii=False)
    return out

def allstr(t):
    return " ".join(fields(t).values())

res = []
def chk(name, cond, extra=""):
    res.append((("PASS" if cond else "FAIL"), name, extra))

# T1
t = T["M1.S1.T1"]
chk("T1 opening direction verbatim in chunk",
    "(કૌરવ અને પાંડવ કુમારો ખુલ્લા મેદાનમાં ઊભા છે. દૂર વૃક્ષો દેખાય છે.)" in t["original_chunk"])
chk("T1 explanation points at દૂર વૃક્ષો/વૃક્ષો as the ઝાડ", "વૃક્ષો" in t["explanation"] and "ઝાડ" in t["explanation"])
chk("T1 explanation names દુઃશાસન + another કુમાર",
    "દુઃશાસન" in t["explanation"] and any(x in t["explanation"] for x in ("દુર્યોધન","અર્જુન","યુધિષ્ઠિર")))
chk("T1 explanation reports the fear line and a reply",
    "ડર" in t["explanation"] and "સદ્ભાગ્ય" in t["explanation"])
INTERIOR = ["ને લાગ્યું","મનમાં થયું","ગભરાઈ ગય","ડરી ગય","વિચાર્યું કે મન"]
chk("T1 no unspoken interior state", not any(x in allstr(t) for x in INTERIOR),
    [x for x in INTERIOR if x in allstr(t)])

# T2
t = T["M1.S1.T2"]
for par in ["(ગુરુ દ્રોણાચાર્યનો પ્રવેશ થાય છે. સૌ કુમારો વિનયપૂર્વક પ્રણામ કરે છે.)","(એક સાથે)",
            "(ધીમા અવાજે)","(ઊંચા અવાજે)","(નકુલ તેના બંને હાથ, બે ધનુષ્ય સાથે ઊંચા કરે છે.)",
            "(દુરાધર સામે બે ડગલાં ચાલીને)"]:
    chk("T2 parenthetical verbatim: %s" % par[:28], par in t["original_chunk"])
JUDGE_BHIM = ["તોછડો","ગુસ્સાખોર","ઉદ્ધત","ખરાબ"]
chk("T2 no judging word on ભીમ", not any(x in allstr(t) for x in JUDGE_BHIM))
s = allstr(t)
chk("T2 ડરપોક/ચુગલીખોર attributed to ભીમ where used",
    ("ડરપોક" not in s and "ચુગલીખોર" not in s) or "ભીમ" in s,
    "present" if ("ડરપોક" in s or "ચુગલીખોર" in s) else "absent")

# T3
t = T["M1.S2.T3"]
DIRECTIVE3 = ["ધીરજ રાખો","રાહ જોવી જોઈએ","ઉતાવળ ન કરો","ધીરજ રાખવી જોઈએ"]
chk("T3 no directive built on બધાનો વારો આવશે", not any(x in allstr(t) for x in DIRECTIVE3))
JUDGE_DUR = ["સ્વાર્થી","ઘમંડી","ઉદ્ધત","ખરાબ","બેજવાબદાર","બડાઈખોર"]
chk("T3 no judging word on દુર્યોધન", not any(x in allstr(t) for x in JUDGE_DUR))
LORE = ["ધૃતરાષ્ટ્ર","પાંડુના","કુરુક્ષેત્ર","મહાભારત","યુદ્ધ","કૃષ્ણ"]
chk("T3 no Mahabharat lore for the count", not any(x in allstr(t) for x in LORE))

# T4
t = T["M1.S2.T4"]
chk("T4 explanation two voices", ("દ્રોણ" in t["explanation"] or "ગુરુજી" in t["explanation"]) and "યુધિષ્ઠિર" in t["explanation"])
chk("T4 second question reported", "બીજું શું શું દેખાય છે" in t["explanation"])
chk("T4 printed answer quoted", "મને એ ઝાડ દેખાય છે, આપ દેખાઓ છો, સૌ ભાઈઓ પણ દેખાય છે." in t["explanation"])
chk("T4 closing direction verbatim",
    "(યુધિષ્ઠિરને કશું સમજાતું નથી. તે નવાઈ પામી એક બાજુ ઊભો રહે છે.)" in t["original_chunk"])

# T5
t = T["M1.S2.T5"]
chk("T5 no judging word on દુર્યોધન", not any(x in allstr(t) for x in JUDGE_DUR))
chk("T5 દ્રોણનું ધીરજ line reported", "ધીરજ" in allstr(t))

# T6
t = T["M1.S3.T6"]
chk("T6 (કુમારોમાં હસાહસ થાય છે.) verbatim", "(કુમારોમાં હસાહસ થાય છે.)" in t["original_chunk"])
chk("T6 (સ્વગત) verbatim", "(સ્વગત)" in t["original_chunk"])
JUDGE_BH = ["મૂર્ખ","ખાઉધરો","બેધ્યાન","બુદ્ધિ વગરનો"]
chk("T6 no judging word on ભીમ", not any(x in allstr(t) for x in JUDGE_BH))
chk("T6 explanation lists his four items",
    all(x in t["explanation"] for x in ("પંખી","વૃક્ષો","ફળ","આકાશ")))

# T7
t = T["M1.S3.T7"]
for n in ("દીર્ઘતાલ","દુરોધર","દુરાચાર","દુર્મુખ"):
    chk("T7 printed name kept: %s" % n, n in t["original_chunk"])
chk("T7 દુરાધર spelling not merged into this topic", "દુરાધર" not in allstr(t) and "દુરાધર" not in t["original_chunk"])
chk("T7 અર્જુન clause stays inside the બધા turn",
    "એકલો અર્જુન ના, ના કહેવા હાથ હલાવે છે." in t["original_chunk"])
ADD7 = ["ગુસ્સો આવ્યો","ભરોસો ન રહ્યો","આશા હતી"]
chk("T7 nothing added past the two printed signs", not any(x in allstr(t) for x in ADD7))
chk("T7 નિરાશા quoted as printed", "ધૂળમાં મળ્યું" in allstr(t) or "નિરાશ" in allstr(t))

# T8
t = T["M2.S4.T8"]
chk("T8 explanation names દ્રોણ/ગુરુજી and અર્જુન",
    ("દ્રોણ" in t["explanation"] or "ગુરુજી" in t["explanation"]) and "અર્જુન" in t["explanation"])
chk("T8 turn line quoted", "મને પંખીની માત્ર લાલ આંખ જ દેખાય છે." in t["explanation"])
chk("T8 shot direction verbatim (no full stop before bracket)",
    "(અર્જુન બાણ છોડે છે. રૂના બનાવેલા પંખીની આંખ વીંધાય છે, તે નીચે પડે છે)" in t["original_chunk"])
COT = "રૂના બનાવેલા પંખી"
shot_fields = {k: v for k, v in fields(t).items() if "વીંધ" in v or "બાણ છોડ" in v or "નિશાન" in v}
chk("T8 every field describing the shot names the cotton bird",
    all(COT in v or "રૂનું બનાવેલું" in v for v in shot_fields.values()),
    list(shot_fields.keys()))
md = t["media"][0]
chk("T8 media prompt names the cotton model bird",
    "cotton wadding" in md["generation_prompt"] and "not a living creature" in md["generation_prompt"])
chk("T8 media prompt says no live bird in frame", "No live bird appears anywhere" in md["generation_prompt"])
chk("T8 media prompt: nothing shot / nothing hurt",
    "nothing has been shot and nothing is hurt" in md["generation_prompt"].lower())
chk("T8 media description names the cotton bird", COT in md["description"])
chk("T8 media teaching_notes names the cotton bird and the supervision caution",
    ("રૂનું બનાવેલું" in md["teaching_notes"] or COT in md["teaching_notes"]) and "ઘરે અજમાવવાની" in md["teaching_notes"])
chk("T8 negative_prompt refuses live/wounded bird",
    all(x in md["negative_prompt"] for x in ("live bird","wounded or bleeding bird","arrow piercing a living creature")))
UNPRINTED8 = ["સૌથી હોશિયાર","પહેલેથી ખબર","ભગવાનની કૃપા"]
chk("T8 no unprinted reason for અર્જુનની સફળતા", not any(x in allstr(t) for x in UNPRINTED8))

# T9
t = T["M2.S4.T9"]
DIRECT9 = ["એકાગ્રતા રાખો","એકાગ્ર થવું જોઈએ","ધ્યેય નક્કી કરવું જોઈએ","મન એક જગ્યાએ પરોવવું જોઈએ","આપણે એકાગ્ર"]
chk("T9 no directive to the child", not any(x in allstr(t) for x in DIRECT9))
BODH = ["બોધ","સંદેશ","શિખામણ","ઉપદેશ","આપણે શીખવું જોઈએ"]
chk("T9 no બોધ/ઉપદેશ closer in authored fields", not any(x in allstr(t) for x in BODH),
    [x for x in BODH if x in allstr(t)])
chk("T9 unfinished line kept unfinished in chunk",
    "બાણ તો ત્યારે જ છૂટશે, જ્યારે..." in t["original_chunk"])
COMPLETIONS = ["જ્યારે લક્ષ્ય સિવાય કશું ન દેખાય","જ્યારે મન એકાગ્ર થાય"]
chk("T9 sentence never completed", not any(x in allstr(t) for x in COMPLETIONS))
chk("T9 કુમારોના છેલ્લા શબ્દો quoted as theirs",
    "એકાગ્રતાની વાત બરાબર યાદ રાખીશું" in allstr(t) or "બધું જ સમજાઈ ગયું" in allstr(t))

# chapter-level
alltopics = " ".join(allstr(t) for t in T.values())
alldisplay = alltopics + " " + " ".join(o["objective_text"] for o in m["objectives"]) + " " + \
             " ".join(t["topic_name"] for t in T.values()) + " " + m["guiding_question"]
chk("chapter: no Mahabharat lore anywhere in display text",
    not any(x in alldisplay for x in ["કુરુક્ષેત્ર","ધૃતરાષ્ટ્ર","પાંડુના","કૃષ્ણ","મહાભારત"]),
    [x for x in ["કુરુક્ષેત્ર","ધૃતરાષ્ટ્ર","પાંડુના","કૃષ્ણ","મહાભારત","યુદ્ધ"] if x in alldisplay])
media_blob = json.dumps([md for t in T.values() for md in t["media"]], ensure_ascii=False)
chk("chapter: no Mahabharat lore in media strings",
    not any(x in media_blob for x in ["કુરુક્ષેત્ર","ધૃતરાષ્ટ્ર","કૃષ્ણ","મહાભારત"]))
chk("chapter: કૃતિ never called નાટક/એકાંકી in display text",
    "એકાંકી" not in alldisplay)
chk("chapter: no કૌરવ-vs-પાંડવ rivalry framing",
    not any(x in alldisplay for x in ["દુશ્મન","વેર","હરીફાઈ","શત્રુ"]))
# safety: real_life_example domain
WEAPON = ["ધનુષ્ય","બાણ","ગદા","તીર"]
bad = [t["topic_id"] for t in T.values() if any(w in t["real_life_example"] for w in WEAPON)]
chk("safety: no real_life_example puts a child near a weapon", not bad, bad)

print("%-5s %s" % ("", ""))
for st, name, extra in res:
    print("%-4s %s %s" % (st, name, ("| " + str(extra)) if extra and st == "FAIL" else ""))
print("\nTOTAL %d, FAIL %d" % (len(res), sum(1 for r in res if r[0] == "FAIL")))
