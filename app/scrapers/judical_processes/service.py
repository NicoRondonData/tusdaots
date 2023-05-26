from fastapi import BackgroundTasks, Request

from app.base.settings import get_settings

# from app.main import app
from app.scrapers.base import Service
from app.scrapers.judical_processes.entities import Case, JudicialCase, ProcessEnum


async def insert_data_into_table(data_list: list, request: Request, db_session):
    """
    Insert the data into the corresponding table.

    Args:
        data_list (list): List of data to insert.
        request (Request): FastAPI Request object.
        db_session: Database session.

    Returns:
        None
    """
    judicial_cases = [JudicialCase(**data) for data in data_list]
    await request.app.repositories_registry.judicial_case_repository(
        db_session
    ).bulk_insert(judicial_cases)


class JudicialProcessesService(Service):
    def __init__(self):
        super().__init__()
        self.api_url = get_settings().judicial_processes_api

    async def get_number_of_cases(self, data: Case):
        """
        Get the number of cases based on the specified data.

        Args:
            data (Case): Case data.

        Returns:
            dict: API response with the number of cases.
        """
        url = self.api_url + "contarCausas"
        response = self.client.post(url=url, json=data.dict(by_alias=True))
        return response.json()

    async def get_data_demandante_demandado(
        self,
        data: Case,
        process: ProcessEnum,
        background_tasks: BackgroundTasks,
        request: Request,
        db_session,
    ) -> dict:
        """
        Get the data of the plaintiff or defendant based on the specified data.

        Args:
            data (Case): Case data.
            process (ProcessEnum): Type of process.
            background_tasks (BackgroundTasks): FastAPI BackgroundTasks object.
            request (Request): FastAPI Request object.
            db_session: Database session.

        Returns:
            dict: Response with the formatted data and the count of cases.
        """
        number_of_cases = await self.get_number_of_cases(data)
        user_id = None
        if data.defendant:
            user_id = data.defendant.id_number
        if data.plaintiff:
            user_id = data.plaintiff.id_number
        url = self.api_url + "buscarCausas"
        params = {"size": number_of_cases}
        response = self.client.post(
            url=url, json=data.dict(by_alias=True), params=params
        )
        total_response = response.json()
        if not total_response:
            return {"data": [], "count": number_of_cases}

        format_result = [
            {**r, "proceso": process, "user_id": user_id} for r in total_response
        ]
        background_tasks.add_task(
            insert_data_into_table, format_result, request, db_session
        )
        return {"data": format_result, "count": number_of_cases}
