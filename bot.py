import logging

from aiogram import Bot, Dispatcher, executor, types

import api
import conf

from markups import cat_markup, cat_help_markup

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


async def send_cat(message: types.Message, markup, reply=False):
    try:
        cat_url = api.get_cat()
        if not reply:
            await bot.send_photo(message.chat.id, cat_url,
                                 reply_markup=markup)
        else:
            await bot.send_photo(message.chat.id, cat_url, reply_to_message_id=message.message_id,
                                 reply_markup=markup)
    except Exception as e:

        msg = messages["error"] + f'\nerror_msg = {e}'
        if not reply:
            await bot.send_message(message.chat.id, msg,
                                   reply_markup=markup)
        else:
            await bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id,
                                   reply_markup=markup)


@dp.message_handler(content_types=["text"], chat_type=["private"])
async def cat(message: types.Message):
    if message.text not in ['/randcat', '/cat', '/loaf']:
        return
    await send_cat(message, markup=cat_help_markup, reply=False)


@dp.message_handler(content_types=["text"], chat_type=["group", "supergroup"], commands=['randcat', 'cat', 'loaf'])
async def chat_cat(message: types.Message):
    await send_cat(message, markup=cat_markup, reply=True)


@dp.message_handler(content_types=["text"], chat_type=["group", "supergroup"])
async def chat_cat_trigger(message: types.Message):
    if message.text not in ['кот', 'коть', 'cat', 'loaf', 'булка', 'буханка', 'буханочка', 'хлебушек']:
        return
    await send_cat(message, markup=cat_markup, reply=False)
