from aiogram import Bot
from aiogram_i18n import I18nContext
from aiogram_i18n.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

from data.repositoryDB.UserRepository import UserRepository


class NotificationAdmin:
    @staticmethod  # Розсилка за списком (лише текст)
    async def __notify_list_text(bot: Bot, users, message, error_message):
        counter = 0

        for user in users:
            try:
                await bot.send_message(chat_id=user, text=message)
                counter += 1
            except Exception as e:
                print(f"{error_message}: {e}")

        print(f"notification {error_message}: {counter}/{len(users)}")

    # Розсилка адмінам про те що домени закінчилися
    async def domain_havnt_admins(self, bot: Bot, i18n: I18nContext):
        message = i18n.ADMIN.NOTIFICATION.HAVENT_DOMAIN()
        users = [user['telegram_id'] for user in UserRepository().get_admins() if user['banned'] == 0]
        await self.__notify_list_text(bot, users, message, "domain havent")

    # Розсилка адмінам про те що у певної команди закінчився денний ліміт доменів
    async def daily_domains_limit_over(self, bot: Bot, i18n: I18nContext, team_name):
        message = i18n.ADMIN.NOTIFICATION.DOMAIN_LIMIT_WAS_OVER(team=team_name)
        users = [user['telegram_id'] for user in UserRepository().get_admins() if user['banned'] == 0]
        await self.__notify_list_text(bot, users, message, "domain limit over")

