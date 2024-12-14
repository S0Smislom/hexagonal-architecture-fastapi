from abc import ABC, abstractmethod
from typing import List, Tuple

from core.domain.equipment import (
    Equipment,
    EquipmentCreate,
    EquipmentFilter,
    EquipmentUpdate,
)


class IEquipmentRepository(ABC):
    @abstractmethod
    async def get_list(
        self, *, limit: int = None, offset: int = None, filters: EquipmentFilter = None
    ) -> List[Equipment]:
        pass

    @abstractmethod
    async def count(self, filters: EquipmentFilter) -> int:
        pass

    @abstractmethod
    async def create(self, data: EquipmentCreate) -> Equipment:
        pass

    @abstractmethod
    async def update(self, id: int, data: EquipmentUpdate) -> None:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass

    @abstractmethod
    async def get_one(self, filters: EquipmentFilter) -> Equipment:
        pass


class IEquipmentService(ABC):
    @abstractmethod
    async def get_list(
        self, *, limit: int = None, offset: int = None, filters: EquipmentFilter = None
    ) -> Tuple[List[Equipment], int]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Equipment:
        pass

    @abstractmethod
    async def create(self, data: EquipmentCreate) -> Equipment:
        pass

    @abstractmethod
    async def update(self, id: int, data: EquipmentUpdate) -> Equipment:
        pass

    @abstractmethod
    async def delete(self, id: int) -> Equipment:
        pass
