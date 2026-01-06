import uuid
from pydantic import BaseModel, Field

# Relative
from .config import BaseConfig, OutputConfig, InputConfig
from .link import LinkCreate, ProjectLinkResponse
from .tag import TagCreate, ProjectTagResponse
from .types import StringField, TextField

class ProjectBase(BaseConfig, BaseModel):
    title: StringField
    image_url: StringField
    summary: StringField
    description: TextField

class ProjectResponse(OutputConfig, ProjectBase):
    pid: uuid.UUID = Field(..., alias="projectPid")
    tags: list[ProjectTagResponse]
    links: list[ProjectLinkResponse]

class ProjectCreate(InputConfig, ProjectBase):
    tags: list[TagCreate]
    links: list[LinkCreate]