from config import *
from buttons import *
from text import *

import telebot
import sqlite3

# Инициализация
bot = telebot.TeleBot(key)
db = sqlite3.connect(f"{mainSource}{dbName}", check_same_thread=False)
cur = db.cursor()

cur.execute(f"select tID, groupID from users")
data = cur.fetchall()

for a in data:
    try:
        s = a[1].split("/")
        cur.execute(f'update users set groupID = "{s[4]}-{s[6]}" where tID = {a[0]}')
    except:
        pass

db.commit()
