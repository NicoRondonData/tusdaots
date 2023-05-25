import pytest
from fastapi import status


@pytest.mark.asyncio
async def test_livez(api_client, get_db_session):
    response = await api_client.get("/tusdatos/livez")

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_register(api_client, get_db_session):
    response = await api_client.post(
        "/tusdatos/register",
        json={
            "username": "string",
            "password": "string",
            "password2": "string",
            "email": "user@example.com",
        },
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_login_fail_without_existing_user(api_client, get_db_session):
    response = await api_client.post(
        "/tusdatos/login",
        json={
            "username": "string",
            "password": "string",
        },
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.asyncio
async def test_login_success(api_client, get_db_session):
    await api_client.post(
        "/tusdatos/register",
        json={
            "username": "string",
            "password": "string",
            "password2": "string",
            "email": "user@example.com",
        },
    )
    response = await api_client.post(
        "/tusdatos/login",
        json={
            "username": "string",
            "password": "string",
        },
    )
    assert response.status_code == status.HTTP_200_OK
