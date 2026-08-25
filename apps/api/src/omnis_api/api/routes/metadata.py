"""
Metadata API routes.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from omnis_api.api.dependencies import get_metadata_service
from omnis_api.schemas.metadata import (
    MetadataCreateRequest,
    MetadataResponse,
    MetadataUpdateRequest,
)
from omnis_api.services.metadata_service import MetadataService

router = APIRouter(
    prefix="/metadata",
    tags=["Metadata"],
)


@router.get(
    "/{key}",
    response_model=MetadataResponse,
    summary="Get metadata by key",
)
async def get_metadata(
    key: str,
    service: MetadataService = Depends(get_metadata_service),
) -> MetadataResponse:
    """
    Retrieve metadata by its key.
    """

    metadata = await service.get_metadata(key)

    if metadata is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Metadata '{key}' not found.",
        )

    return MetadataResponse.model_validate(metadata)


@router.post(
    "",
    response_model=MetadataResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create metadata",
)
async def create_metadata(
    request: MetadataCreateRequest,
    service: MetadataService = Depends(get_metadata_service),
) -> MetadataResponse:
    """
    Create a new metadata entry.
    """

    try:
        metadata = await service.create_metadata(request)

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc

    return MetadataResponse.model_validate(metadata)


@router.put(
    "/{key}",
    response_model=MetadataResponse,
    summary="Update metadata",
)
async def update_metadata(
    key: str,
    request: MetadataUpdateRequest,
    service: MetadataService = Depends(get_metadata_service),
) -> MetadataResponse:
    """
    Update an existing metadata entry.
    """

    metadata = await service.update_metadata(
        key=key,
        value=request.value,
    )

    if metadata is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Metadata '{key}' not found.",
        )

    return MetadataResponse.model_validate(metadata)
