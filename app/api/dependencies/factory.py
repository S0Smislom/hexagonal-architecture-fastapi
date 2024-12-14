from api.dependencies.fetcher.factory import get_factory_plot_fetcher
from api.dependencies.repository.factory import get_factory_repository
from core.port.factory import IFactoryRepository, IFactoryService
from core.port.fetcher import IFetcher
from core.service.factory import FactoryService
from fastapi import Depends


def get_factory_service(
    factory_repository: IFactoryRepository = Depends(get_factory_repository),
    factory_plot_fetcher: IFetcher = Depends(get_factory_plot_fetcher),
) -> IFactoryService:
    return FactoryService(
        factory_repository=factory_repository,
        factory_plot_fetcher=factory_plot_fetcher,
    )
