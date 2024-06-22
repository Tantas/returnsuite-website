from pathlib import Path

import i18n
from babel.core import Locale
from babel.dates import format_date as babel_format_date

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
