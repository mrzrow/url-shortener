from src.domain.entities.url import Url
from src.domain.repositories.dto.url import CreateUrlDTO, GetByIdUrlDTO, GetByShortUrlDTO
from src.domain.repositories.url import UrlRepository
from src.infrastructure.utils.short_url import create_short_url


class UrlService:
    def __init__(self, repository: UrlRepository):
        self.repository = repository

    async def create(self, create_url: CreateUrlDTO) -> Url:
        short_url = create_short_url()
        url_dump = create_url.model_dump()
        url = Url(
            **url_dump,
            short_url=short_url
        )
        result = await self.repository.create(url)
        return result

    async def get_by_id(self, get_url: GetByIdUrlDTO) -> Url:
        url = await self.repository.get_by_id(get_url)
        if url is None:
            raise ValueError('Url not found')
        return url

    async def get_by_short_url(self, get_url: GetByShortUrlDTO) -> Url:
        url = await self.repository.get_by_short_url(get_url)
        if url is None:
            raise ValueError('Url not found')
        return url
