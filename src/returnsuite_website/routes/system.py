from fastapi import APIRouter
from sqlalchemy import text
from starlette.responses import JSONResponse, Response
from starlette.staticfiles import StaticFiles
from starlette.types import Scope

from returnsuite_website.core.config import get_app_settings
from returnsuite_website.services.database import DBSession

router = APIRouter()


@router.get("/health")
async def get_health(db: DBSession):
    db.execute(text("SELECT 1"))
    return JSONResponse(content={"status": "ok"})


@router.get("/robots.txt")
async def get_robots_text():
    return Response(
        content="User-agent: *\nAllow: /\n",
        media_type="text/plain",
    )


class CacheControlledStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope: Scope) -> Response:
        response = await super().get_response(path, scope)
        if not get_app_settings().debug:
            response.headers["Cache-Control"] = "public, max-age=31536000"
        return response
