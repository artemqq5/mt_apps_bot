from datetime import datetime
from doctest import SKIP

from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext

from data.constants.access import MACROS, validate_user_link
from data.repositoryDB.AccessRepository import AccessRepository
from data.repositoryDB.AppRepository import AppRepository
from data.repositoryDB.DomainRepository import DomainRepository
from data.repositoryDB.FlowRepository import FlowRepository
from data.repositoryDB.PixelRepository import PixelRepository
from data.repositoryDB.TeamRepository import TeamRepository
from data.repositoryKeitaro.KeitaroLinkRepository import KeitaroLink
from data.repositoryKeitaro.usecase.KeitaroDomainUseCase import KeitaroDomainUseCase
from domain.notify.NotificationAdmin import NotificationAdmin
from domain.states.user.flow_.CreateFlow import CreateFlowState
from presenter.keyboards._keyboard import kb_cancel, kb_skip
from presenter.keyboards.user_keyboard import AppCreateLinkKeyboard, pixel_choice_keyboard_list, \
    PixelChoiceKeyboardList, kb_create_pixelfb, kb_menu_user, kb_call_admin

router = Router()


@router.callback_query(AppCreateLinkKeyboard.filter())
async def create_link_handler(callback: CallbackQuery, bot: Bot, i18n: I18nContext, state: FSMContext):
    # update domains from keitaro
    KeitaroDomainUseCase().domains_update_db()

    id_ = callback.data.split(":")[1]
    app = AppRepository().get_app_by_id_for_users(id_)

    if not app:
        return  # додаток не доступний

    pixels = PixelRepository().get_all_pixels(callback.from_user.id)
    if len(pixels) < 1:
        await callback.message.answer(i18n.FLOW.HAVENT_PIXEL_FB(), reply_markup=kb_create_pixelfb)
        return

    team_id = AccessRepository().get_access_by_user_id(callback.from_user.id)['team_id']
    team = TeamRepository().get_team_by_id(team_id)
    limit = DomainRepository().check_domain_limit(team_id)
    if limit['COUNT(*)'] >= team['limit']:
        await callback.message.answer(i18n.FLOW.DOMAIN_LIMIT_OVER(limit=limit['COUNT(*)']), reply_markup=kb_call_admin)
        await NotificationAdmin().daily_domains_limit_over(bot, i18n, team['team_name'])
        return

    if not DomainRepository().check_free_domain():
        await callback.message.answer(i18n.FLOW.HAVNT_FREE_DOMAINS(), reply_markup=kb_menu_user)
        await NotificationAdmin().domain_havnt_admins(bot, i18n)
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
    if message.text != i18n.SKIP():
        await state.update_data(comment=message.text)

    await state.set_state(CreateFlowState.LinkOffer)
    await message.answer(i18n.FLOW.OFFER_LINK(), reply_markup=kb_cancel)


@router.message(CreateFlowState.LinkOffer)
async def offer_link(message: Message, i18n: I18nContext, state: FSMContext, bot: Bot):
    # Валідуємо лінку від юзера
    if not validate_user_link(message.text):
        await message.answer(i18n.FLOW.OFFER_LINK_ERROR(subid=MACROS), reply_markup=kb_cancel)
        return

    access = AccessRepository().get_access_by_user_id(message.from_user.id)
    team = TeamRepository().get_team_by_id(access['team_id'])
    limit = DomainRepository().check_domain_limit(access['team_id'])

    # Перевіряємо поточні ліміти команди
    if limit['COUNT(*)'] >= team['limit']:
        await message.answer(i18n.FLOW.DOMAIN_LIMIT_OVER(limit=limit['COUNT(*)']), reply_markup=kb_call_admin)
        await NotificationAdmin().daily_domains_limit_over(bot, i18n, team['team_name'])
        return

    domain = DomainRepository().check_free_domain()

    # Перевіряємо наявність вільного невикористаного домену
    if not domain:
        await state.clear()
        await message.answer(i18n.FLOW.HAVNT_FREE_DOMAINS(), reply_markup=kb_menu_user)
        await NotificationAdmin().domain_havnt_admins(bot, i18n)
        return

    await state.update_data(offer_link=message.text)
    await state.update_data(domain_id=domain['domain_id'])
    await state.update_data(domain=domain['domain'])
    data = await state.get_data()

    team_unq = ''.join(filter(str.isalnum, access['team_name'].lower()))
    response = KeitaroLink().generate_link_keitaro(data, access, team_unq)

    # Створюємо кампанії та оффер для заливу
    if not response:
        await state.clear()
        await message.answer(i18n.FLOW.FLOW_FAIL_CREATED(error="kt"), reply_markup=kb_menu_user)
        return

    # Резервуємо домен в бд
    if not DomainRepository().reserve_domain(domain['domain'], access['team_id'], access['user_id'],
                                             access['team_name'], datetime.now()):
        await state.clear()
        await message.answer(i18n.FLOW.FLOW_FAIL_CREATED(error="domain"), reply_markup=kb_menu_user)
        return

    # Додаємо потік в бд
    if not FlowRepository().add_flow(
            link_user=response.link_user,
            link_keitaro=response.link_keitaro,
            user_id=response.user_id,
            pixel=response.pixel,
            token=response.token,
            client_campain_id=response.client_campain_id,
            client_campaign_name=response.client_campaign_name,
            distribution_campaign_id=response.distribution_campaign_id,
            distribution_campaign_name=response.distribution_campaign_name,
            offer_id=response.offer_id,
            offer_name=response.offer_name,
            domain=response.domain,
            bundle=response.bundle,
            comment=response.comment,
            client_alias=response.alias_client_cmp,
            distribution_alias=response.distribution_campaign_alias
    ):
        await state.clear()
        await message.answer(i18n.FLOW.FLOW_FAIL_CREATED(error="db"), reply_markup=kb_menu_user)
        return

    await message.answer(i18n.FLOW.FLOW_SUCCESS_CREATED(flow=response.link_keitaro), reply_markup=kb_menu_user)
    await state.clear()



