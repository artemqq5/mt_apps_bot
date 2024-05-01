from aiogram.fsm.state import StatesGroup, State


class EditCommentFlowState(StatesGroup):
    NewComment = State()
