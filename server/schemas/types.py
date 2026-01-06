from datetime import date
from pydantic import Field
from typing import Optional
from typing_extensions import Annotated

# Annotations
EndDateField = Annotated[
    Optional[date],
    Field(
        alias="endDate"
    )
]

PositiveInt = Annotated[
    int,
    Field(
        ...,
        ge=0
    )
]

StartDateField = Annotated [
    date,
    Field(
        ...,
        alias="startDate",
    )
]

StringField = Annotated[
    str,
    Field(
        ...,
        min_length=1,
        max_length=64
    )
]

TextField = Annotated[
    str,
    Field(
        ...,
        min_length=1,
    )
]