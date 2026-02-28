from dataclasses import dataclass
from uuid import UUID

from uuid_utils import uuid7

from application.common.ports.id_generator import IdGenerator


@dataclass
class IdGeneratorImpl(IdGenerator):
    @staticmethod
    def generate_id() -> UUID:
        new_id: UUID = uuid7()

        return new_id