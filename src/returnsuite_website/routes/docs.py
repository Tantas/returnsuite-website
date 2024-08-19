from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from returnsuite_website.core.html import templates

router = APIRouter(default_response_class=HTMLResponse)


@router.get("/docs")
async def get_documentation(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/1-introduction.html.jinja2",
    )


@router.get("/docs/concepts/introduction")
async def get_concepts_introduction(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/1-introduction.html.jinja2",
    )


@router.get("/docs/concepts/foundational-concepts")
async def get_concepts_foundational_concepts(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/2-foundational-concepts.html.jinja2",
    )


@router.get("/docs/concepts/math/overview")
async def get_concepts_math_overview(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/math/01-overview.html.jinja2",
    )


@router.get("/docs/concepts/math/time-value-of-money")
async def get_concepts_time_value_of_money(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/math/02-time-value-of-money.html.jinja2",
    )


@router.get("/docs/concepts/math/net-present-value")
async def get_concepts_net_present_value(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/math/03-net-present-value.html.jinja2",
    )


@router.get("/docs/concepts/math/risk-rates")
async def get_concepts_risk_rates(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/math/04-risk-rates.html.jinja2",
    )


@router.get("/docs/concepts/math/internal-rate-of-return")
async def get_concepts_internal_rate_of_return(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/math/05-internal-rate-of-return.html.jinja2",
    )


@router.get("/docs/concepts/math/perpetuities")
async def get_concepts_perpetuities(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/math/06-perpetuities.html.jinja2",
    )


@router.get("/docs/concepts/math/gordon-growth-model")
async def get_concepts_gordon_growth_model(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/math/07-gordon-growth-model.html.jinja2",
    )


@router.get("/docs/concepts/math/expected-value")
async def get_concepts_expected_value(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/math/08-expected-value.html.jinja2",
    )


@router.get("/docs/concepts/noi")
async def get_concepts_noi(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/overview.html.jinja2",
    )


@router.get("/docs/concepts/valuation-approaches/overview")
async def get_concepts_valuation_approaches_overview(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/valuation-approaches/01-overview.html.jinja2",
    )


@router.get("/docs/concepts/valuation-approaches/market-approach")
async def get_concepts_valuation_approaches_market_approach(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/valuation-approaches/02-market-approach.html.jinja2",
    )


@router.get("/docs/concepts/valuation-approaches/cost-approach")
async def get_concepts_valuation_approaches_cost_approach(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/valuation-approaches/03-cost-approach.html.jinja2",
    )


@router.get("/docs/concepts/valuation-approaches/income-approach")
async def get_concepts_valuation_approaches_income_approach(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/valuation-approaches/04-income-approach.html.jinja2",
    )


@router.get("/docs/concepts/valuation-approaches/income-approach-methods")
async def get_concepts_valuation_approaches_income_approach_methods(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/valuation-approaches/05-income-approach-methods.html.jinja2",
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


@router.get("/docs/concepts/analysis/overview")
async def get_concepts_analysis_overview(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/analysis/01-overview.html.jinja2",
    )


@router.get("/docs/concepts/analysis/analysis-period")
async def get_concepts_analysis_analysis_period(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/analysis/02-analysis-period.html.jinja2",
    )


@router.get("/docs/concepts/analysis/reversionary-value")
async def get_concepts_analysis_reversionary_value(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/analysis/03-reversionary-value.html.jinja2",
    )


@router.get("/docs/concepts/analysis/valuation-method")
async def get_concepts_analysis_valuation_method(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/analysis/04-valuation-method.html.jinja2",
    )


@router.get("/docs/concepts/analysis/noi-line-adjustments")
async def get_concepts_analysis_noi_line_adjustments(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/analysis/05-noi-line-adjustments.html.jinja2",
    )


@router.get("/docs/concepts/analysis/reversionary-capitalization-rate")
async def get_concepts_analysis_reversionary_capitalization_rate(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/analysis/06-reversionary-capitalization-rate.html.jinja2",
    )


@router.get("/docs/concepts/analysis/value-adjustments")
async def get_concepts_analysis_value_adjustments(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/analysis/07-value-adjustments.html.jinja2",
    )


@router.get("/docs/concepts/analysis/investment-analysis")
async def get_concepts_analysis_investment_analysis(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/analysis/08-investment-analysis.html.jinja2",
    )
