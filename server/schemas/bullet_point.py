import uuid
from pydantic import BaseModel, Field
from schemas import (
    BaseConfig,
    OutputConfig,
    InputConfig,
    PositiveInt,
    StringField,
    TextField,
)

# Bullet Point
class BulletPointBase(BaseConfig, BaseModel):
    content: TextField
    position: PositiveInt

class BulletPointResponse(OutputConfig, BulletPointBase):
    pid: uuid.UUID = Field(..., alias="bulletPointPid")

# Change this.... When creating we may not need this information
class BulletPointCreate(InputConfig, BulletPointBase):
    parent_type: StringField
    parent_pid: uuid.UUID = Field(..., alias="parentPid")