from fastapi import APIRouter, Depends

from app.scrapers.judical_processes.use_case import get_data_from_judicial_processes
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


@router.post("/get-data-plaintiff")
async def get_data_plaintiff(
    response: dict = Depends(get_data_from_judicial_processes),
):
    return response
