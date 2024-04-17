from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hlink
from aiogram_i18n import L, I18nContext

from data.KeitaroRepository import KeitaroRepository
from presenter.keyboards.user_keyboard import AppCreateLinkKeyboard

router = Router()


# response = KeitaroRepository().clone_campaign("test campaign for rent bot", "test_alias_1212")
# # Перевірка результату
# if response.status_code == 200:
#     print("Кампанія успішно створена")
#     print(response.json())  # Виведення деталей створеної кампанії
# else:
#     print(f"Помилка створення кампанії: {response.status_code}")
#     print(response.text)  # Виведення тексту помилки

@router.callback_query(AppCreateLinkKeyboard.filter())
async def create_link_handler(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    app_id = callback.data.split(":")[1]


    await callback.message.answer(i18n.FLOW.SELECT_PIXEL_FB, reply_markup=)


