from core.domain.plot import Plot as PlotDomain
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Plot(Base):
    __tablename__ = "plot"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    factory_id = Column(Integer, ForeignKey("factory.id"))
    factory = relationship("Factory", back_populates="plots")

    equipment = relationship(
        "Equipment", secondary="plot_equipment", back_populates="plots"
    )

    def serialize(self) -> PlotDomain:
        return PlotDomain(
            id=self.id,
            title=self.title,
            factory_id=self.factory_id,
        )
