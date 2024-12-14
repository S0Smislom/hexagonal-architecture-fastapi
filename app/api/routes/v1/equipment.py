from typing import List

from api.dependencies.equipment import get_equipment_service
from api.dto.equipment import (
    EquipmentCreateDTO,
    EquipmentDTO,
    EquipmentFilterDTO,
    EquipmentUpdateDTO,
)
from core.port.equipment import IEquipmentService
from fastapi import APIRouter, Body, Depends, Path, status
from fastapi.responses import Response

v1_equipment_router = APIRouter()


@v1_equipment_router.get(
    "",
    response_model=List[EquipmentDTO],
)
async def get_equipment_list(
    filters: EquipmentFilterDTO = Depends(),
    service: IEquipmentService = Depends(get_equipment_service),
):
    items, total = await service.get_list(filters=filters.to_domain())
    return items


@v1_equipment_router.get(
    "/{item_id}",
    response_model=EquipmentDTO,
)
async def get_equipment_by_id(
    item_id: int = Path(...),
    service: IEquipmentService = Depends(get_equipment_service),
):
    return await service.get_by_id(item_id)


@v1_equipment_router.post("", response_model=EquipmentDTO)
async def create_equipment(
    data: EquipmentCreateDTO = Body(...),
    service: IEquipmentService = Depends(get_equipment_service),
):
    return await service.create(data.to_domain())


@v1_equipment_router.patch("/{item_id}", response_model=EquipmentDTO)
async def update_equipment(
    item_id: int = Path(...),
    data: EquipmentUpdateDTO = Body(...),
    service: IEquipmentService = Depends(get_equipment_service),
):
    return await service.update(item_id, data.to_domain())


@v1_equipment_router.delete(
    "/{item_id}",
    response_class=Response,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def get_equipment_by_id(
    item_id: int = Path(...),
    service: IEquipmentService = Depends(get_equipment_service),
):
    await service.delete(item_id)
