from dishka import (
    Provider,
    Scope,
    provide,
)

from application.bot.usecases.create import CreateTextUseCase
from application.bot.usecases.get_all import GetAllTextsUseCase
from application.bot.usecases.delete_by_id.uc import DeleteTextByIdUseCase
from application.bot.ports.datamappers.text import TextDataMapper
from application.common.ports.id_generator import IdGenerator
from application.common.ports.transactional_manager import TransactionalManager


class UseCasesProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_create_text_case(
        self,
        dm: TextDataMapper,
        tm: TransactionalManager,
        id_gen: IdGenerator,
    ) -> CreateTextUseCase:
        usecase = CreateTextUseCase(
            _text_datamapper=dm,
            _id_generator=id_gen,
            _transactional_manager=tm,
        )

        return usecase

    @provide(scope=Scope.REQUEST)
    def provide_get_all_texts_case(self, dm: TextDataMapper) -> GetAllTextsUseCase:
        usecase = GetAllTextsUseCase(_text_datamapper=dm)

        return usecase

    @provide(scope=Scope.REQUEST)
    def provide_delete_by_id_case(
        self,
        dm: TextDataMapper,
        tm: TransactionalManager,
    ) -> DeleteTextByIdUseCase:
        usecase = DeleteTextByIdUseCase(
            _text_datamapper=dm,
            _transactional_manager=tm,
        )

        return usecase