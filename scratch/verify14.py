import json,re,sys
P="/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch03/learning_plan_logical.json"
d=json.load(open(P,encoding="utf-8"))
err=[]
ROOT=set("board genre grade level phase author modules plan_id subject version ordering textbook _activate medium_id chapter_id objectives unit_title topic_title unit_number chapter_name textbook_url topic_number teaching_lens estimated_time publication_id subject_ref_id textbook_pages english_plan_id guiding_question chapter_master_id english_chapter_id strand_to_objective_map".split())
if set(d)!=ROOT: err.append(f"root key mismatch: missing {ROOT-set(d)} extra {set(d)-ROOT}")
objs={o["objective_id"]:o for o in d["objectives"]}
GU=re.compile(r"[઀-૿]")
LATIN=re.compile(r"[A-Za-z]"); DEVA=re.compile(r"[ऀ-ॿ]")
mi=si=ti=ci=0
for m in d["modules"]:
    mi+=1; assert m["module_id"]==f"M{mi}"
    for s in m["segments"]:
        si+=1; assert s["segment_id"]==f"M{mi}.S{si}", s["segment_id"]
        for t in s["topics"]:
            ti+=1; tid=f"M{mi}.S{si}.T{ti}"
            if t["topic_id"]!=tid: err.append(f"topic id {t['topic_id']}!={tid}")
            if t["topic_type"] not in ("instructional","summary","assessment"): err.append(f"topic_type {t['topic_type']}")
            oc=t["original_chunk"]
            if not oc or not GU.search(oc): err.append(f"{tid} original_chunk not Gujarati")
            if LATIN.search(oc) or DEVA.search(oc): err.append(f"{tid} original_chunk has non-Gujarati script")
            if not t["concepts"]: err.append(f"{tid} no concepts")
            for c in t["concepts"]:
                ci+=1; cid=f"{tid}.C{ci}"
                if c["concept_id"]!=cid: err.append(f"concept {c['concept_id']}!={cid}")
                if c["objective_id"] not in objs: err.append(f"concept {cid} bad objective")
                if not c["content"]: err.append(f"concept {cid} empty content")
            for i,rq in enumerate(t["recall_questions"],1):
                if rq["id"]!=f"{tid}.RQ{i}": err.append(f"recall {rq['id']}")
                if rq["legacy_id"]!=f"{tid}.TR{i}": err.append(f"recall legacy {rq['legacy_id']}")
            for md in t["media"]:
                if not re.fullmatch(r"M\d+\.S\d+\.T\d+\.C\d+\.(IMG|VID|2D|3D|SIM)\d+", md["id"]): err.append(f"media {md['id']}")
                if md["concept_id"] not in {c["concept_id"] for c in t["concepts"]}: err.append(f"media {md['id']} concept not in topic")
                if md["image_url"]=="" and not md.get("generation_prompt"): err.append(f"media {md['id']} both empty")
            for lo in t["learning_objectives"]:
                r=objs[lo["objective_id"]]
                for k in ("objective_text","home_topic_id","anchor","legacy_id","strand","bloom_level","status"):
                    if lo[k]!=r[k]: err.append(f"{tid} inline mirror drift on {k}")
            if set(t["objective_ids"])!={lo["objective_id"] for lo in t["learning_objectives"]}: err.append(f"{tid} objective_ids vs inline")
            # numbers in display text
            for f in ("topic_name","explanation","real_life_example","brief_summary","summary","detailed_summary"):
                if re.search(r"(કડી|પ્રશ્ન|સ્વાધ્યાય|દુહો|ટેક)\s*\d", t[f]): err.append(f"{tid} number in display {f}")
print("modules",mi,"segments",si,"topics",ti,"concepts",ci)
print("ERRORS:", len(err)); [print(" -",e) for e in err]
