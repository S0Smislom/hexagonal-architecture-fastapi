from dataclasses import dataclass
from typing import List

from core.domain.factory import Factory
from core.domain.plot import PlotFilter
from core.port.fetcher import IFetcher
from core.port.plot import IPlotRepository


@dataclass
class FactoryPlotFetcher(IFetcher):
    plot_repository: IPlotRepository
    plot_equipment_fetcher: IFetcher

    async def fetch(self, data: List[Factory]):
        if not data:
            return
        id_map = {item.id: item for item in data}
        filters = PlotFilter(factory_id_list=[key for key in id_map])
        plots = await self.plot_repository.get_list(filters=filters)
        await self.plot_equipment_fetcher.fetch(plots)
        for plot in plots:
            factory = id_map[plot.factory_id]
            factory.plots.append(plot)
