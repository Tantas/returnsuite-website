from fastapi.testclient import TestClient

from returnsuite_website.main import app

client = TestClient(app)


def test_get_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
