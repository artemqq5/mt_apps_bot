from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.constants.access import BANNED_APP_STATUS, ACTIVE_APP_STATUS
from data.repositoryDB.AppRepository import AppRepository
from data.repositoryDB.FlowRepository import FlowRepository
from presenter.keyboards.user_keyboard import FlowShowKeyboard, kb_flow_edit

router = Router()


@router.callback_query(FlowShowKeyboard.filter())
async def show_flow_detail(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    # KeitaroAppUseCase().check_available_apps()  # Перевіряємо чи не видалили з кейтаро додаток

    id_ = callback.data.split(":")[1]
    flow = FlowRepository().get_flow(id_)

    if not flow:
        return  # потока не існує

    app = AppRepository().get_app_by_bundle_keitaro_for_users(flow['bundle'])

    if app['visibility'] == 0 or app['status'] == BANNED_APP_STATUS:
        status = f"{BANNED_APP_STATUS} ❌"
    else:
        status = f"{ACTIVE_APP_STATUS} ✅"

    await callback.message.answer(
        i18n.FLOW.DETAIL_FLOW(
            link_keitaro=flow['link_keitaro'],
            id=flow['id'],
            app_name=app['name'],
            platform=app['platform'],
            source=app['source'],
            status=status,
            domain=flow['domain'],
            link_user=flow['link_user'],
            pixel=flow['pixel_fb'],
            token=flow['token_fb'],
            date=flow['created_at'],
            geo=app['geo']
        ),
        reply_markup=kb_flow_edit(id_)
    )
