from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from src.keyboards.command_keyboards import start_keyboard
from src.lexicon.lexicon_ru import LEXICON_RU
from src.states.states import RegistrationStateGroup

router: Router = Router()



@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await message.answer(LEXICON_RU['/start'], reply_markup=start_keyboard)
    await state.set_state(RegistrationStateGroup.waiting_for_role)
