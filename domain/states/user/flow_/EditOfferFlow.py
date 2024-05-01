from aiogram.fsm.state import StatesGroup, State


class EditOfferFlowState(StatesGroup):
    NewOffer = State()
