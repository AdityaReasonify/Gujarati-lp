import json, copy, sys

BASE = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output8/ch12"

merged = json.load(open(f"{BASE}/13_merged.json", encoding="utf-8"))

# ---------- 1. ARRANGE ----------
# Reading order per natak_ekanki.md / 05b_textbook_order.json: the merged tree's own
# module/segment/topic order already matches 05b_textbook_order.json's textbook_order
# list exactly (M1.S1.T1 .. M3.S6.T10, verified). No reordering needed.
modules = merged["modules"]

order_doc = json.load(open(f"{BASE}/05b_textbook_order.json", encoding="utf-8"))
walked = []
for m in modules:
    for s in m["segments"]:
        for t in s["topics"]:
            walked.append(t["topic_id"])
assert walked == order_doc["textbook_order"], (walked, order_doc["textbook_order"])
print("Merged tree order matches 05b_textbook_order.json exactly:", walked)

# ---------- 2. RENUMBER CONSECUTIVELY (walk the arranged tree) ----------
old_to_new_module = {}
old_to_new_segment = {}
old_to_new_topic = {}
old_to_new_concept = {}

m_ctr = 0
s_ctr = 0
t_ctr = 0
c_ctr = 0

for module in modules:
    m_ctr += 1
    new_module_id = f"M{m_ctr}"
    old_to_new_module[module["module_id"]] = new_module_id
    module["module_id"] = new_module_id

    for segment in module["segments"]:
        s_ctr += 1
        new_segment_id = f"{new_module_id}.S{s_ctr}"
        old_to_new_segment[segment["segment_id"]] = new_segment_id
        segment["segment_id"] = new_segment_id

        for topic in segment["topics"]:
            t_ctr += 1
            new_topic_id = f"{new_segment_id}.T{t_ctr}"
            old_to_new_topic[topic["topic_id"]] = new_topic_id
            topic["topic_id"] = new_topic_id

            for concept in topic["concepts"]:
                c_ctr += 1
                new_concept_id = f"{new_topic_id}.C{c_ctr}"
                old_to_new_concept[concept["concept_id"]] = new_concept_id
                concept["concept_id"] = new_concept_id

print("module map:", old_to_new_module)
print("segment map identity?", all(k == v for k, v in old_to_new_segment.items()))
print("topic map identity?", all(k == v for k, v in old_to_new_topic.items()))
print("concept map identity?", all(k == v for k, v in old_to_new_concept.items()))
print("num topics", t_ctr, "num concepts", c_ctr)

# ---------- 3. TRANSLATE EVERY REFERENCE ----------

def translate_media_id(old_id, concept_map):
    for old_c, new_c in concept_map.items():
        prefix = old_c + "."
        if old_id.startswith(prefix):
            suffix = old_id[len(prefix):]
            return f"{new_c}.{suffix}"
    raise ValueError(f"media id {old_id} does not resolve to a known concept")

for module in modules:
    for segment in module["segments"]:
        if "recall_questions" in segment:
            new_seg_id = segment["segment_id"]
            for rq in segment["recall_questions"]:
                suffix = rq["id"].split(".RQ")[-1]
                rq["id"] = f"{new_seg_id}.RQ{suffix}"

        for topic in segment["topics"]:
            new_topic_id = topic["topic_id"]

            for lo in topic.get("learning_objectives", []):
                if lo.get("home_topic_id") in old_to_new_topic:
                    lo["home_topic_id"] = old_to_new_topic[lo["home_topic_id"]]
                lo["anchor"] = [old_to_new_concept.get(a, a) for a in lo.get("anchor", [])]

            for rq in topic.get("recall_questions", []):
                n = rq["id"].split(".RQ")[-1]
                rq["id"] = f"{new_topic_id}.RQ{n}"
                n2 = rq["legacy_id"].split(".TR")[-1]
                rq["legacy_id"] = f"{new_topic_id}.TR{n2}"

            for md in topic.get("media", []):
                old_media_id = md["id"]
                md["id"] = translate_media_id(old_media_id, old_to_new_concept)
                if md.get("concept_id") in old_to_new_concept:
                    md["concept_id"] = old_to_new_concept[md["concept_id"]]
                if md.get("home_concept_id") in old_to_new_concept:
                    md["home_concept_id"] = old_to_new_concept[md["home_concept_id"]]

            topic["depends_on"] = [old_to_new_topic.get(x, x) for x in topic.get("depends_on", [])]
            topic["source_topic_ids"] = [old_to_new_topic.get(x, x) for x in topic.get("source_topic_ids", [])]

for obj in merged["objectives"]:
    if obj.get("home_topic_id") in old_to_new_topic:
        obj["home_topic_id"] = old_to_new_topic[obj["home_topic_id"]]
    obj["anchor"] = [old_to_new_concept.get(a, a) for a in obj.get("anchor", [])]

# ---------- 4. ASSERT: every reference resolves ----------
all_topic_ids = set()
all_concept_ids = set()
all_segment_ids = set()
all_module_ids = set()
for module in modules:
    all_module_ids.add(module["module_id"])
    for segment in module["segments"]:
        all_segment_ids.add(segment["segment_id"])
        for topic in segment["topics"]:
            all_topic_ids.add(topic["topic_id"])
            for concept in topic["concepts"]:
                all_concept_ids.add(concept["concept_id"])

errors = []
for obj in merged["objectives"]:
    if obj["home_topic_id"] not in all_topic_ids:
        errors.append(f"objective {obj['objective_id']} home_topic_id {obj['home_topic_id']} unresolved")
    for a in obj["anchor"]:
        if a not in all_concept_ids:
            errors.append(f"objective {obj['objective_id']} anchor {a} unresolved")

for module in modules:
    for segment in module["segments"]:
        for topic in segment["topics"]:
            for lo in topic.get("learning_objectives", []):
                if lo["home_topic_id"] not in all_topic_ids:
                    errors.append(f"topic {topic['topic_id']} learning_objectives home_topic_id {lo['home_topic_id']} unresolved")
                for a in lo["anchor"]:
                    if a not in all_concept_ids:
                        errors.append(f"topic {topic['topic_id']} learning_objectives anchor {a} unresolved")
            for d in topic.get("depends_on", []):
                if d not in all_topic_ids:
                    errors.append(f"topic {topic['topic_id']} depends_on {d} unresolved")
            for st in topic.get("source_topic_ids", []):
                if st not in all_topic_ids:
                    errors.append(f"topic {topic['topic_id']} source_topic_ids {st} unresolved")
            for md in topic.get("media", []):
                if md.get("concept_id") not in all_concept_ids:
                    errors.append(f"media {md['id']} concept_id {md.get('concept_id')} unresolved")
                if md.get("home_concept_id") not in all_concept_ids:
                    errors.append(f"media {md['id']} home_concept_id {md.get('home_concept_id')} unresolved")
            for rq in topic.get("recall_questions", []):
                if not rq["id"].startswith(topic["topic_id"] + ".RQ"):
                    errors.append(f"topic {topic['topic_id']} recall id malformed {rq['id']}")
                if not rq["legacy_id"].startswith(topic["topic_id"] + ".TR"):
                    errors.append(f"topic {topic['topic_id']} recall legacy_id malformed {rq['legacy_id']}")

root_obj_ids = {o["objective_id"] for o in merged["objectives"]}
for module in modules:
    for segment in module["segments"]:
        for topic in segment["topics"]:
            for oid in topic.get("objective_ids", []):
                if oid not in root_obj_ids:
                    errors.append(f"topic {topic['topic_id']} objective_ids {oid} not in root registry")

if errors:
    print("REFERENCE ERRORS:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
else:
    print("All references resolve cleanly. No stale anchors.")

# ---------- covered_by_topics rewrite in 10_exercise_solutions.json ----------
ex = json.load(open(f"{BASE}/10_exercise_solutions.json", encoding="utf-8"))
ex_errors = []
for e in ex["exercises"]:
    new_list = []
    for tid in e.get("covered_by_topics", []) or []:
        new_tid = old_to_new_topic.get(tid, tid)
        if new_tid not in all_topic_ids:
            ex_errors.append(f"exercise {e['exercise_id']} covered_by_topics {tid} -> {new_tid} unresolved")
        new_list.append(new_tid)
    e["covered_by_topics"] = new_list

if ex_errors:
    print("EXERCISE REFERENCE ERRORS:")
    for e in ex_errors:
        print(" -", e)
    sys.exit(1)
else:
    print("All covered_by_topics resolve cleanly after rewrite.")

json.dump(ex, open(f"{BASE}/10_exercise_solutions.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("rewrote 10_exercise_solutions.json covered_by_topics in place")

json.dump(merged, open(f"{BASE}/_tmp_renumbered.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("wrote _tmp_renumbered.json")
