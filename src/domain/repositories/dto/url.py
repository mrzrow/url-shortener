from pydantic import BaseModel, HttpUrl


class CreateUrlDTO(BaseModel):
    url: HttpUrl


class GetShortUrlDTO(BaseModel):
    short_url: HttpUrl


class GetByIdUrlDTO(BaseModel):
    id: int


class GetByShortUrlDTO(BaseModel):
    short_url: str
