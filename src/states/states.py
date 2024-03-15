from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


# Create your states here.

class RegistrationStateGroup(StatesGroup):
    waiting_for_role = State()
    waiting_for_password = State()


class ProfileSpecialist(StatesGroup):
    waiting_for_fio = State()
    waiting_for_grade = State()
    waiting_for_skills = State()

