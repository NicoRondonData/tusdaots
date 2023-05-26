from app.repositories.protocols import RepositoryInterface


class RepositoriesRegistry:
    def __init__(
        self,
        user_repository: RepositoryInterface,
        judicial_case_repository: RepositoryInterface,
    ):
        self.user_repository = user_repository
        self.judicial_case_repository = judicial_case_repository
