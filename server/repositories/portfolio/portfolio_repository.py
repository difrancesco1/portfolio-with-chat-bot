from sqlalchemy.ext.asyncio import AsyncSession
from repositories.portfolio.mutations import PortfolioMutations
from repositories.portfolio.writes import PortfolioWrites
from repositories.portfolio.queries import PortfolioQueries

from core.config import get_config

config = get_config()
if config.DEBUG:
    from .debug import PortfolioDebug
    
class PortfolioRepository():
    def __init__(self, session: AsyncSession):
        self.mutations = PortfolioMutations(session)
        self.writes = PortfolioWrites(session)
        self.queries = PortfolioQueries(session)
        if config.DEBUG:
            self.debug = PortfolioDebug(session)


    
    