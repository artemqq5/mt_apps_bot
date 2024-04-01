import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from domain.middlewares.IsUserBanned import UserBannedMiddleware
from domain.middlewares.IsUserRegistration import UserRegistationMiddleware
from domain.routers.admin import admin_handler
from domain.routers.user import user_handler, user_no_team_handler

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

dp.include_routers(
    admin_handler.router,
    user_handler.router,
    user_no_team_handler.router,
)


async def main():
    logging.basicConfig(level=logging.INFO)
    default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(token=config.BOT_TOKEN, default=default_properties)

    try:
        dp.message.outer_middleware(UserRegistationMiddleware())  # register if user not registered
        dp.callback_query.outer_middleware(UserRegistationMiddleware())  # register if user not registered

        dp.message.outer_middleware(UserBannedMiddleware())  # check if user banned
        dp.callback_query.outer_middleware(UserBannedMiddleware())  # check if user banned

        # start bot
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        print(f"start bot: {e}")
        return


if __name__ == '__main__':
    asyncio.run(main())
