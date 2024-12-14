from api.routes.v1.equipment import v1_equipment_router
from api.routes.v1.factory import v1_factory_router
from api.routes.v1.plot import v1_plot_router
from fastapi import APIRouter

v1_router = APIRouter()


v1_router.include_router(v1_factory_router, prefix="/factory", tags=["Factory V1"])
v1_router.include_router(v1_plot_router, prefix="/plot", tags=["Plot V1"])
v1_router.include_router(
    v1_equipment_router, prefix="/equipment", tags=["Equipment V1"]
)
