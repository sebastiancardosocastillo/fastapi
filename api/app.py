from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.middleware.db_monitor import DBConnectionMonitorMiddleware

from api.public import api as public_api
from api.config import Settings

def create_app(settings: Settings):
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.DESCRIPTION,
        version=settings.VERSION,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # Add middleware to monitor database connections
    app.add_middleware(DBConnectionMonitorMiddleware)

    # Routers
    app.include_router(public_api, prefix="/api/v1")

    return app