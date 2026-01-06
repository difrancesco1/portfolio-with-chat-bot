from sqlalchemy.orm import selectinload
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
    PortfolioLink,
    Project,
    ProjectLink,
    ProjectTag
)

BIOGRAPHY_MINIMUM = ()

BIOGRAPHY_WITH_BULLETS = (
    selectinload(Biography.bullet_points)
    .selectinload(BiographyBulletPoint.bullet_point)
)

BIOGRAPHY_BULLET_POINT_LOAD = (
    selectinload(BiographyBulletPoint.bullet_point)
)

EDUCATION_WITH_BULLETS = (
    selectinload(Education.bullet_points)
    .selectinload(EducationBulletPoint.bullet_point)
)

EDUCATION_BULLET_POINT_LOAD = (
    selectinload(EducationBulletPoint.bullet_point)
)

EMPLOYMENT_WITH_BULLETS = (
    selectinload(Employment.bullet_points)
    .selectinload(EmploymentBulletPoint.bullet_point)
)

EMPLOYMENT_BULLET_POINT_LOAD = (
    selectinload(EmploymentBulletPoint.bullet_point)
)

EXPERIENCE_WITH_BULLETS = (
    selectinload(Experience.bullet_points)
    .selectinload(ExperienceBulletPoint.bullet_point)
)

EXPERIENCE_BULLET_POINT_LOAD = (
    selectinload(ExperienceBulletPoint.bullet_point)
)

PROJECT_WITH_LINKS = (
    selectinload(Project.links)
    .selectinload(ProjectLink.link)
)

PROJECT_WITH_TAGS = (
    selectinload(Project.tags)
    .selectinload(ProjectTag.tag)
)

PROJECT_FULL = (
    PROJECT_WITH_LINKS, 
    PROJECT_WITH_TAGS
)

PORTFOLIO_MINIMUM = ()

PORTFOLIO_DOCUMENT = (
    selectinload(Portfolio.document)
)

PORTFOLIO_BIOGRAPHY = (
    selectinload(Portfolio.biography)
    .selectinload(Biography.bullet_points)
    .selectinload(BiographyBulletPoint.bullet_point)
)

PORTFOLIO_EDUCATION = (
    selectinload(Portfolio.education)
    .selectinload(Education.bullet_points)
    .selectinload(EducationBulletPoint.bullet_point)
)

PORTFOLIO_EMPLOYMENT = (
    selectinload(Portfolio.employment)
    .selectinload(Employment.bullet_points)
    .selectinload(EmploymentBulletPoint.bullet_point)
)

PORTFOLIO_EXPERIENCE = (
    selectinload(Portfolio.experiences)
    .selectinload(Experience.bullet_points)
    .selectinload(ExperienceBulletPoint.bullet_point)
)

PORTFOLIO_LINKS = (
    selectinload(Portfolio.links)
    .selectinload(PortfolioLink.link)
)

PORTFOLIO_PROJECT = (
    selectinload(Portfolio.projects)
    .selectinload(Project.links)
    .selectinload(ProjectLink.link),
    selectinload(Portfolio.projects)
    .selectinload(Project.tags)
    .selectinload(ProjectTag.tag)
)

PORTFOLIO_FULL = (
    PORTFOLIO_BIOGRAPHY,
    PORTFOLIO_EDUCATION, 
    PORTFOLIO_EMPLOYMENT, 
    PORTFOLIO_EXPERIENCE, 
    *PORTFOLIO_PROJECT,
    PORTFOLIO_DOCUMENT,
    PORTFOLIO_LINKS,
)