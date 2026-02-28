from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass


@dataclass
class TransactionalManager(ABC):
    """
    Эта штука нужна для единой точки работы с транзакцией бд типа понял хз у гпт спрашивай еще чтоб подробнее было
    но эт типа интерфейс потом поймешь крч
    """

    @abstractmethod
    async def commit(self) -> None: ...

    @abstractmethod
    async def flush(self) -> None: ...