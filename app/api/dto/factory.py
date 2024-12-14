from typing import List, Optional

from api.dto.plot import PlotDTO
from core.domain.factory import FactoryCreate, FactoryFilter, FactoryUpdate
from pydantic import BaseModel


class FactoryDTO(BaseModel):
    id: int
    title: str
    plots: List[PlotDTO] = []


class FactoryFilterDTO(BaseModel):
    id: Optional[int] = None
    title: Optional[int] = None

    def to_domain(self) -> FactoryFilter:
        return FactoryFilter(**self.model_dump(exclude_none=True))


class FactoryCreateDTO(BaseModel):
    title: str

    def to_domain(self) -> FactoryCreate:
        return FactoryCreate(**self.model_dump(exclude_unset=True))


class FactoryUpdateDTO(BaseModel):
    title: Optional[str] = None

    def to_domain(self) -> FactoryUpdate:
        return FactoryUpdate(**self.model_dump(exclude_unset=True))
