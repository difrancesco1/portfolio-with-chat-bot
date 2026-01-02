import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from schemas.portfolio import (
    EducationCreate,
    EducationResponse,
    EmploymentCreate,
    EmploymentResponse,
    ExperienceCreate,
    ExperienceResponse,
    PortfolioCreate,
    PortfolioResponse,
    PortfolioEducationResponse,
    PortfolioEmploymentResponse,
    PortfolioExperienceResponse,
    PortfolioFullResponse,
)
from services.portfolio_service import PortfolioService
from database.session import get_db

from api.routers.admin import admin_router
from core.config import get_config

config = get_config()

router = APIRouter(prefix="/portfolio", tags=["portfolio"])

if config.DEBUG: 
    router.include_router(admin_router)

@router.get("/{portfolio_pid}/education/all", response_model=list[EducationResponse])
async def get_all_educations(
    portfolio_pid: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.get_education_all(portfolio_pid)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

@router.get("/{portfolio_pid}/education/{education_pid}", response_model=EducationResponse)
async def get_education_by_pid(
    portfolio_pid: uuid.UUID,
    education_pid: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.get_education_by_pid(portfolio_pid, education_pid)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    
@router.get("/{portfolio_pid}/employment/all", response_model=list[EmploymentResponse])
async def get_all_employment(
    portfolio_pid: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.get_employment_all(portfolio_pid)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

@router.get("/{portfolio_pid}/employment/{employment_pid}", response_model=EmploymentResponse)
async def get_employment_by_pid(
    portfolio_pid: uuid.UUID,
    employment_pid: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.get_employment_by_pid(portfolio_pid, employment_pid)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    
@router.get("/{portfolio_pid}/experience/all", response_model=list[ExperienceResponse])
async def get_all_experience(
    portfolio_pid: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.get_experience_all(portfolio_pid)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    
@router.get("/{portfolio_pid}/experience/{experience_pid}", response_model=ExperienceResponse)
async def get_experience_by_pid(
    portfolio_pid: uuid.UUID,
    experience_pid: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.get_experience_by_pid(portfolio_pid, experience_pid)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))