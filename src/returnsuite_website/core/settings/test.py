from pydantic import SecretStr
from pydantic_settings import SettingsConfigDict

from returnsuite_website.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    model_config = SettingsConfigDict(env_file=".test.env")
    debug: bool = True
    title: str = "Test"
    smtp_enabled: bool = False
    database_url: SecretStr = SecretStr("sqlite://")
