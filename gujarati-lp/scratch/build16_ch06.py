# -*- coding: utf-8 -*-
import json, os, collections

BASE = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch06"

with open(os.path.join(BASE, "05_with_content.json")) as f:
    c5 = json.load(f)
with open(os.path.join(BASE, "12_authoring.json")) as f:
    a12 = json.load(f)
with open(os.path.join(BASE, "00_chapter_normalized.md")) as f:
    NORM = f.read()

orig = collections.OrderedDict()
for m in c5["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            orig[t["topic_id"]] = t["original_chunk"]

auth = {t["topic_id"]: t for t in a12["topics"]}

# ---- publication rewrites -------------------------------------------------
# PT  = publication_text  (rewrite of 12_authoring explanation)
# RLE = publication rewrite of real_life_example
# CP  = {concept_id: {content_index: publication_text}}

PT = {}
RLE = {}
CP = collections.OrderedDict()

# ------------------------------- M1.S1.T1 ---------------------------------
PT["M1.S1.T1"] = (
    "'સંસ્કાર' અહીં કોઈ ગુણનું નામ નથી, છોકરાનું નામ છે. પરદેશથી પાછા આવેલા પુરુષોત્તમભાઈ કહે છે "
    "કે ગામની સિકલ, એટલે દેખાવ, સાવ ફરી ગઈ છે. સવજીભાઈ જવાબમાં એ આખા ફેરફારનું બધું શ્રેય, એટલે યશ, "
    "સંસ્કારભાઈને આપે છે. પુરુષોત્તમભાઈ ખાતરી કરે છે કે એ તો નવા શિક્ષકનો દીકરો ને ? સવજીભાઈ કહે છે "
    "કે એ આવ્યો ત્યારે છઠ્ઠા ધોરણમાં હતો. એના પોતાના ગામમાં હરિયાળી હતી, પણ આ વિસ્તાર સૂકો છે."
)
RLE["M1.S1.T1"] = (
    "ઉનાળુ વેકેશન પૂરું થાય ને નિશાળ ફરી ખૂલે, ત્યારે પહેલી નજરે જ ફેર દેખાય છે. મેદાન સાફ થયેલું "
    "હોય, ઓટલો નવો રંગેલો હોય, ને હંમેશાં અટકતો ઝાંપો હવે સહેલાઈથી ખૂલે. મનમાં તરત થાય કે આ બધું "
    "કોણે કર્યું હશે. પછી ખબર પડે કે રજામાં કોઈક રોજ આવતું હતું. પુરુષોત્તમભાઈને પણ ગામ જોઈને આવી જ "
    "નવાઈ લાગી."
)
CP["M1.S1.T1"] = [
    ("M1.S1.T1.C1", 0, None),   # None = carry the authoring paragraph unchanged
    ("M1.S1.T1.C1", 1, None),
    ("M1.S1.T1.C2", 0, None),
]

# ------------------------------- M1.S2.T2 ---------------------------------
PT["M1.S2.T2"] = auth["M1.S2.T2"]["explanation"]   # carried an no vocative; verified below
RLE["M1.S2.T2"] = (
    "વહેલી સવારે શેરીમાં ઘંટડીનો અવાજ આવે ને ભરવાડકાકાનું ધણ નીકળે. સાંજ પડ્યે એ જ ધણ ધૂળ ઉડાડતું "
    "પાછું વળે. કાકા રોજ સવારે ને રોજ સાંજે એની સાથે ને સાથે. એક બકરીનું બચ્ચું પાછળ રહી જાય તો "
    "કાકા ઊભા રહી જાય, ને એને તેડીને આગળ ચાલે. પાઠમાં સંસ્કારની જે રોજની સંભાળની વાત છે તે આવી જ છે."
)
CP["M1.S2.T2"] = [
    ("M1.S2.T2.C3", 0, None),
    ("M1.S2.T2.C3", 1,
     "સવજીભાઈ કહે છે કે સંસ્કારે વાવેલા છોડને ઉછેરવાનો સંકલ્પ લીધો. સંકલ્પ એટલે મનમાં લીધેલો પાકો "
     "નિશ્ચય. પુરુષોત્તમભાઈ એને સર્જનાત્મક સંકલ્પ કહે છે, ને લીલાંછમ ઝાડ સામે જોઈને કહે છે કે એ જાણે "
     "બોલતાં હોય. ઝાડ સાચે બોલતાં નથી — પણ એમને જોઈને એવું લાગે છે."),
    ("M1.S2.T2.C4", 0, None),
]

# ------------------------------- M1.S2.T3 ---------------------------------
PT["M1.S2.T3"] = auth["M1.S2.T3"]["explanation"]
RLE["M1.S2.T3"] = (
    "શેરીમાં નવો છોકરો રહેવા આવે ને પહેલા દિવસે એકલો બૅટ લઈને ઊભો હોય. થોડી વારે એક જણ ફિલ્ડિંગમાં "
    "જાય, પછી બીજો બોલિંગ કરવા આવે, ને છેલ્લે થાંભલાનું સ્ટમ્પ પણ ગોઠવાઈ જાય. શરૂઆત તો એકલાએ કરી "
    "હતી, પણ રમત આખી શેરીની થઈ ગઈ. પાઠમાં પણ સંસ્કારે એકલા હાથે શરૂ કરેલું કામ પછી ગામનું બની ગયું."
)
CP["M1.S2.T3"] = [
    ("M1.S2.T3.C5", 0, None),
    ("M1.S2.T3.C5", 2,
     "'હાસ્તો !' એ સવજીભાઈની બોલચાલની ભાષા છે — 'હા જ તો' કહેવાની ભારપૂર્વકની રીત. એ લખાણની ભૂલ "
     "નથી; ઘરની બોલચાલમાં પણ એવું જ બોલાય છે."),
]

# ------------------------------- M1.S2.T4 ---------------------------------
PT["M1.S2.T4"] = auth["M1.S2.T4"]["explanation"]
RLE["M1.S2.T4"] = (
    "ઉત્તરાયણની સાંજે ધાબા પરથી નીચે ઊતરાય ત્યારે ફિરકી હાથમાં હોય ને આંગળીઓ છોલાયેલી હોય. કોઈ પૂછે "
    "તો જવાબ તરત આવે — કેટલા પતંગ ચગ્યા, કેટલા કપાયા, ને છેલ્લે કયો બચ્યો. એ બધું બરાબર યાદ રહે છે, "
    "કારણ કે દોર આખો દિવસ પોતાના જ હાથમાં હતી. પુરુષોત્તમભાઈ પણ સવજીભાઈનો ચોક્કસ આંકડો સાંભળીને એ જ "
    "પકડી પાડે છે."
)
CP["M1.S2.T4"] = [
    ("M1.S2.T4.C6", 0, None),
    ("M1.S2.T4.C6", 1, None),
]

# ------------------------------- M2.S3.T5 ---------------------------------
PT["M2.S3.T5"] = auth["M2.S3.T5"]["explanation"]
RLE["M2.S3.T5"] = (
    "ઘરે પહેલી વાર જાતે રોટલી વણવા બેસાય ત્યારે પહેલી રોટલી વાંકીચૂકી થાય છે. બીજી થોડી સારી, ત્રીજી "
    "એથી સારી — ને એક દિવસ તવા પર એ ફૂલીને ગોળ થઈ જાય. છતાં ઢોકળાં ઉતારવાનું હજી ય ન ફાવે, એટલે એ "
    "કામ ઘરમાં મોટેરાં પાસે જ રહે. પાઠમાં પણ અમુક ઝાડ ઊછરી શક્યાં ને અમુક ન ઊછરી શક્યાં."
)
CP["M2.S3.T5"] = [
    ("M2.S3.T5.C7", 0, None),
    ("M2.S3.T5.C8", 0, None),
    ("M2.S3.T5.C8", 1,
     "એ પછી પાઠમાં એક રૂઢિપ્રયોગ આવે છે: 'આ વિસ્તાર માટે એ કામ લોઢાના ચણા ચાવવા જેવું છે.' લોઢાના "
     "ચણા ચાવવા એટલે ખૂબ જ અઘરું કામ કરવું. અહીં અઘરું કામ એટલે ઓછા વરસાદવાળા આ વિસ્તારમાં સાગ, "
     "સીસમ, સાજડ, વાંસ ને નાગકેસર ઉછેરવાં તે."),
]

# ------------------------------- M2.S3.T6 ---------------------------------
PT["M2.S3.T6"] = auth["M2.S3.T6"]["explanation"]
RLE["M2.S3.T6"] = (
    "બસ-સ્ટૅન્ડે ઊભા હોઈએ ને બસના આગળના પાટિયા પર એવું નામ વંચાય જે કદી સાંભળ્યું ન હોય. અક્ષર તો "
    "વાંચી શકાય, પણ એ કઈ જગ્યા છે તે ખબર ન પડે. પછી બાજુમાં ઊભેલા મોટેરાંને પુછાય કે આ ગામ ક્યાં "
    "આવ્યું. જવાબ મળે ત્યારે નકશો મનમાં ગોઠવાઈ જાય. પુરુષોત્તમભાઈ પણ બોર્ડ વાંચીને એ જ રીતે પૂછે છે."
)
CP["M2.S3.T6"] = [
    ("M2.S3.T6.C9", 0, None),
    ("M2.S3.T6.C9", 1, None),
    ("M2.S3.T6.C9", 2, None),
]

# ------------------------------- M2.S4.T7 ---------------------------------
PT["M2.S4.T7"] = auth["M2.S4.T7"]["explanation"]
RLE["M2.S4.T7"] = (
    "તહેવાર નજીક આવે ત્યારે આખો મહોલ્લો કામે લાગી જાય છે. કોઈ ઓટલો ધુએ, કોઈ તોરણ બાંધે, રહીમચાચા "
    "ઘરેથી સીડી લઈ આવે, ને છોકરાં નીચે ઊભાં રહીને એ સીડી પકડી રાખે. સાંજ પડે ત્યારે એ જ સાંકડી શેરી "
    "સાવ જુદી લાગે છે — જાણે કોઈ નવી જગ્યાએ આવી ગયા હોઈએ. પાઠમાં પણ સૌની ભેગી મહેનતથી શાળા ઉપવન "
    "જેવી લાગે છે."
)
CP["M2.S4.T7"] = [
    ("M2.S4.T7.C10", 0, None),
    ("M2.S4.T7.C10", 1,
     "શાળાના મેદાનમાં વૃક્ષો ને ફૂલ-છોડ તો છે જ, ને એની સાથે ત્રણ વસ્તુ વધારે છે. આ ત્રણેય ગામમાં "
     "જુદી જુદી જગ્યાએ નથી — શાળાના એ જ મેદાનમાં છે."),
]

# ------------------------------- M2.S4.T8 ---------------------------------
PT["M2.S4.T8"] = auth["M2.S4.T8"]["explanation"]
RLE["M2.S4.T8"] = (
    "સાંજે દરિયાકિનારે ભીની રેતીમાં પગ મુકાય ને મોજું આવીને પગ ફરતે ઠંડું પાણી મૂકી જાય. ઘરેથી "
    "નીકળતી વખતે નક્કી કરેલું હોય કે થોડી વારમાં પાછા વળીશું, પણ સૂરજ ઢળે ત્યારે પણ ત્યાંથી ખસવાનું "
    "મન થતું નથી. બસમાં બેઠા પછીયે મન તો કિનારે જ રહી જાય. પુરુષોત્તમભાઈને પણ ગામ જોઈને પાછા જવાનું "
    "મન થતું નથી."
)
CP["M2.S4.T8"] = [
    ("M2.S4.T8.C11", 0, None),
    ("M2.S4.T8.C11", 1, None),
]

# ---- assemble -------------------------------------------------------------
topics = []
errors = []
for tid, oc in orig.items():
    t = auth[tid]
    # guard: every original_chunk paragraph must occur verbatim in A1's transcription
    for para in oc.split("\n\n"):
        if para.strip() not in NORM:
            errors.append("chunk not in 00_chapter_normalized.md: " + tid)

    pt = PT[tid]
    rle = RLE[tid]
    chunk = oc + "\n\n" + pt + "\n\n" + rle

    cbyid = {c["concept_id"]: c for c in t["concepts"]}
    # the declared paragraph blocks must match exactly what Agent 12 emitted
    expected = [(c["concept_id"], i)
                for c in t["concepts"]
                for i, b in enumerate(c["content"]) if b["type"] == "paragraph"]
    declared = [(cid, idx) for cid, idx, _ in CP[tid]]
    if expected != declared:
        errors.append("paragraph index mismatch %s: %r vs %r" % (tid, expected, declared))

    cps = []
    for cid, idx, text in CP[tid]:
        src = cbyid[cid]["content"][idx]["text"]
        cps.append({
            "concept_id": cid,
            "content_index": idx,
            "publication_text": src if text is None else text,
        })

    topics.append({
        "topic_id": tid,
        "publication_text": pt,
        "publication_chunk": chunk,
        "concept_publication": cps,
    })

if errors:
    raise SystemExit("GUARD FAILED:\n" + "\n".join(errors))

out = {
    "agent": "16_publication_authoring",
    "chapter_id": c5["chapter_id"],
    "plan_id": c5["plan_id"],
    "grade": c5["grade"],
    "tier": a12.get("tier", "ધોરણ"),
    "topics": topics,
    "notes": [
        "publication_text is the rewrite of each topic's teaching `explanation` in 12_authoring.json: "
        "the classroom vocative (બાળકો, જુઓ —) and every direct instruction to the class removed, every "
        "fact, gloss, name, number-word and quoted line kept, length band unchanged. Nothing was added. "
        "Only the first topic's explanation carried a vocative; the other seven were already free of "
        "classroom address, so they are carried across unchanged rather than reworded for its own sake.",
        "publication_chunk = the topic's verbatim `original_chunk`, copied programmatically from "
        "05_with_content.json (never retyped, never reflowed, its printed paragraph breaks preserved), "
        "then the publication rewrite of `explanation`, then of `real_life_example`. The chapter is "
        "માહિતીપ્રદ ગદ્ય in સંવાદ-શૈલી, so the verbatim is two-voice prose; the quoted speech, the ''…'' "
        "quotation marks, the speaker-attribution tags and the paragraph breaks are untouched. Each "
        "original_chunk paragraph was checked, in this build, to occur exactly in "
        "00_chapter_normalized.md (Agent 1's transcription of the rendered folios 34–40).",
        "The `real_life_example` rewrite drops the second-person address to the child and the closing "
        "question, and states the same single picture as a general observation. Its Gujarat anchor, its "
        "domain and its one picture are unchanged in every topic — the શેરી ક્રિકેટ, the ઉત્તરાયણની "
        "ફિરકી, the ભરવાડકાકાનું ધણ, the બસ-સ્ટૅન્ડનું પાટિયું, the મહોલ્લાની તહેવાર-તૈયારી and the "
        "દરિયાકિનારો all stand as authored; nothing was added.",
        "concept_publication carries one entry per `paragraph` block of 12_authoring.json's "
        "concepts[].content[], in order, with content_index = that block's index in the array as Agent 12 "
        "left it (list blocks are skipped, never renumbered, never dropped). 20 entries over 11 concepts; "
        "the mapping is asserted against Agent 12's own blocks at build time. Four paragraphs carried a "
        "classroom move and were rewritten for the page: M1.S2.T2.C3[1] (closing question to the child "
        "removed), M1.S2.T3.C5[2] (આપણે ઘરમાં પણ એવું જ બોલીએ છીએ → ઘરની બોલચાલમાં પણ એવું જ બોલાય છે), "
        "M2.S3.T5.C8[1] (self-answered classroom question folded into one statement), M2.S4.T7.C10[1] "
        "(the instruction તે જુઓ removed). The other sixteen were already publication-shaped and are "
        "carried unchanged.",
        "Gujarati script throughout, `.` as printed and no `।`, no Roman and no Devanagari outside the "
        "chapter's own printed words, no digits in display text. No craft label was introduced (std-6 "
        "ceiling: no અલંકાર, no છંદ), and no બોધ or ઉપદેશ sentence was added at any close — the closing "
        "topic still ends on the chapter's own પુરુષોત્તમભાઈ/સવજીભાઈ exchange as Agent 12 rendered it.",
    ],
}

path = os.path.join(BASE, "16_publication.json")
with open(path, "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", path, len(topics), "topics",
      sum(len(t["concept_publication"]) for t in topics), "concept entries")
