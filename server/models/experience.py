import uuid
from datetime import date
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

# Relative
from .base import Base
from .bullet_points import BulletPoint
from .portfolio import Portfolio

class Experience(Base):
    __tablename__ = "experience"

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
    portfolio_id: Mapped[int] = mapped_column(
        ForeignKey("portfolio.id", ondelete="CASCADE"),
        nullable=False
    )
    title: Mapped[str] = mapped_column(String(64), nullable=False)
    
    start_date: Mapped[date] = mapped_column(nullable=False)
    end_date: Mapped[date | None] = mapped_column()

    portfolio: Mapped["Portfolio"] = relationship(back_populates="experiences")
    bullet_points: Mapped[list["ExperienceBulletPoint"]] = relationship(
        back_populates="experience",
        cascade="all, delete-orphan",
        order_by="ExperienceBulletPoint.position",
        lazy="selectin"
    )

class ExperienceBulletPoint(Base):
    __tablename__ = "experience_bullet_point"

    experience_id: Mapped[int] = mapped_column(
        ForeignKey("experience.id", ondelete="CASCADE"), 
        primary_key=True
    )
    bullet_point_id: Mapped[int] = mapped_column(
        ForeignKey("bullet_point.id", ondelete="CASCADE"), 
        primary_key=True
    )
    position: Mapped[int] = mapped_column(nullable=False)
    
    experience: Mapped["Experience"] = relationship(
        back_populates="bullet_points",
        foreign_keys=[experience_id]
    )
    bullet_point: Mapped["BulletPoint"] = relationship(
        foreign_keys=[bullet_point_id],
        lazy="selectin"
    )