import os

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

from app.base.settings import get_settings

DATABASE_HOST = os.environ.get(
    "DATABASE_HOST", "postgresql+asyncpg://localhost@tusdatos-db:5432/tusdatos"
)
engine = create_async_engine(
    DATABASE_HOST, echo=get_settings().sqlalchemy_echo, future=True
)


async def init_db():
    async with engine.begin() as conn:  # noqa F841
        return 0


async def get_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        yield session
