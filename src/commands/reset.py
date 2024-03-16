from aiogram import Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, any_state, default_state
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from src.commands.start import start_command
from src.keyboards.command_keyboards import start_keyboard
from src.lexicon.lexicon_ru import LEXICON_RU
from src.states.states import RegistrationStateGroup

router: Router = Router()


@router.message(Command('reset'), StateFilter(any_state))
async def reset_command(message: Message, state: FSMContext):
    await state.set_state(default_state)
    await state.clear()
    await start_command(message, state)
