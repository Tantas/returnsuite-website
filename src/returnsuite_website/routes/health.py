from fastapi import APIRouter
from sqlalchemy import text
from starlette.responses import JSONResponse

from returnsuite_website.services.database import DBSession

router = APIRouter()


@router.get("/health")
async def get_health(db: DBSession):
    db.execute(text("SELECT 1"))
    return JSONResponse(content={"status": "ok"})
