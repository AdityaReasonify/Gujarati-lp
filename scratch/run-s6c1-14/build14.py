# -*- coding: utf-8 -*-
"""Agent 14 — arrange in reading order, renumber M/S/T/C consecutively, translate every
reference, apply the phase-2 whitelist, emit learning_plan_logical.json.

Shape authority: reference/phase2_contract.md + lib/assemble.py (the pack's own emitter).
"""
import json, os, re, sys

OUT = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch01"
merged = json.load(open(os.path.join(OUT, "13_merged.json"), encoding="utf-8"))
ex = json.load(open(os.path.join(OUT, "10_exercise_solutions.json"), encoding="utf-8"))
order = json.load(open(os.path.join(OUT, "05b_textbook_order.json"), encoding="utf-8"))

# ---------------------------------------------------------------- 1. arrange
# Reading sequence = the merged structure's own scene order (ટેક + પહેલી કડી → બીજી કડી →
# ત્રીજી કડી), confirmed against the rendered printed page (05b_textbook_order.json).
reading = []
for m in merged["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            reading.append(t["topic_id"])
assert reading == order["textbook_order"], (reading, order["textbook_order"])

# ---------------------------------------------------------------- 2. renumber
# Walk the arranged tree; m/s/t/c are chapter-continuous and never restart.
idmap = {}          # old id -> new id (modules, segments, topics, concepts)
mi = si = ti = ci = 0
for m in merged["modules"]:
    mi += 1
    new_m = "M%d" % mi
    idmap[m["module_id"]] = new_m
    for s in m["segments"]:
        si += 1
        new_s = "%s.S%d" % (new_m, si)
        idmap[s["segment_id"]] = new_s
        for t in s["topics"]:
            ti += 1
            new_t = "%s.T%d" % (new_s, ti)
            idmap[t["topic_id"]] = new_t
            for c in t["concepts"]:
                ci += 1
                idmap[c["concept_id"]] = "%s.C%d" % (new_t, ci)

def tr(old):
    if old not in idmap:
        raise SystemExit("STALE REFERENCE: %r resolves to no node" % (old,))
    return idmap[old]

# ---------------------------------------------------------------- 3. emit
TOPIC_TYPE = {"POEM": "instructional", "CONCEPT": "instructional",
              "STORY_TELLING": "instructional", "REVIEW": "summary",
              "EXERCISE": "assessment"}

OBJ_INLINE = ("objective_id", "legacy_id", "strand", "strand_name", "objective_text",
              "bloom_level", "home_topic_id", "anchor", "theme_category")

registry = {o["objective_id"]: o for o in merged["objectives"]}

objectives = []
for o in merged["objectives"]:
    n = dict(o)
    n["home_topic_id"] = tr(o["home_topic_id"])
    n["anchor"] = [tr(a) for a in o["anchor"]]
    objectives.append(n)
registry_new = {o["objective_id"]: o for o in objectives}

TOPIC_KEYS = ["topic_id", "topic_name", "topic_type", "topic_category", "difficulty",
              "original_chunk", "modified_chunk", "word_count", "explanation",
              "real_life_example", "brief_summary", "summary", "detailed_summary",
              "key_terms", "concept_bullets", "important_points",
              "figures_of_speech", "rhyme_scheme",
              "shabdarth", "samanarthi", "vilom", "vyakaran",
              "objective_ids", "learning_objectives", "concepts", "recall_questions",
              "media", "2d_tool", "publication_text", "publication_chunk",
              "depends_on", "source_topic_ids", "estimated_exchanges",
              "primary_content_type", "secondary_content_type", "tertiary_content_type",
              "available_content_types"]

MEDIA_KEYS = ["id", "type", "subtype", "title", "description", "image_url", "aspect_ratio",
              "concept_id", "home_concept_id", "objective_id", "image_category",
              "teaching_notes", "negative_prompt", "generation_prompt"]


def build_topic(t):
    nt = tr(t["topic_id"])
    out = {}
    for k in TOPIC_KEYS:
        out[k] = t.get(k)

    out["topic_id"] = nt
    out["topic_type"] = TOPIC_TYPE[t["topic_type"]]
    out["depends_on"] = [tr(x) for x in t.get("depends_on") or []]
    out["source_topic_ids"] = [tr(x) for x in t.get("source_topic_ids") or []]

    # objectives: ids are NOT renumbered; the inline mirror is the registry entry verbatim
    # plus image_examples (lib/assemble.py) — `status` lives in the registry only.
    out["objective_ids"] = list(t["objective_ids"])
    inline = []
    for lo in t["learning_objectives"]:
        reg = registry_new[lo["objective_id"]]
        assert lo["objective_text"] == reg["objective_text"], lo["objective_id"]
        o = {k: reg[k] for k in OBJ_INLINE}
        o["image_examples"] = lo.get("image_examples", [])
        inline.append(o)
    out["learning_objectives"] = inline

    out["concepts"] = [{"concept_id": tr(c["concept_id"]),
                        "concept_name": c["concept_name"],
                        "objective_id": c["objective_id"],
                        "key_terms": c.get("key_terms", []),
                        "content": c["content"]} for c in t["concepts"]]

    rqs = []
    for i, r in enumerate(t.get("recall_questions") or [], 1):
        rqs.append({"id": "%s.RQ%d" % (nt, i), "legacy_id": "%s.TR%d" % (nt, i),
                    "prompt": r["prompt"], "answer": r["answer"],
                    "difficulty": r["difficulty"], "bloom_level": r["bloom_level"]})
    out["recall_questions"] = rqs

    media = []
    for mm in t.get("media") or []:
        n = {k: mm.get(k) for k in MEDIA_KEYS}
        cid = tr(mm["concept_id"])
        suffix = re.match(r"^M\d+\.S\d+\.T\d+\.C\d+\.((?:IMG|VID|2D|3D|SIM)\d+)$",
                          mm["id"]).group(1)
        n["id"] = "%s.%s" % (cid, suffix)
        n["concept_id"] = cid
        n["home_concept_id"] = tr(mm["home_concept_id"])
        media.append(n)
    out["media"] = media
    return out


modules = []
for m in merged["modules"]:
    segs = []
    for s in m["segments"]:
        seg = {"segment_id": tr(s["segment_id"]), "segment_name": s["segment_name"]}
        for k in ("brief_summary", "summary", "detailed_summary", "important_points"):
            if k in s:
                seg[k] = s[k]
        if s.get("recall_questions"):
            seg["recall_questions"] = [
                {"id": "%s.RQ%d" % (seg["segment_id"], i), "prompt": r["prompt"],
                 "answer": r["answer"], "difficulty": r["difficulty"],
                 "bloom_level": r["bloom_level"]}
                for i, r in enumerate(s["recall_questions"], 1)]
        seg["topics"] = [build_topic(t) for t in s["topics"]]
        segs.append(seg)
    mod = {"module_id": tr(m["module_id"]), "module_name": m["module_name"]}
    for k in ("brief_summary", "summary", "detailed_summary", "important_points",
              "difficult_words", "overall_rhyme_scheme"):
        if k in m:
            mod[k] = m[k]
    mod["segments"] = segs
    modules.append(mod)

ROOT_KEYS = ["phase", "board", "subject", "grade", "level", "version", "ordering",
             "author", "chapter_id", "plan_id", "chapter_name", "unit_title",
             "unit_number", "topic_title", "topic_number", "genre", "teaching_lens",
             "guiding_question", "textbook", "textbook_url", "textbook_pages",
             "_activate", "medium_id", "subject_ref_id", "publication_id",
             "chapter_master_id", "estimated_time", "english_plan_id",
             "english_chapter_id", "objectives", "strand_to_objective_map", "modules"]

plan = {}
for k in ROOT_KEYS:
    if k == "ordering":
        plan[k] = "logical"
    elif k == "objectives":
        plan[k] = objectives
    elif k == "modules":
        plan[k] = modules
    else:
        plan[k] = merged[k]

plan["phase"] = 2
plan["chapter_id"] = "gseb_eng_gujarati%d_ch%d" % (plan["grade"], plan["unit_number"])
plan["plan_id"] = "%s_v%d" % (plan["chapter_id"], plan["version"])
plan["english_plan_id"] = None
plan["english_chapter_id"] = None
plan["subject_ref_id"] = None
plan["medium_id"] = None
plan["_activate"] = False

assert len(plan) == 32, len(plan)

# ---------------------------------------------------------------- 4. assert
nodes, concepts_all, topics_all = set(), set(), set()
for m in plan["modules"]:
    nodes.add(m["module_id"])
    for s in m["segments"]:
        nodes.add(s["segment_id"])
        for r in s.get("recall_questions") or []:
            assert r["id"].startswith(s["segment_id"] + ".RQ"), r["id"]
        for t in s["topics"]:
            nodes.add(t["topic_id"]); topics_all.add(t["topic_id"])
            for c in t["concepts"]:
                nodes.add(c["concept_id"]); concepts_all.add(c["concept_id"])

err = []
def need(i, where, pool=nodes):
    if i not in pool:
        err.append("%s -> %s" % (where, i))

for o in plan["objectives"]:
    need(o["home_topic_id"], "objectives[%s].home_topic_id" % o["objective_id"], topics_all)
    for a in o["anchor"]:
        need(a, "objectives[%s].anchor" % o["objective_id"], concepts_all)
oids = {o["objective_id"] for o in plan["objectives"]}
assert set(plan["strand_to_objective_map"].values()) == oids
assert {o["legacy_id"] for o in plan["objectives"]} == set(plan["strand_to_objective_map"])

seen_t, seen_s, seen_m, seen_c = [], [], [], []
for m in plan["modules"]:
    seen_m.append(m["module_id"])
    for s in m["segments"]:
        seen_s.append(s["segment_id"])
        for t in s["topics"]:
            seen_t.append(t["topic_id"])
            assert t["topic_type"] in ("instructional", "summary", "assessment")
            for d in t["depends_on"]:
                need(d, "%s.depends_on" % t["topic_id"], topics_all)
            for d in t["source_topic_ids"]:
                need(d, "%s.source_topic_ids" % t["topic_id"], topics_all)
            for o in t["objective_ids"]:
                if o not in oids:
                    err.append("%s.objective_ids -> %s" % (t["topic_id"], o))
            for lo in t["learning_objectives"]:
                need(lo["home_topic_id"], "%s inline home_topic_id" % t["topic_id"], topics_all)
                for a in lo["anchor"]:
                    need(a, "%s inline anchor" % t["topic_id"], concepts_all)
                assert lo["objective_text"] == registry_new[lo["objective_id"]]["objective_text"]
                assert "status" not in lo
            for c in t["concepts"]:
                seen_c.append(c["concept_id"])
                assert c["concept_id"].startswith(t["topic_id"] + ".C"), c["concept_id"]
                if c["objective_id"] not in oids:
                    err.append("%s.objective_id -> %s" % (c["concept_id"], c["objective_id"]))
            for i, r in enumerate(t["recall_questions"], 1):
                assert r["id"] == "%s.RQ%d" % (t["topic_id"], i)
                assert r["legacy_id"] == "%s.TR%d" % (t["topic_id"], i)
            for mm in t["media"]:
                need(mm["concept_id"], "%s media concept_id" % mm["id"], concepts_all)
                need(mm["home_concept_id"], "%s media home_concept_id" % mm["id"], concepts_all)
                assert re.match(r"^M\d+\.S\d+\.T\d+\.C\d+\.(IMG|VID|2D|3D|SIM)\d+$", mm["id"])
                assert mm["id"].startswith(mm["concept_id"] + ".")

assert seen_m == ["M%d" % i for i in range(1, len(seen_m) + 1)], seen_m
assert [x.split(".")[1] for x in seen_s] == ["S%d" % i for i in range(1, len(seen_s) + 1)], seen_s
assert [x.split(".")[2] for x in seen_t] == ["T%d" % i for i in range(1, len(seen_t) + 1)], seen_t
assert [x.split(".")[3] for x in seen_c] == ["C%d" % i for i in range(1, len(seen_c) + 1)], seen_c

# covered_by_topics in the exercise deliverable must survive the renumber
bad = [c for e in ex["exercises"] for c in (e.get("covered_by_topics") or [])
       if idmap.get(c) not in topics_all]
if bad:
    err.append("covered_by_topics stale: %s" % sorted(set(bad)))
identity = all(idmap[k] == k for k in idmap)

if err:
    raise SystemExit("HARD FAIL — stale references:\n  " + "\n  ".join(err))

json.dump(plan, open(os.path.join(OUT, "learning_plan_logical.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

print("modules %d  segments %d  topics %d  concepts %d  objectives %d"
      % (len(seen_m), len(seen_s), len(seen_t), len(seen_c), len(plan["objectives"])))
print("id map is identity:", identity)
print("root keys:", len(plan))
print("covered_by_topics rewrite needed in 10_exercise_solutions.json:", not identity)
