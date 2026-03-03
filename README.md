# FastAPI Users CRUD Example

FastAPI와 SQLAlchemy ORM을 사용한 사용자(User) CRUD API 실습 프로젝트입니다.  
Dependency Injection 기반 세션 관리와 BackgroundTasks를 활용한 비동기 작업 처리까지 포함되어 있습니다.

---

## Features

- SQLite + SQLAlchemy ORM 연동
- 사용자 CRUD API 구현
- Dependency Injection 기반 DB 세션 관리
- Pydantic Response Model 적용
- BackgroundTasks를 활용한 회원가입 후 이메일 전송 처리
- Swagger 자동 문서화

---

## Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

---

## Project Structure

```
.
├── main.py
├── models.py
├── schema.py
├── db_connection.py
├── test.db
├── session.py
├── typehint.db
└── README.md
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
pip install fastapi uvicorn sqlalchemy
```

---

## Run Server

```bash
uvicorn main:app --reload
```

또는

```bash
fastapi dev main.py
```

---

## API Endpoints

### 1. 전체 사용자 조회

```
GET /users
```

---

### 2. 회원가입

```
POST /users/sign-up
```

#### Request Body

```json
{
  "name": "alex",
  "age": 20
}
```

회원가입 후 BackgroundTasks를 통해 이메일 전송 작업이 비동기로 실행됩니다.

---

### 3. 단일 사용자 조회

```
GET /users/{user_id}
```

---

### 4. 사용자 정보 수정 (PATCH)

```
PATCH /users/{user_id}
```

#### Request Body (부분 수정 가능)

```json
{
  "name": "new_name"
}
```

---

### 5. 사용자 삭제

```
DELETE /users/{user_id}
```

---

## API Documentation

서버 실행 후 Swagger UI에서 확인:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## Learning Goals

- FastAPI 기본 라우팅 이해
- SQLAlchemy ORM 사용법 이해
- Dependency Injection 개념 학습
- Response Model 직렬화 구조 이해
- BackgroundTasks 동작 원리 이해