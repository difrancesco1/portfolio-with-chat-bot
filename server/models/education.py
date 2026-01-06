from datetime import date
import uuid
from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from typing import TYPE_CHECKING

# Relative
from .base import Base
from .bullet_points import BulletPoint
if TYPE_CHECKING:
    from .portfolio import Portfolio

class Education(Base):
    __tablename__ = "education"

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

    major: Mapped[str] = mapped_column(String(64), nullable=False)
    degree: Mapped[str] = mapped_column(String(64), nullable=False)
    gpa: Mapped[float] = mapped_column(Float(precision=2), nullable=True)

    start_date: Mapped[date] = mapped_column (nullable=False)
    end_date: Mapped[date] = mapped_column(nullable=True)

    bullet_points: Mapped[list["EducationBulletPoint"]] = relationship(
        back_populates="education",
        cascade="all, delete-orphan",
        passive_deletes=True,
        order_by="EducationBulletPoint.position",
        lazy="selectin"
    )

    portfolio: Mapped["Portfolio"] = relationship(back_populates="education")

class EducationBulletPoint(Base):
    __tablename__ = "education_bullet_point"

    education_id: Mapped[int] = mapped_column(
        ForeignKey("education.id", ondelete="CASCADE"), 
        primary_key=True
    )
    bullet_point_id: Mapped[int] = mapped_column(
        ForeignKey("bullet_point.id", ondelete="CASCADE"),
        primary_key=True
    )
    position: Mapped[int] = mapped_column(nullable=False)
    
    education: Mapped["Education"] = relationship(
        back_populates="bullet_points",
        foreign_keys=[education_id]
    )
    bullet_point: Mapped["BulletPoint"] = relationship()