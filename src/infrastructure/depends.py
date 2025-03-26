from src.domain.services.url import UrlService
from src.infrastructure.repositories.url import SQLAlchemyUrlRepository


async def get_url_service() -> UrlService:
    url_repository = SQLAlchemyUrlRepository()
    url_service = UrlService(url_repository)
    return url_service
