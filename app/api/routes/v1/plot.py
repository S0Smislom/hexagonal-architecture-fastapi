from typing import List

from api.dependencies.plot import get_plot_service
from api.dto.plot import PlotCreateDTO, PlotDTO, PlotFilterDTO, PlotUpdateDTO
from core.port.plot import IPlotService
from fastapi import APIRouter, Body, Depends, Path, status
from fastapi.responses import Response

v1_plot_router = APIRouter()


@v1_plot_router.get(
    "",
    response_model=List[PlotDTO],
)
async def get_plot_list(
    filters: PlotFilterDTO = Depends(),
    service: IPlotService = Depends(get_plot_service),
):
    items, total = await service.get_list(filters=filters.to_domain())
    return items


@v1_plot_router.get(
    "/{item_id}",
    response_model=PlotDTO,
)
async def get_plot_by_id(
    item_id: int = Path(...), service: IPlotService = Depends(get_plot_service)
):
    return await service.get_by_id(item_id)


@v1_plot_router.post("", response_model=PlotDTO)
async def create_plot(
    data: PlotCreateDTO = Body(...),
    service: IPlotService = Depends(get_plot_service),
):
    return await service.create(data.to_domain(), data.equipment_ids)


@v1_plot_router.patch("/{item_id}", response_model=PlotDTO)
async def update_plot(
    item_id: int = Path(...),
    data: PlotUpdateDTO = Body(...),
    service: IPlotService = Depends(get_plot_service),
):
    return await service.update(item_id, data.to_domain(), data.equipment_ids)


@v1_plot_router.delete(
    "/{item_id}",
    response_class=Response,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def get_plot_by_id(
    item_id: int = Path(...), service: IPlotService = Depends(get_plot_service)
):
    await service.delete(item_id)
