import uuid
from pydantic import BaseModel, Field
from typing import Optional

# Relative
from .config import BaseConfig, OutputConfig, InputConfig
from .bullet_point import BulletPointCreate, BiographyBulletPointBase, BiographyBulletPointResponse
from .types import TextField

# Biography
class BiographyBase(BaseConfig, BaseModel):
    description: TextField
    pass

class BiographyResponse(OutputConfig, BiographyBase):
    bullet_points: list[BiographyBulletPointResponse] = Field(..., alias="content")
    pid: uuid.UUID = Field(..., alias="biographyPid")

class BiographyCreate(InputConfig, BiographyBase):
    bullet_points: Optional[list[BulletPointCreate]] = Field(alias="content")

class BiographyUpdate(BaseConfig, InputConfig, BaseModel):
    description: TextField | None = None
    bullet_points: list[BiographyBulletPointBase] | None = Field(
        default=None, 
        alias="content"
    )