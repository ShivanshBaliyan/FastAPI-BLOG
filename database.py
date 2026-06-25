import os

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import settings


def get_database_url() -> str:
    database_url = settings.database_url
    if database_url.startswith("postgresql+psycopg") and os.name == "nt":
        return "sqlite+aiosqlite:///./app.db"
    return database_url


DATABASE_URL = get_database_url()
engine = create_async_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
        