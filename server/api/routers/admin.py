import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from schemas.portfolio import (
    BiographyResponse,
    BiographyCreate,
    EducationCreate,
    EducationResponse,
    EmploymentCreate,
    EmploymentResponse,
    ExperienceCreate,
    ExperienceResponse,
    PortfolioCreate,
    PortfolioResponse,
    PortfolioFullResponse,
)
from services.portfolio_service import PortfolioService
from database.session import get_db

admin_router = APIRouter(prefix="/admin", tags=["admin"])

@admin_router.post("/{portfolio_pid}/add/biography", response_model=BiographyResponse)
async def add_biography(
    portfolio_pid: uuid.UUID,
    bio_data: BiographyCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.add_biography(portfolio_pid, bio_data)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

@admin_router.post("/{portfolio_pid}/add/education", response_model=EducationResponse)
async def add_education(
    portfolio_pid: uuid.UUID,
    edu_data: EducationCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.add_education(portfolio_pid, edu_data)
    except ValueError as error:
        raise HTTPException(status_code=400, details=str(error))
    
@admin_router.post("/{portfolio_pid}/add/employment", response_model=EmploymentResponse)
async def add_employment(
    portfolio_pid: uuid.UUID,
    emp_data: EmploymentCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.add_employment(portfolio_pid, emp_data)
    except ValueError as error:
        raise HTTPException(status_code=400, details=str(error))
    
@admin_router.post("/{portfolio_pid}/add/experience", response_model=ExperienceResponse)
async def add_experience(
    portfolio_pid: uuid.UUID,
    exp_data: ExperienceCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.add_experience(portfolio_pid, exp_data)
    except ValueError as error:
        raise HTTPException(status_code=400, details=str(error))
    
@admin_router.post("/create/portfolio", response_model=PortfolioResponse)
async def create_portfolio(
    data: PortfolioCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.create_portfolio(data.email)
    except ValueError as error:
        raise HTTPException(status_code=400, details=str(error))

@admin_router.delete("/{portfolio_pid}", status_code=204)
async def delete_portfolio(
    portfolio_pid: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        await service.delete_portfolio(portfolio_pid)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    
@admin_router.delete("/{portfolio_pid}/delete/education/{education_pid}", status_code=204)
async def delete_portfolio_education(
    portfolio_pid: uuid.UUID,
    education_pid: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        await service.delete_education(portfolio_pid, education_pid)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    
@admin_router.delete("/{portfolio_pid}/delete/employment/{employment_pid}", status_code=204)
async def delete_portfolio_employment(
    portfolio_pid: uuid.UUID,
    employment_pid: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        await service.delete_employment(portfolio_pid, employment_pid)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    
@admin_router.delete("/{portfolio_pid}/delete/experience/{experience_pid}", status_code=204)
async def delete_portfolio_experience(
    portfolio_pid: uuid.UUID,
    experience_pid: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        await service.delete_experience(portfolio_pid, experience_pid)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))