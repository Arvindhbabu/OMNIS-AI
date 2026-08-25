"""
Application factory.
"""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from omnis_api.api.router import api_router
from omnis_api.cache.redis import close_redis
from omnis_api.core.config import get_settings
from omnis_api.core.logging import configure_logging
from omnis_api.database.session import close_database

settings = get_settings()


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    """
    Manage application startup and shutdown resources.
    """

    yield

    await close_redis()
    await close_database()


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """

    configure_logging()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="OMNIS AI Cognitive Operating System API",
        lifespan=lifespan,
    )

    app.include_router(
        api_router,
        prefix=settings.api_prefix,
    )

    return app
