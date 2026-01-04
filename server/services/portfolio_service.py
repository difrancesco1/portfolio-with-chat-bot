import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import (
    Biography,
    Document,
    Education,
    Employment,
    Experience,
    Portfolio
)
from schemas import (
    BiographyCreate,
    EducationCreate,
    EmploymentCreate,
    ExperienceCreate,
)
from server.repositories.portfolio.portfolio_repository import PortfolioRepository
class PortfolioService:
    def __init__(self, session: AsyncSession):
        self.repository = PortfolioRepository(session)
        self.session = session

    # Queries
    async def get_portfolio_by_pid(self, portfolio_pid: uuid.UUID) -> Portfolio:
        portfolio = await self.repository.queries.get_by_pid(portfolio_pid)
        if not portfolio:
            raise ValueError("Portfolio doesn't exist")
        return portfolio

    async def add_biography(self, portfolio_pid: uuid.UUID, bio_data: BiographyCreate) -> Biography:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        biography = await self.repository.writes.add_biography(
            portfolio_id=portfolio.id,
            bio_data=bio_data
        )
        await self.session.commit()
        return biography
    
    async def add_education(self, portfolio_pid: uuid.UUID, edu_data: EducationCreate) -> Education:
        # Check if portfolio exists
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)

        # Add data to portfolio
        education = await self.repository.writes.add_education(
            portfolio_id=portfolio.id, 
            edu_data=edu_data
        )
        
        # Commit changes
        await self.session.commit()
        
        # Return Education
        return education

    async def add_employment(self, portfolio_pid: uuid.UUID, emp_data: EmploymentCreate) -> Education:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        
        employment = await self.repository.writes.add_employment(
            portfolio_id=portfolio.id, 
            emp_data=emp_data
        )
        await self.session.commit()
        return employment
    
    async def add_experience(self, portfolio_pid: uuid.UUID, exp_data: ExperienceCreate) -> Experience:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        
        experience = await self.repository.writes.add_experience(
            portfolio_id=portfolio.id,
            exp_data=exp_data
        )
        await self.session.commit()
        return experience

    async def delete_portfolio(self, portfolio_pid: uuid.UUID) -> None:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        self.repository.writes.delete_portfolio(portfolio)
        self.session.commit()
    
    async def delete_education(self, portfolio_pid: uuid.UUID, education_pid: uuid.UUID) -> None:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        education = await self.repository.queries.get_education_by_pid(
            portfolio_id=portfolio.id, 
            education_pid=education_pid
        )
        if not education:
            raise ValueError("Education doesn't exist")
        result = await self.repository.writes.delete_education(
            portfolio_id=portfolio.id, 
            education_id=education.id
        )
        if result < 1:
            raise ValueError("Association doesn't exist")
        await self.session.commit()

    async def delete_employment(self, portfolio_pid: uuid.UUID, employment_pid: uuid.UUID) -> None:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        employment = await self.repository.queries.get_employment_by_pid(
            portfolio_id=portfolio.id, 
            employment_pid=employment_pid
        )
        if not employment:
            raise ValueError("Employment doesn't exist")
        result = await self.repository.writes.delete_employment(
            portfolio_id=portfolio.id,
            employment_id=employment.id
        )
        if result < 1:
            raise ValueError("Assocation doesn't exist")
        await self.session.commit()

    async def delete_experience(self, portfolio_pid: uuid.UUID, experience_pid: uuid.UUID) -> None:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        experience = await self.repository.queries.get_experience_by_pid(
            portfolio_id=portfolio.id, 
            experience_pid=experience_pid
        )
        if not experience:
            raise ValueError("Experience doesn't exist")
        result = await self.repository.writes.delete_experience(
            portfolio_id=portfolio.id,
            experience_id=experience.id
        )
        if result < 1:
            raise ValueError("Assocation doesn't exist")
        await self.session.commit()
    
    async def get_all_full_portfolios(self) -> list[Portfolio]:
        return await self.repository.queries.get_all_full_portfolios()
    
    async def get_education_all(self, portfolio_pid: uuid.UUID) -> list[Education]:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        return await self.repository.queries.get_education_all(portfolio.id)
    
    async def get_education_by_pid(
        self, portfolio_pid: uuid.UUID, education_pid: uuid.UUID
    ) -> Education:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        education = await self.repository.queries.get_education_by_pid(
            portfolio_id=portfolio.id, 
            education_pid=education_pid
        )
        if not education:
            raise ValueError("Education doesn't exist")
        return education
    
    async def get_employment_all(self, portfolio_pid: uuid.UUID) -> list[Employment]:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        return await self.repository.queries.get_employment_all(portfolio.id)
    
    async def get_employment_by_pid(
        self, portfolio_pid: uuid.UUID, employment_pid: uuid.UUID
    ) -> Employment:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        employment = await self.repository.queries.get_employment_by_pid(
            portfolio_id=portfolio.id, 
            employment_pid=employment_pid
        )
        if not employment:
            raise ValueError("Employment doesn't exist")
        return employment
     
    async def get_experience_all(self, portfolio_pid: uuid.UUID) -> list[Experience]:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        return await self.repository.queries.get_experience_all(portfolio.id)
    
    async def get_experience_by_pid(
        self, portfolio_pid: uuid.UUID, experience_pid: uuid.UUID
    ) -> Experience:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        experience = await self.repository.queries.get_experience_by_pid(
            portfolio_id=portfolio.id, 
            experience_pid=experience_pid
        )
        if not experience:
            raise ValueError("Experience doesn't exist")
        return experience
    
    async def create_portfolio(self, email:str) -> None:
        exists = await self.repository.get_by_email(email)
        if exists:
            raise ValueError("Portfolio already exists")

        portfolio = await self.repository.writes.create_portfolio(
            email=email
        )
        await self.session.commit()

        return portfolio