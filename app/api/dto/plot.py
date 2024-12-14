from typing import List, Optional

from api.dto.equipment import EquipmentDTO
from core.domain.plot import PlotCreate, PlotFilter, PlotUpdate
from pydantic import BaseModel


class PlotDTO(BaseModel):
    id: int
    title: str

    equipment: List[EquipmentDTO]


class PlotFilterDTO(BaseModel):
    id: Optional[int] = None
    title: Optional[int] = None
    factory_id: Optional[int] = None

    def to_domain(self) -> PlotFilter:
        return PlotFilter(**self.model_dump(exclude_none=True))


class PlotCreateDTO(BaseModel):
    title: str
    factory_id: int
    equipment_ids: Optional[List[int]] = None

    def to_domain(self) -> PlotCreate:
        return PlotCreate(**self.model_dump(exclude_unset=True))


class PlotUpdateDTO(BaseModel):
    title: Optional[str] = None
    equipment_ids: Optional[List[int]] = None

    def to_domain(self) -> PlotUpdate:
        return PlotUpdate(**self.model_dump(exclude_unset=True))
