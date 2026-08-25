"""
Tests for the system endpoint.
"""

from fastapi.testclient import TestClient
from omnis_api.app import create_app

app = create_app()
client = TestClient(app)


def test_system_endpoint() -> None:
    """Test that the system endpoint returns runtime information."""

    response = client.get("/api/v1/system")

    assert response.status_code == 200

    body = response.json()

    assert body["name"] == "OMNIS"
    assert body["version"] == "0.1.0"
    assert body["environment"] == "development"
    assert body["status"] == "operational"
