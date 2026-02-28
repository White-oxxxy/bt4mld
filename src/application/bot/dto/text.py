from dataclasses import dataclass
from uuid import UUID

from application.common.dto import ApplicationDto


@dataclass(
    frozen=True,
    slots=True,
)
class TextDto(ApplicationDto):
    """
    дтошка текста типа
    """

    text_id: UUID
    content: str