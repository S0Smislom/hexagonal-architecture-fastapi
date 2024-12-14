from typing import List, Optional

from pydantic import BaseModel

from .plot import Plot


class Factory(BaseModel):
    id: int
    title: str

    plots: List[Plot] = []


class FactoryCreate(BaseModel):
    title: str


class FactoryUpdate(BaseModel):
    title: Optional[str] = None


class FactoryFilter(BaseModel):
    id: Optional[int] = None
    id_list: Optional[List[int]] = None
    title: Optional[str] = None
