from abc import ABC, abstractmethod
from typing import List, Tuple

from core.domain.plot import Plot, PlotCreate, PlotFilter, PlotUpdate


class IPlotRepository(ABC):
    @abstractmethod
    async def get_list(
        self, *, limit: int = None, offset: int = None, filters: PlotFilter = None
    ) -> List[Plot]:
        pass

    @abstractmethod
    async def count(self, filters: PlotFilter) -> int:
        pass

    @abstractmethod
    async def create(self, data: PlotCreate) -> Plot:
        pass

    @abstractmethod
    async def update(self, id: int, data: PlotUpdate) -> None:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass

    @abstractmethod
    async def get_one(self, filters: PlotFilter) -> Plot:
        pass


class IPlotService(ABC):
    @abstractmethod
    async def get_list(
        self, *, limit: int = None, offset: int = None, filters: PlotFilter = None
    ) -> Tuple[List[Plot], int]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Plot:
        pass

    @abstractmethod
    async def create(self, data: PlotCreate, equipment_ids: List[int] = None) -> Plot:
        pass

    @abstractmethod
    async def update(
        self, id: int, data: PlotUpdate, equipment_ids: List[int] = None
    ) -> Plot:
        pass

    @abstractmethod
    async def delete(self, id: int) -> Plot:
        pass
