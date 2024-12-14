from api.dependencies.fetcher.plot import get_plot_equipment_fetcher
from api.dependencies.repository.equipment import get_equipment_repository
from core.port.equipment import IEquipmentRepository, IEquipmentService
from core.port.fetcher import IFetcher
from core.service.equipment import EquipmentService
from fastapi import Depends


def get_equipment_service(
    equipment_repository: IEquipmentRepository = Depends(get_equipment_repository),
    plot_equipment_fetcher: IFetcher = Depends(get_plot_equipment_fetcher),
) -> IEquipmentService:
    return EquipmentService(
        equipment_repository=equipment_repository,
        plot_quipment_fetcher=plot_equipment_fetcher,
    )
