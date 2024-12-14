from typing import List, Optional

from pydantic import BaseModel


class PlotEquipment(BaseModel):
    plot_id: int
    equipment_id: int


class PlotEquipmentFilter(BaseModel):
    plot_id: Optional[int] = None
    plot_id_list: Optional[List[int]] = None
    equipment_id: Optional[int] = None
    equipment_id_list: Optional[List[int]] = None
