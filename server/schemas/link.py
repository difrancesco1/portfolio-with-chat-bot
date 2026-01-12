import uuid
from pydantic import BaseModel, Field

# Relative
from .config import BaseConfig, OutputConfig, InputConfig
from .types import StringField

class LinkBase(BaseConfig, BaseModel):
    url: StringField
    platform: StringField

class LinkResponse(OutputConfig, LinkBase):
    pid: uuid.UUID = Field(..., alias="linkPid")

class LinkCreate(InputConfig, LinkBase):
    pass

class PortfolioLinkBase(BaseConfig, BaseModel):
    link: LinkResponse

class PortfolioLinkResponse(OutputConfig, PortfolioLinkBase):
    pass

class ProjectLinkBase(BaseConfig, BaseModel):
    link: LinkResponse

class ProjectLinkResponse(OutputConfig, ProjectLinkBase):
    pass