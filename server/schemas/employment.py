import uuid
from pydantic import BaseModel, Field
from typing import Optional

# Relative
from .config import BaseConfig, OutputConfig, InputConfig
from .bullet_point import BulletPointCreate, EmploymentBulletPointResponse, EmploymentBulletPointBase
from .types import EndDateField, StartDateField, StringField

# Employment
class EmploymentBase(BaseConfig, BaseModel):
    company: StringField
    position: StringField
    start_date: StartDateField
    end_date: EndDateField | None = None

class EmploymentResponse(OutputConfig, EmploymentBase):
    bullet_points: list[EmploymentBulletPointResponse] = Field(alias="content")
    pid: uuid.UUID = Field(..., alias="employmentPid")

class EmploymentCreate(InputConfig, EmploymentBase):
    bullet_points: list[BulletPointCreate] | None = Field(alias="content", default=None)

class EmploymentUpdate(BaseConfig, InputConfig, BaseModel):
    company: StringField | None = None
    position: StringField | None = None
    start_date: StartDateField
    end_date: EndDateField | None = None
    bullet_points: list[EmploymentBulletPointBase] | None = Field(
        default=None, 
        alias="content"
    )
