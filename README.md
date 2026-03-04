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
- Async SQLAlchemy (AsyncSession) 기반 비동기 DB 처리
- 사용자 CRUD API 구현 (async/await 적용)

---

## Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy (AsyncSession)
- aiosqlite
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
├── db_connection_async.py
├── test.db
├── create_tables.py
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
---
### 2. requirements.txt 기반 설치

프로젝트 실행 환경 재현을 위해  
requirements.txt 파일을 제공합니다.

```bash
pip install -r requirements.txt
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
## Background Task (회원가입 이메일 비동기 처리)

회원가입 API에서 BackgroundTasks를 사용하여 
이메일 전송 작업을 요청-응답 사이클과 분리하였습니다.

FastAPI는 async endpoint에서도 BackgroundTasks를 지원합니다.
이메일 전송과 같이 I/O가 발생하는 작업을 요청-응답 사이클과 분리하여,
응답 이후 실행되도록 구성하였습니다.


### 적용 이유

- 요청 응답 지연 방지
- 부가 작업을 비동기적으로 처리
- FastAPI의 BackgroundTasks 동작 원리 학습

### 동작 흐름

1. 사용자가 회원가입 요청
2. DB에 사용자 저장
3. 응답 반환
4. 응답 이후 Background Task에서 이메일 전송 실행

### Thread Limiter 설정

anyio의 thread limiter를 조정하여 
threadpool의 최대 스레드 수를 200으로 확장하였습니다.

기본 제한보다 여유 있게 설정하여,
동시 Background Task 실행 시 발생할 수 있는 병목 현상을 완화하도록 구성하였습니다.
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

- FastAPI 라우팅 구조 및 요청-응답 흐름 이해
- Dependency Injection 기반 DB 세션 생명주기 관리
- SQLAlchemy ORM을 활용한 데이터 조회 및 수정 흐름 이해
- Pydantic Response Model을 통한 직렬화 구조 이해
- Sync endpoint의 threadpool 동작 방식 이해
- BackgroundTasks를 활용한 요청-응답 분리 구조 설계
- AsyncSession을 활용한 비동기 DB 처리 구조 이해
- await 기반 이벤트 루프 동작 방식 이해
- Sync vs Async 처리 방식 비교 및 차이점 학습