import requests

# import aiohttp
# import asyncio

from config import *
from buttons import *
from text import *

import threading
import telebot
import sqlite3
import pytz
import dog
import time

from datetime import datetime, timedelta
from bs4 import BeautifulSoup


# Инициализация бота
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


global scheduleTeacherCurrentDate
scheduleTeacherCurrentDate = datetime.now()


def sndLoc(call, tid, place_id):
    bot.delete_message(tid, call.message.message_id)
    bot.send_location(
        tid,
        latitude=places[place_id]["coords"]["x"],
        longitude=places[place_id]["coords"]["y"],
    )
    text = replyMessage_6.format(
        places[place_id]["fullname"], places[place_id]["address"]
    )
    bot.send_message(tid, text, parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        chat_id = call.message.chat.id
        msg_id = call.message.id
        if call.data == "reg_start":
            bot.edit_message_reply_markup(chat_id, message_id=msg_id, reply_markup=None)
            text = regMessage_1
            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            msg = bot.send_message(
                chat_id, text, parse_mode="Markdown", reply_markup=markup
            )
            bot.register_next_step_handler(msg, inputName)

        elif call.data == "reg_link":
            bot.delete_message(chat_id, call.message.message_id)
            text = replyMessage_2
            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            markup.add(buttons["navigation"]["cancel"])
            msg = bot.send_message(
                chat_id, text, parse_mode="Markdown", reply_markup=markup
            )
            bot.register_next_step_handler(msg, addLink)

        elif call.data == "nav_cancel":
            bot.clear_step_handler_by_chat_id(chat_id=chat_id)
            bot.delete_message(chat_id, call.message.message_id)
            text = replyMessage_4
            bot.send_message(chat_id, text, parse_mode="Markdown")

        elif call.data.startswith("map_") and call.data in places:
            sndLoc(call.data)

        elif call.data == "settings_name":
            bot.delete_message(chat_id, call.message.message_id)
            try:
                lock.acquire(True)
                cur.execute(f"select name,  tID from users where tID = {chat_id}")
                name = cur.fetchall()[0][0]
            finally:
                lock.release()
            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            markup.add(buttons["navigation"]["cancel"])
            text = settingsMessage_1.format(name)
            msg = bot.send_message(
                chat_id, text, parse_mode="Markdown", reply_markup=markup
            )
            bot.register_next_step_handler(msg, editName)

        elif call.data == "settings_group":
            bot.delete_message(chat_id, call.message.message_id)
            text = settingsMessage_2
            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            markup.add(buttons["navigation"]["cancel"])
            msg = bot.send_message(
                chat_id, text, parse_mode="Markdown", reply_markup=markup
            )
            bot.register_next_step_handler(msg, editLink)

        elif call.data == "settings_help":
            bot.delete_message(chat_id, call.message.message_id)
            text = settingsMessage_3
            bot.send_message(chat_id, text, parse_mode="Markdown")

        elif call.data == "settings_about":
            bot.delete_message(chat_id, call.message.message_id)
            text = settingsMessage_4
            bot.send_message(chat_id, text, parse_mode="Markdown")

        elif call.data == "sendMessage":
            bot.delete_message(chat_id, call.message.message_id)
            try:
                lock.acquire(True)
                cur.execute(f"select tID, name from users")
                data = cur.fetchall()
            finally:
                lock.release()
            for a in data:
                try:
                    bot.send_message(a[0], allSendMessage, parse_mode="Markdown")
                    time.sleep(1)
                except Exception as e:
                    if "bot was blocked by the user" in str(e):
                        try:
                            lock.acquire(True)
                            cur.execute(f"delete from users where tID = {a[0]}")
                            db.commit()
                        finally:
                            lock.release()
            text = serviceMessage_4
            bot.send_message(chat_id, text, parse_mode="Markdown")

        elif call.data == "settings_restart":
            bot.delete_message(chat_id, call.message.message_id)
            try:
                lock.acquire(True)
                cur.execute(f"delete from users where tID = {chat_id}")
                db.commit()
            except Exception:
                text = errorMessage_5
                bot.send_message(chat_id, text, parse_mode="Markdown")
            finally:
                lock.release()
                startReply(call.message)

        elif call.data == "nav_forward_stud":
            try:
                lock.acquire(True)
                cur.execute(f"select tID, groupID from users where tID = {chat_id}")
                data = cur.fetchall()
                cur.execute(
                    f"select tID, scheduleStudentCurrentDate from users where tID = {chat_id}"
                )
                scheduleStudentCurrentDate = cur.fetchall()[0][1]
                scheduleStudentCurrentDate = datetime.strptime(
                    scheduleStudentCurrentDate, "%Y-%m-%d"
                ).date()
                print(scheduleStudentCurrentDate)
                scheduleStudentCurrentDate += timedelta(1)
                cur.execute(
                    f'update users set scheduleStudentCurrentDate = "{scheduleStudentCurrentDate}" where tID = {chat_id}'
                )
                db.commit()
            except TypeError as e:
                text = errorMessage_11
                bot.send_message(chat_id, text, parse_mode="Markdown")
                print(f"None error\n{chat_id}: {e}")
            finally:
                lock.release()

            gettingData = getSchedule(scheduleStudentCurrentDate, 0, data[0][1])
            match gettingData:
                case -1:
                    text = errorMessage_11
                    bot.send_message(chat_id, text, parse_mode="Markdown")
                case _:
                    text = sendSchedule(chat_id, gettingData)
                    keyboard = telebot.types.ReplyKeyboardRemove()
                    keyboard = telebot.types.ReplyKeyboardMarkup()
                    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                    markup.add(
                        buttons["navigation"]["back_stud"],
                        buttons["navigation"]["forward_stud"],
                    )
                    bot.edit_message_text(
                        text=text,
                        chat_id=chat_id,
                        message_id=msg_id,
                        reply_markup=markup,
                        parse_mode="Markdown",
                    )

        elif call.data == "nav_back_stud":
            try:
                lock.acquire(True)
                cur.execute(f"select tID, groupID from users where tID = {chat_id}")
                data = cur.fetchall()
                cur.execute(
                    f"select tID, scheduleStudentCurrentDate from users where tID = {chat_id}"
                )
                scheduleStudentCurrentDate = cur.fetchall()[0][1]
                scheduleStudentCurrentDate = datetime.strptime(
                    scheduleStudentCurrentDate, "%Y-%m-%d"
                ).date()
                scheduleStudentCurrentDate -= timedelta(1)
                cur.execute(
                    f'update users set scheduleStudentCurrentDate = "{scheduleStudentCurrentDate}" where tID = {chat_id}'
                )
                db.commit()
            finally:
                lock.release()

            gettingData = getSchedule(scheduleStudentCurrentDate, 0, data[0][1])
            match gettingData:
                case -1:
                    text = errorMessage_11
                    bot.send_message(chat_id, text, parse_mode="Markdown")
                case _:
                    text = sendSchedule(chat_id, gettingData)
                    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                    markup.add(
                        buttons["navigation"]["back_stud"],
                        buttons["navigation"]["forward_stud"],
                    )
                    bot.edit_message_text(
                        text=text,
                        chat_id=chat_id,
                        message_id=msg_id,
                        reply_markup=markup,
                        parse_mode="Markdown",
                    )

        elif call.data == "nav_forward_teacher":
            global scheduleTeacherCurrentDate
            scheduleTeacherCurrentDate += timedelta(1)
            # print(scheduleStudentCurrentDate)
            try:
                lock.acquire(True)
                cur.execute(
                    f"select tID, scheduleTeacherCurrentID from users where tID = {chat_id}"
                )
                scheduleTeacherCurrentID = cur.fetchall()[0][1]
                cur.execute(
                    f"select tID, scheduleTeacherCurrentDate from users where tID = {chat_id}"
                )
                scheduleTeacherCurrentDate = cur.fetchall()[0][1]
                scheduleTeacherCurrentDate = datetime.strptime(
                    scheduleTeacherCurrentDate, "%Y-%m-%d"
                ).date()
                scheduleTeacherCurrentDate += timedelta(1)
                cur.execute(
                    f'update users set scheduleTeacherCurrentDate = "{scheduleTeacherCurrentDate}" where tID = {chat_id}'
                )
                db.commit()
            finally:
                lock.release()
            gettingData = getSchedule(
                scheduleTeacherCurrentDate, 1, scheduleTeacherCurrentID
            )
            match gettingData:
                case -1:
                    text = errorMessage_11
                    bot.send_message(chat_id, text, parse_mode="Markdown")
                    # print("1111")
                case _:
                    text = sendSchedule(chat_id, gettingData)
                    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                    markup.add(
                        buttons["navigation"]["back_teacher"],
                        buttons["navigation"]["forward_teacher"],
                    )
                    bot.edit_message_text(
                        text=text,
                        chat_id=chat_id,
                        message_id=msg_id,
                        reply_markup=markup,
                        parse_mode="Markdown",
                    )

        elif call.data == "nav_back_teacher":
            try:
                lock.acquire(True)
                cur.execute(
                    f"select tID, scheduleTeacherCurrentID from users where tID = {chat_id}"
                )
                scheduleTeacherCurrentID = cur.fetchall()[0][1]
                cur.execute(
                    f"select tID, scheduleTeacherCurrentDate from users where tID = {chat_id}"
                )
                scheduleTeacherCurrentDate = cur.fetchall()[0][1]
                scheduleTeacherCurrentDate = datetime.strptime(
                    scheduleTeacherCurrentDate, "%Y-%m-%d"
                ).date()
                scheduleTeacherCurrentDate -= timedelta(1)
                cur.execute(
                    f'update users set scheduleTeacherCurrentDate = "{scheduleTeacherCurrentDate}" where tID = {chat_id}'
                )
                db.commit()
            finally:
                lock.release()
            gettingData = getSchedule(
                scheduleTeacherCurrentDate, 1, scheduleTeacherCurrentID
            )
            match gettingData:
                case -1:
                    text = errorMessage_11
                    bot.send_message(chat_id, text, parse_mode="Markdown")
                case _:
                    text = sendSchedule(chat_id, gettingData)
                    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                    markup.add(
                        buttons["navigation"]["back_teacher"],
                        buttons["navigation"]["forward_teacher"],
                    )
                    bot.edit_message_text(
                        text=text,
                        chat_id=chat_id,
                        message_id=msg_id,
                        reply_markup=markup,
                        parse_mode="Markdown",
                    )


# -----------------------------------------------------------------------------------------


@bot.message_handler(commands=["start"])
def startReply(message):
    telebot.types.ReplyKeyboardRemove()
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
            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            markup.add(buttons["registration"]["start"])
            text = startMessage_1
            bot.send_message(tID, text, reply_markup=markup, parse_mode="Markdown")


@bot.message_handler(commands=["schedule"])
def startDchedule(message):
    tID = message.chat.id
    print(datetime.now(IST).ctime(), f"{tID}/getSchedule()")
    if inDatabase(tID):
        try:
            lock.acquire(True)
            cur.execute(f"select tID, groupID from users where tID = {tID}")
            data = cur.fetchall()
        finally:
            lock.release()
        if data[0][1] == 0:
            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            markup.add(buttons["registration"]["link"])
            text = errorMessage_2
            bot.send_message(tID, text, reply_markup=markup, parse_mode="Markdown")
        else:
            currentDate = datetime.now()
            gettingData = getSchedule(currentDate, 0, data[0][1])
            match gettingData:
                case -1:
                    text = errorMessage_11
                    bot.send_message(tID, text, parse_mode="Markdown")
                case _:
                    text = sendSchedule(tID, gettingData)
                    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                    markup.add(
                        buttons["navigation"]["back_stud"],
                        buttons["navigation"]["forward_stud"],
                    )
                    bot.send_message(
                        tID, text, parse_mode="Markdown", reply_markup=markup
                    )
    else:
        text = errorMessage_5
        bot.send_message(tID, text, parse_mode="Markdown")


@bot.message_handler(commands=["tschedule"])
def startTeacherSchedule(message):
    tID = message.chat.id
    print(datetime.now(IST).ctime(), f"{tID}/getTeacherSchedule()")
    keyboard = telebot.types.ReplyKeyboardMarkup()
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(buttons["navigation"]["cancel"])
    msg = bot.send_message(
        tID,
        scheduleMessage_6,
        parse_mode="Markdown",
        reply_markup=markup,
    )
    bot.register_next_step_handler(msg, teacherSchedule_1)


@bot.message_handler(commands=["routes"])
def startRoutes(message):
    telebot.types.ReplyKeyboardRemove()
    tID = message.chat.id
    if inDatabase(tID):
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            buttons["routes"]["main"],
            buttons["routes"]["chem"],
            buttons["routes"]["mech"],
            buttons["routes"]["hydro_1"],
            buttons["routes"]["hydro_2"],
            buttons["routes"]["hydro_3"],
            buttons["routes"]["nik"],
            buttons["routes"]["stud_1"],
            buttons["routes"]["stud_2"],
            buttons["routes"]["stud_3"],
            buttons["routes"]["stud_4"],
            buttons["routes"]["stud_5"],
            buttons["routes"]["stud_6"],
            buttons["routes"]["stud_9"],
            buttons["routes"]["stud_10"],
            buttons["routes"]["stud_11"],
            buttons["routes"]["stud_15"],
            buttons["routes"]["stud_16"],
            buttons["routes"]["sport"],
            buttons["routes"]["lab"],
            buttons["routes"]["ran"],
            buttons["routes"]["prof_1"],
            buttons["routes"]["prof_2"],
            buttons["routes"]["teach_house"],
            buttons["routes"]["abit"],
            buttons["routes"]["ipm"],
        )
        text = replyMessage_5
        bot.send_message(tID, text, reply_markup=markup, parse_mode="Markdown")
    else:
        text = errorMessage_5
        bot.send_message(tID, text, parse_mode="Markdown")


@bot.message_handler(commands=["settings"])
def startSettings(message):
    telebot.types.ReplyKeyboardRemove()
    tID = message.chat.id
    if inDatabase(tID):
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            buttons["settings"]["name"],
            buttons["settings"]["group"],
            buttons["settings"]["help"],
            buttons["settings"]["about"],
            buttons["settings"]["suggest"],
        )
        text = replyMessage_7
        bot.send_message(tID, text, parse_mode="Markdown", reply_markup=markup)
    else:
        text = errorMessage_5
        bot.send_message(tID, text, parse_mode="Markdown")


@bot.message_handler(commands=["find"])
def startFind(message):
    telebot.types.ReplyKeyboardRemove()
    tID = message.chat.id
    if inDatabase(tID):
        bot.send_message(tID, "Эта функция пока находится в разработке")
    else:
        text = errorMessage_5
        bot.send_message(tID, text, parse_mode="Markdown")


@bot.message_handler(commands=["dogs"])
def startDogs(message):
    telebot.types.ReplyKeyboardRemove()
    tID = message.chat.id
    if inDatabase(tID):
        dog.getDog(directory=f"{mainSource}/cats/", filename=str(tID))
        bot.send_photo(tID, photo=open(f"{mainSource}/cats/{tID}.jpg", "rb"))
    else:
        text = errorMessage_5
        bot.send_message(tID, text, parse_mode="Markdown")


@bot.message_handler(commands=["message"])
def startMessage(message):
    telebot.types.ReplyKeyboardRemove()
    tID = message.chat.id
    if tID in adminList:
        text = serviceMessage_2
        msg = bot.send_message(tID, text, parse_mode="Markdown")
        bot.register_next_step_handler(msg, sendText)


@bot.message_handler(commands=["cats"])
def startCats(message):
    tID = message.chat.id
    if inDatabase(tID):
        getCat(tID)
    else:
        text = errorMessage_5
        bot.send_message(
            tID,
            text,
            parse_mode="Markdown",
            reply_markup=telebot.types.ReplyKeyboardRemove(),
        )


@bot.message_handler(commands=["restart"])
def startRestart(message):
    tID = message.chat.id
    bot.delete_message(tID, message_id=message.id - 1)
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


@bot.message_handler(content_types=["text"])
def startCheckText(message):
    tID = message.chat.id
    localText = message.text
    currentDate = datetime.now(IST)
    if "(" in localText and ")" in localText:
        bot.delete_message(tID, message_id=message.id - 1)
        teacherID = localText[localText.find("(") + 1 : localText.find(")")]
        try:
            lock.acquire(True)
            cur.execute(
                f"update users set scheduleTeacherCurrentID = {int(teacherID)} where tID = {tID}"
            )
            db.commit()
        finally:
            lock.release()
        gettingData = getSchedule(currentDate, 1, teacherID)
        match gettingData:
            case -1:
                text = errorMessage_11
                bot.send_message(tID, text, parse_mode="Markdown")
            case _:
                sendSchedule(tID, gettingData)
                text = sendSchedule(tID, gettingData)
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                markup.add(
                    buttons["navigation"]["back_teacher"],
                    buttons["navigation"]["forward_teacher"],
                )
                bot.send_message(tID, text, parse_mode="Markdown", reply_markup=markup)


def inputName(message):
    tID = message.chat.id
    name = message.text.strip()
    flag = checkName(name)
    if flag == 0:
        try:
            lock.acquire(True)
            cur.execute(
                f'insert into users (tID, name, regFlag, groupID) values ({tID}, "{name.capitalize()}", 1, "0")'
            )
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
        marker1, marker2 = (
            link[link.index("faculty") + 1],
            link[link.index("groups") + 1],
        )
        if "?" in marker2:
            marker2 = marker2[0:5]
        if checkURL(marker1, marker2):
            try:
                lock.acquire(True)
                cur.execute(
                    f'update users set groupID = "{marker1}-{marker2}" where tID = {tID}'
                )
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


def editName(message):
    tID = message.chat.id
    bot.delete_message(tID, int(message.id) - 1)
    name = message.text.strip()
    flag = checkName(name)
    if flag == 0:
        try:
            lock.acquire(True)
            cur.execute(f'update users set name = "{name}" where tID = {tID}')
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
    bot.delete_message(tID, int(mID) - 1)
    link = message.text
    link = link.split("/")
    try:
        marker1, marker2 = (
            link[link.index("faculty") + 1],
            link[link.index("groups") + 1],
        )
        if "?" in marker2:
            marker2 = marker2[0:5]
        if checkURL(marker1, marker2):
            try:
                lock.acquire(True)
                cur.execute(
                    f'update users set groupID = "{marker1}-{marker2}" where tID = {tID}'
                )
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
            count += 1
    if (
        count == len(name)
        and len(name) < 26
        and len(name) > 1
        and len(name.split(" ")) == 1
    ):
        return 0
    elif count != len(name):
        return 1
    elif len(name) > 25:
        return 2
    elif len(name) < 2:
        return 3
    elif len(name.split(" ")) > 1:
        return 4


def checkURL(m1, m2):
    response = requests.get(scheduleStudentLink.format(m1, m2, datetime.now().date()))
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
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(buttons["admin"]["send"], buttons["navigation"]["cancel"])
    bot.send_message(tID, text, reply_markup=markup, parse_mode="Markdown")


def getCat(tID):
    link2 = ""
    while True:
        link = requests.get(catLink).text
        if "jpg" in link:
            link2 = link.split("\/")[4]
            break
    link2 = link2[0 : link2.find('"')]
    r = requests.get(catLinkGet.format(link2))

    with open(f"{mainSource}/cats/{tID}.jpg", "wb") as f:
        f.write(r.content)
        f.close()

    bot.send_photo(tID, open(f"{mainSource}/cats/{tID}.jpg", "rb"))


def getSchedule(inputDate, type: int, groupID: str) -> None | list:
    outputData = []
    try:
        localDate = inputDate.date()
    except AttributeError:
        localDate = inputDate
    requestLink = ""
    match type:
        case 0:  # Студент
            try:
                marker1, marker2 = map(int, groupID.split("-"))
            except Exception as e:
                print(f"Error split {groupID}")
                return None
            requestLink = scheduleStudentLink.format(marker1, marker2, localDate)

        case 1:  # Преподаватель
            marker1 = groupID
            requestLink = scheduleTeacherLink.format(groupID, localDate)

    contents = requests.get(requestLink)
    match contents.status_code:
        case 200:  # Если доступ к странице получен успешно
            outputLessonData = {}
            contents = contents.text
            soup = BeautifulSoup(contents, "lxml")
            curSchedule = soup.find_all("li", class_="schedule__day")
            workingDay = ""
            flag = 0
            for a in curSchedule:
                a = str(a)
                soup = BeautifulSoup(a, "lxml")
                if int(soup.find("div", class_="schedule__date").text[0:2]) == int(
                    localDate.day
                ):
                    workingDay = a
                    flag = 1
                    break
            if flag == 0:
                outputLessonData["name"] = "None"
                outputLessonData["type"] = "None"
                outputLessonData["place"] = "None"
                outputLessonData["teacher"] = "None"
                outputData.append(outputLessonData)
                return [outputData, localDate, type]

            soup = BeautifulSoup(workingDay, "lxml")
            lessonsArr = soup.find_all("li", class_="lesson")

            for lesson in lessonsArr:
                lesson = str(lesson)
                soup = BeautifulSoup(lesson, "lxml")
                subjectName = soup.find("div", class_="lesson__subject").text
                subjectPlace = soup.find("div", class_="lesson__places").text
                subjectTeacher = soup.find("div", class_="lesson__teachers")
                subjectType = soup.find("div", class_="lesson__type").text
                if str(subjectTeacher) == "None":
                    subjectTeacher = "Неизвестно"
                else:
                    subjectTeacher = subjectTeacher.text
                outputLessonData["name"] = subjectName
                outputLessonData["type"] = subjectType
                outputLessonData["place"] = subjectPlace
                outputLessonData["teacher"] = subjectTeacher

                outputData.append(outputLessonData)
                outputLessonData = {}

            # print(outputData)
            return [outputData, localDate, type]

        case 404:
            # print(requestLink)
            return -1


def sendSchedule(tID, inputData):
    keyboard = telebot.types.ReplyKeyboardRemove()
    keyboard = telebot.types.ReplyKeyboardMarkup()
    schedule, scheduleDate, type = inputData[0], inputData[1], inputData[2]
    match type:
        case 0:
            try:
                lock.acquire(True)
                scheduleDate = datetime.strptime(str(scheduleDate), "%Y-%m-%d").date()
                cur.execute(
                    f'update users set scheduleStudentCurrentDate = "{scheduleDate}" where tID = {tID}'
                )
                db.commit()
            finally:
                lock.release()
            if schedule[0]["name"] != "None":
                toSendText = scheduleMessage_1.format(
                    scheduleDate.strftime("%d/%m/%Y")
                )  # ИЗМЕНИТЬ ФОРМАТ
                for lesson in schedule:
                    subjectName = lesson["name"]
                    subjectPlace = lesson["place"]
                    subjectTeacher = lesson["teacher"].strip()
                    subjectType = lesson["type"]
                    line = scheduleMessage_3.format(
                        subjectName, subjectType, subjectPlace, subjectTeacher
                    )
                    toSendText = toSendText + line + "\n\n"
            else:
                toSendText = scheduleMessage_2.format(scheduleDate.strftime("%d/%m/%Y"))

        case 1:
            try:
                lock.acquire(True)
                scheduleDate = datetime.strptime(str(scheduleDate), "%Y-%m-%d").date()
                cur.execute(
                    f'update users set scheduleTeacherCurrentDate = "{scheduleDate}" where tID = {tID}'
                )
                db.commit()
            finally:
                lock.release()
            if schedule[0]["name"] != "None":
                toSendText = scheduleMessage_9.format(
                    schedule[0]["teacher"].strip(), scheduleDate.strftime("%d/%m/%Y")
                )  # ИЗМЕНИТЬ ФОРМАТ
                for lesson in schedule:
                    subjectName = lesson["name"]
                    subjectPlace = lesson["place"]
                    subjectType = lesson["type"]
                    line = scheduleMessage_10.format(
                        subjectName, subjectType, subjectPlace
                    )
                    toSendText = toSendText + line + "\n\n"
            else:
                toSendText = scheduleMessage_2.format(scheduleDate.strftime("%d/%m/%Y"))

    return toSendText


def teacherSchedule_1(message):
    contents = ""
    tID = message.chat.id
    bot.delete_message(chat_id=tID, message_id=int(message.id) - 1)
    localText = message.text.split(" ")
    if len(localText) == 1:
        contents = requests.get(searchTeacherLink + localText[0])
    elif len(localText) > 1:
        localLink = searchTeacherLink
        for a in localText:
            localLink = localLink + a + "%20"
        contents = requests.get(localLink)
    if contents.status_code == 200:
        contents = contents.text
        soup = BeautifulSoup(contents, "lxml")
        teachersList = soup.find_all("div", class_="search-result__title")
        keyboard = telebot.types.ReplyKeyboardRemove()
        keyboard = telebot.types.ReplyKeyboardMarkup()
        if len(teachersList) != 0:
            for a in teachersList:
                cur = str(a)[str(a).find("href") : -10]
                curTeacherID = cur[cur.find("rs/") + 3 : cur.find('">')]
                curTeacherlocalText = cur[cur.find('">') + 2 :]
                keyboard.add(
                    telebot.types.KeyboardButton(
                        text=f"{curTeacherlocalText} ({curTeacherID})"
                    )
                )
            bot.send_message(
                tID, scheduleMessage_7, reply_markup=keyboard, parse_mode="Markdown"
            )

        else:
            bot.send_message(tID, errorMessage_12, parse_mode="Markdown")

    else:
        bot.send_message(tID, errorMessage_11, parse_mode="Markdown")


bot.polling(none_stop=True)
