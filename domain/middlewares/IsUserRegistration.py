from typing import Callable, Any, Dict, Awaitable

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject, Update

from data.constants.just_message import REGISTER_FAIL, REGISTER_SUCCESS, SEND_REQUEST_TO_ADMIN
from data.repository.UserRepository import UserRepository


class UserRegistationMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if isinstance(event, types.Message) or isinstance(event, types.CallbackQuery):
            user = event.from_user
        else:
            print(type(event))
            return

        if not UserRepository().get_user(user.id):
            if not UserRepository().add_user(user.id, user.username, user.first_name, user.last_name, user.language_code):
                await event.bot.send_message(chat_id=user.id, text=REGISTER_FAIL)
                return None

            await event.bot.send_message(chat_id=user.id, text=REGISTER_SUCCESS)
            await event.bot.send_message(chat_id=user.id, text=SEND_REQUEST_TO_ADMIN)

        return await handler(event, data)

