from adapters.repository.sqlalchemy.repository.plot_equipment import (
    PlotEquipmentRepository,
)
from core.port.plot_equipment import IPlotEquipmentRepository
from fastapi import Depends

from .db import get_session


def get_plot_equipment_repository(
    session=Depends(get_session),
) -> IPlotEquipmentRepository:
    return PlotEquipmentRepository(session)
