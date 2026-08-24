# -*- coding: utf-8 -*-
"""Agent 14 — arrange in reading order, renumber M/S/T/C consecutively,
translate every reference, apply the phase-2 whitelist, emit learning_plan_logical.json."""
import json, re, sys, collections

D = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output8/ch01/"
MAP = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/upload_reference/chapter_master_map.json"

merged = json.load(open(D + "13_merged.json", encoding="utf-8"))
order  = json.load(open(D + "05b_textbook_order.json", encoding="utf-8"))
cmm    = json.load(open(MAP, encoding="utf-8"))

# ---------------------------------------------------------------- 1. arrange
# Reading order = the merged structure's own traversal (kadi after kadi).
# 05b_textbook_order.json records the printed order; it is used only as a check.
modules = merged["modules"]
traversal = [t["topic_id"] for m in modules for s in m["segments"] for t in s["topics"]]
assert traversal == order["textbook_order"], (traversal, order["textbook_order"])

# ---------------------------------------------------------------- 2. renumber
idmap = {}
m_i = s_i = t_i = c_i = 0
for m in modules:
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
            for c in t["concepts"]:
                c_i += 1
                idmap[c["concept_id"]] = "%s.C%d" % (new_t, c_i)

def tr(old):
    """Translate a node id; a dotted suffix (RQ/TR/IMG/...) rides along."""
    if old in idmap:
        return idmap[old]
    m = re.match(r"^(M\d+(?:\.S\d+)?(?:\.T\d+)?(?:\.C\d+)?)\.((?:RQ|TR|IMG|VID|2D|3D|SIM)\d+)$", old)
    if m and m.group(1) in idmap:
        return idmap[m.group(1)] + "." + m.group(2)
    raise KeyError("unresolvable id: %r" % old)

def trlist(xs):
    return [tr(x) for x in (xs or [])]

# ---------------------------------------------------------------- 3. rewrite
TOPIC_TYPE = {"POEM": "instructional", "STORY_TELLING": "instructional",
              "CONCEPT": "instructional", "REVIEW": "summary", "EXERCISE": "assessment"}

TOPIC_KEYS = ["topic_id", "topic_name", "topic_type", "topic_category", "difficulty",
              "original_chunk", "modified_chunk", "word_count", "explanation",
              "real_life_example", "brief_summary", "summary", "detailed_summary",
              "key_terms", "concept_bullets", "important_points",
              "figures_of_speech", "rhyme_scheme", "shabdarth", "samanarthi", "vilom", "vyakaran",
              "objective_ids", "learning_objectives", "concepts", "recall_questions",
              "media", "2d_tool", "publication_text", "publication_chunk",
              "depends_on", "source_topic_ids", "estimated_exchanges",
              "primary_content_type", "secondary_content_type", "tertiary_content_type",
              "available_content_types"]
OPTIONAL = {"figures_of_speech", "rhyme_scheme", "shabdarth", "samanarthi", "vilom",
            "vyakaran", "2d_tool"}

def obj_copy(o):
    return collections.OrderedDict([
        ("objective_id", o["objective_id"]), ("legacy_id", o["legacy_id"]),
        ("strand", o["strand"]), ("strand_name", o["strand_name"]),
        ("objective_text", o["objective_text"]), ("bloom_level", o["bloom_level"]),
        ("home_topic_id", tr(o["home_topic_id"])), ("anchor", trlist(o.get("anchor"))),
        ("status", o.get("status")), ("theme_category", o.get("theme_category")),
        ("image_examples", o.get("image_examples", [])),
    ])

def build_topic(t):
    out = collections.OrderedDict()
    for k in TOPIC_KEYS:
        if k not in t:
            if k in OPTIONAL:
                continue
            raise KeyError("topic %s missing %s" % (t["topic_id"], k))
        v = t[k]
        if k == "topic_id":
            v = tr(v)
        elif k == "topic_type":
            if v not in TOPIC_TYPE:
                raise ValueError("unmapped topic_type %r" % v)
            v = TOPIC_TYPE[v]
        elif k in ("depends_on", "source_topic_ids"):
            v = trlist(v)
        elif k == "learning_objectives":
            v = [obj_copy(o) for o in v]
        elif k == "concepts":
            v = [collections.OrderedDict([
                    ("concept_id", tr(c["concept_id"])),
                    ("concept_name", c["concept_name"]),
                    ("objective_id", c["objective_id"]),
                    ("key_terms", c.get("key_terms", [])),
                    ("content", c["content"]),
                 ]) for c in v]
        elif k == "recall_questions":
            v = [collections.OrderedDict(
                    [("id", tr(q["id"]))] +
                    ([("legacy_id", tr(q["legacy_id"]))] if "legacy_id" in q else []) +
                    [(kk, vv) for kk, vv in q.items() if kk not in ("id", "legacy_id")]
                 ) for q in v]
        elif k == "media":
            nv = []
            for md in v:
                mo = collections.OrderedDict()
                for kk, vv in md.items():
                    if kk in ("id", "concept_id", "home_concept_id") and vv:
                        vv = tr(vv)
                    mo[kk] = vv
                nv.append(mo)
            v = nv
        out[k] = v
    return out

def build_segment(s):
    out = collections.OrderedDict()
    out["segment_id"] = tr(s["segment_id"])
    out["segment_name"] = s["segment_name"]
    for k in ("brief_summary", "summary", "detailed_summary"):
        if k in s:
            out[k] = s[k]
    if "recall_questions" in s:
        out["recall_questions"] = [collections.OrderedDict(
            [("id", tr(q["id"]))] +
            [(kk, vv) for kk, vv in q.items() if kk != "id"]) for q in s["recall_questions"]]
    out["topics"] = [build_topic(t) for t in s["topics"]]
    return out

def build_module(m):
    out = collections.OrderedDict()
    out["module_id"] = tr(m["module_id"])
    out["module_name"] = m["module_name"]
    for k in ("difficult_words", "overall_rhyme_scheme"):
        if k in m:
            out[k] = m[k]
    for k in ("brief_summary", "summary", "detailed_summary"):
        if k in m:
            out[k] = m[k]
    out["segments"] = [build_segment(s) for s in m["segments"]]
    return out

# ---------------------------------------------------------------- 4/5/6. emit
row = cmm.get(merged["chapter_id"], {})
plan = collections.OrderedDict([
    ("phase", 2),
    ("board", merged["board"]),
    ("subject", merged["subject"]),
    ("grade", merged["grade"]),
    ("level", merged["level"]),
    ("version", merged["version"]),
    ("ordering", "logical"),
    ("author", merged["author"]),
    ("chapter_id", merged["chapter_id"]),
    ("plan_id", "%s_v%s" % (merged["chapter_id"], merged["version"])),
    ("chapter_name", merged["chapter_name"]),
    ("unit_title", merged["unit_title"]),
    ("unit_number", merged["unit_number"]),
    ("topic_title", merged["topic_title"]),
    ("topic_number", merged["topic_number"]),
    ("genre", merged["genre"]),
    ("teaching_lens", merged["teaching_lens"]),
    ("guiding_question", merged["guiding_question"]),
    ("textbook", merged["textbook"]),
    ("textbook_url", merged["textbook_url"]),
    ("textbook_pages", merged["textbook_pages"]),
    ("_activate", False),
    ("medium_id", None),
    ("subject_ref_id", None),
    ("publication_id", row.get("publication_id")),
    ("chapter_master_id", row.get("chapter_master_id")),
    ("estimated_time", merged["estimated_time"]),
    ("english_plan_id", None),
    ("english_chapter_id", None),
    ("objectives", [obj_copy(o) for o in merged["objectives"]]),
    ("strand_to_objective_map", merged["strand_to_objective_map"]),
    ("modules", [build_module(m) for m in modules]),
])
# root objectives carry no image_examples (that key belongs to the inline mirror only)
for o in plan["objectives"]:
    o.pop("image_examples", None)

json.dump(plan, open(D + "learning_plan_logical.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
open(D + "learning_plan_logical.json", "a", encoding="utf-8").write("\n")

# ---------------------------------------------------------------- covered_by_topics
ex = json.load(open(D + "10_exercise_solutions.json", encoding="utf-8"))
changed = 0
for e in ex["exercises"]:
    new = trlist(e.get("covered_by_topics"))
    if new != (e.get("covered_by_topics") or []):
        changed += 1
    e["covered_by_topics"] = new
if changed:
    json.dump(ex, open(D + "10_exercise_solutions.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    open(D + "10_exercise_solutions.json", "a", encoding="utf-8").write("\n")

print("idmap identity:", all(k == v for k, v in idmap.items()))
print("nodes renumbered:", len(idmap))
print("covered_by_topics rows rewritten:", changed)
