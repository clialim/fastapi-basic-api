from fastapi import FastAPI, Path, Query, HTTPException

app = FastAPI()

"""서버에 GET /hello 요청이 들어오면, root_handler를 실행한다.
@app.get("/hello")
def hello_handler():
    return {"ping": "pong"}
"""

users = [
    {"id": 1, "name": "alex"},
    {"id": 2, "name": "bob"},
    {"id": 3, "name": "chris"},
]


# 전체 사용자 조회 APIs
@app.get("/users")
def get_users_handler():
    return users


# 회원 검색 API
# Query Parameter -> ?key=value 형태로 Path 뒤에 붙는 값
# 데이터 조회시 부가 조건을 명시(필터링, 정렬, 검색, 페이지네이션 등)
@app.get("/users/search")
def search_user_handler(
    name: str = Query(..., min_length=2),  # (...) = 필수값 default
    age: int = Query(20, ge=1),  # (None) = 선택값 optional
):
    """http://127.0.0.1:8000/users/search?name=alex
    위와 같이 age가 없으면 age 부분은 null로 출력됨
    name은 필수이기 때문에 없으면 missing 에러 발생"""
    # name이라는 key로 넘어오는 Query Parameter 값을 사용하겠다
    # GET 127.0.0.1:8000/users/search?name=alex
    return {"name": name, "age": age}


# 단일 사용자 조회 API
# Path(경로) + Paraneter(매개변수) -> 동적으로 바뀌는 값을 한번에 처리
# Path Parameter에 type hint 추가하면 -> 명시한 타입에 맞는지 검사 & 보장


# ?field = id -> id값만 반환
# ?field = name -> name값만 반환
# 없으면 -> id, name 반환
@app.get("/users/{user_id}")
def get_user_handler(  # id가 없으면 name만 나오게 하고, name이 없으면 id가 나오게 하기 위해 Query(None)을 사용
    user_id: int = Path(..., ge=1, description="사용자의 ID"),
    field: str = Query(None, description="출력할 필드 선택 (id 또는 name)"),
):
    for user in users:
        if user["id"] == user_id:
            if field in ("id", "name"):
                return {field: user[field]}
            return user

    raise HTTPException(status_code=404, detail="User not found")


"""실습
GET /items/{item_name}
item_name: str & 최대 글자수 (max_length) 6
# 응답 형식: {"item_name": ...}"""


@app.get("/items/{item_name}")
def get_item_handler(item_name: str = Path(..., max_length=6)):
    return {"item_name": item_name}


""" Query Parameter
?key = value 형태로 Path 뒤에 붙는 값
대아토 조회시 부가 조건을 명시(필터링, 정렬, 검색, 페이지네이션 등)
"""
