from re import findall

from starlette.testclient import TestClient


def check_image_urls(body: str, client: TestClient):
    for image_url in findall('<img[^>]+src="([^">]+)', body):
        assert image_url.startswith("http://testserver/img/")
        assert (
            image_url.endswith(".webp")
            or image_url.endswith(".svg")
            or image_url.endswith(".gif")
        ), image_url
        relative_url = image_url.replace("http://testserver", "")
        image_response = client.get(relative_url)
        assert image_response.status_code == 200, image_url
