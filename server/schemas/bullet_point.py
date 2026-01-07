import uuid
from pydantic import BaseModel, Field
from core.enum import BulletPointType

# Relative
from .config import BaseConfig, OutputConfig, InputConfig
from .types import PositiveInt, TextField

# Bullet Point
class BulletPointBase(BaseConfig, BaseModel):
    content: TextField
    # Problem is that Bullet Point doesn't contain position anymore, and the position is in the cross reference class
    
    # position: PositiveInt

class BulletPointResponse(OutputConfig, BulletPointBase):
    pid: uuid.UUID = Field(..., alias="bulletPointPid")

# Change this.... When creating we may not need this information
class BulletPointCreate(InputConfig, BulletPointBase):
    position: PositiveInt
    parent_type: BulletPointType # May remove this later

class BiographyBulletPointBase(BaseConfig, BaseModel):
    position: PositiveInt
    bullet_point: BulletPointResponse

class BiographyBulletPointResponse(OutputConfig, BiographyBulletPointBase):
    pass

class EducationBulletPointResponse(OutputConfig, BaseModel):
    position: PositiveInt
    bullet_point: BulletPointResponse

class EmploymentBulletPointResponse(OutputConfig, BaseModel):
    position: PositiveInt
    bullet_point: BulletPointResponse

class ExperienceBulletPointResponse(OutputConfig, BaseModel):
    position: PositiveInt
    bullet_point: BulletPointResponse