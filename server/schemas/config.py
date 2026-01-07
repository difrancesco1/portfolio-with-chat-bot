# Configurations
from pydantic import BaseModel, ConfigDict

class BaseConfig:
    model_config = ConfigDict(
        populate_by_name=True
    )

class InputConfig:
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True
    )

class OutputConfig:
    model_config = ConfigDict(
        from_attributes=True,
        ser_json_by_alias=True,
    )