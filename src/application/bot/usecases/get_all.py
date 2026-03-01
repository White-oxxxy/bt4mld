from dataclasses import dataclass
import logging

from application.bot.dto.text import TextDto
from application.common.usecase.base import (
    BaseUseCaseCommand,
    BaseUseCaseResult,
    BaseUseCase,
)
from application.bot.ports.datamappers.text import TextDataMapper
from infra.common.adapters.log.constants import LogType


logger = logging.getLogger(__name__)


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class GetAllTextsUseCaseCommand(BaseUseCaseCommand):
    """
    типа ээээ команда для получения всех записей
    """

    ...


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class GetAllTextsUseCaseResult(BaseUseCaseResult):
    """
    результа нашего кейсв на лицо буквально
    """

    texts: list[TextDto]


@dataclass
class GetAllTextsUseCase(BaseUseCase[GetAllTextsUseCaseCommand, GetAllTextsUseCaseResult]):
    _text_datamapper: TextDataMapper

    async def act(self, command: GetAllTextsUseCaseCommand) -> GetAllTextsUseCaseResult:
        """
        такс ну тут просто дергаем нужный нам метод и все чилл
        """

        texts: list[TextDto] = await self._text_datamapper.get_all()

        result = GetAllTextsUseCaseResult(texts=texts)

        logger.info(
            msg="Get all texts usecase: texts have gotten!",
            extra={"log_type": LogType.ANALYTIC}
        )

        return result

