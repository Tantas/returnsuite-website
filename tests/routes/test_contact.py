import os
import sys

from fastapi.testclient import TestClient

from returnsuite_website.main import app
from returnsuite_website.services.database import (
    ContactRequest,
    ContactRequestStatus,
    get_db,
)

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from routes.utils import check_image_urls  # noqa: E402

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


def test_post_contact_multiple():
    def run_submission():
        client.post(
            "/contact",
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

    run_submission()
    run_submission()
    run_submission()
    db = get_db().__next__()
    contact_requests = db.query(ContactRequest).order_by(ContactRequest.id).all()
    assert contact_requests[0].status == ContactRequestStatus.valid
    assert contact_requests[1].status == ContactRequestStatus.valid
    assert contact_requests[2].status == ContactRequestStatus.spam
    db.delete(contact_requests[0])
    db.delete(contact_requests[1])
    db.delete(contact_requests[2])
    db.commit()


def test_post_contract_no_js_spam():
    client.post(
        "/contact",
        data={
            "timezone": "",
            "name": "Test Name",
            "organization": "Test Organization",
            "email": "sample@example.com",
            "subject": "Testing Contact Submission",
            "message": "Testing contact submission message.",
        },
        follow_redirects=False,
    )
    db = get_db().__next__()
    contact_requests = db.query(ContactRequest).order_by(ContactRequest.id).all()
    assert contact_requests[0].status == ContactRequestStatus.spam
    db.delete(contact_requests[0])
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
