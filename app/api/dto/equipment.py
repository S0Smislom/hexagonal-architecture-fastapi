from typing import List, Optional

from core.domain.equipment import EquipmentCreate, EquipmentFilter, EquipmentUpdate
from pydantic import BaseModel


class EquipmentDTO(BaseModel):
    id: int
    title: str


class EquipmentFilterDTO(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None

    def to_domain(self) -> EquipmentFilter:
        return EquipmentFilter(**self.model_dump(exclude_none=True))


class EquipmentCreateDTO(BaseModel):
    title: str

    def to_domain(self) -> EquipmentCreate:
        return EquipmentCreate(**self.model_dump(exclude_unset=True))


class EquipmentUpdateDTO(BaseModel):
    title: Optional[str] = None

    def to_domain(self) -> EquipmentUpdate:
        return EquipmentUpdate(**self.model_dump(exclude_unset=True))
