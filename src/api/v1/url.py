from fastapi import APIRouter, Depends

from src.domain.repositories.dto.url import CreateUrlDTO, GetByIdUrlDTO, UrlDTO, GetByShortUrlDTO
from src.domain.services.url import UrlService
from src.infrastructure.depends import get_url_service

router = APIRouter(tags=['URL'], prefix='/url')


@router.post('/')
async def create_url(
        url_in: CreateUrlDTO,
        service: UrlService = Depends(get_url_service)
):
    return await service.create(url_in)


@router.get('/id/{url_id}', response_model=UrlDTO)
async def get_url_by_id(
        url_id: int,
        service: UrlService = Depends(get_url_service)
):
    get_url = GetByIdUrlDTO(id=url_id)
    return await service.get_by_id(get_url)


@router.get('/{short_url}', response_model=UrlDTO)
async def get_url_by_short_url(
        short_url: str,
        service: UrlService = Depends(get_url_service)
):
    get_url = GetByShortUrlDTO(short_url=short_url)
    return await service.get_by_short_url(get_url)
