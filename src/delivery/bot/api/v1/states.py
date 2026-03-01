from aiogram.fsm.state import (
    State,
    StatesGroup,
)


class AddTextState(StatesGroup):
    TEXT = State()


class DeleteByIdState(StatesGroup):
    TEXT_ID = State()