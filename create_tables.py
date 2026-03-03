from models import Base
from db_connection import engine
from models import User

print("등록된 테이블:", Base.metadata.tables.keys())

Base.metadata.create_all(bind=engine)
