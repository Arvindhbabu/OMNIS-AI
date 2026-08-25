"""
Version API routes.
"""

from fastapi import APIRouter
from omnis_api.core.config import get_settings

settings = get_settings()

router = APIRouter(
    prefix="/version",
    tags=["Version"],
)


@router.get("")
async def get_version() -> dict[str, str]:
    """
    Return application version information.
    """
    return {
        "app_name": settings.app_name,
        "version": settings.app_version,
    }
