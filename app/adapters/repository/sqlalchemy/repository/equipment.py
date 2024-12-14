from adapters.repository.sqlalchemy.models.equipment import Equipment as EquipmentDAO
from core.domain.equipment import (
    Equipment,
    EquipmentCreate,
    EquipmentFilter,
    EquipmentUpdate,
)
from core.port.equipment import IEquipmentRepository
from sqlalchemy import Select, delete, func, select, update
from sqlalchemy.ext.asyncio.session import AsyncSession


class EquipmentRepository(IEquipmentRepository):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def count(self, filters: EquipmentFilter) -> int:
        stmt = select(func.count("*")).select_from(EquipmentDAO)
        stmt = self._prepare_filters(stmt, filters)
        res = await self._session.execute(stmt)
        return res.scalar()

    async def get_list(self, *, limit=None, offset=None, filters=None):
        stmt = self._prepare_filters(select(EquipmentDAO), filters)
        if limit is not None:
            stmt = stmt.limit(limit)
        if offset is not None:
            stmt = stmt.offset(offset)
        result = await self._session.execute(stmt)
        db_models = result.scalars().all()
        return [item.serialize() for item in db_models]

    async def create(self, data: EquipmentCreate) -> Equipment:
        db_object = EquipmentDAO(**data.model_dump(exclude_unset=True))
        self._session.add(db_object)
        await self._session.flush()
        return db_object.serialize()

    async def update(self, id, data: EquipmentUpdate):
        stmt = (
            update(EquipmentDAO)
            .where(EquipmentDAO.id == id)
            .values(**data.model_dump(exclude_unset=True))
        )
        await self._session.execute(stmt)

    async def delete(self, id):
        stmt = delete(EquipmentDAO).where(EquipmentDAO.id == id)
        await self._session.execute(stmt)

    async def get_one(self, filters):
        stmt = self._prepare_filters(select(EquipmentDAO), filters)
        result = await self._session.execute(stmt)
        db_model = result.scalar()
        return db_model.serialize() if db_model else None

    def _prepare_filters(self, stmt: Select, filters: EquipmentFilter) -> Select:
        if filters:
            if filters.id:
                stmt = stmt.where(EquipmentDAO.id == filters.id)
            if filters.id_list:
                stmt = stmt.where(EquipmentDAO.id.in_(filters.id_list))
            if filters.title:
                stmt = stmt.where(EquipmentDAO.title.icontains(filters.title))
        return stmt
