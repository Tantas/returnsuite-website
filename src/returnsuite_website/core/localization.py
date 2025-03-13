from pathlib import Path

import i18n
from babel.core import Locale
from babel.dates import format_date as babel_format_date
from babel.numbers import format_currency as babel_format_currency
from babel.numbers import format_decimal as babel_format_decimal
from babel.numbers import format_percent as babel_format_percent
from babel.numbers import get_currency_symbol as babel_get_currency_symbol

from returnsuite_website.core.config import get_app_settings
from returnsuite_website.core.settings.base import AppEnvTypes

i18n.set("file_format", "yml")
i18n.set("fallback", "en_US")

if get_app_settings().app_env == AppEnvTypes.prod:
    i18n.set("enable_memoization", True)
else:
    i18n.set("error_on_missing_translation", True)

package_root = Path(__file__).parent.parent.resolve()
i18n.load_path.append(f"{package_root}/resources/localization")


def localize(value, locale: Locale, **kwargs) -> str:
    return i18n.t("messages.%s" % value, locale=str(locale), **kwargs)


def format_date_medium(value, locale: Locale) -> str:
    return babel_format_date(value, format="medium", locale=locale)


def format_date_long(value, locale: Locale) -> str:
    return babel_format_date(value, format="long", locale=locale)


def format_currency_symbol(value: str, locale: Locale) -> str:
    return babel_get_currency_symbol(value, locale)


def format_currency(value, currency: str, locale: Locale) -> str:
    # for currency_locale in currency_info():
    #     if currency_locale[0] == currency.upper():
    #         return babel_format_currency(
    #             number=value,
    #             currency=currency_locale[0],
    #             locale=currency_locale[1],
    #         )
    return babel_format_currency(value, currency.upper(), locale=locale)
