from aiogram import Router
import hashlib
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.lexicon.lexicon_ru import LEXICON_RU
from src.states.states import RegistrationStateGroup, ProfileCustomer, ProfileSpecialist

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
    data = await state.get_data()
    data['password'] = password_hash.hexdigest()
    await message.delete()
    await message.answer(LEXICON_RU['msg_fio_waiting'])
    await state.set_state(RegistrationStateGroup.waiting_for_fio.state)


@router.message(StateFilter(RegistrationStateGroup.waiting_for_fio.state))
async def get_fio(message: Message, state: FSMContext):
    fio = message.text.split()
    data = await state.get_data()
    data['userId'] = message.from_user.id
    data['fio'] = fio
    await save_user(data)
    await message.answer(LEXICON_RU['user_reg_success'])
    await message.answer(LEXICON_RU['profile_filling'])
    if data['role'] == 'customer':
        await state.set_state(ProfileCustomer.waiting_for_company_name.state)
        await message.answer(LEXICON_RU['msg_company_name_waiting'])
    elif data['role'] == 'specialist':
        await state.set_state(ProfileSpecialist.waiting_for_grade.state)
        await message.answer(LEXICON_RU['msg_choice_grade'])
    else:
        await message.answer(LEXICON_RU['im_broken'])

# # Регистрация компании
# @router.message(StateFilter(ProfileCustomer.waiting_for_fio.state))
# async def customer_fio_wait(message: Message, state: FSMContext):
#     fio = message.text.split()
#     await state.set_data({'fio': fio})
#     await message.answer(LEXICON_RU['msg_company_name_waiting'])
#     await state.set_state(ProfileCustomer.waiting_for_company_name.state)
#
#
# @router.message(StateFilter(ProfileCustomer.waiting_for_company_name.state))
# async def company_name_wait(message: Message, state: FSMContext):
#     await state.set_data({'company_name': message.text})
#     await message.answer(LEXICON_RU['msg_end_profile_edit'])
#
#
# # Регистрация специалиста
# @router.message(StateFilter(ProfileSpecialist.waiting_for_grade.state))
# async def specialist_grade_answer(message: Message, state: FSMContext):
#     await state.set_data({'company_name': message.text})
#     await message.answer(LEXICON_RU[''])
#     await state.set_state(ProfileCustomer.waiting_for_company_name.state)
