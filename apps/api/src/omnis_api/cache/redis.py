from redis.asyncio import Redis

from omnis_api.core.config import get_settings

settings = get_settings()

redis_client = Redis.from_url(
    settings.redis_url,
    decode_responses=True,
)


async def close_redis() -> None:
    """Close the Redis client."""

    await redis_client.aclose()
