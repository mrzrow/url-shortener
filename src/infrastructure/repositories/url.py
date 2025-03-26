from sqlalchemy import select

from src.domain.entities.url import Url
from src.domain.repositories.url import UrlRepository
from src.domain.repositories.dto.url import GetByIdUrlDTO, GetByShortUrlDTO
from src.infrastructure.database.db_helper import db_helper
from src.infrastructure.database.models.url import UrlModel


class SQLAlchemyUrlRepository(UrlRepository):
    async def create(self, create_url: Url) -> Url:
        async with db_helper.session_dependency() as session:
            url_dump = create_url.model_dump()
            url = UrlModel(**url_dump)
            session.add(url)
            await session.commit()
            await session.refresh(url)
            return Url(
                id=url.id,
                url=url.url,
                short_url=url.short_url
            )

    async def get_by_id(self, get_url: GetByIdUrlDTO) -> Url | None:
        async with db_helper.session_dependency() as session:
            url = await session.get(UrlModel, get_url.id)
            if url is None:
                return None
            return Url(
                id=url.id,
                url=url.url,
                short_url=url.short_url
            )

    async def get_by_short_url(self, get_url: GetByShortUrlDTO) -> Url | None:
        async with db_helper.session_dependency() as session:
            stmt = select(UrlModel).where(UrlModel.short_url == get_url.short_url)
            result = await session.execute(stmt)
            url = result.scalar_one_or_none()
            if url is None:
                return url
            return Url(
                id=url.id,
                url=url.url,
                short_url=url.short_url
            )
