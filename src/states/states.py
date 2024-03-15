from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


# Create your states here.

class RegistrationStateGroup(StatesGroup):
    waiting_for_role = State()
    waiting_for_password = State()
    waiting_for_fio = State()


class ProfileSpecialist(StatesGroup):
    waiting_for_grade = State()
    waiting_for_skills = State()


class ProfileCustomer(StatesGroup):
    waiting_for_company_name = State()


class CustomerStateGroup(StatesGroup):
    pass


class SpecialistStateGroup(StatesGroup):
    pass
