from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.repositoryDB.FlowRepository import FlowRepository
from presenter.keyboards.user_keyboard import EditFlowApp

router = Router()


@router.callback_query(EditFlowApp.filter())
async def edit_flow_app(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    id_ = callback.data.split(":")[1]
    flow = FlowRepository().get_flow(id_)

    if not flow:
        return  # потока не існує

    await callback.answer("Не реалізовано поки")

