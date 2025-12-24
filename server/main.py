from http.client import HTTPException
from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import get_config
from database.session import get_db

config = get_config()

app = FastAPI(
    title=config.APP_NAME,
    debug=config.DEBUG
)

async def check_db_tables(db: AsyncSession):
    result = await db.execute(
        text(
            """
            SELECT tablename
            FROM pg_catalog.pg_tables
            WHERE schemaname = 'public';
            """
        )
    )

    tables = [row[0] for row in result.fetchall()]
    return tables

@app.get("/db")
async def db_health_check(db: AsyncSession = Depends(get_db)):
    try:
        tables = await check_db_tables(db)
        return {
            "status": "ok",
            "database": "connected",
            "tables": tables,
        }
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )