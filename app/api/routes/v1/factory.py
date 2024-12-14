from typing import List

from api.dependencies.factory import get_factory_service
from api.dto.factory import (
    FactoryCreateDTO,
    FactoryDTO,
    FactoryFilterDTO,
    FactoryUpdateDTO,
)
from core.port.factory import IFactoryService
from fastapi import APIRouter, Body, Depends, Path, status
from fastapi.responses import Response

v1_factory_router = APIRouter()


@v1_factory_router.get(
    "",
    response_model=List[FactoryDTO],
)
async def get_factory_list(
    filters: FactoryFilterDTO = Depends(),
    service: IFactoryService = Depends(get_factory_service),
):
    items, total = await service.get_list(filters=filters.to_domain())
    return items


@v1_factory_router.get(
    "/{item_id}",
    response_model=FactoryDTO,
)
async def get_factory_by_id(
    item_id: int = Path(...), service: IFactoryService = Depends(get_factory_service)
):
    return await service.get_by_id(item_id)


@v1_factory_router.post("", response_model=FactoryDTO)
async def create_factory(
    data: FactoryCreateDTO = Body(...),
    service: IFactoryService = Depends(get_factory_service),
):
    return await service.create(data.to_domain())


@v1_factory_router.patch("/{item_id}", response_model=FactoryDTO)
async def update_factory(
    item_id: int = Path(...),
    data: FactoryUpdateDTO = Body(...),
    service: IFactoryService = Depends(get_factory_service),
):
    return await service.update(item_id, data.to_domain())


@v1_factory_router.delete(
    "/{item_id}",
    response_class=Response,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def get_factory_by_id(
    item_id: int = Path(...), service: IFactoryService = Depends(get_factory_service)
):
    await service.delete(item_id)
