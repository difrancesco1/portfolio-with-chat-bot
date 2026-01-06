import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from core.enum import BulletPointType
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
from schemas import (
    BiographyCreate,
    BulletPointCreate,
    EducationCreate,
    EmploymentCreate,
    ExperienceCreate,
    PortfolioCreate,
    ProjectCreate,
)
from repositories.portfolio import PortfolioRepository

class PortfolioService:
    def __init__(self, session: AsyncSession):
        self.repository = PortfolioRepository(session)
        self.session = session

    """ DEBUG FUNCTIONS """
    async def debug_bio_all(self):
        return await self.repository.debug.get_all_bio()
    
    async def debug_bio_bp_all(self):
        return await self.repository.debug.get_all_bio_bp()
    
    async def debug_all_bp(self):
        return await self.repository.debug.get_all_bp()
    
    async def debug_clear_bp_tables(self):
        await self.repository.debug.clear_bp_tables()
        await self.session.commit()
        return
    
    """ **************************************************************************** """
    async def get_portfolio_by_pid(self, portfolio_pid: uuid.UUID) -> Portfolio:
        portfolio = await self.repository.queries.get_by_pid(portfolio_pid)
        if not portfolio:
            raise ValueError("Portfolio doesn't exist")
        return portfolio

    async def add_biography(self, portfolio_pid: uuid.UUID, bio_data: BiographyCreate) -> Biography:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        biography = await self.repository.writes.add_biography(
            portfolio_id=portfolio.id
        )
        await self.session.flush()
        for bp_create in bio_data.content:
            if bp_create.parent_type != BulletPointType.BIOGRAPHY:
                raise ValueError(f"Invalid bullet point type ({bp_create.parent_type}). Has to be of type Biography")
            bio_bp = await self.repository.mutations.add_biography_bullet_point(
                bp_data=bp_create,
                biography=biography
            )
            biography.bullet_points.append(bio_bp)
        await self.session.commit()
        return biography
    
    async def add_biography_bullet_point(
        self, portfolio_pid: uuid.UUID, biography_pid: uuid.UUID, bp_data: BulletPointCreate
    ) -> BiographyBulletPoint:
        if bp_data.parent_type != BulletPointType.BIOGRAPHY:
            raise ValueError(f"Invalid bullet point type ({bp_data.parent_type}). Has to be of type Biography")
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        biography = await self.repository.queries.get_biography_by_pid(
            portfolio_id=portfolio.id,
            biography_pid=biography_pid
        )
        if not biography:
            raise ValueError("Biography doesn't exist")

        bio_bp = await self.repository.mutations.add_biography_bullet_point(
            bp_data=bp_data,
            biography=biography
        )
        if not bio_bp:
            raise ValueError("Biography Bullet Point doesn't exist")
        biography.bullet_points.append(bio_bp)
        await self.session.commit()

        bio_bp = await self.repository.queries.get_biography_bullet_point(
            biography_id=bio_bp.biography_id,
            bullet_point_id=bio_bp.bullet_point_id
        )
        return bio_bp

    async def add_education(self, portfolio_pid: uuid.UUID, edu_data: EducationCreate) -> Education:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)

        education = await self.repository.writes.add_education(
            portfolio_id=portfolio.id, 
            edu_data=edu_data
        )
        await self.session.flush()
        for bp_create in edu_data.bullet_points:
            if bp_create.parent_type != BulletPointType.EDUCATION:
                raise ValueError(f"Invalid bullet point type ({bp_create.parent_type}). Has to be of type Education")
            edu_bp = await self.repository.mutations.add_education_bullet_point(
                education=education,
                bp_data=bp_create
            )
            if not edu_bp:
                raise ValueError("Education Bullet Point add error.")
        
        await self.session.commit()
        return await self.repository.queries.get_education_by_pid(
            portfolio_id=portfolio.id,
            education_pid=education.pid
        )
    
    async def add_education_bullet_point(
        self, portfolio_pid: uuid.UUID, education_pid: uuid.UUID, bp_data: BulletPointCreate
    ) -> EducationBulletPoint:
        if bp_data.parent_type != BulletPointType.EDUCATION:
            raise ValueError(f"Invalid bullet point type ({bp_data.parent_type}). Has to be of type Education")
        portfolio = await self.get_portfolio_by_pid(portfolio_pid=portfolio_pid)
        education = await self.repository.queries.get_education_by_pid(
            portfolio_id=portfolio.id,
            education_pid=education_pid
        )
        if not education:
            raise ValueError("Education doesn't exist")

        edu_bp = await self.repository.mutations.add_education_bullet_point(
            education=education,
            bp_data=bp_data
        )
        if not edu_bp:
            raise ValueError("Education Bullet Point add error.")
        
        await self.session.commit()
        return await self.repository.queries.get_education_bullet_point(
            education_id=edu_bp.education_id,
            bullet_point_id=edu_bp.bullet_point_id
        )
    
    async def add_employment(self, portfolio_pid: uuid.UUID, emp_data: EmploymentCreate) -> Education:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        
        employment = await self.repository.writes.add_employment(
            portfolio_id=portfolio.id, 
            emp_data=emp_data
        )
        await self.session.flush()
        for bp_create in emp_data.bullet_points:
            emp_bp = await self.repository.mutations.add_employment_bullet_point(
                employment=employment,
                bp_data=bp_create
            )
            if not emp_bp:
                raise ValueError("Employee Bullet Point add error")
        await self.session.commit()
        return await self.repository.queries.get_employment_by_pid(
            portfolio_id=portfolio.id, 
            employment_pid=employment.pid
        )
    
    async def add_employment_bullet_point(
        self, portfolio_pid: uuid.UUID, employment_pid: uuid.UUID, bp_data: BulletPointCreate 
    ) -> EmploymentBulletPoint:
        if bp_data.parent_type != BulletPointType.EMPLOYMENT:
            raise ValueError(f"Invalid Bullet Point Type ({bp_data.parent_type}). Must be of type Employment")
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        employment = await self.repository.queries.get_employment_by_pid(
            portfolio_id=portfolio.id,
            employment_pid=employment_pid
        )
        if not employment:
            raise ValueError("Employment doesn't exists")
        emp_bp = await self.repository.mutations.add_employment_bullet_point(
            employment=employment,
            bp_data=bp_data
        )
        employment.bullet_points.append(emp_bp)
        await self.session.commit()

        return await self.repository.queries.get_employment_bullet_point(
            employment_id=emp_bp.employment_id,
            bullet_point_id=emp_bp.bullet_point_id
        )
       
    async def add_experience(self, portfolio_pid: uuid.UUID, exp_data: ExperienceCreate) -> Experience:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        
        experience = await self.repository.writes.add_experience(
            portfolio_id=portfolio.id,
            exp_data=exp_data
        )
        await self.session.flush()
        for bp_create in exp_data.bullet_points:
            exp_bp = await self.repository.mutations.add_experience_bullet_point(
                experience=experience,
                bp_data=bp_create
            )
            if not exp_bp:
                raise ValueError("Employee Bullet Point add error")
        await self.session.commit()
        return await self.repository.queries.get_experience_by_pid(
            portfolio_id=portfolio.id, 
            experience_pid=experience.pid
        )
    
    async def add_experience_bullet_point(
        self, portfolio_pid: uuid.UUID, experience_pid: uuid.UUID, bp_data: BulletPointCreate 
    ) -> ExperienceBulletPoint:
        if bp_data.parent_type != BulletPointType.EXPERIENCE:
            raise ValueError(f"Invalid Bullet Point Type ({bp_data.parent_type}). Must be of type experience")
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        experience = await self.repository.queries.get_experience_by_pid(
            portfolio_id=portfolio.id,
            experience_pid=experience_pid
        )
        if not experience:
            raise ValueError("experience doesn't exists")
        emp_bp = await self.repository.mutations.add_experience_bullet_point(
            experience=experience,
            bp_data=bp_data
        )
        await self.session.commit()

        return await self.repository.queries.get_experience_bullet_point(
            experience_id=emp_bp.experience_id,
            bullet_point_id=emp_bp.bullet_point_id
        )
    
    async def add_project(self, portfolio_pid: uuid.UUID, project_data: ProjectCreate) -> Project:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        
        project = await self.repository.writes.add_project(
            portfolio_id=portfolio.id,
            project_data=project_data
        )
        await self.session.flush()
        for tag in project_data.tags:
            proj_tag = await self.repository.mutations.add_project_tag(
                project=project,
                tag_data=tag
            )
            if not proj_tag:
                raise ValueError("Project Tag add error")
        for link in project_data.links:
            proj_link = await self.repository.mutations.add_project_link(
                project=project,
                link_data=link
            )
            if not proj_link:
                raise ValueError("Project link add error")
        await self.session.commit()
        return await self.repository.queries.get_project_by_pid(
            portfolio_id=portfolio.id, 
            project_pid=project.pid
        )
    
    async def delete_portfolio(self, portfolio_pid: uuid.UUID) -> None:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        await self.repository.writes.delete_portfolio(portfolio)
        await self.session.commit()
    
    async def delete_biography(self, portfolio_pid: uuid.UUID, biography_pid: uuid.UUID) -> None:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        biography = await self.repository.queries.get_biography_by_pid(
            portfolio_id=portfolio.id, 
            biography_pid=biography_pid
        )
        if not biography:
            raise ValueError("Biography doesn't exist")
        
        for bio_bp in biography.bullet_points:
            await self.repository.mutations.delete_biography_bullet_point(
                biography=biography,
                bullet_point=bio_bp.bullet_point
            )
        result = await self.repository.writes.delete_biography(
            portfolio_id=portfolio.id, 
            biography_id=biography.id
        )
        if result < 1:
            raise ValueError("Association doesn't exist")
        await self.session.commit()
    
    async def delete_biography_bullet_point(
        self, portfolio_pid: uuid.UUID, biography_pid: uuid.UUID, bp_pid: uuid.UUID
    ) -> None:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        biography = await self.repository.queries.get_biography_by_pid(
            portfolio_id=portfolio.id,
            biography_pid=biography_pid
        )
        if not biography:
            raise ValueError("Biography doesn't exist")
        bullet_point = await self.repository.queries.get_bullet_point_by_pid(
            bp_pid=bp_pid
        )
        if not bullet_point:
            raise ValueError("Bullet point doesn't exist")
        
        await self.repository.mutations.delete_biography_bullet_point(
            biography=biography,
            bullet_point=bullet_point
        )
        await self.session.commit()
        
    async def delete_education(self, portfolio_pid: uuid.UUID, education_pid: uuid.UUID) -> None:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        education = await self.repository.queries.get_education_by_pid(
            portfolio_id=portfolio.id, 
            education_pid=education_pid
        )
        if not education:
            raise ValueError("Education doesn't exist")
                
        for edu_bp in education.bullet_points:
            await self.repository.mutations.delete_education_bullet_point(
                education=education,
                bullet_point=edu_bp.bullet_point
            )

        result = await self.repository.writes.delete_education(
            portfolio_id=portfolio.id, 
            education_id=education.id
        )
        if result < 1:
            raise ValueError("Association doesn't exist")
        await self.session.commit()
    
    async def delete_education_bullet_point(
        self, portfolio_pid: uuid.UUID, education_pid: uuid.UUID, bp_pid: uuid.UUID
    ) -> None:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        education = await self.repository.queries.get_education_by_pid(
            portfolio_id=portfolio.id,
            education_pid=education_pid
        )
        if not education:
            raise ValueError("Education doesn't exist")
        bullet_point = await self.repository.queries.get_bullet_point_by_pid(
            bp_pid=bp_pid
        )
        if not bullet_point:
            raise ValueError("Bullet point doesn't exist")
        
        await self.repository.mutations.delete_education_bullet_point(
            education=education,
            bullet_point=bullet_point
        )
        await self.session.commit()

    async def delete_employment(self, portfolio_pid: uuid.UUID, employment_pid: uuid.UUID) -> None:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        employment = await self.repository.queries.get_employment_by_pid(
            portfolio_id=portfolio.id, 
            employment_pid=employment_pid
        )
        if not employment:
            raise ValueError("Employment doesn't exist")
        
        for emp_bp in employment.bullet_points:
            await self.repository.mutations.delete_employment_bullet_point(
                employment=employment,
                bullet_point=emp_bp.bullet_point
            )
        result = await self.repository.writes.delete_employment(
            portfolio_id=portfolio.id,
            employment_id=employment.id
        )
        if result < 1:
            raise ValueError("Assocation doesn't exist")
        await self.session.commit()
    
    async def delete_employment_bullet_point(
        self, portfolio_pid: uuid.UUID, employment_pid: uuid.UUID, bp_pid: uuid.UUID
    ) -> None:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        employment = await self.repository.queries.get_employment_by_pid(
            portfolio_id=portfolio.id,
            employment_pid=employment_pid
        )
        if not employment:
            raise ValueError("Employment doesn't exist")
        bullet_point = await self.repository.queries.get_bullet_point_by_pid(
            bp_pid=bp_pid
        )
        if not bullet_point:
            raise ValueError("Bullet point doesn't exist")
        
        await self.repository.mutations.delete_employment_bullet_point(
            employment=employment,
            bullet_point=bullet_point
        )
        await self.session.commit()
    
    async def delete_experience(self, portfolio_pid: uuid.UUID, experience_pid: uuid.UUID) -> None:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        experience = await self.repository.queries.get_experience_by_pid(
            portfolio_id=portfolio.id, 
            experience_pid=experience_pid
        )
        if not experience:
            raise ValueError("Experience doesn't exist")
        
        for exp_bp in experience.bullet_points:
            await self.repository.mutations.delete_experience_bullet_point(
                experience=experience,
                bullet_point=exp_bp.bullet_point
            )
        result = await self.repository.writes.delete_experience(
            portfolio_id=portfolio.id,
            experience_id=experience.id
        )
        if result < 1:
            raise ValueError("Assocation doesn't exist")
        await self.session.commit()
    
    async def delete_experience_bullet_point(
        self, portfolio_pid: uuid.UUID, experience_pid: uuid.UUID, bp_pid: uuid.UUID
    ) -> None:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        experience = await self.repository.queries.get_experience_by_pid(
            portfolio_id=portfolio.id,
            experience_pid=experience_pid
        )
        if not experience:
            raise ValueError("Experience doesn't exist")
        bullet_point = await self.repository.queries.get_bullet_point_by_pid(
            bp_pid=bp_pid
        )
        if not bullet_point:
            raise ValueError("Bullet point doesn't exist")
        
        await self.repository.mutations.delete_experience_bullet_point(
            experience=experience,
            bullet_point=bullet_point
        )
        await self.session.commit()    

    async def delete_project(self, portfolio_pid: uuid.UUID, project_pid: uuid.UUID) -> None:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        project = await self.repository.queries.get_project_by_pid(
            portfolio_id=portfolio.id, 
            project_pid=project_pid
        )
        if not project:
            raise ValueError("Project doesn't exist")
        
        for proj_tag in project.tags:
            await self.repository.mutations.delete_project_tag(
                project=project,
                tag=proj_tag.tag
            )
        for proj_link in project.links:
            await self.repository.mutations.delete_project_link(
                project=project,
                link=proj_link.link
            )
        result = await self.repository.writes.delete_project(
            portfolio_id=portfolio.id,
            project_id=project.id
        )
        if result < 1:
            raise ValueError("Assocation doesn't exist")
        await self.session.commit()

    async def get_all_full_portfolios(self) -> list[Portfolio]:
        return await self.repository.queries.get_all_full_portfolios()
    
    async def get_biography(self, portfolio_pid: uuid.UUID) -> Biography:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        biography = await self.repository.queries.get_biography(portfolio.id)
        if not biography:
            raise ValueError("Biography doesn't exist")
        return biography
    
    async def get_biography_all(self, portfolio_pid: uuid.UUID) -> list[Biography]:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        return await self.repository.queries.get_biography_all(portfolio.id)
    
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

    async def get_project_by_pid(
        self, portfolio_pid: uuid.UUID, project_pid: uuid.UUID
    ) -> Project:
        portfolio = await self.get_portfolio_by_pid(portfolio_pid)
        project = await self.repository.queries.get_project_by_pid(
            portfolio_id=portfolio.id, 
            project_pid=project_pid
        )
        if not project:
            raise ValueError("Project doesn't exist")
        return project
    
    async def create_portfolio(self, data: PortfolioCreate) -> None:
        exists = await self.repository.queries.get_by_email(data.email)
        if exists:
            raise ValueError("Portfolio already exists")

        portfolio = await self.repository.writes.create_portfolio(data=data)
        await self.session.flush()
        biography = await self.repository.writes.add_biography(portfolio_id=portfolio.id)
        portfolio.biography = biography
        await self.session.commit()

        return portfolio