from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import get_session, init_db
from app.repositories.judicial_case_repository import JudicialCaseRepository
from app.repositories.register import RepositoriesRegistry
from app.repositories.user_repository import UserRepository
from app.routes import router


class TusDatosApp(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.repositories_registry = RepositoriesRegistry(
            user_repository=UserRepository,
            judicial_case_repository=JudicialCaseRepository,
        )

        self.get_db_session = get_session


docs_url = "/tusdatos/docs"
app = TusDatosApp(openapi_url=f"{docs_url}/openapi.json", docs_url=docs_url)
app.include_router(router)


@app.on_event("startup")
async def on_startup():
    # Database
    await init_db()


# CORS
origins = ["http://localhost", "http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
