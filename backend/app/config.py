from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "NoteFlow"
    debug: bool = True
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/noteflow"
    cors_origins: list = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
    static_dir: str = "static"
    images_dir: str = "static_images"

    class Config:
        env_file = "app/.env"


settings = Settings()
