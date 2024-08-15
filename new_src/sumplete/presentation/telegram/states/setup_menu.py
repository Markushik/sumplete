from aiogram.fsm.state import State, StatesGroup


class SetupMenu(StatesGroup):
    CONTROL = State()

    GENERATE = State()
    RANDOM = State()
    DAILY = State()
    SEARCH = State()
