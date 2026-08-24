#!/usr/bin/env python3
"""Pack integrity check — run before any chapter run.

This pack was ported file by file: the agent numbering keeps deliberate gaps (there are no agents
03 or 06), the genre roster was rebuilt from the GSEB books, and several reference files were
renamed on the way in (gujarati_verbatim.md, teaching_voice_gu.md, gseb_gujarati.md,
gujarati_learning_plan_skeleton.json). Every one of those is a chance for a document to keep
citing a file that no longer exists, or for the index to route at a profile nobody wrote — drift
that stays invisible until an agent is dispatched mid-run and the file is not there. This checks
it mechanically instead of trusting it.

    python check_pack.py
"""

import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

PATH_RE = re.compile(r"\b((?:reference|profiles|schema|agents)/[A-Za-z0-9_./-]+\.(?:md|json))")


def main() -> int:
    files = {p.replace("\\", "/") for p in glob.glob("**/*", recursive=True) if os.path.isfile(p)}
    problems = []

    # 1. every in-pack path mentioned in any doc resolves
    for doc in sorted(glob.glob("**/*.md", recursive=True)):
        text = open(doc, encoding="utf-8").read()
        for ref in sorted(set(PATH_RE.findall(text))):
            if ref not in files:
                problems.append(f"missing file {ref!r}, referenced in {doc}")

    # 2. agent frontmatter name matches its filename, and declares inputs/outputs
    agents = sorted(glob.glob("agents/*.md"))
    if not agents:
        problems.append("no agents found")
    for path in agents:
        text = open(path, encoding="utf-8").read()
        stem = os.path.basename(path)[:-3]
        name = re.search(r"^name:\s*(\S+)", text, re.M)
        if not name:
            problems.append(f"{path}: no frontmatter 'name'")
        elif name.group(1) != stem:
            problems.append(f"{path}: frontmatter name {name.group(1)!r} != filename {stem!r}")
        for key in ("description", "inputs", "outputs"):
            if not re.search(rf"^{key}:", text, re.M):
                problems.append(f"{path}: frontmatter missing {key!r}")

    # 3. the orchestrator dispatches only agents that exist, and every agent is dispatched
    orch = open("orchestrator.md", encoding="utf-8").read()
    declared = {os.path.basename(p)[:-3] for p in agents}
    numbers_in_orch = set(re.findall(r"\bAgents?\s+(\d+)", orch)) | set(
        re.findall(r"\bA(\d+)\b", orch))
    agent_numbers = {s.split("_")[0].lstrip("0") or "0" for s in declared}
    for n in sorted(numbers_in_orch - agent_numbers, key=int):
        problems.append(f"orchestrator dispatches Agent {n}, which has no file")
    for n in sorted(agent_numbers - numbers_in_orch, key=int):
        problems.append(f"agent {n} exists but the orchestrator never dispatches it")

    # 4. the genre index points only at profiles that exist
    idx = open("profiles/genres/_genre_index.md", encoding="utf-8").read()
    # bare filenames only — a path-qualified mention like reference/genre_diagnosis.md
    # is a cross-reference, not a routing target
    for g in sorted(set(re.findall(r"(?<![/\w])([a-z][a-z_]+)\.md", idx))):
        if g == "_genre_index":
            continue
        if f"profiles/genres/{g}.md" not in files:
            problems.append(f"genre index points at missing profile {g}.md")
    for prof in sorted(glob.glob("profiles/genres/*.md")):
        stem = os.path.basename(prof)[:-3]
        if stem != "_genre_index" and stem not in idx:
            problems.append(f"profile {stem}.md exists but the index never routes to it")

    # 5. schemas parse
    for path in sorted(glob.glob("schema/*.json")):
        try:
            json.load(open(path, encoding="utf-8"))
        except Exception as exc:
            problems.append(f"{path}: invalid JSON — {exc}")

    print(f"{len(files)} files, {len(agents)} agents, "
          f"{len(glob.glob('profiles/genres/*.md')) - 1} genre profiles, "
          f"{len(glob.glob('reference/*.md'))} reference files")
    for p in problems:
        print(f"  FAIL {p}")
    print("\n" + ("OK — pack is internally consistent" if not problems
                  else f"{len(problems)} problem(s)"))
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
