import uuid
from sqlalchemy import ForeignKey, LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from typing import TYPE_CHECKING

# Relative
from .base import Base
if TYPE_CHECKING:
    from .portfolio import Portfolio

class Document(Base):
    __tablename__ = "document"
    
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
    filename: Mapped[str] = mapped_column(String(64), nullable=False)
    content_type: Mapped[str] = mapped_column(String(64), nullable=False)
    data: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)

    portfolio_id: Mapped[int] = mapped_column(
        ForeignKey("portfolio.id", ondelete="CASCADE"),
        nullable=False,
        unique=True
    )
    portfolio: Mapped["Portfolio"] = relationship(back_populates="document")