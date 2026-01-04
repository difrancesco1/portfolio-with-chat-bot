from datetime import date
import uuid
from models import (
    Base,
    BulletPoint, 
    Portfolio
)
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

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
        order_by="EmploymentBulletPoint.bullet_point.position",
        lazy="selectin"
    )

class EmploymentBulletPoint(Base):
    __tablename__ = "employment_bullet_point"

    employment_id: Mapped[int] = ForeignKey("employment.id", primary_key=True)
    bullet_point_id: Mapped[int] = ForeignKey("bullet_point.id", primary_key=True)

    employment: Mapped["Employment"] = relationship(back_populates="bullet_points")
    bullet_point: Mapped["BulletPoint"] = relationship(lazy="selectin")