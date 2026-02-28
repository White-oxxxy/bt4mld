from application.bot.dto.text import TextDto
from infra.bot.db.models.text import TextModel


class TextModelDtoConvertor:
    @staticmethod
    def to_model(dto: TextDto) -> TextModel:
        model = TextModel(
            id=dto.text_id,
            content=dto.content,
        )

        return model

    @staticmethod
    def to_dto(model: TextModel) -> TextDto:
        dto = TextDto(
            text_id=model.id,
            content=model.content,
        )

        return dto