from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from src.lexicon.lexicon_ru import LEXICON_RU
from src.states.states import RegistrationStateGroup

router: Router = Router()


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    btn_specialist = InlineKeyboardButton(text=LEXICON_RU['btn_specialist'], callback_data='btn_specialist')
    btn_customer = InlineKeyboardButton(text=LEXICON_RU['btn_customer'], callback_data='btn_customer')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[btn_specialist], [btn_customer]])
    await message.answer(LEXICON_RU['/start'], reply_markup=keyboard)
    await state.set_state(RegistrationStateGroup.waiting_for_role)
