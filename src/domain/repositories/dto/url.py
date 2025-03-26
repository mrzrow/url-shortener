from pydantic import BaseModel


class UrlDTO(BaseModel):
    id: int | None = None
    url: str
    short_url: str


class CreateUrlDTO(BaseModel):
    url: str


class GetByIdUrlDTO(BaseModel):
    id: int


class GetByShortUrlDTO(BaseModel):
    short_url: str
