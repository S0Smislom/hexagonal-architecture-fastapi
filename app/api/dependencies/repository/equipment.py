from adapters.repository.sqlalchemy.repository.equipment import EquipmentRepository
from core.port.equipment import IEquipmentRepository
from fastapi import Depends

from .db import get_session


def get_equipment_repository(session=Depends(get_session)) -> IEquipmentRepository:
    return EquipmentRepository(session)
