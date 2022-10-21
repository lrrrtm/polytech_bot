#!/usr/bin/env python3

import logging
import re
import sqlite3
from datetime import datetime, timedelta

from aiogram import Bot, Dispatcher, executor, md, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import config
import schedule

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize bot, dispatcher and sqlite connection
storage = MemoryStorage()
bot = Bot(token=config.key)
dp = Dispatcher(bot, storage=storage)
db_con = sqlite3.connect(config.db_path)
cur = db_con.cursor()

# Create db table if not exists
cur.execute(
    """CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        gid INTEGER,
        lang TEXT
    )"""
)
cur.execute(
    """CREATE TABLE IF NOT EXISTS schedule_datetime_states(
        id INTEGER PRIMARY KEY,
        datetime TEXT
    )"""
)

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


@dp.message_handler(commands=["schedule"])
async def send_schedule(message: types.Message):
    """Send schedule for today"""

    msg = await message.reply("Loading...")
    user = message.from_user
    cur.execute(
        f"INSERT OR REPLACE INTO schedule_datetime_states VALUES"
        f"('{user['id']}','{datetime.now()}')"
    )
    await schedule_send_any(user, msg, 0)


@dp.callback_query_handler(lambda cq: cq["data"] == "schedule_prev")
async def schedule_next(callback_query: types.CallbackQuery):
    await schedule_send_any(callback_query.from_user, callback_query.message, -1)


@dp.callback_query_handler(lambda cq: cq["data"] == "schedule_next")
async def schedule_next(callback_query: types.CallbackQuery):
    await schedule_send_any(callback_query.from_user, callback_query.message, 1)


async def schedule_send_any(user: types.User, message: types.Message, step: int):
    res = cur.execute(f"SELECT gid FROM users WHERE id='{user['id']}'")
    try:
        (gid,) = res.fetchone()
        res = cur.execute(
            f"SELECT datetime FROM schedule_datetime_states WHERE id='{user['id']}'"
        )
        dt = datetime.fromisoformat(res.fetchone()[0]) + timedelta(days=step)
        cur.execute(
            f"INSERT OR REPLACE INTO schedule_datetime_states VALUES"
            f"('{user['id']}','{str(dt)}')"
        )
        await message.edit_text(
            await schedule.get_shedule(gid, target_date=dt),
            parse_mode=types.message.ParseMode.MARKDOWN,
        )
        buttons = types.InlineKeyboardMarkup(row_width=2)
        buttons.add(
            types.InlineKeyboardButton(text="◀️", callback_data="schedule_prev"),
            types.InlineKeyboardButton(text="▶️", callback_data="schedule_next"),
        )
        await message.edit_reply_markup(buttons)
    except TypeError:
        await message.edit_text(
            "Тебе нужно зарегистрироваться используя команду `\\start`\!\!\!\!",
            parse_mode=types.message.ParseMode.MARKDOWN_V2,
        )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
