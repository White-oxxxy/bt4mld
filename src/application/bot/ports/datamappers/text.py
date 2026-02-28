from abc import (
    ABC,
    abstractmethod,
)
from uuid import UUID

from application.common.ports.datamapper import DataMapper
from application.bot.dto.text import TextDto


class TextDataMapper(
    DataMapper,
    ABC,
):
    """
    Твой типа интерфейс для текст датамапера
    """

    @abstractmethod
    async def get_all(self) -> list[TextDto]: ...

    @abstractmethod
    async def create(self, text: TextDto) -> None: ...

    @abstractmethod
    async def delete_by_id(self, text_id: UUID) -> None: ...