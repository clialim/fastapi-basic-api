from db_connection import SessionFactory
from sqlalchemy import select
from models import User

session = SessionFactory()
result = session.execute(select(1))
print(list(result))


result.scalar()
result = session.execute(select(1))
print(result.scalar())

# sql문 출력 확인
stmt = select(User)
print(stmt)
