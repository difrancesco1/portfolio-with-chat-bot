import uuid
from pydantic import BaseModel, Field
from schemas import (
    BaseConfig,
    OutputConfig,
    InputConfig,
    BulletPointResponse,
    EndDateField,
    StartDateField,
    StringField,
)

# Experience
class ExperienceBase(BaseConfig, BaseModel):
    title: StringField
    start_date: StartDateField
    end_date: EndDateField

class ExperienceResponse(OutputConfig, ExperienceBase):
    content: list[BulletPointResponse]
    pid: uuid.UUID = Field(..., alias="experiencePid")

class ExperienceCreate(InputConfig, ExperienceBase):
    pass