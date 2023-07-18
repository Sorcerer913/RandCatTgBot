from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

_start_btn = KeyboardButton('/start')
_help_btn = KeyboardButton('/help')
_cat_btn = KeyboardButton('/cat')

start_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(_start_btn)
cat_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(_cat_btn)
cat_help_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(_cat_btn).add(_help_btn)
