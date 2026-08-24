#!/usr/bin/env python3
# Agent 14 — arrange, renumber, translate references, emit learning_plan_logical.json
import json, re, collections, sys, os

OUT = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output8/ch03"
merged = json.load(open(os.path.join(OUT, "13_merged.json"), encoding="utf-8"))

ROOT_ORDER = ["phase","board","subject","grade","level","version","ordering","author",
    "chapter_id","plan_id","chapter_name","unit_title","unit_number","topic_title","topic_number",
    "genre","teaching_lens","guiding_question","textbook","textbook_url","textbook_pages",
    "_activate","medium_id","subject_ref_id","publication_id","chapter_master_id","estimated_time",
    "english_plan_id","english_chapter_id","objectives","strand_to_objective_map","modules"]

MOD_ORDER = ["module_id","module_name","difficult_words","overall_rhyme_scheme","segments"]
SEG_ORDER = ["segment_id","segment_name","topics"]
TOPIC_ORDER = ["topic_id","topic_name","topic_type","topic_category","difficulty",
    "original_chunk","modified_chunk","word_count","explanation","real_life_example",
    "brief_summary","summary","detailed_summary","key_terms","concept_bullets","important_points",
    "figures_of_speech","rhyme_scheme","shabdarth","samanarthi","vilom","vyakaran",
    "objective_ids","learning_objectives","concepts","recall_questions","media","2d_tool",
    "publication_text","publication_chunk","depends_on","source_topic_ids","estimated_exchanges",
    "primary_content_type","secondary_content_type","tertiary_content_type","available_content_types"]
OBJ_ORDER = ["objective_id","legacy_id","strand","strand_name","objective_text","bloom_level",
    "home_topic_id","anchor","status","theme_category"]
INLINE_OBJ_ORDER = OBJ_ORDER + ["image_examples"]
CONCEPT_ORDER = ["concept_id","concept_name","objective_id","key_terms","content"]
MEDIA_ORDER = ["id","type","subtype","title","description","image_url","aspect_ratio",
    "concept_id","home_concept_id","objective_id","image_category","teaching_notes",
    "negative_prompt","generation_prompt"]
RQ_ORDER = ["id","legacy_id","prompt","answer","bloom_level","difficulty"]

TYPE_MAP = {"POEM":"instructional","STORY_TELLING":"instructional","CONCEPT":"instructional",
            "REVIEW":"summary","EXERCISE":"assessment"}

# ---------- 1. arrange (reading order = merged traversal, confirmed vs 05b_textbook_order.json)
modules = merged["modules"]

# ---------- 2. renumber consecutively, chapter-continuous m/s/t/c
idmap = {}          # old node id -> new node id
m_i = s_i = t_i = c_i = 0
for mod in modules:
    m_i += 1
    new_m = "M%d" % m_i
    idmap[mod["module_id"]] = new_m
    for seg in mod["segments"]:
        s_i += 1
        new_s = "%s.S%d" % (new_m, s_i)
        idmap[seg["segment_id"]] = new_s
        for top in seg["topics"]:
            t_i += 1
            new_t = "%s.T%d" % (new_s, t_i)
            idmap[top["topic_id"]] = new_t
            for con in top["concepts"]:
                c_i += 1
                idmap[con["concept_id"]] = "%s.C%d" % (new_t, c_i)

NODE_RE = re.compile(r"^M\d+(?:\.S\d+(?:\.T\d+(?:\.C\d+)?)?)?$")

def mapnode(old):
    if old is None:
        return None
    if old not in idmap:
        raise SystemExit("STALE REFERENCE: %r resolves to no node" % old)
    return idmap[old]

def mapsuffixed(old, allowed):
    """old like '<node>.RQ1' / '<node>.TR1' / '<node>.IMG1'"""
    node, _, suf = old.rpartition(".")
    if not re.match(r"^(%s)\d+$" % "|".join(allowed), suf):
        raise SystemExit("BAD SUFFIXED ID: %r" % old)
    return mapnode(node) + "." + suf

def order(d, keys):
    out = collections.OrderedDict()
    for k in keys:
        if k in d:
            out[k] = d[k]
    extra = [k for k in d if k not in keys]
    if extra:
        raise SystemExit("NON-WHITELIST KEYS %r" % extra)
    return out

# ---------- 3. translate every reference
new_modules = []
for mod in modules:
    mod = dict(mod)
    mod["module_id"] = mapnode(mod["module_id"])
    new_segs = []
    for seg in mod["segments"]:
        seg = dict(seg)
        seg["segment_id"] = mapnode(seg["segment_id"])
        if seg.get("recall_questions"):
            for rq in seg["recall_questions"]:
                rq["id"] = mapsuffixed(rq["id"].replace(".SR", ".RQ"), ["RQ"])
                if rq.get("legacy_id"):
                    rq["legacy_id"] = mapsuffixed(rq["legacy_id"], ["TR", "SR"])
        new_tops = []
        for top in seg["topics"]:
            top = dict(top)
            top["topic_id"] = mapnode(top["topic_id"])
            top["topic_type"] = TYPE_MAP[top["topic_type"]] if top["topic_type"] in TYPE_MAP else top["topic_type"]
            if top["topic_type"] not in ("instructional", "summary", "assessment"):
                raise SystemExit("BAD topic_type %r" % top["topic_type"])
            top["depends_on"] = [mapnode(x) for x in (top.get("depends_on") or [])]
            top["source_topic_ids"] = [mapnode(x) for x in (top.get("source_topic_ids") or [])]
            top["concepts"] = [order({**c, "concept_id": mapnode(c["concept_id"])}, CONCEPT_ORDER)
                               for c in top["concepts"]]
            rqs = []
            for rq in (top.get("recall_questions") or []):
                rq = dict(rq)
                rq["id"] = mapsuffixed(rq["id"], ["RQ"])
                rq["legacy_id"] = mapsuffixed(rq["legacy_id"], ["TR"])
                rqs.append(order(rq, RQ_ORDER))
            top["recall_questions"] = rqs
            meds = []
            for md in (top.get("media") or []):
                md = dict(md)
                md["id"] = mapsuffixed(md["id"], ["IMG", "VID", "2D", "3D", "SIM"])
                md["concept_id"] = mapnode(md["concept_id"])
                md["home_concept_id"] = mapnode(md["home_concept_id"])
                meds.append(order(md, MEDIA_ORDER))
            top["media"] = meds
            top["learning_objectives"] = [order({**lo,
                    "home_topic_id": mapnode(lo["home_topic_id"]),
                    "anchor": [mapnode(a) for a in lo.get("anchor") or []],
                    "image_examples": lo.get("image_examples") or []}, INLINE_OBJ_ORDER)
                for lo in (top.get("learning_objectives") or [])]
            new_tops.append(order(top, TOPIC_ORDER))
        seg["topics"] = new_tops
        new_segs.append(order(seg, SEG_ORDER))
    mod["segments"] = new_segs
    new_modules.append(order(mod, MOD_ORDER))

objectives = []
for ob in merged["objectives"]:
    ob = dict(ob)
    ob["home_topic_id"] = mapnode(ob["home_topic_id"])
    ob["anchor"] = [mapnode(a) for a in ob.get("anchor") or []]
    objectives.append(order(ob, OBJ_ORDER))

# ---------- 4/5/6. root assembly
plan = dict(merged)
plan["modules"] = new_modules
plan["objectives"] = objectives
plan["ordering"] = "logical"
plan["phase"] = 2
plan["_activate"] = False
plan["medium_id"] = None
plan["subject_ref_id"] = None
plan["english_plan_id"] = None
plan["english_chapter_id"] = None
plan["chapter_id"] = "gseb_eng_gujarati%d_ch%d" % (plan["grade"], plan["unit_number"])
plan["plan_id"] = "%s_v%d" % (plan["chapter_id"], plan["version"])

cm = json.load(open("/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/upload_reference/chapter_master_map.json",
                    encoding="utf-8")).get(plan["chapter_id"], {})
plan["chapter_master_id"] = cm.get("chapter_master_id")
plan["publication_id"] = cm.get("publication_id")

plan = order(plan, ROOT_ORDER)
assert len(plan) == 32, len(plan)

# ---------- assertions: no stale reference anywhere
live_nodes = set(idmap.values())
obj_ids = {o["objective_id"] for o in objectives}
errors = []

def chk(nid, where):
    if nid not in live_nodes:
        errors.append("%s -> %s" % (where, nid))

for o in objectives:
    chk(o["home_topic_id"], "objectives.home_topic_id")
    for a in o["anchor"]:
        chk(a, "objectives.anchor")
for lid, oid in plan["strand_to_objective_map"].items():
    if oid not in obj_ids:
        errors.append("strand_to_objective_map %s -> %s" % (lid, oid))
for lid in {o["legacy_id"] for o in objectives}:
    if lid not in plan["strand_to_objective_map"]:
        errors.append("legacy_id %s missing from strand_to_objective_map" % lid)

seen_m = seen_s = seen_t = seen_c = 0
for mi, mod in enumerate(plan["modules"], 1):
    if mod["module_id"] != "M%d" % mi:
        errors.append("module traversal %s" % mod["module_id"])
    for seg in mod["segments"]:
        seen_s += 1
        if seg["segment_id"] != "M%d.S%d" % (mi, seen_s):
            errors.append("segment traversal %s" % seg["segment_id"])
        for rq in (seg.get("recall_questions") or []):
            if not re.match(r"^%s\.RQ\d+$" % re.escape(seg["segment_id"]), rq["id"]):
                errors.append("segment recall id %s" % rq["id"])
        for top in seg["topics"]:
            seen_t += 1
            exp_t = "%s.T%d" % (seg["segment_id"], seen_t)
            if top["topic_id"] != exp_t:
                errors.append("topic traversal %s != %s" % (top["topic_id"], exp_t))
            for oid in top["objective_ids"]:
                if oid not in obj_ids:
                    errors.append("topic %s objective_ids -> %s" % (top["topic_id"], oid))
            reg = {o["objective_id"]: o for o in objectives}
            for lo in top["learning_objectives"]:
                if lo["objective_id"] not in obj_ids:
                    errors.append("inline objective %s" % lo["objective_id"])
                elif lo["objective_text"] != reg[lo["objective_id"]]["objective_text"]:
                    errors.append("inline mirror text drift on %s / %s" % (top["topic_id"], lo["objective_id"]))
                chk(lo["home_topic_id"], "inline home_topic_id")
                for a in lo["anchor"]:
                    chk(a, "inline anchor")
            for d in top["depends_on"]:
                chk(d, "depends_on")
            for d in top["source_topic_ids"]:
                chk(d, "source_topic_ids")
            for con in top["concepts"]:
                seen_c += 1
                exp_c = "%s.C%d" % (top["topic_id"], seen_c)
                if con["concept_id"] != exp_c:
                    errors.append("concept traversal %s != %s" % (con["concept_id"], exp_c))
                if con["objective_id"] not in obj_ids:
                    errors.append("concept objective %s" % con["objective_id"])
                if not con.get("content"):
                    errors.append("empty concept content %s" % con["concept_id"])
            cids = {c["concept_id"] for c in top["concepts"]}
            for rq in top["recall_questions"]:
                if not re.match(r"^%s\.RQ\d+$" % re.escape(top["topic_id"]), rq["id"]):
                    errors.append("topic recall id %s" % rq["id"])
                if not re.match(r"^%s\.TR\d+$" % re.escape(top["topic_id"]), rq["legacy_id"]):
                    errors.append("topic recall legacy_id %s" % rq["legacy_id"])
            for md in top["media"]:
                if not re.match(r"^M\d+\.S\d+\.T\d+\.C\d+\.(IMG|VID|2D|3D|SIM)\d+$", md["id"]):
                    errors.append("media id %s" % md["id"])
                if md["concept_id"] not in cids or md["home_concept_id"] not in cids:
                    errors.append("media concept scope %s" % md["id"])
                if not md["id"].startswith(md["concept_id"] + "."):
                    errors.append("media id/concept mismatch %s" % md["id"])
                if not md.get("image_url") and not md.get("generation_prompt"):
                    errors.append("media %s has neither image_url nor generation_prompt" % md["id"])
            if not top.get("original_chunk", "").strip():
                errors.append("empty original_chunk %s" % top["topic_id"])
            b, s_, dsum = len(top["brief_summary"]), len(top["summary"]), len(top["detailed_summary"])
            if not (b < s_ < dsum):
                errors.append("summary tiers not increasing on %s (%d/%d/%d)" % (top["topic_id"], b, s_, dsum))

if errors:
    print("HARD FAIL:")
    for e in errors:
        print("  -", e)
    sys.exit(1)

# stale-id sweep over the serialized plan
blob = json.dumps(plan, ensure_ascii=False)
for found in set(re.findall(r"M\d+(?:\.S\d+)?(?:\.T\d+)?(?:\.C\d+)?(?:\.(?:RQ|TR|IMG|VID|2D|3D|SIM)\d+)?", blob)):
    base = re.sub(r"\.(?:RQ|TR|IMG|VID|2D|3D|SIM)\d+$", "", found)
    if base not in live_nodes:
        print("HARD FAIL: dangling id in serialized plan:", found)
        sys.exit(1)

with open(os.path.join(OUT, "learning_plan_logical.json"), "w", encoding="utf-8") as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)
    f.write("\n")

# ---------- covered_by_topics rewrite in 10_exercise_solutions.json
ex_path = os.path.join(OUT, "10_exercise_solutions.json")
ex = json.load(open(ex_path, encoding="utf-8"))
changed = 0
for e in ex["exercises"]:
    new = []
    for tid in (e.get("covered_by_topics") or []):
        n = mapnode(tid)
        changed += (n != tid)
        new.append(n)
    e["covered_by_topics"] = new
ex["plan_id"] = plan["plan_id"]
ex["chapter_id"] = plan["chapter_id"]
if changed:
    with open(ex_path, "w", encoding="utf-8") as f:
        json.dump(ex, f, ensure_ascii=False, indent=2)
        f.write("\n")

# ---------- copy to exercise_solutions.json
with open(os.path.join(OUT, "exercise_solutions.json"), "w", encoding="utf-8") as f:
    json.dump(ex, f, ensure_ascii=False, indent=2)
    f.write("\n")

print("OK modules=%d segments=%d topics=%d concepts=%d objectives=%d rootkeys=%d covered_by_topics_rewritten=%d"
      % (len(plan["modules"]), seen_s, seen_t, seen_c, len(objectives), len(plan), changed))
print("identity_renumber =", all(k == v for k, v in idmap.items()))
