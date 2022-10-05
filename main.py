import requests

from config import *
from buttons import *
from text import *

import telebot
import sqlite3
import os
import itertools
import pytz
import xlsxwriter

from datetime import datetime
from bs4 import BeautifulSoup
from docxtpl import DocxTemplate

#ИНИЦИАЛИЗАЦИЯ
bot = telebot.TeleBot(key)
db = sqlite3.connect(f"{mainSource}{dbName}", check_same_thread=False)
cur = db.cursor()

IST = pytz.timezone(timeZone)
dateNow = str(datetime.now(IST))[0:10]
timeNow = str(datetime.now(IST))[11:16]
text = serviceMessage_1
bot.send_message(mainAdminID, serviceMessage_1.format(dateNow, timeNow))

#-----------------------------------------------------------------------------------------

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        tID = call.message.chat.id
        mID = call.message.id
        if call.data == "reg_start":
            bot.edit_message_reply_markup(tID, message_id=mID, reply_markup=None)
            text = regMessage_1
            markup = types.InlineKeyboardMarkup(row_width=1)
            msg = bot.send_message(tID, text, parse_mode="Markdown", reply_markup=markup)
            bot.register_next_step_handler(msg, inputName)

        elif call.data == "reg_link":
            bot.delete_message(tID, call.message.message_id)
            text = replyMessage_2
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(btn_11)
            msg = bot.send_message(tID, text, parse_mode="Markdown", reply_markup=markup)
            bot.register_next_step_handler(msg, addLink)

        elif call.data == "nav_cancel":
            bot.clear_step_handler_by_chat_id(chat_id=tID)
            bot.delete_message(tID, call.message.message_id)
            text = replyMessage_4
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_1":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[1][0], longitude=location[1][1])
            text = replyMessage_6.format(places["main"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_2":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[2][0], longitude=location[2][1])
            text = replyMessage_6.format(places["chem"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_3":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[3][0], longitude=location[3][1])
            text = replyMessage_6.format(places["mech"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_4":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[4][0], longitude=location[4][1])
            text = replyMessage_6.format(places["hydro_1"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_5":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[5][0], longitude=location[5][1])
            text = replyMessage_6.format(places["hydro_2"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_6":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[6][0], longitude=location[6][1])
            text = replyMessage_6.format(places["nik"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_7":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[7][0], longitude=location[7][1])
            text = replyMessage_6.format(places["stud_1"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_8":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[8][0], longitude=location[8][1])
            text = replyMessage_6.format(places["stud_2"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_9":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[9][0], longitude=location[9][1])
            text = replyMessage_6.format(places["stud_3"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_10":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[10][0], longitude=location[10][1])
            text = replyMessage_6.format(places["stud_4"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_11":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[11][0], longitude=location[11][1])
            text = replyMessage_6.format(places["stud_5"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_12":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[12][0], longitude=location[12][1])
            text = replyMessage_6.format(places["stud_6"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_13":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[13][0], longitude=location[13][1])
            text = replyMessage_6.format(places["stud_9"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_14":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[14][0], longitude=location[14][1])
            text = replyMessage_6.format(places["stud_10"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_15":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[15][0], longitude=location[15][1])
            text = replyMessage_6.format(places["stud_11"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_16":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[16][0], longitude=location[16][1])
            text = replyMessage_6.format(places["stud_15"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_17":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[17][0], longitude=location[17][1])
            text = replyMessage_6.format(places["stud_16"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_18":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[18][0], longitude=location[18][1])
            text = replyMessage_6.format(places["sport"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_19":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[19][0], longitude=location[19][1])
            text = replyMessage_6.format(places["lab"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_20":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[20][0], longitude=location[20][1])
            text = replyMessage_6.format(places["hydro_3"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_21":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[21][0], longitude=location[21][1])
            text = replyMessage_6.format(places["ran"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_22":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[22][0], longitude=location[22][1])
            text = replyMessage_6.format(places["prof_1"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_23":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[23][0], longitude=location[23][1])
            text = replyMessage_6.format(places["prof_2"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_24":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[24][0], longitude=location[24][1])
            text = replyMessage_6.format(places["teach_house"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_25":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[25][0], longitude=location[25][1])
            text = replyMessage_6.format(places["abit"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_26":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[26][0], longitude=location[26][1])
            text = replyMessage_6.format(places["abitipm"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "settings_name":
            bot.delete_message(tID, call.message.message_id)
            cur.execute(f"select name, tID from users where tID = {tID}")
            name = cur.fetchall()[0][0]
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(btn_11)
            text = settingsMessage_1.format(name)
            msg = bot.send_message(tID, text, parse_mode="Markdown", reply_markup=markup)
            bot.register_next_step_handler(msg, editName)

        elif call.data == "settings_group":
            bot.delete_message(tID, call.message.message_id)
            text = settingsMessage_2
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(btn_11)
            msg = bot.send_photo(tID, photo=open("reg_link.png", "rb"), caption=text, parse_mode="Markdown", reply_markup=markup)
            bot.register_next_step_handler(msg, editLink)

        elif call.data == "settings_help":
            bot.delete_message(tID, call.message.message_id)
            text = settingsMessage_3
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "settings_about":
            bot.delete_message(tID, call.message.message_id)
            text = settingsMessage_4
            bot.send_message(tID, text, parse_mode="Markdown")

#-----------------------------------------------------------------------------------------

@bot.message_handler(commands=['start'])
def startReply(message):
    tID = message.chat.id
    if str(tID)[0] == "-":
        text = errorMessage_6
        bot.send_message(tID, text, parse_mode="Markdown")
    else:
        cur.execute(f"select regFlag, name from users where tID = {tID}")
        regFlag = cur.fetchall()
        if len(regFlag) > 0 and regFlag[0][0] == 1:
            text = errorMessage_3.format(regFlag[0][1])
            bot.send_message(tID, text, parse_mode="Markdown")
        else:
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(reg_1)
            text = startMessage_1
            bot.send_message(tID, text, reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(commands=['schedule'])
def startDchedule(message):
    tID = message.chat.id
    if inDatabase(tID):
        cur.execute(f"select tID, groupID from users where tID = {tID}")
        data = cur.fetchall()
        if data[0][1] == 0:
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(reg_2)
            text = errorMessage_2
            bot.send_photo(tID, caption=text, reply_markup=markup, parse_mode="Markdown",
                           photo=open("reg_link.png", "rb"))
        else:
            getSchedule(tID)
    else:
        text = errorMessage_5
        bot.send_message(tID, text, parse_mode="Markdown")

@bot.message_handler(commands=['routes'])
def startRoutes(message):
    tID = message.chat.id
    if inDatabase(tID):
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(map_1, map_2, map_3, map_4, map_5, map_6,
                   map_7, map_8, map_9, map_10, map_11, map_12,
                   map_13, map_14, map_15, map_16, map_17, map_18,
                   map_19, map_20, map_21, map_22, map_23, map_24,
                   map_25, map_26)
        text = replyMessage_5
        bot.send_message(tID, text, reply_markup=markup, parse_mode="Markdown")
    else:
        text = errorMessage_5
        bot.send_message(tID, text, parse_mode="Markdown")

@bot.message_handler(commands=['settings'])
def startSettings(message):
    tID = message.chat.id
    if inDatabase(tID):
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(btn_19, btn_20, btn_21, btn_22)
        text = replyMessage_7
        bot.send_message(tID, text, parse_mode="Markdown", reply_markup=markup)
    else:
        text = errorMessage_5
        bot.send_message(tID, text, parse_mode="Markdown")

@bot.message_handler(commands=['find'])
def startFind(message):
    tID = message.chat.id
    if inDatabase(tID):
        bot.send_message(tID, "Эта функция пока находится в разработке")
    else:
        text = errorMessage_5
        bot.send_message(tID, text, parse_mode="Markdown")

@bot.message_handler(commands=['reminders'])
def startFind(message):
    tID = message.chat.id
    if inDatabase(tID):
        bot.send_message(tID, "Эта функция пока находится в разработке")
    else:
        text = errorMessage_5
        bot.send_message(tID, text, parse_mode="Markdown")

#-----------------------------------------------------------------------------------------

def inputName(message):
    tID = message.chat.id
    name = message.text.strip()
    if checkName(name):
        cur.execute(f"insert into users (tID, name, regFlag, groupID) values ({tID}, \"{name.capitalize()}\", 1, \"0\")")
        print(f"{tID}/{name} зарегистрирован(а)")
        db.commit()
        text = replyMessage_1.format(name.capitalize())
        bot.send_message(tID, text, parse_mode="Markdown")
        text = startMessage_2
        bot.send_message(tID, text, parse_mode="Markdown")
    else:
        text = errorMessage_1
        msg = bot.send_message(tID, text, parse_mode="Markdown")
        bot.register_next_step_handler(msg, inputName)

def addLink(message):
    tID = message.chat.id
    text = message.text.split(" ")
    if checkURL(text):
        cur.execute(f"update users set groupID = \"{scheduleLink.format(text[0], text[1])}\" where tID = {tID}")
        db.commit()
        text = replyMessage_3
        bot.send_message(tID, text, parse_mode="Markdown")
    else:
        text = errorMessage_4
        msg = bot.send_message(tID, text, parse_mode="Markdown")
        bot.register_next_step_handler(msg, addLink)

def getSchedule(tID):
    cur.execute(f"select groupID from users where tID = {tID}")
    link = cur.fetchall()[0][0]
    contents = requests.get(link).text
    soup = BeautifulSoup(contents, 'lxml')
    IST = pytz.timezone(timeZone)
    dateNow = str(datetime.now(IST))[0:10]
    timeNow_ = int(str(datetime.now(IST))[11:13])
    schedules = soup.find_all("li", class_="schedule__day")

    for a in schedules:
        text = str(a)
        soup = BeautifulSoup(text, 'lxml')
        date = soup.find("div", class_="schedule__date").text
        curSchedule = soup.find("ul", class_="schedule__lessons")
        soup = BeautifulSoup(str(curSchedule), 'lxml')
        lessons = soup.find_all("li", class_="lesson")
        flag = 0
        mainText = ""
        for b in lessons:
            text = str(b)
            soup = BeautifulSoup(text, 'lxml')
            subName = soup.find("div", class_="lesson__subject")
            placeName = soup.find("div", class_="lesson__places")
            teacherName = soup.find("div", class_="lesson__teachers")
            typeName = soup.find("div", class_="lesson__type")
            time = soup.find("span", class_="lesson__time").text.split("-")
            if str(teacherName) == "None":
                teacherName = "отсутствует"
            else:
                teacherName = teacherName.text
            textFlag = ""
            timeNow = datetime.now(IST)
            timeStart = timeNow.replace(hour=int(time[0].split(":")[0]), minute=int(time[0].split(":")[1]))
            timeEnd = timeNow.replace(hour=int(time[1].split(":")[0]), minute=int(time[1].split(":")[1]))
            if timeStart < timeNow and timeNow < timeEnd and int(date[0:2]) == int(dateNow[-2:]):
                textFlag = "🟢"
            elif timeStart > timeNow and int(date[0:2]) == int(dateNow[-2:]):
                textFlag = "🟠"
            elif timeNow > timeEnd and int(date[0:2]) == int(dateNow[-2:]):
                textFlag = "🔴"
            if timeNow_ > 16:
                if int(date[0:2]) == int(dateNow[-2:]) + 1:
                    flag = 1
                    head = scheduleMessage_1.format(date[0:2], str(dateNow)[-5:-3], str(dateNow)[0:4])
                else:
                    head = scheduleMessage_2.format(date[0:2], str(dateNow)[-5:-3], str(dateNow)[0:4])
            else:
                if int(date[0:2]) == int(dateNow[-2:]):
                    flag = 1
                    head = scheduleMessage_1.format(date[0:2], str(dateNow)[-5:-3], str(dateNow)[0:4])
                else:
                    head = scheduleMessage_2.format(date[0:2], str(dateNow)[-5:-3], str(dateNow)[0:4])
            if flag == 1:
                mainText += f"{textFlag}_{subName.text}_\nТип: *{typeName.text}*\nМесто: *{placeName.text}*\nПреподаватель: *{teacherName}*\n\n"
        result = head + mainText
        if flag == 1:
            bot.send_message(tID, result, parse_mode="Markdown")

def editName(message):
    tID = message.chat.id
    mID = message.id
    name = message.text.strip()
    if checkName(name):
        bot.edit_message_reply_markup(tID, message_id=mID-1, reply_markup=None)
        cur.execute(f"update users set name = \"{name.capitalize()}\" where tID = {tID}")
        db.commit()
        text = replyMessage_8.format(name.capitalize())
        bot.send_message(tID, text, parse_mode="Markdown")
    else:
        text = errorMessage_1
        msg = bot.send_message(tID, text, parse_mode="Markdown")
        bot.register_next_step_handler(msg, editName)

def editLink(message):
    tID = message.chat.id
    mID = message.id
    text = message.text.split(" ")
    if checkURL(text):
        cur.execute(f"update users set groupID = \"{scheduleLink.format(text[0], text[1])}\" where tID = {tID}")
        db.commit()
        text = replyMessage_9
        bot.send_message(tID, text, parse_mode="Markdown")
    else:
        text = errorMessage_4
        msg = bot.send_message(tID, text, parse_mode="Markdown")
        bot.register_next_step_handler(msg, editLink)

def checkName(name):
    count = 0
    for a in name:
        if a.upper() in alphabet:
            count +=1
    if count == len(name):
        return True
    return False

def checkURL(url):
    response = requests.get(scheduleLink.format(url[0], url[1]))
    if int(response.status_code) == 200:
        return True
    return False

def inDatabase(tID):
    cur.execute(f"select regFlag from users where tID = {tID}")
    flag = cur.fetchall()
    if len(flag) == 0:
        return False
    return True

bot.polling(none_stop=True)