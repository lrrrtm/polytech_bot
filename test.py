import requests

from config import *
from buttons import *
from text import *

import threading
import telebot
import sqlite3
import os
import itertools
import pytz
import xlsxwriter
import dog

from datetime import datetime
from datetime import time as dTime
from bs4 import BeautifulSoup
from docxtpl import DocxTemplate

#ИНИЦИАЛИЗАЦИЯ
bot = telebot.TeleBot(key)
db = sqlite3.connect(f"{mainSource}{dbName}", check_same_thread=False)
cur = db.cursor()

cur.execute(f"select tID, groupID from users")
data = cur.fetchall()

for a in data:
    try:
        s = a[1].split("/")
        cur.execute(f"update users set groupID = \"{s[4]}-{s[6]}\" where tID = {a[0]}")
    except:
        pass

db.commit()