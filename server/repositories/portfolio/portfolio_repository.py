from sqlalchemy.ext.asyncio import AsyncSession
from repositories.portfolio.writes import PortfolioWrites
from repositories.portfolio.queries import PortfolioQueries

class PortfolioRepository():
    def __init__(self, session: AsyncSession):
        self.writes = PortfolioWrites(session)
        self.queries = PortfolioQueries(session)


    
    