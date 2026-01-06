import uuid
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from typing import TYPE_CHECKING

# Relative
from .base import Base
if TYPE_CHECKING:
    from .biography import Biography
    from .document import Document
    from .education import Education
    from .employment import Employment
    from .experience import Experience
    from .link import Link
    from .project import Project

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

    biography: Mapped["Biography"] = relationship(
        back_populates="portfolio",
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    document: Mapped["Document"] = relationship(
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
    links: Mapped[list["PortfolioLink"]] = relationship(
        back_populates="portfolio",
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    projects: Mapped[list["Project"]] = relationship(
        back_populates="portfolio",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

class PortfolioLink(Base):
    __tablename__ = "portfolio_link"

    portfolio_id: Mapped[int] = mapped_column(
        ForeignKey("portfolio.id"), 
        primary_key=True
    )
    link_id: Mapped[int] = mapped_column(
        ForeignKey("link.id", ondelete="CASCADE"),
        primary_key=True
    )
    portfolio: Mapped["Portfolio"] = relationship(
        back_populates="links",
        foreign_keys=[portfolio_id]
    )
    link: Mapped["Link"] = relationship(
        foreign_keys=[link_id],
        lazy="selectin"
    )