#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Std-6 Gujarati logical-plan upload via the LP2 API only (no DB writes).

    python3 scratch/upload6.py --dry-run      # show what would be sent
    python3 scratch/upload6.py                # fix + upload + read back

Reads chapter_master_id from upload_reference/chapter_master_map.json. Refuses to upload any
chapter whose id is null -- ids are never invented (phase2_contract rule, VERIFY-2).

Fixes applied to a COPY under _upload/ (originals are never mutated):
  * board/subject segments -> cbse_eng_guj6_chN   (master records: boardId 1 CBSE, languageId 1 English;
    matches the cbse_eng_hindi6_ch1 precedent for a language subject)
  * publication_id  1 (CBSE, unchanged)
  * chapter_master_id  null -> the mapped id
"""
import argparse, json, os, subprocess, sys, io, time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = "/Users/aditya/Downloads/Gujarati-lp"
PACK = os.path.join(ROOT, "gujarati-lp")
OUT  = os.path.join(PACK, "output6")
STAGE = os.path.join(OUT, "_upload")
MAP  = os.path.join(PACK, "upload_reference", "chapter_master_map.json")
BASE = "https://staging.singularity-learn.com/agentapi"
UPLOAD = BASE + "/api/lp2/learning-plans/upload?activate=true"
FETCH  = BASE + "/api/lp2/learning-plans/chapter/%s?include_json=true"

MEDIUM, BOARD, PUBLICATION_ID = "eng", "cbse", 1


def curl(args, timeout=180):
    p = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--chapters", default="1-15")
    a = ap.parse_args()

    lo, hi = (a.chapters.split("-") + [a.chapters])[:2]
    todo = range(int(lo), int(hi) + 1)

    cmap = json.load(open(MAP, encoding="utf-8"))
    os.makedirs(STAGE, exist_ok=True)

    missing = [n for n in todo
               if (cmap.get("cbse_eng_guj6_ch%d" % n) or {}).get("chapter_master_id") is None]
    if missing:
        print("REFUSING TO UPLOAD -- chapter_master_id is null for chapters: %s" % list(missing))
        print("Fill upload_reference/chapter_master_map.json from the education DB (VERIFY-2).")
        print("Ids are never invented. Nothing was sent.")
        return 2

    for n in todo:
        key = "cbse_eng_guj6_ch%d" % n
        cmid = cmap[key]["chapter_master_id"]
        src = os.path.join(OUT, "ch%02d" % n, "learning_plan_logical.json")
        d = json.load(open(src, encoding="utf-8"))

        new_cid = "%s_%s_guj6_ch%d" % (BOARD, MEDIUM, n)
        d["chapter_id"] = new_cid
        d["plan_id"] = new_cid + "_v1"
        d["publication_id"] = PUBLICATION_ID
        d["board"] = BOARD
        d["chapter_master_id"] = cmid

        dst = os.path.join(STAGE, "ch%02d_logical.json" % n)
        with open(dst, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)

        print("ch%02d  %-26s cmid=%-5s pub=%s  -> %s" % (n, new_cid, cmid, PUBLICATION_ID, dst))
        if a.dry_run:
            continue

        rc, out, err = curl(["curl", "-s", "--max-time", "180", "-X", "POST", UPLOAD,
                             "-F", "file=@%s;type=application/json" % dst,
                             "-F", "chapter_master_id=%s" % cmid,
                             "-F", "phase=2",
                             "-w", "\nHTTP %{http_code}"])
        print("      upload:", (out or err).strip()[-400:])

        time.sleep(2)
        rc, out, err = curl(["curl", "-s", "--max-time", "120", FETCH % new_cid])
        try:
            body = json.loads(out)
            dd = body["data"]; pl = dd["plan"]
            raw = pl["planJson"]
            if isinstance(raw, str):
                raw = json.loads(raw)
            topics = [t for m in raw["modules"] for sg in m["segments"] for t in sg["topics"]]
            print("      readback: v%s phase=%s active=%s medium=%s subject=%s cmid=%s topics=%d"
                  % (pl["version"], raw.get("phase"), pl["isActive"], dd.get("medium"),
                     dd.get("subject"), dd.get("chapterMasterId"), len(topics)))
        except Exception as e:
            print("      readback FAILED: %s :: %s" % (e, out[:200]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
