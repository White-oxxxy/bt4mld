from dataclasses import dataclass
import logging
from uuid import UUID

from sqlalchemy import (
    Result,
    Select,
    delete,
    select,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.dml import ReturningDelete

from application.bot.dto.text import TextDto
from application.bot.ports.datamappers.text import TextDataMapper
from infra.bot.db.convertors.text import TextModelDtoConvertor
from infra.bot.db.models.text import TextModel
from infra.common.adapters.log.constants import LogType


logger = logging.getLogger(__name__)


@dataclass
class SQLAlchemyTextDataMapperImpl(TextDataMapper):
    """
    Это реализация нашей абстракции для работы с данными ака датамаппер вот тоже с гпт посоветуйся чо как и зачем
    ну крч оно все что делает это с помощью алхимии работает с базой данных твоей
    """

    _session: AsyncSession
    _dto_model_convertor: TextModelDtoConvertor

    async def get_all(self) -> list[TextDto]:
        """
        Метод для получения всех записей
        """

        stmt: Select[tuple["TextModel"]] = (select(TextModel))

        result: Result[tuple["TextModel"]] = await self._session.execute(statement=stmt)

        text_models: list[TextModel] = list(result.scalars().all())

        if len(text_models) == 0:
            logger.debug(
                msg="Text data mapper: no texts available!",
                extra={"log_type": LogType.DEV,},
            )

            return []

        logger.info(
            msg="Text data mapper: picked all texts",
            extra={"log_type": LogType.DEV},
        )

        texts: list[TextDto] = []

        for text_model in text_models:
            text: TextDto = self._dto_model_convertor.to_dto(model=text_model)

            texts.append(text)

        return texts

    async def create(self, text: TextDto) -> None:
        """
        метод для создания записи текста
        """

        model: TextModel = self._dto_model_convertor.to_model(dto=text)

        self._session.add(model)

        logger.info(
            msg="Text data mapper: text added into session, need flush or commit!",
            extra={
                "text_id": str(text.text_id),
                "session_id": id(self._session),
                "log_type": LogType.DEV,
            },
        )

    async def delete_by_id(self, text_id: UUID) -> None:
        """
        Метод для удаления текста
        """

        stmt: ReturningDelete[tuple[UUID]] = (
            delete(TextModel)
            .where(TextModel.id == text_id)
            .returning(TextModel.id)
        )

        result: Result = await self._session.execute(statement=stmt)

        if result.fetchone() is None:
            logger.debug(
                msg="Text data mapper: cannot delete non-existent text!",
                extra={
                    "text_id": str(text_id),
                    "session_id": id(self._session),
                    "log_type": LogType.DEV,
                },
            )

        logger.info(
            msg="Text data mapper: delete expression have executed, need flush or commit!",
            extra={
                "text_id": str(text_id),
                "session_id": id(self._session),
                "log_type": LogType.DEV,
            },
        )