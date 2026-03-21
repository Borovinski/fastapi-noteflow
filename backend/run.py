import os
from alembic.config import Config
from alembic import command
import uvicorn

from app.config import settings


def run_migrations():
    # alembic.ini лежит в той же папке, что и run.py
    alembic_ini_path = os.path.join(os.path.dirname(__file__), "alembic.ini")
    alembic_cfg = Config(alembic_ini_path)
    command.upgrade(alembic_cfg, "head")


if __name__ == "__main__":
    run_migrations()

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
        log_level="info",
    )
