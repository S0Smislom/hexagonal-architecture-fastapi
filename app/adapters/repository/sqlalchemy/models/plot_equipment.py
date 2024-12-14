from core.domain.plot_equipment import PlotEquipment as PlotEquipmentDomain
from sqlalchemy import Column, ForeignKey, Integer

from .base import Base


class PlotEquipment(Base):
    __tablename__ = "plot_equipment"

    plot_id = Column(Integer, ForeignKey("plot.id"), primary_key=True)
    equipment_id = Column(Integer, ForeignKey("equipment.id"), primary_key=True)

    def serialize(self) -> PlotEquipmentDomain:
        return PlotEquipmentDomain(
            plot_id=self.plot_id,
            equipment_id=self.equipment_id,
        )
