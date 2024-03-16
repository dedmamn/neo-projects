from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.lexicon.lexicon_ru import LEXICON_RU

btn_specialist = InlineKeyboardButton(text=LEXICON_RU['btn_specialist'], callback_data='btn_specialist')
btn_customer = InlineKeyboardButton(text=LEXICON_RU['btn_customer'], callback_data='btn_customer')
start_keyboard = InlineKeyboardMarkup(inline_keyboard=[[btn_specialist], [btn_customer]])

