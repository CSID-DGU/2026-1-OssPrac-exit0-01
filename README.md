<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:4F46E5,100:7C3AED&height=200&section=header&text=exit0&fontSize=90&fontColor=ffffff&animation=fadeIn" />
</div>

<div align="center">

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FCSID-DGU%2F2026-1-OssPrac-exit0-01&count_bg=%234F46E5&title_bg=%237C3AED&icon=github.svg&icon_color=%23FFFFFF&title=방문자&edge_flat=false)](https://hits.seeyoufarm.com)

**2026년 1학기 오픈소스소프트웨어실습 | 동국대학교 정보통신공학과**

</div>

---

## 👥 팀원 소개

<div align="center">

| 이름 | 학번 | 역할 | GitHub |
|:----:|:----:|:----:|:------:|
| 김보성 | 2022xxxxxx | 🎯 Coordinator | [@BoseongKim02](https://github.com/BoseongKim02) |
| 한규민 | 2022xxxxxx | 📝 Recorder | [@hgm0827](https://github.com/hgm0827) |
| 김현진 | 2024xxxxxx | ⏱️ Gatekeeper & Timer | [@guswls-714](https://github.com/guswls-714) |

</div>

---

## 🛠️ 기술 스택

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

</div>

---

## 📁 프로젝트 구조

```
2026-1-OssPrac-exit0-01/
├── 📂 Subject3_1/                  # 팀과제 3-1: Flask 학생 정보 입력 웹
│   ├── 🐍 ex4.py                   # Flask 메인 서버
│   └── 📂 templates/
│       ├── 🌐 input.html           # 학생 정보 입력 폼
│       └── 🌐 result.html          # 입력 결과 출력 페이지
│
├── 📂 Subject3_2/                  # 팀과제 3-2 & 4: 팀 소개 웹 + Docker
│   ├── 🐍 team.py                  # Flask 메인 서버
│   ├── 🐳 Dockerfile               # Docker 이미지 빌드 설정
│   ├── 🐳 docker-compose.yml       # Docker Compose 설정
│   └── 📂 templates/
│       ├── 🌐 index.html           # 팀 메인 소개 페이지
│       ├── 🌐 input.html           # 학생 정보 입력 폼
│       ├── 🌐 result.html          # 입력 결과 출력 페이지
│       └── 🌐 contact.html         # 팀원 상세 정보 페이지
│
├── 📄 LICENSE
└── 📄 README.md
```

---

## 📌 과제 내용

### 📝 Subject 3-1 — Flask 학생 정보 입력 웹

Flask를 이용해 학생 정보를 입력받고 결과 페이지에 출력하는 웹 애플리케이션입니다.

<div align="center">

| 팀원 | 담당 모듈 |
|:----:|:--------:|
| 김보성 | Name, Student Number (기본 필드) |
| 한규민 | Gender 라디오 버튼 |
| 김현진 | Programming Languages 체크박스 |

</div>

### 🌐 Subject 3-2 — 팀 소개 웹페이지

Bootstrap 기반의 팀 소개 웹페이지를 제작했습니다.

- ✅ 팀원 카드 UI (이름, 역할, 학과, 기술 스택)
- ✅ 다크모드 지원
- ✅ AOS 애니메이션 적용
- ✅ 팀원 상세 페이지 (`/member/<id>`)

### 🐳 Subject 4 — Docker 활용 팀 소개 웹 구축

Subject 3-2 웹을 Docker로 컨테이너화하여 Docker Hub에 배포했습니다.

<div align="center">

| 항목 | 내용 |
|:----:|:----:|
| Base Image | `python:3.11-slim` |
| Web Framework | Flask |
| Frontend | Bootstrap 5 |
| Container | Docker, Docker Compose |
| Registry | Docker Hub (`guswls714/oss-team`) |

</div>

---

## 🐳 Docker 실행 방법

```bash
# 1. 레포지토리 클론
git clone https://github.com/CSID-DGU/2026-1-OssPrac-exit0-01.git
cd 2026-1-OssPrac-exit0-01/Subject3_2

# 2. Docker 이미지 빌드
docker compose build

# 3. 컨테이너 실행
docker compose up -d

# 4. 브라우저에서 접속
# 👉 http://localhost:5000
```

---

## 🔗 관련 링크

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/CSID-DGU/2026-1-OssPrac-exit0-01)
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-guswls714%2Foss--team-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/r/guswls714/oss-team)

</div>

---

## 🎯 Commit Convention

<div align="center">

| 태그 | 설명 |
|:----:|:----:|
| `feat` | 새로운 기능 추가 |
| `fix` | 버그 수정 |
| `docs` | 문서 수정 |
| `style` | 코드 포맷팅, 세미콜론 누락 |
| `refactor` | 코드 리팩토링 |
| `chore` | 빌드 업무 수정, 패키지 매니저 수정 |

</div>

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:7C3AED,100:4F46E5&height=100&section=footer" />
</div>