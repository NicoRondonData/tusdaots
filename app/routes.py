from fastapi import APIRouter, BackgroundTasks, Depends, Request

from app.db import get_session
from app.scrapers.judical_processes.entities import ProcessEnum
from app.scrapers.judical_processes.use_case import get_data_from_judicial_processes
from app.users.auth import auth_handler
from app.users.services import get_add_user_status, get_login_user_status

router = APIRouter(prefix="/tusdatos")


@router.get("/livez")
async def liveness_probe():
    return {"liveness": "True"}


@router.post("/register")
async def register(response: dict = Depends(get_add_user_status)):
    """
    Register a new user.

    This endpoint handles the registration of a new user. It depends on the
    status returned by the `get_add_user_status` function.

    Args:
        response (dict, optional): The status of the new user registration.
            Defaults to Depends(get_add_user_status).

    Returns:
        dict: The status of the registration.
    """
    return response


@router.post("/login")
async def login(response: dict = Depends(get_login_user_status)):
    """
    Log in an existing user.

    This endpoint handles the login of an existing user. It depends on the
    status returned by the `get_login_user_status` function.

    Args:
        response (dict, optional): The status of the user login.
            Defaults to Depends(get_login_user_status).

    Returns:
        dict: The status of the login.
    """
    return response


@router.post("/get-data/{process}")
async def get_data(
    process: ProcessEnum,
    background_tasks: BackgroundTasks,
    request: Request,
    response: dict = Depends(get_data_from_judicial_processes),
):
    """
    Endpoint to retrieve data for the plaintiff from the judicial processes API.

    Args:
        process (ProcessEnum): Process type.
        background_tasks (BackgroundTasks): Background tasks.
        request (Request): FastAPI request object.
        response (dict, optional): Response data from get_data_from_judicial_processes.
            Defaults to Depends(get_data_from_judicial_processes).

    Returns:
        dict: Response data.

    """
    return response


@router.post("/get-info")
async def get_info(
    request: Request,
    db_session=Depends(get_session),
    user=Depends(auth_handler.get_current_user),
):
    result = await request.app.repositories_registry.judicial_case_repository(
        db_session
    ).get_all()
    return list(result)


@router.post("/get-info-details")
async def get_info_details(
    request: Request,
    db_session=Depends(get_session),
    user=Depends(auth_handler.get_current_user),
):
    result = await request.app.repositories_registry.judicial_case_repository(
        db_session
    ).get_all_info()
    return list(result)
