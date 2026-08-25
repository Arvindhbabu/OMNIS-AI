"""
Integration tests for the metadata API.
"""

import pytest
from httpx import AsyncClient
from omnis_api.database.models.system_metadata import SystemMetadata
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio
async def test_create_metadata(
    client: AsyncClient,
    db_session: AsyncSession,
) -> None:
    """Test creating a new metadata entry."""

    response = await client.post(
        "/api/v1/metadata",
        json={
            "key": "test_app_name",
            "value": "OMNIS AI",
        },
    )

    assert response.status_code == 201

    body = response.json()

    assert body["key"] == "test_app_name"
    assert body["value"] == "OMNIS AI"
    assert body["created_at"] is not None
    assert body["updated_at"] is not None

    result = await db_session.execute(
        select(SystemMetadata).where(SystemMetadata.key == "test_app_name")
    )

    metadata = result.scalar_one()

    assert metadata.value == "OMNIS AI"


@pytest.mark.asyncio
async def test_create_duplicate_metadata(
    client: AsyncClient,
) -> None:
    """Test that duplicate metadata keys return a conflict."""

    payload = {
        "key": "duplicate_key",
        "value": "first",
    }

    first_response = await client.post(
        "/api/v1/metadata",
        json=payload,
    )

    assert first_response.status_code == 201

    second_response = await client.post(
        "/api/v1/metadata",
        json={
            "key": "duplicate_key",
            "value": "second",
        },
    )

    assert second_response.status_code == 409
    assert second_response.json()["detail"] == ("Metadata 'duplicate_key' already exists.")


@pytest.mark.asyncio
async def test_get_metadata(
    client: AsyncClient,
) -> None:
    """Test retrieving an existing metadata entry."""

    create_response = await client.post(
        "/api/v1/metadata",
        json={
            "key": "get_test",
            "value": "initial",
        },
    )

    assert create_response.status_code == 201

    response = await client.get(
        "/api/v1/metadata/get_test",
    )

    assert response.status_code == 200

    body = response.json()

    assert body["key"] == "get_test"
    assert body["value"] == "initial"


@pytest.mark.asyncio
async def test_get_missing_metadata(
    client: AsyncClient,
) -> None:
    """Test retrieving a nonexistent metadata entry."""

    response = await client.get(
        "/api/v1/metadata/does_not_exist",
    )

    assert response.status_code == 404
    assert response.json()["detail"] == ("Metadata 'does_not_exist' not found.")


@pytest.mark.asyncio
async def test_update_metadata(
    client: AsyncClient,
) -> None:
    """Test updating an existing metadata entry."""

    create_response = await client.post(
        "/api/v1/metadata",
        json={
            "key": "update_test",
            "value": "before",
        },
    )

    assert create_response.status_code == 201

    response = await client.put(
        "/api/v1/metadata/update_test",
        json={
            "value": "after",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["key"] == "update_test"
    assert body["value"] == "after"


@pytest.mark.asyncio
async def test_update_missing_metadata(
    client: AsyncClient,
) -> None:
    """Test updating a nonexistent metadata entry."""

    response = await client.put(
        "/api/v1/metadata/does_not_exist",
        json={
            "value": "new value",
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == ("Metadata 'does_not_exist' not found.")
