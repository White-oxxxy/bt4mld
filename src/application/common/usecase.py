from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import (
    Generic,
    TypeVar,
)


@dataclass(
    kw_only=True,
    frozen=True,
    slots=True,
)
class BaseUseCaseCommand(ABC):
    """
    Базовый класс команды для юзкейса (типа данные которые нужны для определенного сценария)
    """
    ...


@dataclass(
    kw_only=True,
    frozen=True,
    slots=True,
)
class BaseUseCaseResult(ABC):
    """
    Базовый класс для результата юзкейса (типа что ты получаешь после определенного сценария)
    """
    ...


CommandType = TypeVar("CommandType", bound=BaseUseCaseCommand)
ResultType = TypeVar("ResultType", bound=BaseUseCaseResult)


@dataclass
class BaseUseCase(
    Generic[CommandType, ResultType],
    ABC
):
    @abstractmethod
    async def act(self, command: CommandType) -> ResultType:
        """
        Базовый класс для юзкейса типа
        """
        ...