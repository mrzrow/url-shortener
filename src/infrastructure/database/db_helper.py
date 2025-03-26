from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.core.config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    @asynccontextmanager
    async def session_dependency(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
        # async with self.session_factory() as session:
        #     try:
        #         yield session
        #     except Exception:
        #         await session.rollback()
        #         raise
        #     finally:
        #         await session.close()


db_helper = DatabaseHelper(
    url=settings.db.url,
    echo=settings.db.echo
)
