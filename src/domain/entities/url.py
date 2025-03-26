from pydantic import BaseModel


class Url(BaseModel):
    id: int | None = None
    url: str
    short_url: str
