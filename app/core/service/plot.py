import asyncio
from dataclasses import dataclass
from typing import List, Tuple

from core.domain.equipment import EquipmentFilter
from core.domain.factory import FactoryFilter
from core.domain.plot import Plot, PlotCreate, PlotFilter, PlotUpdate
from core.exception import ObjectDoesNotExistError
from core.port.equipment import IEquipmentRepository
from core.port.factory import IFactoryRepository
from core.port.fetcher import IFetcher
from core.port.plot import IPlotRepository, IPlotService
from core.port.plot_equipment import IPlotEquipmentRepository


@dataclass
class PlotService(IPlotService):
    plot_repository: IPlotRepository
    factory_repository: IFactoryRepository
    equipment_repository: IEquipmentRepository
    plot_equipment_repository: IPlotEquipmentRepository

    plot_equipment_fetcher: IFetcher

    async def get_list(
        self, *, limit: int = None, offset: int = None, filters: PlotFilter = None
    ) -> Tuple[List[Plot], int]:
        total = await self.plot_repository.count(filters=filters)
        if not total:
            return [], 0
        items = await self.plot_repository.get_list(
            limit=limit, offset=offset, filters=filters
        )
        await self._fetch(items)
        return items, total

    async def get_by_id(self, id: int) -> Plot:
        item = await self._get_by_id(id)
        await self._fetch([item])
        return item

    async def create(self, data: PlotCreate, equipment_ids: List[int] = None) -> Plot:
        await self._check_factory(data.factory_id)
        item = await self.plot_repository.create(data)
        await self._add_equpment(item, equipment_ids)
        await self._fetch([item])
        return item

    async def update(
        self, id: int, data: PlotUpdate, equipment_ids: List[int] = None
    ) -> Plot:
        item = await self._get_by_id(id)
        await self.plot_repository.update(item.id, data)
        await self._update_equpment(item, equipment_ids)
        return await self.get_by_id(id)

    async def delete(self, id: int) -> Plot:
        item = await self.get_by_id(id)
        await self.plot_repository.delete(id)
        return item

    async def _update_equpment(self, plot: Plot, ids: List[int] = None):
        if ids is None:
            return
        await self.plot_equipment_repository.remove_equipment(plot.id)
        await self._add_equpment(plot, ids)

    async def _add_equpment(self, plot: Plot, ids: List[int]):
        if not ids:
            return
        equipment = await self.equipment_repository.get_list(
            filters=EquipmentFilter(id_list=ids)
        )
        if not equipment:
            return
        await self.plot_equipment_repository.add_equipment(
            plot.id, [item.id for item in equipment]
        )

    async def _check_factory(self, factory_id: int):
        item = await self.factory_repository.get_one(FactoryFilter(id=factory_id))
        if not item:
            raise ObjectDoesNotExistError("Фабрика не найдена")

    async def _fetch(self, data: List[Plot]):
        await asyncio.gather(
            self.plot_equipment_fetcher.fetch(data),
        )

    async def _get_by_id(self, id: int) -> Plot:
        item = await self.plot_repository.get_one(PlotFilter(id=id))
        if not item:
            raise ObjectDoesNotExistError("Участок не найдена")
        return item
