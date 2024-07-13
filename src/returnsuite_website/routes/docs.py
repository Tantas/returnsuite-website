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


@router.get("/docs/concepts/noi")
async def get_concepts_noi(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/4-noi-statement.html.jinja2",
        context={},
    )


@router.get("/docs/concepts/noi/overview")
async def get_concepts_noi_overview(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/01-overview.html.jinja2",
    )


@router.get("/docs/concepts/noi/real-estate-model")
async def get_concepts_noi_real_estate_model(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/02-workings-real-estate-model.html.jinja2",
    )


@router.get("/docs/concepts/noi/market-and-potential-base-rent")
async def get_concepts_noi_market_and_potential_base_rent(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/03-potential-base-rent.html.jinja2",
    )


@router.get("/docs/concepts/noi/actual-or-projected-base-rent")
async def get_concepts_noi_projected_base_real_rent(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/04-actual-base-rent.html.jinja2",
    )


@router.get("/docs/concepts/noi/additional-rent")
async def get_concepts_noi_additional_rent(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/05-additional-rent.html.jinja2",
    )


@router.get("/docs/concepts/noi/other-tenant-revenue")
async def get_concepts_noi_other_tenant_revenue(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/06-other-tenant-revenue.html.jinja2",
    )


@router.get("/docs/concepts/noi/other-revenue")
async def get_concepts_noi_other_revenue(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/07-other-revenue.html.jinja2",
    )


@router.get("/docs/concepts/noi/potential-gross-income")
async def get_concepts_noi_potential_gross_income(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/08-potential-gross-income.html.jinja2",
    )


@router.get("/docs/concepts/noi/vacancy-and-credit-loss")
async def get_concepts_noi_vacancy_and_credit_loss(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/09-vacancy-and-credit-loss.html.jinja2",
    )


@router.get("/docs/concepts/noi/effective-gross-income")
async def get_concepts_noi_effective_gross_income(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/10-effective-gross-income.html.jinja2",
    )


@router.get("/docs/concepts/noi/operating-expenses")
async def get_concepts_noi_operating_expenses(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/11-operating-expenses.html.jinja2",
    )


@router.get("/docs/concepts/noi/net-operating-income")
async def get_concepts_noi_net_operating_income(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/12-net-operating-income.html.jinja2",
    )


@router.get("/docs/concepts/noi/noi-and-cash-flow-statement")
async def get_concepts_noi_noi_and_cash_flow_statement(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/13-noi-and-cash-flow-statement.html.jinja2",
    )


@router.get("/docs/concepts/noi/valuation-and-capitalization")
async def get_concepts_noi_valuation_and_capitalization(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/14-valuation-and-capitalization.html.jinja2",
    )


@router.get("/docs/concepts/noi/exercise-1")
async def get_concepts_noi_exercise_1(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/15-exercise-1.html.jinja2",
    )


@router.get("/docs/concepts/noi/valuation-tiered-direct-capitalization")
async def get_concepts_noi_valuation_tiered_direct_capitalization(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/16-valuation-tiered-direct-capitalization.html.jinja2",
    )


@router.get("/docs/concepts/noi/exercise-2")
async def get_concepts_noi_exercise_2(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/17-exercise-2.html.jinja2",
    )


@router.get("/docs/concepts/noi/valuation-top-slice")
async def get_concepts_noi_valuation_top_slice(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/18-valuation-top-slice.html.jinja2",
    )


@router.get("/docs/concepts/noi/exercise-3")
async def get_concepts_noi_exercise_3(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/19-exercise-3.html.jinja2",
    )
