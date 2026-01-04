# Configurations
from pydantic import BaseModel, ConfigDict

class BaseConfig(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True
    )

class InputConfig(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        strip_white_space=True
    )

class OutputConfig(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        ser_json_by_alias=True,
    )