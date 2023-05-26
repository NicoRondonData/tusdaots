from typing import Dict

from fastapi import BackgroundTasks, Depends, Request, Response, status

from app.db import get_session
from app.scrapers.judical_processes.entities import Case, ProcessEnum
from app.scrapers.judical_processes.service import JudicialProcessesService
from app.utils import response_message


async def get_data_from_judicial_processes(
    data: Case,
    process: ProcessEnum,
    background_tasks: BackgroundTasks,
    request: Request,
    session=Depends(get_session),
) -> Dict:
    """
    Retrieve data from the judicial processes API.

    Args:
        data (Case): Case data.
        process (ProcessEnum): Process type.
        background_tasks (BackgroundTasks): Background tasks.
        request (Request): FastAPI request object.
        session: Database session (dependency injection).

    Returns:
        Dict: Data from the judicial processes API.

    """
    client = JudicialProcessesService()
    result = await client.get_data_demandante_demandado(
        data=data,
        process=process,
        background_tasks=background_tasks,
        request=request,
        db_session=session,
    )
    return {
        "response": {"count": result.get("count", 0), "detail": result.get("data", [])},
        "status_code": status.HTTP_200_OK,
    }


def get_data_from_judicial_processes_status(
    response: Response, status_get_data_response: Dict
):
    """
    Set the status and response data for the get_data_from_judicial_processes endpoint.

    Args:
        response (Response): FastAPI response object.
        status_get_data_response (Dict): Status and response data.

    Returns:
        dict: Response body.

    """
    response_body = response_message()

    if status_get_data_response["status_code"] != status.HTTP_200_OK:
        response_body["success"] = False

    response.status_code = status_get_data_response["status_code"]
    response_body["data"] = status_get_data_response["response"]

    return response_body
