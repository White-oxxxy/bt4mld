from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)
from pydantic import Field


class PgSettings(BaseSettings):
    """
    крч эта типа вот вариант реализации настроек типа для твоего приложения
    тут мы будем с помощью убого пидантика из енв файлов подтягивать данные вот крч
    это конкретно данные которые для постгреса нужны
    """

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parents[2] / ".dev.env"),
        extra="ignore",
    )

    db: str = Field(default="bt4mld", alias="PG_DB")
    user: str = Field(default="admin", alias="PG_USER")
    password: str = Field(default="admin", alias="PG_PASSWORD")
    host: str = Field(default="bt4mld", alias="PG_HOST")
    port: str = Field(default="5432", alias="PG_PORT")

    @property
    def postgres_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"

    @property
    def migration_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@localhost:45432/{self.db}"


class Settings(BaseSettings):
    """
    нууу ээээ это типа класс которые в себе агрегирует настройки отдельных частей ну у нас тк все проста
    у нас будет ток для постгреса и редиса но так их больше бывает
    """

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parents[2] / ".dev.env"),
        extra="ignore",
    )

    pg: PgSettings = PgSettings()