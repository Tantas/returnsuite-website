import logging
import sys
from datetime import UTC, datetime
from typing import Any

from loguru import logger
from pydantic import SecretStr
from pydantic_settings import SettingsConfigDict

from returnsuite_website.core.logging import InterceptHandler
from returnsuite_website.core.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    model_config = SettingsConfigDict(validate_assignment=True)
    debug: bool = False
    title: str = "ReturnSuite"
    version: str = "1.0.0"

    app_website: str = "https://app.returnsuite.com"
    compress_web_responses: bool = True
    proxy_header_trusted_hosts: list[str] | str | None = "*"
    html_live_reload: bool = False
    css_version: str = str(round(datetime.now(UTC).timestamp()))
    google_tag: str | None = "G-7VZZ355CPV"

    smtp_enabled: bool = True
    smtp_use_ssl: bool = True
    smtp_aws_arn: str | None = None
    smtp_host: str = "email-smtp.us-east-1.amazonaws.com:465"
    smtp_user: str | None = None
    smtp_password: SecretStr | None = None
    smtp_from: str = "ReturnSuite <noreply@returnsuite.com>"

    create_database: bool = True
    database_url: SecretStr

    landing_contact_email: list[str] = ("info@returnsuite.com",)
    landing_waitlist_email: list[str] = ("info@returnsuite.com",)
    signup_enabled: bool = True
    hide_docs: bool = True
    hide_demo: bool = True

    logging_level: int = logging.INFO
    loggers: tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    @property
    def fastapi_kwargs(self) -> dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": "/api",
            "openapi_prefix": "",
            "openapi_url": "/openapi.json",
            "redoc_url": "/reapi",
            "title": self.title,
            "version": self.version,
        }

    def configure_logging(self) -> None:
        logging.root.handlers = [InterceptHandler()]
        logging.root.setLevel(self.logging_level)

        for name in logging.root.manager.loggerDict.keys():
            logging.getLogger(name).handlers = []
            logging.getLogger(name).propagate = True

        logger.configure(handlers=[{"sink": sys.stdout}])
