# -*- coding: utf-8 -*-
import json, os, collections
D="/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch06"
L=lambda f: json.load(open(os.path.join(D,f),encoding="utf-8"))
meta=L("01_meta.json"); base=L("05_with_content.json"); auth=L("12_authoring.json")
med=L("09_media.json"); pub=L("16_publication.json"); pages=L("11_pages.json")

A={t["topic_id"]:t for t in auth["topics"]}
AM={m["module_id"]:m for m in auth["modules"]}
P={t["topic_id"]:t for t in pub["topics"]}
OBJ={o["objective_id"]:o for o in base["objectives"]}
MEDIA_BY_TOPIC=collections.defaultdict(list)
MEDIA_KEYS=["id","type","subtype","title","description","image_url","aspect_ratio","concept_id",
            "home_concept_id","objective_id","image_category","teaching_notes","negative_prompt","generation_prompt"]
for mm in med["media"]:
    tid=".".join(mm["concept_id"].split(".")[:3])
    MEDIA_BY_TOPIC[tid].append({k:mm[k] for k in MEDIA_KEYS})

TOPIC_KEY_ORDER=["topic_id","topic_name","topic_type","topic_category","difficulty","depends_on",
 "source_topic_ids","objective_ids","learning_objectives","original_chunk","modified_chunk",
 "publication_chunk","word_count","key_terms","explanation","real_life_example","publication_text",
 "brief_summary","summary","detailed_summary","concept_bullets","important_points","concepts",
 "recall_questions","estimated_exchanges","figures_of_speech","rhyme_scheme","shabdarth",
 "samanarthi","vilom","vyakaran","media","2d_tool","primary_content_type","secondary_content_type",
 "tertiary_content_type","available_content_types"]

modules=[]
for m in base["modules"]:
    am=AM[m["module_id"]]
    segs=[]
    for s in m["segments"]:
        tops=[]
        for t in s["topics"]:
            tid=t["topic_id"]; a=A[tid]; p=P[tid]
            ac={c["concept_id"]:c for c in a["concepts"]}
            cp=collections.defaultdict(dict)
            for x in p["concept_publication"]: cp[x["concept_id"]][x["content_index"]]=x["publication_text"]
            concepts=[]
            for c in t["concepts"]:
                cid=c["concept_id"]; content=[]
                for i,blk in enumerate(ac[cid]["content"]):
                    if blk["type"]=="paragraph":
                        nb={"type":"paragraph","text":blk["text"]}
                        if i in cp[cid]: nb["publication_text"]=cp[cid][i]
                        content.append(nb)
                    else:
                        content.append({"type":blk["type"],"items":list(blk["items"])})
                concepts.append({"concept_id":cid,"concept_name":c["concept_name"],
                                 "objective_id":c["objective_id"],"key_terms":list(c.get("key_terms",[])),
                                 "content":content})
            lo=[]
            for oid in t["objective_ids"]:
                o=dict(OBJ[oid]); o["image_examples"]=[]; lo.append(o)
            nt={
              "topic_id":tid,"topic_name":t["topic_name"],"topic_type":t["topic_type"],
              "topic_category":t["topic_category"],"difficulty":t["difficulty"],
              "depends_on":list(t.get("depends_on",[])),"source_topic_ids":[],
              "objective_ids":list(t["objective_ids"]),"learning_objectives":lo,
              "original_chunk":t["original_chunk"],"modified_chunk":t["modified_chunk"],
              "publication_chunk":p["publication_chunk"],"word_count":t["word_count"],
              "key_terms":list(t["key_terms"]),
              "explanation":a["explanation"],"real_life_example":a["real_life_example"],
              "publication_text":p["publication_text"],
              "brief_summary":a["brief_summary"],"summary":a["summary"],
              "detailed_summary":a["detailed_summary"],
              "concept_bullets":list(a["concept_bullets"]),"important_points":list(a["important_points"]),
              "concepts":concepts,"recall_questions":a["recall_questions"],
              "estimated_exchanges":a["estimated_exchanges"],
              "figures_of_speech":a["figures_of_speech"],"rhyme_scheme":a["rhyme_scheme"],
              "shabdarth":a.get("shabdarth",[]),"samanarthi":a.get("samanarthi",[]),
              "vilom":a.get("vilom",[]),"vyakaran":a.get("vyakaran",[]),
              "media":MEDIA_BY_TOPIC.get(tid,[]),"2d_tool":med["2d_tool"],
              "primary_content_type":t["primary_content_type"],
              "secondary_content_type":t["secondary_content_type"],
              "tertiary_content_type":t["tertiary_content_type"],
              "available_content_types":list(t["available_content_types"]),
            }
            assert set(nt)==set(TOPIC_KEY_ORDER), set(nt)^set(TOPIC_KEY_ORDER)
            tops.append({k:nt[k] for k in TOPIC_KEY_ORDER})
        segs.append({"segment_id":s["segment_id"],"segment_name":s["segment_name"],"topics":tops})
    modules.append({"module_id":m["module_id"],"module_name":m["module_name"],
                    "difficult_words":am["difficult_words"],
                    "overall_rhyme_scheme":am["overall_rhyme_scheme"],
                    "segments":segs})

plan={
 "phase":2,
 "board":meta["board"],
 "subject":meta["subject"],
 "grade":meta["grade"],
 "level":meta["level"],
 "version":meta["version"],
 "chapter_id":meta["chapter_id"],
 "plan_id":meta["plan_id"],
 "chapter_name":meta["chapter_name"],
 "unit_title":meta["unit_title"],
 "unit_number":meta["unit_number"],
 "topic_title":meta["chapter_name"],
 "topic_number":meta["topic_number"],
 "genre":meta["genre"],
 "teaching_lens":meta["teaching_lens"],
 "guiding_question":meta["guiding_question"],
 "textbook":pages["textbook"],
 "textbook_url":pages["textbook_url"],
 "textbook_pages":pages["textbook_pages"],
 "author":"",
 "_activate":False,
 "ordering":None,
 "medium_id":None,
 "subject_ref_id":None,
 "english_plan_id":None,
 "english_chapter_id":None,
 "chapter_master_id":None,
 "publication_id":1,
 "estimated_time":1.5,
 "objectives":base["objectives"],
 "strand_to_objective_map":base["strand_to_objective_map"],
 "modules":modules,
}
ROOT32=set("""board genre grade level phase author modules plan_id subject version ordering
textbook _activate medium_id chapter_id objectives unit_title topic_title unit_number
chapter_name textbook_url topic_number teaching_lens estimated_time publication_id
subject_ref_id textbook_pages english_plan_id guiding_question chapter_master_id
english_chapter_id strand_to_objective_map""".split())
assert set(plan)==ROOT32, set(plan)^ROOT32
out=os.path.join(D,"13_merged.json")
json.dump(plan,open(out,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("wrote",out,os.path.getsize(out),"bytes; root keys",len(plan))
