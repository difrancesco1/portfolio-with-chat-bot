import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from schemas import (
    BiographyResponse,
    BiographyCreate,
    BulletPointCreate,
    BulletPointResponse,
    BiographyBulletPointResponse,
    EducationCreate,
    EducationResponse,
    EmploymentCreate,
    EmploymentResponse,
    ExperienceCreate,
    ExperienceResponse,
    LinkResponse,
    PortfolioCreate,
    PortfolioResponse,
)
from services.portfolio_service import PortfolioService
from database.session import get_db

debug_router = APIRouter(prefix="/debug", tags=["debug"])

@debug_router.get("/all/biography", response_model=list[BiographyResponse])
async def get_biography_all_debug(db: AsyncSession = Depends(get_db)):
    service = PortfolioService(db)
    try:
        return await service.debug_bio_all()
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))

@debug_router.get("/all/biography/bullet_points", response_model=list[BiographyBulletPointResponse])
async def get_biography_all_debug(db: AsyncSession = Depends(get_db)):
    service = PortfolioService(db)
    try:
        return await service.debug_bio_bp_all()
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))
    
@debug_router.get("/all/bullet_points", response_model=list[BulletPointResponse])
async def get_all_bullet_points(db: AsyncSession = Depends(get_db)):
    service = PortfolioService(db)
    try:
        return await service.debug_all_bp()
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))
    
@debug_router.delete("/clear/all/bullet_points", status_code=204)
async def clear_all_bullet_points(db: AsyncSession = Depends(get_db)):
    service = PortfolioService(db)
    try:
        return await service.debug_clear_bp_tables()
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))
    
@debug_router.get("/all/links", response_model=list[LinkResponse])
async def get_all_links(db: AsyncSession = Depends(get_db)):
    service = PortfolioService(db)
    try:
        return await service.debug_all_links()
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))