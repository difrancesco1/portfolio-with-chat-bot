import uuid
from pydantic import BaseModel,Field
from typing import Optional

from schemas import (
    BaseConfig,
    OutputConfig,
    InputConfig,
    EndDateField,
    StartDateField,
    StringField
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