from aiogram import Router
import hashlib
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.keyboards.specialist_reg_keyboards import grade_keyboard
from src.lexicon.lexicon_ru import LEXICON_RU
from src.states.states import RegistrationStateGroup, ProfileCustomer, ProfileSpecialist, CustomerStateGroup

router: Router = Router()


# TODO: Работа с БД
async def save_user(data):
    pass


async def save_specialist(data):
    pass


async def save_customer(data):
    pass


@router.message(StateFilter(RegistrationStateGroup.waiting_for_password.state))
async def get_password(message: Message, state: FSMContext):
    password_hash = hashlib.new('sha256')
    password_hash.update(message.text.encode())
    user_data = await state.get_data()
    await state.set_data({**user_data, 'password': password_hash.hexdigest()})
    await message.delete()
    await message.answer(LEXICON_RU['msg_fio_waiting'])
    await state.set_state(RegistrationStateGroup.waiting_for_fio.state)


@router.message(StateFilter(RegistrationStateGroup.waiting_for_fio.state))
async def get_fio(message: Message, state: FSMContext):
    fio = message.text.split()
    user_data = await state.get_data()
    await state.set_data({**user_data, 'fio': fio})
    await message.answer(LEXICON_RU['user_reg_success'])
    await message.answer(LEXICON_RU['profile_filling'])
    if user_data['role'] == 'customer':
        await state.set_state(ProfileCustomer.waiting_for_company_name.state)
        await message.answer(LEXICON_RU['msg_company_name_waiting'])
    elif user_data['role'] == 'specialist':
        await state.set_state(ProfileSpecialist.waiting_for_grade.state)
        await message.answer(LEXICON_RU['msg_choice_grade'], reply_markup=grade_keyboard)
    else:
        await message.answer(LEXICON_RU['im_broken'])


# Регистрация компании
@router.message(StateFilter(ProfileCustomer.waiting_for_company_name.state))
async def get_company_name(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await state.set_data({**user_data, 'company_name': message.text})
    await message.answer(LEXICON_RU['msg_end_profile_edit'])
    await state.set_state(CustomerStateGroup.default.state)




