from typing import List

from adapters.repository.sqlalchemy.models.equipment import Equipment as EquipmentDAO
from adapters.repository.sqlalchemy.models.plot import Plot as PlotDAO
from adapters.repository.sqlalchemy.models.plot_equipment import (
    PlotEquipment as PlotEquipmentDAO,
)
from core.domain.plot_equipment import PlotEquipment, PlotEquipmentFilter
from core.port.plot_equipment import IPlotEquipmentRepository
from sqlalchemy import Select, delete, func, insert, select, update
from sqlalchemy.ext.asyncio.session import AsyncSession


class PlotEquipmentRepository(IPlotEquipmentRepository):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_list(self, filters: PlotEquipmentFilter) -> List[PlotEquipment]:
        stmt = select(PlotEquipmentDAO)
        stmt = self._prepare_filters(stmt, filters)
        result = await self._session.execute(stmt)
        return [item.serialize() for item in result.scalars().all()]

    async def add_equipment(self, plot_id: int, equipment_ids: List[int]) -> None:
        equipment_ids = await self._filter_equipment_ids(equipment_ids)
        if not equipment_ids:
            return
        objects_to_create = [
            PlotEquipmentDAO(plot_id=plot_id, equipment_id=item)
            for item in equipment_ids
        ]
        self._session.add_all(objects_to_create)
        await self._session.flush()

    async def _filter_equipment_ids(self, equipment_ids: List[int]) -> List[int]:
        stmt = select(EquipmentDAO.id).where(EquipmentDAO.id.in_(equipment_ids))
        res = await self._session.execute(stmt)
        return res.scalars().all()

    async def remove_equipment(self, plot_id: int):
        stmt = delete(PlotEquipmentDAO).where(PlotEquipmentDAO.plot_id == plot_id)
        await self._session.execute(stmt)

    def _prepare_filters(self, stmt: Select, filters: PlotEquipmentFilter) -> Select:
        if filters:
            if filters.equipment_id:
                stmt = stmt.where(PlotEquipmentDAO.equipment_id == filters.equipment_id)
            if filters.equipment_id_list:
                stmt = stmt.where(
                    PlotEquipmentDAO.equipment_id.in_(filters.equipment_id_list)
                )
            if filters.plot_id:
                stmt = stmt.where(PlotEquipmentDAO.plot_id == filters.plot_id)
            if filters.plot_id_list:
                stmt = stmt.where(PlotEquipmentDAO.plot_id.in_(filters.plot_id_list))
        return stmt
