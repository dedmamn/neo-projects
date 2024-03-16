from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from src.lexicon.lexicon_ru import LEXICON_RU
from src.states.states import RegistrationStateGroup

router: Router = Router()


@router.callback_query(F.data == 'btn_specialist', StateFilter(RegistrationStateGroup.waiting_for_role.state))
async def specialist(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    await callback.message.answer(LEXICON_RU['msg_write_password'])
    await state.set_data({**user_data, 'role': 'specialist'})
    await state.set_state(RegistrationStateGroup.waiting_for_password)


@router.callback_query(F.data == 'btn_customer', StateFilter(RegistrationStateGroup.waiting_for_role.state))
async def customer(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    await callback.message.answer(LEXICON_RU['msg_write_password'])
    await state.set_data({**user_data, 'role': 'customer'})
    await state.set_state(RegistrationStateGroup.waiting_for_password)
