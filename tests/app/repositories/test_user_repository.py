import pytest

from app.users.entities import UserInput


@pytest.mark.asyncio
async def test_get_by_username(user_repo, get_db_session):
    user_input = UserInput(
        username="username2",
        email="user@example.com",
        password="string",
        password2="string",
    )
    await user_repo.add(user_input)
    result = await user_repo.get_by_username("username2")
    assert result.username == "username2"


@pytest.mark.asyncio
async def test_get_by_username_fail(user_repo, get_db_session):
    user_input = UserInput(
        username="username2",
        email="user@example.com",
        password="string",
        password2="string",
    )
    await user_repo.add(user_input)
    result = await user_repo.get_by_username("username")
    assert result is None


@pytest.mark.asyncio
async def test_get_all(user_repo, get_db_session):
    user_input = UserInput(
        username="username2",
        email="user@example.com",
        password="string",
        password2="string",
    )
    user_input_2 = UserInput(
        username="username",
        email="user@example.com",
        password="string",
        password2="string",
    )
    await user_repo.add(user_input)
    await user_repo.add(user_input_2)
    results = await user_repo.get_all()
    assert len(list(results)) == 2


@pytest.mark.asyncio
async def test_add(user_repo, get_db_session):
    user_input = UserInput(
        username="username",
        email="user@example.com",
        password="string",
        password2="string",
    )
    result = await user_repo.add(user_input)
    assert result.username == "username"
