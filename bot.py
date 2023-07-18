import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import BoundFilter

import api
import conf

from markups import start_markup, cat_markup, cat_help_markup

API_TOKEN = conf.TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def start_bot():
    executor.start_polling(dp, skip_updates=True)


messages = {
    "help": "Hello I'm random cat bot.\n"
            "I can send random cat if you want!\n"
            "Meow! =^..^=",
    "error": "cannot reach data from The Cat Api"
}


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    msg = messages["help"]

    await bot.send_message(chat_id=message.chat.id, text=msg, reply_markup=cat_help_markup)


@dp.message_handler(commands=['randcat', 'cat'])
async def cat(message: types.Message):
    try:
        cat_url = api.get_cat()
        await bot.send_photo(message.chat.id, cat_url,
                             reply_markup=cat_help_markup)
    except Exception as e:

        msg = messages["error"] + f'\nerror_msg = {e}'
        await bot.send_message(message.chat.id, msg,
                               reply_markup=cat_help_markup)


# filter.py
class IsGroup(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPER_GROUP,
        )


@dp.message_handler(IsGroup(), commands=['randcat', 'cat', 'loaf'])
async def chat_cat(message: types.Message):
    try:
        cat_url = api.get_cat()
        await bot.send_photo(message.chat.id, cat_url, reply_to_message_id=message.message_id,
                             reply_markup=cat_markup)
    except Exception as e:

        msg = messages["error"] + f'\nerror_msg = {e}'
        await bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id,
                               reply_markup=cat_markup)


@dp.message_handler(
    lambda message: IsGroup() and (message.text in ['кот', 'коть', 'cat', 'loaf', 'булка', 'буханка', 'буханочка']))
async def chat_cat_trigger(message: types.Message):
    try:
        cat_url = api.get_cat()
        await bot.send_photo(message.chat.id, cat_url, reply_to_message_id=message.message_id,
                             reply_markup=cat_markup)
    except Exception as e:

        msg = messages["error"] + f'\nerror_msg = {e}'
        await bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id,
                               reply_markup=cat_markup)
