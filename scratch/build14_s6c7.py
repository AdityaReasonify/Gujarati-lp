#!/usr/bin/env python3
# Agent 14 — logical plan for std6 / ch07.
# Arrange in reading order, renumber M/S/T/C consecutively (chapter-continuous),
# translate every reference, whitelist keys, map topic_type, emit root fields.
import json, re, sys, copy, pathlib

OUT = pathlib.Path("/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch07")
merged = json.loads((OUT / "13_merged.json").read_text())

# ---------- 1. Arrange (reading order = merged traversal; cross-checked vs 05b) ----------
tb = json.loads((OUT / "05b_textbook_order.json").read_text())

traversal_topics = []
for m in merged["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            traversal_topics.append(t["topic_id"])

# ---------- 2. Renumber consecutively, chapter-continuous m/s/t/c ----------
idmap = {}          # old node id -> new node id  (modules, segments, topics, concepts)
mi = si = ti = ci = 0
new_modules = []
for m in merged["modules"]:
    mi += 1
    new_mid = f"M{mi}"
    idmap[m["module_id"]] = new_mid
    nm = copy.deepcopy(m)
    nm["module_id"] = new_mid
    for s in nm["segments"]:
        si += 1
        new_sid = f"{new_mid}.S{si}"
        idmap[s["segment_id"]] = new_sid
        s["segment_id"] = new_sid
        for t in s["topics"]:
            ti += 1
            new_tid = f"{new_sid}.T{ti}"
            idmap[t["topic_id"]] = new_tid
            for c in t["concepts"]:
                ci += 1
                idmap[c["concept_id"]] = f"{new_tid}.C{ci}"
            t["topic_id"] = new_tid
    new_modules.append(nm)

def remap(old):
    """Translate a node id, or an id that hangs off a node id (recall / media)."""
    if old in idmap:
        return idmap[old]
    m = re.match(r"^(M\d+\.S\d+\.T\d+(?:\.C\d+)?)\.((?:RQ|TR|IMG|VID|2D|3D|SIM)\d+)$", old)
    if m and m.group(1) in idmap:
        return f"{idmap[m.group(1)]}.{m.group(2)}"
    raise SystemExit(f"UNRESOLVED ID: {old!r}")

def remap_list(lst):
    return [remap(x) for x in lst]

# ---------- 3. Translate every reference ----------
TOPIC_TYPE_MAP = {
    "POEM": "instructional", "STORY_TELLING": "instructional", "CONCEPT": "instructional",
    "REVIEW": "summary", "EXERCISE": "assessment",
}

TOPIC_KEYS = [
    "topic_id", "topic_name", "topic_type", "topic_category", "difficulty",
    "depends_on", "source_topic_ids", "objective_ids", "learning_objectives",
    "original_chunk", "modified_chunk", "publication_chunk", "publication_text",
    "word_count", "key_terms", "explanation", "real_life_example",
    "brief_summary", "summary", "detailed_summary", "concept_bullets",
    "important_points", "recall_questions", "estimated_exchanges", "concepts",
    "media", "2d_tool",
    # કાવ્ય extras
    "figures_of_speech", "rhyme_scheme",
    # ભાષા-બોધ extras (romanized key names, as the server stores them)
    "shabdarth", "samanarthi", "vilom", "vyakaran",
    "primary_content_type", "secondary_content_type", "tertiary_content_type",
    "available_content_types",
]
MODULE_KEYS = ["module_id", "module_name", "difficult_words", "overall_rhyme_scheme", "segments"]
SEGMENT_KEYS = ["segment_id", "segment_name", "topics"]
OBJ_KEYS = ["objective_id", "legacy_id", "strand", "strand_name", "objective_text",
            "bloom_level", "home_topic_id", "anchor", "status", "theme_category"]
MEDIA_KEYS = ["id", "type", "subtype", "title", "description", "image_url", "aspect_ratio",
              "concept_id", "home_concept_id", "objective_id", "image_category",
              "teaching_notes", "negative_prompt", "generation_prompt"]

out_modules = []
for m in new_modules:
    out_segs = []
    for s in m["segments"]:
        out_topics = []
        for t in s["topics"]:
            t["depends_on"] = remap_list(t.get("depends_on") or [])
            t["source_topic_ids"] = remap_list(t.get("source_topic_ids") or [])
            for lo in t.get("learning_objectives") or []:
                lo["home_topic_id"] = remap(lo["home_topic_id"])
                lo["anchor"] = remap_list(lo.get("anchor") or [])
            for rq in t.get("recall_questions") or []:
                rq["id"] = remap(rq["id"])
                if rq.get("legacy_id"):
                    rq["legacy_id"] = remap(rq["legacy_id"])
            for c in t.get("concepts") or []:
                c["concept_id"] = remap(c["concept_id"])
            for md in t.get("media") or []:
                md["id"] = remap(md["id"])
                md["concept_id"] = remap(md["concept_id"])
                md["home_concept_id"] = remap(md["home_concept_id"])
                for k in MEDIA_KEYS:
                    md.setdefault(k, "" if k in ("negative_prompt", "generation_prompt",
                                                 "image_url", "teaching_notes") else None)
                for k in list(md.keys()):
                    if k not in MEDIA_KEYS:
                        del md[k]
            tool = t.get("2d_tool")
            if isinstance(tool, dict):
                for k in ("id", "concept_id", "home_concept_id"):
                    if tool.get(k):
                        tool[k] = remap(tool[k])
            # topic_type -> closed server enum
            t["topic_type"] = TOPIC_TYPE_MAP[t["topic_type"]]
            # whitelist
            out_topics.append({k: t[k] for k in TOPIC_KEYS if k in t})
        out_segs.append({**{k: s[k] for k in SEGMENT_KEYS if k in s and k != "topics"},
                         "topics": out_topics})
    out_modules.append({**{k: m[k] for k in MODULE_KEYS if k in m and k != "segments"},
                        "segments": out_segs})

objectives = []
for o in merged["objectives"]:
    o = dict(o)
    o["home_topic_id"] = remap(o["home_topic_id"])
    o["anchor"] = remap_list(o.get("anchor") or [])
    objectives.append({k: o[k] for k in OBJ_KEYS})

# ---------- 4/5/6. Root fields — 32 keys, ordering logical ----------
plan = {
    "phase": 2,
    "board": merged["board"],
    "subject": merged["subject"],
    "grade": merged["grade"],
    "level": merged["level"],
    "version": merged["version"],
    "ordering": "logical",
    "author": merged.get("author", ""),
    "chapter_id": merged["chapter_id"],
    "plan_id": merged["plan_id"],
    "chapter_name": merged["chapter_name"],
    "unit_title": merged["unit_title"],
    "unit_number": merged["unit_number"],
    "topic_title": merged["topic_title"],
    "topic_number": merged["topic_number"],
    "genre": merged["genre"],
    "teaching_lens": merged["teaching_lens"],
    "guiding_question": merged["guiding_question"],
    "textbook": merged["textbook"],
    "textbook_url": merged["textbook_url"],
    "textbook_pages": merged["textbook_pages"],
    "_activate": False,
    "medium_id": None,
    "subject_ref_id": None,
    "publication_id": merged.get("publication_id"),
    "chapter_master_id": merged.get("chapter_master_id"),
    "estimated_time": merged["estimated_time"],
    "english_plan_id": None,
    "english_chapter_id": None,
    "objectives": objectives,
    "strand_to_objective_map": merged["strand_to_objective_map"],
    "modules": out_modules,
}
assert len(plan) == 32, len(plan)
assert plan["plan_id"] == f'{plan["chapter_id"]}_v{plan["version"]}'

# ---------- assert: nothing points at a node that no longer exists ----------
node_ids, concept_ids, topic_ids = set(), set(), set()
errors = []
mi = si = ti = ci = 0
for m in plan["modules"]:
    mi += 1
    if m["module_id"] != f"M{mi}": errors.append(f"module {m['module_id']} != M{mi}")
    node_ids.add(m["module_id"])
    for s in m["segments"]:
        si += 1
        exp = f"M{mi}.S{si}"
        if s["segment_id"] != exp: errors.append(f"segment {s['segment_id']} != {exp}")
        node_ids.add(s["segment_id"])
        for t in s["topics"]:
            ti += 1
            expt = f"{exp}.T{ti}"
            if t["topic_id"] != expt: errors.append(f"topic {t['topic_id']} != {expt}")
            node_ids.add(t["topic_id"]); topic_ids.add(t["topic_id"])
            for c in t["concepts"]:
                ci += 1
                expc = f"{expt}.C{ci}"
                if c["concept_id"] != expc: errors.append(f"concept {c['concept_id']} != {expc}")
                concept_ids.add(c["concept_id"])

obj_ids = {o["objective_id"] for o in objectives}
for o in objectives:
    if o["home_topic_id"] not in topic_ids: errors.append(f"O anchor home {o['home_topic_id']}")
    for a in o["anchor"]:
        if a not in concept_ids: errors.append(f"O{o['objective_id']} stale anchor {a}")
for lg, oid in plan["strand_to_objective_map"].items():
    if oid not in obj_ids: errors.append(f"strand map {lg}->{oid}")
if {o["legacy_id"] for o in objectives} != set(plan["strand_to_objective_map"]):
    errors.append("strand_to_objective_map does not cover every legacy_id")

MEDIA_RE = re.compile(r"^(M\d+\.S\d+\.T\d+\.C\d+)\.(IMG|VID|2D|3D|SIM)\d+$")
for m in plan["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            tid = t["topic_id"]
            if t["topic_type"] not in ("instructional", "summary", "assessment"):
                errors.append(f"{tid} topic_type {t['topic_type']}")
            for d in t["depends_on"] + t["source_topic_ids"]:
                if d not in topic_ids: errors.append(f"{tid} stale dep {d}")
            for oid in t["objective_ids"]:
                if oid not in obj_ids: errors.append(f"{tid} stale objective {oid}")
            reg = {o["objective_id"]: o for o in objectives}
            for lo in t["learning_objectives"]:
                r = reg.get(lo["objective_id"])
                if not r: errors.append(f"{tid} inline lo {lo['objective_id']} not in registry"); continue
                if lo["objective_text"] != r["objective_text"]:
                    errors.append(f"{tid} inline objective_text drift {lo['objective_id']}")
                if lo["home_topic_id"] != r["home_topic_id"] or lo["anchor"] != r["anchor"]:
                    errors.append(f"{tid} inline anchor drift {lo['objective_id']}")
            for rq in t["recall_questions"]:
                if not re.match(rf"^{re.escape(tid)}\.RQ\d+$", rq["id"]):
                    errors.append(f"{tid} recall id {rq['id']}")
                if rq.get("legacy_id") and not re.match(rf"^{re.escape(tid)}\.TR\d+$", rq["legacy_id"]):
                    errors.append(f"{tid} recall legacy {rq['legacy_id']}")
            for c in t["concepts"]:
                if c["objective_id"] not in obj_ids: errors.append(f"{tid} concept obj {c['objective_id']}")
                if not c.get("content"): errors.append(f"{tid} concept {c['concept_id']} empty content")
            for md in t["media"]:
                mm = MEDIA_RE.match(md["id"])
                if not mm: errors.append(f"{tid} media id {md['id']}")
                elif mm.group(1) != md["concept_id"] or md["concept_id"] not in concept_ids:
                    errors.append(f"{tid} media concept {md['id']}")
                if md["home_concept_id"] not in concept_ids:
                    errors.append(f"{tid} media home_concept {md['home_concept_id']}")
                if not md["image_url"] and not md["generation_prompt"]:
                    errors.append(f"{tid} media {md['id']} has neither image_url nor generation_prompt")
            if not (t["original_chunk"] or "").strip():
                errors.append(f"{tid} empty original_chunk")
            if not re.search(r"[઀-૿]", t["original_chunk"]):
                errors.append(f"{tid} original_chunk not Gujarati script")
            for a, b in (("brief_summary", "summary"), ("summary", "detailed_summary")):
                if not len(t[a]) < len(t[b]): errors.append(f"{tid} summaries not increasing {a}<{b}")
            for k in list(t.keys()):
                if k not in TOPIC_KEYS: errors.append(f"{tid} non-whitelisted key {k}")

# segment recalls, if any, must be .RQ{n}
for m in plan["modules"]:
    for s in m["segments"]:
        for rq in s.get("recall_questions") or []:
            if not re.match(rf"^{re.escape(s['segment_id'])}\.RQ\d+$", rq["id"]):
                errors.append(f"segment recall id {rq['id']}")

# ---------- covered_by_topics rewrite in 10_exercise_solutions.json ----------
exf = OUT / "10_exercise_solutions.json"
ex_raw = exf.read_text()
ex = json.loads(ex_raw)
changed = 0
for e in ex["exercises"]:
    old = e.get("covered_by_topics") or []
    new = []
    for x in old:
        nx = remap(x)
        if nx != x: changed += 1
        new.append(nx)
    e["covered_by_topics"] = new
    if x_bad := [x for x in new if x not in topic_ids]:
        errors.append(f"{e['exercise_id']} covered_by_topics stale {x_bad}")

if errors:
    print("HARD FAIL:")
    for e_ in errors: print("  -", e_)
    sys.exit(1)

# textbook-order cross-check (informational: Agent 15 owns printed order)
tb_ok = tb["textbook_order"] == [remap(x) for x in tb["textbook_order"]] == traversal_topics

(OUT / "learning_plan_logical.json").write_text(
    json.dumps(plan, ensure_ascii=False, indent=2) + "\n")
if changed:
    exf.write_text(json.dumps(ex, ensure_ascii=False, indent=2) + "\n")

print("OK  topics=%d concepts=%d objectives=%d  covered_by_topics rewrites=%d  "
      "textbook_order==logical: %s" % (len(topic_ids), len(concept_ids), len(objectives),
                                       changed, tb_ok))
print("renumber map was identity:", all(k == v for k, v in idmap.items()))
