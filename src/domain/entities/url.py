from pydantic import BaseModel


class ULR(BaseModel):
    id: int
    url: str
    short_url: str
