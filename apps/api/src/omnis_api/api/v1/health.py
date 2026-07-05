"""
Health check endpoints.

These endpoints provide service health information and are used by
load balancers, monitoring systems, and orchestration platforms.
"""

from fastapi import APIRouter

from omnis_api.core.config import get_settings

router = APIRouter(tags=["Health"])

settings = get_settings()


@router.get(
    "/health",
    summary="Health Check",
    description="Returns the current health status of the OMNIS API service.",
)
async def health_check() -> dict[str, str]:
    """
    Health check endpoint.

    Returns:
        Basic health information about the running service.
    """
    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
    }
