# -*- coding: utf-8 -*-
import json, io, collections, os

BASE = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch14"

with io.open(os.path.join(BASE, "00_chapter_normalized.md"), encoding="utf-8") as f:
    md_lines = f.read().split("\n")


def chunk(a, b):
    """1-indexed inclusive line range; drop [[..]] markers and blank lines."""
    out = []
    for ln in md_lines[a - 1:b]:
        s = ln.rstrip()
        if not s.strip():
            continue
        if s.lstrip().startswith("[["):
            continue
        out.append(s)
    return "\n".join(out)


SPANS = {
    "M1.S1.T1": (12, 34),
    "M1.S1.T2": (38, 74),
    "M1.S2.T3": (80, 120),
    "M2.S3.T4": (126, 174),
    "M2.S4.T5": (178, 196),
}

MODIFIED = {
    "M1.S1.T1": (
        "ઝલક શાળાએથી ઘરે આવીને મમ્મી વનિતાબેનને એક ખબર આપે છે — શાળામાં નોટિસ (લેખિત જાણ) આવી છે "
        "અને એક દિવસના પ્રવાસમાં આજવા-નિમેટા જવાનું છે. મમ્મી કહે છે કે એ જગ્યા વડોદરા પાસે છે અને "
        "ઝલક નાની હતી ત્યારે એ ત્યાં જઈ આવી છે. ઝલક બહેનપણીઓ સાથે બસમાં ગાવા-રમવાની ને ત્યાં જઈને "
        "તોફાન (મસ્તી) કરવાની મજાની વાત કરીને જવાની રજા માગે છે. મમ્મી હા કે ના કહેવાને બદલે એટલું "
        "કહે છે કે પપ્પા જોડે વાત કરી લઈએ."
    ),
    "M1.S1.T2": (
        "પપ્પા મહેશભાઈ અને નાનો ભાઈ મનન વાતમાં જોડાય છે. ઝલક કહે છે કે આજવા-નિમેટામાં મોટું સરોવર "
        "(તળાવ), મોટો બગીચો, લપસણી, હીંચકા અને જુદીજુદી રાઈડ્સ છે, રાત્રે લાઈટિંગ થાય છે અને "
        "મ્યુઝિકલ ફાઉન્ટેન પણ છે. પપ્પા સમજાવે છે કે એમાં પાણીની સેર (ધાર) સંગીતના તાલે ઊંચી-નીચી "
        "થાય છે, અને મમ્મી ઉમેરે છે કે એના પર જુદા જુદા રંગનો પ્રકાશ ફેંકાય છે. આ સાંભળીને મનન કહે "
        "છે કે મારે પણ દીદી સાથે જવું છે, અને ઝલક તથા મમ્મી બંને ના પાડે છે."
    ),
    "M1.S2.T3": (
        "મનન જીદ (હઠ) પકડે છે અને ઘરનાં બધાં સાથે રિસાઈ જાય છે. એ મમ્મીને કહે છે કે તમને દીદી જ "
        "વહાલી છે, અને ઊભો થઈને જતો રહે છે. મમ્મી એને મનાવવા એક પછી એક રસ્તા અજમાવે છે — સાંજે "
        "ભાવતું બનાવવાનું, બહાર ફરવા જવાનું, રાત્રે પિક્ચર અને ચીઝ પોપકોર્ન — પણ મનન દરેક વાત "
        "નકારે છે અને કહે છે કે તું મને ફોસલાવે (મીઠી વાતે મનાવે) છે. સામે ઝલક કહે છે કે અજાણી "
        "જગ્યાએ એને સાચવવો પડે, અને મમ્મી કહે છે કે શિક્ષકો બહારનાં બાળકોને લઈ જઈ ન શકે."
    ),
    "M2.S3.T4": (
        "પપ્પા મહેશભાઈ મનનને એકલો પોતાની પાસે લે છે અને 'તારી વાત તો સાચી છે બેટા' કહીને પહેલાં "
        "એની વાત સાંભળે છે. પછી એ સામી દરખાસ્ત મૂકે છે — દીદી ભલે પ્રવાસમાં જાય, આપણે એમના મિત્ર "
        "કરસનકાકાની વાડીએ (ફળ-ઝાડ વાવેલા ખેતરે) જઈએ. પપ્પા કહે છે કે ત્યાં મનન ઝાડ પર ચડી શકશે, "
        "પાણી પાવાની મોટી ખુલ્લી ટાંકીમાં ડૂબકી મારીને નાહી શકશે અને ગામડાનું મીઠું ભોજન જમશે. "
        "મનન 'તો તો ખૂબ મજ્જા પડશે' કહીને 'પછી ?', 'ખરેખર, પપ્પા ?' એમ પૂછતો જાય છે."
    ),
    "M2.S4.T5": (
        "મમ્મી છેલ્લી એક વાત ઉમેરે છે — શહેરમાં રાત્રે લાઈટો ચાલુ હોય એટલે આકાશ ને તારા એટલા સરસ "
        "દેખાતા નથી, પણ ગામડાની વાડીમાં લાઈટો ન હોય એટલે તારા એવા ચમકતા લાગે કે જાણે નજીક આવી "
        "ગયા હોય. મનન કહે છે કે દીદી ભલે આજવા-નિમેટા જાય, હું તો ગામડે જઈશ; ઝલક પણ સાથે આવવાનું "
        "કહે છે. પપ્પા દીદીને સાથે લઈ જવાનું પૂછે છે ત્યારે મનન પહેલાં ના પાડે છે અને પછી પોતે જ "
        "કહે છે કે મને દીદી વગર મજા ના આવે. છેલ્લે એ જાતે નક્કી કરે છે — અત્યારે દીદી એના "
        "પ્રવાસમાં જઈ આવે, ને રજા હશે ત્યારે બધાં સાથે કરસનકાકાને ત્યાં જવું."
    ),
}

KEY_TERMS = {
    "M1.S1.T1": [
        "પ્રવાસ — મુસાફરી, ફરવા જવાનું",
        "નોટિસ — શાળા તરફથી અપાતી લેખિત જાણ; અંગ્રેજીમાંથી આવેલો શબ્દ",
        "બહેનપણીઓ — સાથે ભણતી-રમતી સખીઓ",
        "બેનબા — દીકરીને વહાલથી બોલાવવાનું સંબોધન",
        "તોફાન — (અહીં) મસ્તી, ધમાલ",
    ],
    "M1.S1.T2": [
        "સરોવર — મોટું તળાવ",
        "લપસણી — ઉપરથી સરકીને નીચે આવવાનું રમતનું સાધન",
        "ફુવારા — પાણી ઊંચે ઉડાડતાં સાધનો; અંગ્રેજીમાં એને ફાઉન્ટેન કહે છે",
        "ગોઠવણ — ગોઠવવાની રીત, રચના",
        "સેર — (અહીં) પાણીની ધાર",
        "તાલ — સંગીતના સૂરનું માપ, ઠેકો",
    ],
    "M1.S2.T3": [
        "જીદ — હઠ, પોતાની જ વાત પકડી રાખવી",
        "ફોસલાવવું — મીઠી વાત કરીને મનાવી લેવું",
        "સાચવવું — સંભાળ રાખવી, ધ્યાન રાખવું",
        "અજાણી — જેની ઓળખ ન હોય એવી, અજાણ્યી",
        "નકામી — કશા કામની નહીં, વ્યર્થ",
    ],
    "M2.S3.T4": [
        "વાડી — ફળ-ઝાડ વાવેલી ખેતરની જમીન",
        "ઊપડીએ — નીકળી પડીએ, જવા માટે ઊપડવું",
        "ટાંકી — પાણી ભરી રાખવાનું મોટું ખુલ્લું પાત્ર, હોજ",
        "ડૂબકી — પાણીમાં આખા ડૂબીને લેવાતી બોળ",
        "ભોજન — જમવાનું, ખાવાનું",
        "મજ્જા — 'મજા'નું બોલચાલમાં વપરાતું ભારવાળું રૂપ; ભૂલ નથી",
    ],
    "M2.S4.T5": [
        "લાઈટો — દીવા, બત્તીઓ; અંગ્રેજીમાંથી આવેલો શબ્દ",
        "ચમકતા — તેજથી ઝગમગતા",
        "એમાંયે — 'એમાં પણ' માટેનું બોલચાલનું ટૂંકું રૂપ",
        "નક્કી કરવું — મનમાં પાકું ઠરાવવું, નિર્ણય લેવો",
        "સમજદાર — સમજણવાળો, વાત સમજી શકે એવો",
    ],
}

# Every topic is a reading scene of this સંવાદ — one image per scene, per the
# active genre profiles. No second medium is planned for any topic.
CONTENT_TYPES = {
    t: {
        "primary_content_type": "image",
        "secondary_content_type": None,
        "tertiary_content_type": None,
        "available_content_types": ["image"],
    }
    for t in SPANS
}

with io.open(os.path.join(BASE, "02_structure.json"), encoding="utf-8") as f:
    plan = json.load(f, object_pairs_hook=collections.OrderedDict)

order = []
seen = set()
for m in plan["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            tid = t["topic_id"]
            assert tid in SPANS, tid
            seen.add(tid)
            a, b = SPANS[tid]
            oc = chunk(a, b)
            t["original_chunk"] = oc
            t["modified_chunk"] = MODIFIED[tid]
            t["word_count"] = {
                "original": len(oc.split()),
                "modified": len(MODIFIED[tid].split()),
            }
            t["key_terms"] = KEY_TERMS[tid]
            ct = CONTENT_TYPES[tid]
            t["primary_content_type"] = ct["primary_content_type"]
            t["secondary_content_type"] = ct["secondary_content_type"]
            t["tertiary_content_type"] = ct["tertiary_content_type"]
            t["available_content_types"] = ct["available_content_types"]
            order.append(tid)

assert seen == set(SPANS), (seen, set(SPANS))

plan["provenance_05"] = {
    "agent": "05_verbatim_attachment",
    "original_chunk_source": "00_chapter_normalized.md, copied line-for-line over the ranges named by each topic's source_span; [[…]] marker lines and blank lines stripped, nothing else altered",
    "verification": "every attached line cross-read against the 150 dpi renders _renders/page-1.png … page-5.png (printed folios 92–96); turn counts recounted on the page and match source_span.turn_count (12 + 17 + 21 + 23 + 10 = 83, equal to 01_meta.json structure_inventory.dialogue_turns)",
    "notes": [
        "This chapter prints zero રંગસૂચના, so natak_ekanki.md's directions-are-text gate has nothing to attach; the count of '(' in every original_chunk is zero, matching the page.",
        "Printed double spaces recorded by Agent 1 are preserved as printed: 'ભઈલું,  હું છે ને', 'ભઈલું,  ખોટી જીદ', 'ભઈલું,  આ તો', 'ભઈલું,  તને ખબર', 'દીદીના  ટીચરને'.",
        "Printed-as-is oddities kept, not corrected: 'ભાઈલુ' on p. 92 against 'ભઈલું' elsewhere; 'મજ્જા' on p. 96; 'નહિ'/'નહીં' both in the book; the spaced ? and ! GSEB sets.",
        "No Devanagari daṇḍa appears on these pages and none was introduced; the chapter's પૂર્ણવિરામ is '.' throughout. No Roman or Devanagari character occurs in any original_chunk.",
        "The પ્રવેશપેટી, the શબ્દાર્થ box on p. 97, the p. 100 ચિત્રવર્ણન illustration and all fifteen સ્વાધ્યાય blocks — including the five-line rhyme 'એક છોકરું  રિસાણું…' printed inside a સ્વાધ્યાય block — are outside every original_chunk.",
        "key_terms are chosen per topic from that topic's own chunk at the std-6 L2 bar (shabd_gloss.md: 4–6, sit high in the band). The printed શબ્દાર્થ box was read as evidence of difficulty, not emptied into the field; its entries ઉત્સાહ and ખંત do not occur in the reading text and are not used.",
        "Every topic is one reading scene of the સંવાદ, so each carries primary_content_type 'image' with available_content_types ['image']; no second or third medium is planned. Agent 9 owns the prompts. The two printed illustrations (p. 93 inside T2, p. 95 inside T4) are the book's own, not a media plan.",
    ],
}

with io.open(os.path.join(BASE, "05_with_content.json"), "w", encoding="utf-8") as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)
    f.write("\n")

tb = collections.OrderedDict()
tb["chapter_id"] = plan["chapter_id"]
tb["textbook_order"] = order
tb["source"] = "printed pages 92–96 read off the render (_renders/page-1.png … page-5.png); the five [[સંવાદ: …]] stretches appear on the page in exactly this sequence"
tb["equals_logical_order"] = True
tb["notes"] = [
    "The printed order equals the logical order of 02_structure.json: the chapter is one continuous conversation printed front to back, and no topic is reordered.",
    "Excluded from this index, because they are not this chapter's teaching text: the teacher-addressed પ્રવેશપેટી, the શબ્દાર્થ box (p. 97), all fifteen સ્વાધ્યાય blocks (pp. 97–100) and the p. 100 ચિત્રવર્ણન illustration.",
]

with io.open(os.path.join(BASE, "05b_textbook_order.json"), "w", encoding="utf-8") as f:
    json.dump(tb, f, ensure_ascii=False, indent=2)
    f.write("\n")

for tid in order:
    a, b = SPANS[tid]
    c = chunk(a, b)
    lines = c.split("\n")
    print(tid, "turns=%d" % len(lines), "words=%d" % len(c.split()))
    print("   first:", lines[0])
    print("   last :", lines[-1])
print("total turns:", sum(len(chunk(*SPANS[t]).split("\n")) for t in order))
