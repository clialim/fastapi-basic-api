# type hint 사용
name: str = "Alex"
price: float = 10.5
is_active: bool = True

# integer와 float 둘다 가능
score: int | float = 90

# string과 integer 둘다 가능
age: str | int = "10살"
age: str | int = 10


# int+int=int 반환
def add(num1: int, num2: int) -> int:
    return num1 + num2


# list
names = ["Bailey", "Eva", "Melissa"]
names: list = ["Bailey", "Eva", "Melissa"]
names: list[str] = ["Bailey", "Eva", "Melissa"]

scores = [100, 90, 85]
scores: list[int] = [100, 90, 85]

# list에 다양한 typehint 지정
data = ["Bailey", 98, True]
data: list[str | int | bool] = ["Bailey", 98, True]

# dictionary
scores: dict[str, int] = {"Calculus": 100, "Korean": 90, "Biology": 75}
scores: dict[str | int, int | float | bool] = {
    "Calculus": 100,
    "Korean": 90.5,
    "Biology": True,
    1: 80,
}


# class
class User: ...


user: User = User()

"""
class User → 새로운 타입 정의
user: User → 그 타입을 타입 힌트로 사용
User() → 그 타입의 객체 생성
"""
