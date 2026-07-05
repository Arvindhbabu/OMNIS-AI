"""
Application factory.
"""

from fastapi import FastAPI

from omnis_api.api.router import api_router
from omnis_api.core.config import get_settings
from omnis_api.core.logging import configure_logging

settings = get_settings()


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """

    configure_logging()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="OMNIS AI Cognitive Operating System API",
    )

    app.include_router(
        api_router,
        prefix=settings.api_prefix,
    )

    return app
