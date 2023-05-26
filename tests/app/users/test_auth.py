from unittest.mock import patch

import jwt
import pytest
from fastapi import HTTPException
from passlib.context import CryptContext

from app.users.auth import AuthHandler


def test_get_password_hash():
    auth_handler = AuthHandler()
    password = "my_password"
    hashed_password = auth_handler.get_password_hash(password)

    assert hashed_password != password
    assert CryptContext(schemes=["bcrypt"]).verify(password, hashed_password)


def test_verify_password():
    auth_handler = AuthHandler()
    password = "my_password"
    hashed_password = auth_handler.get_password_hash(password)

    assert auth_handler.verify_password(password, hashed_password)
    assert not auth_handler.verify_password("wrong_password", hashed_password)


def test_encode_decode_token():
    auth_handler = AuthHandler()
    user_id = "user1"
    token = auth_handler.encode_token(user_id)
    decoded_user_id = auth_handler.decode_token(token)

    assert user_id == decoded_user_id


def test_decode_token_with_expired_signature():
    auth_handler = AuthHandler()
    expired_token = "expired_token"

    with patch("jwt.decode", side_effect=jwt.ExpiredSignatureError):
        with pytest.raises(HTTPException) as excinfo:
            auth_handler.decode_token(expired_token)
        assert str(excinfo.value.status_code) == "401"
        assert excinfo.value.detail == "Expired signature"


def test_decode_token_with_invalid_token():
    auth_handler = AuthHandler()
    invalid_token = "invalid_token"

    with patch("jwt.decode", side_effect=jwt.InvalidTokenError):
        with pytest.raises(HTTPException) as excinfo:
            auth_handler.decode_token(invalid_token)
        assert str(excinfo.value.status_code) == "401"
        assert excinfo.value.detail == "Invalid token"
