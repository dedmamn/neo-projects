from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.lexicon.lexicon_ru import LEXICON_RU

keyboard = [
    [InlineKeyboardButton(text=LEXICON_RU['btn_jun'], callback_data='btn_jun')],
    [InlineKeyboardButton(text=LEXICON_RU['btn_jun_plus'], callback_data='btn_jun_plus')],
    [InlineKeyboardButton(text=LEXICON_RU['btn_middle_minus'], callback_data='btn_middle_minus')],
    [InlineKeyboardButton(text=LEXICON_RU['btn_middle'], callback_data='btn_middle')],
    [InlineKeyboardButton(text=LEXICON_RU['btn_middle_plus'], callback_data='btn_middle_plus')],
    [InlineKeyboardButton(text=LEXICON_RU['btn_senior'], callback_data='btn_senior')]
]

grade_keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)

