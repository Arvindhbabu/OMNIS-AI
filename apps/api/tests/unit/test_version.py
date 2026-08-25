from fastapi.testclient import TestClient
from omnis_api.app import create_app

app = create_app()
client = TestClient(app)


def test_version_endpoint() -> None:
    """Test that the version endpoint returns application information."""

    response = client.get("/api/v1/version")

    assert response.status_code == 200

    body = response.json()

    assert body["app_name"] == "OMNIS API"
    assert body["version"] == "0.1.0"
