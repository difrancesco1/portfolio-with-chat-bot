import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import delete, exists, select

from models.portfolio import (
    Education,
    Employment,
    Experience,
    Portfolio
)
from schemas.portfolio import (
    EducationCreate,
    EmploymentCreate,
    ExperienceCreate
)

class PortfolioRepository():
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_education(
        self, portfolio_id: int, edu_data: EducationCreate
    ) -> Education:
        education = Education(
            portfolio_id=portfolio_id,
            major=edu_data.major,
            degree=edu_data.degree,
            gpa=edu_data.gpa,
            start_date=edu_data.start_date,
            end_date=edu_data.end_date
        )
        self.session.add(education)
        return education

    async def add_employment(
        self, portfolio_id: int, emp_data: EmploymentCreate
    ) -> Employment:
        employment = Employment(
            portfolio_id=portfolio_id,
            company=emp_data.company,
            position=emp_data.position,
            content=emp_data.content,
            start_date=emp_data.start_date,
            end_date=emp_data.end_date
        )
        self.session.add(employment)
        return employment
    
    async def add_experience(
        self, portfolio_id: int, exp_data: ExperienceCreate
    ) -> Experience:
        experience = Experience(
            portfolio_id=portfolio_id,
            title=exp_data.title,
            content=exp_data.content,
            start_date=exp_data.start_date,
            end_date=exp_data.end_date
        )
        self.session.add(experience)
        return experience
    
    async def create_portfolio(self, email: str) -> Portfolio:
        portfolio = Portfolio(email=email)
        self.session.add(portfolio)
        return portfolio
    
    async def delete_portfolio(self, portfolio: Portfolio) -> None:
        await self.session.delete(portfolio)
    
    async def delete_education(self, portfolio_id: int, education_id: int) -> int:
        stmt = (
            delete(Education)
            .where(
                Education.portfolio_id == portfolio_id,
                Education.id == education_id
            )
        )
        result = await self.session.execute(stmt)
        return result.rowcount

    async def delete_employment(self, portfolio_id: int, employment_id: int) -> int:
        stmt = (
            delete(Employment)
            .where(
                Employment.portfolio_id == portfolio_id,
                Employment.id == employment_id
            )
        )
        result = await self.session.execute(stmt)
        return result.rowcount

    async def delete_experience(self, portfolio_id: int, experience_id: int) -> int:
        stmt = (
            delete(Experience)
            .where(
                Experience.portfolio_id == portfolio_id,
                Experience.id == experience_id
            )
        )
        result = await self.session.execute(stmt)
        return result.rowcount
    
    async def get_all_full_portfolios(self) -> list[Portfolio]:
        stmt = select(Portfolio).options(
            selectinload(Portfolio.education),
            selectinload(Portfolio.employment),
            selectinload(Portfolio.experiences)
        )
        results = await self.session.execute(stmt)
        return results.scalars().all()
    
    async def get_by_email(self, email: str) -> Portfolio:
        stmt = select(Portfolio).where(Portfolio.email == email)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_by_pid(self, portfolio_pid: uuid.UUID) -> Portfolio:
        stmt = select(Portfolio).where(Portfolio.pid == portfolio_pid)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_education_all(self, portfolio_id: int) -> list[Education]:
        stmt = select(Education).where(Education.portfolio_id == portfolio_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def get_education_by_pid(
        self, portfolio_id: int, education_pid: uuid.UUID
    ) -> Education:
        stmt = select(Education).where(
            Education.portfolio_id == portfolio_id,
            Education.pid == education_pid
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_employment_all(self, portfolio_id: int) -> list[Employment]:
        stmt = select(Employment).where(Employment.portfolio_id == portfolio_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def get_employment_by_pid(
        self, portfolio_id: int, employment_pid: uuid.UUID
    ) -> Employment:
        stmt = select(Employment).where(
            Employment.portfolio_id == portfolio_id,
            Employment.pid == employment_pid
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
       
    async def get_experience_all(self, portfolio_id: int) -> list[Experience]:
        stmt = select(Experience).where(Experience.portfolio_id == portfolio_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def get_experience_by_pid(
        self, portfolio_id: int, experience_pid: uuid.UUID
    ) -> Experience:
        stmt = select(Experience).where(
            Experience.portfolio_id == portfolio_id,
            Experience.pid == experience_pid
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def portfolio_exists(self, portfolio_pid: int) -> bool:
        stmt = select(exists().where(Portfolio.pid == portfolio_pid))
        result = await self.session.scalar(stmt)
        return result