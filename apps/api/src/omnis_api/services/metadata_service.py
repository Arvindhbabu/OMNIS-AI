from omnis_api.database.models.system_metadata import SystemMetadata
from omnis_api.database.repositories.system_metadata import (
    SystemMetadataRepository,
)
from omnis_api.schemas.metadata import MetadataCreateRequest


class MetadataService:
    """Business logic for system metadata."""

    def __init__(
        self,
        repository: SystemMetadataRepository,
    ):
        self.repository = repository

    async def get_metadata(
        self,
        key: str,
    ) -> SystemMetadata | None:
        """Get metadata by key."""

        return await self.repository.get_by_key(key)

    async def create_metadata(
        self,
        request: MetadataCreateRequest,
    ) -> SystemMetadata:
        """Create a new metadata entry."""

        existing = await self.repository.get_by_key(request.key)

        if existing is not None:
            raise ValueError(f"Metadata '{request.key}' already exists.")

        metadata = SystemMetadata(
            key=request.key,
            value=request.value,
        )

        self.repository.session.add(metadata)

        await self.repository.session.commit()
        await self.repository.session.refresh(metadata)

        return metadata

    async def update_metadata(
        self,
        key: str,
        value: str,
    ) -> SystemMetadata | None:
        """Update an existing metadata entry."""

        return await self.repository.update_value(
            key=key,
            value=value,
        )
