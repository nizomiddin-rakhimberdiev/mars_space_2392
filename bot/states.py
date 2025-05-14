from aiogram.fsm.state import  State, StatesGroup

class RegisterStates(StatesGroup):
    space_id = State()