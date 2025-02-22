from sqlmodel import select, desc, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

class BaseService:
    def __init__(self, session:AsyncSession):
        # self.model = model
        self.session = session

    async def execute(self, statement):
        return await self.session.exec(statement)