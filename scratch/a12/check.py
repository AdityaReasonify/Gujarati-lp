# -*- coding: utf-8 -*-
import json, re, unicodedata
D = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch12/"
plan = json.load(open(D + "12_authoring.json"))
src = json.load(open(D + "05_with_content.json"))

chunks = {}
ids = []
concept_ids = {}
for m in src["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            chunks[t["topic_id"]] = t["original_chunk"]
            ids.append(t["topic_id"])
            concept_ids[t["topic_id"]] = [c["concept_id"] for c in t["concepts"]]

err = []
# id order and completeness
got = [t["topic_id"] for t in plan["topics"]]
if got != ids:
    err.append("TOPIC ID MISMATCH %s vs %s" % (got, ids))

for t in plan["topics"]:
    tid = t["topic_id"]
    # word bands
    for f in ("explanation", "real_life_example"):
        n = len(t[f].split())
        if not (55 <= n <= 90):
            err.append("%s %s words=%d" % (tid, f, n))
    # summaries strictly increasing
    b, s, d = len(t["brief_summary"]), len(t["summary"]), len(t["detailed_summary"])
    if not (b < s < d):
        err.append("%s summaries not increasing %d %d %d" % (tid, b, s, d))
    nb = t["brief_summary"].count(".") + t["brief_summary"].count("!")
    ns = t["summary"].count(".")
    nd = t["detailed_summary"].count(".")
    if nb != 1: err.append("%s brief sentences=%d" % (tid, nb))
    if not (2 <= ns <= 3): err.append("%s summary sentences=%d" % (tid, ns))
    if not (4 <= nd <= 6): err.append("%s detailed sentences=%d" % (tid, nd))
    # bullets
    for f in ("concept_bullets", "important_points"):
        if not (3 <= len(t[f]) <= 4): err.append("%s %s n=%d" % (tid, f, len(t[f])))
    # concepts
    cg = [c["concept_id"] for c in t["concepts"]]
    if cg != concept_ids[tid]: err.append("%s concept ids %s vs %s" % (tid, cg, concept_ids[tid]))
    for c in t["concepts"]:
        if not c["content"]: err.append("%s %s empty content" % (tid, c["concept_id"]))
        for blk in c["content"]:
            if blk["type"] == "paragraph" and "text" not in blk: err.append("%s bad para" % tid)
            if blk["type"] == "list" and "items" not in blk: err.append("%s bad list" % tid)
            if blk["type"] not in ("paragraph", "list"): err.append("%s bad type" % tid)
    # recall
    rq = t["recall_questions"]
    if not (2 <= len(rq) <= 3): err.append("%s rq n=%d" % (tid, len(rq)))
    for i, q in enumerate(rq, 1):
        if q["id"] != "%s.RQ%d" % (tid, i): err.append("%s bad rq id %s" % (tid, q["id"]))
        if q["legacy_id"] != "%s.TR%d" % (tid, i): err.append("%s bad legacy %s" % (tid, q["legacy_id"]))
        if q["bloom_level"] != q["bloom_level"].lower(): err.append("%s bloom case" % tid)
        if q["bloom_level"] not in ("remember","understand","apply","analyze","evaluate","create"):
            err.append("%s bloom %s" % (tid, q["bloom_level"]))
        if q["difficulty"] not in ("easy","medium","hard"): err.append("%s diff" % tid)
        if not q["answer"].strip(): err.append("%s empty answer" % tid)
    blooms = [q["bloom_level"] for q in rq]
    if "remember" not in blooms: err.append("%s no remember" % tid)
    if not ({"apply","analyze","evaluate"} & set(blooms)): err.append("%s no higher bloom" % tid)
    # bhasha bodh
    if not (3 <= len(t["shabdarth"]) <= 5): err.append("%s shabdarth n=%d" % (tid, len(t["shabdarth"])))
    if len(t["samanarthi"]) > 2: err.append("%s samanarthi n=%d" % (tid, len(t["samanarthi"])))
    if len(t["vilom"]) > 1: err.append("%s vilom n=%d" % (tid, len(t["vilom"])))
    if len(t["vyakaran"]) != 1: err.append("%s vyakaran n=%d" % (tid, len(t["vyakaran"])))
    for e in t["shabdarth"]:
        if e["prakar"] not in ("તત્સમ","તદ્ભવ","દેશ્ય","આગત","કાવ્ય-રૂપ"):
            err.append("%s prakar %s" % (tid, e["prakar"]))
    if t["figures_of_speech"] != []: err.append("%s fos not []" % tid)
    if t["rhyme_scheme"] is not None: err.append("%s rhyme not null" % tid)
    if not isinstance(t["estimated_exchanges"], str): err.append("%s ee not str" % tid)

# script purity + banned chars across all authored strings
BANNED_RE = re.compile(r"[ऀ-ॿ]")          # Devanagari
DANDA = "।"
def walk(o, path=""):
    if isinstance(o, str):
        if BANNED_RE.search(o): err.append("DEVANAGARI at %s" % path)
        if DANDA in o: err.append("DANDA at %s" % path)
        for ch in o:
            if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
                yield ("ROMAN", path, o)
                break
    elif isinstance(o, dict):
        for k, v in o.items():
            yield from walk(v, path + "." + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from walk(v, path + "[%d]" % i)

roman = list(walk(plan["topics"])) + list(walk(plan["modules"]))
print("ROMAN HITS:", len(roman))
for r in roman: print("   ", r[1], r[2][:80])

print("ERRORS:", len(err))
for e in err: print("  -", e)
