#!/usr/bin/env python3
"""Emit ready-to-launch workflow args for a standard, skipping completed chapters."""
import json,subprocess,sys,os
STD=int(sys.argv[1]); CONC=int(sys.argv[2]) if len(sys.argv)>2 else 3
S="/Users/aditya/Downloads/Gujarati-lp/scratch"
subprocess.run(["python3",f"{S}/progress.py",str(STD)],capture_output=True)
p=f"/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output{STD}/progress.json"
d=json.load(open(p))
a=d["resume_args"]; a["concurrency"]=CONC
N=d.get("stage_count",14)   # A15 disabled -> 13; read it, never hardcode
a["chapters"]=[c for c in a["chapters"] if len(c["done"])<N]
print(json.dumps(a))
