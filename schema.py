from pydantic import BaseModel


# 회원가입 요청 본문(Request Body)의 데이터 형태
class UserSignUpRequest(BaseModel):
    name: str  # 필수값
    age: int | None = None


# python의 None은 swagger UI에서 JSON 형태로 변환되어 null로 출력된다.


# 회원가입 응답 본문의 데이터 형태
class UserResponse(BaseModel):
    id: int
    name: str
    age: int | None

    class Config:
        from_attributes = True


# 사용자 정보 수정 요청 본문
class UserUpdateRequest(BaseModel):
    name: str | None = None
    age: int | None = None


# 부분 수정(patch)
# 1) name만 수정하는 경우
# 2) age만 수정하는 경우
# 3) name, age 모두 수정하는 경우
