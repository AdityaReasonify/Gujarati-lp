import json
order=["t1","t2","t3","t4","t5","t6","t7","t8","t9"]
topics=[json.load(open(f+".json")) for f in order]
out={"tier":"ધોરણ","grade":6,
     "topics":topics,
     "modules":json.load(open("modules.json")),
     "notes":json.load(open("notes.json"))}
p="/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch02/12_authoring.json"
json.dump(out,open(p,"w"),ensure_ascii=False,indent=1)
print("written",p)
