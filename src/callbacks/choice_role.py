from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from src.states.states import RegistrationStateGroup

router: Router = Router()


@router.callback_query(F.data == 'btn_specialist', StateFilter(RegistrationStateGroup.waiting_for_role.state))
async def specialist(callback: CallbackQuery):
    await callback.message.answer('специалист')


@router.callback_query(F.data == 'btn_customer', StateFilter(RegistrationStateGroup.waiting_for_role.state))
async def customer(callback: CallbackQuery):
    await callback.message.answer('заказчик')
