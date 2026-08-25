"""
Health check API routes.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from omnis_api.cache.redis import redis_client
from omnis_api.database.session import check_database_connection

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("")
async def health_check() -> dict[str, str]:
    """
    Health check endpoint.

    This endpoint only verifies that the API process is alive.
    """

    return {
        "status": "healthy",
    }


@router.get("/ready")
async def readiness_check() -> JSONResponse:
    """
    Readiness check endpoint.

    Verifies that required infrastructure dependencies are available.
    """

    database_healthy = await check_database_connection()

    try:
        await redis_client.ping()
        redis_healthy = True
    except Exception:
        redis_healthy = False

    ready = database_healthy and redis_healthy

    response = {
        "status": "ready" if ready else "not_ready",
        "database": "healthy" if database_healthy else "unhealthy",
        "redis": "healthy" if redis_healthy else "unhealthy",
    }

    return JSONResponse(
        status_code=200 if ready else 503,
        content=response,
    )
