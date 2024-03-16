from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from src.lexicon.lexicon_ru import LEXICON_RU
from src.states.states import ProfileSpecialist

router: Router = Router()


@router.callback_query(StateFilter(ProfileSpecialist.waiting_for_grade.state))
async def get_grade(callback: CallbackQuery, state: FSMContext):
    grade = LEXICON_RU[callback.data]
    await state.set_data({'grade': grade})
    await callback.message.answer(LEXICON_RU['msg_write_skills'])
    await state.set_state(ProfileSpecialist.waiting_for_skills.state)


@router.callback_query(StateFilter(ProfileSpecialist.waiting_for_skills.state))
async def get_skills(callback: CallbackQuery, state: FSMContext):
    pass
