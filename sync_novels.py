#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import pathlib
import re
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parent

ORDER_META = {
    "lost_time_office": {
        "order": 1,
        "category": "daily",
        "date": "2026-10-20",
        "badge": "감성 판타지·로맨스",
    },
    "memory_auditor": {
        "order": 2,
        "category": "mystery",
        "date": "2026-10-20",
        "badge": "SF 추리·스릴러",
    },
    "auto_connect": {
        "order": 3,
        "category": "mystery",
        "date": "2026-10-18",
        "badge": "미스터리·스릴러",
    },
    "behind_the_wall": {
        "order": 4,
        "category": "mystery",
        "date": "2026-10-16",
        "badge": "미스터리·스릴러",
    },
    "carrot_appliance": {
        "order": 5,
        "category": "daily",
        "date": "2026-10-19",
        "badge": "일상·공감",
    },
    "doorbell_11pm": {
        "order": 6,
        "category": "daily",
        "date": "2026-10-19",
        "badge": "일상·드라마",
    },
    "mom_shoes": {
        "order": 7,
        "category": "daily",
        "date": "2026-10-19",
        "badge": "일상·드라마",
    },
}


def infer_category(genre_text: str) -> str:
    if any(k in genre_text for k in ["일상", "감동", "가족", "휴먼", "공감", "드라마", "감성", "로맨스"]):
        return "daily"
    return "mystery"


def parse_novel(folder: pathlib.Path) -> dict | None:
    slug = folder.name
    md_file = folder / f"{slug}_threads.md"
    if not md_file.exists():
        return None

    raw = md_file.read_text(encoding="utf-8")

    title_match = re.search(r"^#\s+(.+?)(?:\s*—|\s*$)", raw, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else slug

    genre_match = re.search(r"^>\s*(?:장르:\s*)?(.+?)(?:\s*/|$)", raw, re.MULTILINE)
    genre = genre_match.group(1).strip() if genre_match else "단편"

    blocks = re.findall(r"```text\s*([\s\S]*?)\s*```", raw)
    episodes = []

    for idx, block in enumerate(blocks):
        block_text = block.strip()
        lines = block_text.splitlines()
        ep_title = f"{idx + 1}화"
        body_lines = lines

        if lines and re.match(r"^\[(\d+화[^\]]*)\]\s*(.*)$", lines[0]):
            m = re.match(r"^\[(\d+화[^\]]*)\]\s*(.*)$", lines[0])
            ep_sub = m.group(2).strip()
            ep_title = ep_sub if ep_sub else f"{idx + 1}화"
            body_lines = lines[1:]

        body_text = "\n".join(body_lines).strip()

        episodes.append(
            {
                "number": idx + 1,
                "title": ep_title,
                "body": body_text,
                "rawCopy": block_text,
            }
        )

    hook = ""
    if episodes:
        non_empty = [
            ln.strip() for ln in episodes[0]["body"].splitlines() if ln.strip()
        ]
        if non_empty:
            hook = non_empty[0]

    meta = ORDER_META.get(
        slug,
        {
            "order": 0,
            "category": infer_category(genre),
            "date": date.today().isoformat(),
            "badge": genre,
        },
    )

    return {
        "slug": slug,
        "title": title,
        "genre": genre,
        "badge": meta["badge"],
        "category": meta["category"],
        "date": meta["date"],
        "order": meta["order"],
        "hook": hook,
        "mdPath": f"./{slug}/{slug}_threads.md",
        "climaxImage": f"./{slug}/{slug}_climax.jpg",
        "episodes": episodes,
    }


def main() -> None:
    novels = []
    for sub in sorted(ROOT.iterdir()):
        if sub.is_dir() and not sub.name.startswith("."):
            item = parse_novel(sub)
            if item:
                novels.append(item)

    novels.sort(key=lambda x: (x["order"], x["slug"]))
    out_path = ROOT / "novels.json"
    out_path.write_text(
        json.dumps(novels, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Synced {len(novels)} novels to {out_path.name}")


if __name__ == "__main__":
    main()
