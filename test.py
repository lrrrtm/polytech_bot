from bs4 import BeautifulSoup
import requests
import sqlite3
from config import *
from datetime import datetime
import pytz
import telebot
import types
bot = telebot.TeleBot("5307163611:AAEuyYRyxAU7HReIoTzPt1Wl4EZ1O0LFHgA")

IST = pytz.timezone(timeZone)
dateNow = datetime.now(IST)
curDay, curHour = dateNow.day, dateNow.hour
curMonth, curYear = dateNow.month, dateNow.year
curMin = dateNow.min

searchTeacherLink = "https://ruz.spbstu.ru/search/teacher?q="
openTeacherLink = "https://ruz.spbstu.ru/{0}"
contents = ""
name = input("Введи фамилию преподавателя, если знаешь ФИО полностью, то отправь его мне: ").split(" ")
keyboard = telebot.types.ReplyKeyboardMarkup()
@bot.message_handler(commands=['t'])
    def startT(message):
    if len(name) == 1:
        contents = requests.get(searchTeacherLink + name[0])
    elif len(name) > 1:
        localLink = searchTeacherLink
        for a in name:
            localLink = localLink + a + "%20"
        contents = requests.get(localLink)

    if contents.status_code == 200:
        contents = contents.text
        soup = BeautifulSoup(contents, 'lxml')
        teachersList = soup.find_all("div", class_="search-result__title")
        if len(teachersList) != 0:
            for a in teachersList:
                cur = str(a)[str(a).find("href"):-10]
                curTeacherLink = cur[cur.find("\"/")+2:cur.find("\">")]
                curTeacherName = cur[cur.find("\">")+2:]
                print(curTeacherLink, curTeacherName)
                keyboard.add(telebot.types.KeyboardButton(text=f"{curTeacherName}"))

        else:
            print("Такого преподавателя нет")

    else:
        print("Ошибка")


        msg = bot.send_message(409801981, "Выбери препода", reply_markup=keyboard)
        bot.register_next_step_handler(msg, delkb)

def delkb(message):
    bot.delete_message(message_id=message.id-1)