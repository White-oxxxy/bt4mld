from abc import ABC
from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class ApplicationDto(ABC):
    """
    Базовая дтошка типа чек у гпт чо такое дто
    """
    ...