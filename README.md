# FastAPI Users Example

FastAPI 기본 라우팅과 간단한 GET API 구현 실습 프로젝트입니다.

## Features

- FastAPI 애플리케이션 생성
- `/users` GET 엔드포인트 구현
- 정적 사용자 리스트 반환

---

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn

---

## Project Structure

```
.
├── main.py
└── .venv (not included in git)
```

---

## Setup

### 1. 가상환경 생성 및 활성화

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. 패키지 설치

```bash
pip install fastapi uvicorn
```

---

## Run Server

```bash
fastapi dev main:app
```

또는

```bash
uvicorn main:app --reload
```

---

## API Endpoints

### GET /users

전체 사용자 목록을 반환합니다.

#### Response

```json
[
  {"id": 1, "name": "alex"},
  {"id": 2, "name": "bob"},
  {"id": 3, "name": "chris"}
]
```

---

## API Docs

서버 실행 후 아래 주소에서 Swagger UI 확인 가능:

- http://127.0.0.1:8000/docs