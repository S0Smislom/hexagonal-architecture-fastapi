from adapters.repository.sqlalchemy.models.factory import Factory as FactoryDAO
from core.domain.factory import Factory, FactoryCreate, FactoryFilter, FactoryUpdate
from core.port.factory import IFactoryRepository
from sqlalchemy import Select, delete, func, select, update
from sqlalchemy.ext.asyncio.session import AsyncSession


class FactoryRepository(IFactoryRepository):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def count(self, filters: FactoryFilter) -> int:
        stmt = select(func.count("*")).select_from(FactoryDAO)
        stmt = self._prepare_filters(stmt, filters)
        res = await self._session.execute(stmt)
        return res.scalar()

    async def get_list(self, *, limit=None, offset=None, filters=None):
        stmt = self._prepare_filters(select(FactoryDAO), filters)
        if limit is not None:
            stmt = stmt.limit(limit)
        if offset is not None:
            stmt = stmt.offset(offset)
        result = await self._session.execute(stmt)
        db_models = result.scalars().all()
        return [item.serialize() for item in db_models]

    async def create(self, data: FactoryCreate) -> Factory:
        db_object = FactoryDAO(**data.model_dump(exclude_unset=True))
        self._session.add(db_object)
        await self._session.flush()
        return db_object.serialize()

    async def update(self, id, data: FactoryUpdate):
        stmt = (
            update(FactoryDAO)
            .where(FactoryDAO.id == id)
            .values(**data.model_dump(exclude_unset=True))
        )
        await self._session.execute(stmt)

    async def delete(self, id):
        stmt = delete(FactoryDAO).where(FactoryDAO.id == id)
        await self._session.execute(stmt)

    async def get_one(self, filters):
        stmt = self._prepare_filters(select(FactoryDAO), filters)
        result = await self._session.execute(stmt)
        db_model = result.scalar()
        return db_model.serialize() if db_model else None

    def _prepare_filters(self, stmt: Select, filters: FactoryFilter) -> Select:
        if filters:
            if filters.id:
                stmt = stmt.where(FactoryDAO.id == filters.id)
            if filters.id_list:
                stmt = stmt.where(FactoryDAO.id.in_(filters.id_list))
            if filters.title:
                stmt = stmt.where(FactoryDAO.title.icontains(filters.title))
        return stmt
