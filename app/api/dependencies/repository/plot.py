from adapters.repository.sqlalchemy.repository.plot import PlotRepository
from core.port.plot import IPlotRepository
from fastapi import Depends

from .db import get_session


def get_plot_repository(session=Depends(get_session)) -> IPlotRepository:
    return PlotRepository(session)
