from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from infra.bot.integrations.telegram.constants import BotButtons


class KeyboardsBuilder:
    """
    ааа ээээ это вот хуйняшка чисто генерить клавиатуры нашему ботику понял да)
    ничо сложного нету вроде)00
    """

    @staticmethod
    def create_menu_kb() -> ReplyKeyboardMarkup:
        buttons: list[KeyboardButton] = [
            KeyboardButton(text=BotButtons.ADD_TEXT),
            KeyboardButton(text=BotButtons.GET_ALL_TEXTS),
            KeyboardButton(text=BotButtons.DELETE_BY_ID),
            KeyboardButton(text=BotButtons.HELP),
        ]

        kb_builder = ReplyKeyboardBuilder()

        kb_builder.row(*buttons, width=3)

        kb: ReplyKeyboardMarkup = kb_builder.as_markup(
            one_type_keyboard=True,
            resize_keyboard=True,
        )

        return kb

    @staticmethod
    def create_back_to_manu_kb() -> ReplyKeyboardMarkup:
        buttons: list[KeyboardButton] = [
            KeyboardButton(text=BotButtons.BACK_TO_MENU),
        ]

        kb_builder = ReplyKeyboardBuilder()

        kb_builder.row(*buttons, width=3)

        kb: ReplyKeyboardMarkup = kb_builder.as_markup(
            one_type_keyboard=True,
            resize_keyboard=True,
        )

        return kb