from datetime import UTC, datetime, tzinfo
from pathlib import Path

import i18n
from babel.core import Locale

# noinspection PyProtectedMember
from babel.dates import format_date as babel_format_date
from babel.dates import format_datetime as babel_format_datetime
from babel.dates import format_timedelta as babel_format_timedelta
from babel.numbers import format_currency as babel_format_currency
from babel.numbers import format_decimal as babel_format_decimal
from babel.numbers import get_currency_symbol as babel_get_currency_symbol
from babel.numbers import get_territory_currencies

from returnsuite_website.core.config import get_app_settings
from returnsuite_website.core.settings.base import AppEnvTypes

# class RuamelYamlLoader(Loader):
#     def __init__(self):
#         super(RuamelYamlLoader, self).__init__()
#         self.yaml = YAML(typ="safe", pure=True)
#
#     def parse_file(self, file_content):
#         try:
#             return self.yaml.load(file_content)
#         except ScannerError as e:
#             raise I18nFileLoadError(f"Invalid YAML: {str(e)}")


# register_loader(RuamelYamlLoader, ["yml", "yaml"])
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


def supported_currencies() -> list[str]:
    return [
        "AUD",
        "CAD",
        "CHF",
        "EUR",
        "GBP",
        "JPY",
        "MXN",
        "NZD",
        "USD",
        "ZAR",
    ]


def get_currency_for_territory(territory: str | None) -> str:
    if territory:
        currencies = get_territory_currencies(territory, start_date=datetime.now(UTC))
        if len(currencies):
            main_currency = currencies[0]
            if main_currency in supported_currencies():
                return main_currency
    return "USD"


def get_currency_symbol_and_name(currency: str, locale: Locale) -> str:
    return f"{babel_get_currency_symbol(currency, locale)} {currency}"


def format_currency(value, currency: str, locale: Locale) -> str:
    return babel_format_currency(value, currency.upper(), locale=locale)


def format_currency_short(value, currency, locale: Locale) -> str:
    def _is_integer(numeric_value):
        return numeric_value.as_integer_ratio()[1] == 1

    if _is_integer(value):
        return babel_format_currency(
            value,
            currency.upper(),
            locale=locale,
            format="¤ #,##0",
            currency_digits=False,
        )
    else:
        return format_currency(value, currency, locale)


def format_count(value, locale: Locale) -> str:
    return babel_format_decimal(value, locale=locale)


def format_date_medium(value, locale: Locale) -> str:
    return babel_format_date(value, format="medium", locale=locale)


def format_date_long(value, locale: Locale) -> str:
    return babel_format_date(value, format="long", locale=locale)


# def format_datetime_as_date_medium(value, locale, timezone: tzinfo = None) -> str:
#     if timezone is None:
#         timezone = pytz.UTC
#     timezone_corrected = _ensure_datetime_tzinfo(_get_datetime(value), timezone)
#     return babel_format_date(timezone_corrected, format="medium", locale=locale)


def format_datetime_long(value, locale: Locale, timezone: tzinfo = None) -> str:
    return babel_format_datetime(value, format="long", locale=locale, tzinfo=timezone)


def format_datetime_medium(value, locale: Locale, timezone: tzinfo = None) -> str:
    return babel_format_datetime(value, format="medium", locale=locale, tzinfo=timezone)


def format_datetime_short(value, locale: Locale, timezone: tzinfo = None) -> str:
    return babel_format_datetime(value, format="short", locale=locale, tzinfo=timezone)


def format_timedelta(value, locale: Locale) -> str:
    return babel_format_timedelta(value, locale=locale)


def format_timezone(value: str) -> str:
    return value.replace("/", " / ").replace("_", " ")


def format_locale(value: str, locale: Locale | str) -> str | None:
    return Locale.parse(value).get_display_name(locale)  # type: ignore
