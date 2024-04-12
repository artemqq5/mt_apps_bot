from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import L, I18nContext

from data.repository.PixelRepository import PixelRepository
from presenter.keyboards.user_keyboard import PixelDeleteKeyboard, kb_pixel_menu

router = Router()


@router.callback_query(PixelDeleteKeyboard.filter())
async def pixel_detail_handler(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    pixel_id = callback.data.split(":")[1]

    if not PixelRepository().delete_pixel(pixel_id):
        await callback.message.answer(i18n.USER.FAIL_DELETE_PIXEL(), reply_markup=kb_pixel_menu)
        return

    await callback.message.answer(i18n.USER.SUCCESS_DELETE_PIXEL(), reply_markup=kb_pixel_menu)
