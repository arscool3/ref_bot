import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.methods import send_message
from aiogram.types import Message, KeyboardButton, InlineKeyboardButton
from aiogram.utils.markdown import hbold
from pydantic_settings import BaseSettings


# Bot token can be obtained via https://t.me/BotFather

class BotSettings(BaseSettings):
    token: str

    class Config:
        env_prefix = "BOT_"


settings = BotSettings()
TOKEN = settings.token

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

refer_interface_start = InlineKeyboardButton(
    text='I want to be referral',
    callback_data='refer_interface_start'
)

candidate_interface_start = InlineKeyboardButton(
    text='I want to be candidate',
    callback_data='candidate_interface_start'
)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    markup = types.InlineKeyboardMarkup(inline_keyboard=[[refer_interface_start, candidate_interface_start]])
    await message.reply("Hi!\nChoose an option:", reply_markup=markup)


@dp.callback_query(F.data == 'I want to be referral')
async def refer_interface_handler(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.message.chat.id, 'test')



async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
