from sqlalchemy import select

from omnis_api.database.models.system_metadata import SystemMetadata
from omnis_api.database.repositories.base import BaseRepository


class SystemMetadataRepository(BaseRepository[SystemMetadata]):
    """Repository for system metadata."""

    async def get_by_key(
        self,
        key: str,
    ) -> SystemMetadata | None:
        """Return metadata by key."""

        statement = select(SystemMetadata).where(SystemMetadata.key == key)

        result = await self.session.execute(statement)

        return result.scalar_one_or_none()

    async def update_value(
        self,
        key: str,
        value: str,
    ) -> SystemMetadata | None:
        """Update the value of an existing metadata entry."""

        metadata = await self.get_by_key(key)

        if metadata is None:
            return None

        metadata.value = value

        await self.session.commit()
        await self.session.refresh(metadata)

        return metadata
