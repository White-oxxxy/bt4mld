from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from application.common.exceptions import ApplicationError


@dataclass(eq=False)
class UseCaseException(
    ApplicationError,
    ABC,
):
    @abstractmethod
    @property
    def message(self) -> str:
        message = f"Use case exception!"

        return message