from pydantic import BaseModel, HttpUrl


class Url(BaseModel):
    id: int | None = None
    url: str
    short_url: str
