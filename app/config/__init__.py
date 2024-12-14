from pydantic_settings import BaseSettings


class Config(BaseSettings):
    VERSION: str = "0.0"
    DB_URL: str = "sqlite+aiosqlite:////absolute/path/to/sqlite.db"


config = Config()
