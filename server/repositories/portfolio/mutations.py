from sqlalchemy.ext.asyncio import AsyncSession
from core.enum import BulletPointType
from models import (
    Biography,
    BiographyBulletPoint,
    BulletPoint,
    Education,
    EducationBulletPoint,
    Employment,
    EmploymentBulletPoint,
    Experience,
    ExperienceBulletPoint,
    Link,
    Portfolio,
    Project,
    Tag
)
from schemas import (
    BiographyCreate,
    BiographyUpdate,
    BulletPointCreate,
    EducationCreate,
    EmploymentCreate,
    ExperienceCreate,
    TagCreate,
    LinkCreate,
)
# Relative
from .writes import PortfolioWrites
from .queries import PortfolioQueries

class PortfolioMutations:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.writes = PortfolioWrites(session)
        self.queries = PortfolioQueries(session)

    async def add_biography_bullet_point(
        self, biography: Biography, bp_data: BulletPointCreate
    ) -> BiographyBulletPoint:
        bullet_point = await self.writes.add_bullet_point(
            bp_data=bp_data
        )
        await self.session.flush()

        bio_bp = await self.writes.add_biography_bullet_point(
            bullet_point_id=bullet_point.id,
            biography_id=biography.id,
            position=bp_data.position
        )
        return bio_bp

    async def add_education_bullet_point(
        self, education: Education, bp_data: BulletPointCreate
    ) -> EducationBulletPoint | None:
        bullet_point = await self.writes.add_bullet_point(
            bp_data=bp_data
        )
        await self.session.flush()

        edu_bp = await self.writes.add_education_bullet_point(
            bullet_point_id=bullet_point.id,
            education_id=education.id,
            position=bp_data.position
        )
        return edu_bp 
    
    async def add_employment_bullet_point(
        self, employment: Employment, bp_data: BulletPointCreate
    ) -> EmploymentBulletPoint | None:
        bullet_point = await self.writes.add_bullet_point(
            bp_data=bp_data
        )
        await self.session.flush()

        emp_bp = await self.writes.add_employment_bullet_point(
            bullet_point_id=bullet_point.id,
            employment_id=employment.id,
            position=bp_data.position
        )
        return emp_bp     
    
    async def add_experience_bullet_point(
        self, experience: Experience, bp_data: BulletPointCreate
    ) -> ExperienceBulletPoint:
        bullet_point = await self.writes.add_bullet_point(
            bp_data=bp_data
        )
        await self.session.flush()

        exp_bp = await self.writes.add_experience_bullet_point(
            bullet_point_id=bullet_point.id,
            experience_id=experience.id,
            position=bp_data.position
        )
        return exp_bp
    
    async def add_project_link(
        self, project: Project, link_data: LinkCreate
    ) -> Link:
        link = await self.writes.add_link(
            link_data=link_data
        )
        await self.session.flush()

        project_link = await self.writes.add_project_link(
            project_id=project.id,
            link_id=link.id,
        )
        return project_link
    
    async def add_project_tag(
        self, project: Project, tag_data: TagCreate
    ) -> Tag:
        tag = await self.writes.add_tag(
            tag_data=tag_data
        )
        await self.session.flush()

        project_tag = await self.writes.add_project_tag(
            project_id=project.id,
            tag_id=tag.id,
        )
        return project_tag
    
    async def delete_biography_bullet_point(
        self, biography: Biography, bullet_point: BulletPoint
    ) -> None:
        bio_bp_result = await self.writes.delete_biography_bullet_point(
            biography_id=biography.id,
            bp_id=bullet_point.id
        )
        if bio_bp_result < 1:
            raise ValueError("Association between biography and bullet point doesn't exist")
        bp_result = await self.writes.delete_bullet_point(bp_id=bullet_point.id)
        if bp_result < 1:
            raise ValueError(f"No row for bullet point ({bullet_point.id}) exists")
        
    async def delete_education_bullet_point(
        self, education: Education, bullet_point: BulletPoint
    ) -> None:
        bio_bp_result = await self.writes.delete_education_bullet_point(
            education_id=education.id,
            bp_id=bullet_point.id
        )
        if bio_bp_result < 1:
            raise ValueError("Association between education and bullet point doesn't exist")
        bp_result = await self.writes.delete_bullet_point(bp_id=bullet_point.id)
        if bp_result < 1:
            raise ValueError(f"No row for bullet point ({bullet_point.id}) exists")
        
    async def delete_employment_bullet_point(
        self, employment: Employment, bullet_point: BulletPoint
    ) -> None:
        bio_bp_result = await self.writes.delete_employment_bullet_point(
            employment_id=employment.id,
            bp_id=bullet_point.id
        )
        if bio_bp_result < 1:
            raise ValueError("Association between employment and bullet point doesn't exist")
        bp_result = await self.writes.delete_bullet_point(bp_id=bullet_point.id)
        if bp_result < 1:
            raise ValueError(f"No row for bullet point ({bullet_point.id}) exists")
        
    async def delete_experience_bullet_point(
        self, experience: Experience, bullet_point: BulletPoint
    ) -> None:
        bio_bp_result = await self.writes.delete_experience_bullet_point(
            experience_id=experience.id,
            bp_id=bullet_point.id
        )
        if bio_bp_result < 1:
            raise ValueError("Association between experience and bullet point doesn't exist")
        bp_result = await self.writes.delete_bullet_point(bp_id=bullet_point.id)
        if bp_result < 1:
            raise ValueError(f"No row for bullet point ({bullet_point.id}) exists")
        
            
    async def delete_project_link(
        self, project: Project, link: Link
    ) -> None:
        proj_link_result = await self.writes.delete_project_link(
            project_id=project.id,
            link_id=link.id
        )
        if proj_link_result < 1:
            raise ValueError("Association between experience and bullet point doesn't exist")
        link_result = await self.writes.delete_link(link_id=link.id)
        if link_result < 1:
            raise ValueError(f"No row for bullet point ({link.id}) exists")
    
            
    async def delete_project_tag(
        self, project: Project, tag: Tag
    ) -> None:
        proj_tag_result = await self.writes.delete_project_tag(
            project_id=project.id,
            tag_id=tag.id
        )
        if proj_tag_result < 1:
            raise ValueError("Association between experience and bullet point doesn't exist")
        tag_result = await self.writes.delete_tag(tag_id=tag.id)
        if tag_result < 1:
            raise ValueError(f"No row for bullet point ({tag.id}) exists")
        
    async def update_biography(
        self, biography: Biography, bio_data: BiographyUpdate
    ):
        pass