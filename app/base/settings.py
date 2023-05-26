from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_host: str = "postgresql+asyncpg://localhost@tusdatos-db:5432/tusdatos"
    judicial_processes_api: str = "https://api.funcionjudicial.gob.ec/informacion/"
    sqlalchemy_echo: bool = False


@lru_cache()
def get_settings():
    return Settings()
