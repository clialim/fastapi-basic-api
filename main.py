from sqlalchemy.orm import Session
from fastapi import FastAPI, Path, Query, Body, status, HTTPException, Depends
from sqlalchemy import select
from db_connection import SessionFactory, get_session
from models import User
from schema import UserSignUpRequest, UserResponse, UserUpdateRequest

app = FastAPI()


# 전체 사용자 조회 APIs
@app.get(
    "/users",
    status_code=status.HTTP_200_OK,
    response_model=list[UserResponse],
)
def get_users_handler(
    # 요청이 시작 -> session이 생성
    # 응답 반환 -> session.close()
    session=Depends(get_session),
):
    # stmt = statement(구문) -> SELECT * FROM user
    stmt = select(User)
    result = session.execute(stmt)

    users = result.scalars().all()
    return users


# 회원가입 API
@app.post("/users/sign-up", response_model=UserResponse)
def sign_up_handler(
    body: UserSignUpRequest,
    session: Session = Depends(get_session),
):
    new_user = User(name=body.name, age=body.age)

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


# 회원 검색 API
# Query Parameter -> ?key=value 형태로 Path 뒤에 붙는 값
# 데이터 조회시 부가 조건을 명시(필터링, 정렬, 검색, 페이지네이션 등)
@app.get(
    "/users/search",
    status_code=status.HTTP_200_OK,
    response_model=UserResponse,
)
def search_user_handler(
    name: str = Query(..., min_length=2),
    age: int = Query(20, ge=1),
):
    return {"id": 0, "name": name, "age": age}


# 단일 사용자 조회 API
# Path(경로) + Paraneter(매개변수) -> 동적으로 바뀌는 값을 한번에 처리
# Path Parameter에 type hint 추가하면 -> 명시한 타입에 맞는지 검사 & 보장
# ?field = id -> id값만 반환
# ?field = name -> name값만 반환
# 없으면 -> id, name 반환
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user_handler(
    user_id: int,
    session: Session = Depends(get_session),
):
    stmt = select(User).where(User.id == user_id)
    result = session.execute(stmt)
    user = result.scalar()

    if user is None:
        raise HTTPException(status_code=404, detail="존재하지 않는 사용자 ID입니다.")

    return user


# 사용자 정보 수정 API
# Put -> {name, age} 한번에 교체
# Patch -> name | age 하나씩 교체
@app.patch("/users/{user_id}", response_model=UserResponse)
def update_user_handler(
    user_id: int,
    body: UserUpdateRequest,
    session: Session = Depends(get_session),
):
    stmt = select(User).where(User.id == user_id)
    result = session.execute(stmt)
    user = result.scalar()

    if user is None:
        raise HTTPException(status_code=404, detail="존재하지 않는 사용자 ID입니다.")

    if body.name is not None:
        user.name = body.name
    if body.age is not None:
        user.age = body.age

    session.commit()
    session.refresh(user)

    return user


# 사용자 삭제(회원탈퇴) API
@app.delete("/users/{user_id}", status_code=204)
def delete_user_handler(
    user_id: int,
    session: Session = Depends(get_session),
):
    stmt = select(User).where(User.id == user_id)
    result = session.execute(stmt)
    user = result.scalar()

    if user is None:
        raise HTTPException(status_code=404, detail="존재하지 않는 사용자 ID입니다.")

    session.delete(user)
    session.commit()


"""실습
GET /items/{item_name}
item_name: str & 최대 글자수 (max_length) 6
# 응답 형식: {"item_name": ...}"""


@app.get("/items/{item_name}")
def get_item_handler(item_name: str = Path(..., max_length=6)):
    return {"item_name": item_name}


""" Query Parameter
?key = value 형태로 Path 뒤에 붙는 값
데이터 조회시 부가 조건을 명시(필터링, 정렬, 검색, 페이지네이션 등)
"""
