from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hlink
from aiogram_i18n import L, I18nContext

from data.repository.AppRepository import AppRepository
from domain.states.admin.apps_.AddApplication import AddAplicationState
from presenter.keyboards._keyboard import kb_apps_platform, kb_cancel
from presenter.keyboards.admin_keyboard import kb_preview, kb_apps

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
    await state.update_data(bundle=message.text)
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
    await message.answer(i18n.APP.SET_SOURCE(), reply_markup=kb_cancel)


@router.message(AddAplicationState.Source)
async def add_desc(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(AddAplicationState.Desc)
    await state.update_data(source=message.text)
    await message.answer(i18n.APP.SET_DESC(), reply_markup=kb_cancel)


@router.message(AddAplicationState.Desc)
async def add_preview(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(AddAplicationState.PreView)
    await state.update_data(desc=message.text)
    data = await state.get_data()
    await message.answer_photo(photo=data['photo'], caption=preview_app(data, i18n))
    await message.answer(i18n.APP.PREVIEW(), reply_markup=kb_preview)


@router.message(AddAplicationState.PreView, F.text == L.PUBLUSH_APP())
async def add_publish(message: types.Message, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    if not AppRepository().add_app(
            name=data['name'], bundle=data['bundle'], image=data['photo'], geo=data['geo'],
            source=data['source'], platform=data['platform'], desc=data['desc']):
        await state.clear()
        await message.answer(i18n.APP.FAIL_PUBLISHED(), reply_markup=kb_apps)
        return

    await message.answer(i18n.APP.SUCCESS_PUBLISHED(), reply_markup=kb_apps)
    await state.clear()


@router.message(AddAplicationState.PreView, F.text == L.START_ADD_OVER())
async def add_start_over(message: types.Message, state: FSMContext, i18n: I18nContext):
    await state.set_state(AddAplicationState.Platform)
    await message.answer(i18n.APP.SET_PLATFORM(), reply_markup=kb_apps_platform)


def preview_app(data, i18n) -> str:
    if data['platform'] == i18n.IOS():
        name_url = hlink(data['name'], f"https://apps.apple.com/app/id{data['bundle']}")
    elif data['platform'] == i18n.ANDROID():
        name_url = hlink(data['name'], f"https://play.google.com/store/apps/details?id={data['bundle']}")
    else:
        name_url = data['name']

    return i18n.APP.DESC_TEMPLATE(
        name_url=name_url,
        platform=data['platform'],
        source=data['source'],
        geo=data['geo'],
        desc=data['desc']
    )
