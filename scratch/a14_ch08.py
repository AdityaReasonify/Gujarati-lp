#!/usr/bin/env python3
"""Agent 14 — arrange, renumber, translate references, emit learning_plan_logical.json."""
import json, os, shutil, sys

D = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch08"
merged = json.load(open(os.path.join(D, "13_merged.json"), encoding="utf-8"))

ROOT_KEYS = ["board", "genre", "grade", "level", "phase", "author", "modules", "plan_id",
             "subject", "version", "ordering", "textbook", "_activate", "medium_id",
             "chapter_id", "objectives", "unit_title", "topic_title", "unit_number",
             "chapter_name", "textbook_url", "topic_number", "teaching_lens",
             "estimated_time", "publication_id", "subject_ref_id", "textbook_pages",
             "english_plan_id", "guiding_question", "chapter_master_id",
             "english_chapter_id", "strand_to_objective_map"]

TOPIC_KEYS = ["media", "2d_tool", "summary", "concepts", "topic_id", "key_terms",
              "depends_on", "difficulty", "topic_name", "topic_type", "word_count",
              "explanation", "brief_summary", "objective_ids", "modified_chunk",
              "original_chunk", "topic_category", "concept_bullets", "detailed_summary",
              "important_points", "publication_text", "recall_questions",
              "source_topic_ids", "publication_chunk", "real_life_example",
              "estimated_exchanges", "learning_objectives", "primary_content_type",
              "tertiary_content_type", "secondary_content_type",
              "available_content_types",
              # કાવ્ય extras
              "figures_of_speech", "rhyme_scheme",
              # optional ભાષા-બોધ extras (romanized keys, as the server stores them)
              "shabdarth", "samanarthi", "vilom", "vyakaran"]

MODULE_KEYS = ["module_id", "module_name", "difficult_words", "overall_rhyme_scheme", "segments"]
SEGMENT_KEYS = ["segment_id", "segment_name", "topics"]

TYPE_MAP = {"POEM": "instructional", "STORY_TELLING": "instructional",
            "CONCEPT": "instructional", "REVIEW": "summary", "EXERCISE": "assessment",
            "instructional": "instructional", "summary": "summary", "assessment": "assessment"}

# ---------------------------------------------------------------- 1. arrange
# Reading order = the merged tree's own order, which 05b_textbook_order.json
# confirms is the printed order of the letter (સરનામું/તારીખ/સંબોધન → કાર્ડ →
# મૃદુલ ઘોષ → મનોજ ભિંગારે → મંડળ ને ભેટ → સમાપન).
order = json.load(open(os.path.join(D, "05b_textbook_order.json"), encoding="utf-8"))
walk_order = [t["topic_id"] for m in merged["modules"] for s in m["segments"] for t in s["topics"]]
assert walk_order == order["textbook_order"], (walk_order, order["textbook_order"])

# ---------------------------------------------------------------- 2. renumber
idmap = {}          # old id -> new id  (modules, segments, topics, concepts)
m_i = s_i = t_i = c_i = 0
for m in merged["modules"]:
    m_i += 1
    new_m = "M%d" % m_i
    idmap[m["module_id"]] = new_m
    for s in m["segments"]:
        s_i += 1
        new_s = "%s.S%d" % (new_m, s_i)
        idmap[s["segment_id"]] = new_s
        for t in s["topics"]:
            t_i += 1
            new_t = "%s.T%d" % (new_s, t_i)
            idmap[t["topic_id"]] = new_t
            for c in t.get("concepts") or []:
                c_i += 1
                new_c = "%s.C%d" % (new_t, c_i)
                idmap[c["concept_id"]] = new_c

def nid(old):
    if old not in idmap:
        raise KeyError("stale reference: %r" % (old,))
    return idmap[old]

# ---------------------------------------------------------------- 3. rewrite
def prune(d, keys):
    out = {}
    for k in keys:
        if k in d:
            out[k] = d[k]
    dropped = [k for k in d if k not in keys]
    return out, dropped

dropped_keys = set()
new_modules = []
for m in merged["modules"]:
    mm, dr = prune(m, MODULE_KEYS); dropped_keys |= set(dr)
    mm["module_id"] = nid(m["module_id"])
    new_segments = []
    for s in m["segments"]:
        ss, dr = prune(s, SEGMENT_KEYS); dropped_keys |= set(dr)
        old_sid = s["segment_id"]
        ss["segment_id"] = nid(old_sid)
        # segment-level recalls, if any: {segment_id}.RQ{n}
        if "recall_questions" in s and s["recall_questions"]:
            rqs = []
            for i, r in enumerate(s["recall_questions"], 1):
                r = dict(r)
                r["id"] = "%s.RQ%d" % (ss["segment_id"], i)
                if "legacy_id" in r:
                    r["legacy_id"] = "%s.TR%d" % (ss["segment_id"], i)
                rqs.append(r)
            ss["recall_questions"] = rqs
        new_topics = []
        for t in s["topics"]:
            tt, dr = prune(t, TOPIC_KEYS); dropped_keys |= set(dr)
            old_tid = t["topic_id"]
            new_tid = nid(old_tid)
            tt["topic_id"] = new_tid
            tt["topic_type"] = TYPE_MAP[t["topic_type"]]
            tt["depends_on"] = [nid(x) for x in (t.get("depends_on") or [])]
            tt["source_topic_ids"] = [nid(x) for x in (t.get("source_topic_ids") or [])]
            # concepts
            tt["concepts"] = []
            for c in t.get("concepts") or []:
                c = dict(c)
                c["concept_id"] = nid(c["concept_id"])
                tt["concepts"].append(c)
            # topic recalls
            rqs = []
            for i, r in enumerate(t.get("recall_questions") or [], 1):
                r = dict(r)
                r["id"] = "%s.RQ%d" % (new_tid, i)
                r["legacy_id"] = "%s.TR%d" % (new_tid, i)
                rqs.append(r)
            tt["recall_questions"] = rqs
            # media — concept-scoped
            media = []
            per_concept = {}
            for md in t.get("media") or []:
                md = dict(md)
                new_cid = nid(md["concept_id"])
                suffix = md["id"].rsplit(".", 1)[1]
                kind = "".join(ch for ch in suffix if not ch.isdigit())
                per_concept.setdefault((new_cid, kind), 0)
                per_concept[(new_cid, kind)] += 1
                md["id"] = "%s.%s%d" % (new_cid, kind, per_concept[(new_cid, kind)])
                md["concept_id"] = new_cid
                if md.get("home_concept_id"):
                    md["home_concept_id"] = nid(md["home_concept_id"])
                media.append(md)
            tt["media"] = media
            # inline learning objectives
            los = []
            for lo in t.get("learning_objectives") or []:
                lo = dict(lo)
                lo["home_topic_id"] = nid(lo["home_topic_id"])
                lo["anchor"] = [nid(a) for a in (lo.get("anchor") or [])]
                lo.setdefault("image_examples", [])
                los.append(lo)
            tt["learning_objectives"] = los
            new_topics.append(tt)
        ss["topics"] = new_topics
        new_segments.append(ss)
    mm["segments"] = new_segments
    new_modules.append(mm)

# root objectives registry — O{n} and strand_to_objective_map are NOT renumbered
new_objectives = []
for o in merged["objectives"]:
    o = dict(o)
    o["home_topic_id"] = nid(o["home_topic_id"])
    o["anchor"] = [nid(a) for a in (o.get("anchor") or [])]
    new_objectives.append(o)

# ---------------------------------------------------------------- root fields
plan = dict(merged)
plan["modules"] = new_modules
plan["objectives"] = new_objectives
plan["phase"] = 2
plan["ordering"] = "logical"
plan["version"] = merged.get("version") or 1
plan["chapter_id"] = "gseb_eng_gujarati%d_ch%d" % (plan["grade"], plan["unit_number"])
plan["plan_id"] = "%s_v%d" % (plan["chapter_id"], plan["version"])
plan["_activate"] = False
plan["subject_ref_id"] = None
plan["medium_id"] = None
plan["english_plan_id"] = None
plan["english_chapter_id"] = None

cmm = json.load(open("/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/upload_reference/chapter_master_map.json", encoding="utf-8"))
row = cmm.get(plan["chapter_id"]) or {}
plan["chapter_master_id"] = row.get("chapter_master_id")          # null until VERIFY-2
pub = row.get("publication_id")
if pub is None:
    pub = merged.get("publication_id")                            # sibling-chapter precedent
plan["publication_id"] = pub
assert plan["publication_id"] is not None, "publication_id must not be null"

plan, dr_root = prune(plan, ROOT_KEYS)
dropped_keys |= set(dr_root)
assert len(plan) == 32, (len(plan), sorted(plan))
assert set(plan) == set(ROOT_KEYS)

# ---------------------------------------------------------------- 4. assert
node_ids, concept_ids, topic_ids = set(), set(), set()
for m in plan["modules"]:
    node_ids.add(m["module_id"])
    for s in m["segments"]:
        node_ids.add(s["segment_id"])
        for t in s["topics"]:
            node_ids.add(t["topic_id"]); topic_ids.add(t["topic_id"])
            for c in t["concepts"]:
                node_ids.add(c["concept_id"]); concept_ids.add(c["concept_id"])

obj_ids = {o["objective_id"] for o in plan["objectives"]}
errs = []

# traversal-position id check (the validator's own check)
mi = si = ti = ci = 0
for m in plan["modules"]:
    mi += 1
    if m["module_id"] != "M%d" % mi: errs.append("module %s" % m["module_id"])
    for s in m["segments"]:
        si += 1
        exp_s = "M%d.S%d" % (mi, si)
        if s["segment_id"] != exp_s: errs.append("segment %s != %s" % (s["segment_id"], exp_s))
        for t in s["topics"]:
            ti += 1
            exp_t = "%s.T%d" % (exp_s, ti)
            if t["topic_id"] != exp_t: errs.append("topic %s != %s" % (t["topic_id"], exp_t))
            for c in t["concepts"]:
                ci += 1
                exp_c = "%s.C%d" % (exp_t, ci)
                if c["concept_id"] != exp_c: errs.append("concept %s != %s" % (c["concept_id"], exp_c))

for o in plan["objectives"]:
    if o["home_topic_id"] not in topic_ids: errs.append("obj %s home %s" % (o["objective_id"], o["home_topic_id"]))
    for a in o["anchor"]:
        if a not in concept_ids: errs.append("obj %s anchor %s" % (o["objective_id"], a))
for lid, oid in plan["strand_to_objective_map"].items():
    if oid not in obj_ids: errs.append("strand map %s->%s" % (lid, oid))
for o in plan["objectives"]:
    if o["legacy_id"] not in plan["strand_to_objective_map"]: errs.append("legacy %s unmapped" % o["legacy_id"])

reg = {o["objective_id"]: o for o in plan["objectives"]}
for m in plan["modules"]:
    for s in m["segments"]:
        for r in s.get("recall_questions") or []:
            if not r["id"].startswith(s["segment_id"] + ".RQ"): errs.append("seg recall %s" % r["id"])
        for t in s["topics"]:
            for x in t["depends_on"] + t["source_topic_ids"]:
                if x not in topic_ids: errs.append("%s dep/src %s" % (t["topic_id"], x))
            for oid in t["objective_ids"]:
                if oid not in obj_ids: errs.append("%s objective_ids %s" % (t["topic_id"], oid))
            for c in t["concepts"]:
                if c["objective_id"] not in obj_ids: errs.append("%s concept obj %s" % (c["concept_id"], c["objective_id"]))
                if not c.get("content"): errs.append("%s empty content" % c["concept_id"])
            for lo in t["learning_objectives"]:
                if lo["objective_id"] not in obj_ids: errs.append("%s inline obj" % t["topic_id"])
                elif lo["objective_text"] != reg[lo["objective_id"]]["objective_text"]:
                    errs.append("%s inline text drift %s" % (t["topic_id"], lo["objective_id"]))
                elif lo["home_topic_id"] != reg[lo["objective_id"]]["home_topic_id"] or \
                     lo["anchor"] != reg[lo["objective_id"]]["anchor"]:
                    errs.append("%s inline anchor drift %s" % (t["topic_id"], lo["objective_id"]))
            for r in t["recall_questions"]:
                if not r["id"].startswith(t["topic_id"] + ".RQ"): errs.append("recall %s" % r["id"])
                if not r["legacy_id"].startswith(t["topic_id"] + ".TR"): errs.append("recall legacy %s" % r["legacy_id"])
            for md in t["media"]:
                if md["concept_id"] not in concept_ids: errs.append("media %s concept" % md["id"])
                if md.get("home_concept_id") and md["home_concept_id"] not in concept_ids: errs.append("media %s home" % md["id"])
                if not md["id"].startswith(md["concept_id"] + "."): errs.append("media id scope %s" % md["id"])
            if t["topic_type"] not in ("instructional", "summary", "assessment"):
                errs.append("topic_type %s" % t["topic_type"])
            if set(t) - set(TOPIC_KEYS): errs.append("topic extra keys %s" % (set(t) - set(TOPIC_KEYS)))

if errs:
    print("HARD FAIL:"); [print(" ", e) for e in errs]; sys.exit(1)

out = os.path.join(D, "learning_plan_logical.json")
json.dump(plan, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
open(out, "a", encoding="utf-8").write("\n")
print("wrote", out)
print("identity renumber:", all(k == v for k, v in idmap.items()))
print("dropped working keys:", sorted(dropped_keys) or "none")

# ------------------------------------------- 5. covered_by_topics rewrite
exp = os.path.join(D, "10_exercise_solutions.json")
ex = json.load(open(exp, encoding="utf-8"))
changed = 0
for e in ex["exercises"]:
    new = [nid(x) for x in e.get("covered_by_topics") or []]
    if new != e.get("covered_by_topics"):
        changed += 1
    e["covered_by_topics"] = new
    for x in new:
        assert x in topic_ids, x
ex["plan_id"] = plan["plan_id"]
ex["chapter_id"] = plan["chapter_id"]
json.dump(ex, open(exp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
open(exp, "a", encoding="utf-8").write("\n")
print("covered_by_topics rewritten in 10_exercise_solutions.json; entries changed:", changed)

shutil.copyfile(exp, os.path.join(D, "exercise_solutions.json"))
print("copied -> exercise_solutions.json")
