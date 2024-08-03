import os
import sys

from fastapi.testclient import TestClient

from returnsuite_website.main import app
from returnsuite_website.services.database import Waitlist, WaitlistStatus, get_db

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from routes.utils import check_image_urls  # noqa: E402

client = TestClient(app)


def test_get_index():
    response = client.get("/")
    assert response.status_code == 200
    check_image_urls(response.text, client)


def test_post_waitlist_success_min():
    response = client.post(
        "/waitlist",
        data={
            "name": "Test Name",
            "email": "sample@example.com",
            "organization": "Test Organization",
            "usage": "Landlord",
        },
        follow_redirects=False,
    )
    assert response.status_code == 302
    redirect_url = response.headers.get("location")
    assert redirect_url.endswith("?success=true#Request-Early-Access")
    db = get_db().__next__()
    waitlist = db.query(Waitlist).one()
    assert waitlist.name == "Test Name"
    assert waitlist.status == WaitlistStatus.spam
    db.delete(waitlist)
    db.commit()


def test_post_waitlist_success_all():
    response = client.post(
        "/waitlist",
        data={
            "timezone": "America/New_York",
            "name": "Test Name",
            "email": "sample@example.com",
            "organization": "Test Organization",
            "usage": "Landlord",
            "linkedin_url": "https://linked.com/identifier",
            "twitter_url": "https://twitter.com/identifier",
            "other_url": "https://example.com/identifier",
            "message": "Looking forward to trying the software.",
        },
        follow_redirects=False,
    )
    assert response.status_code == 302
    redirect_url = response.headers.get("location")
    assert redirect_url.endswith("?success=true#Request-Early-Access")
    db = get_db().__next__()
    waitlist = db.query(Waitlist).one()
    assert waitlist.name == "Test Name"
    assert waitlist.status == WaitlistStatus.waiting
    db.delete(waitlist)
    db.commit()


def test_post_waitlist_failure():
    response = client.post(
        "/waitlist",
        headers={
            "Accept-Language": "en-US",
        },
        data={},
        follow_redirects=False,
    )
    assert response.status_code == 422


def test_post_waitlist_multiple():
    def run_submission():
        client.post(
            "/waitlist",
            data={
                "timezone": "America/New_York",
                "name": "Test Name",
                "email": "sample@example.com",
                "organization": "Test Organization",
                "usage": "Landlord",
            },
            follow_redirects=False,
        )

    run_submission()
    run_submission()
    run_submission()
    db = get_db().__next__()
    waiting = db.query(Waitlist).order_by(Waitlist.id).all()
    assert waiting[0].status == WaitlistStatus.waiting
    assert waiting[1].status == WaitlistStatus.waiting
    assert waiting[2].status == WaitlistStatus.spam
    db.delete(waiting[0])
    db.delete(waiting[1])
    db.delete(waiting[2])
    db.commit()


def test_get_view_demo():
    response = client.get("/view-demo")
    assert response.status_code == 200
    check_image_urls(response.text, client)


def test_get_about():
    response = client.get("/about")
    assert response.status_code == 200
    check_image_urls(response.text, client)


def test_get_privacy():
    response = client.get("/privacy")
    assert response.status_code == 200
    check_image_urls(response.text, client)


def test_get_terms():
    response = client.get("/terms")
    assert response.status_code == 200
    check_image_urls(response.text, client)


def test_get_landing_images():
    response = client.get("/landing-images")
    assert response.status_code == 200
    check_image_urls(response.text, client)
