# -*- coding: utf-8 -*-
import json,os,re
D="/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch06"
L=lambda f: json.load(open(os.path.join(D,f),encoding="utf-8"))
base=L("05_with_content.json"); auth=L("12_authoring.json"); pub=L("16_publication.json")
A={t["topic_id"]:t for t in auth["topics"]}
P={t["topic_id"]:t for t in pub["topics"]}
fields={}
for m in base["modules"]:
  for s in m["segments"]:
    for t in s["topics"]:
      tid=t["topic_id"]; a=A[tid]; p=P[tid]; acc=[]
      acc.append(("topic_name",t["topic_name"]))
      for k in ("explanation","real_life_example","brief_summary","summary","detailed_summary"): acc.append((k,a[k]))
      for i,x in enumerate(a["concept_bullets"]): acc.append(("concept_bullets[%d]"%i,x))
      for i,x in enumerate(a["important_points"]): acc.append(("important_points[%d]"%i,x))
      for i,x in enumerate(t["key_terms"]): acc.append(("key_terms[%d]"%i,x))
      for q in a["recall_questions"]: acc.append((q["id"]+".prompt",q["prompt"])); acc.append((q["id"]+".answer",q["answer"]))
      for c in a["concepts"]:
        for i,b in enumerate(c["content"]):
          if b["type"]=="paragraph": acc.append((c["concept_id"]+".content[%d]"%i,b["text"]))
          else:
            for j,it in enumerate(b["items"]): acc.append((c["concept_id"]+".content[%d].items[%d]"%(i,j),it))
      acc.append(("publication_text",p["publication_text"]))
      for x in p["concept_publication"]: acc.append(("cp %s[%d]"%(x["concept_id"],x["content_index"]),x["publication_text"]))
      for sd in a.get("shabdarth",[]): acc.append(("shabdarth",sd["shabd"]+" — "+sd["arth"]))
      for v in a.get("vyakaran",[]): acc.append(("vyakaran",v.get("bindu","")+" | "+v.get("udaharan","")+" | "+v.get("note","")))
      fields[tid]=acc

pats={
 "craft label": r"સજીવારોપણ|ઉપમા|અલંકાર|રૂપક|છંદ|પ્રાસ",
 "tacked-on બોધ / directive": r"જોઈએ|આ પાઠ આપણને શીખવે|શીખવે છે|બોધ",
 "imperative to child (વાવો/રાખો/કરો)": r"વૃક્ષો વાવો|સફાઈ રાખો|જતન કરો|સંભાળ રાખો",
 "printed-wrong ર/ળ exercise forms": r"મરવા|સીતાફર|મોકરાશ|પીપરા|સાંભરીને|ભેરા|મેરો|વરતાં|કઠોર",
 "generalised exam claim": r"ઝળહળતી સફળતા|સારાં પરિણામ|પરીક્ષામાં",
 "judging word on villagers": r"બેદરકાર|આળસુ|બેજવાબદાર|સ્વાર્થી",
 "numeral/derived count": r"[0-9૦-૯]|ટકા|બાદ",
}
for tid,acc in fields.items():
    for label,txt in acc:
        for pn,pat in pats.items():
            for mo in re.finditer(pat,txt):
                print("HIT [%s] %s :: %s :: ...%s..."%(pn,tid,label,txt[max(0,mo.start()-45):mo.end()+45]))
print("---- both-voices check ----")
for tid in ("M1.S1.T1","M2.S3.T6"):
    e=A[tid]["explanation"]
    print(tid,"પુરુષોત્તમભાઈ" in e,"સવજીભાઈ" in e)
print("---- proper nouns invented? (place/country names) ----")
alltext=" ".join(t for acc in fields.values() for _,t in acc)
for w in ["ગુજરાત","અમદાવાદ","સૌરાષ્ટ્ર","કચ્છ","ભારત","અમેરિકા","આફ્રિકા","લંડન","જિલ્લો","રાજ્ય"]:
    if w in alltext: print("  present:",w)
print("---- silent persons given lines? ----")
for w in ["શિવરામકાકા","સરતાનકાકા","સુશીલાબેન","નારાયણભાઈ","શ્રવણભાઈ","ભૂરાભાઈ"]:
    hits=[(tid,l) for tid,acc in fields.items() for l,t in acc if w in t]
    print("  ",w,len(hits),hits[:4])
