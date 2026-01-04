import uuid
from models import (
    Base,
    BulletPoint,
    Portfolio
)
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

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
        order_by="BiographyBulletPoint.bullet_point.position",
        lazy="selectin"
    )
    portfolio_id: Mapped[int] = mapped_column(
        ForeignKey("portfolio.id", ondelete="CASCADE"),
        nullable=False,
        unique=True
    )
    portfolio: Mapped["Portfolio"] = relationship(back_populates="biography")

class BiographyBulletPoint(Base):
    __tablename__ = "biography_bullet_point"

    biography_id: Mapped[int] = ForeignKey("biography.id", primary_key=True)
    bullet_point_id: Mapped[int] = ForeignKey("bullet_point.id", primary_key=True)

    biography: Mapped["Biography"] = relationship(back_populates="bullet_points")
    bullet_point: Mapped["BulletPoint"] = relationship(lazy="selectin")