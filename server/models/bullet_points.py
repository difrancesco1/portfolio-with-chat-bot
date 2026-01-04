import uuid
from models import (
    Base
)
from sqlalchemy import Index, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

class BulletPoint(Base):
    __tablename__ = "bullet_point"
    
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
    content: Mapped[str] = mapped_column(Text)
    position: Mapped[int] = mapped_column(nullable=False)
