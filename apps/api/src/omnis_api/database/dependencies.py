"""
Database dependencies.
"""

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from omnis_api.database.session import SessionLocal


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Provide a database session for a request.

    The session is automatically closed after the request finishes.
    """
    async with SessionLocal() as session:
        yield session
