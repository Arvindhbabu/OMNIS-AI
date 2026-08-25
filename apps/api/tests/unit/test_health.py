from fastapi.testclient import TestClient
from omnis_api.app import create_app

app = create_app()
client = TestClient(app)


def test_health_endpoint() -> None:
    """Test that the health endpoint returns a healthy status."""

    response = client.get("/api/v1/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
