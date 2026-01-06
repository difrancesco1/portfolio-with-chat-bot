import uuid
from pydantic import BaseModel, Field
from typing import Optional

# Relative
from .config import BaseConfig, OutputConfig, InputConfig
from .bullet_point import BulletPointCreate, ExperienceBulletPointResponse
from .types import EndDateField, StartDateField, StringField

# Experience
class ExperienceBase(BaseConfig, BaseModel):
    title: StringField
    start_date: StartDateField
    end_date: EndDateField

class ExperienceResponse(OutputConfig, ExperienceBase):
    bullet_points: list[ExperienceBulletPointResponse] = Field(..., alias="content")
    pid: uuid.UUID = Field(..., alias="experiencePid")

class ExperienceCreate(InputConfig, ExperienceBase):
    bullet_points: Optional[list[BulletPointCreate]] = Field(alias="content")