from doctest import SKIP

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext

from data.constants.access import MACROS
from data.repositoryDB.AccessRepository import AccessRepository
from data.repositoryDB.AppRepository import AppRepository
from data.repositoryDB.PixelRepository import PixelRepository
from data.repositoryKeitaro.KeitaroLinkRepository import KeitaroLinkRepository
from domain.states.user.flow_.CreateFlow import CreateFlowState
from presenter.keyboards._keyboard import kb_cancel, kb_skip
from presenter.keyboards.user_keyboard import AppCreateLinkKeyboard, pixel_choice_keyboard_list, \
    PixelChoiceKeyboardList, kb_create_pixelfb, kb_menu_user

router = Router()


@router.callback_query(AppCreateLinkKeyboard.filter())
async def create_link_handler(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    id_ = callback.data.split(":")[1]
    app = AppRepository().get_app_by_id(id_)
    pixels = PixelRepository().get_all_pixels(callback.from_user.id)
    if len(pixels) < 1:
        await callback.message.answer(i18n.FLOW.HAVENT_PIXEL_FB(), reply_markup=kb_create_pixelfb)
        return

    await state.set_state(CreateFlowState.ChoicePixelFB)
    await state.update_data(bundle=app['bundle'])
    await callback.message.answer(i18n.FLOW.SELECT_PIXEL_FB(), reply_markup=pixel_choice_keyboard_list(pixels))


@router.callback_query(PixelChoiceKeyboardList.filter(), CreateFlowState.ChoicePixelFB)
async def choice_pixel(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    id_ = callback.data.split(":")[1]
    pixel = PixelRepository().get_pixel(id_)
    await state.set_state(CreateFlowState.CommentFlow)
    await state.update_data(pixel=pixel['pixel_fb'])
    await state.update_data(token=pixel['token_fb'])
    await callback.message.answer(i18n.FLOW.COMMENT(), reply_markup=kb_skip)


@router.message(CreateFlowState.CommentFlow)
async def comment_flow(message: Message, i18n: I18nContext, state: FSMContext):
    if message.text == SKIP:
        await state.update_data(comment=SKIP)
    else:
        await state.update_data(comment=message.text)

    await state.set_state(CreateFlowState.LinkOffer)
    await message.answer(i18n.FLOW.OFFER_LINK(), reply_markup=kb_cancel)


@router.message(CreateFlowState.LinkOffer)
async def offer_link(message: Message, i18n: I18nContext, state: FSMContext):
    if not validate_user_link(message.text):
        await message.answer(i18n.FLOW.OFFER_LINK_ERROR(subid=MACROS), reply_markup=kb_cancel)
        return

    access = AccessRepository().get_access_by_user_id(message.from_user.id)

    await state.update_data(offer_link=message.text)
    data = await state.get_data()

    response = KeitaroLinkRepository().generate_link_keitaro(data, access)
    if not response:
        await state.clear()
        await message.answer(i18n.FLOW.FLOW_FAIL_CREATED(), reply_markup=kb_menu_user)
        return

    await message.answer(i18n.FLOW.FLOW_SUCCESS_CREATED(flow=response), reply_markup=kb_menu_user)
    await state.clear()


def validate_user_link(link: str) -> bool:
    return link.startswith("https://") and link.__contains__(MACROS)
