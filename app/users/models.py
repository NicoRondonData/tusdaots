import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class UserModel(SQLModel, table=True):
    __tablename__ = "user"
    id: Optional[int] = Field(primary_key=True)
    username: str = Field(index=True, unique=True)
    password: str = Field(max_length=256, min_length=6)
    created_at: datetime.datetime = datetime.datetime.now()
