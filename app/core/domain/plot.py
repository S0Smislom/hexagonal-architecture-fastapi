from typing import List, Optional

from pydantic import BaseModel

from .equipment import Equipment


class Plot(BaseModel):
    id: int
    title: str
    factory_id: int
    equipment: List[Equipment] = []


class PlotCreate(BaseModel):
    title: str
    factory_id: int


class PlotUpdate(BaseModel):
    title: Optional[str] = None


class PlotFilter(BaseModel):
    id: Optional[int] = None
    id_list: Optional[List[int]] = None
    title: Optional[str] = None
    factory_id: Optional[int] = None
    factory_id_list: Optional[List[int]] = None
