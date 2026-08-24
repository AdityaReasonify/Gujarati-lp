# Phase-2 Fetch — reading a plan back out of the DB

> Companion to `reference/phase2_contract.md`, which covers the write path. This file covers the
> read path only. Every envelope shape below was **verified live against staging on 2026-08-07**
> during the Hindi runs (by fetching `cbse_eng_hindi6_ch1`, `cbse_eng_hindi7_ch1` and
> `cbse_eng_hindi8_ch1`) — the envelope is board-agnostic. The GSEB-specific values (ids,
> `chapterMasterId`, echoed `medium`/`subject`) have NOT been verified yet: re-verify them against
> the first uploaded Gujarati chapter (VERIFY-1/VERIFY-5) before trusting any table in this file
> that is marked provisional.

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
GET {base}/api/lp2/learning-plans/chapters      # 369 rows on staging at last Hindi count — connectivity sanity check
```

For this pack the `/chapters` enumeration is more than a sanity check: it is **VERIFY-1's tool**.
Before the first Gujarati upload, enumerate it and filter client-side for the GSEB board value to
(a) confirm the board/medium segments the server actually uses in existing GSEB rows, and (b) pull
`chapterMasterId` values for any GSEB chapters that already exist. Until the first Gujarati chapter
is uploaded, fetching a `gseb_…gujarati…` chapter id returns `404` — that is expected, not an
error.

## The envelope — three deep, and that is the trap

```
body
├─ success        true
├─ message
└─ data
   ├─ id                  "gseb_eng_gujarati7_ch1"   ← chapter id (not the plan id) — PROVISIONAL form, see below
   ├─ name                "<પ્રકરણનું નામ ગુજરાતી લિપિમાં>"
   ├─ subject, grade, board, medium, textbook, textbookUrl
   ├─ chapterMasterId     <int — TO BE FETCHED, never invented>
   ├─ publicationId, publicationName
   └─ plan
      ├─ id               "gseb_eng_gujarati7_ch1_v1"   ← plan id = {chapter_id}_v{N}
      ├─ level, version, phase, isActive, isDraft, status, createdAt
      └─ planJson  ← THE PLAN
```

So the plan is `body["data"]["plan"]["planJson"]`. Guessing at `body["data"]["raw_json"]` yields
zero topics and reads as an empty chapter rather than as an error.

Read the version/state off `body["data"]["plan"]` (`version`, `isActive`, `status`), **not** off
`planJson` — the blob's own `version` is what the author intended, the row's is what the server
assigned.

The echoed `medium` and `subject` fields on `data` are the cheapest re-verification of the
chapter-id medium slot: after the first upload, read them back and confirm they landed in the
intended DB columns (`subject` = Gujarati; `medium` = whatever VERIFY-1 established). A wrong
medium segment uploads clean and mis-files the plan — the fetch is where it becomes visible.

`planJson` came back as a **dict** in every verified call, but the verify scripts
(`output6/_verify6.py` and siblings) defend against a string. Keep that guard; it costs one line
and a JSON-string blob would otherwise crash on `raw["modules"]`.

```python
raw = pl["planJson"]
if isinstance(raw, str):
    raw = json.loads(raw)
```

**`include_json=true` is not currently load-bearing** — staging returned `planJson` without it.
Send it anyway: `lp_sync` does, the contract documents it, and a default that flips silently would
be invisible until a survey came back empty.

## Chapter ids

`{board}_{medium}_{subject}{grade}_ch{N}` (regex: `config.py: CHAPTER_RE`). For Gujarati the
provisional form is:

> ⚠ **PROVISIONAL (VERIFY-1).** `gseb_eng_gujarati{grade}_ch{N}` — the `eng` medium slot is the
> medium of instruction, NOT the subject language, and it is copied from the Hindi pack's verified
> quirk, not from any GSEB row. It must be confirmed against the live server (enumerate
> `GET /chapters`, inspect existing GSEB rows, read the echoed `medium`) before the first upload.
> A wrong medium segment uploads clean and registers under the wrong DB column — this once
> mis-filed all 23 Hindi plans.

| Std | Chapter id (provisional) | `chapterMasterId` |
|---|---|---|
| 6 | `gseb_eng_gujarati6_ch{N}` | TO BE FETCHED |
| 7 | `gseb_eng_gujarati7_ch{N}` | TO BE FETCHED |
| 8 | `gseb_eng_gujarati8_ch{N}` | TO BE FETCHED |
| 9 | `gseb_eng_gujarati9_ch{N}` | TO BE FETCHED |
| 10 | `gseb_eng_gujarati10_ch{N}` | TO BE FETCHED |

**Never fill this table by arithmetic or analogy.** The Hindi pack's `355 − N` formula was a
verified accident of that corpus and does not transfer. GSEB `chapterMasterId` values come from
exactly two places: the education DB fetch-chapters flow (recorded into
`upload_reference/chapter_master_map.json`), or — the cheapest way to recover a mapping you have
lost — this very endpoint. The contract's warning that `chapter_master_id` is "not discoverable
from the LP2 API" applies **before the first upload**. Once a chapter exists, the fetch returns it
as `data.chapterMasterId`, and it is authoritative because it is what the row actually carries.

## Client A — `lp_sync` (preferred when you are already in that tool)

```python
from lp_sync.api_client import ApiClient

data = ApiClient("https://staging.singularity-learn.com/agentapi").get_chapter("gseb_eng_gujarati7_ch1")
if data is None:          # 404 — chapter/plan not uploaded yet
    ...
plan = data["plan"]["planJson"]
```

`get_chapter()` already sends `include_json=true`, maps 404 → `None`, and retries 3× with 2s/4s
backoff. It returns the **`data` dict**, not the whole body.

## Client B — zero-dependency (what every script in this pack uses)

`lp_sync` needs `requests` and its own package root on the path. The survey/verify scripts here
avoid both by borrowing the stdlib helper from the v1 client — it is transport only, so using it
against LP2 carries no v1 semantics (the Gujarati pack has no v1 corpus, but the helper is just
HTTP):

```python
import sys; sys.path.insert(0, "../../imagebyGPT")
from lp_v1_api import _request           # returns (status, parsed_body)

API = "https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/chapter/%s?include_json=true"
status, body = _request(API % "gseb_eng_gujarati7_ch1")
```

Pass **no token**. `_request` supports one because the v1 .NET half needs it; LP2 does not, and
sending v1's bearer/cookie handling here is trap #1 in the contract.

## Copy-paste: fetch every standard with the retry that staging requires

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, json, os, sys, time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "imagebyGPT"))
from lp_v1_api import _request  # noqa: E402

PY = "https://staging.singularity-learn.com/agentapi/api"

# Chapter counts per standard come from profiles/boards/gseb_gujarati.md — never assume them.
CHAPTERS = {6: 0, 7: 0, 8: 0, 9: 0, 10: 0}   # fill from the board profile


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


for grade in (6, 7, 8, 9, 10):
    for n in range(1, CHAPTERS[grade] + 1):
        cid = "gseb_eng_gujarati%d_ch%d" % (grade, n)
        data = fetch(cid)
        if not data:
            print("std%-2d ch%-2d  NO PLAN ON SERVER" % (grade, n))
            continue
        pl = data["plan"]
        raw = pl["planJson"]
        if isinstance(raw, str):
            raw = json.loads(raw)
        topics = [t for m in raw["modules"] for sg in m["segments"] for t in sg["topics"]]
        media = sum(len(t.get("media", [])) for t in topics)
        print("std%-2d ch%-2d %-24s v%-2d phase %s active %-5s  topics %2d  media %2d"
              % (grade, n, data["name"], pl["version"], raw.get("phase"), pl["isActive"],
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
| 6 | Assuming the URLs resolve | `image_url` can 404 while the plan validates perfectly. HEAD every asset — each `output{N}/_verify{N}.py` does. |
| 7 | Diffing local vs remote naively | The server injects/rewrites `plan_id`, `version`, `chapter_master_id`, `subject_ref_id`, `medium_id`, `_activate`, `created_by`. `config.VOLATILE_TOP_LEVEL_KEYS` is the drop-list. |

## What this endpoint does not give you

- **Older versions.** It serves the active (or latest) plan for a chapter. None of the six LP2
  endpoints this pack uses exposes a version history; recovering a superseded version is not a
  read you can do from here.
- **Search.** There is no query by grade/subject. Enumerate `GET /chapters` and filter client-side
  (this is also how VERIFY-1 confirms the GSEB board/medium segments), or construct ids directly —
  the id grammar is deterministic, so construction is usually right **once VERIFY-1 has fixed the
  segments**; before that, construction is a guess.
- **Drafts by id.** The chapter route is the only read path in use.

## Verify scripts in this pack that fetch

One read-back script per standard, created as that standard's chapters upload. All five follow the
same pattern: round-trip every uploaded chapter of the standard, check `phase`, `isActive` and
ભાષા-બોધ coverage against the correct three-deep nesting with the 3× retry, and HEAD every
`image_url` — catching plans that validate but point at 404s.

| Script | Covers |
|---|---|
| `output6/_verify6.py` | Std 6 chapters |
| `output7/_verify7.py` | Std 7 chapters |
| `output8/_verify8.py` | Std 8 chapters |
| `output9/_verify9.py` | Std 9 chapters |
| `output10/_verify10.py` | Std 10 chapters |

Start from the closest existing one rather than writing a fetch from scratch; the copy-paste block
above is the seed for the first.
