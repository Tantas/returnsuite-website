from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from returnsuite_website.core.html import templates

router = APIRouter(default_response_class=HTMLResponse)


@router.get("/docs")
async def get_documentation(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/1-introduction.html.jinja2",
        context={},
    )


@router.get("/docs/concepts/introduction")
async def get_concepts_introduction(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/1-introduction.html.jinja2",
        context={},
    )


@router.get("/docs/concepts/foundational-concepts")
async def get_concepts_foundational_concepts(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/2-foundational-concepts.html.jinja2",
        context={},
    )
