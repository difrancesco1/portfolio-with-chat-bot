import uuid
from pydantic import BaseModel,Field

# Relative
from .bullet_point import BulletPointCreate, EducationBulletPointBase, EducationBulletPointResponse
from .config import BaseConfig, OutputConfig, InputConfig
from .types import EndDateField, StartDateField, StringField

# Education
class EducationBase(BaseConfig, BaseModel):
    major: StringField
    degree: StringField
    gpa: float | None = Field(default=None)
    start_date: StartDateField
    end_date: EndDateField = None

class EducationResponse(OutputConfig, EducationBase):
    pid: uuid.UUID = Field(..., alias="educationPid")
    bullet_points: list[EducationBulletPointResponse] = Field(..., alias="content")

class EducationCreate(InputConfig, EducationBase):
    bullet_points: list[BulletPointCreate] | None = Field(alias="content", default=None)

class EducationUpdate(BaseConfig, InputConfig, BaseModel):
    major: StringField | None = None
    degree: StringField | None = None
    gpa: float | None = Field(default=None)
    start_date: StartDateField
    end_date: EndDateField | None = None
    bullet_points: list[EducationBulletPointBase] | None = Field(
        default=None, 
        alias="content"
    )