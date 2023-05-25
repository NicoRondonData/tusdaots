from typing import List, Optional

from sqlmodel import Session, select

from app.users.auth import auth_handler
from app.users.entities import UserInput, UserResponse
from app.users.models import UserModel


class UserRepository:
    def __init__(self, session: Session):
        """
        Initialize UserRepository with a SQLModel Session.

        Args:
            session (Session): A SQLModel Session for database operations.
        """
        self.session = session

    async def get_by_username(self, username: str) -> Optional[UserModel]:
        """
        Retrieve a user by username.

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            Optional[UserModel]: The user record if found, else None.
        """
        statement = select(UserModel).where(UserModel.username == username)
        results = (await self.session.execute(statement)).one_or_none()
        if not results:
            return None

        user_record = results[0]
        return user_record

    async def get_all(self) -> List[UserModel]:
        """
        Retrieve all users.

        Returns:
            List[UserModel]: A list of all user records.
        """
        statement = select(UserModel)
        results = await self.session.execute(statement)
        return results

    async def add(self, data: UserInput) -> UserResponse:
        """
        Add a new user.

        Args:
            data (UserInput): The user input data, containing username and password.

        Returns:
            UserResponse: The response containing the username of the added user.
        """
        print("nicoo")
        print(data)
        hashed_pwd = auth_handler.get_password_hash(data.password)
        new_user = UserModel(username=data.username, password=hashed_pwd)
        print(new_user)
        self.session.add(new_user)
        print("cool")
        await self.session.flush()
        print("nenaaaa")
        return UserResponse(username=new_user.username)
