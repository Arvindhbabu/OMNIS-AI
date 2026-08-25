"""
System API routes.
"""

from fastapi import APIRouter
from omnis_api.core.config import get_settings
from omnis_api.schemas.system import SystemResponse

router = APIRouter(
    prefix="/system",
    tags=["System"],
)

settings = get_settings()


@router.get(
    "",
    response_model=SystemResponse,
    summary="Get system information",
)
async def get_system() -> SystemResponse:
    """
    Return information about the running OMNIS system.
    """

    return SystemResponse(
        name="OMNIS",
        version=settings.app_version,
        environment=settings.environment,
        status="operational",
    )
