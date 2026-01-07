from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete

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
    Link,
    Portfolio,
    Project,
    ProjectLink,
    ProjectTag,
    Tag
)
from schemas import (
    BiographyCreate,
    BulletPointCreate,
    EducationCreate,
    EmploymentCreate,
    ExperienceCreate,
    LinkCreate,
    PortfolioCreate,
    ProjectCreate,
    TagCreate
)
class PortfolioWrites:
    def __init__(self, session: AsyncSession):
        self.session = session

    # Creates
    async def create_portfolio(self, data: PortfolioCreate) -> Portfolio:
        portfolio = Portfolio(
            email=data.email,
            first_name=data.first_name,
            last_name=data.last_name
        )
        self.session.add(portfolio)
        return portfolio
    
    async def add_biography(
        self, portfolio_id: int, data: BiographyCreate
    ) -> Biography:
        biography = Biography(
            portfolio_id=portfolio_id,
            decription=data.description
        )
        self.session.add(biography)
        return biography
    
    async def add_biography_bullet_point(
        self, biography_id: int, bullet_point_id: int, position: int
    ) -> BiographyBulletPoint:
        bio_bp = BiographyBulletPoint(
            biography_id=biography_id,
            bullet_point_id=bullet_point_id,
            position=position
        )
        self.session.add(bio_bp)
        return bio_bp
    
    async def add_bullet_point(
        self, bp_data: BulletPointCreate
    ) -> BulletPoint | None:
        bullet_point = BulletPoint(
            content=bp_data.content
        )
        self.session.add(bullet_point)
        return bullet_point
    
    async def add_document(
        self, filename: str, content_type: str, data: bytes 
    ) -> Document:
        document = Document(
            filename=filename,
            content_type=content_type,
            data=data
        )
        self.session.add(document)
        return document
    
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
    
    async def add_education_bullet_point(
        self, education_id: int, bullet_point_id: int, position: int
    ) -> EducationBulletPoint:
        edu_bp = EducationBulletPoint(
            education_id=education_id,
            bullet_point_id=bullet_point_id,
            position=position
        )
        self.session.add(edu_bp)
        return edu_bp
    
    async def add_employment(
        self, portfolio_id: int, emp_data: EmploymentCreate
    ) -> Employment:
        employment = Employment(
            portfolio_id=portfolio_id,
            company=emp_data.company,
            position=emp_data.position,
            start_date=emp_data.start_date,
            end_date=emp_data.end_date
        )
        self.session.add(employment)
        return employment
    
    async def add_employment_bullet_point(
        self, employment_id: int, bullet_point_id: int, position: int
    ) -> EmploymentBulletPoint:
        emp_bp = EmploymentBulletPoint(
            employment_id=employment_id,
            bullet_point_id=bullet_point_id,
            position=position
        )
        self.session.add(emp_bp)
        return emp_bp
    
    async def add_experience(
        self, portfolio_id: int, exp_data: ExperienceCreate
    ) -> Experience:
        experience = Experience(
            portfolio_id=portfolio_id,
            title=exp_data.title,
            start_date=exp_data.start_date,
            end_date=exp_data.end_date
        )
        self.session.add(experience)
        return experience

    async def add_experience_bullet_point(
        self, experience_id: int, bullet_point_id: int, position: int
    ) -> ExperienceBulletPoint:
        exp_bp = ExperienceBulletPoint(
            experience_id=experience_id,
            bullet_point_id=bullet_point_id,
            position=position
        )
        self.session.add(exp_bp)
        return exp_bp
    
    async def add_link(
        self, link_data: LinkCreate
    ) -> Link | None:
        link = Link(
            url=link_data.url,
            platform=link_data.platform
        )
        self.session.add(link)
        return link
    
    async def add_project(
        self, portfolio_id: int, project_data: ProjectCreate
    ) -> Project:
        project = Project(
            portfolio_id=portfolio_id,
            title=project_data.title,
            image_url=project_data.image_url,
            summary=project_data.summary,
            description=project_data.description
        )
        self.session.add(project)
        return project
    
    async def add_project_link(
        self, project_id: int, link_id: int
    ) -> ProjectLink | None:
        project_link = ProjectLink(
            project_id=project_id,
            link_id=link_id
        )
        self.session.add(project_link)
        return project_link
    
    async def add_project_tag(
        self, project_id: int, tag_id: int
    ) -> ProjectTag | None:
        project_tag = ProjectTag(
            project_id=project_id,
            tag_id=tag_id
        )
        self.session.add(project_tag)
        return project_tag
    
    async def add_tag(
        self, tag_data: TagCreate
    ) -> Tag | None:
        tag = Tag(
            tag=tag_data.tag
        )
        self.session.add(tag)
        return tag
    
    # Updates

    # Deletes
    async def delete_portfolio(self, portfolio: Portfolio) -> None:
        await self.session.delete(portfolio)

    async def delete_biography(self, portfolio_id: int, biography_id: int) -> int:
        stmt = (
            delete(Biography)
            .where(
                Biography.portfolio_id == portfolio_id,
                Biography.id == biography_id
            )
        )
        result = await self.session.execute(stmt)
        return result.rowcount
    
    async def delete_biography_bullet_point(
        self, biography_id: int, bp_id: int
    ) -> int:
        stmt = (
            delete(BiographyBulletPoint)
            .where(
                BiographyBulletPoint.biography_id == biography_id,
                BiographyBulletPoint.bullet_point_id == bp_id
            )
        )
        result = await self.session.execute(stmt)
        return result.rowcount
    
    async def delete_bullet_point(
        self, bp_id: int
    ) -> int:
        stmt = (
            delete(BulletPoint)
            .where(
                BulletPoint.id == bp_id
            )
        )
        result = await self.session.execute(stmt)
        return result.rowcount
    
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
    
    async def delete_education_bullet_point(
        self, education_id: int, bp_id: int
    ) -> int:
        stmt = (
            delete(EducationBulletPoint)
            .where(
                EducationBulletPoint.education_id == education_id,
                EducationBulletPoint.bullet_point_id == bp_id
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
    
    async def delete_employment_bullet_point(
        self, employment_id: int, bp_id: int
    ) -> int:
        stmt = (
            delete(EmploymentBulletPoint)
            .where(
                EmploymentBulletPoint.employment_id == employment_id,
                EmploymentBulletPoint.bullet_point_id == bp_id
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
    
    async def delete_experience_bullet_point(
        self, experience_id: int, bp_id: int
    ) -> int:
        stmt = (
            delete(ExperienceBulletPoint)
            .where(
                ExperienceBulletPoint.experience_id == experience_id,
                ExperienceBulletPoint.bullet_point_id == bp_id
            )
        )
        result = await self.session.execute(stmt)
        return result.rowcount

    async def delete_link(
        self, link_id: int
    ) -> int:
        stmt = (
            delete(Link)
            .where(
                Link.id == link_id
            )
        )
        result = await self.session.execute(stmt)
        return result.rowcount
    
    async def delete_project_link(self, project_id: int, link_id: int) -> int:
        stmt = (
            delete(ProjectLink)
            .where(
                ProjectLink.project_id == project_id,
                ProjectLink.id == link_id
            )
        )
        result = await self.session.execute(stmt)
        return result.rowcount
    
    async def delete_project(self, portfolio_id: int, project_id: int) -> int:
        stmt = (
            delete(Project)
            .where(
                Project.portfolio_id == portfolio_id,
                Project.id == project_id
            )
        )
        result = await self.session.execute(stmt)
        return result.rowcount
    
    async def delete_project_tag(self, project_id: int, tag_id: int) -> int:
        stmt = (
            delete(ProjectTag)
            .where(
                ProjectTag.project_id == project_id,
                ProjectTag.id == tag_id
            )
        )
        result = await self.session.execute(stmt)
        return result.rowcount
    
    async def delete_tag(
        self, tag_id: int
    ) -> int:
        stmt = (
            delete(Tag)
            .where(
                Tag.id == tag_id
            )
        )
        result = await self.session.execute(stmt)
        return result.rowcount