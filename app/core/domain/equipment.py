from typing import List, Optional

from pydantic import BaseModel


class Equipment(BaseModel):
    id: int
    title: str


class EquipmentCreate(BaseModel):
    title: str


class EquipmentUpdate(BaseModel):
    title: Optional[str] = None


class EquipmentFilter(BaseModel):
    id: Optional[int] = None
    id_list: Optional[List[int]] = None
    title: Optional[str] = None
