from dishka import (
    Provider,
    Scope,
    provide,
)

from infra.bot.db.convertors.text import TextModelDtoConvertor


class InfraConvertorsProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_text_model_dto_convertor(self) -> TextModelDtoConvertor:

        return TextModelDtoConvertor()