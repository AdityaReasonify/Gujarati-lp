#!/usr/bin/env python3
# Agent 13 — merge for output7/ch03
import json, os, collections

D = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output7/ch03"
L = lambda n: json.load(open(os.path.join(D, n), encoding="utf-8"))

meta   = L("01_meta.json")
base   = L("05_with_content.json")
auth   = L("12_authoring.json")
media  = L("09_media.json")
pub    = L("16_publication.json")
pages  = L("11_pages.json")

auth_t = {t["topic_id"]: t for t in auth["topics"]}
auth_m = {m["module_id"]: m for m in auth["modules"]}
pub_t  = {t["topic_id"]: t for t in pub["topics"]}
media_by_topic = collections.defaultdict(list)
for m in media["media"]:
    media_by_topic[m["topic_id"]].append(m)

MEDIA_KEYS = ["id","type","subtype","title","description","image_url","aspect_ratio",
              "concept_id","home_concept_id","objective_id","image_category",
              "teaching_notes","negative_prompt","generation_prompt"]

obj_by_id = {o["objective_id"]: o for o in base["objectives"]}

TOPIC_ORDER = ["topic_id","topic_name","topic_type","topic_category","difficulty",
    "objective_ids","learning_objectives","original_chunk","modified_chunk",
    "publication_chunk","word_count","key_terms","explanation","real_life_example",
    "publication_text","brief_summary","summary","detailed_summary","concept_bullets",
    "important_points","recall_questions","concepts","media","2d_tool",
    "figures_of_speech","rhyme_scheme","shabdarth","samanarthi","vilom","vyakaran",
    "estimated_exchanges","depends_on","source_topic_ids","primary_content_type",
    "secondary_content_type","tertiary_content_type","available_content_types"]

out_modules = []
for mod in base["modules"]:
    am = auth_m.get(mod["module_id"], {})
    om = {"module_id": mod["module_id"], "module_name": mod["module_name"],
          "difficult_words": am.get("difficult_words", []),
          "overall_rhyme_scheme": am.get("overall_rhyme_scheme", None),
          "segments": []}
    for seg in mod["segments"]:
        os_ = {"segment_id": seg["segment_id"], "segment_name": seg["segment_name"],
               "topics": []}
        for t in seg["topics"]:
            tid = t["topic_id"]
            a = auth_t[tid]
            p = pub_t[tid]
            ac = {c["concept_id"]: c for c in a["concepts"]}
            pc = collections.defaultdict(dict)
            for e in p["concept_publication"]:
                pc[e["concept_id"]][e["content_index"]] = e["publication_text"]
            concepts = []
            for c in t["concepts"]:
                cid = c["concept_id"]
                content = []
                for i, blk in enumerate(ac.get(cid, {}).get("content", [])):
                    nb = dict(blk)
                    if nb.get("type") == "paragraph" and i in pc[cid]:
                        nb = {"type": "paragraph", "text": nb["text"],
                              "publication_text": pc[cid][i]}
                    content.append(nb)
                concepts.append({"concept_id": cid, "concept_name": c["concept_name"],
                                 "objective_id": c["objective_id"],
                                 "key_terms": c.get("key_terms", []),
                                 "content": content})
            lo = []
            for oid in t["objective_ids"]:
                o = dict(obj_by_id[oid]); o["image_examples"] = []
                lo.append(o)
            mnodes = [{k: n[k] for k in MEDIA_KEYS} for n in media_by_topic.get(tid, [])]
            ot = {
                "topic_id": tid, "topic_name": t["topic_name"],
                "topic_type": t["topic_type"], "topic_category": t["topic_category"],
                "difficulty": t["difficulty"], "objective_ids": t["objective_ids"],
                "learning_objectives": lo,
                "original_chunk": t["original_chunk"],
                "modified_chunk": t["modified_chunk"],
                "publication_chunk": p["publication_chunk"],
                "word_count": t["word_count"], "key_terms": t["key_terms"],
                "explanation": a["explanation"], "real_life_example": a["real_life_example"],
                "publication_text": p["publication_text"],
                "brief_summary": a["brief_summary"], "summary": a["summary"],
                "detailed_summary": a["detailed_summary"],
                "concept_bullets": a["concept_bullets"],
                "important_points": a["important_points"],
                "recall_questions": a["recall_questions"],
                "concepts": concepts, "media": mnodes, "2d_tool": None,
                "figures_of_speech": a.get("figures_of_speech", []),
                "rhyme_scheme": a.get("rhyme_scheme", None),
                "shabdarth": a.get("shabdarth", []), "samanarthi": a.get("samanarthi", []),
                "vilom": a.get("vilom", []), "vyakaran": a.get("vyakaran", []),
                "estimated_exchanges": a["estimated_exchanges"],
                "depends_on": t.get("depends_on", []), "source_topic_ids": [],
                "primary_content_type": t["primary_content_type"],
                "secondary_content_type": t["secondary_content_type"],
                "tertiary_content_type": t["tertiary_content_type"],
                "available_content_types": t["available_content_types"],
            }
            assert list(ot.keys()) == TOPIC_ORDER, set(ot) ^ set(TOPIC_ORDER)
            os_["topics"].append(ot)
        om["segments"].append(os_)
    out_modules.append(om)

plan = {
    "phase": 2,
    "board": meta["board"],
    "subject": meta["subject"],
    "grade": meta["grade"],
    "level": meta["level"],
    "version": meta["version"],
    "chapter_id": meta["chapter_id"],
    "plan_id": meta["plan_id"],
    "author": "",
    "_activate": False,
    "medium_id": None,
    "subject_ref_id": None,
    "english_plan_id": None,
    "english_chapter_id": None,
    "chapter_master_id": None,
    "publication_id": 1,
    "estimated_time": 1.5,
    "textbook": pages["textbook"],
    "textbook_url": pages["textbook_url"],
    "textbook_pages": pages["textbook_pages"],
    "chapter_name": meta["chapter_name"],
    "unit_title": meta["unit_title"],
    "unit_number": meta["unit_number"],
    "topic_title": meta["chapter_name"],
    "topic_number": meta["topic_number"],
    "genre": "varta",
    "teaching_lens": meta["teaching_lens"],
    "guiding_question": meta["guiding_question"],
    "objectives": base["objectives"],
    "strand_to_objective_map": base["strand_to_objective_map"],
    "modules": out_modules,
}

with open(os.path.join(D, "13_merged.json"), "w", encoding="utf-8") as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)
    f.write("\n")

print("root keys:", len(plan))
print("topics:", sum(len(s["topics"]) for m in out_modules for s in m["segments"]))
print("media:", sum(len(t["media"]) for m in out_modules for s in m["segments"] for t in s["topics"]))
print("concepts:", sum(len(t["concepts"]) for m in out_modules for s in m["segments"] for t in s["topics"]))
