from datetime import date
import uuid
from models import (
    Base, 
    Portfolio
)
from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

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

    portfolio: Mapped["Portfolio"] = relationship(back_populates="education")