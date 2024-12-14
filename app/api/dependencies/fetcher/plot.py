from api.dependencies.repository.equipment import get_equipment_repository
from api.dependencies.repository.plot_equipment import get_plot_equipment_repository
from core.port.equipment import IEquipmentRepository
from core.port.fetcher import IFetcher
from core.port.plot_equipment import IPlotEquipmentRepository
from core.service.fetchers.plot import PlotEquipmentFetcher
from fastapi import Depends


def get_plot_equipment_fetcher(
    plot_equipment_repository: IPlotEquipmentRepository = Depends(
        get_plot_equipment_repository
    ),
    equipment_repository: IEquipmentRepository = Depends(get_equipment_repository),
) -> IFetcher:
    return PlotEquipmentFetcher(
        plot_equipment_repository=plot_equipment_repository,
        equipment_repository=equipment_repository,
    )
