import sqlalchemy.orm
from core.domain.factory import Factory as FactoryDomain
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Factory(Base):
    __tablename__ = "factory"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    plots = relationship("Plot", back_populates="factory")

    def serialize(self) -> FactoryDomain:
        return FactoryDomain(id=self.id, title=self.title)
