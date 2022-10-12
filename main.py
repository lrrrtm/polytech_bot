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
key = "5761336221:AAEiDuuhrVTfUOUZgWYUfd1Y6kyEb2ZBth4"
bot = telebot.TeleBot(key)
db = sqlite3.connect(f"{mainSource}{dbName}", check_same_thread=False)
cur = db.cursor()

IST = pytz.timezone(timeZone)
dateNow = str(datetime.now(IST))[0:10]
timeNow = str(datetime.now(IST))[11:16]
text = serviceMessage_1
bot.send_message(mainAdminID, serviceMessage_1.format(dateNow, timeNow))
global lock
lock = threading.Lock()
global allSendMessage
allSendMessage = ""
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
            text = replyMessage_6.format(places["main"], address["main"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_2":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[2][0], longitude=location[2][1])
            text = replyMessage_6.format(places["chem"], address["chem"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_3":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[3][0], longitude=location[3][1])
            text = replyMessage_6.format(places["mech"], address["mech"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_4":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[4][0], longitude=location[4][1])
            text = replyMessage_6.format(places["hydro_1"], address["hydro_1"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_5":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[5][0], longitude=location[5][1])
            text = replyMessage_6.format(places["hydro_2"], address["hydro_2"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_6":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[6][0], longitude=location[6][1])
            text = replyMessage_6.format(places["nik"], address["nik"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_7":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[7][0], longitude=location[7][1])
            text = replyMessage_6.format(places["stud_1"], address["stud_1"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_8":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[8][0], longitude=location[8][1])
            text = replyMessage_6.format(places["stud_2"], address["stud_2"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_9":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[9][0], longitude=location[9][1])
            text = replyMessage_6.format(places["stud_3"], address["stud_3"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_10":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[10][0], longitude=location[10][1])
            text = replyMessage_6.format(places["stud_4"], address["stud_4"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_11":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[11][0], longitude=location[11][1])
            text = replyMessage_6.format(places["stud_5"], address["stud_5"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_12":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[12][0], longitude=location[12][1])
            text = replyMessage_6.format(places["stud_6"], address["stud_6"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_13":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[13][0], longitude=location[13][1])
            text = replyMessage_6.format(places["stud_9"], address["stud_9"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_14":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[14][0], longitude=location[14][1])
            text = replyMessage_6.format(places["stud_10"], address["stud_10"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_15":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[15][0], longitude=location[15][1])
            text = replyMessage_6.format(places["stud_11"], address["stud_11"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_16":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[16][0], longitude=location[16][1])
            text = replyMessage_6.format(places["stud_15"], address["stud_15"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_17":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[17][0], longitude=location[17][1])
            text = replyMessage_6.format(places["stud_16"], address["stud_16"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_18":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[18][0], longitude=location[18][1])
            text = replyMessage_6.format(places["sport"], address["sport"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_19":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[19][0], longitude=location[19][1])
            text = replyMessage_6.format(places["lab"], address["lab"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_20":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[20][0], longitude=location[20][1])
            text = replyMessage_6.format(places["hydro_3"], address["hydro_3"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_21":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[21][0], longitude=location[21][1])
            text = replyMessage_6.format(places["ran"], address["ran"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_22":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[22][0], longitude=location[22][1])
            text = replyMessage_6.format(places["prof_1"], address["prof_1"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_23":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[23][0], longitude=location[23][1])
            text = replyMessage_6.format(places["prof_2"], address["prof_2"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_24":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[24][0], longitude=location[24][1])
            text = replyMessage_6.format(places["teach_house"], address["teach_house"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_25":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[25][0], longitude=location[25][1])
            text = replyMessage_6.format(places["abit"], address["abit"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "map_26":
            bot.delete_message(tID, call.message.message_id)
            bot.send_location(tID, latitude=location[26][0], longitude=location[26][1])
            text = replyMessage_6.format(places["ipm"], address["ipm"])
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "settings_name":
            bot.delete_message(tID, call.message.message_id)
            try:
                lock.acquire(True)
                cur.execute(f"select name, tID from users where tID = {tID}")
                name = cur.fetchall()[0][0]
            finally:
                lock.release()
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
            msg = bot.send_message(tID, text, parse_mode="Markdown", reply_markup=markup)
            bot.register_next_step_handler(msg, editLink)

        elif call.data == "settings_help":
            bot.delete_message(tID, call.message.message_id)
            text = settingsMessage_3
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "settings_about":
            bot.delete_message(tID, call.message.message_id)
            text = settingsMessage_4
            bot.send_message(tID, text, parse_mode="Markdown")

        elif call.data == "sendMessage":
            bot.delete_message(tID, call.message.message_id)
            try:
                lock.acquire(True)
                cur.execute(f"select tID, name from users")
                data = cur.fetchall()
            finally:
                lock.release()
            for a in data:
                try:
                    bot.send_message(a[0], allSendMessage, parse_mode="Markdown")
                except Exception as e:
                    if "bot was blocked by the user" in str(e):
                        try:
                            lock.acquire(True)
                            cur.execute(f"delete from users where tID = {a[0]}")
                            db.commit()
                        finally:
                            lock.release()
            text = serviceMessage_4
            bot.send_message(mainAdminID, text, parse_mode="Markdown")

        elif call.data == "settings_restart":
            bot.delete_message(tID, call.message.message_id)
            try:
                lock.acquire(True)
                cur.execute(f"delete from users where tID = {tID}")
                db.commit()
            except Exception:
                text = errorMessage_5
                bot.send_message(tID, text, parse_mode="Markdown")
            finally:
                lock.release()
                startReply(call.message)

        elif call.data == "schedule_nextd":
            bot.delete_message(tID, call.message.message_id)
            getSchedule(tID, 1)

#-----------------------------------------------------------------------------------------

@bot.message_handler(commands=['start'])
def startReply(message):
    tID = message.chat.id
    if str(tID)[0] == "-":
        text = errorMessage_6
        bot.send_message(tID, text, parse_mode="Markdown")
    else:
        try:
            lock.acquire(True)
            cur.execute(f"select regFlag, name from users where tID = {tID}")
            regFlag = cur.fetchall()
        finally:
            lock.release()
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
        try:
            lock.acquire(True)
            cur.execute(f"select tID, groupID from users where tID = {tID}")
            data = cur.fetchall()
        finally:
            lock.release()
        if data[0][1] == 0:
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(reg_2)
            text = errorMessage_2
            bot.send_message(tID, text, reply_markup=markup, parse_mode="Markdown")
        else:
            getSchedule(tID, 0)
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
        markup.add(btn_19, btn_20, btn_21, btn_22, btn_23, btn_24)
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

@bot.message_handler(commands=['dogs'])
def startDogs(message):
    tID = message.chat.id
    if inDatabase(tID):
        dog.getDog(directory=f"{mainSource}/cats/", filename=str(tID))
        bot.send_photo(tID, photo=open(f"{mainSource}/cats/{tID}.jpg", "rb"))
    else:
        text = errorMessage_5
        bot.send_message(tID, text, parse_mode="Markdown")

@bot.message_handler(commands=['message'])
def startMessage(message):
    tID = message.chat.id
    if tID in adminList:
        text = serviceMessage_2
        msg = bot.send_message(tID, text, parse_mode="Markdown")
        bot.register_next_step_handler(msg, sendText)

@bot.message_handler(commands=['cats'])
def startCats(message):
    tID = message.chat.id
    if inDatabase(tID):
        getCat(tID)
    else:
        text = errorMessage_5
        bot.send_message(tID, text, parse_mode="Markdown")
'''
@bot.message_handler(commands=['cats'])
def startCats(message):
    tID = message.chat.id
    text = scheduleMessage_4
    markup = types.InlineKeyboardMarkup(row_width=1)

    msg = bot.send_message(tID, text)
    bot.register_next_step_handler(msg, otherSchedule)
'''

@bot.message_handler(commands=['restart'])
def startRestart(message):
    tID = message.chat.id
    try:
        lock.acquire(True)
        cur.execute(f"delete from users where tID = {tID}")
        db.commit()
    except Exception:
        text = errorMessage_5
        bot.send_message(tID, text, parse_mode="Markdown")
    finally:
        lock.release()
        startReply(message)

#-----------------------------------------------------------------------------------------

def inputName(message):
    tID = message.chat.id
    name = message.text.strip()
    flag = checkName(name)
    flagCheckReg = 0
    try:
        lock.acquire(True)
        cur.execute(f"select tID from users where tID = {tID}")
        if len(cur.fetchall()) > 0:
            flagCheckReg = 1
    finally:
        lock.release()
    if flag == 0 and flagCheckReg == 0:
        try:
            lock.acquire(True)
            cur.execute(f"insert into users (tID, name, regFlag, groupID) values ({tID}, \"{name.capitalize()}\", 1, \"0\")")
            print(datetime.now(IST).ctime(), f"{tID}/{name} зарегистрирован(а)")
            db.commit()
        finally:
            lock.release()
        text = replyMessage_1.format(name.capitalize())
        bot.send_message(tID, text, parse_mode="Markdown")
        text = startMessage_2
        bot.send_message(tID, text, parse_mode="Markdown")
    else:
        if flag == 1:
            text = errorMessage_8
        elif flag == 2:
            text = errorMessage_1
        elif flag == 3:
            text = errorMessage_7
        elif flag == 4:
            text = errorMessage_9
        msg = bot.send_message(tID, text, parse_mode="Markdown")
        bot.register_next_step_handler(msg, inputName)

def addLink(message):
    tID = message.chat.id
    link = message.text
    link = link.split("/")
    try:
        marker1, marker2 = link[link.index("faculty") + 1], link[link.index("groups") + 1]
        if "?" in marker2:
            marker2 = marker2[0:5]
        if checkURL(marker1, marker2):
            try:
                lock.acquire(True)
                cur.execute(f"update users set groupID = \"{scheduleLink.format(marker1, marker2)}\" where tID = {tID}")
                db.commit()
            finally:
                lock.release()
            text = replyMessage_3
            bot.send_message(tID, text, parse_mode="Markdown")
        else:
            text = errorMessage_4
            msg = bot.send_message(tID, text, parse_mode="Markdown")
            bot.register_next_step_handler(msg, addLink)
    except ValueError:
        text = errorMessage_4
        msg = bot.send_message(tID, text, parse_mode="Markdown")
        bot.register_next_step_handler(msg, addLink)

def getSchedule(tID, dayFlag):
    try:
        lock.acquire(True)
        cur.execute(f"select groupID from users where tID = {tID}")
        link = cur.fetchall()[0][0]
    finally:
        lock.release()
    IST = pytz.timezone(timeZone)
    dateNow = datetime.now(IST)
    curDay, curHour = dateNow.day, dateNow.hour
    curMonth, curYear = dateNow.month, dateNow.year
    curMin = dateNow.min
    contents = requests.get(str(link) + f"?date={curYear}-{curMonth}-{curDay}").text
    soup = BeautifulSoup(contents, 'lxml')
    schedules = soup.find_all("li", class_="schedule__day")

    schedule = {}
    for a in schedules:
        text = str(a)
        soup = BeautifulSoup(text, 'lxml')
        date = soup.find("div", class_="schedule__date").text[0:2]
        curSchedule = soup.find("ul", class_="schedule__lessons")
        soup = BeautifulSoup(str(curSchedule), 'lxml')
        lessons = soup.find_all("li", class_="lesson")
        day = []
        for b in lessons:
            text = str(b)
            soup = BeautifulSoup(text, 'lxml')
            subName = soup.find("div", class_="lesson__subject")
            placeName = soup.find("div", class_="lesson__places")
            teacherName = soup.find("div", class_="lesson__teachers")
            typeName = soup.find("div", class_="lesson__type")
            time = soup.find("span", class_="lesson__time").text.split("-")
            if str(teacherName) == "None":
                teacherName = "Несколько преподавателей/преподаватель отсутствует"
            else:
                teacherName = teacherName.text.strip()
            lesson = {
                "date": int(date),
                "time": time,
                "subject": subName.text,
                "type": typeName.text,
                "place": placeName.text,
                "teacher": teacherName
            }
            day.append(lesson)
        schedule[int(date)] = day

    try:
        print(datetime.now(IST).ctime(), tID, "getSchedule")
        if dayFlag == 1:
            curdaySchedule = schedule[curDay+1]
        elif dayFlag == 0:
            curdaySchedule = schedule[curDay]
    except KeyError:
        if int(dateNow.weekday()) + 1 == 6:
            bot.send_message(tID, scheduleMessage_2.format(curDay, curMonth, curYear), parse_mode="Markdown")
        else:
            text = errorMessage_10
            bot.send_message(tID, text)
        return 0

    endingLastLesson = int(curdaySchedule[-1]["time"][1].split(":")[0])
    if curHour <= endingLastLesson:
        if dayFlag == 1: message = scheduleMessage_1.format(curDay+1, curMonth, curYear) + "\n"
        else: message = scheduleMessage_1.format(curDay, curMonth, curYear) + "\n"

        for a in curdaySchedule:
            time_ = a['time']
            start, end = dateNow.replace(hour=int(time_[0].split(":")[0]),
                                         minute=int(time_[0].split(":")[1])), \
                         dateNow.replace(hour=int(time_[1].split(":")[0]),
                                         minute=int(time_[1].split(":")[1]))
            if curDay == a['date']:
                if dateNow >= start and dateNow < end:
                    sign = "🟢"
                elif dateNow < start:
                    sign = "🟠"
                elif dateNow > end:
                    sign = "🔴"
                else: sign = ""
            else: sign = ""
            subject = a['subject']
            type = a['type']
            place = a['place']
            teacher = a['teacher']
            curLessonText = scheduleMessage_3.format(sign, subject, type, place, teacher)
            message += curLessonText + "\n\n"
        markup = types.InlineKeyboardMarkup(row_width=1)
        if int(dateNow.weekday()) + 1 != 6 and dayFlag == 0:
            markup.add(btn_27)
        bot.send_message(tID, message, parse_mode="Markdown", reply_markup=markup)
    else:
        if int(dateNow.weekday()) + 1 == 6:
            bot.send_message(tID, scheduleMessage_2.format(curDay, curMonth, curYear), parse_mode="Markdown")
        else:
            try:
                curdaySchedule = schedule[curDay+1]
            except KeyError:
                text = scheduleMessage_5
                bot.send_message(tID, text, parse_mode="Markdown")
            message = "*Занятия на сегодня закончились*\n" + scheduleMessage_1.format(int(curDay)+1, curMonth, curYear) + "\n"

            for a in curdaySchedule:
                time_ = a['time']
                sign = ""
                subject = a['subject']
                type = a['type']
                place = a['place']
                teacher = a['teacher']
                curLessonText = scheduleMessage_3.format(sign, subject, type, place, teacher)
                message += curLessonText + "\n\n"
            bot.send_message(tID, message, parse_mode="Markdown")



def editName(message):
    tID = message.chat.id
    name = message.text.strip()
    flag = checkName(name)
    if flag == 0:
        try:
            lock.acquire(True)
            cur.execute(
                f"update users set name = \"{name}\" where tID = {tID}")
            db.commit()
        finally:
            lock.release()
        text = replyMessage_8.format(name.capitalize())
        bot.send_message(tID, text, parse_mode="Markdown")
    else:
        if flag == 1:
            text = errorMessage_8
        elif flag == 2:
            text = errorMessage_1
        elif flag == 3:
            text = errorMessage_7
        elif flag == 4:
            text = errorMessage_9
        msg = bot.send_message(tID, text, parse_mode="Markdown")
        bot.register_next_step_handler(msg, editName)

def editLink(message):
    tID = message.chat.id
    mID = message.id
    link = message.text
    link = link.split("/")
    try:
        marker1, marker2 = link[link.index("faculty") + 1], link[link.index("groups") + 1]
        if "?" in marker2:
            marker2 = marker2[0:5]
        if checkURL(marker1, marker2):
            try:
                lock.acquire(True)
                cur.execute(f"update users set groupID = \"{scheduleLink.format(marker1, marker2)}\" where tID = {tID}")
                db.commit()
            finally:
                lock.release()
            text = replyMessage_9
            bot.send_message(tID, text, parse_mode="Markdown")
        else:
            text = errorMessage_4
            msg = bot.send_message(tID, text, parse_mode="Markdown")
            bot.register_next_step_handler(msg, editLink)
    except ValueError as e:
        text = errorMessage_4
        msg = bot.send_message(tID, text, parse_mode="Markdown")
        bot.register_next_step_handler(msg, addLink)

def checkName(name):
    count = 0
    for a in name:
        if a.upper() in alphabet:
            count +=1
    if count == len(name) and len(name) < 26 and len(name) > 1 and len(name.split(" ")) == 1:
        return 0
    elif count != len(name):
        return 1
    elif len(name) > 25:
        return 2
    elif len(name) < 2:
        return 3
    elif len(name.split(" ")) > 1:
        return 4

def checkURL(m1,m2):
    response = requests.get(scheduleLink.format(m1, m2))
    if int(response.status_code) == 200:
        return True
    else:
        return False

def inDatabase(tID):
    try:
        lock.acquire(True)
        cur.execute(f"select regFlag from users where tID = {tID}")
        flag = cur.fetchall()
    finally:
        lock.release()
    if len(flag) == 0:
        return False
    return True

def sendText(message):
    global allSendMessage
    tID = message.chat.id
    inputText = message.text.strip()
    allSendMessage = inputText
    text = serviceMessage_3.format(inputText)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(btn_34, btn_11)
    bot.send_message(tID, text, reply_markup=markup, parse_mode="Markdown")


def getCat(tID):
    link2 = ""
    while True:
        link = requests.get(catLink).text
        if "jpg" in link:
            link2 = link.split("\/")[4]
            break
    link2 = link2[0:link2.find("\"")]
    r = requests.get(catLinkGet.format(link2))

    with open(f"{mainSource}/cats/{tID}.jpg", 'wb') as f:
        f.write(r.content)
        f.close()

    bot.send_photo(tID, open(f"{mainSource}/cats/{tID}.jpg",'rb'))
'''
def otherSchedule(message):
    tID = message.chat.id
    marker1, marker2 = message.text.split("/")[0], message.text.split("/")[1]
    if checkOtherUrl(marker1, marker2)
    else:
        text = errorMessage_4
        msg = bot.send_message(tID, text)
        bot.register_next_step_handler(msg, otherSchedule)
'''
bot.polling(none_stop=True)