from collections import defaultdict
from dataclasses import dataclass
from typing import List

from core.domain.equipment import EquipmentFilter
from core.domain.factory import Factory, FactoryFilter
from core.domain.plot import Plot
from core.domain.plot_equipment import PlotEquipmentFilter
from core.port.equipment import IEquipmentRepository
from core.port.factory import IFactoryRepository
from core.port.fetcher import IFetcher
from core.port.plot_equipment import IPlotEquipmentRepository


@dataclass
class PlotFactoryFetcher(IFetcher):
    factory_repository: IFactoryRepository

    async def fetch(self, data: List[Plot]):
        if not data:
            return
        factory_id_map = defaultdict(list)
        for item in data:
            factory_id_map[item.factory_id].append(item)

        filters = FactoryFilter(id_list=[item for item in factory_id_map])
        factories = await self.factory_repository.get_list(filters=filters)
        for factory in factories:
            for plot in factory_id_map[factory.id]:
                plot.factory = factory


@dataclass
class PlotEquipmentFetcher(IFetcher):
    plot_equipment_repository: IPlotEquipmentRepository
    equipment_repository: IEquipmentRepository

    async def fetch(self, data: List[Plot]):
        if not data:
            return

        id_map = {item.id: item for item in data}

        filters = PlotEquipmentFilter(plot_id_list=[item for item in id_map])
        plot_equipment = await self.plot_equipment_repository.get_list(filters=filters)
        if not plot_equipment:
            return
        equipment_plot_map = defaultdict(list)
        for item in plot_equipment:
            equipment_plot_map[item.equipment_id].append(id_map[item.plot_id])

        filters = EquipmentFilter(id_list=[item for item in equipment_plot_map])
        equipment = await self.equipment_repository.get_list(filters=filters)
        for item in equipment:
            for plot in equipment_plot_map[item.id]:
                plot.equipment.append(item)
