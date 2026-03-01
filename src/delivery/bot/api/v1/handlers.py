from aiogram import (
    F,
    Router,
)
from aiogram.filters import (
    Command,
    CommandStart,
    StateFilter,
)
from aiogram.types import Message
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from dishka.integrations.aiogram import (
    FromDishka,
    inject,
)
from html import escape

from delivery.bot.api.v1.states import (
    AddTextState,
    DeleteByIdState,
)
from application.bot.usecases.create import (
    CreateTextUseCase,
    CreateTextUseCaseCommand,
    CreateTextUseCaseResult,
)
from application.bot.usecases.get_all import (
    GetAllTextsUseCase,
    GetAllTextsUseCaseCommand,
    GetAllTextsUseCaseResult,
)
from application.bot.usecases.delete_by_id.uc import (
    DeleteTextByIdUseCase,
    DeleteTextByIdUseCaseCommand,
    DeleteTextByIdUseCaseResult,
)
from infra.bot.integrations.telegram.kbd import KeyboardsBuilder
from infra.bot.integrations.telegram.constants import (
    BotAnswers,
    BotButtons,
)


text_router = Router()


@text_router.message(
    CommandStart(),
    StateFilter(default_state),
)
@inject
async def command_start_handler(
    message: Message,
    kb_builder: FromDishka[KeyboardsBuilder],
) -> None:
    """
    хэндлер на команду старт ничо необычного)))
    вообще давай по базе сразу чо тут везде
    крч смотри ээээ вначале мы обьявили роутер вон текст_роутер
    это мы с помощью него будем наши хендлеры привязывать к боту воть это аля узел связи
    мы юзаем его в форме декоратора ну ты видишь да хз у гпт спроси чо такое декоратор если не знаешь
    в него мы передает 2 параметра
    1. это то на что будет тригериться наш хэндлер в данном случае на команду старт
    2. это фильтр состояний типа в каком состоянии будет наш хэндлер работать типа в данном случае у нас это дэфолт стет
    потом идет декоратор inlect это вот читсо темка dishka для того что бы мы могли получать
    зависимости в нашем хэндлере из контейнера)
    потом идет сама функция типа ну понял да в ней почти всегда идет обьект Message
    эта хуйня типа смс понял да с помощью нее мы получаем инфу которая в чате и отправляем если кратко
    а кб билдер чисто класс для генерации клавиатур)000
    """

    await message.answer(
        text=BotAnswers.START,
        reply_markup=kb_builder.create_menu_kb(),
    )


@text_router.message(
    Command(commands="help"),
    StateFilter(default_state),
)
@inject
async def command_help_handler(
    message: Message,
    kb_builder: FromDishka[KeyboardsBuilder],
) -> None:
    """
    хэндлер на команду помощи тоже дэфолт)
    """

    await message.answer(
        text=BotAnswers.HELP,
        reply_markup=kb_builder.create_menu_kb(),
    )


@text_router.message(
    F.text == BotButtons.MENU,
    StateFilter(default_state),
)
@inject
async def command_menu_handler(
    message: Message,
    kb_builder: FromDishka[KeyboardsBuilder],
) -> None:
    """
    ну чисто хэндлер который тригерится на нажатие кнопочки меню))
    """

    await message.answer(
        text=BotAnswers.MENU,
        reply_markup=kb_builder.create_menu_kb(),
    )


@text_router.message(
    F.text == BotButtons.BACK_TO_MENU,
    ~StateFilter(default_state),
)
@inject
async def command_back_to_menu_while_any_state_handler(
    message: Message,
    state: FSMContext,
    kb_builder: FromDishka[KeyboardsBuilder],
) -> None:
    """
    это чисто хэндлер который реактит на кнопочку вернуться в меню и он ЧИСТИТ состояние понял да
    вот эта хуйня ~ (тильда) которая перед стейтфильтр
    она обозначает что у нас он будет проходить фильтр состояний на любое КРОМЕ дэфолтного
    """

    await message.answer(
        text=BotAnswers.MENU,
        reply_markup=kb_builder.create_menu_kb(),
    )

    await state.clear()


@text_router.message(
    F.text == BotButtons.ADD_TEXT,
    StateFilter(default_state),
)
@inject
async def command_add_text_handler(
    message: Message,
    state: FSMContext,
    kb_builder: FromDishka[KeyboardsBuilder],
) -> None:
    """
    хэндлер который реактит на кнопочку добавить текст и устанавливает состояние AddText для дальнейшей работы КЕКВ
    """

    await state.set_state(state=AddTextState.TEXT)

    await message.answer(
        text=BotAnswers.INSERT_TEXT,
        reply_markup=kb_builder.create_back_to_manu_kb(),
    )


@text_router.message(StateFilter(AddTextState.TEXT))
@inject
async def insert_text_handler(
    message: Message,
    state: FSMContext,
    kb_builder: FromDishka[KeyboardsBuilder],
    usecsae: FromDishka[CreateTextUseCase],
) -> None:
    """
    крч это хэндлер СОСТОЯНИЯ вот в чом смысл когда чел нажал кнопку добавить текст отработал нащ
    хэндлер выше он поставил состояние AddText, и потом тригерится этот хэндлер на это состояние,
    и тут мы типа дергаем наш юз_кейсик вот и ФСЯ мораль
    ну и типа потом не забываем стейт почистить.
    """

    command = CreateTextUseCaseCommand(content=message.text)

    result: CreateTextUseCaseResult = await usecsae.act(command=command)

    await message.answer(
        text=BotAnswers.SUCCESS_TEXT_ADDED,
        reply_markup=kb_builder.create_menu_kb(),
    )

    await state.clear()


@text_router.message(
    F.text == BotButtons.GET_ALL_TEXTS,
    StateFilter(default_state),
)
@inject
async def command_get_all_texts_handler(
    message: Message,
    kb_builder: FromDishka[KeyboardsBuilder],
    usecase: FromDishka[GetAllTextsUseCase],
) -> None:
    """
    хз мне лень тут делать по уму просто будет тупа список и похуй что куча корнер кейсов вот
    а эт типа хендлер на кнопочку получить все текста когда в чате тг нажимаешь и он выводит типа список всех текстов
    которые ты добавил ЛОЛ
    """

    command  = GetAllTextsUseCaseCommand()

    result: GetAllTextsUseCaseResult = await usecase.act(command=command)

    if len(result.texts) == 0:
        await message.answer(
            text=BotAnswers.EMPTY_TEXT_LIST,
            reply_markup=kb_builder.create_menu_kb(),
        )

        return

    """
    мне ваще пох этот кусок гпт нагенерил))
    """

    text_parts = [f"<b>{BotAnswers.RESULT}</b>\n"]
    for i, dto in enumerate(result.texts, 1):
        safe_content = escape(dto.content)
        content_preview = safe_content[:100] + "..." if len(safe_content) > 100 else safe_content
        text_parts.append(f"{i}. <code>{content_preview}</code>")

    full_text = "\n".join(text_parts)

    await message.answer(
        full_text,
        parse_mode="HTML",
        reply_markup=kb_builder.create_menu_kb(),
    )


@text_router.message(
    F.text == BotButtons.DELETE_BY_ID,
    StateFilter(default_state),
)
@inject
async def command_delete_text_by_id_handler(
    message: Message,
    state: FSMContext,
    kb_builder: FromDishka[KeyboardsBuilder],
) -> None:
    """
    аналогично
    """

    await state.set_state(state=DeleteByIdState.TEXT_ID)

    await message.answer(
        text=BotAnswers.ENTER_ID,
        reply_markup=kb_builder.create_back_to_manu_kb(),
    )


@text_router.message(StateFilter(DeleteByIdState.TEXT_ID))
@inject
async def entering_text_id_for_deleting_text_handler(
    message: Message,
    state: FSMContext,
    kb_builder: FromDishka[KeyboardsBuilder],
    usecase: FromDishka[DeleteTextByIdUseCase],
) -> None:
    command = DeleteTextByIdUseCaseCommand(text_id=message.text)

    result: DeleteTextByIdUseCaseResult = await usecase.act(command=command)

    await message.answer(
        text=BotAnswers.SUCCESS_TEXT_REMOVED,
        reply_markup=kb_builder.create_menu_kb(),
    )

    await state.clear()