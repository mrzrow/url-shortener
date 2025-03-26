from pydantic import BaseModel, HttpUrl


class Url(BaseModel):
    id: int | None = None
    url: HttpUrl
    short_url: HttpUrl
