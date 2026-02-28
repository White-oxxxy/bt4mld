import datetime

from sqlalchemy import sql
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)


class BaseModel(DeclarativeBase):
    """
    Базовый класс для орм модельки типа
    """
    ...


class TimedBaseModel(BaseModel):
    """
    Это типа наследник от базовой модели ток с полями для времени типа
    """

    __abstract__ = True

    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, server_default=sql.func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(
        nullable=False,
        server_default=sql.func.now(),
        onupdate=sql.func.now(),
    )