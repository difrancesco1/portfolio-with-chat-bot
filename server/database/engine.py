from sqlalchemy.ext.asyncio import create_async_engine
from core.config import get_config

config = get_config()

engine = create_async_engine(
    config.DATABASE_URL,
    echo=config.DEBUG,
    max_overflow=config.DB_MAX_OVERFLOW,
    pool_size=config.DB_POOL_SIZE,
    pool_pre_ping=True
)