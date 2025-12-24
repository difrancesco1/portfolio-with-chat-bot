from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional
from typing_extensions import Annotated

# Annotations
EndDateField = Annotated[
    Optional[datetime],
    Field(
        alias="endDate"
    )
]

StartDateField = Annotated [
    datetime,
    Field(
        ...,
        alias="startDate",
    )
]

StringField = Annotated[
    str,
    Field(
        ...,
        min_length=1,
        max_length=64
    )
]

TextField = Annotated[
    str,
    Field(
        ...,
        min_length=1,
    )
]

# Configurations
class BaseConfig(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        ser_json_by_alias=True,
    )

class InputConfig(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        strict=True,
        strip_white_space=True
    )

class OutputConfig(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

# Education
class EducationBase(BaseConfig, BaseModel):
    major: StringField
    degree: StringField
    gpa: Optional[float] = Field(default=None)
    start_date: StartDateField
    end_date: EndDateField = None

class EducationResponse(OutputConfig, EducationBase):
    education_id: int = Field(..., alias="educationId")

class EducationCreate(InputConfig, EducationBase):
    pass

# Employment
class EmploymentBase(BaseModel):
    company: StringField
    content: TextField
    start_date: StartDateField
    end_date: EndDateField = None

class EmploymentResponse(OutputConfig, EmploymentBase):
    employment_id: int = Field(..., alias="employmentId")

class EmploymentCreate(InputConfig, EmploymentBase):
    pass

# Experience
class ExperienceBase(BaseModel):
    title: StringField
    content: TextField
    start_date: StartDateField
    end_date: EndDateField

class ExperienceResponse(OutputConfig, ExperienceBase):
    experience_id: int = Field(..., alias="experienceId")

class ExperienceCreate(InputConfig, ExperienceBase):
    pass

# Portfolio
class PortfolioBase(BaseModel):
    email: EmailStr

class PortfolioCreate(InputConfig, PortfolioBase):
    pass

class PortfolioResponse(OutputConfig, PortfolioBase):
    portfolio_id: int = Field(..., alias="portfolioId")

class PortfolioEducationResponse(PortfolioResponse):
    education: list[EducationResponse]

class PortfolioEmploymentResponse(PortfolioResponse):
    employment: list[EmploymentResponse]

class PortfolioExperienceResponse(PortfolioResponse):
    experiences: list[ExperienceResponse]

class PortfolioFullResponse(PortfolioResponse):
    education: list[EducationResponse]
    employment: list[EmploymentResponse]
    experiences: list[EmploymentResponse]