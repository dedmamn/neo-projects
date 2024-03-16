from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.states.states import SpecialistStateGroup, CustomerStateGroup

router: Router = Router()


@router.message(Command('profile'), StateFilter(SpecialistStateGroup.default.state))
async def profile_command(message: Message, state: FSMContext):
    data = await state.get_data()
    msg = f"""
Роль: {data.get('role')}
ФИО: {data.get('fio')}
Телеграмм ID: {message.from_user.id}
Хеш пароля: {data.get('password')}
Уровень: {data.get('grade')}
Специальность: {data.get('clean_skills')}    
            """

    await message.answer(msg)


@router.message(Command('profile'), StateFilter(CustomerStateGroup.default.state))
async def profile_command(message: Message, state: FSMContext):
    data = await state.get_data()
    msg = f"""
Роль: {data.get('role')}
Название компании: {data.get('company_name')}
ФИО контактного лица: {data.get('fio')}
Телеграмм ID: {message.from_user.id}
Хеш пароля: {data.get('password')}  
            """
    await message.answer(msg)
