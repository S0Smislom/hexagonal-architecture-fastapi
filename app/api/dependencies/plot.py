from api.dependencies.fetcher.plot import get_plot_equipment_fetcher
from api.dependencies.repository.equipment import get_equipment_repository
from api.dependencies.repository.factory import get_factory_repository
from api.dependencies.repository.plot import get_plot_repository
from api.dependencies.repository.plot_equipment import get_plot_equipment_repository
from core.port.equipment import IEquipmentRepository
from core.port.factory import IFactoryRepository
from core.port.fetcher import IFetcher
from core.port.plot import IPlotRepository, IPlotService
from core.port.plot_equipment import IPlotEquipmentRepository
from core.service.plot import PlotService
from fastapi import Depends


def get_plot_service(
    plot_repository: IPlotRepository = Depends(get_plot_repository),
    factory_repository: IFactoryRepository = Depends(get_factory_repository),
    equipment_repository: IEquipmentRepository = Depends(get_equipment_repository),
    plot_equipment_fetcher: IFetcher = Depends(get_plot_equipment_fetcher),
    plot_equipment_repository: IPlotEquipmentRepository = Depends(
        get_plot_equipment_repository
    ),
) -> IPlotService:
    return PlotService(
        plot_repository=plot_repository,
        factory_repository=factory_repository,
        equipment_repository=equipment_repository,
        plot_equipment_fetcher=plot_equipment_fetcher,
        plot_equipment_repository=plot_equipment_repository,
    )
