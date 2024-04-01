from typing import Callable, Any, Dict, Awaitable

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject, Update

from data.repository.UserRepository import UserRepository


class UserRoleMiddleware(BaseMiddleware):

    def __init__(self, role):
        self.role = role

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if isinstance(event, types.Message) or isinstance(event, types.CallbackQuery):
            user_id = event.from_user.id
        else:
            return

        if not UserRepository().is_admin(user_id)['role'] == self.role:
            return

        return await handler(event, data)
