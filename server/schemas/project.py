import uuid
from pydantic import BaseModel, Field

# Relative
from .config import BaseConfig, OutputConfig, InputConfig
from .link import LinkCreate, ProjectLinkBase, ProjectLinkResponse
from .tag import TagCreate, ProjectTagBase, ProjectTagResponse
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

class ProjectUpdate(BaseConfig, InputConfig, BaseModel):
    title: StringField | None = None
    image_url: StringField | None = None
    summary: StringField | None = None
    description: TextField | None = None
    tags: list[ProjectTagBase] | None = None
    links: list[ProjectLinkBase] | None = None