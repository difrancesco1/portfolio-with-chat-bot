import uuid
from models import (
    Base, 
    Biography,
    Document,
    Education, 
    Employment, 
    Experience
)
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

class Portfolio(Base):
    __tablename__ = "portfolio"

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
    first_name: Mapped[str] = mapped_column(
        String(64), 
        nullable=False
    )
    last_name: Mapped[str] = mapped_column(
        String(64),
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(64), 
        unique=True,
        nullable=False
    )

    biography: Mapped["Biography | None"] = relationship(
        back_populates="portfolio",
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    document: Mapped["Document | None"] = relationship(
        back_populates="portfolio",
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    education: Mapped[list["Education"]] = relationship(
        back_populates="portfolio",
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    employment: Mapped[list["Employment"]] = relationship(
        back_populates="portfolio",
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    experiences: Mapped[list["Experience"]] = relationship(
        back_populates="portfolio",
        cascade="all, delete-orphan",
        passive_deletes=True
    )