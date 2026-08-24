# -*- coding: utf-8 -*-
import json, re, sys

BASE = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch07/"
d = json.load(open(BASE + "12_authoring.json"))
src = json.load(open(BASE + "05_with_content.json"))

guj = re.compile('[઀-૿]')
deva = re.compile('[ऀ-ॿ]')
roman = re.compile('[A-Za-z]')
digits = re.compile('[0-9૦-૯]')

fails, warns = [], []

# ---- ids from 05
chunks, kt, cids = {}, {}, {}
for m in src["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            chunks[t["topic_id"]] = t["original_chunk"]
            kt[t["topic_id"]] = t["key_terms"]
            cids[t["topic_id"]] = [c["concept_id"] for c in t["concepts"]]

got = [t["topic_id"] for t in d["topics"]]
if got != list(chunks.keys()):
    fails.append("topic id order/set mismatch: %s vs %s" % (got, list(chunks.keys())))

DISPLAY = ["explanation", "real_life_example", "brief_summary", "summary", "detailed_summary"]

def toks(s):
    return [x for x in s.split() if guj.search(x)]

def sentences(s):
    return [x for x in re.split(r'[.!?]\s+|\.$', s) if x.strip()]

def scan(label, s):
    if deva.search(s): fails.append(label + ": Devanagari present")
    if '।' in s: fails.append(label + ": danda present")
    if roman.search(s): fails.append(label + ": Roman letters -> " + s[:80])
    if digits.search(s): fails.append(label + ": digit -> " + s[:80])
    if 'જોઈએ' in s: fails.append(label + ": slogan gate word જોઈએ -> " + s[:80])

BANNED = ['જીવાણુ','જંતુ','બૅક્ટેરિયા','બેક્ટેરિયા','વાઇરસ','ચેપ','રોગપ્રતિકારક',
          'મલેરિયા','ડેન્ગ્યુ','બાષ્પીભવન','જલચક્ર',
          'સરકાર','યોજના','ઝુંબેશ','પક્ષ','સેના','સરહદ','રાષ્ટ્રધ્વજ','તિરંગો','ધ્વજવંદન',
          'સજીવારોપણ','રૂપક','ઉપમા','અતિશયોક્તિ','વર્ણાનુપ્રાસ','પુનરુક્તિ','અલંકાર','છંદ','માત્રામેળ',
          'વલ્લભભાઈ','પટેલ','ગાંધીજી',
          'જ્ઞાતિ','કોમ','હિન્દુ','મુસ્લિમ','જૈન','ધર્મ']

def collect_all_strings(o, path=""):
    if isinstance(o, str):
        yield path, o
    elif isinstance(o, dict):
        for k, v in o.items():
            yield from collect_all_strings(v, path + "." + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from collect_all_strings(v, path + "[%d]" % i)

for t in d["topics"]:
    tid = t["topic_id"]
    # word bands
    for f in ("explanation", "real_life_example"):
        n = len(toks(t[f]))
        if not (55 <= n <= 90):
            fails.append("%s %s: %d Gujarati words (band 55-90)" % (tid, f, n))
        else:
            print("  %s %-18s %d words" % (tid, f, n))
    # summaries strictly increase
    b, s_, ds = t["brief_summary"], t["summary"], t["detailed_summary"]
    if not (len(b) < len(s_) < len(ds)):
        fails.append("%s: summaries not strictly increasing (%d,%d,%d)" % (tid, len(b), len(s_), len(ds)))
    ns = len(sentences(s_)); nds = len(sentences(ds))
    if not (2 <= ns <= 3): warns.append("%s summary sentences=%d (want 2-3)" % (tid, ns))
    if not (4 <= nds <= 6): warns.append("%s detailed_summary sentences=%d (want 4-6)" % (tid, nds))
    # bullets
    for f in ("concept_bullets", "important_points"):
        if not (3 <= len(t[f]) <= 4): fails.append("%s %s len=%d" % (tid, f, len(t[f])))
    # concepts
    if [c["concept_id"] for c in t["concepts"]] != cids[tid]:
        fails.append("%s concept ids mismatch" % tid)
    for c in t["concepts"]:
        types = [b_["type"] for b_ in c["content"]]
        if not types or types[0] != "paragraph":
            fails.append("%s %s content shape %s" % (tid, c["concept_id"], types))
        for b_ in c["content"]:
            if b_["type"] == "paragraph" and "publication_text" in b_:
                fails.append("publication_text written")
    # recall
    rq = t["recall_questions"]
    if not (2 <= len(rq) <= 3): fails.append("%s recall count %d" % (tid, len(rq)))
    for i, q in enumerate(rq, 1):
        if q["id"] != "%s.RQ%d" % (tid, i): fails.append("bad rq id " + q["id"])
        if q["legacy_id"] != "%s.TR%d" % (tid, i): fails.append("bad legacy id " + q["legacy_id"])
        if q["bloom_level"] != q["bloom_level"].lower(): fails.append("bloom not lowercase " + q["id"])
        if q["bloom_level"] not in ("remember","understand","apply","analyze","evaluate","create"):
            fails.append("bad bloom " + q["id"])
        if q["difficulty"] not in ("easy","medium","hard"): fails.append("bad difficulty " + q["id"])
        if not q["answer"].strip(): fails.append("empty answer " + q["id"])
    blooms = [q["bloom_level"] for q in rq]
    if blooms[0] != "remember": warns.append("%s first bloom %s" % (tid, blooms[0]))
    if not set(blooms) & {"apply","analyze","evaluate"}: fails.append("%s no higher bloom" % tid)
    # estimated_exchanges
    if not (isinstance(t["estimated_exchanges"], str) and t["estimated_exchanges"].isdigit()):
        fails.append("%s estimated_exchanges" % tid)
    # bhasha bodh caps for std 6
    if not (3 <= len(t["shabdarth"]) <= 5): fails.append("%s shabdarth %d" % (tid, len(t["shabdarth"])))
    if len(t["samanarthi"]) > 2: fails.append("%s samanarthi %d" % (tid, len(t["samanarthi"])))
    if len(t["vilom"]) > 1: fails.append("%s vilom %d" % (tid, len(t["vilom"])))
    if len(t["vyakaran"]) != 1: fails.append("%s vyakaran %d" % (tid, len(t["vyakaran"])))
    if t["figures_of_speech"] != []: fails.append("%s figures_of_speech non-empty at std 6" % tid)
    # every shabd/samanarthi/vilom headword must occur in THIS chunk
    ch = chunks[tid]
    for e in t["shabdarth"]:
        head = e["shabd"].split()[0]
        if head not in ch: fails.append("%s shabdarth '%s' not in chunk" % (tid, e["shabd"]))
        if e["prakar"] not in ("તત્સમ","તદ્ભવ","દેશ્ય","આગત","કાવ્ય-રૂપ"):
            fails.append("%s bad prakar %s" % (tid, e["prakar"]))
    for e in t["samanarthi"]:
        if e["shabd"] not in ch: fails.append("%s samanarthi '%s' not in chunk" % (tid, e["shabd"]))
    for e in t["vilom"]:
        if e["shabd"] not in ch: fails.append("%s vilom '%s' not in chunk" % (tid, e["shabd"]))
    BINDU_OK = {"નામ","સર્વનામ","વિશેષણ","ક્રિયાપદ","કાળ","વચન","જાતિ","રૂઢિપ્રયોગ","કહેવત",
                "વિરામચિહ્નો","જોડાક્ષર","ક્રિયાવિશેષણ","સંયોજક","વાક્યના પ્રકારો","ઉપસર્ગ-પ્રત્યય",
                "દ્વિરુક્ત / રવાનુકારી શબ્દો","શબ્દસમૂહ માટે એક શબ્દ","અનુસ્વાર","શબ્દકોશ ક્રમ"}
    for v in t["vyakaran"]:
        if v["bindu"] not in BINDU_OK: fails.append("%s bindu off-ladder: %s" % (tid, v["bindu"]))
    rs = t["rhyme_scheme"]
    if not (isinstance(rs, dict) and rs.get("pattern") and isinstance(rs.get("rhyming_words"), list) and rs.get("note")):
        fails.append("%s rhyme_scheme shape" % tid)
    # display-text scans
    for f in DISPLAY:
        scan("%s.%s" % (tid, f), t[f])
    for f in ("concept_bullets", "important_points"):
        for line in t[f]: scan("%s.%s" % (tid, f), line)
    for q in rq:
        scan(q["id"] + ".prompt", q["prompt"])
        scan(q["id"] + ".answer", q["answer"])

# banned words across every authored string
for path, s in collect_all_strings({"topics": d["topics"], "modules": d["modules"]}):
    for w in BANNED:
        if w in s:
            fails.append("BANNED '%s' at %s -> %s" % (w, path, s[:90]))

# modules
mids = [m["module_id"] for m in d["modules"]]
if mids != [m["module_id"] for m in src["modules"]]:
    fails.append("module ids mismatch")
ors_count = 0
for m in d["modules"]:
    n = len(m["difficult_words"])
    if not (5 <= n <= 10): fails.append("%s difficult_words %d" % (m["module_id"], n))
    for w in m["difficult_words"]:
        for k in ("word","meaning","example"):
            if not w.get(k): fails.append("%s difficult_word missing %s" % (m["module_id"], k))
        scan(m["module_id"] + ".dw", w["meaning"]); scan(m["module_id"] + ".dw", w["example"])
    if m.get("overall_rhyme_scheme"): ors_count += 1
if ors_count != 1:
    warns.append("overall_rhyme_scheme stated %d times" % ors_count)

# quoted-line fidelity: two-dot line must never appear with three dots
allstr = json.dumps(d, ensure_ascii=False)
if "રોશન થાશે..." in allstr: fails.append("two-dot printed line quoted with three dots")
if "થશે'" in allstr and "થાશે એટલે થશે" not in allstr: warns.append("check થાશે quoting")
if "સ્વચ્છતા ત્યાં પ્રભુતા" in allstr: fails.append("placard artwork text used as verse")
# no Devanagari/danda anywhere
if deva.search(allstr): fails.append("Devanagari somewhere in file")
if "।" in allstr: fails.append("danda somewhere in file")

print("\n--- FAILS (%d) ---" % len(fails))
for f in fails: print(" X", f)
print("--- WARNS (%d) ---" % len(warns))
for w in warns: print(" !", w)
sys.exit(1 if fails else 0)
