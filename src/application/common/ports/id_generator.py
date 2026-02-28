from abc import (
    ABC,
    abstractmethod,
)
from uuid import UUID


class IdGenerator(ABC):
    """
    Типа единая точка генерации уникальных индентификаторов будет в наешй бл
    """

    @staticmethod
    @abstractmethod
    def generate_id() -> UUID: ...