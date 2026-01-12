import uuid
from pydantic import BaseModel, Field

# Relative
from .config import BaseConfig, OutputConfig, InputConfig
from .types import StringField

class TagBase(BaseConfig, BaseModel):
    tag: StringField

class TagResponse(OutputConfig, TagBase):
    pid: uuid.UUID = Field(..., alias="tagPid")

class TagCreate(InputConfig, TagBase):
    pass

class ProjectTagBase(BaseConfig, BaseModel):
    tag: TagResponse

class ProjectTagResponse(OutputConfig, ProjectTagBase):
    pass