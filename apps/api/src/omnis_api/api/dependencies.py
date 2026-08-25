"""
FastAPI dependency providers.
"""

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from omnis_api.database.dependencies import get_db
from omnis_api.database.repositories.system_metadata import (
    SystemMetadataRepository,
)
from omnis_api.services.metadata_service import MetadataService


async def get_metadata_service(
    db: AsyncSession = Depends(get_db),
) -> MetadataService:
    repository = SystemMetadataRepository(db)
    return MetadataService(repository)
