from pathlib import Path
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

# path так как env находится в файле корня проекта
BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    app_name: str = "NoteFlow"
    debug: bool = True
    # БД и значения по умолчанию
    DB_HOST: str = ""
    DB_PORT: int = 0
    DB_USER: str = ""
    DB_PASS: str = ""
    DB_NAME: str = ""
    # cors-пути для доступа
    CORS_ORIGINS: List[str] = []
    # пути для сторонних директорий
    static_dir: str = "static"
    images_dir: str = "static_images"

    # Генерации URL
    # async
    @property
    def database_url_async(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    # sync
    @property
    def database_url_sync(self) -> str:
        return (
            f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    # создание модели конфигурации
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


# экспортируемая переменная настроек
settings = Settings()
