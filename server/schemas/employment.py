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

# Employment
class EmploymentBase(BaseConfig, BaseModel):
    company: StringField
    position: StringField
    start_date: StartDateField
    end_date: EndDateField = None

class EmploymentResponse(OutputConfig, EmploymentBase):
    content: list[BulletPointResponse]
    pid: uuid.UUID = Field(..., alias="employmentPid")

class EmploymentCreate(InputConfig, EmploymentBase):
    pass