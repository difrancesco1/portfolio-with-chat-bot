import uuid
from sqlalchemy import exists, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from models.portfolio import (
    Education,
    Employment,
    Experience,
    Portfolio
)
class PortfolioQueries:
    def __init__(self, session: AsyncSession):
        self.session = session

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