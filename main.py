from fastapi import FastAPI

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
