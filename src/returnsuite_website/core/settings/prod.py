from pydantic_settings import SettingsConfigDict

from returnsuite_website.core.settings.app import AppSettings


class ProdAppSettings(AppSettings):
    model_config = SettingsConfigDict(env_file="prod.env")
