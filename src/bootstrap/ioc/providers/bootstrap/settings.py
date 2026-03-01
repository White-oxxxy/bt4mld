from dishka import (
    Provider,
    Scope,
    provide,
)

from bootstrap.settings import Settings


class SettingsProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_settings(self) -> Settings:
        return Settings()