from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext

from src.lexicon.lexicon_ru import LEXICON_RU
from src.states.states import ProfileSpecialist, SpecialistStateGroup

router: Router = Router()


@router.callback_query(StateFilter(ProfileSpecialist.waiting_for_grade.state))
async def get_grade(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    grade = LEXICON_RU[callback.data]
    await state.set_data({**user_data,'grade': grade})
    keyboard = await update_skills_keyboard(state)
    await callback.message.answer(LEXICON_RU['msg_write_skills'], reply_markup=keyboard)
    await state.set_state(ProfileSpecialist.waiting_for_skills.state)


button_texts = {
    "btn_backend": "Backend ⚙️",
    "btn_frontend": "Frontend 👨🏻‍💻",
    "btn_designer": "Designer 🖌",
    "btn_analyst": "Аналитик 📊",
    "btn_security": "Безопасник 🛡",
}


async def update_skills_keyboard(state: FSMContext) -> InlineKeyboardMarkup:
    user_data = await state.get_data()
    selected_skills = user_data.get("selected_skills", [])

    buttons = []
    for key, text in button_texts.items():
        # Добавление галочки к выбранным кнопкам
        display_text = f"✅ {text}" if key in selected_skills else text
        buttons.append([InlineKeyboardButton(text=display_text, callback_data=key)])
    buttons.append([InlineKeyboardButton(text="Готово", callback_data='skills_approve')])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


@router.callback_query(F.data == 'skills_approve', StateFilter(ProfileSpecialist.waiting_for_skills.state))
async def save_skills(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    clean_skills_array = [skill.replace('btn_', '') for skill in user_data.get('selected_skills')]
    await state.set_data({**user_data, 'clean_skills': clean_skills_array})
    await callback.message.answer(LEXICON_RU['edit_profile_end'])
    await state.set_state(SpecialistStateGroup.default.state)


@router.callback_query(StateFilter(ProfileSpecialist.waiting_for_skills.state))
async def get_skills(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    selected_skills = user_data.get("selected_skills", [])

    # Добавление или удаление навыка из списка
    if callback.data in selected_skills:
        selected_skills.remove(callback.data)
    else:
        selected_skills.append(callback.data)

    await state.set_data({**user_data, "selected_skills": selected_skills})

    # Обновление клавиатуры
    keyboard = await update_skills_keyboard(state)
    await callback.message.edit_reply_markup(reply_markup=keyboard)
