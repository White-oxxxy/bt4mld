from dishka import (
    Provider,
    Scope,
    provide,
)

from sqlalchemy.ext.asyncio import AsyncSession

from application.bot.ports.datamappers.text import TextDataMapper
from application.common.ports.id_generator import IdGenerator
from application.common.ports.transactional_manager import TransactionalManager
from infra.common.adapters.id_generator import IdGeneratorImpl
from infra.common.adapters.transactional_manager.impl import SQLAlchemyTransactionalManagerImpl
from infra.bot.adapters.data_mappers.text import SQLAlchemyTextDataMapperImpl
from infra.bot.db.convertors.text import TextModelDtoConvertor


class AdaptersProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_text_datamapper(
        self,
        session: AsyncSession,
        convertor: TextModelDtoConvertor,
    ) -> TextDataMapper:
        dm = SQLAlchemyTextDataMapperImpl(
            _session=session,
            _dto_model_convertor=convertor,
        )

        return dm

    @provide(scope=Scope.REQUEST)
    def provide_id_generator(self) -> IdGenerator:

        return IdGeneratorImpl()

    @provide(scope=Scope.REQUEST)
    def provide_tm(self, session: AsyncSession) -> TransactionalManager:
        tm = SQLAlchemyTransactionalManagerImpl(_session=session)

        return tm