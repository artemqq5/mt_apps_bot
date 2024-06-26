from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hlink
from aiogram_i18n import L, I18nContext

from data.constants.access import MASONS_LINK, DEFAULT_DESC
from data.repositoryDB.AppRepository import AppRepository
from data.repositoryKeitaro.KeitaroAppRepository import KeitaroAppRepository
from domain.states.admin.apps_.AddApplication import AddAplicationState
from presenter.keyboards._keyboard import kb_apps_platform, kb_cancel, kb_skip
from presenter.keyboards.admin_keyboard import kb_preview, kb_apps, kb_source

router = Router()


@router.message(F.text == L.ADD_APP())
async def add_platform(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(AddAplicationState.Platform)
    await message.answer(i18n.APP.SET_PLATFORM(), reply_markup=kb_apps_platform)


@router.message(AddAplicationState.Platform, F.text.in_((L.IOS(),)))  # L.ANDROID(), L.PWA()
async def add_name(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(AddAplicationState.Name)
    await state.update_data(platform=message.text)
    await message.answer(i18n.APP.SET_NAME(), reply_markup=kb_cancel)


@router.message(AddAplicationState.Name)
async def add_bundle(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(AddAplicationState.Bundle)
    await state.update_data(name=message.text)
    await message.answer(i18n.APP.SET_BUNDLE(), reply_markup=kb_cancel)


@router.message(AddAplicationState.Bundle)
async def add_image(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(AddAplicationState.Image)
    data = await state.get_data()
    sub_name = ''.join(filter(str.isalnum, data['name'].lower()))
    await state.update_data(bundle=f"{message.text}{sub_name}")
    await state.update_data(url=generate_url(message.text, data['platform'], i18n))
    await message.answer(i18n.APP.SET_IMAGE(), reply_markup=kb_cancel)


@router.message(AddAplicationState.Image, F.photo)
async def add_geo(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(AddAplicationState.Geo)
    await state.update_data(photo=message.photo[-1].file_id)
    await message.answer(i18n.APP.SET_GEO(), reply_markup=kb_cancel)


@router.message(AddAplicationState.Geo)
async def add_source(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(AddAplicationState.Source)
    await state.update_data(geo=message.text)
    await message.answer(i18n.APP.SET_SOURCE(), reply_markup=kb_source)


@router.message(AddAplicationState.Source, F.text.in_((MASONS_LINK,)))
async def add_desc(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(AddAplicationState.Desc)
    await state.update_data(source=message.text)
    await message.answer(i18n.APP.SET_DESC(), reply_markup=kb_skip)


@router.message(AddAplicationState.Desc)
async def add_preview(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(AddAplicationState.PreView)
    await state.update_data(desc=message.text)
    if message.text == i18n.SKIP():
        await state.update_data(desc=DEFAULT_DESC)

    data = await state.get_data()
    await message.answer_photo(photo=data['photo'], caption=preview_app(data, i18n))
    await message.answer(i18n.APP.PREVIEW(), reply_markup=kb_preview)


@router.message(AddAplicationState.PreView, F.text == L.PUBLUSH_APP())
async def add_publish(message: types.Message, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()

    if AppRepository().get_app_by_bundle_keitaro_for_users(bundle=data['bundle']):
        await state.clear()
        await message.answer(i18n.APP.ALREADY_ADDED(), reply_markup=kb_apps)
        return

    response = KeitaroAppRepository().upload_app_keitaro(
        flow_url=data['url'], flow_name=data['name'], bundle=data['bundle'], app_name=data['name']
    )
    if not response:
        await state.clear()
        await message.answer(i18n.APP.FAIL_PUBLISHED(error="Keitaro"), reply_markup=kb_apps)
        return

    if not AppRepository().add_app(
            keitaro_id=response.flow_app_id, name=data['name'], url=data['url'], bundle=data['bundle'],
            image=data['photo'], geo=data['geo'], source=data['source'], platform=data['platform'],
            desc=data['desc'], organic_campaign_id=response.organic_campaign_id,
            organic_campaign_name=response.organic_campaign_name
    ):
        await state.clear()
        await message.answer(i18n.APP.FAIL_PUBLISHED(error="DataBase"), reply_markup=kb_apps)
        return

    await message.answer(i18n.APP.SUCCESS_PUBLISHED(
        masons=f"https://masonsapps.tech/v2?name={data['bundle']}",
        id=response.organic_campaign_id,
        name=response.organic_campaign_name,
        link=response.link_keitaro
    ), reply_markup=kb_apps)
    await state.clear()


@router.message(AddAplicationState.PreView, F.text == L.START_ADD_OVER())
async def add_start_over(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(AddAplicationState.Platform)
    await message.answer(i18n.APP.SET_PLATFORM(), reply_markup=kb_apps_platform)


def preview_app(data, i18n) -> str:
    return i18n.USER.DESC_TEMPLATE(
        name_url=hlink(data['name'], data['url']),
        platform=data['platform'],
        source=data['source'],
        geo=data['geo'],
        desc=(i18n.APP.DEFAULT_DESC() if data['desc'] == DEFAULT_DESC else data['desc'])
    )


def generate_url(bundle, platform, i18n) -> str | None:
    if platform == i18n.IOS():
        return f"https://apps.apple.com/app/id{bundle}"
    elif platform == i18n.ANDROID():
        return f"https://play.google.com/store/apps/details?id={bundle}"
    else:
        return None
