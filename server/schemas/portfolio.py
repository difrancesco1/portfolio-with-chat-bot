import uuid
from pydantic import BaseModel, EmailStr, Field
from schemas import (
    BaseConfig,
    OutputConfig,
    InputConfig,
    BiographyResponse,
    EducationResponse,
    EmploymentResponse,
    ExperienceResponse
)

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
    biographgy: BiographyResponse
    education: list[EducationResponse]
    employment: list[EmploymentResponse]
    experiences: list[ExperienceResponse]