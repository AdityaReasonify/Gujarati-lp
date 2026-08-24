# Phase-2 Fetch — reading a plan back out of the DB

> Companion to `reference/phase2_contract.md`, which covers the write path. This file covers the
> read path only. Every shape below was **verified live against staging on 2026-08-07** by
> fetching `cbse_eng_hindi6_ch1`, `cbse_eng_hindi7_ch1` and `cbse_eng_hindi8_ch1`.

There is no direct database access in this pack and none is needed. "The DB" is reached through
one LP2 endpoint, and what it returns is the stored row — the same blob the platform serves to a
child. **Read the server's copy, never the local file**, whenever the question is "what is
actually published?" A plan can assemble perfectly, upload cleanly, and still be wrong on the
server; only a fetch tells you.

## The endpoint

```
GET {base}/api/lp2/learning-plans/chapter/{chapter_id}?include_json=true
```

| | |
|---|---|
| Base (staging) | `https://staging.singularity-learn.com/agentapi` |
| Base (beta) | `https://beta.singularity-learn.com/agentapi` |
| Auth | **none** — send no bearer, no cookie. The agentapi half answers unauthenticated. |
| Missing chapter | `404` with `{"detail": "chapter '…' not found"}` — no `success` envelope |

Two supporting endpoints:

```
GET {base}/api/lp2/learning-plans/chapters      # 369 rows on staging — connectivity sanity check
```

## The envelope — three deep, and that is the trap

```
body
├─ success        true
├─ message
└─ data
   ├─ id                  "cbse_eng_hindi7_ch1"      ← chapter id (not the plan id)
   ├─ name                "माँ, कह एक कहानी"
   ├─ subject, grade, board, medium, textbook, textbookUrl
   ├─ chapterMasterId     247
   ├─ publicationId, publicationName
   └─ plan
      ├─ id               "cbse_eng_hindi7_ch1_v1"   ← plan id = {chapter_id}_v{N}
      ├─ level, version, phase, isActive, isDraft, status, createdAt
      └─ planJson  ← THE PLAN
```

So the plan is `body["data"]["plan"]["planJson"]`. Guessing at `body["data"]["raw_json"]` yields
zero topics and reads as an empty chapter rather than as an error.

Read the version/state off `body["data"]["plan"]` (`version`, `isActive`, `status`), **not** off
`planJson` — the blob's own `version` is what the author intended, the row's is what the server
assigned.

`planJson` came back as a **dict** in every call, but `output/_verify_all.py` defends against a
string. Keep that guard; it costs one line and a JSON-string blob would otherwise crash on
`raw["modules"]`.

```python
raw = pl["planJson"]
if isinstance(raw, str):
    raw = json.loads(raw)
```

**`include_json=true` is not currently load-bearing** — staging returned `planJson` without it.
Send it anyway: `lp_sync` does, the contract documents it, and a default that flips silently would
be invisible until a survey came back empty.

## Chapter ids

`{board}_{medium}_{subject}{grade}_ch{N}` (regex: `config.py: CHAPTER_RE`). For Hindi:

| Class | Chapter id | `chapterMasterId` |
|---|---|---|
| 6 | `cbse_eng_hindi6_ch{N}` | `355 − N` (ch1 = 354) |
| 7 | `cbse_eng_hindi7_ch{N}` | ch1 = 247 |
| 8 | `cbse_eng_hindi8_ch{N}` | ch1 = 292 |

`medium` is `eng` even for Hindi plans.

Note the contract's warning that `chapter_master_id` is "not discoverable from the LP2 API" applies
**before the first upload**. Once a chapter exists, this fetch returns it as `data.chapterMasterId`
— the cheapest way to recover a mapping you have lost, and it is authoritative because it is what
the row actually carries.

## Client A — `lp_sync` (preferred when you are already in that tool)

```python
from lp_sync.api_client import ApiClient

data = ApiClient("https://staging.singularity-learn.com/agentapi").get_chapter("cbse_eng_hindi7_ch1")
if data is None:          # 404 — chapter/plan not uploaded yet
    ...
plan = data["plan"]["planJson"]
```

`get_chapter()` already sends `include_json=true`, maps 404 → `None`, and retries 3× with 2s/4s
backoff. It returns the **`data` dict**, not the whole body.

## Client B — zero-dependency (what every script in this pack uses)

`lp_sync` needs `requests` and its own package root on the path. The survey/verify scripts here
avoid both by borrowing the stdlib helper from the v1 client — it is transport only, so using it
against LP2 carries no v1 semantics:

```python
import sys; sys.path.insert(0, "../../imagebyGPT")
from lp_v1_api import _request           # returns (status, parsed_body)

API = "https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/chapter/%s?include_json=true"
status, body = _request(API % "cbse_eng_hindi7_ch1")
```

Pass **no token**. `_request` supports one because the v1 .NET half needs it; LP2 does not, and
sending v1's bearer/cookie handling here is trap #1 in the contract.

## Copy-paste: fetch a range of chapters with the retry that staging requires

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, json, os, sys, time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "imagebyGPT"))
from lp_v1_api import _request  # noqa: E402

PY = "https://staging.singularity-learn.com/agentapi/api"


def fetch(chapter_id, attempts=3):
    """The data dict, or None when the chapter has no plan on the server."""
    for i in range(attempts):
        try:
            status, body = _request(
                "%s/lp2/learning-plans/chapter/%s?include_json=true" % (PY, chapter_id))
        except Exception:
            time.sleep(3)          # staging DNS, not an API error — see below
            continue
        if status == 404:
            return None
        data = (body or {}).get("data")
        if data and data.get("plan"):
            return data
        time.sleep(3)
    return None


for n in range(1, 11):
    cid = "cbse_eng_hindi7_ch%d" % n
    data = fetch(cid)
    if not data:
        print("ch%-2d  NO PLAN ON SERVER" % n)
        continue
    pl = data["plan"]
    raw = pl["planJson"]
    if isinstance(raw, str):
        raw = json.loads(raw)
    topics = [t for m in raw["modules"] for sg in m["segments"] for t in sg["topics"]]
    media = sum(len(t.get("media", [])) for t in topics)
    print("ch%-2d %-24s v%-2d phase %s active %-5s  topics %2d  media %2d"
          % (n, data["name"], pl["version"], raw.get("phase"), pl["isActive"],
             len(topics), media))
```

The topic walk is always `modules → segments → topics`; media hang off each topic as
`t["media"]`.

## Traps

| # | Trap | What to do |
|---|---|---|
| 1 | Plan nested three deep | `body["data"]["plan"]["planJson"]`. Anything else returns empty, not an error. |
| 2 | Sending auth | Send none. LP2 is unauthenticated; v1's bearer/cookie belongs to the other API. |
| 3 | `getaddrinfo failed` on staging | Random, ~1 in a few dozen calls, **not** an API error. Retry 2–3× before believing any result. |
| 4 | Reading `version` off `planJson` | The server assigns the version. Use `data["plan"]["version"]`. |
| 5 | Trusting a fetch that "worked" | Check `isActive` and `status` too. A superseded draft still returns 200 with a full plan. |
| 6 | Assuming the URLs resolve | `image_url` can 404 while the plan validates perfectly. HEAD every asset — `output7/_verify7.py` does. |
| 7 | Diffing local vs remote naively | The server injects/rewrites `plan_id`, `version`, `chapter_master_id`, `subject_ref_id`, `medium_id`, `_activate`, `created_by`. `config.VOLATILE_TOP_LEVEL_KEYS` is the drop-list. |

## What this endpoint does not give you

- **Older versions.** It serves the active (or latest) plan for a chapter. None of the six LP2
  endpoints this pack uses exposes a version history; recovering a superseded version is not a
  read you can do from here.
- **Search.** There is no query by grade/subject. Enumerate `GET /chapters` and filter client-side,
  or construct ids directly — the id grammar is deterministic, so construction is usually right.
- **Drafts by id.** The chapter route is the only read path in use.

## Existing scripts in this pack that fetch

| Script | What it does |
|---|---|
| `output/_verify_all.py` | Round-trips all 13 class-6 chapters; checks phase, `isActive`, भाषा-बोध coverage. The reference for the correct nesting and the 3× retry. |
| `output7/_verify7.py` | Class-7 read-back plus a HEAD on every `image_url` — catches plans that validate but point at 404s. |
| `output/_where_is_it.py` | Same read across staging **and** beta, to find which environment a plan actually landed in. |
| `output/_verify_collages.py` | Reads back and asserts every media URL sits in `learning_plan_assets`. |

Start from the closest of these rather than writing a fetch from scratch.
