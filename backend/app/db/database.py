# backend/app/db.py
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.config import settings

# Асинхронный движок
engine = create_async_engine(
    settings.database_url_async,
    echo=True,
)

# Асинхронный sessionmaker
AsyncSessionLocal = async_sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


# Функция-депенденси для FastAPI
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
