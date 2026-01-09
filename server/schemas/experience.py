import uuid
from pydantic import BaseModel, Field
from typing import Optional

# Relative
from .config import BaseConfig, OutputConfig, InputConfig
from .bullet_point import BulletPointCreate, ExperienceBulletPointResponse, ExperienceBulletPointBase
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
    bullet_points: list[BulletPointCreate] | None = Field(alias="content", default=None)

class ExperienceUpdate(BaseConfig, InputConfig, BaseModel):
    title: StringField | None = None
    start_date: StartDateField | None = None
    end_date: EndDateField | None = None
    bullet_points: list[ExperienceBulletPointBase] | None = Field(
        default=None, 
        alias="content"
    )