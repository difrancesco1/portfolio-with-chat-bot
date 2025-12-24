from models import Base

from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, func, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Portfolio(Base):
    __tablename__ = "portfolio"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True)

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

    id: Mapped[int] = mapped_column(primary_key=True)
    portfolio_id: Mapped[int] = mapped_column(
        ForeignKey("portfolio.id", ondelete="CASCADE"),
        nullable=False
    )

    major: Mapped[str] = mapped_column(String(64), nullable=False)
    degree: Mapped[str] = mapped_column(String(64), nullable=False)
    gpa: Mapped[float] = mapped_column(Float(precision=2))

    start_date: Mapped[datetime] = mapped_column (
        DateTime(timezone=True),
        nullable=False
    )
    end_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )

    portfolio: Mapped["Portfolio"] = relationship(back_populates="education")

class Employment(Base):
    __tablename__ = "employment"

    id: Mapped[int] = mapped_column(primary_key=True)
    portfolio_id: Mapped[int] = mapped_column(
        ForeignKey("portfolio.id", ondelete="CASCADE"),
        nullable=False
    )

    company: Mapped[str] = mapped_column(String(64), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable = False)

    start_date: Mapped[datetime] = mapped_column (
        DateTime(timezone=True),
        nullable=False
    )
    end_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )

    portfolio: Mapped["Portfolio"] = relationship(back_populates="employment")
    
class Experience(Base):
    __tablename__ = "experience"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    portfolio_id: Mapped[int] = mapped_column(
        ForeignKey("portfolio.id", ondelete="CASCADE"),
        nullable=False
    )

    title: Mapped[str] = mapped_column(String(64), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    
    start_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    end_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True)
    )

    portfolio: Mapped["Portfolio"] = relationship(back_populates="experience")