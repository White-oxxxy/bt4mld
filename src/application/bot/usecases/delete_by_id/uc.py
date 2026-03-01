from dataclasses import dataclass
import logging
from uuid import UUID

from application.common.ports.transactional_manager import TransactionalManager
from application.common.usecase.base import (
    BaseUseCaseCommand,
    BaseUseCaseResult,
    BaseUseCase,
)
from application.bot.ports.datamappers.text import TextDataMapper
from application.bot.usecases.delete_by_id.exceptions import CannotConvertToUUIDException
from infra.common.adapters.log.constants import LogType


logger = logging.getLogger(__name__)


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class DeleteTextByIdUseCaseCommand(BaseUseCaseCommand):
    """
    хз бля ты наверное уже понял чо ета)
    """

    text_id: str


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class DeleteTextByIdUseCaseResult(BaseUseCaseResult):
    """
    аналогично)))00
    """

    ...


@dataclass
class DeleteTextByIdUseCase(BaseUseCase[DeleteTextByIdUseCaseCommand, DeleteTextByIdUseCaseResult]):
    _text_datamapper: TextDataMapper
    _transactional_manager: TransactionalManager

    async def act(self, command: DeleteTextByIdUseCaseCommand) -> DeleteTextByIdUseCaseResult:
        try:
            text_uuid = UUID(command.text_id)

        except:

            raise CannotConvertToUUIDException()

        await self._text_datamapper.delete_by_id(text_id=text_uuid)

        await self._transactional_manager.commit()

        logger.info(
            msg="Delete text usecase: text deleted from db!",
            extra={
                "text_id": command.text_id,
                "log_type": LogType.ANALYTIC,
            }
        )

        result = DeleteTextByIdUseCaseResult()

        return result