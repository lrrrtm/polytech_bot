#!/usr/bin/env python3

import logging

# import asyncio
from aiogram import Bot, Dispatcher, executor, types

# import uvloop
# import sys

import schedule

import config

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.key)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("оригинальное приветствие")


@dp.message_handler(commands=["schedule"])
async def send_welcome(message: types.Message):
    await message.reply(
        await schedule.get_shedule(36243), parse_mode=types.message.ParseMode.MARKDOWN
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
