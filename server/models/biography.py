import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from typing import TYPE_CHECKING

# Relative
from .base import Base
from .bullet_points import BulletPoint

if TYPE_CHECKING:
    from .portfolio import Portfolio

class Biography(Base):
    __tablename__ = "biography"
    
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
    bullet_points: Mapped[list["BiographyBulletPoint"]] = relationship(
        back_populates="biography",
        cascade="all, delete-orphan",
        passive_deletes=True,
        order_by="BiographyBulletPoint.position"
    )
    portfolio_id: Mapped[int] = mapped_column(
        ForeignKey("portfolio.id", ondelete="CASCADE"),
        nullable=False,
        unique=True
    )
    portfolio: Mapped["Portfolio"] = relationship(back_populates="biography")

class BiographyBulletPoint(Base):
    __tablename__ = "biography_bullet_point"

    biography_id: Mapped[int] = mapped_column(
        ForeignKey("biography.id", ondelete="CASCADE"), 
        primary_key=True
    )
    bullet_point_id: Mapped[int] = mapped_column(
        ForeignKey("bullet_point.id", ondelete="CASCADE"),
        primary_key=True
    )
    position: Mapped[int] = mapped_column(nullable=False)
    
    biography: Mapped["Biography"] = relationship(
        back_populates="bullet_points",
        foreign_keys=[biography_id]
    )
    bullet_point: Mapped["BulletPoint"] = relationship(
        foreign_keys=[bullet_point_id],
        lazy="selectin"
    )