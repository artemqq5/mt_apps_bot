from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import L, I18nContext

from data.repositoryDB.PixelRepository import PixelRepository
from presenter.keyboards.user_keyboard import kb_pixel_menu, pixel_keyboard_list, PixelKeyboardList, kb_delte_pixel

router = Router()


@router.message(L.USER.SHOW_MY_PIXELS())
async def show_pixel_list(message: Message, i18n: I18nContext, state: FSMContext):
    pixels = PixelRepository().get_all_pixels(message.from_user.id)

    if not pixels:
        await message.answer(i18n.USER.HAVENT_ANY_PIXEL(), reply_markup=kb_pixel_menu)
        return

    await message.answer(i18n.USER.YOUR_PIXELS(), reply_markup=pixel_keyboard_list(pixels))


@router.callback_query(PixelKeyboardList.filter())
async def pixel_detail_handler(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    _id = callback.data.split(":")[1]
    pixel = PixelRepository().get_pixel(_id)

    if not pixel:
        return

    await callback.message.answer(
        i18n.USER.PIXEL_INFO(
            pixel_id=pixel['pixel_fb'],
            token=pixel['token_fb'],
            date=pixel['created_at']
        ),
        reply_markup=kb_delte_pixel(_id)
    )





