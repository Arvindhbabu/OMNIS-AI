"""
Central API router registration.
"""

from fastapi import APIRouter

from omnis_api.api.routes.health import router as health_router
from omnis_api.api.routes.metadata import router as metadata_router
from omnis_api.api.routes.system import router as system_router
from omnis_api.api.routes.version import router as version_router

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(version_router)
api_router.include_router(metadata_router)
api_router.include_router(system_router)
