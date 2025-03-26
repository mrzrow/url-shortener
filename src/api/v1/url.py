from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from pydantic import HttpUrl

from src.domain.entities.url import Url
from src.domain.repositories.dto.url import CreateUrlDTO, GetByIdUrlDTO, GetByShortUrlDTO, GetShortUrlDTO
from src.domain.services.url import UrlService
from src.infrastructure.depends import get_url_service

router = APIRouter(tags=['URL'], prefix='/url')


@router.post('/', response_model=GetShortUrlDTO)
async def create_url(
        url_in: CreateUrlDTO,
        request: Request,
        service: UrlService = Depends(get_url_service)
):
    base_url = HttpUrl(str(request.url))
    result = await service.create(url_in)
    return GetShortUrlDTO(
        short_url=HttpUrl(f'{base_url}{result.short_url}')
    )


@router.get('/id/{url_id}', response_model=Url)
async def get_url_by_id(
        url_id: int,
        service: UrlService = Depends(get_url_service)
):
    get_url = GetByIdUrlDTO(id=url_id)
    return await service.get_by_id(get_url)


@router.get('/{short_url}', response_class=RedirectResponse)
async def get_url_by_short_url(
        short_url: str,
        service: UrlService = Depends(get_url_service)
):
    get_url = GetByShortUrlDTO(short_url=short_url)
    url = await service.get_by_short_url(get_url)
    return RedirectResponse(url.url)
