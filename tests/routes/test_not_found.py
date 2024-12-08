from starlette.testclient import TestClient

from returnsuite_website.main import app

client = TestClient(app)


def test_not_found():
    response = client.get("/does-not-exist", follow_redirects=False)
    assert response.status_code == 302
    assert response.headers.get("Location") == "/"
