import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from schemas import (
    BiographyResponse,
    BiographyCreate,
    BiographyUpdate,
    BulletPointCreate,
    BulletPointResponse,
    BiographyBulletPointResponse,
    DocumentResponse,
    EducationCreate,
    EducationResponse,
    EducationUpdate,
    EducationBulletPointResponse,
    EmploymentCreate,
    EmploymentResponse,
    EmploymentUpdate,
    EmploymentBulletPointResponse,
    ExperienceCreate,
    ExperienceResponse,
    ExperienceUpdate,
    ExperienceBulletPointResponse,
    LinkCreate,
    PortfolioCreate,
    PortfolioResponse,
    PortfolioFullResponse,
    PortfolioUpdate,
    ProjectResponse,
    ProjectCreate,
    ProjectUpdate,
    TagCreate
)
from services.portfolio_service import PortfolioService
from database.session import get_db

admin_router = APIRouter(prefix="/admin", tags=["admin"])
    
@admin_router.get("/{portfolio_pid}/all/biography", response_model=list[BiographyResponse])
async def get_biography_all(
    portfolio_pid: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.get_biography_all(portfolio_pid=portfolio_pid)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    
@admin_router.post("/{portfolio_pid}/add/biography", response_model=BiographyResponse)
async def add_biography(
    portfolio_pid: uuid.UUID,
    bio_data: BiographyCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.add_biography(
            portfolio_pid=portfolio_pid, 
            bio_data=bio_data
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

@admin_router.post("/{portfolio_pid}/biography/{biography_pid}/add/bullet_point", response_model=BiographyBulletPointResponse)
async def add_biography_bullet_point(
    portfolio_pid: uuid.UUID,
    biography_pid:uuid.UUID,
    bp_data: BulletPointCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.add_biography_bullet_point(
            portfolio_pid=portfolio_pid,
            biography_pid=biography_pid,
            bp_data=bp_data    
        )
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))

@admin_router.post("/{portfolio_pid}/add/document", response_model=DocumentResponse)
async def add_document(
    portfolio_pid: uuid.UUID,
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):
    data = await file.read()
    service = PortfolioService(db)
    try:
        return await service.add_document(
            portfolio_pid=portfolio_pid,
            file_name=file.filename,
            content_type=file.content_type,
            data=data
        )
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))

@admin_router.post("/{portfolio_pid}/add/education", response_model=EducationResponse)
async def add_education(
    portfolio_pid: uuid.UUID,
    edu_data: EducationCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.add_education(
            portfolio_pid=portfolio_pid, 
            edu_data=edu_data
        )
    except ValueError as error:
        raise HTTPException(status_code=400, details=str(error))

@admin_router.post("/{portfolio_pid}/education/{education_pid}/add/bullet_point", response_model=EducationBulletPointResponse)
async def add_education_bullet_point(
    portfolio_pid: uuid.UUID,
    education_pid: uuid.UUID,
    bp_data: BulletPointCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.add_education_bullet_point(
            portfolio_pid=portfolio_pid,
            education_pid=education_pid,
            bp_data=bp_data    
        )
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))
    
@admin_router.post("/{portfolio_pid}/add/employment", response_model=EmploymentResponse)
async def add_employment(
    portfolio_pid: uuid.UUID,
    emp_data: EmploymentCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.add_employment(
            portfolio_pid=portfolio_pid, 
            emp_data=emp_data
        )
    except ValueError as error:
        raise HTTPException(status_code=400, details=str(error))


@admin_router.post("/{portfolio_pid}/employment/{employment_pid}/add/bullet_point", response_model=EmploymentBulletPointResponse)
async def add_employment_bullet_point(
    portfolio_pid: uuid.UUID,
    employment_pid: uuid.UUID,
    bp_data: BulletPointCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.add_employment_bullet_point(
            portfolio_pid=portfolio_pid,
            employment_pid=employment_pid,
            bp_data=bp_data    
        )
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))
        
@admin_router.post("/{portfolio_pid}/add/experience", response_model=ExperienceResponse)
async def add_experience(
    portfolio_pid: uuid.UUID,
    exp_data: ExperienceCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.add_experience(
            portfolio_pid=portfolio_pid, 
            exp_data=exp_data
        )
    except ValueError as error:
        raise HTTPException(status_code=400, details=str(error))


@admin_router.post("/{portfolio_pid}/experience/{experience_pid}/add/bullet_point", response_model=ExperienceBulletPointResponse)
async def add_experience_bullet_point(
    portfolio_pid: uuid.UUID,
    experience_pid: uuid.UUID,
    bp_data: BulletPointCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.add_experience_bullet_point(
            portfolio_pid=portfolio_pid,
            experience_pid=experience_pid,
            bp_data=bp_data    
        )
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))

@admin_router.post("/{portfolio_pid}/add/link", response_model=PortfolioFullResponse)
async def add_portfolio_link(
    portfolio_pid: uuid.UUID,
    link_data: LinkCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.add_portfolio_link(
            portfolio_pid=portfolio_pid,
            link_data=link_data
        )
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))
    
@admin_router.post("/{portfolio_pid}/add/project", response_model=ProjectResponse)
async def add_project(
    portfolio_pid: uuid.UUID,
    project_data: ProjectCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.add_project(
            portfolio_pid=portfolio_pid, 
            project_data=project_data
        )
    except ValueError as error:
        raise HTTPException(status_code=400, details=str(error))

@admin_router.post("/{portfolio_pid}/add/project/{project_pid}/link", response_model=ProjectResponse)
async def add_project_link(
    portfolio_pid: uuid.UUID,
    project_pid: uuid.UUID,
    link_data: LinkCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.add_project_link(
            portfolio_pid=portfolio_pid,
            project_pid=project_pid,
            link_data=link_data
        )
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))

@admin_router.post("/{portfolio_pid}/add/project/{project_pid}/tag", response_model=ProjectResponse)
async def add_project_tag(
    portfolio_pid: uuid.UUID,
    project_pid: uuid.UUID,
    tag_data: TagCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.add_project_tag(
            portfolio_pid=portfolio_pid,
            project_pid=project_pid,
            tag_data=tag_data
        )
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))
     
@admin_router.post("/create/portfolio", response_model=PortfolioResponse)
async def create_portfolio(
    data: PortfolioCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.create_portfolio(data)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

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

@admin_router.delete("/{portfolio_pid}/delete/biography/{biography_pid}", status_code=204)
async def delete_portfolio_biography(
    portfolio_pid: uuid.UUID,
    biography_pid: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        await service.delete_biography(portfolio_pid, biography_pid)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))

@admin_router.delete("/{portfolio_pid}/biography/{biography_pid}/delete/bullet_point/{bp_pid}", status_code=204)
async def delete_biography_bullet_point(
    portfolio_pid: uuid.UUID,
    biography_pid: uuid.UUID,
    bp_pid: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        await service.delete_biography_bullet_point(
            portfolio_pid=portfolio_pid,
            biography_pid=biography_pid,
            bp_pid=bp_pid
        )
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

@admin_router.delete("/{portfolio_pid}/education/{education_pid}/delete/bullet_point/{bp_pid}", status_code=204)
async def delete_education_bullet_point(
    portfolio_pid: uuid.UUID,
    education_pid: uuid.UUID,
    bp_pid: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        await service.delete_education_bullet_point(
            portfolio_pid=portfolio_pid,
            education_pid=education_pid,
            bp_pid=bp_pid
        )
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

@admin_router.delete("/{portfolio_pid}/employment/{employment_pid}/delete/bullet_point/{bp_pid}", status_code=204)
async def delete_employment_bullet_point(
    portfolio_pid: uuid.UUID,
    employment_pid: uuid.UUID,
    bp_pid: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        await service.delete_employment_bullet_point(
            portfolio_pid=portfolio_pid,
            employment_pid=employment_pid,
            bp_pid=bp_pid
        )
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
    
@admin_router.delete("/{portfolio_pid}/experience/{experience_pid}/delete/bullet_point/{bp_pid}", status_code=204)
async def delete_experience_bullet_point(
    portfolio_pid: uuid.UUID,
    experience_pid: uuid.UUID,
    bp_pid: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        await service.delete_experience_bullet_point(
            portfolio_pid=portfolio_pid,
            experience_pid=experience_pid,
            bp_pid=bp_pid
        )
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    
@admin_router.delete("/{portfolio_pid}/delete/project/{project_pid}", status_code=204)
async def delete_portfolio_project(
    portfolio_pid: uuid.UUID,
    project_pid: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        await service.delete_project(
            portfolio_pid=portfolio_pid, 
            project_pid=project_pid
        )
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    
@admin_router.patch("/{portfolio_pid}/update/biography/{biography_pid}", response_model=BiographyResponse)
async def update_biography(
    portfolio_pid: uuid.UUID,
    biography_pid: uuid.UUID,
    update_data: BiographyUpdate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.update_biography(
            portfolio_pid=portfolio_pid,
            biography_pid=biography_pid,
            update_data=update_data
        )
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))
    
@admin_router.patch("/{portfolio_pid}/update/education/{education_pid}", response_model=EducationResponse)
async def update_education(
    portfolio_pid: uuid.UUID,
    education_pid: uuid.UUID,
    update_data: EducationUpdate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.update_education(
            portfolio_pid=portfolio_pid,
            education_pid=education_pid,
            update_data=update_data
        )
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))
    
@admin_router.patch("/{portfolio_pid}/update/employment/{employment_pid}", response_model=EmploymentResponse)
async def update_employment(
    portfolio_pid: uuid.UUID,
    employment_pid: uuid.UUID,
    update_data: EmploymentUpdate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.update_employment(
            portfolio_pid=portfolio_pid,
            employment_pid=employment_pid,
            update_data=update_data
        )
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))
    
@admin_router.patch("/{portfolio_pid}/update/experience/{experience_pid}", response_model=ExperienceResponse)
async def update_experience(
    portfolio_pid: uuid.UUID,
    experience_pid: uuid.UUID,
    update_data: ExperienceUpdate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.update_experience(
            portfolio_pid=portfolio_pid,
            experience_pid=experience_pid,
            update_data=update_data
        )
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))

@admin_router.patch("/{portfolio_pid}/update/portfolio", response_model=PortfolioFullResponse)
async def update_portfolio(
    portfolio_pid: uuid.UUID,
    update_data: PortfolioUpdate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.update_portfolio(
            portfolio_pid=portfolio_pid,
            update_data=update_data
        )
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))

@admin_router.patch("/{portfolio_pid}/update/project/{project_pid}", response_model=ProjectResponse)
async def update_project(
    portfolio_pid: uuid.UUID,
    project_pid: uuid.UUID,
    update_data: ProjectUpdate,
    db: AsyncSession = Depends(get_db)
):
    service = PortfolioService(db)
    try:
        return await service.update_project(
            portfolio_pid=portfolio_pid,
            project_pid=project_pid,
            update_data=update_data
        )
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))