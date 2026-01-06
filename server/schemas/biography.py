import uuid
from pydantic import BaseModel, Field
from typing import Optional

# Relative
from .config import BaseConfig, OutputConfig, InputConfig
from .bullet_point import BulletPointCreate, BiographyBulletPointResponse

# Biography
class BiographyBase(BaseConfig, BaseModel):
    pass

class BiographyResponse(OutputConfig, BiographyBase):
    bullet_points: list[BiographyBulletPointResponse] = Field(..., alias="content")
    pid: uuid.UUID = Field(..., alias="biographyPid")

class BiographyCreate(InputConfig, BiographyBase):
    bullet_points: Optional[list[BulletPointCreate]] = Field(alias="content")