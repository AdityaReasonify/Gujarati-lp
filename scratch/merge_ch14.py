#!/usr/bin/env python3
# Agent 13 — merge every layer onto 05_with_content.json into one phase-2 plan.
import json, os, collections

D = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch14"
L = lambda n: json.load(open(os.path.join(D, n)))

meta = L("01_meta.json")
base = L("05_with_content.json")
media = L("09_media.json")
pages = L("11_pages.json")
auth = L("12_authoring.json")
pub = L("16_publication.json")

AUTH = {t["topic_id"]: t for t in auth["topics"]}
AUTHM = {m["module_id"]: m for m in auth["modules"]}
PUB = {t["topic_id"]: t for t in pub["topics"]}
MEDIA = collections.defaultdict(list)
for m in media["media"]:
    MEDIA[m["topic_id"]].append(m)

TOPIC_KEYS = ["media", "2d_tool", "summary", "concepts", "topic_id", "key_terms", "depends_on",
              "difficulty", "topic_name", "topic_type", "word_count", "explanation",
              "brief_summary", "objective_ids", "modified_chunk", "original_chunk",
              "topic_category", "concept_bullets", "detailed_summary", "important_points",
              "publication_text", "recall_questions", "source_topic_ids", "publication_chunk",
              "real_life_example", "estimated_exchanges", "learning_objectives",
              "primary_content_type", "tertiary_content_type", "secondary_content_type",
              "available_content_types"]
EXTRA_KEYS = ["figures_of_speech", "rhyme_scheme", "shabdarth", "samanarthi", "vilom", "vyakaran"]

OBJ = {o["objective_id"]: o for o in base["objectives"]}

modules = []
for m in base["modules"]:
    am = AUTHM.get(m["module_id"], {})
    nm = {"module_id": m["module_id"], "module_name": m["module_name"],
          "difficult_words": am.get("difficult_words", []),
          "overall_rhyme_scheme": am.get("overall_rhyme_scheme", None),
          "segments": []}
    for s in m["segments"]:
        ns = {"segment_id": s["segment_id"], "segment_name": s["segment_name"], "topics": []}
        for t in s["topics"]:
            tid = t["topic_id"]
            a = AUTH[tid]
            p = PUB[tid]
            cp = collections.defaultdict(dict)
            for e in p["concept_publication"]:
                cp[e["concept_id"]][e["content_index"]] = e["publication_text"]
            acon = {c["concept_id"]: c["content"] for c in a["concepts"]}
            concepts = []
            for c in t["concepts"]:
                cid = c["concept_id"]
                content = []
                for i, blk in enumerate(acon.get(cid, [])):
                    nb = dict(blk)
                    if nb.get("type") == "paragraph" and i in cp.get(cid, {}):
                        nb["publication_text"] = cp[cid][i]
                    content.append(nb)
                concepts.append({"concept_id": cid, "concept_name": c["concept_name"],
                                 "objective_id": c["objective_id"],
                                 "key_terms": c.get("key_terms", []), "content": content})
            lo = []
            for oid in t["objective_ids"]:
                o = dict(OBJ[oid])
                o["image_examples"] = []
                lo.append(o)
            nt = {
                "topic_id": tid,
                "topic_name": t["topic_name"],
                "topic_type": t["topic_type"],
                "topic_category": t["topic_category"],
                "difficulty": t["difficulty"],
                "depends_on": t.get("depends_on", []),
                "source_topic_ids": t.get("source_topic_ids", []),
                "objective_ids": t["objective_ids"],
                "learning_objectives": lo,
                "original_chunk": t["original_chunk"],
                "modified_chunk": t["modified_chunk"],
                "word_count": {"original": t["word_count"]["original"]},
                "key_terms": t.get("key_terms", []),
                "explanation": a["explanation"],
                "real_life_example": a["real_life_example"],
                "brief_summary": a["brief_summary"],
                "summary": a["summary"],
                "detailed_summary": a["detailed_summary"],
                "concept_bullets": a["concept_bullets"],
                "important_points": a["important_points"],
                "concepts": concepts,
                "recall_questions": a["recall_questions"],
                "estimated_exchanges": a["estimated_exchanges"],
                "publication_text": p["publication_text"],
                "publication_chunk": p["publication_chunk"],
                "media": MEDIA.get(tid, []),
                "2d_tool": None,
                "primary_content_type": t["primary_content_type"],
                "secondary_content_type": t["secondary_content_type"],
                "tertiary_content_type": t["tertiary_content_type"],
                "available_content_types": t["available_content_types"],
                "figures_of_speech": a.get("figures_of_speech", []),
                "rhyme_scheme": a.get("rhyme_scheme", None),
                "shabdarth": a.get("shabdarth"),
                "samanarthi": a.get("samanarthi"),
                "vilom": a.get("vilom"),
                "vyakaran": a.get("vyakaran"),
            }
            # strip working fields carried on media nodes
            nt["media"] = [{k: v for k, v in mm.items() if k != "topic_id"} for mm in nt["media"]]
            for mm in nt["media"]:
                mm.setdefault("concept_id", mm.get("home_concept_id"))
            ns["topics"].append(nt)
        nm["segments"].append(ns)
    modules.append(nm)

plan = {
    "phase": 2,
    "board": meta["board"],
    "subject": meta["subject"],
    "grade": meta["grade"],
    "level": meta["level"],
    "version": meta["version"],
    "chapter_id": meta["chapter_id"],
    "plan_id": meta["plan_id"],
    "chapter_name": meta["chapter_name"],
    "unit_title": meta["unit_title"],
    "unit_number": meta["unit_number"],
    "topic_title": meta["chapter_name"],
    "topic_number": meta["topic_number"],
    "genre": base["genre"],
    "teaching_lens": meta["teaching_lens"],
    "guiding_question": meta["guiding_question"],
    "textbook": pages["textbook"],
    "textbook_url": pages["textbook_url"],
    "textbook_pages": pages["textbook_pages"],
    "author": "",
    "_activate": False,
    "medium_id": None,
    "subject_ref_id": None,
    "english_plan_id": None,
    "english_chapter_id": None,
    "estimated_time": 1.5,
    "publication_id": 1,
    "chapter_master_id": meta["chapter_master_id"],
    "objectives": base["objectives"],
    "strand_to_objective_map": base["strand_to_objective_map"],
    "modules": modules,
}

with open(os.path.join(D, "13_merged.json"), "w") as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("root keys", len(plan))
print("topics", sum(len(s["topics"]) for m in plan["modules"] for s in m["segments"]))
t0 = plan["modules"][0]["segments"][0]["topics"][0]
print("topic keys", len(t0), sorted(set(t0) - set(TOPIC_KEYS) - set(EXTRA_KEYS)),
      "missing", sorted(set(TOPIC_KEYS) - set(t0)))
