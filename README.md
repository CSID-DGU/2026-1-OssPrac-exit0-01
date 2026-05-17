# 🚀 2026-1-OssPrac-exit0-01

> 2026년 1학기 오픈소스소프트웨어실습 | 동국대학교 정보통신공학과

---

## 👥 팀 소개

| 이름 | 학번 | 역할 | GitHub |
|------|------|------|--------|
| 김보성 | 2022xxxxxx | Coordinator — 팀 진행, 회의 준비, 합의 유도 | [@BoseongKim02](https://github.com/BoseongKim02) |
| 한규민 | 2022xxxxxx | Recorder — 기록 및 자료 배포 | [@hgm0827](https://github.com/hgm0827) |
| 김현진 | 2024xxxxxx | Gatekeeper & Timer — 주제 이탈 방지, 일정 관리 | [@guswls-714](https://github.com/guswls-714) |

---

## 📁 프로젝트 구조

```
2026-1-OssPrac-exit0-01/
├── Subject3_1/                  # 팀과제 3-1: Flask 학생 정보 입력 웹
│   ├── ex4.py                   # Flask 메인 서버
│   └── templates/
│       ├── input.html           # 학생 정보 입력 폼
│       └── result.html          # 입력 결과 출력 페이지
│
├── Subject3_2/                  # 팀과제 3-2 & 4: 팀 소개 웹 + Docker
│   ├── team.py                  # Flask 메인 서버
│   ├── Dockerfile               # Docker 이미지 빌드 설정
│   ├── docker-compose.yml       # Docker Compose 설정
│   └── templates/
│       ├── index.html           # 팀 메인 소개 페이지
│       ├── input.html           # 학생 정보 입력 폼
│       ├── result.html          # 입력 결과 출력 페이지
│       └── contact.html         # 팀원 상세 정보 페이지
│
├── LICENSE
└── README.md
```

---

## 📌 과제 내용

### Subject 3-1 — Flask 학생 정보 입력 웹
Flask를 이용해 학생 정보(이름, 학번, 성별, 전공, 프로그래밍 언어)를 입력받고 결과 페이지에 출력하는 웹 애플리케이션을 구현했습니다.

**팀원별 담당 모듈**
- 김보성: Name, Student Number (기본 필드)
- 한규민: Gender 라디오 버튼
- 김현진: Programming Languages 체크박스

### Subject 3-2 — 팀 소개 웹페이지
Bootstrap 기반의 팀 소개 웹페이지를 제작했습니다.

**주요 기능**
- 팀원 카드 UI (이름, 역할, 학과, 기술 스택)
- 다크모드 지원
- AOS 애니메이션 적용
- 팀원 상세 페이지 (`/member/<id>`)

### Subject 4 — Docker 활용 팀 소개 웹 구축
Subject 3-2 웹을 Docker로 컨테이너화하여 배포했습니다.

**기술 스택**

| 항목 | 내용 |
|------|------|
| Base Image | `python:3.11-slim` |
| Web Framework | Flask |
| Frontend | Bootstrap 5, HTML/CSS |
| Container | Docker, Docker Compose |
| Registry | Docker Hub |

---

## 🌐 웹 페이지 미리보기

### 메인 팀 소개 페이지
> `localhost:5000` 접속 시 확인 가능

### 팀원 상세 페이지
> `localhost:5000/member/<id>` 접속 시 확인 가능

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
# http://localhost:5000
```

---

## 🔗 관련 링크

- **GitHub Repository**: [CSID-DGU/2026-1-OssPrac-exit0-01](https://github.com/CSID-DGU/2026-1-OssPrac-exit0-01)
- **Docker Hub**: [guswls714/oss-team](https://hub.docker.com/r/guswls714/oss-team)