from api.routes.v1 import v1_router
from config import Config, config
from fastapi import FastAPI


def init_api(config: Config) -> FastAPI:
    app = FastAPI(
        title="Polus",
        description="",
        version=config.VERSION,
        docs_url="/",
    )

    add_routes(app)
    return app


def add_routes(app: FastAPI):
    app.include_router(v1_router, prefix="/v1")


app = init_api(config)
