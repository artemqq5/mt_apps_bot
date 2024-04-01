from aiogram.filters import BaseFilter
from aiogram.types import Message

from data.constants.access import ADMIN, USER
from data.repository.UserRepository import UserRepository


class IsAdminFilter(BaseFilter):

    def __init__(self, is_admin: bool = True):
        self.is_admin = is_admin

    async def __call__(self, message: Message):
        return UserRepository().is_admin(message.from_user.id)['role'] == (ADMIN if self.is_admin else USER)
