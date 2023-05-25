from fastapi import Depends, Response, status

from app.users.usecases import add_user_use_case, login_user_use_case
from app.utils import response_message


def get_add_user_status(
    response: Response, add_user_status_response: dict = Depends(add_user_use_case)
):
    """
    Handle the status response for adding a new user.

    This function takes the status response from the add_user_use_case function, formats it
    and sets the status of the HTTP response accordingly.

    Args:
        response (Response): The HTTP response.
        add_user_status_response (dict): The status response from the add_user_use_case function. Defaults to Depends(add_user_use_case).

    Returns:
        dict: A dictionary containing the response message.
    """
    response_body = response_message()

    if add_user_status_response["status_code"] != status.HTTP_200_OK:
        response_body["success"] = False

    response.status_code = add_user_status_response["status_code"]
    response_body["data"] = add_user_status_response["response"]

    return response_body


def get_login_user_status(
    response: Response, login_user_status_response: dict = Depends(login_user_use_case)
):
    """
    Handle the status response for logging in a user.

    This function takes the status response from the login_user_use_case function, formats it
    and sets the status of the HTTP response accordingly.

    Args:
        response (Response): The HTTP response.
        login_user_status_response (dict): The status response from the login_user_use_case function. Defaults to Depends(login_user_use_case).

    Returns:
        dict: A dictionary containing the response message.
    """
    response_body = response_message()

    if login_user_status_response["status_code"] != status.HTTP_200_OK:
        response_body["success"] = False

    response.status_code = login_user_status_response["status_code"]
    response_body["data"] = login_user_status_response["response"]

    return response_body
