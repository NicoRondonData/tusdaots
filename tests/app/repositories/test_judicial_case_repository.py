import pytest


@pytest.mark.asyncio
async def test_add_judicial_data_to_db(judicial_repo, get_db_session, api_client):
    await api_client.post(
        "/tusdatos/get-data/demandante",
        json={
            "numeroCausa": "",
            "actor": {"cedulaActor": "1791251237001", "nombreActor": ""},
            "demandado": {"cedulaDemandado": "", "nombreDemandado": ""},
            "provincia": "",
            "numeroFiscalia": "",
            "recaptcha": "",
        },
    )
    result = await judicial_repo.get_all()
    assert len(list(result)) > 0
