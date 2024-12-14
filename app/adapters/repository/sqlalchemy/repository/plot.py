from adapters.repository.sqlalchemy.models.plot import Plot as PlotDAO
from core.domain.plot import Plot, PlotCreate, PlotFilter, PlotUpdate
from core.port.plot import IPlotRepository
from sqlalchemy import Select, delete, func, insert, select, update
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import Session


class PlotRepository(IPlotRepository):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def count(self, filters: PlotFilter) -> int:
        stmt = select(func.count("*")).select_from(PlotDAO)
        stmt = self._prepare_filters(stmt, filters)
        res = await self._session.execute(stmt)
        return res.scalar()

    async def get_list(self, *, limit=None, offset=None, filters=None):
        stmt = self._prepare_filters(select(PlotDAO), filters)
        if limit is not None:
            stmt = stmt.limit(limit)
        if offset is not None:
            stmt = stmt.offset(offset)
        result = await self._session.execute(stmt)
        db_models = result.scalars().all()
        return [item.serialize() for item in db_models]

    async def create(self, data: PlotCreate) -> Plot:
        db_object = PlotDAO(**data.model_dump(exclude_unset=True))
        self._session.add(db_object)
        await self._session.flush()
        return db_object.serialize()

    async def update(self, id, data: PlotUpdate):
        stmt = (
            update(PlotDAO)
            .where(PlotDAO.id == id)
            .values(**data.model_dump(exclude_unset=True))
        )
        await self._session.execute(stmt)

    async def delete(self, id):
        stmt = delete(PlotDAO).where(PlotDAO.id == id)
        await self._session.execute(stmt)

    async def get_one(self, filters):
        stmt = self._prepare_filters(select(PlotDAO), filters)
        result = await self._session.execute(stmt)
        db_model = result.scalar()
        return db_model.serialize() if db_model else None

    def _prepare_filters(self, stmt: Select, filters: PlotFilter) -> Select:
        if filters:
            if filters.id:
                stmt = stmt.where(PlotDAO.id == filters.id)
            if filters.id_list:
                stmt = stmt.where(PlotDAO.id.in_(filters.id_list))
            if filters.title:
                stmt = stmt.where(PlotDAO.title.icontains(filters.title))
            if filters.factory_id:
                stmt = stmt.where(PlotDAO.factory_id == filters.factory_id)
            if filters.factory_id_list:
                stmt = stmt.where(PlotDAO.factory_id.in_(filters.factory_id_list))
        return stmt
