from aiogram.types import User
from aiogram_i18n.managers import BaseManager


class LocaleManager(BaseManager):

    async def set_locale(self, locale: str) -> None:
        pass

    async def get_locale(self, event_from_user: User) -> str:
        # if database is null do bellow:
        return event_from_user.language_code
