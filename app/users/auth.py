import datetime

import jwt
from fastapi import Depends, HTTPException, Request, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext

from app.db import get_session


class AuthHandler:
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"])
    secret = "supersecret"

    def get_password_hash(self, password):
        """
        Hash a password.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        return self.pwd_context.hash(password)

    def verify_password(self, pwd, hashed_pwd):
        """
        Verify a password against a hashed password.

        Args:
            pwd (str): The password to verify.
            hashed_pwd (str): The hashed password to verify against.

        Returns:
            bool: True if the password matches the hash, False otherwise.
        """
        return self.pwd_context.verify(pwd, hashed_pwd)

    def encode_token(self, user_id):
        """
        Encode a JWT token.

        Args:
            user_id (str): The user ID to encode in the token.

        Returns:
            str: The encoded JWT token.
        """
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=8),
            "iat": datetime.datetime.utcnow(),
            "sub": user_id,
        }
        return jwt.encode(payload, self.secret, algorithm="HS256")

    def decode_token(self, token):
        """
        Decode a JWT token.

        Args:
            token (str): The JWT token to decode.

        Returns:
            str: The user ID encoded in the token.

        Raises:
            HTTPException: If the token signature has expired or if the token is invalid.
        """
        try:
            payload = jwt.decode(token, self.secret, algorithms=["HS256"])
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=401, detail="Expired signature"
            )  # noqa B904
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")  # noqa B904

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        """
        Wrapper for token decoding.

        Args:
            auth (HTTPAuthorizationCredentials): The authorization credentials.

        Returns:
            str: The user ID encoded in the token.
        """
        return self.decode_token(auth.credentials)

    async def get_current_user(
        self,
        request: Request,
        auth: HTTPAuthorizationCredentials = Security(security),
        db_session=Depends(get_session),
    ):
        """
        Get the current user.

        Args:
            request (Request): The incoming request.
            auth (HTTPAuthorizationCredentials): The authorization credentials.
            db_session (Session): The database session.

        Returns:
            UserModel: The current user.

        Raises:
            HTTPException: If the user could not be validated.
        """
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
        username = self.decode_token(auth.credentials)
        if username is None:
            raise credentials_exception
        user = await request.app.repositories_registry.user_repository(
            db_session
        ).get_by_username(username)
        if user is None:
            raise credentials_exception
        return user


auth_handler = AuthHandler()
