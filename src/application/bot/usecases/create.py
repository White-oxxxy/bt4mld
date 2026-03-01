from dataclasses import dataclass
import logging

from application.bot.dto.text import TextDto
from application.bot.ports.datamappers.text import TextDataMapper
from application.common.ports.transactional_manager import TransactionalManager
from application.common.ports.id_generator import IdGenerator
from application.common.usecase.base import (
    BaseUseCaseCommand,
    BaseUseCaseResult,
    BaseUseCase,
)
from infra.common.adapters.log.constants import LogType


logger = logging.getLogger(__name__)


@dataclass(
    frozen=True,
    kw_only=True,
    slots=True,
)
class CreateTextUseCaseCommand(BaseUseCaseCommand):
    """
    Типа команда для нашего юз кейса мы в ней передаем данные для нашего сценария нужные
    """

    content: str


@dataclass(
    frozen=True,
    kw_only=True,
    slots=True,
)
class CreateTextUseCaseResult(BaseUseCaseResult):
    """
    Типа данные которые мы возвращаем после выполнения сценария нужные внешнему миру но в этом юзкейсе ничо не надо
    возвращать поэтому тут пуста
    """

    ...


@dataclass
class CreateTextUseCase(BaseUseCase[CreateTextUseCaseCommand, CreateTextUseCaseResult]):
    _transactional_manager: TransactionalManager
    _text_datamapper: TextDataMapper
    _id_generator: IdGenerator

    async def act(self, command: CreateTextUseCaseCommand) -> CreateTextUseCaseResult:
        """
        крч тут у нас типа идет сценарий использования нашей хуйни и последовательность шагов
        1. мы создаем обьект текста который у нас TextDto
        2. вызываем соответствующий метод у нашего датамаппер
        3. комитим транзакцию с помощью транзакционал_манагера нашего что бы типа зафиксировать изменения в бд
        """

        new_text = TextDto(
            text_id=self._id_generator.generate_id(),
            content=command.content,
        )

        await self._text_datamapper.create(text=new_text)

        await self._transactional_manager.commit()

        logger.info(
            msg="Create text usecase: text added into db!",
            extra={
                "content": new_text.content,
                "log_type": LogType.ANALYTIC,
            }
        )

        result = CreateTextUseCaseResult()

        return result