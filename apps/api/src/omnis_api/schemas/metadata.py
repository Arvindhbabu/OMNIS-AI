from datetime import datetime

from pydantic import BaseModel


class MetadataResponse(BaseModel):
    """Metadata response."""

    key: str
    value: str
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True,
    }


class MetadataCreateRequest(BaseModel):
    """Request to create metadata."""

    key: str
    value: str


class MetadataUpdateRequest(BaseModel):
    """Request to update metadata."""

    value: str
