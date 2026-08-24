#!/usr/bin/env python3
# Agent 14 — arrange in reading order, renumber M/S/T/C consecutively,
# translate every reference, apply the whitelist, map topic_type.
import json, os, re, sys
from collections import OrderedDict

OUT = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output7/ch01"
MERGED = os.path.join(OUT, "13_merged.json")
EXSRC = os.path.join(OUT, "10_exercise_solutions.json")

with open(MERGED, encoding="utf-8") as f:
    src = json.load(f, object_pairs_hook=OrderedDict)
with open(os.path.join(OUT, "05b_textbook_order.json"), encoding="utf-8") as f:
    tb = json.load(f)

# ---------------------------------------------------------------- 1. arrange
# Reading sequence = the merged structure's own traversal order (05b confirms
# printed order == this order for this chapter). No re-sorting is applied.
traversal = [t["topic_id"] for m in src["modules"] for s in m["segments"] for t in s["topics"]]
assert traversal == tb["textbook_order"], (traversal, tb["textbook_order"])

# ------------------------------------------------- 2. renumber + build old->new
idmap = {}          # node ids: module / segment / topic / concept
m = s = t = c = 0
for mod in src["modules"]:
    m += 1
    new_m = "M%d" % m
    idmap[mod["module_id"]] = new_m
    for seg in mod["segments"]:
        s += 1
        new_s = "%s.S%d" % (new_m, s)
        idmap[seg["segment_id"]] = new_s
        for top in seg["topics"]:
            t += 1
            new_t = "%s.T%d" % (new_s, t)
            idmap[top["topic_id"]] = new_t
            for con in top["concepts"]:
                c += 1
                new_c = "%s.C%d" % (new_t, c)
                idmap[con["concept_id"]] = new_c

def nid(old):
    if old is None:
        return None
    if old not in idmap:
        raise KeyError("stale reference to a node that does not exist: %r" % old)
    return idmap[old]

# ------------------------------------------------------------- 3. whitelists
ROOT_KEYS = ["phase", "board", "subject", "grade", "level", "version", "ordering",
             "chapter_id", "plan_id", "author", "_activate", "medium_id",
             "subject_ref_id", "chapter_master_id", "publication_id",
             "english_plan_id", "english_chapter_id", "estimated_time",
             "textbook", "textbook_url", "textbook_pages", "unit_title",
             "unit_number", "topic_title", "topic_number", "chapter_name",
             "genre", "teaching_lens", "guiding_question", "objectives",
             "strand_to_objective_map", "modules"]
assert len(ROOT_KEYS) == 32, len(ROOT_KEYS)

TOPIC_KEYS = ["topic_id", "topic_name", "topic_type", "topic_category", "difficulty",
              "depends_on", "source_topic_ids", "objective_ids", "learning_objectives",
              "original_chunk", "modified_chunk", "publication_chunk", "word_count",
              "key_terms", "explanation", "real_life_example", "publication_text",
              "brief_summary", "summary", "detailed_summary", "concept_bullets",
              "important_points", "concepts", "recall_questions", "media", "2d_tool",
              "estimated_exchanges",
              # કાવ્ય extras
              "figures_of_speech", "rhyme_scheme",
              # optional ભાષા-બોધ extras (romanized key names, as the server stores them)
              "shabdarth", "samanarthi", "vilom", "vyakaran",
              "primary_content_type", "secondary_content_type", "tertiary_content_type",
              "available_content_types"]
CORE_TOPIC = [k for k in TOPIC_KEYS if k not in
              ("figures_of_speech", "rhyme_scheme", "shabdarth", "samanarthi",
               "vilom", "vyakaran")]
assert len(CORE_TOPIC) == 31, len(CORE_TOPIC)

OBJ_KEYS = ["objective_id", "legacy_id", "strand", "strand_name", "objective_text",
            "bloom_level", "home_topic_id", "anchor", "status", "theme_category"]
LO_KEYS = OBJ_KEYS + ["image_examples"]
CONCEPT_KEYS = ["concept_id", "concept_name", "objective_id", "key_terms", "content"]
RQ_KEYS = ["id", "legacy_id", "prompt", "answer", "difficulty", "bloom_level"]
MEDIA_KEYS = ["id", "type", "subtype", "title", "description", "image_url",
              "aspect_ratio", "concept_id", "home_concept_id", "objective_id",
              "image_category", "teaching_notes", "negative_prompt", "generation_prompt"]
MODULE_KEYS = ["module_id", "module_name", "difficult_words", "overall_rhyme_scheme",
               "segments"]
SEGMENT_KEYS = ["segment_id", "segment_name", "recall_questions", "topics"]

def pick(obj, keys):
    return OrderedDict((k, obj[k]) for k in keys if k in obj)

# --------------------------------------------------- 5. topic_type at emit
TYPE_MAP = {"POEM": "instructional", "STORY_TELLING": "instructional",
            "CONCEPT": "instructional", "REVIEW": "summary", "EXERCISE": "assessment",
            # already-mapped values pass through unchanged
            "instructional": "instructional", "summary": "summary",
            "assessment": "assessment"}

MEDIA_ID_RE = re.compile(r"^(M\d+\.S\d+\.T\d+\.C\d+)\.(IMG|VID|2D|3D|SIM)(\d+)$")

def objective_out(o, keys):
    out = pick(o, keys)
    out["home_topic_id"] = nid(o["home_topic_id"])
    out["anchor"] = [nid(a) for a in o.get("anchor") or []]
    return out

# ------------------------------------------------------------- build modules
modules = []
for mod in src["modules"]:
    mo = pick(mod, MODULE_KEYS)
    mo["module_id"] = nid(mod["module_id"])
    segs = []
    for seg in mod["segments"]:
        so = pick(seg, SEGMENT_KEYS)
        so["segment_id"] = nid(seg["segment_id"])
        if "recall_questions" in so:
            rqs = []
            for i, r in enumerate(seg.get("recall_questions") or [], 1):
                ro = pick(r, RQ_KEYS)
                # segment recalls are {segment_id}.RQ{n} — never .SR{n}
                ro["id"] = "%s.RQ%d" % (so["segment_id"], i)
                if "legacy_id" in ro:
                    ro["legacy_id"] = "%s.TR%d" % (so["segment_id"], i)
                rqs.append(ro)
            so["recall_questions"] = rqs
        tops = []
        for top in seg["topics"]:
            to = pick(top, TOPIC_KEYS)
            new_t = nid(top["topic_id"])
            to["topic_id"] = new_t
            to["topic_type"] = TYPE_MAP[top["topic_type"]]
            to["depends_on"] = [nid(x) for x in top.get("depends_on") or []]
            to["source_topic_ids"] = [nid(x) for x in top.get("source_topic_ids") or []]
            to["learning_objectives"] = [objective_out(o, LO_KEYS)
                                         for o in top.get("learning_objectives") or []]
            cons = []
            for con in top["concepts"]:
                co = pick(con, CONCEPT_KEYS)
                co["concept_id"] = nid(con["concept_id"])
                cons.append(co)
            to["concepts"] = cons
            rqs = []
            for i, r in enumerate(top.get("recall_questions") or [], 1):
                ro = pick(r, RQ_KEYS)
                ro["id"] = "%s.RQ%d" % (new_t, i)
                ro["legacy_id"] = "%s.TR%d" % (new_t, i)
                rqs.append(ro)
            to["recall_questions"] = rqs
            meds = []
            for md in top.get("media") or []:
                mm = pick(md, MEDIA_KEYS)
                old = MEDIA_ID_RE.match(md["id"])
                if not old:
                    raise ValueError("media id does not match MEDIA_ID_RE: %r" % md["id"])
                mm["id"] = "%s.%s%s" % (nid(old.group(1)), old.group(2), old.group(3))
                mm["concept_id"] = nid(md["concept_id"])
                mm["home_concept_id"] = nid(md["home_concept_id"])
                meds.append(mm)
            to["media"] = meds
            tops.append(to)
        so["topics"] = tops
        segs.append(so)
    mo["segments"] = segs
    modules.append(mo)

# --------------------------------------------------------------- 6. root
plan = OrderedDict()
for k in ROOT_KEYS:
    if k == "ordering":
        plan[k] = "logical"
    elif k == "modules":
        plan[k] = modules
    elif k == "objectives":
        # O{n} and strand_to_objective_map are NOT renumbered; their tree
        # references are.
        plan[k] = [objective_out(o, OBJ_KEYS) for o in src["objectives"]]
    else:
        plan[k] = src[k]

grade = plan["grade"]
plan["chapter_id"] = "gseb_eng_gujarati%d_ch%d" % (grade, plan["unit_number"])
plan["plan_id"] = "%s_v%d" % (plan["chapter_id"], plan["version"])
plan["phase"] = 2
plan["_activate"] = False
plan["subject_ref_id"] = None
plan["medium_id"] = None
plan["english_plan_id"] = None
plan["english_chapter_id"] = None

# chapter_master_id / publication_id come from upload_reference/chapter_master_map.json
cm = json.load(open("/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/"
                    "upload_reference/chapter_master_map.json", encoding="utf-8"))
row = cm.get(plan["chapter_id"], {})
plan["chapter_master_id"] = row.get("chapter_master_id")
plan["publication_id"] = row.get("publication_id")

# ------------------------------------------------------------- 7. ASSERTIONS
nodes = set()
for mod in plan["modules"]:
    nodes.add(mod["module_id"])
    for seg in mod["segments"]:
        nodes.add(seg["segment_id"])
        for top in seg["topics"]:
            nodes.add(top["topic_id"])
            for con in top["concepts"]:
                nodes.add(con["concept_id"])

errs = []
def need(x, where):
    if x not in nodes:
        errs.append("stale reference %r in %s" % (x, where))

objids = set()
for o in plan["objectives"]:
    if o["objective_id"] in objids:
        errs.append("duplicate objective_id %s" % o["objective_id"])
    objids.add(o["objective_id"])
    need(o["home_topic_id"], "objectives[%s].home_topic_id" % o["objective_id"])
    for a in o["anchor"]:
        need(a, "objectives[%s].anchor" % o["objective_id"])
objtext = {o["objective_id"]: o["objective_text"] for o in plan["objectives"]}

for lid, oid in plan["strand_to_objective_map"].items():
    if oid not in objids:
        errs.append("strand_to_objective_map[%s] -> unknown %s" % (lid, oid))
for o in plan["objectives"]:
    if plan["strand_to_objective_map"].get(o["legacy_id"]) != o["objective_id"]:
        errs.append("strand_to_objective_map missing %s" % o["legacy_id"])

# traversal-position id check (the validator checks position, not just grammar)
mi = si = ti = ci = 0
for mod in plan["modules"]:
    mi += 1
    if mod["module_id"] != "M%d" % mi:
        errs.append("expected module_id=M%d, got %s" % (mi, mod["module_id"]))
    for seg in mod["segments"]:
        si += 1
        exp = "M%d.S%d" % (mi, si)
        if seg["segment_id"] != exp:
            errs.append("expected segment_id=%s, got %s" % (exp, seg["segment_id"]))
        for r in seg.get("recall_questions") or []:
            if not r["id"].startswith(seg["segment_id"] + ".RQ"):
                errs.append("bad segment recall id %s" % r["id"])
        for top in seg["topics"]:
            ti += 1
            expt = "%s.T%d" % (exp, ti)
            if top["topic_id"] != expt:
                errs.append("expected topic_id=%s, got %s" % (expt, top["topic_id"]))
            if top["topic_type"] not in ("instructional", "summary", "assessment"):
                errs.append("bad topic_type %s" % top["topic_type"])
            if not top.get("original_chunk", "").strip():
                errs.append("%s empty original_chunk" % top["topic_id"])
            for x in top["depends_on"]:
                need(x, "%s.depends_on" % top["topic_id"])
            for x in top["source_topic_ids"]:
                need(x, "%s.source_topic_ids" % top["topic_id"])
            for oid in top["objective_ids"]:
                if oid not in objids:
                    errs.append("%s.objective_ids -> unknown %s" % (top["topic_id"], oid))
            for lo in top["learning_objectives"]:
                if lo["objective_text"] != objtext.get(lo["objective_id"]):
                    errs.append("%s inline objective_text drift for %s"
                                % (top["topic_id"], lo["objective_id"]))
                need(lo["home_topic_id"], "%s.learning_objectives.home_topic_id" % top["topic_id"])
                for a in lo["anchor"]:
                    need(a, "%s.learning_objectives.anchor" % top["topic_id"])
            if not top["concepts"]:
                errs.append("%s has no concepts" % top["topic_id"])
            for con in top["concepts"]:
                ci += 1
                expc = "%s.C%d" % (expt, ci)
                if con["concept_id"] != expc:
                    errs.append("expected concept_id=%s, got %s" % (expc, con["concept_id"]))
                if con["objective_id"] not in objids:
                    errs.append("%s.objective_id -> unknown %s"
                                % (con["concept_id"], con["objective_id"]))
                if not con.get("content"):
                    errs.append("%s empty content" % con["concept_id"])
            for i, r in enumerate(top["recall_questions"], 1):
                if r["id"] != "%s.RQ%d" % (expt, i):
                    errs.append("bad recall id %s" % r["id"])
                if r.get("legacy_id") != "%s.TR%d" % (expt, i):
                    errs.append("bad recall legacy_id %s" % r.get("legacy_id"))
            for md in top["media"]:
                mo2 = MEDIA_ID_RE.match(md["id"])
                if not mo2:
                    errs.append("media id fails regex: %s" % md["id"])
                    continue
                need(mo2.group(1), "media %s" % md["id"])
                need(md["concept_id"], "media[%s].concept_id" % md["id"])
                need(md["home_concept_id"], "media[%s].home_concept_id" % md["id"])
                if mo2.group(1) != md["concept_id"]:
                    errs.append("media %s not scoped to its concept_id" % md["id"])
                if not md.get("image_url") and not md.get("generation_prompt"):
                    errs.append("media %s has neither image_url nor generation_prompt" % md["id"])
            # three-tier summaries strictly increase
            a, b, cc = (len(top["brief_summary"]), len(top["summary"]),
                        len(top["detailed_summary"]))
            if not (a < b < cc):
                errs.append("%s summaries not strictly increasing (%d,%d,%d)"
                            % (top["topic_id"], a, b, cc))

for k in ROOT_KEYS:
    if k not in plan:
        errs.append("missing root key %s" % k)
if set(plan.keys()) != set(ROOT_KEYS):
    errs.append("root key set mismatch: %s" % (set(plan.keys()) ^ set(ROOT_KEYS)))

# ------------------------------------ 8. covered_by_topics rewrite in 10_*.json
with open(EXSRC, encoding="utf-8") as f:
    ex = json.load(f, object_pairs_hook=OrderedDict)
changed = 0
for e in ex["exercises"]:
    old = e.get("covered_by_topics") or []
    new = [nid(x) for x in old]
    if new != old:
        changed += 1
    e["covered_by_topics"] = new
    for x in new:
        need(x, "%s.covered_by_topics" % e["exercise_id"])
ex["plan_id"] = plan["plan_id"]
ex["chapter_id"] = plan["chapter_id"]

if errs:
    print("HARD FAIL:")
    for e in errs:
        print("  -", e)
    sys.exit(1)

with open(os.path.join(OUT, "learning_plan_logical.json"), "w", encoding="utf-8") as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)
    f.write("\n")
if changed:
    with open(EXSRC, "w", encoding="utf-8") as f:
        json.dump(ex, f, ensure_ascii=False, indent=2)
        f.write("\n")
with open(os.path.join(OUT, "exercise_solutions.json"), "w", encoding="utf-8") as f:
    json.dump(ex, f, ensure_ascii=False, indent=2)
    f.write("\n")

identity = all(k == v for k, v in idmap.items())
print("OK. nodes=%d  idmap identity=%s  covered_by_topics rewritten=%d  exercises=%d"
      % (len(nodes), identity, changed, len(ex["exercises"])))
print("modules=%d segments=%d topics=%d concepts=%d" % (mi, si, ti, ci))
