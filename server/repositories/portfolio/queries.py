import uuid
from sqlalchemy import exists, select
from sqlalchemy.ext.asyncio import AsyncSession
from models import (
    Biography,
    BiographyBulletPoint,
    BulletPoint,
    Document,
    Education,
    EducationBulletPoint,
    Employment,
    EmploymentBulletPoint,
    Experience,
    ExperienceBulletPoint,
    Portfolio,
    Project
)
from .loaders import (
    BIOGRAPHY_WITH_BULLETS,
    BIOGRAPHY_BULLET_POINT_LOAD,
    EDUCATION_WITH_BULLETS,
    EDUCATION_BULLET_POINT_LOAD,
    EMPLOYMENT_WITH_BULLETS,
    EMPLOYMENT_BULLET_POINT_LOAD,
    EXPERIENCE_WITH_BULLETS,
    EXPERIENCE_BULLET_POINT_LOAD,
    PORTFOLIO_FULL,
    PROJECT_FULL
)

class PortfolioQueries:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_full_portfolios(self) -> list[Portfolio] | None:
        stmt = select(Portfolio).options(*PORTFOLIO_FULL)
        results = await self.session.execute(stmt)
        return results.scalars().all()
    
    async def get_by_email(self, email: str) -> Portfolio | None:
        stmt = select(Portfolio).where(Portfolio.email == email)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_by_pid(self, portfolio_pid: uuid.UUID) -> Portfolio:
        stmt = select(Portfolio).where(Portfolio.pid == portfolio_pid)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_biography(self, portfolio_id: int) -> Biography | None:
        stmt = select(Biography).where(
            Biography.portfolio_id == portfolio_id
        ).options(BIOGRAPHY_WITH_BULLETS)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_biography_all(self, portfolio_id: int) -> list[Biography]:
        stmt = select(Biography).where(Biography.portfolio_id == portfolio_id).options(BIOGRAPHY_WITH_BULLETS)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def get_biography_by_pid(
        self, portfolio_id: int, biography_pid: uuid.UUID
    ) -> Biography | None:
        stmt = select(Biography).where(
            Biography.portfolio_id == portfolio_id,
            Biography.pid == biography_pid
        ).options(BIOGRAPHY_WITH_BULLETS)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_biography_bullet_point(
        self, biography_id: int, bullet_point_id: int
    ) -> BiographyBulletPoint | None:
        stmt = select(BiographyBulletPoint).where(
            BiographyBulletPoint.biography_id == biography_id,
            BiographyBulletPoint.bullet_point_id == bullet_point_id
        ).options(BIOGRAPHY_BULLET_POINT_LOAD)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    # Possibly move to mutations!
    async def get_bullet_point_by_pid(self, bp_pid: uuid.UUID) -> BulletPoint | None:
        stmt = select(BulletPoint).where(BulletPoint.pid == bp_pid)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_document_by_pid(
        self, portfolio_id:int, document_pid: uuid.UUID
    ) -> Document | None:
        stmt = select(Document).where(
            Document.portfolio_id == portfolio_id,
            Document.pid == document_pid
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_education_all(self, portfolio_id: int) -> list[Education] | None:
        stmt = select(Education).where(Education.portfolio_id == portfolio_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def get_education_by_pid(
        self, portfolio_id: int, education_pid: uuid.UUID
    ) -> Education | None:
        stmt = select(Education).where(
            Education.portfolio_id == portfolio_id,
            Education.pid == education_pid
        ).options(EDUCATION_WITH_BULLETS)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_education_bullet_point(
        self, education_id: int, bullet_point_id: int
    ) -> EducationBulletPoint | None:
        stmt = select(EducationBulletPoint).where(
            EducationBulletPoint.education_id == education_id,
            EducationBulletPoint.bullet_point_id == bullet_point_id
        ).options(EDUCATION_BULLET_POINT_LOAD)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
        
    async def get_employment_all(self, portfolio_id: int) -> list[Employment] | None:
        stmt = select(Employment).where(Employment.portfolio_id == portfolio_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def get_employment_by_pid(
        self, portfolio_id: int, employment_pid: uuid.UUID
    ) -> Employment | None:
        stmt = select(Employment).where(
            Employment.portfolio_id == portfolio_id,
            Employment.pid == employment_pid
        ).options(EMPLOYMENT_WITH_BULLETS)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_employment_bullet_point(
        self, employment_id: int, bullet_point_id: int
    ) -> EmploymentBulletPoint | None:
        stmt = select(EmploymentBulletPoint).where(
            EmploymentBulletPoint.employment_id == employment_id,
            EmploymentBulletPoint.bullet_point_id == bullet_point_id
        ).options(EMPLOYMENT_BULLET_POINT_LOAD)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
           
    async def get_experience_all(self, portfolio_id: int) -> list[Experience] | None:
        stmt = select(Experience).where(Experience.portfolio_id == portfolio_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def get_experience_by_pid(
        self, portfolio_id: int, experience_pid: uuid.UUID
    ) -> Experience | None:
        stmt = select(Experience).where(
            Experience.portfolio_id == portfolio_id,
            Experience.pid == experience_pid
        ).options(EXPERIENCE_WITH_BULLETS)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_experience_bullet_point(
        self, experience_id: int, bullet_point_id: int
    ) -> ExperienceBulletPoint | None:
        stmt = select(ExperienceBulletPoint).where(
            ExperienceBulletPoint.experience_id == experience_id,
            ExperienceBulletPoint.bullet_point_id == bullet_point_id
        ).options(EXPERIENCE_BULLET_POINT_LOAD)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_portfolio_by_email(self, email: str) -> Portfolio | None:
        stmt = select(Portfolio).where(Portfolio.email == email)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def portfolio_exists(self, portfolio_pid: uuid.UUID) -> bool:
        stmt = select(exists().where(Portfolio.pid == portfolio_pid))
        result = await self.session.scalar(stmt)
        return result
    
    async def get_project_by_pid(
        self, portfolio_id: int, project_pid: uuid.UUID
    ) -> Project | None:
        stmt = select(Project).where(
            Project.portfolio_id == portfolio_id,
            Project.pid == project_pid
        ).options(*PROJECT_FULL)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()