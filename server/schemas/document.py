import uuid
from datetime import date
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional
from typing_extensions import Annotated

from schemas import (
    BaseConfig,
    OutputConfig,
    InputConfig,
    TextField,
    StringField
)

class DocumentBase(BaseConfig, BaseModel):
    filename: StringField
    content_type: StringField

class DocumentResponse(OutputConfig, DocumentBase):
    pid: uuid.UUID = Field(..., alias="documentPid")