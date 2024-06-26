from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.constants.access import BANNED_APP_STATUS, ACTIVE_APP_STATUS
from data.repositoryDB.AppRepository import AppRepository
from data.repositoryDB.FlowRepository import FlowRepository
from domain.routers.user.sub_routers.flows import edit_app_, edit_comment_, edit_offer_, edit_pixel_
from presenter.keyboards.user_keyboard import FlowShowKeyboard, kb_flow_edit

router = Router()
router.include_routers(
    edit_app_.router,
    edit_comment_.router,
    edit_offer_.router,
    edit_pixel_.router,
)


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

    link_ = flow['link_user'].split("&team")

    await callback.message.answer(
        i18n.FLOW.DETAIL_FLOW(
            link_keitaro=flow['link_keitaro'],
            id=flow['id'],
            app_name=app['name'],
            platform=app['platform'],
            source=app['source'],
            status=status,
            domain=flow['domain'],
            link_user=link_[0],
            pixel=flow['pixel_fb'],
            token=flow['token_fb'],
            date=flow['created_at'],
            geo=app['geo'],
            comment=str(flow['comment'])
        ),
        reply_markup=kb_flow_edit(id_)
    )
