from starlette.testclient import TestClient

from returnsuite_website.main import app

client = TestClient(app)


def test_post_helpful():
    response = client.post(
        "/docs/was-this-page-helpful",
        json={
            "page_name": "test",
            "helpful": True,
        },
    )
    assert response.status_code == 200


def test_subscribe_newsletter():
    response = client.post(
        "/docs/newsletter-signup",
        json={
            "email": "sample@example.com",
            "timezone": "America/New_York",
        },
    )
    assert response.status_code == 200


def test_subscribe_twice():
    test_subscribe_newsletter()
    test_subscribe_newsletter()
