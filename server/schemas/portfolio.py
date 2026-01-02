import uuid
from datetime import date
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional
from typing_extensions import Annotated

# Annotations
EndDateField = Annotated[
    Optional[date],
    Field(
        alias="endDate"
    )
]

StartDateField = Annotated [
    date,
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
        populate_by_name=True
    )

class InputConfig(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        strip_white_space=True
    )

class OutputConfig(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        ser_json_by_alias=True,
    )

# Education
class EducationBase(BaseConfig, BaseModel):
    major: StringField
    degree: StringField
    gpa: Optional[float] = Field(default=None)
    start_date: StartDateField
    end_date: EndDateField = None

class EducationResponse(OutputConfig, EducationBase):
    pid: uuid.UUID = Field(..., alias="educationPid")

class EducationCreate(InputConfig, EducationBase):
    pass

# Employment
class EmploymentBase(BaseConfig, BaseModel):
    company: StringField
    position: StringField
    content: TextField
    start_date: StartDateField
    end_date: EndDateField = None

class EmploymentResponse(OutputConfig, EmploymentBase):
    pid: uuid.UUID = Field(..., alias="employmentPid")

class EmploymentCreate(InputConfig, EmploymentBase):
    pass

# Experience
class ExperienceBase(BaseConfig, BaseModel):
    title: StringField
    content: TextField
    start_date: StartDateField
    end_date: EndDateField

class ExperienceResponse(OutputConfig, ExperienceBase):
    pid: uuid.UUID = Field(..., alias="experiencePid")

class ExperienceCreate(InputConfig, ExperienceBase):
    pass

# Portfolio
class PortfolioBase(BaseConfig, BaseModel):
    email: EmailStr

class PortfolioCreate(InputConfig, PortfolioBase):
    pass

class PortfolioResponse(OutputConfig, PortfolioBase):
    pid: uuid.UUID = Field(..., alias="portfolioPid")

class PortfolioEducationResponse(PortfolioResponse):
    education: list[EducationResponse]

class PortfolioEmploymentResponse(PortfolioResponse):
    employment: list[EmploymentResponse]

class PortfolioExperienceResponse(PortfolioResponse):
    experiences: list[ExperienceResponse]

class PortfolioFullResponse(PortfolioResponse):
    education: list[EducationResponse]
    employment: list[EmploymentResponse]
    experiences: list[ExperienceResponse]