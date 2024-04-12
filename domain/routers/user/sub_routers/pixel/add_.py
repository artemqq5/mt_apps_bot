from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram_i18n import L, I18nContext

from data.repository.PixelRepository import PixelRepository
from domain.states.user.pixel_.AddPixelFB import AddPixelFBState
from presenter.keyboards._keyboard import kb_cancel
from presenter.keyboards.user_keyboard import kb_pixel_menu

router = Router()


@router.message(F.text == L.USER.ADD_PIXEL_FB())
async def pixel_id(message: types.Message, i18n: I18nContext, state: FSMContext):
    await state.set_state(AddPixelFBState.PixelId)
    await message.answer(i18n.USER.ADD_PIXEL_ID(), reply_markup=kb_cancel)


@router.message(AddPixelFBState.PixelId)
async def token(message: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(pixel_id=message.text)
    await state.set_state(AddPixelFBState.TokenEAAG)
    await message.answer(i18n.USER.ADD_TOKEN_EAAG(), reply_markup=kb_cancel)


@router.message(AddPixelFBState.TokenEAAG)
async def add_pixel_fb(message: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(token=message.text)
    data = await state.get_data()

    if not PixelRepository().add_pixel(data['pixel_id'], data['token'], message.from_user.id):
        await message.answer(i18n.USER.FAIL_ADD_PIXEL(), reply_markup=kb_pixel_menu)
        await state.clear()
        return

    await message.answer(i18n.USER.SUCCESS_ADD_PIXEL(), reply_markup=kb_pixel_menu)
    await state.clear()

