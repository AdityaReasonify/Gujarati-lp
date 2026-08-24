# -*- coding: utf-8 -*-
import json, re, sys, os
HERE = "/Users/aditya/Downloads/Gujarati-lp/scratch"
sys.path.insert(0, HERE)
from a12_part1 import T1, T2, T3, T4
from a12_part2 import T5, T6, T7, T8

MODULES = [
 {"module_id": "M1",
  "difficult_words": [
    {"word": "સિકલ", "meaning": "ચહેરો, દેખાવ",
     "example": "નવો રંગ થતાં અમારા વર્ગખંડની સિકલ જ ફરી ગઈ."},
    {"word": "શ્રેય", "meaning": "યશ, જશ; સારા કામનું મળતું માન",
     "example": "શાળાની સફાઈનું શ્રેય આખા વર્ગને મળ્યું."},
    {"word": "હરિયાળી", "meaning": "લીલોતરી, ચારે બાજુ લીલાં ઝાડ-છોડ",
     "example": "ચોમાસા પછી ડુંગર પર હરિયાળી છવાઈ જાય છે."},
    {"word": "દરકાર", "meaning": "પરવા, કાળજી",
     "example": "દાદી ઘરના તુલસી-ક્યારાની બહુ દરકાર રાખે છે."},
    {"word": "સંકલ્પ", "meaning": "મનમાં લીધેલો પાકો નિશ્ચય",
     "example": "મેં રોજ વહેલા ઊઠવાનો સંકલ્પ લીધો છે."},
    {"word": "પરિશ્રમ", "meaning": "ખૂબ મહેનત",
     "example": "એના પરિશ્રમથી જ બગીચો આટલો સરસ થયો."},
    {"word": "ઘેઘૂર", "meaning": "ખૂબ ઘટાદાર, પાંદડાંથી ભરચક",
     "example": "ઘેઘૂર વડલા નીચે આખું ટોળું બેસી શકે છે."},
    {"word": "વડીલ", "meaning": "ઉંમરમાં મોટા ને માનનીય માણસ",
     "example": "ફળિયાના વડીલો સાંજે ઓટલે ભેગા થાય છે."}
  ],
  "overall_rhyme_scheme": None},
 {"module_id": "M2",
  "difficult_words": [
    {"word": "વનરાજી", "meaning": "ઝાડપાનની હાર, લીલોછમ ઝાડવાળો પ્રદેશ",
     "example": "બારીમાંથી દૂરની વનરાજી દેખાય છે."},
    {"word": "અહોભાવ", "meaning": "વખાણ ને માનથી ભરેલો મનનો ભાવ",
     "example": "એનું ચિત્ર જોઈને સૌ અહોભાવથી જોતાં રહ્યાં."},
    {"word": "મબલખ", "meaning": "પુષ્કળ, ખૂબ બધું",
     "example": "આ વર્ષે અમારા આંબે મબલખ કેરી આવી છે."},
    {"word": "ધગશ", "meaning": "કામ કરવાની ધગધગતી લગની",
     "example": "એની ધગશ જોઈને શિક્ષક પણ રાજી થયા."},
    {"word": "માવજત", "meaning": "સંભાળ રાખીને જતન કરવું",
     "example": "ગાયની માવજત દાદા જાતે કરે છે."},
    {"word": "ઉપવન", "meaning": "સુંદર બગીચો",
     "example": "શિયાળામાં એ ટેકરી આખી ઉપવન જેવી લાગે છે."},
    {"word": "સહયોગ", "meaning": "સાથે મળીને અપાતી મદદ",
     "example": "સૌના સહયોગથી નાટકની તૈયારી બે દિવસમાં થઈ ગઈ."},
    {"word": "પ્રદૂષિત", "meaning": "ખરાબ થયેલું, ગંદું બનેલું",
     "example": "કચરો નાખવાથી તળાવનું પાણી પ્રદૂષિત થયું."}
  ],
  "overall_rhyme_scheme": None}
]

NOTES = [
 "ધોરણ 6, tier ધોરણ (default). std-6.md §3 ની REGISTER/QUESTIONING/PACING હરોળ અને બે ceiling (કોઈ craft label નહીં; કોઈ theme-extraction નહીં) દરેક block લખતી વખતે ફરીથી લાગુ કરી છે.",
 "સ્વરૂપ ગદ્ય (સંવાદ-શૈલી માહિતીપ્રદ ગદ્ય) છે, એટલે આઠેય topic માં figures_of_speech [] અને rhyme_scheme null છે; બંને module માં overall_rhyme_scheme પણ null. 'આ લીલાંછમ ઝાડ પણ જાણે બોલે છે' અને 'શાળા તો ઉપવન જેવી લાગે છે' જેવી પંક્તિઓ ધોરણ-6 છત મુજબ લેબલ વગર, માત્ર સંવેદનથી નોંધી છે (M1.S2.T2 ના concept માં).",
 "key_terms Agent 5 નાં છે અને આઠેય topic માં છ-છ છે (band 3–6 ની ટોચ) — બદલ્યાં નથી. પણ 07_pitfalls.json ની ત્રણ correction એવી entry માગે છે જે એ યાદીમાં નથી: M1.S1.T1 માટે 'સંસ્કાર — અહીં એ છોકરાનું નામ છે', M1.S2.T2 માટે 'વાવવું' અને 'ઉછેરવું' ની સામસામી જોડ, અને M2.S3.T5 માટે 'લોઢાના ચણા ચાવવા'. ત્રણેય explanation માં પહેલા વપરાશના સ્થાને ગ્લોસ કરી છે અને concept_bullets / vyakaran માં પણ મૂકી છે; key_terms band ભરેલો હોવાથી ત્યાં ઉમેરી નથી. Agent 5 ને આ ત્રણ પર ધ્યાન દોરવું.",
 "07_pitfalls.json ના chapter-level નિયમો પાળ્યા છે: ગામ, જિલ્લો, 'પરદેશ' દેશ કે કોઈ સમુદાય ક્યાંય નામ આપ્યાં નથી; સંસ્કાર, શિવરામકાકા, સરતાનકાકા, સુશીલાબેન, નારાયણભાઈ, શ્રવણભાઈ, ભૂરાભાઈ ને એક પણ સંવાદ-પંક્તિ, હેતુ કે દૃશ્ય આપ્યું નથી; આંકડા માત્ર છાપેલા શબ્દરૂપે (અઢી દાયકા, પચીસેક વર્ષ, છઠ્ઠા ધોરણ, એકસો દસ, સાડત્રીસ) અને કોઈ બાદબાકી કે ટકાવારી નહીં; સ્વાધ્યાયના ઇરાદાપૂર્વક ખોટા ર/ળ-રૂપો ક્યાંય ટાંક્યાં નથી.",
 "08_sensitivity.json ની soft ધર્મ-સૂચના (M2.S3.T6) પાળી છે: નક્ષત્ર-વન ને સાચી સરકારી યોજના તરીકે, પરંપરામાં મૂળ ધરાવતી, રજૂ કરી છે — ન તો જ્યોતિષનો પાઠ, ન તો ખંડન. 'પરીક્ષામાં ઝળહળતી સફળતા' સવજીભાઈના પોતાના શબ્દો તરીકે જ રહી છે, કોઈ સામાન્ય સત્ય તરીકે નહીં, અને એ real_life_example કે કોઈ recall answer માં આવતી નથી.",
 "real_life_example નો domain ledger (દરેક દૃશ્ય પછી domain બદલ્યો; સળંગ બે વાર એક domain નહીં): T1 રોજિંદું જીવન (વેકેશન પછીનું નિશાળનું મેદાન) · T2 કામ-આજીવિકા (ભરવાડનું ધણ) · T3 રોજિંદું જીવન (શેરી ક્રિકેટ) · T4 તહેવાર-ઉત્સવ (ઉત્તરાયણનું ધાબું) · T5 ખાનપાન (ઘરે પહેલી રોટલી) · T6 કામ-આજીવિકા (બસ-સ્ટૅન્ડનું પાટિયું) · T7 રોજિંદું જીવન (મહોલ્લાની સહિયારી તૈયારી) · T8 ભૂગોળ-કુદરત (સાંજનો દરિયાકિનારો). એક પણ દૃશ્ય ઉપદેશ કે સૂચનામાં પૂરું થતું નથી.",
 "Agent 1 નું exercise_inventory વાપર્યું છે: M1.S1.T1 નું explanation 'ખોટો શબ્દ છેકો' બ્લૉક માટે જરૂરી સિકલ/શ્રેય/હરિયાળી-ના અર્થભેદ પર ઊભું છે, M1.S2.T4 વિરામચિહ્ન-યાદી પર, M2.S3.T6 જોડાક્ષર-બ્લૉક પર, M2.S4.T7 'વિશેષણ-નામ જોડકાં' અને વક્તા-ઓળખ પર. કોઈ સ્વાધ્યાય-ઉત્તર અહીં આપ્યો નથી — એ Agent 10 નું કામ છે.",
 "objective_text (Agent 2) ને અડ્યા નથી; આઠેય objective આ topic-બ્લૉકથી ખરેખર સિદ્ધ થાય છે, એટલે A2 ને પાછું મોકલવા જેવું કશું મળ્યું નથી.",
 "publication_text / publication_chunk, media અને સ્વાધ્યાયના ઉત્તર આ file માં લખ્યા નથી (Agent 16, Agent 9, Agent 10).",
 "કોઈ પણ PNG render વાંચ્યું નથી; આખું કામ 00_chapter_normalized.md અને 05_with_content.json ના original_chunk પરથી થયું છે."
]

TOPICS = [T1, T2, T3, T4, T5, T6, T7, T8]
OUT = {"tier": "ધોરણ", "grade": 6, "topics": TOPICS, "modules": MODULES, "notes": NOTES}

# ---------- validation ----------
GUJ = re.compile(r'[઀-૿]')
DEV = re.compile(r'[ऀ-ॿ]')
ROMAN = re.compile(r'[A-Za-z]')
DIGITS = re.compile(r'[0-9૦-૯]')

def toks(s):
    raw = s.split()
    alnum = [t for t in raw if any(ch.isalnum() for ch in t)]
    return len(raw), len(alnum)

problems = []

def child_text_strings(t):
    out = [("explanation", t["explanation"]), ("real_life_example", t["real_life_example"]),
           ("brief_summary", t["brief_summary"]), ("summary", t["summary"]),
           ("detailed_summary", t["detailed_summary"])]
    for i, b in enumerate(t["concept_bullets"]): out.append((f"concept_bullets[{i}]", b))
    for i, b in enumerate(t["important_points"]): out.append((f"important_points[{i}]", b))
    for c in t["concepts"]:
        for j, blk in enumerate(c["content"]):
            if blk["type"] == "paragraph": out.append((f"{c['concept_id']}.content[{j}]", blk["text"]))
            else:
                for k, it in enumerate(blk["items"]): out.append((f"{c['concept_id']}.content[{j}].items[{k}]", it))
    for q in t["recall_questions"]:
        out.append((q["id"] + ".prompt", q["prompt"]))
        out.append((q["id"] + ".answer", q["answer"]))
    for e in t["shabdarth"]: out.append(("shabdarth." + e["shabd"], e["arth"]))
    for e in t["vyakaran"]:
        out.append(("vyakaran.bindu", e["bindu"])); out.append(("vyakaran.udaharan", e["udaharan"]))
        out.append(("vyakaran.note", e["note"]))
    return out

DIRECTIVES = ["આપણે", "જોઈએ", "તમારે"]

for t in TOPICS:
    tid = t["topic_id"]
    for f in ("explanation", "real_life_example"):
        raw, al = toks(t[f])
        if not (55 <= al and raw <= 90):
            problems.append(f"{tid}.{f}: raw={raw} alnum={al} OUT OF BAND")
        print(f"{tid:12s} {f:20s} raw={raw:3d} alnum={al:3d}")
    b, s, d = len(t["brief_summary"]), len(t["summary"]), len(t["detailed_summary"])
    if not (b < s < d): problems.append(f"{tid}: summaries not strictly increasing {b}/{s}/{d}")
    if not (3 <= len(t["concept_bullets"]) <= 4): problems.append(f"{tid}: concept_bullets count")
    if not (3 <= len(t["important_points"]) <= 4): problems.append(f"{tid}: important_points count")
    if not (2 <= len(t["recall_questions"]) <= 3): problems.append(f"{tid}: recall count")
    if not (3 <= len(t["shabdarth"]) <= 5): problems.append(f"{tid}: shabdarth count {len(t['shabdarth'])}")
    if len(t["samanarthi"]) > 2: problems.append(f"{tid}: samanarthi count")
    if len(t["vilom"]) > 1: problems.append(f"{tid}: vilom count")
    if len(t["vyakaran"]) != 1: problems.append(f"{tid}: vyakaran count")
    for q in t["recall_questions"]:
        if not q["id"].startswith(tid + ".RQ"): problems.append(f"{tid}: bad rq id {q['id']}")
        if q["legacy_id"] != q["id"].replace(".RQ", ".TR"): problems.append(f"{tid}: bad legacy {q['id']}")
        if q["bloom_level"] != q["bloom_level"].lower(): problems.append(f"{tid}: bloom case")
        if not q["answer"].strip(): problems.append(f"{tid}: empty answer")
    for name, s_ in child_text_strings(t):
        if DEV.search(s_): problems.append(f"{tid}.{name}: DEVANAGARI")
        if ROMAN.search(s_): problems.append(f"{tid}.{name}: ROMAN")
        if DIGITS.search(s_): problems.append(f"{tid}.{name}: DIGIT")
        if "।" in s_: problems.append(f"{tid}.{name}: DANDA")
        if not GUJ.search(s_): problems.append(f"{tid}.{name}: no Gujarati")
    for f in ("explanation", "real_life_example", "brief_summary", "summary", "detailed_summary"):
        for d_ in DIRECTIVES:
            if d_ in t[f]: problems.append(f"{tid}.{f}: directive-word '{d_}'")
    for q in t["recall_questions"]:
        for d_ in DIRECTIVES:
            if d_ in q["answer"]: problems.append(f"{tid}.{q['id']}.answer: directive-word '{d_}'")

for m in MODULES:
    if not (6 <= len(m["difficult_words"]) <= 8):
        problems.append(f"{m['module_id']}: difficult_words count {len(m['difficult_words'])}")
    for w in m["difficult_words"]:
        for s_ in (w["word"], w["meaning"], w["example"]):
            if DEV.search(s_) or ROMAN.search(s_) or DIGITS.search(s_) or "।" in s_:
                problems.append(f"{m['module_id']}.{w['word']}: script/digit problem")

print("\n--- PROBLEMS ---")
for p in problems: print(p)
print("total:", len(problems))

path = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch06/12_authoring.json"
if "--write" in sys.argv:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(OUT, f, ensure_ascii=False, indent=1)
    print("WROTE", path, os.path.getsize(path))
