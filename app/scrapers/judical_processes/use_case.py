from typing import Dict

from fastapi import Response, status

from app.scrapers.judical_processes.entities import Case
from app.scrapers.judical_processes.service import JudicialProcessesService
from app.utils import response_message


async def get_data_from_judicial_processes(data: Case) -> Dict:
    client = JudicialProcessesService()
    result = await client.get_data_demandante(data)
    return {
        "response": {"count": result.get("count", 0), "detail": result.get("data", [])},
        "status_code": status.HTTP_200_OK,
    }


def get_data_from_judicial_processes_status(
    response: Response, status_get_data_response: Dict
):
    response_body = response_message()

    if status_get_data_response["status_code"] != status.HTTP_200_OK:
        response_body["success"] = False

    response.status_code = status_get_data_response["status_code"]
    response_body["data"] = status_get_data_response["response"]

    return response_body
