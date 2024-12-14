from collections import defaultdict
from dataclasses import dataclass
from typing import List

from core.domain.equipment import Equipment
from core.domain.plot import PlotFilter
from core.domain.plot_equipment import PlotEquipmentFilter
from core.port.fetcher import IFetcher
from core.port.plot import IPlotRepository
from core.port.plot_equipment import IPlotEquipmentRepository


@dataclass
class EquipmentPlotFetcher(IFetcher):
    plot_equipment_repository: IPlotEquipmentRepository
    plot_repository: IPlotRepository

    async def fetch(self, data: List[Equipment]):
        if not data:
            return

        id_map = {item.id: item for item in data}

        filters = PlotEquipmentFilter(equipment_id_list=[item for item in id_map])

        plot_equipment = await self.plot_equipment_repository.get_list(filters=filters)
        equipment_plot_map = defaultdict(list)

        for item in plot_equipment:
            equipment_plot_map[item.plot_id].append(id_map[item.equipment_id])

        filters = PlotFilter(id_list=[item for item in equipment_plot_map])
        plots = await self.plot_repository.get_list(filters=filters)
        # TODO fetch factory

        for item in plots:
            for equipment in equipment_plot_map[item.id]:
                equipment.plots.append(item)
