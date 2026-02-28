from uuid import UUID

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from uuid_utils import uuid7

from infra.common.db.model import TimedBaseModel


class TextModel(TimedBaseModel):
    """
    Типа это моделька алхимии для наших данных вот
    ну мы будем пока просто как мре текст тут хранить пон
    """

    __tablename__ = "text"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default_factory=uuid7,
    )
    content: Mapped[str] = mapped_column(nullable=False)
