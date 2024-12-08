from datetime import UTC, datetime
from pathlib import Path

from babel import Locale
from fastapi.templating import Jinja2Templates

from returnsuite_website.core.config import get_app_settings
from returnsuite_website.core.localization import (
    format_date_long,
    format_date_medium,
    localize,
)

package_root = Path(__file__).parent.parent.resolve()
templates = Jinja2Templates(directory=f"{package_root}/templates")
templates.env.add_extension("jinja2.ext.do")
templates.env.globals["html_live_reload"] = get_app_settings().html_live_reload
templates.env.globals["css_version"] = get_app_settings().css_version
templates.env.trim_blocks = True
templates.env.lstrip_blocks = True

# Fixed locale until more supported. Pull from accept header / user in the future.
templates.env.globals["locale"] = Locale.parse("en", "US")

templates.env.globals["app_title"] = get_app_settings().title
templates.env.globals["app_website"] = get_app_settings().app_website
templates.env.globals["signup_enabled"] = get_app_settings().signup_enabled
templates.env.globals["hide_docs"] = get_app_settings().hide_docs
templates.env.globals["hide_demo"] = get_app_settings().hide_demo
templates.env.globals["google_tag"] = get_app_settings().google_tag


def _now():
    return datetime.now(UTC)


def analytics_consent(accept_language: str | None) -> bool:
    if accept_language is None or accept_language == "":
        return True
    if (
        "US" in accept_language
        or "CA" in accept_language
        or "AU" in accept_language
        or "NZ" in accept_language
        or "MX" in accept_language
        or "JP" in accept_language
    ):
        return False
    return True


templates.env.globals["_"] = localize
templates.env.globals["now"] = _now
templates.env.filters["analytics_consent"] = analytics_consent
templates.env.filters["format_date_medium"] = format_date_medium
templates.env.filters["format_date_long"] = format_date_long
