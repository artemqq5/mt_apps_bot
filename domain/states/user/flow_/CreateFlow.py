from aiogram.fsm.state import StatesGroup, State


class CreateFlowState(StatesGroup):
    ChoicePixelFB = State()
    CommentFlow = State()
    LinkOffer = State()
