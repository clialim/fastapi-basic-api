from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

async_engine = create_async_engine(DATABASE_URL)

AsyncSessionFactory = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


async def get_async_session():
    async with AsyncSessionFactory() as session:
        yield session
