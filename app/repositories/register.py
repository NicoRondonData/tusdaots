from app.repositories.protocols import RepositoryInterface


class RepositoriesRegistry:
    def __init__(
        self,
        user_repository: RepositoryInterface,
    ):
        self.user_repository = user_repository
