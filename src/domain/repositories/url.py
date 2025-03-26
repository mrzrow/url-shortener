from abc import ABC, abstractmethod

from .dto.url import UrlDTO, CreateUrlDTO, GetByIdUrlDTO, GetByShortUrlDTO


class UrlRepository(ABC):
    @abstractmethod
    async def create(self, create_url: UrlDTO) -> UrlDTO:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, get_url: GetByIdUrlDTO) -> UrlDTO | None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_short_url(self, get_url: GetByShortUrlDTO) -> UrlDTO | None:
        raise NotImplementedError
