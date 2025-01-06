from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.config import Settings
from apps.utils.logger import logger_config

from apps.api import router 

# from app.db import conn
# from app.data import seed_data_generator 

logger = logger_config(__name__)

def create_app(settings: Settings):
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        docs_url="/",
        description=settings.DESCRIPTION,
    )

    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


    app.include_router(router)

    return app

def create_app1():
    app = FastAPI()
    return app