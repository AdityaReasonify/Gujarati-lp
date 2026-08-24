#!/usr/bin/env python3
# Agent 14 — logical plan emitter for std 7 / ch02 (ત્રણ સવાલ)
import json, re, sys, collections
from pathlib import Path

OUT = Path("/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output7/ch02")
merged = json.loads((OUT / "13_merged.json").read_text(encoding="utf-8"))
ex_doc = json.loads((OUT / "10_exercise_solutions.json").read_text(encoding="utf-8"))
tb_order = json.loads((OUT / "05b_textbook_order.json").read_text(encoding="utf-8"))["textbook_order"]

# ---------- 1. arrange: reading order = the merged structure's own traversal ----------
modules = merged["modules"]  # already in reading order (Agent 5 cut, Agent 13 merged)
traversal = [t["topic_id"] for m in modules for s in m["segments"] for t in s["topics"]]
assert traversal == tb_order, ("reading order disagrees with 05b_textbook_order", traversal, tb_order)

# ---------- 2. renumber consecutively along the traversal ----------
idmap = {}          # old id -> new id, every level
m_i = s_i = t_i = c_i = 0
for mod in modules:
    m_i += 1
    new_m = f"M{m_i}"
    idmap[mod["module_id"]] = new_m
    for seg in mod["segments"]:
        s_i += 1
        new_s = f"{new_m}.S{s_i}"
        idmap[seg["segment_id"]] = new_s
        for top in seg["topics"]:
            t_i += 1
            new_t = f"{new_s}.T{t_i}"
            idmap[top["topic_id"]] = new_t
            for con in top["concepts"]:
                c_i += 1
                idmap[con["concept_id"]] = f"{new_t}.C{c_i}"

IDENTITY = all(k == v for k, v in idmap.items())

CONCEPT_RE = re.compile(r"^M\d+\.S\d+\.T\d+\.C\d+$")
TOPIC_RE = re.compile(r"^M\d+\.S\d+\.T\d+$")


def newid(old):
    if old not in idmap:
        raise KeyError(f"stale reference: {old!r} resolves to no node")
    return idmap[old]


def remap_media_id(old_media_id, concept_old):
    """{concept_id}.{TYPE}{n} -> new concept id + same suffix."""
    mm = re.match(r"^(M\d+\.S\d+\.T\d+\.C\d+)\.(IMG|VID|2D|3D|SIM)(\d+)$", old_media_id)
    if not mm:
        raise ValueError(f"media id does not match MEDIA_ID_RE: {old_media_id!r}")
    assert mm.group(1) == concept_old, (old_media_id, concept_old)
    return f"{newid(mm.group(1))}.{mm.group(2)}{mm.group(3)}"


def remap_recall_id(old, owner_old, suffix):
    """{owner_id}.RQ{n} / .TR{n}"""
    mm = re.match(r"^(M\d+(?:\.S\d+)?(?:\.T\d+)?)\.(RQ|TR)(\d+)$", old)
    if not mm:
        raise ValueError(f"recall id malformed: {old!r}")
    assert mm.group(1) == owner_old, (old, owner_old)
    assert mm.group(2) == suffix, (old, suffix)
    return f"{newid(mm.group(1))}.{suffix}{mm.group(3)}"


# ---------- 3/5. whitelists and key order (mirrors output7/ch01 house order) ----------
ROOT_ORDER = ["phase", "board", "subject", "grade", "level", "version", "ordering",
              "chapter_id", "plan_id", "author", "_activate", "medium_id", "subject_ref_id",
              "chapter_master_id", "publication_id", "english_plan_id", "english_chapter_id",
              "estimated_time", "textbook", "textbook_url", "textbook_pages", "unit_title",
              "unit_number", "topic_title", "topic_number", "chapter_name", "genre",
              "teaching_lens", "guiding_question", "objectives", "strand_to_objective_map",
              "modules"]
MODULE_ORDER = ["module_id", "module_name", "difficult_words", "overall_rhyme_scheme", "segments"]
SEGMENT_ORDER = ["segment_id", "segment_name", "topics"]
TOPIC_ORDER = ["topic_id", "topic_name", "topic_type", "topic_category", "difficulty",
               "depends_on", "source_topic_ids", "objective_ids", "learning_objectives",
               "original_chunk", "modified_chunk", "publication_chunk", "word_count",
               "key_terms", "explanation", "real_life_example", "publication_text",
               "brief_summary", "summary", "detailed_summary", "concept_bullets",
               "important_points", "concepts", "recall_questions", "media", "2d_tool",
               "estimated_exchanges", "figures_of_speech", "rhyme_scheme",
               "shabdarth", "samanarthi", "vilom", "vyakaran",
               "primary_content_type", "secondary_content_type", "tertiary_content_type",
               "available_content_types"]
OBJECTIVE_ORDER = ["objective_id", "legacy_id", "strand", "strand_name", "objective_text",
                   "bloom_level", "home_topic_id", "anchor", "status", "theme_category"]
LO_ORDER = OBJECTIVE_ORDER + ["image_examples"]
CONCEPT_ORDER = ["concept_id", "concept_name", "objective_id", "key_terms", "content"]
MEDIA_ORDER = ["id", "type", "subtype", "title", "description", "image_url", "aspect_ratio",
               "concept_id", "home_concept_id", "objective_id", "image_category",
               "teaching_notes", "negative_prompt", "generation_prompt"]
RQ_ORDER = ["id", "legacy_id", "prompt", "answer", "difficulty", "bloom_level"]

dropped = collections.Counter()


def pick(src, order, label):
    for k in src:
        if k not in order:
            dropped[f"{label}.{k}"] += 1
    return {k: src[k] for k in order if k in src}


TOPIC_TYPE_MAP = {"POEM": "instructional", "STORY_TELLING": "instructional",
                  "CONCEPT": "instructional", "REVIEW": "summary", "EXERCISE": "assessment",
                  # already-mapped values pass through unchanged
                  "instructional": "instructional", "summary": "summary",
                  "assessment": "assessment"}

# ---------- root objectives registry (O{n} NOT renumbered) ----------
objectives_out = []
for o in merged["objectives"]:
    o2 = pick(o, OBJECTIVE_ORDER, "objective")
    o2["home_topic_id"] = newid(o["home_topic_id"])
    o2["anchor"] = [newid(a) for a in o["anchor"]]
    objectives_out.append(o2)
obj_text = {o["objective_id"]: o["objective_text"] for o in objectives_out}

# ---------- walk and emit ----------
modules_out = []
for mod in modules:
    mod_old = mod["module_id"]
    m2 = pick(mod, MODULE_ORDER, "module")
    m2["module_id"] = newid(mod_old)
    segs_out = []
    for seg in mod["segments"]:
        seg_old = seg["segment_id"]
        s2 = pick(seg, SEGMENT_ORDER, "segment")
        s2["segment_id"] = newid(seg_old)
        # segment-level recalls (none in this chapter) -> {segment_id}.RQ{n}, never .SR{n}
        if "recall_questions" in seg:
            s2["recall_questions"] = [
                dict(pick(r, RQ_ORDER, "segment.recall"),
                     id=remap_recall_id(r["id"], seg_old, "RQ"))
                for r in seg["recall_questions"]]
        tops_out = []
        for top in seg["topics"]:
            top_old = top["topic_id"]
            t2 = pick(top, TOPIC_ORDER, "topic")
            t2["topic_id"] = newid(top_old)
            t2["topic_type"] = TOPIC_TYPE_MAP[top["topic_type"]]
            t2["depends_on"] = [newid(d) for d in top.get("depends_on", [])]
            t2["source_topic_ids"] = [newid(d) for d in top.get("source_topic_ids", [])]
            for oid in top["objective_ids"]:
                if oid not in obj_text:
                    raise KeyError(f"{top_old}: objective_ids -> unknown {oid}")
            los = []
            for lo in top["learning_objectives"]:
                lo2 = pick(lo, LO_ORDER, "learning_objective")
                lo2["home_topic_id"] = newid(lo["home_topic_id"])
                lo2["anchor"] = [newid(a) for a in lo["anchor"]]
                if lo2["objective_text"] != obj_text[lo2["objective_id"]]:
                    raise ValueError(f"{top_old}: inline objective_text drifted from registry")
                los.append(lo2)
            t2["learning_objectives"] = los
            cons = []
            for con in top["concepts"]:
                c2 = pick(con, CONCEPT_ORDER, "concept")
                c2["concept_id"] = newid(con["concept_id"])
                if c2["objective_id"] not in obj_text:
                    raise KeyError(f"{con['concept_id']}: unknown objective_id")
                cons.append(c2)
            t2["concepts"] = cons
            t2["recall_questions"] = [
                dict(pick(r, RQ_ORDER, "topic.recall"),
                     id=remap_recall_id(r["id"], top_old, "RQ"),
                     legacy_id=remap_recall_id(r["legacy_id"], top_old, "TR"))
                for r in top["recall_questions"]]
            med = []
            for md in top.get("media", []):
                m3 = pick(md, MEDIA_ORDER, "media")
                m3["id"] = remap_media_id(md["id"], md["concept_id"])
                m3["concept_id"] = newid(md["concept_id"])
                m3["home_concept_id"] = newid(md["home_concept_id"])
                med.append(m3)
            t2["media"] = med
            tops_out.append({k: t2[k] for k in TOPIC_ORDER if k in t2})
        s2["topics"] = tops_out
        segs_out.append({k: s2[k] for k in SEGMENT_ORDER + ["recall_questions"] if k in s2})
    m2["segments"] = segs_out
    modules_out.append({k: m2[k] for k in MODULE_ORDER if k in m2})

# ---------- 6. root fields ----------
GRADE = merged["grade"]
UNIT = merged["unit_number"]
chapter_id = f"gseb_eng_gujarati{GRADE}_ch{UNIT}"
version = merged["version"]
assert chapter_id == merged["chapter_id"], (chapter_id, merged["chapter_id"])

cm_map = json.loads(Path("/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/upload_reference/"
                         "chapter_master_map.json").read_text(encoding="utf-8"))
row = cm_map[chapter_id]

plan = {k: merged[k] for k in ROOT_ORDER if k in merged}
plan["ordering"] = "logical"
plan["phase"] = 2
plan["version"] = version
plan["chapter_id"] = chapter_id
plan["plan_id"] = f"{chapter_id}_v{version}"
plan["_activate"] = False
plan["subject_ref_id"] = None          # server-injected
plan["medium_id"] = None               # server-injected
plan["english_plan_id"] = None         # no English twin
plan["english_chapter_id"] = None
plan["chapter_master_id"] = row["chapter_master_id"]      # null in the map — never invented
plan["publication_id"] = (row["publication_id"] if row["publication_id"] is not None
                          else merged["publication_id"])  # A13's provisional placeholder
plan["objectives"] = objectives_out
plan["strand_to_objective_map"] = merged["strand_to_objective_map"]
plan["modules"] = modules_out
plan = {k: plan[k] for k in ROOT_ORDER}
assert len(plan) == 32, len(plan)

# ---------- covered_by_topics rewrite ----------
ex_changed = False
for e in ex_doc["exercises"]:
    new = [newid(x) for x in e["covered_by_topics"]]
    if new != e["covered_by_topics"]:
        e["covered_by_topics"] = new
        ex_changed = True

# ---------- assert: every reference resolves ----------
live_modules = {m["module_id"] for m in modules_out}
live_segments = {s["segment_id"] for m in modules_out for s in m["segments"]}
live_topics = {t["topic_id"] for m in modules_out for s in m["segments"] for t in s["topics"]}
live_concepts = {c["concept_id"] for m in modules_out for s in m["segments"]
                 for t in s["topics"] for c in t["concepts"]}
live_obj = {o["objective_id"] for o in plan["objectives"]}
errs = []

# traversal position == id (the LP2 validator's own check)
mi = si = ti = ci = 0
for m in modules_out:
    mi += 1
    if m["module_id"] != f"M{mi}":
        errs.append(f"module position: expected M{mi}, got {m['module_id']}")
    for s in m["segments"]:
        si += 1
        if s["segment_id"] != f"M{mi}.S{si}":
            errs.append(f"segment position: expected M{mi}.S{si}, got {s['segment_id']}")
        for r in s.get("recall_questions", []):
            if not re.match(rf"^{re.escape(s['segment_id'])}\.RQ\d+$", r["id"]):
                errs.append(f"segment recall id: {r['id']}")
        for t in s["topics"]:
            ti += 1
            tid = f"M{mi}.S{si}.T{ti}"
            if t["topic_id"] != tid:
                errs.append(f"topic position: expected {tid}, got {t['topic_id']}")
            if t["topic_type"] not in ("instructional", "summary", "assessment"):
                errs.append(f"{tid}: topic_type {t['topic_type']}")
            for d in t["depends_on"] + t["source_topic_ids"]:
                if d not in live_topics:
                    errs.append(f"{tid}: stale depends_on/source {d}")
            for oid in t["objective_ids"]:
                if oid not in live_obj:
                    errs.append(f"{tid}: objective_ids -> {oid}")
            for lo in t["learning_objectives"]:
                if lo["home_topic_id"] not in live_topics:
                    errs.append(f"{tid}: lo home_topic_id {lo['home_topic_id']}")
                for a in lo["anchor"]:
                    if a not in live_concepts:
                        errs.append(f"{tid}: lo anchor {a}")
            for r in t["recall_questions"]:
                if not re.match(rf"^{re.escape(tid)}\.RQ\d+$", r["id"]):
                    errs.append(f"{tid}: recall id {r['id']}")
                if not re.match(rf"^{re.escape(tid)}\.TR\d+$", r["legacy_id"]):
                    errs.append(f"{tid}: recall legacy_id {r['legacy_id']}")
            for c in t["concepts"]:
                ci += 1
                cid = f"{tid}.C{ci}"
                if c["concept_id"] != cid:
                    errs.append(f"concept position: expected {cid}, got {c['concept_id']}")
                if c["objective_id"] not in live_obj:
                    errs.append(f"{cid}: objective_id {c['objective_id']}")
                if not c.get("content"):
                    errs.append(f"{cid}: empty content")
            for md in t["media"]:
                mm = re.match(r"^(M\d+\.S\d+\.T\d+\.C\d+)\.(IMG|VID|2D|3D|SIM)\d+$", md["id"])
                if not mm:
                    errs.append(f"{tid}: media id {md['id']}")
                elif mm.group(1) not in live_concepts:
                    errs.append(f"{tid}: media id scope {md['id']}")
                for k in ("concept_id", "home_concept_id"):
                    if md[k] not in live_concepts:
                        errs.append(f"{tid}: media {k} {md[k]}")

for o in plan["objectives"]:
    if o["home_topic_id"] not in live_topics:
        errs.append(f"{o['objective_id']}: home_topic_id {o['home_topic_id']}")
    for a in o["anchor"]:
        if a not in live_concepts:
            errs.append(f"{o['objective_id']}: anchor {a}")
for lid, oid in plan["strand_to_objective_map"].items():
    if oid not in live_obj:
        errs.append(f"strand_to_objective_map {lid} -> {oid}")
for o in plan["objectives"]:
    if o["legacy_id"] not in plan["strand_to_objective_map"]:
        errs.append(f"{o['objective_id']}: legacy_id {o['legacy_id']} absent from strand map")
for e in ex_doc["exercises"]:
    for x in e["covered_by_topics"]:
        if x not in live_topics:
            errs.append(f"{e['exercise_id']}: covered_by_topics {x}")

# Gujarati-script original_chunk on every topic
GUJ = re.compile(r"[઀-૿]")
DEV = re.compile(r"[ऀ-ॿ]")
for m in modules_out:
    for s in m["segments"]:
        for t in s["topics"]:
            if not t.get("original_chunk") or not GUJ.search(t["original_chunk"]):
                errs.append(f"{t['topic_id']}: original_chunk not Gujarati")
            if DEV.search(t["original_chunk"]):
                errs.append(f"{t['topic_id']}: Devanagari in original_chunk")

if errs:
    print("HARD FAIL:", file=sys.stderr)
    for e in errs:
        print("  -", e, file=sys.stderr)
    sys.exit(1)

(OUT / "learning_plan_logical.json").write_text(
    json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

if ex_changed:
    (OUT / "10_exercise_solutions.json").write_text(
        json.dumps(ex_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print("identity renumber:", IDENTITY)
print("covered_by_topics rewritten:", ex_changed)
print("dropped working keys:", dict(dropped) or "none")
print("modules/segments/topics/concepts:", mi, si, ti, ci)
print("publication_id:", plan["publication_id"], "chapter_master_id:", plan["chapter_master_id"])
print("segments without three-tier summaries:",
      [s["segment_id"] for m in modules_out for s in m["segments"] if "summary" not in s])
print("modules without three-tier summaries:",
      [m["module_id"] for m in modules_out if "summary" not in m])
