from fastapi import APIRouter

from .v1.url import router as url_router
from ..core.config import settings

router_v1 = APIRouter(prefix=settings.api_prefix)
router_v1.include_router(url_router)
