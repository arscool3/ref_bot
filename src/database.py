from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker


class DbSettings(BaseSettings):
    url: str

    class Config:
        env_prefix = "DATABASE_"


settings = DbSettings()

# Create an async engine
async_engine = create_async_engine(settings.url)

# Create async session
async_session = AsyncSession(async_engine, expire_on_commit=False)
