from aiogram import Bot
from aiogram_i18n import I18nContext

from data.repositoryDB.UserRepository import UserRepository

# CASES
DOAMIN_LIMIT = "DOMAIN_LIMIT"
DOAMIN_HAVNT = "DOMAIN_HAVNT"
NEW_USER = "NEW_USER"


class NotificationAdmin:
    @staticmethod  # Розсилка за списком (лише текст)
    async def __notify_list_text(bot: Bot, users, error_message, i18n, type_message, team_name=None, new_user=None):
        counter = 0

        for user in users:
            try:
                with i18n.use_locale(user['lang']):
                    if type_message == DOAMIN_LIMIT:
                        await bot.send_message(
                            chat_id=user['telegram_id'],
                            text=i18n.ADMIN.NOTIFICATION.DOMAIN_LIMIT_WAS_OVER(team=team_name)
                        )
                    elif type_message == DOAMIN_HAVNT:
                        await bot.send_message(
                            chat_id=user['telegram_id'],
                            text=i18n.ADMIN.NOTIFICATION.HAVENT_DOMAIN()
                        )
                    elif type_message == NEW_USER:
                        await bot.send_message(
                            chat_id=user['telegram_id'],
                            text=i18n.ADMIN.NOTIFICATION.NEW_USER(
                                username=f"@{new_user['username']}" if new_user['username'] else "none",
                                id=new_user['telegram_id'],
                                firstname=str(new_user['first_name']),
                                lastname=str(new_user['last_name']),
                                lang=new_user['lang'],
                                time=new_user['join_at']
                            )
                        )
                    else:
                        raise Exception
                counter += 1
            except Exception as e:
                print(f"{error_message}: {e}")

        print(f"notification {error_message}: {counter}/{len(users)}")

    # Розсилка адмінам про те що домени закінчилися
    async def domain_havnt_admins(self, bot: Bot, i18n: I18nContext):
        users = [user for user in UserRepository().get_admins() if user['banned'] == 0]
        await self.__notify_list_text(bot, users, "domain havent", i18n, DOAMIN_HAVNT)

    # Розсилка адмінам про те що у певної команди закінчився денний ліміт доменів
    async def daily_domains_limit_over(self, bot: Bot, i18n: I18nContext, team_name):
        users = [user for user in UserRepository().get_admins() if user['banned'] == 0]
        await self.__notify_list_text(bot, users, "domain limit over", i18n, DOAMIN_LIMIT, team_name)

    async def new_user_db(self, bot, i18n: I18nContext, user):
        users = [user for user in UserRepository().get_admins() if user['banned'] == 0]
        await self.__notify_list_text(bot, users, "new user", i18n, NEW_USER, new_user=user)
