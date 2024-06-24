import logging

from pydantic import SecretStr
from pydantic_settings import SettingsConfigDict

from returnsuite_website.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    model_config = SettingsConfigDict(env_file=".env")
    debug: bool = True
    title: str = "Development"
    server_url: str = "http://localhost:8000"
    google_tag: str | None = None

    app_website: str = "http://localhost:8080"
    html_live_reload: bool = True

    database_url: SecretStr = SecretStr("sqlite://")

    smtp_use_ssl: bool = False
    smtp_host: str = "localhost:1025"
    smtp_from: str = "Local ReturnSuite <noreply@local.returnsuite.com>"

    logging_level: int = logging.DEBUG
