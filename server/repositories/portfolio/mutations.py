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
    EducationUpdate,
    EmploymentCreate,
    EmploymentUpdate,
    ExperienceCreate,
    ExperienceUpdate,
    TagCreate,
    LinkCreate,
    ProjectUpdate
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
        self, biography: Biography, update_data: BiographyUpdate
    ) -> None:
        data = update_data.model_dump(
            by_alias=False,
            exclude={"bullet_points"},
            exclude_unset=True
        )
        if "description" in data:
            biography.description = data["description"]
        
        if update_data.bullet_points is not None:
            for bio_bp in update_data.bullet_points:
                bp = await self.queries.get_bullet_point_by_pid(
                    bp_pid=bio_bp.bullet_point.pid
                )
                bp.content = bio_bp.bullet_point.content
                association = await self.queries.get_biography_bullet_point(
                    biography_id=biography.id,
                    bullet_point_id=bp.id
                )
                association.position = bio_bp.position

    async def update_education(
        self, education: Education, update_data: EducationUpdate
    ) -> None:
        data = update_data.model_dump(
            by_alias=False,
            exclude={"bullet_points"},
            exclude_unset=True
        )
        for key, value in data.items():
            setattr(education, key, value)

        if update_data.bullet_points is not None:
            for edu_bp in update_data.bullet_points:
                bp = await self.queries.get_bullet_point_by_pid(
                    bp_pid=edu_bp.bullet_point.pid
                )
                bp.content = edu_bp.bullet_point.content
                association = await self.queries.get_education_bullet_point(
                    education_id=education.id,
                    bullet_point_id=bp.id
                )
                association.position = edu_bp.position

    async def update_employment(
        self, employment: Employment, update_data: EmploymentUpdate
    ) -> None:
        data = update_data.model_dump(
            by_alias=False,
            exclude={"bullet_points"},
            exclude_unset=True
        )
        for key, value in data.items():
            setattr(employment, key, value)
        if update_data.bullet_points is not None:
            for emp_bp in update_data.bullet_points:
                bp = await self.queries.get_bullet_point_by_pid(
                    bp_pid=emp_bp.bullet_point.pid
                )
                bp.content = emp_bp.bullet_point.content
                association = await self.queries.get_employment_bullet_point(
                    employment_id=employment.id,
                    bullet_point_id=bp.id
                )
                association.position = emp_bp.position

    async def update_experience(
        self, experience: Experience, update_data: ExperienceUpdate
    ) -> None:
        data = update_data.model_dump(
            by_alias=False,
            exclude={"bullet_points"},
            exclude_unset=True
        )
        for key, value in data.items():
            setattr(experience, key, value)
        if update_data.bullet_points is not None:
            for exp_bp in update_data.bullet_points:
                bp = await self.queries.get_bullet_point_by_pid(
                    bp_pid=exp_bp.bullet_point.pid
                )
                bp.content = exp_bp.bullet_point.content
                association = await self.queries.get_experience_bullet_point(
                    experience_id=experience.id,
                    bullet_point_id=bp.id
                )
                association.position = exp_bp.position

    async def update_project(
        self, project: Project, update_data: ProjectUpdate
    ) -> None:
        data = update_data.model_dump(
            by_alias=False,
            exclude={"tags", "links"},
            exclude_unset=True
        )
        for key, value in data.items():
            setattr(project, key, value)
        if update_data.links is not None:
            for proj_link in update_data.links:
                link = await self.queries.get_link_by_pid(
                    link_pid=proj_link.link.pid
                )
                link.url = proj_link.link.url
                link.platform = proj_link.link.platform
        if update_data.tags is not None:
            for proj_tag in update_data.tags:
                tag = await self.queries.get_tag_by_pid(
                    tag_pid=proj_tag.tag.pid
                )
                tag.tag = proj_tag.tag.tag        