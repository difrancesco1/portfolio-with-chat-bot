from http.client import HTTPException
from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.exc import SQLAlchemyError
import os

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_async_engine(DATABASE_URL)

async def check_db_tables():
    async with engine.connect() as conn:
        result = await conn.execute(
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
async def db_health_check():
    try:
        tables = await check_db_tables()
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