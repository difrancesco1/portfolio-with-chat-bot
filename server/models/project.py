import uuid
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from typing import TYPE_CHECKING

# Relative
from .base import Base
from .link import Link 
from .tag import Tag

if TYPE_CHECKING:
    from .portfolio import Portfolio

class Project(Base):
    __tablename__ = "project"

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
    title: Mapped[str] = mapped_column(String(64), nullable=False)
    # Set to default image later
    image_url: Mapped[str] = mapped_column(String(64), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    tags: Mapped[list["ProjectTag"]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    links: Mapped[list["ProjectLink"]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    portfolio_id: Mapped[int] = mapped_column(
        ForeignKey("portfolio.id", ondelete="CASCADE"),
        nullable=False
    )
    portfolio: Mapped["Portfolio"] = relationship(back_populates="projects")

class ProjectTag(Base):
    __tablename__ = "project_tag"

    project_id: Mapped[int] = mapped_column(
        ForeignKey("project.id", ondelete="CASCADE"), 
        primary_key=True
    )
    tag_id: Mapped[int] = mapped_column(
        ForeignKey("tag.id", ondelete="CASCADE"),
        primary_key=True
    )
    project: Mapped["Project"] = relationship(
        back_populates="tags",
        foreign_keys=[project_id]
    )
    tag: Mapped["Tag"] = relationship(
        foreign_keys=[tag_id],
        lazy="selectin"
    )
    
class ProjectLink(Base):
    __tablename__ = "project_link"

    project_id: Mapped[int] = mapped_column(
        ForeignKey("project.id", ondelete="CASCADE"), 
        primary_key=True
    )
    link_id: Mapped[int] = mapped_column(
        ForeignKey("link.id", ondelete="CASCADE"),
        primary_key=True
    )
    project: Mapped["Project"] = relationship(
        back_populates="links",
        foreign_keys=[project_id]
    )
    link: Mapped["Link"] = relationship(
        foreign_keys=[link_id],
        lazy="selectin"
    )