from enum import StrEnum


class BotCommands(StrEnum):
    COMMAND_BUTTON_START = "/start"
    COMMAND_BUTTON_HELP = "/help"


class BotCommandDescriptions(StrEnum):
    COMMAND_BUTTON_START_DESCRIPTION = "Для начала работы нажмите сюда!"
    COMMAND_BUTTON_HELP_DESCRIPTION = "Информация"


class BotButtons(StrEnum):
    GET_ALL_TEXTS = "Все текста"
    ADD_TEXT = "Добавить текст"
    DELETE_BY_ID = "Удалить текст по айди"
    BACK_TO_MENU = "Назад в меню"
    MENU = "Меню"
    HELP = "Помогите!1"


class BotAnswers(StrEnum):
    START = "Типа проста бот пример лол"
    HELP = "Милди хуевый скорпион"
    MENU = "Вы в главном меню."
    RESULT_NOT_FOUND = "Ничего не найдено!"
    RESULT = "Результат поиска:"
    TO_ANOTHER_THINGS = "Я ничо не понял"
    INSERT_TEXT = "Вставьте желаемый текст:"
    SUCCESS_TEXT_ADDED = "Текст успешно добавлен!"
    SUCCESS_TEXT_REMOVED = "Текст успешно удален!"
    EMPTY_TEXT_LIST = "Список текстов пуст!"
    ENTER_ID = "Введите айди текста:"