#!/usr/bin/env python3
# Agent 14 — std 6, ch 4: arrange, renumber, translate refs, whitelist, emit.
import json, re, sys, collections

D = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch04"
merged = json.load(open(f"{D}/13_merged.json"))
exsol = json.load(open(f"{D}/10_exercise_solutions.json"))

# ---------- 1. arrange: reading sequence = merged traversal (05b confirms printed order matches)
# ---------- 2. renumber consecutively along traversal
old2new = {}
m = s = t = c = 0
for mod in merged["modules"]:
    m += 1; nm = f"M{m}"; old2new[mod["module_id"]] = nm
    for seg in mod["segments"]:
        s += 1; ns = f"{nm}.S{s}"; old2new[seg["segment_id"]] = ns
        for top in seg["topics"]:
            t += 1; nt = f"{ns}.T{t}"; old2new[top["topic_id"]] = nt
            for con in top["concepts"]:
                c += 1; old2new[con["concept_id"]] = f"{nt}.C{c}"

def mapid(x):
    return old2new.get(x, x)

# ---------- 3. translate every reference
TOPIC_TYPE = {"POEM": "instructional", "STORY_TELLING": "instructional",
              "CONCEPT": "instructional", "REVIEW": "summary", "EXERCISE": "assessment"}

ROOT_ORDER = ["phase","board","subject","grade","level","version","ordering","author",
              "chapter_id","plan_id","chapter_name","unit_title","unit_number","topic_title",
              "topic_number","genre","teaching_lens","guiding_question","textbook","textbook_url",
              "textbook_pages","_activate","medium_id","subject_ref_id","publication_id",
              "chapter_master_id","estimated_time","english_plan_id","english_chapter_id",
              "objectives","strand_to_objective_map","modules"]

TOPIC_ORDER = ["topic_id","topic_name","topic_type","topic_category","difficulty",
               "original_chunk","modified_chunk","word_count","explanation","real_life_example",
               "brief_summary","summary","detailed_summary","key_terms","concept_bullets",
               "important_points","figures_of_speech","rhyme_scheme","shabdarth","samanarthi",
               "vilom","vyakaran","objective_ids","learning_objectives","concepts",
               "recall_questions","media","2d_tool","publication_text","publication_chunk",
               "depends_on","source_topic_ids","estimated_exchanges","primary_content_type",
               "secondary_content_type","tertiary_content_type","available_content_types"]

OBJ_ORDER = ["objective_id","legacy_id","strand","strand_name","objective_text","bloom_level",
             "home_topic_id","anchor","status","theme_category"]
LO_ORDER = OBJ_ORDER + ["image_examples"]
MEDIA_ORDER = ["id","type","subtype","title","description","image_url","aspect_ratio",
               "concept_id","home_concept_id","objective_id","image_category","teaching_notes",
               "negative_prompt","generation_prompt"]

def reorder(d, order):
    out = {k: d[k] for k in order if k in d}
    for k in d:
        if k not in out:
            out[k] = d[k]
    return out

# root objectives registry — O{n} and strand map are NOT renumbered
objectives = []
for o in merged["objectives"]:
    o = dict(o)
    o["home_topic_id"] = mapid(o["home_topic_id"])
    o["anchor"] = [mapid(a) for a in o["anchor"]]
    objectives.append(reorder(o, OBJ_ORDER))
obj_by_id = {o["objective_id"]: o for o in objectives}

modules = []
for mod in merged["modules"]:
    nmod = {"module_id": mapid(mod["module_id"]), "module_name": mod["module_name"],
            "difficult_words": mod["difficult_words"],
            "overall_rhyme_scheme": mod["overall_rhyme_scheme"], "segments": []}
    for seg in mod["segments"]:
        nseg = {"segment_id": mapid(seg["segment_id"]), "segment_name": seg["segment_name"],
                "topics": []}
        # segment-level recalls, if this pack's segments ever carry them: {segment_id}.RQ{n}
        if "recall_questions" in seg:
            rqs = []
            for i, rq in enumerate(seg["recall_questions"], 1):
                rq = dict(rq); rq["id"] = f"{nseg['segment_id']}.RQ{i}"
                rqs.append(rq)
            nseg["recall_questions"] = rqs
        for top in seg["topics"]:
            nt = mapid(top["topic_id"])
            ntop = dict(top)
            ntop["topic_id"] = nt
            ntop["topic_type"] = TOPIC_TYPE[top["topic_type"]]
            ntop["objective_ids"] = list(top["objective_ids"])
            ntop["depends_on"] = [mapid(x) for x in top["depends_on"]]
            ntop["source_topic_ids"] = [mapid(x) for x in top["source_topic_ids"]]
            los = []
            for lo in top["learning_objectives"]:
                lo = dict(lo)
                root = obj_by_id[lo["objective_id"]]
                lo["objective_text"] = root["objective_text"]      # keep mirror identical
                lo["home_topic_id"] = root["home_topic_id"]
                lo["anchor"] = list(root["anchor"])
                lo.setdefault("image_examples", [])
                los.append(reorder(lo, LO_ORDER))
            ntop["learning_objectives"] = los
            ntop["recall_questions"] = [
                dict(rq, id=f"{nt}.RQ{i}", legacy_id=f"{nt}.TR{i}")
                for i, rq in enumerate(top["recall_questions"], 1)]
            cons = []
            for con in top["concepts"]:
                con = dict(con)
                con["concept_id"] = mapid(con["concept_id"])
                cons.append(con)
            ntop["concepts"] = cons
            meds = []
            for md in top["media"]:
                md = dict(md)
                oldc = md["concept_id"]
                suffix = md["id"][len(oldc) + 1:]
                md["concept_id"] = mapid(oldc)
                md["home_concept_id"] = mapid(md["home_concept_id"])
                md["id"] = f"{md['concept_id']}.{suffix}"
                meds.append(reorder(md, MEDIA_ORDER))
            ntop["media"] = meds
            nseg["topics"].append(reorder(ntop, TOPIC_ORDER))
        nmod["segments"].append(nseg)
    modules.append(nmod)

# ---------- 6. root fields
plan = dict(merged)
plan["ordering"] = "logical"
plan["phase"] = 2
plan["objectives"] = objectives
plan["modules"] = modules
plan["chapter_id"] = f"gseb_eng_gujarati{merged['grade']}_ch{merged['unit_number']}"
plan["plan_id"] = f"{plan['chapter_id']}_v{merged['version']}"
plan["english_plan_id"] = None
plan["english_chapter_id"] = None
plan["subject_ref_id"] = None
plan["medium_id"] = None
plan["_activate"] = False
plan = reorder(plan, ROOT_ORDER)
assert list(plan.keys()) == ROOT_ORDER, [k for k in plan if k not in ROOT_ORDER]

# ---------- assert: no reference resolves to a node that no longer exists
nodes = set(old2new.values())
objids = set(obj_by_id)
errs = []
for o in plan["objectives"]:
    if o["home_topic_id"] not in nodes: errs.append(("obj.home", o["objective_id"]))
    for a in o["anchor"]:
        if a not in nodes: errs.append(("obj.anchor", o["objective_id"], a))
for lid, oid in plan["strand_to_objective_map"].items():
    if oid not in objids: errs.append(("strand_map", lid, oid))
seen_m = seen_s = seen_t = seen_c = 0
for mod in plan["modules"]:
    seen_m += 1
    if mod["module_id"] != f"M{seen_m}": errs.append(("module_id", mod["module_id"]))
    for seg in mod["segments"]:
        seen_s += 1
        if seg["segment_id"] != f"M{seen_m}.S{seen_s}": errs.append(("segment_id", seg["segment_id"]))
        for rq in seg.get("recall_questions", []):
            if not re.match(rf"^{re.escape(seg['segment_id'])}\.RQ\d+$", rq["id"]):
                errs.append(("seg.rq", rq["id"]))
        for top in seg["topics"]:
            seen_t += 1
            tid = top["topic_id"]
            if tid != f"{seg['segment_id']}.T{seen_t}": errs.append(("topic_id", tid))
            if top["topic_type"] not in ("instructional", "summary", "assessment"):
                errs.append(("topic_type", tid, top["topic_type"]))
            for k in top:
                if k not in TOPIC_ORDER: errs.append(("topic key not whitelisted", tid, k))
            for oid in top["objective_ids"]:
                if oid not in objids: errs.append(("topic.objective_ids", tid, oid))
            for lo in top["learning_objectives"]:
                r = obj_by_id[lo["objective_id"]]
                if lo["objective_text"] != r["objective_text"]: errs.append(("mirror", tid))
                if lo["home_topic_id"] not in nodes: errs.append(("lo.home", tid))
                for a in lo["anchor"]:
                    if a not in nodes: errs.append(("lo.anchor", tid, a))
            for x in top["depends_on"] + top["source_topic_ids"]:
                if x not in nodes: errs.append(("depends/source", tid, x))
            for i, rq in enumerate(top["recall_questions"], 1):
                if rq["id"] != f"{tid}.RQ{i}": errs.append(("topic.rq", rq["id"]))
                if rq["legacy_id"] != f"{tid}.TR{i}": errs.append(("topic.rq.legacy", rq["legacy_id"]))
            if not top["concepts"]: errs.append(("no concepts", tid))
            for con in top["concepts"]:
                seen_c += 1
                if con["concept_id"] != f"{tid}.C{seen_c}": errs.append(("concept_id", con["concept_id"]))
                if con["objective_id"] not in objids: errs.append(("concept.objective_id", con["concept_id"]))
                if not con.get("content"): errs.append(("concept.content", con["concept_id"]))
            cids = {con["concept_id"] for con in top["concepts"]}
            for md in top["media"]:
                if not re.match(r"^M\d+\.S\d+\.T\d+\.C\d+\.(IMG|VID|2D|3D|SIM)\d+$", md["id"]):
                    errs.append(("media.id", md["id"]))
                if md["concept_id"] not in cids or md["home_concept_id"] not in nodes:
                    errs.append(("media.concept", md["id"]))
                if not md["id"].startswith(md["concept_id"] + "."):
                    errs.append(("media.prefix", md["id"]))
                if md["image_url"] == "" and not md["generation_prompt"]:
                    errs.append(("media.empty", md["id"]))
if ".SR" in json.dumps(plan): errs.append(("SR recall id present",))
for bad in ("POEM", "STORY_TELLING", "CONCEPT", "REVIEW"):
    if f'"topic_type": "{bad}"' in json.dumps(plan, ensure_ascii=False): errs.append(("authored enum leaked", bad))
if errs:
    print("HARD FAIL", errs); sys.exit(1)

# ---------- covered_by_topics rewrite (identity here — nothing moved)
ex_changed = False
for e in exsol["exercises"]:
    new = [mapid(x) for x in e["covered_by_topics"]]
    if new != e["covered_by_topics"]:
        e["covered_by_topics"] = new; ex_changed = True
for u in exsol["coverage_report"].get("unmapped", []):
    if u.get("covered_by_topics"):
        new = [mapid(x) for x in u["covered_by_topics"]]
        if new != u["covered_by_topics"]:
            u["covered_by_topics"] = new; ex_changed = True
stale = {x for e in exsol["exercises"] for x in e["covered_by_topics"] if x not in nodes}
assert not stale, stale
if ex_changed:
    json.dump(exsol, open(f"{D}/10_exercise_solutions.json", "w"), ensure_ascii=False, indent=1)
print("exercise covered_by_topics rewritten:", ex_changed)

json.dump(plan, open(f"{D}/learning_plan_logical.json", "w"), ensure_ascii=False, indent=1)
json.dump(exsol, open(f"{D}/exercise_solutions.json", "w"), ensure_ascii=False, indent=1)
print("renumbered nodes:", len(old2new), "| ids changed:",
      sum(1 for k, v in old2new.items() if k != v))
print("modules", seen_m, "segments", seen_s, "topics", seen_t, "concepts", seen_c)
