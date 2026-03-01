from dishka import (
    AsyncContainer,
    Provider,
    make_async_container,
)
from dishka.integrations.aiogram import AiogramProvider

from bootstrap.ioc.providers.bootstrap.settings import SettingsProvider
from bootstrap.ioc.providers.infra.db import AlchemyProvider
from bootstrap.ioc.providers.infra.adapters import AdaptersProvider
from bootstrap.ioc.providers.infra.convertors import InfraConvertorsProvider
from bootstrap.ioc.providers.application.usecases import UseCasesProvider


DEV_PROVIDERS: list[Provider] = [
    SettingsProvider(),
    AlchemyProvider(),
    AdaptersProvider(),
    InfraConvertorsProvider(),
    UseCasesProvider(),
    AiogramProvider(),
]


def get_container() -> AsyncContainer:
    container: AsyncContainer = make_async_container(*DEV_PROVIDERS)

    return container