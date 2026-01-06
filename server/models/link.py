import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

# Relative
from .base import Base

class Link(Base):
    __tablename__ = "link"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )
    pid: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        default=uuid.uuid4,
        index=True
    )
    url: Mapped[str] = mapped_column(String(64), nullable=False)
    # Possible refactor to be an enum in the DB
    # Change default to Personal
    platform: Mapped[str] = mapped_column(String(64), nullable=False)