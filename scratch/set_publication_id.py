#!/usr/bin/env python3
"""Set publication_id across a standard's learning plans, then re-validate.

Usage:  python3 scratch/set_publication_id.py <STD> <VALUE> [--apply]

Without --apply it is a DRY RUN: reports what would change and validates nothing.
The value is a decision only the user can make (VERIFY-2):
  1 = what std-6 and 6 of std-7's chapters already carry; validates clean.
  4 = what every GSEB Gujarati-medium row on the live server actually uses.
"""
import json, sys, os, glob, subprocess

ROOT = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp"
URL = "https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate"

def main():
    if len(sys.argv) < 3:
        print(__doc__); return
    std, value = sys.argv[1], int(sys.argv[2])
    apply = "--apply" in sys.argv
    plans = sorted(glob.glob(f"{ROOT}/output{std}/ch*/learning_plan_logical.json"))
    if not plans:
        print(f"  no plans under output{std}"); return
    changed = same = 0
    for p in plans:
        try: d = json.load(open(p, encoding="utf-8"))
        except Exception as e:
            print(f"  {p}: unreadable ({e})"); continue
        cur = d.get("publication_id")
        ch = os.path.basename(os.path.dirname(p))
        if cur == value:
            same += 1; continue
        changed += 1
        print(f"  {ch}: publication_id {cur!r} -> {value}")
        if apply:
            # keep a one-time backup so the edit is reversible
            bak = p + ".pre-pubid"
            if not os.path.exists(bak):
                open(bak, "w", encoding="utf-8").write(open(p, encoding="utf-8").read())
            d["publication_id"] = value
            open(p, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2))
    print(f"\n  {changed} would change, {same} already {value}" if not apply
          else f"\n  {changed} changed, {same} already {value}  (backups: *.pre-pubid)")
    if not apply:
        print("  DRY RUN — re-run with --apply to write, then this script re-validates."); return
    print("\n  re-validating against the live endpoint:")
    clean = fail = 0
    for p in plans:
        ch = os.path.basename(os.path.dirname(p))
        r = subprocess.run(["curl","-s","--max-time","45","-X","POST",URL,"-F",f"file=@{p}"],
                           capture_output=True, text=True)
        try:
            errs = (json.loads(r.stdout) or {}).get("validation_errors") or []
        except Exception:
            print(f"    {ch}: unparseable response"); fail += 1; continue
        if errs: fail += 1; print(f"    {ch}: {len(errs)} error(s) — {str(errs[:1])[:90]}")
        else: clean += 1; print(f"    {ch}: CLEAN")
    print(f"\n  LP2 clean {clean}/{len(plans)}, failing {fail}")

if __name__ == "__main__":
    main()
