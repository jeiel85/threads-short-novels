# 📖 네 컷 소설관 (Threads Short Novels)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-d97742.svg)](https://creativecommons.org/licenses/by/4.0/deed.ko)
[![Format: 4-Cut Card News](https://img.shields.io/badge/Format-기승전결%204화%20%2B%20클라이맥스%20컷신-1b1a18.svg)](https://jeiel85.github.io/threads-short-novels/)

> **기(起)·승(承)·전(轉)·결(結) 네 페이지의 글과 마지막 한 장의 클라이맥스 컷신으로 읽는 숏폼 소설 아카이브**
>
> 🌐 **웹 카드뉴스 리더로 바로 읽기:** [**https://jeiel85.github.io/threads-short-novels/**](https://jeiel85.github.io/threads-short-novels/)

---

## ✨ 프로젝트 소개

**네 컷 소설관**은 스레드(Threads) 타래 연재에 최적화된 **500자 이내 × 4화(기승전결)** 호흡의 창작 단편 소설들을 모아둔 오픈 아카이브입니다.

- **투트랙(Two-Track) 퍼블리싱**:
  1. **Threads 연재**: 각 화 `text` 블록을 그대로 복사해 1화당 1게시물(총 4게시물)로 타래 연재 + 마지막 4화에 클라이맥스 컷신 첨부
  2. **웹 카드뉴스 리더 (`index.html`)**: 방문자가 웹에서 카드를 클릭해 기·승·전·결 1페이지씩 넘겨보며 읽고 마지막 페이지에서 클라이맥스 컷신을 감상

---

## 📚 수록 작품 목록

| # | 작품명 | 장르 | 구성 | 원고 보기 | 웹 리더 바로가기 |
| :-: | :--- | :--- | :-: | :-: | :-: |
| 01 | **기억 감사관** | SF 추리·반전 스릴러 | 기승전결 4화 + 컷신 | [원고](./memory_auditor/memory_auditor_threads.md) | [카드뉴스 읽기](https://jeiel85.github.io/threads-short-novels/#memory_auditor) |
| 02 | **자동 연결** | 현실 밀착 미스터리·스릴러 | 기승전결 4화 + 컷신 | [원고](./auto_connect/auto_connect_threads.md) | [카드뉴스 읽기](https://jeiel85.github.io/threads-short-novels/#auto_connect) |
| 03 | **벽 뒤의 지도** | 현실 밀착 미스터리·스릴러 | 기승전결 4화 + 컷신 | [원고](./behind_the_wall/behind_the_wall_threads.md) | [카드뉴스 읽기](https://jeiel85.github.io/threads-short-novels/#behind_the_wall) |
| 04 | **당근마켓 S급 공기청정기** | 일상 사이다·반전 공감극 | 기승전결 4화 + 컷신 | [원고](./carrot_appliance/carrot_appliance_threads.md) | [카드뉴스 읽기](https://jeiel85.github.io/threads-short-novels/#carrot_appliance) |
| 05 | **밤 11시의 초인종** | 일상 반전·감동 휴먼 드라마 | 기승전결 4화 + 컷신 | [원고](./doorbell_11pm/doorbell_11pm_threads.md) | [카드뉴스 읽기](https://jeiel85.github.io/threads-short-novels/#doorbell_11pm) |
| 06 | **엄마 구두 속의 비밀** | 가족 휴먼 드라마 | 기승전결 4화 + 컷신 | [원고](./mom_shoes/mom_shoes_threads.md) | [카드뉴스 읽기](https://jeiel85.github.io/threads-short-novels/#mom_shoes) |

---

## 📐 표준 작품 구조 (1 Novel = 1 Folder)

모든 작품은 아래와 같이 **개별 폴더 1개 = 마크다운 원고 1개 + 클라이맥스 컷신 1장**의 통일된 규칙으로 관리됩니다.

```text
📦 threads-short-novels
 ┣ 📂 memory_auditor/
 ┃ ┣ 📄 memory_auditor_threads.md   # 기·승·전·결 4화 본문 (각 화 500자 이내)
 ┃ ┗ 🖼️ memory_auditor_climax.jpg   # 4화 마지막에 노출되는 클라이맥스 컷신
 ┣ 📂 auto_connect/
 ┃ ┣ 📄 auto_connect_threads.md
 ┃ ┗ 🖼️ auto_connect_climax.jpg
 ┣ 📂 behind_the_wall/
 ┃ ┣ 📄 behind_the_wall_threads.md
 ┃ ┗ 🖼️ behind_the_wall_climax.jpg
 ┣ 📂 carrot_appliance/
 ┃ ┣ 📄 carrot_appliance_threads.md
 ┃ ┗ 🖼️ carrot_appliance_climax.jpg
 ┣ 📂 doorbell_11pm/
 ┃ ┣ 📄 doorbell_11pm_threads.md
 ┃ ┗ 🖼️ doorbell_11pm_climax.jpg
 ┣ 📂 mom_shoes/
 ┃ ┣ 📄 mom_shoes_threads.md
 ┃ ┗ 🖼️ mom_shoes_climax.jpg
 ┣ 📄 index.html                    # 카드뉴스형 웹 리더 랜딩 페이지
 ┣ 📄 novels.json                   # 랜딩 페이지용 자동 생성 메타데이터
 ┣ 📄 sync_novels.py                # 마크다운 → novels.json 자동 동기화 스크립트
 ┗ 📄 LICENSE                       # CC BY 4.0 라이선스
```

### 새 작품 추가 방법
1. `<slug>/<slug>_threads.md` (기승전결 4화 본문) 및 `<slug>/<slug>_climax.jpg` (클라이맥스 컷신 1장) 생성
2. 로컬에서 `python sync_novels.py` 실행 (또는 `main` 브랜치 푸시 시 GitHub Actions가 자동 동기화 및 배포)

---

## 📜 라이선스 (License)

본 저장소에 수록된 모든 창작 소설 본문과 삽화 이미지는 **[크리에이티브 커먼즈 저작자 표시 4.0 국제 라이선스 (CC BY 4.0)](./LICENSE)**에 따라 보호됩니다.

- **출처 및 저작자(`jeiel85`, 본 저장소 또는 랜딩 페이지 링크)를 명시**하는 조건으로 자유롭게 공유·인용·재가공하실 수 있습니다.
