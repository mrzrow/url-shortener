from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.models.base import Base


class UrlModel(Base):
    url: Mapped[str] = mapped_column(nullable=False, autoincrement=True)
    short_url: Mapped[str] = mapped_column(nullable=False, unique=True)
