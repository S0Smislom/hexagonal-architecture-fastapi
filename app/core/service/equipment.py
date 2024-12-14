from dataclasses import dataclass
from typing import List, Tuple

from core.domain.equipment import (
    Equipment,
    EquipmentCreate,
    EquipmentFilter,
    EquipmentUpdate,
)
from core.exception import ObjectDoesNotExistError
from core.port.equipment import IEquipmentRepository, IEquipmentService
from core.port.fetcher import IFetcher


@dataclass
class EquipmentService(IEquipmentService):
    equipment_repository: IEquipmentRepository

    plot_quipment_fetcher: IFetcher

    async def get_list(
        self, *, limit: int = None, offset: int = None, filters: EquipmentFilter = None
    ) -> Tuple[List[Equipment], int]:
        total = await self.equipment_repository.count(filters=filters)
        if not total:
            return [], 0
        items = await self.equipment_repository.get_list(
            limit=limit, offset=offset, filters=filters
        )
        await self._fetch(items)
        return items, total

    async def get_by_id(self, id: int) -> Equipment:
        item = await self._get_by_id(id)
        await self._fetch([item])
        return item

    async def create(self, data: EquipmentCreate) -> Equipment:
        item = await self.equipment_repository.create(data)
        await self._fetch([item])
        return item

    async def update(self, id: int, data: EquipmentUpdate) -> Equipment:
        item = await self._get_by_id(id)
        await self.equipment_repository.update(item.id, data)
        return await self.get_by_id(id)

    async def delete(self, id: int) -> Equipment:
        item = await self.get_by_id(id)
        await self.equipment_repository.delete(id)
        return item

    async def _fetch(self, data: List[Equipment]):
        await self.plot_quipment_fetcher.fetch(data)

    async def _get_by_id(self, id: int) -> Equipment:
        item = await self.equipment_repository.get_one(EquipmentFilter(id=id))
        if not item:
            raise ObjectDoesNotExistError("Оборудование не найдена")
        return item
