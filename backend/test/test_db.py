import asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from backend.app.config import settings


async def test_connection():
    engine = create_async_engine(settings.database_url_async, echo=True)
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 1"))
        print("Connection test result:", result.scalar())


if __name__ == "__main__":
    asyncio.run(test_connection())
