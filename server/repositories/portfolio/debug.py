import uuid
from sqlalchemy import delete, exists, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from models import (
    Biography,
    BiographyBulletPoint,
    BulletPoint,
    Document,
    Education,
    Employment,
    Experience,
    Link,
    Portfolio
)
from .loaders import BIOGRAPHY_WITH_BULLETS

class PortfolioDebug:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_bio(self):
        stmt = select(Biography).options(BIOGRAPHY_WITH_BULLETS)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def get_all_bio_bp(self):
        stmt = select(BiographyBulletPoint).options(BIOGRAPHY_WITH_BULLETS)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def get_all_bp(self):
        stmt = select(BulletPoint)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def get_all_links(self):
        stmt = select(Link)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def clear_bp_tables(self):
        stmt = delete(BulletPoint)
        await self.session.execute(stmt)
    