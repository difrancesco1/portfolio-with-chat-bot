from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete
from models import (
    Biography,
    BiographyBulletPoint,
    BulletPoint,
    Education,
    Employment,
    Experience,
    Portfolio
)
from schemas import (
    BiographyCreate,
    EducationCreate,
    EmploymentCreate,
    ExperienceCreate
)
class PortfolioWrites:
    def __init__(self, session: AsyncSession):
        self.session = session

    # Creates
    async def create_portfolio(self, email: str) -> Portfolio:
        portfolio = Portfolio(email=email)
        self.session.add(portfolio)
        return portfolio
    
    async def add_biography(
            self, portfolio_id: int
    ) -> Biography:
        biography = Biography(
            portfolio_id=portfolio_id
        )
        self.session.add(biography)
        return biography
    
    # async def add_bullet_point(
    #         self, 
    # )
    
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
    
    # Updates

    # Deletes
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