import logging

from pydantic_settings import SettingsConfigDict

from returnsuite_website.core.settings.app import AppSettings


class StageAppSettings(AppSettings):
    model_config = SettingsConfigDict(env_file="stage.env")
    title: str = "Stage"
    server_url: str = "https://stage.returnsuite.com"
    google_tag: str | None = None
    app_website: str = "https://appstage.returnsuite.com"

    smtp_from: str = "Stage ReturnSuite <noreply@stage.returnsuite.com>"
    landing_contact_email: list[str] = ("testing@returnsuite.com",)
    landing_waitlist_email: list[str] = ("testing@returnsuite.com",)

    ensure_seed_data: bool = True
    run_migrations: bool = True

    logging_level: int = logging.INFO
