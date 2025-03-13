

from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from returnsuite_website.core.html import templates
from returnsuite_website.services import localization_directory

router = APIRouter(default_response_class=HTMLResponse)


@router.get("/pricing")
async def get_pricing(request: Request):
    countries = localization_directory.load2()

    selected_country = None
    selected_language = None
    for country in countries:
        for language in country.languages:
            if language.slug == "en-us":
                selected_country = country
                selected_language = language
                break

    return templates.TemplateResponse(
        request=request,
        name="pricing.html.jinja2",
        context={
            "countries": countries,
            "selected_country": selected_country,
            "selected_language": selected_language,
        },
    )
