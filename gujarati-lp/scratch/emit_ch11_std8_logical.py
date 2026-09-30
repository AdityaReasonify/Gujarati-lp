import json, re, copy

BASE = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output8/ch11"

d = json.load(open(f"{BASE}/13_merged.json", encoding="utf-8"))

# ---------- 1. Confirm reading-order arrangement (already matches 00_chapter_normalized.md
# ??????? markers 1:1 in printed order -- verified by inspection). No module/segment/topic
# reordering is needed for this chapter. ----------

# ---------- 2. Renumber pass -- build old->new maps by walking the tree in its current
# (already-correct) order, and assert the walk is already consecutive with no gaps. ----------
mod_map, seg_map, top_map, con_map = {}, {}, {}, {}
m_i = 0
s_i = 0
t_i = 0
c_i = 0
for m in d["modules"]:
    m_i += 1
    new_m = f"M{m_i}"
    mod_map[m["module_id"]] = new_m
    for s in m["segments"]:
        s_i += 1
        new_s = f"{new_m}.S{s_i}"
        seg_map[s["segment_id"]] = new_s
        for t in s["topics"]:
            t_i += 1
            new_t = f"{new_s}.T{t_i}"
            top_map[t["topic_id"]] = new_t
            for c in t["concepts"]:
                c_i += 1
                new_c = f"{new_t}.C{c_i}"
                con_map[c["concept_id"]] = new_c

# Assert identity (this chapter's ids from Agent 13 were already consecutive/in-order)
assert all(k == v for k, v in mod_map.items()), f"module renumber not identity: {mod_map}"
assert all(k == v for k, v in seg_map.items()), f"segment renumber not identity: {seg_map}"
assert all(k == v for k, v in top_map.items()), f"topic renumber not identity: {top_map}"
assert all(k == v for k, v in con_map.items()), f"concept renumber not identity: {con_map}"

# ---------- 3. Apply topic_type mapping (authored enum -> closed server enum) ----------
TYPE_MAP = {
    "POEM": "instructional",
    "STORY_TELLING": "instructional",
    "CONCEPT": "instructional",
    "REVIEW": "summary",
    "EXERCISE": "assessment",
}

seen_types = set()
for m in d["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            seen_types.add(t["topic_type"])
            if t["topic_type"] not in TYPE_MAP:
                raise SystemExit(f"unknown authored topic_type: {t['topic_type']}")
            t["topic_type"] = TYPE_MAP[t["topic_type"]]

print("authored topic_type values seen:", seen_types)

# ---------- 4. Root fields ----------
d["ordering"] = "logical"
ROOT_ORDER = [
    "board", "genre", "grade", "level", "phase", "author", "modules", "plan_id", "subject",
    "version", "ordering", "textbook", "_activate", "medium_id", "chapter_id", "objectives",
    "unit_title", "topic_title", "unit_number", "chapter_name", "textbook_url", "topic_number",
    "teaching_lens", "estimated_time", "publication_id", "subject_ref_id", "textbook_pages",
    "english_plan_id", "guiding_question", "chapter_master_id", "english_chapter_id",
    "strand_to_objective_map",
]
missing = set(ROOT_ORDER) - set(d.keys())
extra = set(d.keys()) - set(ROOT_ORDER)
assert not missing, f"missing root keys: {missing}"
assert not extra, f"unexpected root keys (whitelist violation): {extra}"
assert len(ROOT_ORDER) == 32, len(ROOT_ORDER)
d = {k: d[k] for k in ROOT_ORDER}

assert d["phase"] == 2
assert d["chapter_id"] == "gseb_eng_gujarati8_ch11"
assert d["plan_id"] == "gseb_eng_gujarati8_ch11_v1"
assert d["publication_id"] is not None
assert d["english_plan_id"] is None and d["english_chapter_id"] is None

# ---------- 5. Whitelist assertions on nested shapes ----------
TOPIC_WHITELIST = {
    "media", "2d_tool", "summary", "concepts", "topic_id", "key_terms", "depends_on",
    "difficulty", "topic_name", "topic_type", "word_count", "explanation", "brief_summary",
    "objective_ids", "modified_chunk", "original_chunk", "topic_category", "concept_bullets",
    "detailed_summary", "important_points", "publication_text", "recall_questions",
    "source_topic_ids", "publication_chunk", "real_life_example", "estimated_exchanges",
    "learning_objectives", "primary_content_type", "tertiary_content_type",
    "secondary_content_type", "available_content_types",
    "figures_of_speech", "rhyme_scheme",
    "shabdarth", "samanarthi", "vilom", "vyakaran",
}
MODULE_WHITELIST = {"module_id", "module_name", "segments", "difficult_words", "overall_rhyme_scheme"}
SEGMENT_WHITELIST = {"segment_id", "segment_name", "topics"}

all_topic_ids = set()
all_concept_ids = set()
all_media_ids = set()
all_rq_ids = set()

for m in d["modules"]:
    extra = set(m.keys()) - MODULE_WHITELIST
    assert not extra, f"module {m.get('module_id')} has non-whitelisted keys: {extra}"
    for s in m["segments"]:
        extra = set(s.keys()) - SEGMENT_WHITELIST
        assert not extra, f"segment {s.get('segment_id')} has non-whitelisted keys: {extra}"
        for t in s["topics"]:
            extra = set(t.keys()) - TOPIC_WHITELIST
            assert not extra, f"topic {t.get('topic_id')} has non-whitelisted keys: {extra}"
            all_topic_ids.add(t["topic_id"])
            for c in t["concepts"]:
                all_concept_ids.add(c["concept_id"])
            for md in t.get("media") or []:
                all_media_ids.add(md["id"])
            for rq in t.get("recall_questions") or []:
                all_rq_ids.add(rq["id"])

# ---------- 6. Reference integrity: every id anywhere resolves to a node that exists ----------
errors = []

for o in d["objectives"]:
    if o["home_topic_id"] not in all_topic_ids:
        errors.append(f"objective {o['objective_id']} home_topic_id {o['home_topic_id']} missing")
    for a in o["anchor"]:
        if a not in all_concept_ids:
            errors.append(f"objective {o['objective_id']} anchor {a} missing")

objective_ids_root = {o["objective_id"] for o in d["objectives"]}
legacy_ids_root = {o["legacy_id"] for o in d["objectives"]}
assert set(d["strand_to_objective_map"].keys()) == legacy_ids_root, "strand_to_objective_map legacy mismatch"
assert set(d["strand_to_objective_map"].values()) == objective_ids_root, "strand_to_objective_map objective mismatch"

for m in d["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            for oid in t["objective_ids"]:
                if oid not in objective_ids_root:
                    errors.append(f"topic {t['topic_id']} objective_ids {oid} not in root registry")
            for lo in t["learning_objectives"]:
                if lo["objective_id"] not in objective_ids_root:
                    errors.append(f"topic {t['topic_id']} learning_objectives objective_id {lo['objective_id']} missing")
                root_obj = next(o for o in d["objectives"] if o["objective_id"] == lo["objective_id"])
                if lo["objective_text"] != root_obj["objective_text"]:
                    errors.append(f"topic {t['topic_id']} inline objective_text drift for {lo['objective_id']}")
            for dep in t.get("depends_on") or []:
                if dep not in all_topic_ids:
                    errors.append(f"topic {t['topic_id']} depends_on {dep} missing")
            for src in t.get("source_topic_ids") or []:
                if src not in all_topic_ids:
                    errors.append(f"topic {t['topic_id']} source_topic_ids {src} missing")
            for c in t["concepts"]:
                if c["objective_id"] not in objective_ids_root:
                    errors.append(f"concept {c['concept_id']} objective_id {c['objective_id']} missing")
            for md in t.get("media") or []:
                if md["concept_id"] not in all_concept_ids:
                    errors.append(f"media {md['id']} concept_id {md['concept_id']} missing")
                if md["home_concept_id"] not in all_concept_ids:
                    errors.append(f"media {md['id']} home_concept_id {md['home_concept_id']} missing")
                if not re.match(r"^M\d+\.S\d+\.T\d+\.C\d+\.(IMG|VID|2D|3D|SIM)\d+$", md["id"]):
                    errors.append(f"media id grammar bad: {md['id']}")
            for rq in t.get("recall_questions") or []:
                if not rq["id"].startswith(t["topic_id"] + ".RQ"):
                    errors.append(f"topic recall id grammar bad: {rq['id']} for topic {t['topic_id']}")
                if not rq["legacy_id"].startswith(t["topic_id"] + ".TR"):
                    errors.append(f"topic recall legacy_id grammar bad: {rq['legacy_id']}")

if errors:
    raise SystemExit("REFERENCE INTEGRITY FAILURES:\n" + "\n".join(errors))

print(f"OK: {len(all_topic_ids)} topics, {len(all_concept_ids)} concepts, "
      f"{len(all_media_ids)} media, {len(all_rq_ids)} topic recall ids, all references resolve.")

json.dump(d, open(f"{BASE}/learning_plan_logical.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
print("wrote learning_plan_logical.json")
