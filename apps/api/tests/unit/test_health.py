from fastapi.testclient import TestClient
from omnis_api.app import create_app

client = TestClient(create_app())


def test_health_endpoint() -> None:
    response = client.get("/api/v1/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert data["service"] == "OMNIS API"
