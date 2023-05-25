import pytest


@pytest.mark.asyncio
async def test_livez(api_client, get_db_session):
    response = await api_client.get("/tusdatos/livez")

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_register(api_client, get_db_session):
    response = await api_client.post(
        "/tusdatos/register",
        json={
            "username": "string323141a",
            "password": "string",
            "password2": "string",
            "email": "user@example.com",
        },
    )
    assert response.status_code == 200
