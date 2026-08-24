#!/usr/bin/env python3
# Agent 14 — arrange, renumber, translate references, whitelist, emit.
import json, collections, re, sys, os

OUT = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch09"
OD = collections.OrderedDict

def load(p):
    with open(os.path.join(OUT, p), encoding="utf-8") as f:
        return json.load(f, object_pairs_hook=OD)

merged = load("13_merged.json")

# ---------- 1. arrange (reading order = merged traversal, confirmed against 05b) ----------
# ---------- 2. renumber consecutively along the traversal ----------
idmap = {}          # old id -> new id  (all levels)
mediamap = {}       # old media id -> new media id
rqmap = {}          # old recall id -> new recall id

m_i = 0
s_i = 0
t_i = 0
c_i = 0
for mod in merged["modules"]:
    m_i += 1
    new_m = "M%d" % m_i
    idmap[mod["module_id"]] = new_m
    for seg in mod["segments"]:
        s_i += 1
        new_s = "%s.S%d" % (new_m, s_i)
        idmap[seg["segment_id"]] = new_s
        for r in seg.get("recall_questions", []) or []:
            n = r["id"].rsplit(".RQ", 1)[-1]
            rqmap[r["id"]] = "%s.RQ%s" % (new_s, n)
            if r.get("legacy_id"):
                n2 = r["legacy_id"].rsplit(".TR", 1)[-1]
                rqmap[r["legacy_id"]] = "%s.TR%s" % (new_s, n2)
        for top in seg["topics"]:
            t_i += 1
            new_t = "%s.T%d" % (new_s, t_i)
            idmap[top["topic_id"]] = new_t
            for con in top.get("concepts", []) or []:
                c_i += 1
                new_c = "%s.C%d" % (new_t, c_i)
                idmap[con["concept_id"]] = new_c
            for r in top.get("recall_questions", []) or []:
                n = r["id"].rsplit(".RQ", 1)[-1]
                rqmap[r["id"]] = "%s.RQ%s" % (new_t, n)
                if r.get("legacy_id"):
                    n2 = r["legacy_id"].rsplit(".TR", 1)[-1]
                    rqmap[r["legacy_id"]] = "%s.TR%s" % (new_t, n2)
            for med in top.get("media", []) or []:
                mm = re.match(r"^(M\d+\.S\d+\.T\d+\.C\d+)\.(IMG|VID|2D|3D|SIM)(\d+)$", med["id"])
                assert mm, "bad media id %s" % med["id"]
                mediamap[med["id"]] = "%s.%s%s" % (idmap[mm.group(1)], mm.group(2), mm.group(3))

def tr(i):
    if i is None:
        return None
    if i not in idmap:
        raise SystemExit("STALE reference, no such node: %r" % (i,))
    return idmap[i]

# ---------- 3. translate every reference ----------
plan = OD()

ROOT_ORDER = ["board", "genre", "grade", "level", "phase", "author", "modules", "plan_id",
              "subject", "version", "ordering", "textbook", "_activate", "medium_id",
              "chapter_id", "objectives", "unit_title", "topic_title", "unit_number",
              "chapter_name", "textbook_url", "topic_number", "teaching_lens",
              "estimated_time", "publication_id", "subject_ref_id", "textbook_pages",
              "english_plan_id", "guiding_question", "chapter_master_id",
              "english_chapter_id", "strand_to_objective_map"]

TOPIC_ORDER = ["media", "2d_tool", "summary", "concepts", "topic_id", "key_terms",
               "depends_on", "difficulty", "topic_name", "topic_type", "word_count",
               "explanation", "brief_summary", "objective_ids", "modified_chunk",
               "original_chunk", "topic_category", "concept_bullets", "detailed_summary",
               "important_points", "publication_text", "recall_questions",
               "source_topic_ids", "publication_chunk", "real_life_example",
               "estimated_exchanges", "learning_objectives", "primary_content_type",
               "tertiary_content_type", "secondary_content_type", "available_content_types"]
TOPIC_EXTRAS = ["figures_of_speech", "rhyme_scheme", "shabdarth", "samanarthi", "vilom", "vyakaran"]

TYPE_MAP = {"POEM": "instructional", "STORY_TELLING": "instructional",
            "CONCEPT": "instructional", "REVIEW": "summary", "EXERCISE": "assessment",
            "instructional": "instructional", "summary": "summary", "assessment": "assessment"}

def fix_objective(o, inline):
    n = OD()
    for k, v in o.items():
        if k == "home_topic_id":
            v = tr(v)
        elif k == "anchor":
            v = [tr(a) for a in (v or [])]
        n[k] = v
    if inline and "image_examples" not in n:
        n["image_examples"] = []
    return n

# root objectives registry (O{n} NOT renumbered)
plan_objectives = [fix_objective(o, False) for o in merged["objectives"]]

new_modules = []
for mod in merged["modules"]:
    nm = OD()
    for k, v in mod.items():
        if k == "module_id":
            nm[k] = idmap[v]
        elif k == "segments":
            continue
        else:
            nm[k] = v
    segs = []
    for seg in mod["segments"]:
        ns = OD()
        for k, v in seg.items():
            if k == "segment_id":
                ns[k] = idmap[v]
            elif k == "topics":
                continue
            elif k == "recall_questions":
                rs = []
                for r in v or []:
                    nr = OD()
                    for rk, rv in r.items():
                        if rk in ("id", "legacy_id"):
                            rv = rqmap[rv]
                        nr[rk] = rv
                    rs.append(nr)
                ns[k] = rs
            else:
                ns[k] = v
        tops = []
        for top in seg["topics"]:
            nt = OD()
            for k in TOPIC_ORDER + TOPIC_EXTRAS:
                if k not in top:
                    if k in TOPIC_ORDER:
                        raise SystemExit("topic %s missing required key %s" % (top["topic_id"], k))
                    continue
                v = top[k]
                if k == "topic_id":
                    v = idmap[v]
                elif k == "topic_type":
                    v = TYPE_MAP[v]
                elif k in ("depends_on", "source_topic_ids"):
                    v = [tr(x) for x in (v or [])]
                elif k == "concepts":
                    cs = []
                    for c in v:
                        nc = OD()
                        for ck, cv in c.items():
                            if ck == "concept_id":
                                cv = idmap[cv]
                            nc[ck] = cv
                        cs.append(nc)
                    v = cs
                elif k == "media":
                    ms = []
                    for md in v or []:
                        nmd = OD()
                        for mk, mv in md.items():
                            if mk == "id":
                                mv = mediamap[mv]
                            elif mk in ("concept_id", "home_concept_id"):
                                mv = tr(mv)
                            nmd[mk] = mv
                        ms.append(nmd)
                    v = ms
                elif k == "recall_questions":
                    rs = []
                    for r in v or []:
                        nr = OD()
                        for rk, rv in r.items():
                            if rk in ("id", "legacy_id"):
                                rv = rqmap[rv]
                            nr[rk] = rv
                        rs.append(nr)
                    v = rs
                elif k == "learning_objectives":
                    v = [fix_objective(o, True) for o in (v or [])]
                nt[k] = v
            tops.append(nt)
        ns["topics"] = tops
        segs.append(ns)
    nm["segments"] = segs
    new_modules.append(nm)

# ---------- 6. root fields ----------
GRADE = merged["grade"]
UNIT = merged["unit_number"]
chapter_id = "gseb_eng_gujarati%d_ch%d" % (GRADE, UNIT)
version = merged.get("version", 1)

root_vals = {
    "board": "gseb",
    "genre": "mahitiprad_gadya",          # slug from the active genre profile
    "grade": GRADE,
    "level": "standard",
    "phase": 2,
    "author": merged.get("author", ""),
    "modules": new_modules,
    "plan_id": "%s_v%d" % (chapter_id, version),
    "subject": "Gujarati",
    "version": version,
    "ordering": "logical",
    "textbook": merged["textbook"],
    "_activate": False,
    "medium_id": None,
    "chapter_id": chapter_id,
    "objectives": plan_objectives,
    "unit_title": merged["unit_title"],
    "topic_title": merged["topic_title"],
    "unit_number": UNIT,
    "chapter_name": merged["chapter_name"],
    "textbook_url": merged["textbook_url"],
    "topic_number": merged["topic_number"],
    "teaching_lens": merged["teaching_lens"],
    "estimated_time": merged["estimated_time"],
    "publication_id": merged["publication_id"],
    "subject_ref_id": None,
    "textbook_pages": merged["textbook_pages"],
    "english_plan_id": None,
    "guiding_question": merged["guiding_question"],
    "chapter_master_id": None,
    "english_chapter_id": None,
    "strand_to_objective_map": merged["strand_to_objective_map"],
}
for k in ROOT_ORDER:
    plan[k] = root_vals[k]
assert len(plan) == 32, len(plan)

# ---------- 3b (assert): no reference resolves to a node that no longer exists ----------
nodes = set()
concepts = set()
topics = set()
for mod in plan["modules"]:
    nodes.add(mod["module_id"])
    for seg in mod["segments"]:
        nodes.add(seg["segment_id"])
        for top in seg["topics"]:
            nodes.add(top["topic_id"]); topics.add(top["topic_id"])
            for c in top["concepts"]:
                nodes.add(c["concept_id"]); concepts.add(c["concept_id"])

errs = []
obj_ids = set()
obj_text = {}
for o in plan["objectives"]:
    if o["objective_id"] in obj_ids:
        errs.append("duplicate objective %s" % o["objective_id"])
    obj_ids.add(o["objective_id"])
    obj_text[o["objective_id"]] = o["objective_text"]
    if o["home_topic_id"] not in topics:
        errs.append("objective %s home_topic_id %s missing" % (o["objective_id"], o["home_topic_id"]))
    for a in o["anchor"]:
        if a not in concepts:
            errs.append("objective %s anchor %s missing" % (o["objective_id"], a))
for lid, oid in plan["strand_to_objective_map"].items():
    if oid not in obj_ids:
        errs.append("strand map %s -> %s missing" % (lid, oid))
for o in plan["objectives"]:
    if o["legacy_id"] not in plan["strand_to_objective_map"]:
        errs.append("legacy_id %s not in strand map" % o["legacy_id"])

MEDIA_RE = re.compile(r"^(?P<c>M\d+\.S\d+\.T\d+\.C\d+)\.(IMG|VID|2D|3D|SIM)\d+$")
n_2d = 0
mi, si, ti, ci = 0, 0, 0, 0
for mod in plan["modules"]:
    mi += 1
    if mod["module_id"] != "M%d" % mi:
        errs.append("module id gap: %s" % mod["module_id"])
    for seg in mod["segments"]:
        si += 1
        exp_s = "M%d.S%d" % (mi, si)
        if seg["segment_id"] != exp_s:
            errs.append("segment id: expected %s got %s" % (exp_s, seg["segment_id"]))
        for r in seg.get("recall_questions", []) or []:
            if not r["id"].startswith(exp_s + ".RQ"):
                errs.append("segment recall id %s" % r["id"])
        for top in seg["topics"]:
            ti += 1
            exp_t = "%s.T%d" % (exp_s, ti)
            tid = top["topic_id"]
            if tid != exp_t:
                errs.append("topic id: expected %s got %s" % (exp_t, tid))
            if top["topic_type"] not in ("instructional", "summary", "assessment"):
                errs.append("topic_type %s on %s" % (top["topic_type"], tid))
            for k in list(top.keys()):
                if k not in TOPIC_ORDER + TOPIC_EXTRAS:
                    errs.append("non-whitelist topic key %s on %s" % (k, tid))
            if not top.get("original_chunk", "").strip():
                errs.append("empty original_chunk on %s" % tid)
            if not re.search(r"[઀-૿]", top.get("original_chunk", "")):
                errs.append("original_chunk not Gujarati on %s" % tid)
            for oid in top["objective_ids"]:
                if oid not in obj_ids:
                    errs.append("topic %s objective_ids %s missing" % (tid, oid))
            for lo in top["learning_objectives"]:
                if lo["objective_id"] not in obj_ids:
                    errs.append("topic %s inline objective %s missing" % (tid, lo["objective_id"]))
                elif lo["objective_text"] != obj_text[lo["objective_id"]]:
                    errs.append("topic %s inline objective_text drift for %s" % (tid, lo["objective_id"]))
                if lo["home_topic_id"] not in topics:
                    errs.append("topic %s inline home_topic_id %s missing" % (tid, lo["home_topic_id"]))
                for a in lo["anchor"]:
                    if a not in concepts:
                        errs.append("topic %s inline anchor %s missing" % (tid, a))
            for d in top["depends_on"]:
                if d not in topics:
                    errs.append("topic %s depends_on %s missing" % (tid, d))
            for d in top["source_topic_ids"]:
                if d not in topics:
                    errs.append("topic %s source_topic_ids %s missing" % (tid, d))
            if not top["concepts"]:
                errs.append("topic %s has no concepts" % tid)
            for c in top["concepts"]:
                ci += 1
                exp_c = "%s.C%d" % (exp_t, ci)
                if c["concept_id"] != exp_c:
                    errs.append("concept id: expected %s got %s" % (exp_c, c["concept_id"]))
                if c["objective_id"] not in obj_ids:
                    errs.append("concept %s objective_id %s missing" % (c["concept_id"], c["objective_id"]))
                if not c.get("content"):
                    errs.append("concept %s empty content" % c["concept_id"])
            for r in top["recall_questions"]:
                if not r["id"].startswith(tid + ".RQ"):
                    errs.append("topic recall id %s on %s" % (r["id"], tid))
                if not r.get("legacy_id", "").startswith(tid + ".TR"):
                    errs.append("topic recall legacy_id %s on %s" % (r.get("legacy_id"), tid))
            for md in top["media"]:
                m = MEDIA_RE.match(md["id"])
                if not m:
                    errs.append("media id %s" % md["id"])
                    continue
                if m.group("c") not in concepts:
                    errs.append("media %s concept missing" % md["id"])
                if md["concept_id"] not in concepts or md["home_concept_id"] not in concepts:
                    errs.append("media %s concept_id/home_concept_id stale" % md["id"])
                if md["concept_id"] != m.group("c"):
                    errs.append("media %s id/concept_id mismatch" % md["id"])
                if not md.get("image_url") and not md.get("generation_prompt"):
                    errs.append("media %s has neither image_url nor generation_prompt" % md["id"])
            if top.get("2d_tool"):
                n_2d += 1
            # summaries strictly increase
            b, s_, dd = top["brief_summary"], top["summary"], top["detailed_summary"]
            if not (len(b) < len(s_) < len(dd)):
                errs.append("summaries not strictly increasing on %s (%d/%d/%d)" % (tid, len(b), len(s_), len(dd)))
if n_2d > 1:
    errs.append("more than one 2d_tool in the chapter: %d" % n_2d)

# no numbers in display text
NUMWORD = re.compile(r"(કડી|પ્રશ્ન|સ્વાધ્યાય|દુહો|પદ|ટેક|ફકરો|ભાગ|મુદ્દો)\s*[0-9૦-૯]")
def scan(v, where):
    if isinstance(v, str):
        m = NUMWORD.search(v)
        if m:
            errs.append("numbered display text %r in %s" % (m.group(0), where))
    elif isinstance(v, list):
        for x in v:
            scan(x, where)
DISPLAY = ["topic_name", "explanation", "real_life_example", "brief_summary", "summary",
           "detailed_summary", "concept_bullets", "important_points"]
for mod in plan["modules"]:
    scan(mod["module_name"], "module_name %s" % mod["module_id"])
    for seg in mod["segments"]:
        scan(seg["segment_name"], "segment_name %s" % seg["segment_id"])
        for top in seg["topics"]:
            for k in DISPLAY:
                scan(top.get(k), "%s.%s" % (top["topic_id"], k))
            for r in top["recall_questions"]:
                scan(r["prompt"], "%s prompt" % r["id"])

if errs:
    print("VALIDATION ERRORS (%d):" % len(errs))
    for e in errs[:80]:
        print("  -", e)
    sys.exit(1)

with open(os.path.join(OUT, "learning_plan_logical.json"), "w", encoding="utf-8") as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote learning_plan_logical.json  modules=%d segments=%d topics=%d concepts=%d"
      % (mi, si, ti, ci))

# ---------- covered_by_topics rewrite in 10_exercise_solutions.json ----------
ex = load("10_exercise_solutions.json")
changed = 0
for e in ex["exercises"]:
    new = []
    for t in e.get("covered_by_topics", []) or []:
        nt = idmap.get(t)
        if nt is None:
            raise SystemExit("covered_by_topics points at missing node %r (%s)" % (t, e["exercise_id"]))
        if nt != t:
            changed += 1
        new.append(nt)
    e["covered_by_topics"] = new
ex["plan_id"] = plan["plan_id"]
ex["chapter_id"] = plan["chapter_id"]
with open(os.path.join(OUT, "10_exercise_solutions.json"), "w", encoding="utf-8") as f:
    json.dump(ex, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("covered_by_topics ids rewritten: %d (identity map -> 0 means nothing moved)" % changed)
with open(os.path.join(OUT, "exercise_solutions.json"), "w", encoding="utf-8") as f:
    json.dump(ex, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote exercise_solutions.json  exercises=%d" % len(ex["exercises"]))
