# -*- coding: utf-8 -*-
import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build12_a import TOPICS_A
from build12_b import TOPICS_B
from build12_c import TOPICS_C, MODULES

OUT = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output7/ch03"
src = json.load(open(os.path.join(OUT, "05_with_content.json")))

chunks, concept_order, topic_order = {}, {}, []
for m in src["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            topic_order.append(t["topic_id"])
            chunks[t["topic_id"]] = t["original_chunk"]
            concept_order[t["topic_id"]] = [c["concept_id"] for c in t["concepts"]]

TOPICS = TOPICS_A + TOPICS_B + TOPICS_C
problems = []

def wc(s):
    return len(s.split())

def alnum_wc(s):
    return len(re.findall(r"[઀-૿A-Za-z0-9]+", s))

def sent_count(s):
    """Count real sentence enders: punctuation inside quotes and ellipses do not end a sentence."""
    s = re.sub(r"‘‘.*?’’", "X", s)
    s = re.sub(r"‘.*?’", "X", s)
    s = s.replace("...", "")
    return len(re.findall(r"[.!?]", s))

ALLOWED_BINDU = {"નામ","સર્વનામ","વિશેષણ","ક્રિયાપદ","કાળ","વચન","જાતિ","રૂઢિપ્રયોગ","કહેવત",
 "વિરામચિહ્નો","જોડાક્ષર","ક્રિયાવિશેષણ","સંયોજક","વાક્યના પ્રકારો","ઉપસર્ગ-પ્રત્યય",
 "દ્વિરુક્ત શબ્દો","શબ્દસમૂહ માટે એક શબ્દ","અનુસ્વાર","શબ્દકોશ ક્રમ"}

SPOILERS = ["વીરગતિ","હત્યા","મૃત્યુ","શહીદ","જયદ્રથ","દુઃશાસન","કૃતવર્મા"]
CLIMAX_IDX = topic_order.index("M3.S6.T12")

DISPLAY_KEYS = ["explanation","real_life_example","brief_summary","summary","detailed_summary"]

ids = [t["topic_id"] for t in TOPICS]
if ids != topic_order:
    problems.append("TOPIC ORDER MISMATCH: %s vs %s" % (ids, topic_order))

for i, t in enumerate(TOPICS):
    tid = t["topic_id"]
    ch = chunks[tid]
    for f in ("explanation", "real_life_example"):
        w, a = wc(t[f]), alnum_wc(t[f])
        if not (55 <= w <= 90) or a < 55:
            problems.append("%s %s words=%d alnum=%d" % (tid, f, w, a))
        else:
            print("ok  %s %-18s ws=%3d alnum=%3d" % (tid, f, w, a))
    b, s, d = wc(t["brief_summary"]), wc(t["summary"]), wc(t["detailed_summary"])
    if not (b < s < d):
        problems.append("%s summaries not strictly increasing: %d %d %d" % (tid, b, s, d))
    if sent_count(t["brief_summary"]) != 1:
        problems.append("%s brief_summary not one sentence" % tid)
    ns = sent_count(t["summary"])
    nd = sent_count(t["detailed_summary"])
    if not (2 <= ns <= 3):
        problems.append("%s summary sentences=%d" % (tid, ns))
    if not (4 <= nd <= 6):
        problems.append("%s detailed_summary sentences=%d" % (tid, nd))
    for k in ("concept_bullets", "important_points"):
        if not (3 <= len(t[k]) <= 4):
            problems.append("%s %s count=%d" % (tid, k, len(t[k])))
    cids = [c["concept_id"] for c in t["concepts"]]
    if cids != concept_order[tid]:
        problems.append("%s concept ids %s != %s" % (tid, cids, concept_order[tid]))
    for c in t["concepts"]:
        for blk in c["content"]:
            if blk["type"] not in ("paragraph", "list"):
                problems.append("%s bad block type" % tid)
    rq = t["recall_questions"]
    if not (2 <= len(rq) <= 3):
        problems.append("%s recall count=%d" % (tid, len(rq)))
    for n, q in enumerate(rq, 1):
        if q["id"] != "%s.RQ%d" % (tid, n) or q["legacy_id"] != "%s.TR%d" % (tid, n):
            problems.append("%s bad rq id %s" % (tid, q["id"]))
        if q["bloom_level"] != q["bloom_level"].lower():
            problems.append("%s bloom not lower" % tid)
        if q["bloom_level"] not in ("remember","understand","apply","analyze","evaluate","create"):
            problems.append("%s bad bloom %s" % (tid, q["bloom_level"]))
        if q["difficulty"] not in ("easy","medium","hard"):
            problems.append("%s bad difficulty" % tid)
        if not q["answer"].strip():
            problems.append("%s empty answer" % tid)
    if not (3 <= len(t["shabdarth"]) <= 5):
        problems.append("%s shabdarth=%d" % (tid, len(t["shabdarth"])))
    if not (1 <= len(t["samanarthi"]) <= 2):
        problems.append("%s samanarthi=%d" % (tid, len(t["samanarthi"])))
    if len(t["vilom"]) > 1:
        problems.append("%s vilom=%d" % (tid, len(t["vilom"])))
    if len(t["vyakaran"]) != 1:
        problems.append("%s vyakaran=%d" % (tid, len(t["vyakaran"])))
    for v in t["vyakaran"]:
        if v["bindu"] not in ALLOWED_BINDU:
            problems.append("%s bindu not allowed: %s" % (tid, v["bindu"]))
        if v["udaharan"] not in ch:
            problems.append("%s udaharan not verbatim in chunk: %s" % (tid, v["udaharan"]))
    for e in t["shabdarth"]:
        if e["prakar"] not in ("તત્સમ","તદ્ભવ","દેશ્ય","આગત","કાવ્ય-રૂપ"):
            problems.append("%s bad prakar %s" % (tid, e["prakar"]))
        if e["shabd"][:3] not in ch:
            problems.append("%s shabdarth word not in chunk: %s" % (tid, e["shabd"]))
    for e in t["samanarthi"]:
        if e["shabd"][:3] not in ch:
            problems.append("%s samanarthi word not in chunk: %s" % (tid, e["shabd"]))
    for e in t["vilom"]:
        if e["shabd"][:3] not in ch:
            problems.append("%s vilom word not in chunk: %s" % (tid, e["shabd"]))
    if t["figures_of_speech"] != [] or t["rhyme_scheme"] is not None:
        problems.append("%s craft fields must be []/null at std 7 ગદ્ય" % tid)
    if not re.fullmatch(r"[0-9]+", t["estimated_exchanges"]):
        problems.append("%s estimated_exchanges" % tid)

    # gathered display text of the topic
    blob = " ".join([t[k] for k in DISPLAY_KEYS] + t["concept_bullets"] + t["important_points"]
                    + [q["prompt"] for q in rq] + [q["answer"] for q in rq]
                    + [b2.get("text", " ".join(b2.get("items", [])))
                       for c in t["concepts"] for b2 in c["content"]])
    if re.search(r"[0-9૦-૯]", blob):
        problems.append("%s digit in display text" % tid)
    if "।" in blob:
        problems.append("%s danda" % tid)
    if re.search(r"[ऀ-ॿ]", blob):
        problems.append("%s devanagari" % tid)
    if re.search(r"[A-Za-z]", blob):
        problems.append("%s roman letters: %s" % (tid, re.findall(r"[A-Za-z]+", blob)))
    if i < CLIMAX_IDX:
        for sp in SPOILERS:
            if sp in blob:
                problems.append("%s SPOILER '%s'" % (tid, sp))

notes = [
 "તબક્કો: std 7, ધોરણ tier, ગદ્ય વાર્તા (પૌરાણિક કથા) — figures_of_speech `[]` અને rhyme_scheme `null` દરેક ટોપિકમાં, અને module-level overall_rhyme_scheme `null`. std-7 genre gate પ્રમાણે કોઈ અલંકાર/છંદ/રસ/સાહિત્યપ્રકારનું નામ બાળક સુધી પહોંચતું નથી; ‘વીરરસ’ શબ્દ ફક્ત શિક્ષક-સંબોધિત પ્રવેશપેટીમાં છે અને ત્યાં જ રહ્યો છે.",
 "Tier ધોરણ was re-injected per block, not per session (profiles/students/std-7.md §5.3): every explanation sits mid-band with at most one subordinate clause per sentence, two to three inline glosses, and the std-7 recall ladder (literal wh- → motive inference → prediction / in-character hypothetical). No Bloom capping; three topics reach analyze and M3.S5.T9 reaches apply.",
 "Anchor domain ledger (gujarat_cultural_anchors.md §3.4), scene → domain → region/community: T1 રોજિંદું જીવન (મામાનું ઘર) · T2 કામ-આજીવિકા (શેરીનાં શાકવાળાં બહેન) · T3 ખાનપાન (ઘરનું રસોડું) · T4 તહેવાર-ઉત્સવ (મેળામાં ખેલ ફરતે ભીડનું કૂંડાળું) · T5 રોજિંદું જીવન (સાયકલ) · T6 ભૂગોળ-કુદરત (કચ્છનું ગામ, પાણીના ટૅન્કરનો વારો) · T7 તહેવાર-ઉત્સવ (ઉત્તરાયણ, ધાબાનો પેચ) · T8 કામ-આજીવિકા (પંક્ચરવાળા કાકા) · T9 રોજિંદું જીવન (શાળાની પ્રાર્થનાસભા) · T10 લોકકલા (શેરી-ગરબો) · T11 ભૂગોળ-કુદરત (ગિરનારનાં પગથિયાં, સૌરાષ્ટ્ર) · T12 રોજિંદું જીવન (શેરી ક્રિકેટનો નિયમ) · T13 તહેવાર-ઉત્સવ (ઈદ, પડોશીનું બંધ ઘર). No two consecutive scenes share a domain and no picture repeats; six of the bank's seven domains are used (હસ્તકલા unused — nothing in this chapter's ભાવ asked for it). Regions/communities touched: કચ્છનું ગામ, સૌરાષ્ટ્ર (ગિરનાર), શેરી/ફળિયું, ધાબું, and one neighbour's ઈદ morning as a lived moment rather than a census line.",
 "Sensitivity 08_sensitivity.json honoured: M2.S3.T6 stays on હક (a fair claim refused) and never on one side being evil; M2.S4.T7 explains ક્ષત્રિય પરંપરા strictly as this કથા's plot rule (‘આ કથાના ક્ષત્રિય રિવાજ પ્રમાણે’) and names બદલો as Sushrma's own stated motive without admiring it; M3.S6.T11 lands on ‘ન તો એ ડર્યો, ન તો એ ડગ્યો’ rather than on the wounds; the hard item M3.S6.T12 names exactly what the page names (‘નીતિનિયમોને નેવે મૂકીને’, six warriors together against one, ઉપરાઉપરી ઘા) with no elaboration and no evaluative label on the six, and the anchor lands on a broken rule in a game; M3.S6.T13 keeps the સંતોષ of the નિર્ણાયક ભૂમિકા and its anchor is a neighbour sorely missed, not death.",
 "Chapter-level gates from 07_pitfalls.json held: nothing outside the thirteen original_chunks entered any field — no કોઠા count, no જયદ્રથનું વરદાન, no અર્જુનની પ્રતિજ્ઞા, no ઉત્તરા/પરીક્ષિત, no ending past યુધિષ્ઠિરના વાક્ય, and no author/compiler named (the page prints only ‘- સંકલિત’). The revenge frame appears nowhere in an explanation, bullet or recall answer; the printed exercise that asks for it is Agent 10's.",
 "The chapter's four printed રૂઢિપ્રયોગ are glossed in the topic where each occurs, in the book's own printed words: પલ્લું ભારે થવું (M2.S3.T6 vyakaran), નેવે મૂકવું and યોજના ધૂળમાં મળવી (M3.S6.T12 vyakaran + concept_bullets), આંખો મીંચી દેવી (M3.S6.T13 vyakaran).",
 "vyakaran runs at one entry per topic (bhasha_bodh.md std-7 cap) and leans towards this chapter's own chapter-final grammar box, સંજ્ઞા વિશે જાણીએ — વ્યક્તિવાચક/જાતિવાચક (T1), ભાવવાચક (T5) and સમૂહવાચક (T8) are all taken from the box's own ladder with the chapter's own words. સંધિ, સમાસ, કૃદંત, નિપાત and પ્રયોગ are out of range at std 7 and appear nowhere.",
 "key_terms is Agent 5's and was not touched. One gap worth routing back: 07_pitfalls.json's correction for M1.S1.T1 asks for `મામા — માતાનો ભાઈ` in that topic's key_terms and it is not there (the list runs સખા, બાણાવળી, વિચક્ષણ, નીડર, રોકટોક — five, inside the 3–6 band). The gloss is therefore carried inline in M1.S1.T1's explanation and as the first concept_bullets line instead. All thirteen key_terms lists are inside the band; no other gap found.",
 "Field-shape note (VERIFY-4): every explanation and real_life_example was counted before emitting and sits inside 55–90 whitespace-delimited words, mid-band as the ધોરણ tier asks. Word counts use the same whitespace convention that produced word_count.original in 05_with_content.json.",
 "One documented tension, resolved and flagged rather than silently decided: reference/alankar_chhand.md's opening line says the module-level `difficult_words` and `overall_rhyme_scheme` are `[]`/`null` for ગદ્ય, while reference/shabd_gloss.md (which owns difficult_words) and reference/field_shape_rules.md give a per-standard band with no genre condition — std 7 = 6–8 per module. For an L2 pack on the chapter with the heaviest તત્સમ war vocabulary in the book, emptying that field would remove the module's vocabulary aid, so difficult_words is authored (M1: 7, M2: 7, M3: 8, each with a fresh everyday example sentence, never the chapter's own line) and overall_rhyme_scheme is null. Flagging for Agent 13 in case the intended reading is the stricter one.",
 "No page render was opened: 00_chapter_normalized.md answered every question this agent had, including the printed શબ્દાર્થ and રૂઢિપ્રયોગ boxes and the chapter-final grammar box.",
 "objective_text was not touched anywhere; all thirteen objectives in 05_with_content.json read correctly against their topics and none needs routing back to Agent 2."
]

out = {"tier": "ધોરણ", "grade": 7, "topics": TOPICS, "modules": MODULES, "notes": notes}

print("\n--- problems ---")
for p in problems:
    print(p)
print("total problems:", len(problems))

if "--write" in sys.argv:
    path = os.path.join(OUT, "12_authoring.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print("WROTE", path, os.path.getsize(path), "bytes")
