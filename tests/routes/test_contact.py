from fastapi.testclient import TestClient

from returnsuite_website.main import app
from returnsuite_website.services.database import ContactRequest, get_db

from utils import check_image_urls


client = TestClient(app)


def test_get_contact():
    response = client.get("/contact")
    assert response.status_code == 200
    check_image_urls(response.text, client)


def test_post_contact_success_min():
    response = client.post(
        "/contact",
        data={
            "name": "Test Name",
            "organization": "Test Organization",
            "email": "sample@example.com",
            "subject": "Testing Contact Submission",
            "message": "Testing contact submission message.",
        },
        follow_redirects=False,
    )
    assert response.status_code == 302
    assert "/contact?success=true" in response.headers.get("location")
    db = get_db().__next__()
    contact_request = db.query(ContactRequest).one()
    assert contact_request.name == "Test Name"
    db.delete(contact_request)
    db.commit()


def test_post_contact_success_all():
    response = client.post(
        "/contact",
        headers={
            "Accept-Language": "en-US",
            "user_agent": "Sample User Agent String",
        },
        data={
            "timezone": "America/New_York",
            "name": "Test Name",
            "organization": "Test Organization",
            "email": "sample@example.com",
            "subject": "Testing Contact Submission",
            "message": "Testing contact submission message.",
        },
        follow_redirects=False,
    )
    assert response.status_code == 302
    assert "/contact?success=true" in response.headers.get("location")
    db = get_db().__next__()
    contact_request = db.query(ContactRequest).one()
    assert contact_request.name == "Test Name"
    db.delete(contact_request)
    db.commit()


def test_post_contact_failure():
    response = client.post(
        "/contact",
        headers={
            "Accept-Language": "en-US",
        },
        data={},
        follow_redirects=False,
    )
    assert response.status_code == 422
