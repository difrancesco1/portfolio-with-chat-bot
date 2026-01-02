import uuid
from models import Base

from datetime import date
from sqlalchemy import Float, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

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
    email: Mapped[str] = mapped_column(String(64), unique=True)

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
    content: Mapped[str] = mapped_column(Text, nullable = False)

    start_date: Mapped[date] = mapped_column (nullable=False)
    end_date: Mapped[date] = mapped_column(nullable=True)

    portfolio: Mapped["Portfolio"] = relationship(back_populates="employment")
    
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
    content: Mapped[str] = mapped_column(Text, nullable=False)
    
    start_date: Mapped[date] = mapped_column(nullable=False)
    end_date: Mapped[date | None] = mapped_column()

    portfolio: Mapped["Portfolio"] = relationship(back_populates="experiences")