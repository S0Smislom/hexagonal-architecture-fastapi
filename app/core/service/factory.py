from dataclasses import dataclass
from typing import List, Tuple

from core.domain.factory import Factory, FactoryCreate, FactoryFilter, FactoryUpdate
from core.exception import ObjectDoesNotExistError
from core.port.factory import IFactoryRepository, IFactoryService
from core.port.fetcher import IFetcher


@dataclass
class FactoryService(IFactoryService):
    factory_repository: IFactoryRepository

    factory_plot_fetcher: IFetcher

    async def get_list(
        self, *, limit: int = None, offset: int = None, filters: FactoryFilter = None
    ) -> Tuple[List[Factory], int]:
        total = await self.factory_repository.count(filters=filters)
        if not total:
            return [], 0
        items = await self.factory_repository.get_list(
            limit=limit, offset=offset, filters=filters
        )
        await self._fetch(items)
        return items, total

    async def get_by_id(self, id: int) -> Factory:
        item = await self._get_by_id(id)
        await self._fetch([item])
        return item

    async def create(self, data: FactoryCreate) -> Factory:
        item = await self.factory_repository.create(data)
        await self._fetch([item])
        return item

    async def update(self, id: int, data: FactoryUpdate) -> Factory:
        item = await self._get_by_id(id)
        await self.factory_repository.update(item.id, data)
        return await self.get_by_id(id)

    async def delete(self, id: int) -> Factory:
        item = await self.get_by_id(id)
        await self.factory_repository.delete(id)
        return item

    async def _fetch(self, data: List[Factory]):
        await self.factory_plot_fetcher.fetch(data)

    async def _get_by_id(self, id: int) -> Factory:
        item = await self.factory_repository.get_one(FactoryFilter(id=id))
        if not item:
            raise ObjectDoesNotExistError("Фабрика не найдена")
        return item
