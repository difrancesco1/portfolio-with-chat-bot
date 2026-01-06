import uuid
from pydantic import BaseModel, Field
from typing import Optional

# Relative
from .config import BaseConfig, OutputConfig, InputConfig
from .bullet_point import BulletPointCreate, EmploymentBulletPointResponse
from .types import EndDateField, StartDateField, StringField

# Employment
class EmploymentBase(BaseConfig, BaseModel):
    company: StringField
    position: StringField
    start_date: StartDateField
    end_date: EndDateField = None

class EmploymentResponse(OutputConfig, EmploymentBase):
    bullet_points: list[EmploymentBulletPointResponse] = Field(alias="content")
    pid: uuid.UUID = Field(..., alias="employmentPid")

class EmploymentCreate(InputConfig, EmploymentBase):
    bullet_points: Optional[list[BulletPointCreate]] = Field(alias="content")