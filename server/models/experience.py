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
        order_by="ExperienceBulletPoint.bullet_point.position",
        lazy="selectin"
    )

class ExperienceBulletPoint(Base):
    __tablename__ = "experience_bullet_point"

    experience_id: Mapped[int] = ForeignKey("experience.id", primary_key=True)
    bullet_point_id: Mapped[int] = ForeignKey("bullet_point.id", primary_key=True)

    experience: Mapped["Experience"] = relationship(back_populates="bullet_points")
    bullet_point: Mapped["BulletPoint"] = relationship(lazy="selectin")