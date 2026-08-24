# -*- coding: utf-8 -*-
import json,re,os
D="/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch06"
p=json.load(open(os.path.join(D,"13_merged.json"),encoding="utf-8"))
bad=[]
OBJ={o["objective_id"]:o for o in p["objectives"]}
allt=set(); allc=set(); cnums=[]
for m in p["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            allt.add(t["topic_id"])
            for c in t["concepts"]: allc.add(c["concept_id"]); cnums.append(int(c["concept_id"].split(".C")[1]))
for m in p["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            tid=t["topic_id"]
            # 1 inline mirror identity
            for lo in t["learning_objectives"]:
                ro=OBJ[lo["objective_id"]]
                if lo["objective_text"]!=ro["objective_text"]: bad.append("mirror text drift "+tid)
                for k in ("legacy_id","strand","strand_name","bloom_level","home_topic_id","status","theme_category"):
                    if lo[k]!=ro[k]: bad.append("mirror %s drift %s"%(k,tid))
                if lo["anchor"]!=ro["anchor"]: bad.append("mirror anchor drift "+tid)
                if "image_examples" not in lo: bad.append("mirror missing image_examples "+tid)
            # 2 working fields gone
            for w in ("markers","source_lines_00_normalized","concept_publication","reuse_score","pitfall","notes"):
                if w in t: bad.append("working field %s survived in %s"%(w,tid))
            # 3 media
            for mm in t["media"]:
                if "topic_id" in mm: bad.append("media working key topic_id survived "+mm["id"])
                if not re.match(r"^M\d+\.S\d+\.T\d+\.C\d+\.(IMG|VID|2D|3D|SIM)\d+$",mm["id"]): bad.append("media id "+mm["id"])
                if mm["concept_id"] not in allc: bad.append("media concept missing "+mm["id"])
                if not mm["concept_id"].startswith(tid+"."): bad.append("media not under topic "+mm["id"])
            # 4 concepts content publication_text present on paragraphs
            for c in t["concepts"]:
                if c["objective_id"] not in OBJ: bad.append("concept obj "+c["concept_id"])
                for i,b in enumerate(c["content"]):
                    if b["type"]=="paragraph" and not b.get("publication_text","").strip():
                        bad.append("no publication_text on %s content[%d]"%(c["concept_id"],i))
            # 5 verbatim untouched
            if t["original_chunk"] not in t["publication_chunk"]: bad.append("verbatim not inside publication_chunk "+tid)
            # 6 recall ids
            for i,q in enumerate(t["recall_questions"],1):
                if q["id"]!="%s.RQ%d"%(tid,i) or q["legacy_id"]!="%s.TR%d"%(tid,i): bad.append("recall id "+tid)
            if t["topic_type"] not in ("POEM","STORY_TELLING","CONCEPT","REVIEW"): bad.append("topic_type "+tid)
for o in p["objectives"]:
    if o["home_topic_id"] not in allt: bad.append("home_topic_id "+o["objective_id"])
    for a in o["anchor"]:
        if a not in allc: bad.append("anchor "+a)
if cnums!=list(range(1,len(cnums)+1)): bad.append("concept counter not continuous %s"%cnums)
if p["publication_id"] is None: bad.append("publication_id null")
if p["plan_id"]!="%s_v%d"%(p["chapter_id"],p["version"]): bad.append("plan_id")
if p["chapter_id"]!="gseb_eng_gujarati%d_ch%d"%(p["grade"],p["unit_number"]): bad.append("chapter_id")
if p["phase"]!=2: bad.append("phase")
s=json.dumps(p,ensure_ascii=False)
if ".SR" in s: bad.append(".SR id present")
print("topics",len(allt),"concepts",len(allc),"concept nums",cnums)
print("POST-MERGE ISSUES:",bad if bad else "NONE")
