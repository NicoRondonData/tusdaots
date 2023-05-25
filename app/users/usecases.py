from fastapi import Depends, Request, status
from sqlalchemy.exc import IntegrityError

from app.db import get_session
from app.users.auth import auth_handler
from app.users.entities import UserInput, UserLogin


async def add_user_use_case(
    request: Request, user_input: UserInput, db_session=Depends(get_session)
):
    """
    Handle user registration.

    This function adds a new user to the database, handling any exceptions that may occur during the process.

    Args:
        request (Request): The incoming request.
        user_input (UserInput): The user data input.
        db_session (Session, optional): The database session. Defaults to Depends(get_session).

    Returns:
        dict: A dictionary containing the response details and status code.
    """
    try:
        new_user = await request.app.repositories_registry.user_repository(
            db_session
        ).add(data=user_input)
        await db_session.commit()
        return {"response": {"detail": new_user}, "status_code": status.HTTP_200_OK}
    except IntegrityError:
        return {
            "response": {"detail": "Username is taken'"},
            "status_code": status.HTTP_400_BAD_REQUEST,
        }
    except Exception as e:
        return {
            "response": {"detail": str(e)},
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
        }


async def login_user_use_case(
    request: Request, user_login: UserLogin, db_session=Depends(get_session)
):
    """
    Handle user login.

    This function verifies a user's login credentials, handling any exceptions that may occur during the process.

    Args:
        request (Request): The incoming request.
        user_login (UserLogin): The user login input.
        db_session (Session, optional): The database session. Defaults to Depends(get_session).

    Returns:
        dict: A dictionary containing the response details and status code.
    """
    user = await request.app.repositories_registry.user_repository(
        db_session
    ).get_by_username(username=user_login.username)
    if not user:
        return {
            "response": {"detail": "Invalid username and/or password"},
            "status_code": status.HTTP_401_UNAUTHORIZED,
        }
    verified = auth_handler.verify_password(user_login.password, user.password)
    if not verified:
        return {
            "response": {"detail": "Invalid username and/or password"},
            "status_code": status.HTTP_401_UNAUTHORIZED,
        }
    token = auth_handler.encode_token(user.username)
    return {"response": {"detail": {"token": token}}, "status_code": status.HTTP_200_OK}
