from dataclasses import dataclass

from application.common.usecase.exception import UseCaseException


@dataclass(eq=False)
class CannotConvertToUUIDException(UseCaseException):
    @property
    def message(self) -> str:
        message = "Cannot convert this into UUID!"

        return message