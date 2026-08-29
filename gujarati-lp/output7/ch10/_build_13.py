#!/usr/bin/env python3
# Agent 13 - merge every layer into 13_merged.json and run the QC gate.
import json, os, re

D = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output7/ch10"
L = lambda n: json.load(open(os.path.join(D, n), encoding="utf-8"))

meta  = L("01_meta.json")
base  = L("05_with_content.json")
pit   = L("07_pitfalls.json")
sens  = L("08_sensitivity.json")
med   = L("09_media.json")
exsol = L("10_exercise_solutions.json")
pages = L("11_pages.json")
auth  = L("12_authoring.json")
pub   = L("16_publication.json")
val04 = L("04_validation.json")
norm  = open(os.path.join(D, "00_chapter_normalized.md"), encoding="utf-8").read()

auth_by  = {t["topic_id"]: t for t in auth["topics"]}
pub_by   = {t["topic_id"]: t for t in pub["topics"]}
mod_auth = {m["module_id"]: m for m in auth["modules"]}
media_by = {}
for m in med["media"]:
    media_by.setdefault(m["topic_id"], []).append(m)

obj_by = {o["objective_id"]: o for o in base["objectives"]}
problems = []

def fail(section, owner, text): problems.append((section, owner, text))

modules = []
for m in base["modules"]:
    ma = mod_auth.get(m["module_id"], {})
    nm = {"module_id": m["module_id"], "module_name": m["module_name"],
          "difficult_words": ma.get("difficult_words", []),
          "overall_rhyme_scheme": ma.get("overall_rhyme_scheme", None),
          "segments": []}
    for s in m["segments"]:
        ns = {"segment_id": s["segment_id"], "segment_name": s["segment_name"], "topics": []}
        for t in s["topics"]:
            tid = t["topic_id"]
            a = auth_by.get(tid, {})
            p = pub_by.get(tid, {})
            cpub = {}
            for cp in p.get("concept_publication", []):
                cpub[(cp["concept_id"], cp["content_index"])] = cp["publication_text"]
            acon = {c["concept_id"]: c for c in a.get("concepts", [])}
            concepts = []
            for c in t["concepts"]:
                cid = c["concept_id"]
                content = []
                for i, blk in enumerate(acon.get(cid, {}).get("content", [])):
                    nb = dict(blk)
                    if nb.get("type") == "paragraph":
                        if (cid, i) in cpub:
                            nb["publication_text"] = cpub[(cid, i)]
                        else:
                            fail("Publication", "16_publication_authoring.md",
                                 cid + " content[" + str(i) + "] (paragraph) has no publication_text")
                    content.append(nb)
                concepts.append({"concept_id": cid, "concept_name": c["concept_name"],
                                 "objective_id": c["objective_id"],
                                 "key_terms": c.get("key_terms", []), "content": content})
            lo = []
            for oid in t["objective_ids"]:
                o = dict(obj_by[oid]); o["image_examples"] = []
                lo.append(o)
            nt = {
                "media": media_by.get(tid, []),
                "2d_tool": None,
                "summary": a.get("summary"),
                "concepts": concepts,
                "topic_id": tid,
                "key_terms": t.get("key_terms", []),
                "depends_on": t.get("depends_on", []),
                "difficulty": t.get("difficulty"),
                "topic_name": t["topic_name"],
                "topic_type": t["topic_type"],
                "word_count": t.get("word_count"),
                "explanation": a.get("explanation"),
                "brief_summary": a.get("brief_summary"),
                "objective_ids": t["objective_ids"],
                "modified_chunk": t.get("modified_chunk"),
                "original_chunk": t["original_chunk"],
                "topic_category": t.get("topic_category"),
                "concept_bullets": a.get("concept_bullets", []),
                "detailed_summary": a.get("detailed_summary"),
                "important_points": a.get("important_points", []),
                "publication_text": p.get("publication_text"),
                "recall_questions": a.get("recall_questions", []),
                "source_topic_ids": t.get("source_topic_ids", []),
                "publication_chunk": p.get("publication_chunk"),
                "real_life_example": a.get("real_life_example"),
                "estimated_exchanges": a.get("estimated_exchanges"),
                "learning_objectives": lo,
                "primary_content_type": t.get("primary_content_type"),
                "tertiary_content_type": t.get("tertiary_content_type"),
                "secondary_content_type": t.get("secondary_content_type"),
                "available_content_types": t.get("available_content_types", []),
                "figures_of_speech": a.get("figures_of_speech", []),
                "rhyme_scheme": a.get("rhyme_scheme", None),
                "shabdarth": a.get("shabdarth", []),
                "samanarthi": a.get("samanarthi", []),
                "vilom": a.get("vilom", []),
                "vyakaran": a.get("vyakaran", []),
            }
            ns["topics"].append(nt)
        nm["segments"].append(ns)
    modules.append(nm)

plan = {
    "phase": 2,
    "board": meta["board"],
    "subject": meta["subject"],
    "grade": meta["grade"],
    "level": meta["level"],
    "version": meta["version"],
    "chapter_id": meta["chapter_id"],
    "plan_id": meta["plan_id"],
    "author": "",
    "_activate": False,
    "medium_id": None,
    "subject_ref_id": None,
    "chapter_master_id": None,
    "publication_id": None,
    "estimated_time": 1.5,
    "textbook": pages.get("textbook") or meta["textbook"],
    "textbook_url": pages.get("textbook_url") or meta["textbook_url"],
    "textbook_pages": pages.get("textbook_pages", ""),
    "unit_title": meta["unit_title"],
    "unit_number": meta["unit_number"],
    "topic_title": meta["chapter_name"],
    "topic_number": meta["topic_number"],
    "chapter_name": meta["chapter_name"],
    "genre": base["genre"],
    "teaching_lens": meta["teaching_lens"],
    "guiding_question": meta["guiding_question"],
    "english_plan_id": None,
    "english_chapter_id": None,
    "objectives": base["objectives"],
    "strand_to_objective_map": base["strand_to_objective_map"],
    "modules": modules,
}

topics = [t for m in plan["modules"] for s in m["segments"] for t in s["topics"]]
segments = [s for m in plan["modules"] for s in m["segments"]]

GUJ = lambda ch: 0x0A80 <= ord(ch) <= 0x0AFF
DEV = lambda ch: 0x0900 <= ord(ch) <= 0x097F
ROM = lambda ch: ("a" <= ch <= "z") or ("A" <= ch <= "Z")
PUNCT_ONLY = re.compile(r"^[^\w\u0A80-\u0AFF]+$", re.UNICODE)
def wc(s):
    # A word is a token carrying at least one letter. Gujarati typography spaces
    # : ? ! - and em/en dashes off as free-standing tokens; a naive whitespace
    # split counts those as words and inflates the band. Pack precedent: output7/ch02.
    return len([t for t in s.split() if not PUNCT_ONLY.match(t)]) if s else 0
def wc_naive(s): return len(s.split()) if s else 0

def script_scan(s, where):
    if not s: return
    stripped = re.sub(r"\([^)]*\)", "", s)
    dev = sorted({c for c in stripped if DEV(c)})
    rom = sorted({c for c in stripped if ROM(c)})
    if dev: fail("B", "05_verbatim_attachment.md", "Devanagari " + str(dev) + " in " + where)
    if rom: fail("B", "05_verbatim_attachment.md", "Roman " + str(rom) + " in " + where)
    if "।" in s: fail("B", "05_verbatim_attachment.md", "danda in " + where)

for t in topics:
    oc = t["original_chunk"]
    if not oc or not oc.strip():
        fail("B", "05_verbatim_attachment.md", t["topic_id"] + " original_chunk empty"); continue
    if not any(GUJ(c) for c in oc):
        fail("B", "05_verbatim_attachment.md", t["topic_id"] + " original_chunk not Gujarati")
    script_scan(oc, t["topic_id"] + ".original_chunk")

marker_counts = {}
for tag in ["કડી", "દુહો", "પદ", "ઘટના", "સ્વાધ્યાય"]:
    marker_counts[tag] = len(re.findall(r"\[\[" + tag + r"[:\]]", norm))
topics_with = {}
for tag in ["કડી", "દુહો", "પદ", "ઘટના"]:
    n = 0
    for m in base["modules"]:
        for s in m["segments"]:
            for tp in s["topics"]:
                if any(mk.startswith("[[" + tag) for mk in tp.get("markers", [])): n += 1
    topics_with[tag] = n
    if marker_counts[tag] != n:
        fail("B", "02_structure.md", "[[" + tag + "]] marker count " + str(marker_counts[tag]) +
             " != topics carrying it " + str(n))

for m in base["modules"]:
    for s in m["segments"]:
        for tp in s["topics"]:
            for mk in tp.get("markers", []):
                if mk.startswith("[[સ્વાધ્યાય"):
                    fail("B", "02_structure.md", tp["topic_id"] + " carries a svadhyay marker")

DISPLAY_FIELDS = ["topic_name","explanation","real_life_example","brief_summary","summary","detailed_summary"]
for t in topics:
    tid = t["topic_id"]
    for f in ("explanation", "real_life_example"):
        if not t.get(f) or not t[f].strip():
            fail("C", "12_runtime_authoring.md", tid + " " + f + " empty")
        else:
            n = wc(t[f])
            if not (55 <= n <= 90):
                fail("C", "12_runtime_authoring.md", tid + " " + f + " is " + str(n) + " words (band 55-90)")
    b, s2, d2 = wc(t["brief_summary"]), wc(t["summary"]), wc(t["detailed_summary"])
    if not (b < s2 < d2):
        fail("Contract", "12_runtime_authoring.md",
             tid + " summaries not strictly increasing (" + str(b) + "/" + str(s2) + "/" + str(d2) + ")")
    for f in DISPLAY_FIELDS: script_scan(t.get(f), tid + "." + f)
    for i, bl in enumerate(t["concept_bullets"] + t["important_points"]):
        script_scan(bl, tid + ".bullet[" + str(i) + "]")
    for rq in t["recall_questions"]:
        script_scan(rq["prompt"], rq["id"] + ".prompt")
        script_scan(rq["answer"], rq["id"] + ".answer")

for o in plan["objectives"]:
    n = wc(o["objective_text"])
    if not (12 <= n <= 30):
        fail("C", "02_structure.md", o["objective_id"] + " objective_text " + str(n) + " words (band 12-30)")
    script_scan(o["objective_text"], o["objective_id"] + ".objective_text")

DIGITS = re.compile(r"[0-9૦-૯]")
for t in topics:
    for f in DISPLAY_FIELDS:
        v = t.get(f)
        if v and DIGITS.search(v):
            fail("Contract", "12_runtime_authoring.md", t["topic_id"] + "." + f + " numeral " + DIGITS.search(v).group())
    for i, bl in enumerate(t["concept_bullets"] + t["important_points"]):
        if DIGITS.search(bl): fail("Contract","12_runtime_authoring.md", t["topic_id"] + ".bullet[" + str(i) + "] numeral")
    for rq in t["recall_questions"]:
        for k in ("prompt","answer"):
            if DIGITS.search(rq[k]): fail("Contract","12_runtime_authoring.md", rq["id"] + "." + k + " numeral")
    for c in t["concepts"]:
        if DIGITS.search(c["concept_name"]): fail("Contract","02_structure.md", c["concept_id"] + " concept_name numeral")
        for i, blk in enumerate(c["content"]):
            txt = blk.get("text") or " ".join(blk.get("items", []))
            if DIGITS.search(txt): fail("Contract","12_runtime_authoring.md", c["concept_id"] + ".content[" + str(i) + "] numeral")
for o in plan["objectives"]:
    if DIGITS.search(o["objective_text"]): fail("Contract","02_structure.md", o["objective_id"] + " numeral")
for m in plan["modules"]:
    if DIGITS.search(m["module_name"]): fail("Contract","02_structure.md", m["module_id"] + " name numeral")
for s in segments:
    if DIGITS.search(s["segment_name"]): fail("Contract","02_structure.md", s["segment_id"] + " name numeral")

AREAS = set(["ધર્મ","સમુદાય","ક્ષેત્ર","વિકલાંગતા","સંઘર્ષ","જાતિ-ભૂમિકા","સુરક્ષા"])
for s in sens.get("topics", []):
    bad = [a for a in s["areas"] if a not in AREAS]
    if bad: fail("D","08_sensitivity_safety.md", s["topic_id"] + " unknown area " + str(bad))

for t in topics:
    oc = t["original_chunk"]
    for i, f in enumerate(t["figures_of_speech"] or []):
        lines = f.get("lines","")
        if lines and lines not in oc:
            fail("D","12_runtime_authoring.md", t["topic_id"] + " figures_of_speech[" + str(i) + "].lines not verbatim")

if plan["phase"] != 2: fail("Contract","01_ingestion_genre_diagnosis.md","phase != 2")
exp_cid = "gseb_eng_gujarati" + str(plan["grade"]) + "_ch" + str(plan["unit_number"])
if plan["chapter_id"] != exp_cid:
    fail("Contract","01_ingestion_genre_diagnosis.md","chapter_id " + plan["chapter_id"] + " != " + exp_cid)
if plan["plan_id"] != plan["chapter_id"] + "_v" + str(plan["version"]):
    fail("Contract","01_ingestion_genre_diagnosis.md","plan_id malformed")

ids = set()
for o in plan["objectives"]:
    if o["objective_id"] in ids: fail("Contract","02_structure.md","duplicate " + o["objective_id"])
    ids.add(o["objective_id"])
topic_ids = set(t["topic_id"] for t in topics)
concept_ids = set(c["concept_id"] for t in topics for c in t["concepts"])
for o in plan["objectives"]:
    if o["home_topic_id"] not in topic_ids: fail("Contract","02_structure.md", o["objective_id"] + " home_topic_id unresolved")
    for a in o["anchor"]:
        if a not in concept_ids: fail("Contract","02_structure.md", o["objective_id"] + " anchor " + a + " unresolved")
for lid, oid in plan["strand_to_objective_map"].items():
    if oid not in ids: fail("Contract","02_structure.md","strand map " + lid + " unresolved")
legacies = set(o["legacy_id"] for o in plan["objectives"])
ml = legacies - set(plan["strand_to_objective_map"])
if ml: fail("Contract","02_structure.md","strand map misses " + str(sorted(ml)))

ENUM = set(["instructional","summary","assessment"])
AUTHORED = set(["POEM","STORY_TELLING","CONCEPT","REVIEW"])
for t in topics:
    if t["topic_type"] not in AUTHORED | ENUM:
        fail("Contract","02_structure.md", t["topic_id"] + " topic_type " + str(t["topic_type"]))
    if not t["concepts"]: fail("Contract","02_structure.md", t["topic_id"] + " no concepts")
    for oid in t["objective_ids"]:
        if oid not in ids: fail("Contract","02_structure.md", t["topic_id"] + " objective " + oid + " unresolved")
    for c in t["concepts"]:
        if c["objective_id"] not in ids: fail("Contract","02_structure.md", c["concept_id"] + " objective unresolved")
        if not c["content"]: fail("Contract","12_runtime_authoring.md", c["concept_id"] + " content[] empty")
    for lo in t["learning_objectives"]:
        if lo["objective_text"] != obj_by[lo["objective_id"]]["objective_text"]:
            fail("Contract","12_runtime_authoring.md", t["topic_id"] + " inline mirror drift")
    for d in t["depends_on"]:
        if d not in topic_ids: fail("Contract","02_structure.md", t["topic_id"] + " depends_on " + d + " unresolved")

cn = 0
for m in plan["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            if not re.fullmatch(r"M\d+\.S\d+\.T\d+", t["topic_id"]):
                fail("Contract","02_structure.md","bad topic_id " + t["topic_id"])
            for c in t["concepts"]:
                cn += 1
                if not re.fullmatch(re.escape(t["topic_id"]) + r"\.C\d+", c["concept_id"]):
                    fail("Contract","02_structure.md","bad concept_id " + c["concept_id"])
                elif int(c["concept_id"].split(".C")[1]) != cn:
                    fail("Contract","02_structure.md","concept counter: expected .C" + str(cn) + ", got " + c["concept_id"])
            for i, rq in enumerate(t["recall_questions"], 1):
                if rq["id"] != t["topic_id"] + ".RQ" + str(i):
                    fail("Contract","12_runtime_authoring.md","bad recall id " + rq["id"])
                if rq.get("legacy_id") != t["topic_id"] + ".TR" + str(i):
                    fail("Contract","12_runtime_authoring.md","bad recall legacy_id " + str(rq.get("legacy_id")))
                if ".SR" in rq["id"]: fail("Contract","12_runtime_authoring.md","SR id " + rq["id"])

MEDIA_ID_RE = re.compile(r"^(M\d+\.S\d+\.T\d+\.C\d+)\.(IMG|VID|2D|3D|SIM)(\d+)$")
n_2d = 0
for t in topics:
    for mn in t["media"]:
        mm = MEDIA_ID_RE.match(mn["id"])
        if not mm: fail("Contract","09_media_planning.md","media id " + mn["id"] + " fails MEDIA_ID_RE")
        elif mm.group(1) not in concept_ids: fail("Contract","09_media_planning.md","media " + mn["id"] + " concept unresolved")
        if mn.get("image_url"): fail("Media","09_media_planning.md", mn["id"] + " non-empty image_url")
        if not mn.get("generation_prompt"): fail("Media","09_media_planning.md", mn["id"] + " empty generation_prompt")
        if "Devanagari script labels" not in (mn.get("negative_prompt") or ""):
            fail("Media","09_media_planning.md", mn["id"] + " negative_prompt lacks Devanagari script labels")
        if "[reused frame" in json.dumps(mn, ensure_ascii=False):
            fail("Media","09_media_planning.md", mn["id"] + " reused-frame stamp")
    if t["2d_tool"]: n_2d += 1
if med.get("2d_tool"): n_2d += 1
if n_2d > 1: fail("Media","09_media_planning.md", str(n_2d) + " 2d_tools (max 1)")

rr = med["reuse_report"]
img_topics = [t for t in topics if "image" in (t["available_content_types"] or [])]
if rr["scenes"] != len(img_topics):
    fail("Media","09_media_planning.md","reuse_report.scenes " + str(rr["scenes"]) + " != topics declaring image " + str(len(img_topics)))
if rr["authored"] != rr["scenes"]: fail("Media","09_media_planning.md","authored != scenes")
if rr["reused"] != 0: fail("Media","09_media_planning.md","reused != 0")

inv = [b["verbatim_heading"] for b in meta["exercise_inventory"]]
cr = exsol["coverage_report"]
def norm_h(s):
    s = re.sub(r"\s+", "", s)
    for a, b in [("આપો","લખો"),("વાક્યોમાં","વાક્યમાં"),("સવિસ્તાર","સવિસ્તર")]:
        s = s.replace(a, b)
    return s
found = [norm_h(x) for x in cr["blocks_found"]]
for h in inv:
    if norm_h(h) not in found: fail("Exercises","10_exercise_solutions.md","inventory block missing: " + h)
if len(cr["blocks_found"]) != len(inv):
    fail("Exercises","10_exercise_solutions.md","blocks_found " + str(len(cr["blocks_found"])) + " != inventory " + str(len(inv)))
if cr["unanswered"]: fail("Exercises","10_exercise_solutions.md","unanswered: " + str(cr["unanswered"]))

VOCATIVES = ["બાળકો", "જુઓ —", "બોલો"]
for t in topics:
    tid = t["topic_id"]
    if not t["publication_text"]: fail("Publication","16_publication_authoring.md", tid + " publication_text missing")
    if not t["publication_chunk"]: fail("Publication","16_publication_authoring.md", tid + " publication_chunk missing")
    elif t["original_chunk"] not in t["publication_chunk"]:
        fail("Publication","16_publication_authoring.md", tid + " original_chunk not preserved byte-exact in publication_chunk")
    for v in VOCATIVES:
        if t["publication_text"] and v in t["publication_text"]:
            fail("Publication","16_publication_authoring.md", tid + " publication_text carries vocative/instruction")
    script_scan(t.get("publication_text"), tid + ".publication_text")
    a = auth_by[tid]
    want = [(c["concept_id"], i) for c in a.get("concepts", []) for i, b in enumerate(c["content"]) if b.get("type") == "paragraph"]
    got = [(cp["concept_id"], cp["content_index"]) for cp in pub_by[tid].get("concept_publication", [])]
    if want != got:
        fail("Publication","16_publication_authoring.md", tid + " concept_publication index mismatch")

out = os.path.join(D, "13_merged.json")
json.dump(plan, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print("TOPICS", len(topics), "CONCEPTS", cn, "OBJECTIVES", len(plan["objectives"]))
print("markers", json.dumps(marker_counts, ensure_ascii=False), "topics_with", json.dumps(topics_with, ensure_ascii=False))
print("media nodes", sum(len(t["media"]) for t in topics), "reuse", rr)
print("word bands (lexical | naive):", [(t["topic_id"], wc(t["explanation"]), wc_naive(t["explanation"]), wc(t["real_life_example"]), wc_naive(t["real_life_example"])) for t in topics])
print("obj words:", [(o["objective_id"], wc(o["objective_text"]), wc_naive(o["objective_text"])) for o in plan["objectives"]])
print("wc.original vs recomputed:", [(t["topic_id"], t["word_count"], wc_naive(t["original_chunk"])) for t in topics])
print("pub_text words:", [(t["topic_id"], wc(t["publication_text"])) for t in topics])
print("PROBLEMS", len(problems))
for s, o, txt in problems:
    print("  [" + s + "] (" + o + ") " + txt)
