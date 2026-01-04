import uuid
from pydantic import BaseModel, Field
from typing import Optional
from schemas import (
    BaseConfig,
    OutputConfig,
    InputConfig,
    BulletPointResponse,
    BulletPointCreate
)
# Biography
class BiographyBase(BaseConfig, BaseModel):
    pass

class BiographyResponse(OutputConfig, BiographyBase):
    content: list[BulletPointResponse]
    pid: uuid.UUID = Field(..., alias="biographyPid")

class BiographyCreate(InputConfig, BiographyBase):
    content: Optional[list[BulletPointCreate]] = None