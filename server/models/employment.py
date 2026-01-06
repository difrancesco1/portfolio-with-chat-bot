from datetime import date
import uuid
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from typing import TYPE_CHECKING

# Relative
from .base import Base
from .bullet_points import BulletPoint
if TYPE_CHECKING:
    from .portfolio import Portfolio

class Employment(Base):
    __tablename__ = "employment"

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

    company: Mapped[str] = mapped_column(String(64), nullable=False)
    position: Mapped[str] = mapped_column(String(64), nullable=False)

    start_date: Mapped[date] = mapped_column (nullable=False)
    end_date: Mapped[date] = mapped_column(nullable=True)

    portfolio: Mapped["Portfolio"] = relationship(back_populates="employment")
    bullet_points: Mapped[list["EmploymentBulletPoint"]] = relationship(
        back_populates="employment",
        cascade="all, delete-orphan",
        order_by="EmploymentBulletPoint.position",
        lazy="selectin"
    )

class EmploymentBulletPoint(Base):
    __tablename__ = "employment_bullet_point"

    employment_id: Mapped[int] = mapped_column(
        ForeignKey("employment.id", ondelete="CASCADE"),
        primary_key=True
    )
    bullet_point_id: Mapped[int] = mapped_column(
        ForeignKey("bullet_point.id", ondelete="CASCADE"), 
        primary_key=True
    )
    position: Mapped[int] = mapped_column(nullable=False)

    employment: Mapped["Employment"] = relationship(
        back_populates="bullet_points",
        foreign_keys=[employment_id]
    )
    bullet_point: Mapped["BulletPoint"] = relationship(
        foreign_keys=[bullet_point_id],
        lazy="selectin"
    )