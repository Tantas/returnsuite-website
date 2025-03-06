from email.utils import make_msgid
from importlib.resources.abc import Traversable

from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse, RedirectResponse

from returnsuite_website.core.config import get_app_settings
from returnsuite_website.core.html import templates

from importlib.resources import files
from typing import Self

import markdown
import yaml
from pydantic import BaseModel

router = APIRouter(default_response_class=HTMLResponse)


@router.get("/docs2")
async def get_documentation(request: Request):
    if get_app_settings().hide_docs:
        return RedirectResponse("/")
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/1-introduction.html.jinja2",
    )


@router.get("/docs2/getting-started")
async def get_getting_started_overview(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/getting-started/overview.html.jinja2",
    )


@router.get("/docs2/concepts/introduction")
async def get_concepts_introduction(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/1-introduction.html.jinja2",
    )


@router.get("/docs2/concepts/foundational-concepts")
async def get_concepts_foundational_concepts(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/2-foundational-concepts.html.jinja2",
    )


@router.get("/docs2/concepts/math/overview")
async def get_concepts_math_overview(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/math/01-overview.html.jinja2",
    )


@router.get("/docs2/concepts/math/time-value-of-money")
async def get_concepts_time_value_of_money(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/math/02-time-value-of-money.html.jinja2",
    )


@router.get("/docs2/concepts/math/net-present-value")
async def get_concepts_net_present_value(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/math/03-net-present-value.html.jinja2",
    )


@router.get("/docs2/concepts/math/risk-rates")
async def get_concepts_risk_rates(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/math/04-risk-rates.html.jinja2",
    )


@router.get("/docs2/concepts/math/internal-rate-of-return")
async def get_concepts_internal_rate_of_return(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/math/05-internal-rate-of-return.html.jinja2",
    )


@router.get("/docs2/concepts/math/perpetuities")
async def get_concepts_perpetuities(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/math/06-perpetuities.html.jinja2",
    )


@router.get("/docs2/concepts/math/gordon-growth-model")
async def get_concepts_gordon_growth_model(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/math/07-gordon-growth-model.html.jinja2",
    )


@router.get("/docs2/concepts/math/expected-value")
async def get_concepts_expected_value(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/math/08-expected-value.html.jinja2",
    )


@router.get("/docs2/concepts/noi")
async def get_concepts_noi(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/overview.html.jinja2",
    )


@router.get("/docs2/concepts/valuation-approaches/overview")
async def get_concepts_valuation_approaches_overview(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/valuation-approaches/01-overview.html.jinja2",
    )


@router.get("/docs2/concepts/valuation-approaches/market-approach")
async def get_concepts_valuation_approaches_market_approach(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/valuation-approaches/02-market-approach.html.jinja2",
    )


@router.get("/docs2/concepts/valuation-approaches/cost-approach")
async def get_concepts_valuation_approaches_cost_approach(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/valuation-approaches/03-cost-approach.html.jinja2",
    )


@router.get("/docs2/concepts/valuation-approaches/income-approach")
async def get_concepts_valuation_approaches_income_approach(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/valuation-approaches/04-income-approach.html.jinja2",
    )


@router.get("/docs2/concepts/valuation-approaches/income-approach-methods")
async def get_concepts_valuation_approaches_income_approach_methods(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/valuation-approaches/05-income-approach-methods.html.jinja2",
    )


@router.get("/docs2/concepts/noi/overview")
async def get_concepts_noi_overview(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/01-overview.html.jinja2",
    )


@router.get("/docs2/concepts/noi/real-estate-model")
async def get_concepts_noi_real_estate_model(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/02-workings-real-estate-model.html.jinja2",
    )


@router.get("/docs2/concepts/noi/market-and-potential-base-rent")
async def get_concepts_noi_market_and_potential_base_rent(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/03-potential-base-rent.html.jinja2",
    )


@router.get("/docs2/concepts/noi/actual-or-projected-base-rent")
async def get_concepts_noi_projected_base_real_rent(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/04-actual-base-rent.html.jinja2",
    )


@router.get("/docs2/concepts/noi/additional-rent")
async def get_concepts_noi_additional_rent(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/05-additional-rent.html.jinja2",
    )


@router.get("/docs2/concepts/noi/other-tenant-revenue")
async def get_concepts_noi_other_tenant_revenue(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/06-other-tenant-revenue.html.jinja2",
    )


@router.get("/docs2/concepts/noi/other-revenue")
async def get_concepts_noi_other_revenue(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/07-other-revenue.html.jinja2",
    )


@router.get("/docs2/concepts/noi/potential-gross-income")
async def get_concepts_noi_potential_gross_income(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/08-potential-gross-income.html.jinja2",
    )


@router.get("/docs2/concepts/noi/vacancy-and-credit-loss")
async def get_concepts_noi_vacancy_and_credit_loss(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/09-vacancy-and-credit-loss.html.jinja2",
    )


@router.get("/docs2/concepts/noi/effective-gross-income")
async def get_concepts_noi_effective_gross_income(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/10-effective-gross-income.html.jinja2",
    )


@router.get("/docs2/concepts/noi/operating-expenses")
async def get_concepts_noi_operating_expenses(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/11-operating-expenses.html.jinja2",
    )


@router.get("/docs2/concepts/noi/net-operating-income")
async def get_concepts_noi_net_operating_income(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/12-net-operating-income.html.jinja2",
    )


@router.get("/docs2/concepts/noi/noi-and-cash-flow-statement")
async def get_concepts_noi_noi_and_cash_flow_statement(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/13-noi-and-cash-flow-statement.html.jinja2",
    )


@router.get("/docs2/concepts/noi/valuation-and-capitalization")
async def get_concepts_noi_valuation_and_capitalization(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/14-valuation-and-capitalization.html.jinja2",
    )


@router.get("/docs2/concepts/noi/exercise-1")
async def get_concepts_noi_exercise_1(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/15-exercise-1.html.jinja2",
    )


@router.get("/docs2/concepts/noi/valuation-tiered-direct-capitalization")
async def get_concepts_noi_valuation_tiered_direct_capitalization(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/16-valuation-tiered-direct-capitalization.html.jinja2",
    )


@router.get("/docs2/concepts/noi/exercise-2")
async def get_concepts_noi_exercise_2(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/17-exercise-2.html.jinja2",
    )


@router.get("/docs2/concepts/noi/valuation-top-slice")
async def get_concepts_noi_valuation_top_slice(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/18-valuation-top-slice.html.jinja2",
    )


@router.get("/docs2/concepts/noi/exercise-3")
async def get_concepts_noi_exercise_3(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/noi/19-exercise-3.html.jinja2",
    )


@router.get("/docs2/concepts/spaces-and-uses/overview")
async def get_concepts_spaces_and_uses_overview(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/10-spaces/01-overview.html.jinja2",
    )


@router.get("/docs2/concepts/spaces-and-uses/spaces")
async def get_concepts_spaces_and_uses_spaces(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/10-spaces/02-spaces.html.jinja2",
    )


@router.get("/docs2/concepts/analysis/overview")
async def get_concepts_analysis_overview(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/analysis/01-overview.html.jinja2",
    )


@router.get("/docs2/concepts/analysis/analysis-period")
async def get_concepts_analysis_analysis_period(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/analysis/02-analysis-period.html.jinja2",
    )


@router.get("/docs2/concepts/analysis/reversionary-value")
async def get_concepts_analysis_reversionary_value(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/analysis/03-reversionary-value.html.jinja2",
    )


@router.get("/docs2/concepts/analysis/valuation-method")
async def get_concepts_analysis_valuation_method(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/analysis/04-valuation-method.html.jinja2",
    )


@router.get("/docs2/concepts/analysis/noi-line-adjustments")
async def get_concepts_analysis_noi_line_adjustments(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/analysis/05-noi-line-adjustments.html.jinja2",
    )


@router.get("/docs2/concepts/analysis/reversionary-capitalization-rate")
async def get_concepts_analysis_reversionary_capitalization_rate(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/analysis/06-reversionary-capitalization-rate.html.jinja2",
    )


@router.get("/docs2/concepts/analysis/value-adjustments")
async def get_concepts_analysis_value_adjustments(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/analysis/07-value-adjustments.html.jinja2",
    )


@router.get("/docs2/concepts/analysis/investment-analysis")
async def get_concepts_analysis_investment_analysis(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="docs/concepts/analysis/08-investment-analysis.html.jinja2",
    )


class MenuRoot(BaseModel):
    children: list[Self] = []


class MenuItem2:
    """Cannot be pydantic type because breaks while mutating in a loop."""
    def __init__(self, title: str, description: str, nav_title: str, nav_group: str, file: str, route: str, page: str):
        self.title = title
        self.description = description
        self.nav_title = nav_title
        self.nav_group = nav_group
        self.file = file
        self.route: str = route
        self.next: Self | None = None
        self.previous: Self | None = None
        self.page = page
        self.selected: bool = False
        self.expanded: bool = False
        self.children = []

    @classmethod
    def try_again(cls, nav: Traversable) -> MenuRoot:

        def recurse(item: str | dict[str, str] | list, path: str = "") -> MenuRoot:
            if isinstance(item, str):
                file = files("returnsuite_website") / "content" / "en" / item
                md = markdown.Markdown(extensions=['meta'])
                md.convert(file.read_text())

                # noinspection PyUnresolvedReferences
                metadata = md.Meta
                return MenuItem2(
                        title=metadata["title"][0],
                        description=metadata["description"][0],
                        nav_title=metadata["nav-title"][0],
                        nav_group=metadata["nav-group"][0],
                        file=item,
                        route=path,
                        page=markdown.markdown(
                            file.read_text(),
                            extensions=[
                                "markdown.extensions.def_list",
                                'meta',
                            ]
                        )
                    )
            elif isinstance(item, dict):
                for entry in item.items():
                    return recurse(entry[1], f"{path}/{entry[0]}")
            elif isinstance(item, list):
                list_root = recurse(item[0], path)
                for child in item[1:]:
                    list_root.children.append(recurse(child, path))
                return list_root

        data = yaml.safe_load(nav.read_bytes())
        menu = recurse(data["nav"])

        # Determine the next and previous from the tree.
        list_representation = []

        def build_list(node: MenuItem2):
            list_representation.append(node)
            if node.children:
                for child in node.children:
                    build_list(child)

        build_list(menu)

        for index, node in enumerate(list_representation[1:-1]):
            node.previous = list_representation[index - 2]
            node.next = list_representation[index + 2]
        return menu



nav_file = files("returnsuite_website") / "content" / "en" / "nav.yml"
pages = MenuItem2.try_again(nav_file)

print(pages)



class PageContent(BaseModel):
    file: str
    route: str

    @classmethod
    def load_pages(cls, nav: Traversable) -> list[Self]:
        pages = []

        def recurse_navigation(item: str | dict[str, str | list], path: str = ""):
            if isinstance(item, str):
                pages.append(PageContent(file=item, route=path))
            elif isinstance(item, dict):
                for entry in item.items():
                    recurse_navigation(entry[1], f"{path}/{entry[0]}")
            elif isinstance(item, list):
                for child in item:
                    recurse_navigation(child, path)

        data = yaml.safe_load(nav.read_bytes())
        recurse_navigation(data["nav"])

        return pages


@router.get("/docs/{path:path}")
def get_docs2(request: Request, path: str):
    return get_docs_locale(request, "en-us", path)


@router.get("/en-au/docs/{path:path}")
def get_docs_en_au(request: Request, path: str):
    return get_docs_locale(request, "en-au", path)


@router.get("/en-ca/docs/{path:path}")
def get_docs_en_ca(request: Request, path: str):
    return get_docs_locale(request, "en-ca", path)


@router.get("/en-gb/docs/{path:path}")
def get_docs_en_gb(request: Request, path: str):
    return get_docs_locale(request, "en-gb", path)


@router.get("/en-nz/docs/{path:path}")
def get_docs_en_nz(request: Request, path: str):
    return get_docs_locale(request, "en-nz", path)


@router.get("/en-us/docs/{path:path}")
def get_docs_en_us(request: Request, path: str):
    return RedirectResponse(request.url_for("get_docs2", path=path))


def get_docs_locale(request: Request, locale: str, path: str):
    #nav_file = files("returnsuite_website") / "content" / "en" / "nav.yml"
    #pages = PageContent.load_pages(nav_file)
    #for page in pages:
#
    #    if page.route.replace("/docs/", "") == path:
    #        file = files("returnsuite_website") / "content" / "en" / page.file
    #        output_html = markdown.markdown(file.read_text(), extensions=["markdown.extensions.def_list", 'meta'])
#
    #        md = markdown.Markdown(extensions=['meta'])
    #        md.convert(file.read_text())
#
    #        # noinspection PyUnresolvedReferences
    #        metadata = md.Meta
#
    #        title = metadata["title"][0]
    #        description = metadata["description"][0]
    #        print(title + description)
#
    #        return templates.TemplateResponse(
    #            request=request,
    #            name="docs.html.jinja2",
    #            context={
    #                "page_title": title,
    #                "description": description,
    #                "content_body": output_html,
    #                "menu": MenuItem2.try_again(nav_file),
    #            }
    #        )

    def find(node: MenuItem2):
        print(f"compare {node.route} == {path}")
        if path in node.route:
            return node
        if node.children:
            for child in node.children:
                result = find(child)
                if result is not None:
                    return result
            return None
        else:
            return None

    page = find(pages)
    if not page:
        raise FileNotFoundError()

    return templates.TemplateResponse(
        request=request,
        name="docs.html.jinja2",
        context={
            "page": page,
            "page_title": page.title,
            "description": page.description,
            "content_body": page.page,
            "menu": pages,
        }
    )
