from core.domain.equipment import Equipment as EquipmentDomain
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)

    plots = relationship("Plot", secondary="plot_equipment", back_populates="equipment")

    def serialize(self) -> EquipmentDomain:
        return EquipmentDomain(id=self.id, title=self.title)
