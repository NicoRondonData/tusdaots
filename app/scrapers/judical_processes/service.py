from app.base.settings import get_settings
from app.scrapers.base import Service
from app.scrapers.judical_processes.entities import Case


class JudicialProcessesService(Service):
    def __init__(self):
        super().__init__()
        self.api_url = get_settings().judicial_processes_api

    async def get_number_of_cases(self, data: Case):
        url = self.api_url + "contarCausas"
        response = self.client.post(url=url, json=data.dict(by_alias=True))
        return response.json()

    async def get_data_demandante(self, data: Case) -> dict:
        number_of_cases = await self.get_number_of_cases(data)
        url = self.api_url + "buscarCausas"
        params = {"size": number_of_cases}
        response = self.client.post(
            url=url, json=data.dict(by_alias=True), params=params
        )
        return {"data": response.json(), "count": number_of_cases}
