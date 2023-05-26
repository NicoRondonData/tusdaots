from typing import List, Optional, Protocol, TypeVar, Union

from app.users.entities import UserInput

T = TypeVar("T")


class RepositoryInterface(Protocol):
    def get_by_username(self, username: str) -> Optional[T]:
        ...

    def get_all(self) -> List[T]:
        ...

    def add(self, value: Union[UserInput]) -> T:
        ...

    def inset_bulk(self, data: List[T]):
        ...
