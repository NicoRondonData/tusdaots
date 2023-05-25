from typing import Optional

from sqlmodel import Field, SQLModel


class UserModel(SQLModel, table=True):
    __tablename__ = "user"
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    hashed_password: str
