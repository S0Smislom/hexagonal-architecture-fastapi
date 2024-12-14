from abc import ABC, abstractmethod
from typing import List

from core.domain.plot_equipment import PlotEquipment, PlotEquipmentFilter


class IPlotEquipmentRepository(ABC):

    @abstractmethod
    async def get_list(self, filters: PlotEquipmentFilter) -> List[PlotEquipment]:
        pass

    @abstractmethod
    async def add_equipment(self, plot_id: int, equipment_ids: List[int]) -> None:
        pass

    @abstractmethod
    async def remove_equipment(self, plot_id: int):
        pass
