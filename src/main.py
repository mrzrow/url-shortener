import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.infrastructure.database.db_helper import db_helper
from src.infrastructure.database.models.base import Base

from src.api import router_v1


@asynccontextmanager
async def lifespan(_app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    try:
        yield
    finally:
        await db_helper.engine.dispose()


app = FastAPI(title='URL-Shortener', lifespan=lifespan)
app.include_router(router=router_v1)

if __name__ == '__main__':
    uvicorn.run(app)
