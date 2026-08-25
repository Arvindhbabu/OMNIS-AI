from typing import Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    """Base repository providing common database operations."""

    def __init__(self, session: AsyncSession):
        self.session = session
