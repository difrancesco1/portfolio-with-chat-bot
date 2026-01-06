import uuid
from pydantic import BaseModel, Field

from .config import BaseConfig, OutputConfig
from .types import StringField

class DocumentBase(BaseConfig, BaseModel):
    filename: StringField
    content_type: StringField

class DocumentResponse(OutputConfig, DocumentBase):
    pid: uuid.UUID = Field(..., alias="documentPid")