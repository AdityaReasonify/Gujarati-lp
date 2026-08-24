# -*- coding: utf-8 -*-
import json, re, os, unicodedata
D="/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch06"
L=lambda f: json.load(open(os.path.join(D,f),encoding="utf-8"))
meta=L("01_meta.json"); base=L("05_with_content.json"); auth=L("12_authoring.json")
med=L("09_media.json"); pub=L("16_publication.json"); pages=L("11_pages.json")
pit=L("07_pitfalls.json"); sens=L("08_sensitivity.json"); ex=L("10_exercise_solutions.json")
norm=open(os.path.join(D,"00_chapter_normalized.md"),encoding="utf-8").read()
issues=[]; notes=[]
def bad(sec,msg,owner): issues.append((sec,msg,owner))

topics=[]
for m in base["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            topics.append((m["module_id"],s["segment_id"],t))
print("topics:",len(topics))

A={t["topic_id"]:t for t in auth["topics"]}
P={t["topic_id"]:t for t in pub["topics"]}
MEDbyC={}
for mm in med["media"]: MEDbyC.setdefault(mm["concept_id"],[]).append(mm)

# ---------- B: script purity ----------
GUJ=lambda ch: 0x0A80<=ord(ch)<=0x0AFF
DEV=lambda ch: 0x0900<=ord(ch)<=0x097F
ROM=lambda ch: ('a'<=ch<='z') or ('A'<=ch<='Z')
def scan(text,label,allow_bracket=True):
    if not isinstance(text,str): return
    # strip bracketed technical terms ( ... ) containing roman
    t=re.sub(r'\([A-Za-z][A-Za-z \-/]*\)','',text) if allow_bracket else text
    r=set(c for c in t if ROM(c)); d=set(c for c in t if DEV(c))
    if r: bad("B","Roman chars %r in %s"%("".join(sorted(r)),label),"A5/A12")
    if d: bad("B","Devanagari chars %r in %s"%("".join(sorted(d)),label),"A5/A12")
    if '।' in t: bad("B","danda U+0964 in %s"%label,"A5")

DIGITS=re.compile(r'[0-9૦-૯]')
def digitcheck(text,label):
    if isinstance(text,str) and DIGITS.search(text):
        bad("F","digit in display text: %s -> %r"%(label,DIGITS.findall(text)),"A12")

def wc(s): return len(s.split())

# ---------- per topic ----------
rows=[]
concept_seq=[]
for mid,sid,t in topics:
    tid=t["topic_id"]; a=A.get(tid); p=P.get(tid)
    if a is None: bad("C","no authoring block for %s"%tid,"A12"); continue
    if p is None: bad("PUB","no publication block for %s"%tid,"A16"); continue
    oc=t.get("original_chunk","")
    if not oc.strip(): bad("B","empty original_chunk %s"%tid,"A5")
    scan(oc,"%s.original_chunk"%tid)
    # C
    for f in ("explanation","real_life_example"):
        v=a.get(f,"")
        if not v.strip(): bad("C","%s.%s empty"%(tid,f),"A12")
        n=wc(v)
        if not (55<=n<=90): bad("C","%s.%s = %d words (band 55-90)"%(tid,f,n),"A12")
    e=wc(a["explanation"]); r=wc(a["real_life_example"])
    # summaries strictly increasing (by chars)
    bs,su,ds=a["brief_summary"],a["summary"],a["detailed_summary"]
    if not (len(bs)<len(su)<len(ds)): bad("F","%s summaries not strictly increasing (%d/%d/%d)"%(tid,len(bs),len(su),len(ds)),"A12")
    # display text scans
    disp={"topic_name":t["topic_name"],"explanation":a["explanation"],"real_life_example":a["real_life_example"],
          "brief_summary":bs,"summary":su,"detailed_summary":ds}
    for k,v in disp.items(): scan(v,"%s.%s"%(tid,k)); digitcheck(v,"%s.%s"%(tid,k))
    for i,b in enumerate(a["concept_bullets"]): scan(b,"%s.cb%d"%(tid,i)); digitcheck(b,"%s.concept_bullets[%d]"%(tid,i))
    for i,b in enumerate(a["important_points"]): scan(b,"%s.ip%d"%(tid,i)); digitcheck(b,"%s.important_points[%d]"%(tid,i))
    for i,b in enumerate(t.get("key_terms",[])): scan(b,"%s.kt%d"%(tid,i)); digitcheck(b,"%s.key_terms[%d]"%(tid,i))
    # recall questions
    for i,q in enumerate(a["recall_questions"],1):
        want="%s.RQ%d"%(tid,i); wantl="%s.TR%d"%(tid,i)
        if q["id"]!=want: bad("Contract","%s recall id %s != %s"%(tid,q["id"],want),"A12")
        if q["legacy_id"]!=wantl: bad("Contract","%s recall legacy_id %s != %s"%(tid,q["legacy_id"],wantl),"A12")
        if ".SR" in q["id"]: bad("Contract",".SR id found %s"%q["id"],"A12")
        if q["bloom_level"]!=q["bloom_level"].lower(): bad("Contract","%s RQ%d bloom not lowercase"%(tid,i),"A12")
        if q["difficulty"] not in ("easy","medium","hard"): bad("Contract","%s RQ%d difficulty %s"%(tid,i,q["difficulty"]),"A12")
        scan(q["prompt"],"%s.RQ%d.prompt"%(tid,i)); digitcheck(q["prompt"],"%s.RQ%d.prompt"%(tid,i))
        scan(q["answer"],"%s.RQ%d.answer"%(tid,i)); digitcheck(q["answer"],"%s.RQ%d.answer"%(tid,i))
    if not (2<=len(a["recall_questions"])<=3): bad("F","%s has %d recall questions (2-3)"%(tid,len(a["recall_questions"])),"A12")
    # figures_of_speech verbatim
    for fs in a.get("figures_of_speech") or []:
        if fs.get("lines","") not in oc:
            bad("D","%s figures_of_speech lines not verbatim in original_chunk: %r"%(tid,fs.get("lines")),"A7/A12")
    # concepts
    ac={c["concept_id"]:c for c in a["concepts"]}
    for c in t["concepts"]:
        cid=c["concept_id"]; concept_seq.append(cid)
        if not re.match(r'^M\d+\.S\d+\.T\d+\.C\d+$',cid): bad("Contract","bad concept_id %s"%cid,"A2")
        if not cid.startswith(tid+"."): bad("Contract","concept %s not under %s"%(cid,tid),"A2")
        if cid not in ac: bad("Contract","no authored content for concept %s"%cid,"A12"); continue
        if not ac[cid]["content"]: bad("Contract","empty content[] for %s"%cid,"A12")
        for i,blk in enumerate(ac[cid]["content"]):
            if blk["type"]=="paragraph": scan(blk["text"],"%s[%d]"%(cid,i)); digitcheck(blk["text"],"%s.content[%d]"%(cid,i))
            elif blk["type"]=="list":
                for j,it in enumerate(blk["items"]): scan(it,"%s[%d][%d]"%(cid,i,j)); digitcheck(it,"%s.content[%d].items[%d]"%(cid,i,j))
        if c["objective_id"] not in [o["objective_id"] for o in base["objectives"]]:
            bad("Contract","concept %s objective_id %s not in registry"%(cid,c["objective_id"]),"A2")
    # publication
    if not p.get("publication_text","").strip(): bad("PUB","%s publication_text empty"%tid,"A16")
    scan(p["publication_text"],"%s.publication_text"%tid); digitcheck(p["publication_text"],"%s.publication_text"%tid)
    for voc in ("બાળકો","જુઓ —","બોલો"):
        if voc in p["publication_text"]: bad("PUB","%s publication_text carries %r"%(tid,voc),"A16")
    pc=p["publication_chunk"]
    if pc==oc: pass
    elif oc in pc: notes.append("%s: publication_chunk contains original_chunk verbatim, then the publication rewrite (A16 spec §publication_chunk)"%tid)
    else: bad("PUB","%s publication_chunk does not carry original_chunk verbatim"%tid,"A16")
    # concept_publication index match
    cp=p.get("concept_publication",[])
    expect=[]
    for c in t["concepts"]:
        cid=c["concept_id"]
        for i,blk in enumerate(ac.get(cid,{}).get("content",[])):
            if blk["type"]=="paragraph": expect.append((cid,i))
    got=[(x["concept_id"],x["content_index"]) for x in cp]
    if expect!=got: bad("PUB","%s concept_publication index mismatch expect=%s got=%s"%(tid,expect,got),"A16")
    for x in cp: scan(x["publication_text"],"%s.cp"%tid); digitcheck(x["publication_text"],"%s.cp %s[%d]"%(tid,x["concept_id"],x["content_index"]))
    # word_count
    if t["word_count"]["original"]!=wc(oc):
        bad("F","%s word_count.original=%s but chunk has %d words"%(tid,t["word_count"]["original"],wc(oc)),"A5")
    rows.append((tid,e,r,len(t["concepts"]),len(a["recall_questions"])))

# ---------- objectives registry ----------
allt={t["topic_id"] for _,_,t in topics}
allc=set(concept_seq)
oids=[]
for o in base["objectives"]:
    oid=o["objective_id"]; oids.append(oid)
    if o["home_topic_id"] not in allt: bad("Contract","objective %s home_topic_id %s missing"%(oid,o["home_topic_id"]),"A2")
    for an in o["anchor"]:
        if an not in allc: bad("Contract","objective %s anchor %s missing"%(oid,an),"A2")
    n=wc(o["objective_text"])
    if not (12<=n<=30): bad("C","objective %s objective_text = %d words (band 12-30)"%(oid,n),"A2")
    scan(o["objective_text"],"%s.objective_text"%oid); digitcheck(o["objective_text"],"%s.objective_text"%oid)
    if o["bloom_level"][0].islower(): bad("Contract","objective %s bloom_level not capitalised"%oid,"A2")
if len(set(oids))!=len(oids): bad("Contract","duplicate objective_id","A2")
smap=base["strand_to_objective_map"]
for o in base["objectives"]:
    if smap.get(o["legacy_id"])!=o["objective_id"]: bad("Contract","strand_to_objective_map missing/wrong for %s"%o["legacy_id"],"A2")
if len(smap)!=len(oids): bad("Contract","strand_to_objective_map size %d != objectives %d"%(len(smap),len(oids)),"A2")
for _,_,t in topics:
    for oid in t["objective_ids"]:
        if oid not in oids: bad("Contract","%s objective_ids %s unknown"%(t["topic_id"],oid),"A2")
    for dep in t.get("depends_on",[]):
        if dep not in allt: bad("Contract","%s depends_on %s missing"%(t["topic_id"],dep),"A2")

# ---------- concept continuity ----------
nums=[int(c.split(".C")[1]) for c in concept_seq]
if nums!=list(range(1,len(nums)+1)): bad("Contract","concept counter not chapter-continuous: %s"%nums,"A2")

# ---------- traversal ids ----------
mi=0
for m in base["modules"]:
    mi+=1
    if m["module_id"]!="M%d"%mi: bad("Contract","module id %s != M%d"%(m["module_id"],mi),"A2")
si=0; ti=0
for m in base["modules"]:
    for s in m["segments"]:
        si+=1
        if s["segment_id"]!="%s.S%d"%(m["module_id"],si): bad("Contract","segment id %s at position %d"%(s["segment_id"],si),"A2")
        for t in s["topics"]:
            ti+=1
            if t["topic_id"]!="%s.T%d"%(s["segment_id"],ti): bad("Contract","topic id %s at position %d"%(t["topic_id"],ti),"A2")

# ---------- media ----------
MEDIA_ID_RE=re.compile(r"^(?P<c>M\d+\.S\d+\.T\d+\.C\d+)\.(?P<s>IMG|VID|2D|3D|SIM)(?P<n>\d+)$")
scenes=sum(1 for _,_,t in topics if "image" in t["available_content_types"])
rr=med["reuse_report"]
if rr["scenes"]!=scenes: bad("F","reuse_report.scenes=%s but %d topics carry image"%(rr["scenes"],scenes),"A9")
if rr["authored"]!=rr["scenes"]: bad("F","authored %s != scenes %s"%(rr["authored"],rr["scenes"]),"A9")
if rr["reused"]!=0: bad("F","reused=%s must be 0 (no Gujarati frame pool)"%rr["reused"],"A9")
for mm in med["media"]:
    if not MEDIA_ID_RE.match(mm["id"]): bad("Contract","media id fails MEDIA_ID_RE: %s"%mm["id"],"A9")
    if mm["concept_id"] not in allc: bad("Contract","media %s concept_id missing"%mm["id"],"A9")
    if mm["image_url"]!="": bad("F","media %s image_url non-empty %r"%(mm["id"],mm["image_url"]),"A9")
    if not (mm.get("generation_prompt") or "").strip(): bad("F","media %s empty generation_prompt"%mm["id"],"A9")
    if "Devanagari script labels" not in mm.get("negative_prompt",""): bad("F","media %s negative_prompt lacks 'Devanagari script labels'"%mm["id"],"A9")
    if "reused frame" in json.dumps(mm,ensure_ascii=False): bad("F","media %s carries a [reused frame] stamp"%mm["id"],"A9")
n2d=sum(1 for _,_,t in topics if False)
print("2d_tool:",json.dumps(med["2d_tool"],ensure_ascii=False)[:60])

# ---------- markers ----------
import collections
mk=collections.Counter(re.findall(r'\[\[(સંવાદ|સ્વાધ્યાય|કડી|દુહો|પદ|ઘટના)[:\s]',norm))
carry=collections.Counter()
for _,_,t in topics:
    for m_ in t.get("markers",[]):
        k=re.match(r'\[\[(\S+?)[:\s]',m_)
        if k: carry[k.group(1).rstrip(':')]+=1
print("markers in 00:",dict(mk)," carried by topics:",dict(carry))
for k in ("સંવાદ",):
    if mk[k]!=carry[k]: bad("B","marker count mismatch %s: %d in 00_chapter_normalized.md vs %d carried"%(k,mk[k],carry[k]),"A2")
if carry.get("સ્વાધ્યાય",0): bad("B","a [[સ્વાધ્યાય]] block became a topic","A2")
if mk["સ્વાધ્યાય"]!=len(meta["exercise_inventory"]): bad("E","સ્વાધ્યાય markers %d != exercise_inventory %d"%(mk["સ્વાધ્યાય"],len(meta["exercise_inventory"])),"A1")

# ---------- exercises ----------
cr=ex["coverage_report"]
if len(cr["blocks_found"])!=len(meta["exercise_inventory"]): bad("E","blocks_found %d != inventory %d"%(len(cr["blocks_found"]),len(meta["exercise_inventory"])),"A10")
if cr["unanswered"]: bad("E","unanswered blocks: %s"%cr["unanswered"],"A10")
inv=[b["verbatim_heading"] for b in meta["exercise_inventory"]]
missing=[h for h in inv if h not in cr["blocks_found"]]
if missing: bad("E","inventory heading not in blocks_found: %s"%missing,"A10")
noans=[e["exercise_id"] for e in ex["exercises"] if not str(e.get("answer","")).strip()]
if noans: bad("E","exercises with empty answer: %s"%noans[:10],"A10")

# ---------- topic_type ----------
for _,_,t in topics:
    if t["topic_type"] not in ("POEM","STORY_TELLING","CONCEPT","REVIEW"):
        bad("Contract","topic_type %s not an authored enum value"%t["topic_type"],"A2")

print("\n--- word counts (expl / rle / concepts / RQ) ---")
for r in rows: print("  %-10s %3d %3d  c=%d rq=%d"%r)
print("\n--- objective word counts ---")
print("  ", [wc(o["objective_text"]) for o in base["objectives"]])
print("\n=== ISSUES (%d) ==="%len(issues))
for s,m_,o in issues: print("[%s] %s   <owner %s>"%(s,m_,o))
print("\n=== NOTES ===")
for n_ in notes[:3]: print(" ",n_)
print(" (+%d more publication_chunk notes)"%max(0,len(notes)-3))
