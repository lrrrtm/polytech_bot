#!/usr/bin/env python3

import logging

# import asyncio
from aiogram import Bot, Dispatcher, executor, types, md
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

# import uvloop
# import sys

import re
import schedule
import config
import sqlite3

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize bot, dispatcher and sqlite connection
storage = MemoryStorage()
bot = Bot(token=config.key)
dp = Dispatcher(bot, storage=storage)
db_con = sqlite3.connect(config.db_path)
cur = db_con.cursor()

# Create db table if not exists
res = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
if not res.fetchone():
    cur.execute("CREATE TABLE users(id, name, gid, lang)")

# Class for gid form
class Form(StatesGroup):
    gid = State()


# Easter eggs
@dp.message_handler(text="мяу")
async def send_mur(message: types.Message):
    await message.reply("мур")


@dp.message_handler(text="мур")
async def send_mur(message: types.Message):
    await message.reply("мяу")


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    """Greet user and prompt for gid"""
    await Form.gid.set()
    await message.reply(
        "зайди на ruz.spbstu.ru выбери свою граппу и скинь мне ссылку\n"
        "типа https://ruz.spbstu.ru/faculty/123/groups/36243"
    )


@dp.message_handler(state="*", commands=["cancel"])
async def cancel_handler(message: types.Message, state: FSMContext):
    """Allow user to cancel action via /cancel command"""

    current_state = await state.get_state()
    if current_state is None:
        # User is not in any state, ignoring
        return

    # Cancel state and inform user about it
    await state.finish()
    await message.reply("Cancelled.")


@dp.message_handler(state=Form.gid)
async def process_gid(message: types.Message, state: FSMContext):
    """Process group id and add user to db"""
    await state.finish()
    user = message.from_user
    if not re.match(
        r"^(https://)?ruz\.spbstu\.ru/faculty/\d+/groups/\d+$", message.text
    ):
        await message.reply(f"Попробуй еще раз.")
    else:
        gid = re.findall(r"\d+$", message.text)[0]
        res = cur.execute(f"SELECT id FROM users WHERE id='{user['id']}'")
        if not res.fetchone():
            cur.execute(
                f"INSERT INTO users VALUES"
                f"('{user['id']}','{user['first_name']}','{gid}','{user['language_code']}')"
            )
            db_con.commit()
        await message.reply(
            "Отлично теперь ты можешь использовать команду `/schedule`",
            parse_mode=types.message.ParseMode.MARKDOWN_V2,
        )


@dp.message_handler(commands=["schedule", "tschedule"])
async def send_welcome(message: types.Message):
    msg = await message.reply("Parsing...")
    user = message.from_user
    res = cur.execute(f"SELECT gid FROM users WHERE id='{user['id']}'")
    (gid,) = res.fetchone()
    if gid:
        logging.info(message.get_command())
        await msg.edit_text(
            await schedule.get_shedule(
                gid,
                is_tomorrow=(True if message.text == "/tschedule" else False),
            ),
            parse_mode=types.message.ParseMode.MARKDOWN,
        )
    else:
        await msg.edit_text(
            "Тебе нужно зарегистрироваться используя команду `\\start`\!\!\!\!",
            parse_mode=types.message.ParseMode.MARKDOWN_V2,
        )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
