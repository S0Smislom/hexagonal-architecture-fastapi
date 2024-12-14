# from adapters.repository.sqlalchemy.models.base import SessionLocal
from config import config
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

engine = create_async_engine(config.DB_URL)

SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def get_session():
    async with SessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()
