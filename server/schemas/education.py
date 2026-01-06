import uuid
from pydantic import BaseModel,Field
from typing import Optional

# Relative
from .bullet_point import BulletPointCreate, EducationBulletPointResponse
from .config import BaseConfig, OutputConfig, InputConfig
from .types import EndDateField, StartDateField, StringField

# Education
class EducationBase(BaseConfig, BaseModel):
    major: StringField
    degree: StringField
    gpa: Optional[float] = Field(default=None)
    start_date: StartDateField
    end_date: EndDateField = None

class EducationResponse(OutputConfig, EducationBase):
    pid: uuid.UUID = Field(..., alias="educationPid")
    bullet_points: list[EducationBulletPointResponse] = Field(..., alias="content")

class EducationCreate(InputConfig, EducationBase):
    bullet_points: Optional[list[BulletPointCreate]] = Field(alias="content")