from abc import ABC, abstractmethod

from .dto.url import GetByIdUrlDTO, GetByShortUrlDTO
from ..entities.url import Url


class UrlRepository(ABC):
    @abstractmethod
    async def create(self, create_url: Url) -> Url:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, get_url: GetByIdUrlDTO) -> Url | None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_short_url(self, get_url: GetByShortUrlDTO) -> Url | None:
        raise NotImplementedError
