import json

BASE = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output8/ch12"

merged = json.load(open(f"{BASE}/_tmp_renumbered.json", encoding="utf-8"))
merged["ordering"] = "logical"  # Agent-14 owned field, not present upstream

ROOT_KEYS = ["board","genre","grade","level","phase","author","modules","plan_id","subject",
             "version","ordering","textbook","_activate","medium_id","chapter_id","objectives",
             "unit_title","topic_title","unit_number","chapter_name","textbook_url","topic_number",
             "teaching_lens","estimated_time","publication_id","subject_ref_id","textbook_pages",
             "english_plan_id","guiding_question","chapter_master_id","english_chapter_id",
             "strand_to_objective_map"]

TOPIC_KEYS = ["media","2d_tool","summary","concepts","topic_id","key_terms","depends_on",
              "difficulty","topic_name","topic_type","word_count","explanation","brief_summary",
              "objective_ids","modified_chunk","original_chunk","topic_category","concept_bullets",
              "detailed_summary","important_points","publication_text","recall_questions",
              "source_topic_ids","publication_chunk","real_life_example","estimated_exchanges",
              "learning_objectives","primary_content_type","tertiary_content_type",
              "secondary_content_type","available_content_types",
              # kavya extras
              "figures_of_speech","rhyme_scheme",
              # optional bhasha-bodh extras
              "shabdarth","samanarthi","vilom","vyakaran"]

MODULE_KEYS = ["module_id","module_name","segments","difficult_words","overall_rhyme_scheme"]
SEGMENT_KEYS_BASE = ["segment_id","segment_name","topics"]  # + optional recall_questions

TYPE_MAP = {"POEM": "instructional", "STORY_TELLING": "instructional",
            "CONCEPT": "instructional", "REVIEW": "summary", "EXERCISE": "assessment"}

out = {}
missing_root = [k for k in ROOT_KEYS if k not in merged]
if missing_root:
    raise SystemExit(f"merged file missing root keys: {missing_root}")

for k in ROOT_KEYS:
    out[k] = merged[k]

assert out["phase"] == 2

new_modules = []
for module in merged["modules"]:
    nm = {}
    for k in MODULE_KEYS:
        if k in module:
            nm[k] = module[k]
    missing = [k for k in MODULE_KEYS if k != "segments" and k not in module]
    if missing:
        raise SystemExit(f"module {module.get('module_id')} missing keys {missing}")

    new_segments = []
    for segment in module["segments"]:
        ns = {}
        for k in SEGMENT_KEYS_BASE:
            ns[k] = segment[k]
        if "recall_questions" in segment:
            ns["recall_questions"] = segment["recall_questions"]

        new_topics = []
        for topic in segment["topics"]:
            missing_t = [k for k in TOPIC_KEYS if k not in topic and k not in
                         ("figures_of_speech","rhyme_scheme","shabdarth","samanarthi","vilom","vyakaran")]
            if missing_t:
                raise SystemExit(f"topic {topic.get('topic_id')} missing required keys {missing_t}")
            extra = set(topic.keys()) - set(TOPIC_KEYS)
            if extra:
                raise SystemExit(f"topic {topic.get('topic_id')} has non-whitelisted keys {extra}")

            nt = {}
            for k in TOPIC_KEYS:
                if k in topic:
                    nt[k] = topic[k]

            authored_type = nt.get("topic_type")
            if authored_type not in TYPE_MAP:
                raise SystemExit(f"topic {nt.get('topic_id')} has unknown topic_type {authored_type!r}")
            nt["topic_type"] = TYPE_MAP[authored_type]

            new_topics.append(nt)
        ns["topics"] = new_topics
        new_segments.append(ns)
    nm["segments"] = new_segments
    new_modules.append(nm)

out["modules"] = new_modules

if set(out.keys()) != set(ROOT_KEYS):
    raise SystemExit(f"root key mismatch: {set(out.keys()) ^ set(ROOT_KEYS)}")
if len(ROOT_KEYS) != 32:
    raise SystemExit(f"ROOT_KEYS count is {len(ROOT_KEYS)}, expected 32")

json.dump(out, open(f"{BASE}/learning_plan_logical.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("wrote learning_plan_logical.json")
print("root key count:", len(out.keys()))

types = set()
for m in out["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            types.add(t["topic_type"])
print("topic_type values used:", types)
