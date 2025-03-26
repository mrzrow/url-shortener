from pydantic import BaseModel


class CreateUrlDTO(BaseModel):
    url: str


class GetByIdUrlDTO(BaseModel):
    id: int


class GetByShortUrlDTO(BaseModel):
    short_url: str
