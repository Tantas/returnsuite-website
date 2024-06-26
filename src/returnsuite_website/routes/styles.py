from importlib.resources import files

from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import RedirectResponse, Response
from starlette.status import HTTP_302_FOUND

from returnsuite_website.core.config import get_app_settings

router = APIRouter()

_css_path = files("returnsuite_website") / "resources" / "css" / "styles.css"
_cached_css = _css_path.read_bytes()


@router.get("/static/{version}/styles.css")
async def get_styles(request: Request, version: str):
    settings = get_app_settings()
    css_version = settings.css_version
    if css_version != version:
        url = request.url_for(get_styles.__name__, version=css_version)
        return RedirectResponse(url, status_code=HTTP_302_FOUND)

    if settings.debug:
        return Response(content=_css_path.read_bytes(), media_type="text/css")
    return Response(
        content=_cached_css,
        headers={"Cache-Control": "public, max-age=31536000, immutable"},
        media_type="text/css",
    )
