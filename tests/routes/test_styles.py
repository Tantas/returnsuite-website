from fastapi.testclient import TestClient

from returnsuite_website.main import app

client = TestClient(app)


def test_get_styles():
    response = client.get("/static/1/styles.css")
    assert response.status_code == 200
