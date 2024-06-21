from fastapi.testclient import TestClient

from returnsuite_website.main import app
from returnsuite_website.routes.blog import get_posts

# from utils import check_image_urls


client = TestClient(app)


def test_get_blog():
    response = client.get("/blog")
    assert response.status_code == 200
    # check_image_urls(response.text, client)
    posts = get_posts()
    for index in range(len(posts) + 1):
        response = client.get(f"/blog?offset={index}&size=1")
        assert response.status_code == 200
        # check_image_urls(response.text, client)
    for index in range(len(posts) + 1):
        response = client.get(f"/blog?offset={index}&size=1&sort=chronological")
        assert response.status_code == 200
        # check_image_urls(response.text, client)


def test_get_blog_posts():
    posts = get_posts()
    for post in posts:
        response = client.get(f"/blog/{post.slug}")
        assert response.status_code == 200
        # check_image_urls(response.text, client)
