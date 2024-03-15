from aiogram import Router
import hashlib
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.lexicon.lexicon_ru import LEXICON_RU
from src.states.states import RegistrationStateGroup

router: Router = Router()


@router.message(StateFilter(RegistrationStateGroup.waiting_for_password.state))
async def get_password(message: Message, state: FSMContext):
    password_hash = hashlib.new('sha256')
    password_hash.update(message.text.encode())
    print(password_hash.hexdigest())

    data = await state.get_data()
    print(data['role'])
    print(message.from_user.id)
    # TODO: Тут функция которая отправляет данные пользователя в БД
    await message.answer(LEXICON_RU['user_reg_success'])
