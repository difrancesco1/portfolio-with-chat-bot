import uuid
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
# Relative
from .config import BaseConfig, OutputConfig, InputConfig
from .biography import BiographyCreate, BiographyResponse
from .document import DocumentResponse
from .education import EducationResponse
from .employment import EmploymentResponse
from .experience import ExperienceResponse
from .link import PortfolioLinkBase, PortfolioLinkResponse
from .project import ProjectResponse

# Portfolio
class PortfolioBase(BaseConfig, BaseModel):
    email: EmailStr
    first_name: str = Field(
        ..., 
        alias="firstName",
        min_length=1,
        max_length=64
    )
    last_name: str = Field(
        ..., 
        alias="lastName",
        min_length=1,
        max_length=64
    )

class PortfolioCreate(InputConfig, PortfolioBase):
    pass

class PortfolioResponse(OutputConfig, PortfolioBase):
    pid: uuid.UUID = Field(..., alias="portfolioPid")

class PortfolioBiographyResponse(PortfolioResponse):
    biography: BiographyResponse

class PortfolioEducationResponse(PortfolioResponse):
    education: list[EducationResponse]

class PortfolioEmploymentResponse(PortfolioResponse):
    employment: list[EmploymentResponse]

class PortfolioExperienceResponse(PortfolioResponse):
    experiences: list[ExperienceResponse]

class PortfolioFullResponse(PortfolioResponse):
    biography: Optional[BiographyResponse]
    document: Optional[DocumentResponse]
    education: list[EducationResponse]
    employment: list[EmploymentResponse]
    experiences: list[ExperienceResponse]
    links: list[PortfolioLinkResponse]
    projects: list[ProjectResponse]

class PortfolioUpdate(BaseConfig, InputConfig, BaseModel):
    email: EmailStr | None = None
    first_name: str | None = Field(
        default=None,
        alias="firstName",
        min_length=1,
        max_length=64
    )
    last_name: str | None = Field(
        default=None, 
        alias="lastName",
        min_length=1,
        max_length=64
    )
    links: list[PortfolioLinkBase] | None = None