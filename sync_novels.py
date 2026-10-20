#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_novels.py
각 소설 폴더(<slug>/<slug>_threads.md 및 <slug>/<slug>_climax.jpg)를 읽어
랜딩 페이지(index.html)에서 사용하는 novels.json을 자동으로 생성합니다.
"""

import json
import pathlib
import re
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parent

ORDER_META = {
    "memory_auditor": {
        "order": 1,
        "category": "mystery",
        "date": "2026-10-20",
        "badge": "SF 추리·반전",
    },
    "auto_connect": {
        "order": 2,
        "category": "mystery",
        "date": "2026-10-18",
        "badge": "현실 밀착 스릴러",
    },
    "behind_the_wall": {
        "order": 3,
        "category": "mystery",
        "date": "2026-10-16",
        "badge": "현실 밀착 미스터리",
    },
    "carrot_appliance": {
        "order": 4,
        "category": "catharsis",
        "date": "2026-10-19",
        "badge": "일상 사이다·반전",
    },
    "doorbell_11pm": {
        "order": 5,
        "category": "warm",
        "date": "2026-10-19",
        "badge": "일상 반전·감동",
    },
    "mom_shoes": {
        "order": 6,
        "category": "warm",
        "date": "2026-10-19",
        "badge": "가족 휴먼 드라마",
    },
}

STEP_NAMES = ["기(起)", "승(承)", "전(轉)", "결(結)"]


def infer_category(genre_text: str) -> str:
    if any(k in genre_text for k in ["사이다", "블랙코미디", "공감극"]):
        return "catharsis"
    if any(k in genre_text for k in ["감동", "가족", "휴먼", "힐링"]):
        return "warm"
    return "mystery"


def parse_novel(folder: pathlib.Path) -> dict | None:
    slug = folder.name
    md_file = folder / f"{slug}_threads.md"
    if not md_file.exists():
        return None

    raw = md_file.read_text(encoding="utf-8")

    # 1. 제목 추출
    title_match = re.search(r"^#\s+(.+?)(?:\s*—|\s*$)", raw, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else slug

    # 2. 장르 추출
    genre_match = re.search(r"^>\s*장르:\s*(.+?)(?:\s*/|$)", raw, re.MULTILINE)
    genre = genre_match.group(1).strip() if genre_match else "창작 단편"

    # 3. 기승전결 4화 텍스트 블록 추출
    blocks = re.findall(r"```text\s*([\s\S]*?)\s*```", raw)
    episodes = []

    for idx, block in enumerate(blocks):
        block_text = block.strip()
        lines = block_text.splitlines()
        ep_title = f"{idx + 1}화"
        body_lines = lines

        if lines and re.match(r"^\[(\d+화[^\]]*)\]\s*(.*)$", lines[0]):
            m = re.match(r"^\[(\d+화[^\]]*)\]\s*(.*)$", lines[0])
            ep_label = m.group(1).strip()
            ep_sub = m.group(2).strip()
            ep_title = f"[{ep_label}] {ep_sub}" if ep_sub else f"[{ep_label}]"
            body_lines = lines[1:]

        body_text = "\n".join(body_lines).strip()
        step_label = STEP_NAMES[idx] if idx < len(STEP_NAMES) else f"{idx + 1}화"

        episodes.append(
            {
                "number": idx + 1,
                "step": step_label,
                "title": ep_title,
                "body": body_text,
                "rawCopy": block_text,
                "charCount": len(block_text),
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
            "badge": genre.split("/")[0].strip(),
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
