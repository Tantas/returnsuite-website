from functools import lru_cache

from returnsuite_website.core.settings.app import AppSettings
from returnsuite_website.core.settings.base import AppEnvTypes, BaseAppSettings
from returnsuite_website.core.settings.dev import DevAppSettings
from returnsuite_website.core.settings.prod import ProdAppSettings
from returnsuite_website.core.settings.stage import StageAppSettings
from returnsuite_website.core.settings.test import TestAppSettings

environments: dict[AppEnvTypes, type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings,
    AppEnvTypes.prod: ProdAppSettings,
    AppEnvTypes.stage: StageAppSettings,
    AppEnvTypes.test: TestAppSettings,
}


@lru_cache
def get_app_settings() -> AppSettings:
    config = environments[BaseAppSettings().app_env]
    return config()
