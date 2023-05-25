import asyncio
from asyncio.events import AbstractEventLoop
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Generator

import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel
from sqlmodel.pool import StaticPool

from app.db import get_session
from app.main import app
from app.repositories.register import RepositoriesRegistry
from app.repositories.user_repository import UserRepository


@pytest.fixture(scope="session")
def event_loop() -> Generator[AbstractEventLoop, None, None]:
    loop = asyncio.get_event_loop_policy().new_event_loop()

    yield loop

    try:
        asyncio.runners._cancel_all_tasks(loop)
    finally:
        loop.close()


#
@pytest_asyncio.fixture(scope="session")
async def db_session(session_mocker) -> AsyncGenerator[AsyncSession, None]:
    engine = create_async_engine("sqlite+aiosqlite://", poolclass=StaticPool)
    session_mocker.patch(
        "app.db.engine",
        engine,
    )
    async with engine.begin() as connection:
        # Create all tables
        await connection.run_sync(SQLModel.metadata.create_all)

    async with asynccontextmanager(get_session)() as db_session:
        # Start a transaction
        trans = await db_session.begin()

        yield db_session

        # Rollback the transaction after the test is done
        await trans.rollback()


@pytest_asyncio.fixture(scope="session")
async def get_db_session(db_session: AsyncSession):
    async def _get_db_session():
        yield db_session

    return _get_db_session


@pytest_asyncio.fixture(scope="function")
async def api_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture(scope="session")
def repositories_registry():
    repositories_registry = RepositoriesRegistry(user_repository=UserRepository)
    return repositories_registry
