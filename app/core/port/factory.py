from abc import ABC, abstractmethod
from typing import List, Tuple

from core.domain.factory import Factory, FactoryCreate, FactoryFilter, FactoryUpdate


class IFactoryRepository(ABC):
    @abstractmethod
    async def get_list(
        self, *, limit: int = None, offset: int = None, filters: FactoryFilter = None
    ) -> List[Factory]:
        pass

    @abstractmethod
    async def count(self, filters: FactoryFilter) -> int:
        pass

    @abstractmethod
    async def create(self, data: FactoryCreate) -> Factory:
        pass

    @abstractmethod
    async def update(self, id: int, data: FactoryUpdate) -> None:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass

    @abstractmethod
    async def get_one(self, filters: FactoryFilter) -> Factory:
        pass


class IFactoryService(ABC):
    @abstractmethod
    async def get_list(
        self, *, limit: int = None, offset: int = None, filters: FactoryFilter = None
    ) -> Tuple[List[Factory], int]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Factory:
        pass

    @abstractmethod
    async def create(self, data: FactoryCreate) -> Factory:
        pass

    @abstractmethod
    async def update(self, id: int, data: FactoryUpdate) -> Factory:
        pass

    @abstractmethod
    async def delete(self, id: int) -> Factory:
        pass
