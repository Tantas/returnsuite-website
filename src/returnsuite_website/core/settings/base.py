from enum import Enum

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppEnvTypes(str, Enum):
    prod = "prod"
    stage = "stage"
    dev = "dev"
    test = "test"


class BaseAppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    app_env: AppEnvTypes = AppEnvTypes.dev
