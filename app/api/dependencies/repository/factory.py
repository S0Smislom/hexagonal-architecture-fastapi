from adapters.repository.sqlalchemy.repository.factory import FactoryRepository
from core.port.factory import IFactoryRepository
from fastapi import Depends

from .db import get_session


def get_factory_repository(session=Depends(get_session)) -> IFactoryRepository:
    return FactoryRepository(session)
