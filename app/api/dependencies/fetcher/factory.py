from api.dependencies.fetcher.plot import get_plot_equipment_fetcher
from api.dependencies.repository.plot import get_plot_repository
from core.port.fetcher import IFetcher
from core.port.plot import IPlotRepository
from core.service.fetchers.factory import FactoryPlotFetcher
from fastapi import Depends


def get_factory_plot_fetcher(
    plot_repository: IPlotRepository = Depends(get_plot_repository),
    plot_equipment_fetcher: IFetcher = Depends(get_plot_equipment_fetcher),
) -> IFetcher:
    return FactoryPlotFetcher(
        plot_repository=plot_repository,
        plot_equipment_fetcher=plot_equipment_fetcher,
    )
