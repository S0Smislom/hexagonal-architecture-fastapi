from abc import ABC, abstractmethod


class IFetcher(ABC):
    @abstractmethod
    async def fetch(self, data: list):
        pass
