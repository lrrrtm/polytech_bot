import telebot.types as types
from telebot.types import InlineKeyboardButton as Ikb

from config import *

# Настройки бота

buttons = {
    "registration": {
        "start": Ikb("Начнём!", callback_data="reg_start"),
        "link": Ikb("Отправить данные 📥", callback_data="reg_link"),
    },
    "menu": {
        "shedule": Ikb("Расписание 🗓️", callback_data="menu_schedule"),
        "routes": Ikb("Маршруты 🗺️", callback_data="menu_routes"),
        "reminders": Ikb("Напоминания 🛎️", callback_data="menu_reminders"),
        "finder": Ikb("Найти в Политехе 🔍", callback_data="menu_finder"),
        "settings": Ikb("Настройки ⚙", callback_data="settings"),
    },
    "navigation": {
        "confirm": Ikb("Подтвердить ✅", callback_data="nav_confirm"),
        "cancel": Ikb("Отменить ❌", callback_data="nav_cancel"),
        "add": Ikb("Добавить 🔽", callback_data="nav_add"),
        "save": Ikb("Сохранить ✅", callback_data="nav_save"),
        "update": Ikb("Обновить 🔄", callback_data="nav_update"),
        "edit": Ikb("Изменить 🔄", callback_data="nav_edit"),
        "forward_stud": Ikb("Вперёд ▶", callback_data="nav_forward_stud"),
        "back_stud": Ikb("Назад ◀", callback_data="nav_back_stud"),
        "forward_teacher": Ikb("Вперёд ▶", callback_data="nav_forward_teacher"),
        "back_teacher": Ikb("Назад ◀", callback_data="nav_back_teacher"),
    },
    "settings": {
        "name": Ikb("Изменить имя 🗣️", callback_data="settings_name"),
        "group": Ikb("Изменить номер группы 🎒", callback_data="settings_group"),
        "help": Ikb("Служба поддержки 📢", callback_data="settings_help"),
        "about": Ikb("О боте ℹ", callback_data="settings_about"),
        "suggest": Ikb("Предложить идею ❗", url="https://forms.gle/DWPkHUrd3JGEhd8j8"),
        "restart": Ikb("Настроить заново ♻", callback_data="settings_restart"),
        # btn_25 = Ikb("", callback_data="")
        # btn_26 = Ikb("", callback_data="")
    },
    "routes": {
        "main": Ikb(f"{places['main']} 🏛️", callback_data="map_1"),
        "chem": Ikb(f"{places['chem']}", callback_data="map_2"),
        "mech": Ikb(f"{places['mech']}", callback_data="map_3"),
        "hydro_1": Ikb(f"{places['hydro_1']}", callback_data="map_4"),
        "hydro_2": Ikb(f"{places['hydro_2']}", callback_data="map_5"),
        "hydro_3": Ikb(f"{places['hydro_3']}", callback_data="map_20"),
        "nik": Ikb(f"{places['nik']}", callback_data="map_6"),
        "stud_1": Ikb(f"{places['stud_1']}", callback_data="map_7"),
        "stud_2": Ikb(f"{places['stud_2']}", callback_data="map_8"),
        "stud_3": Ikb(f"{places['stud_3']}", callback_data="map_9"),
        "stud_4": Ikb(f"{places['stud_4']}", callback_data="map_10"),
        "stud_5": Ikb(f"{places['stud_5']}", callback_data="map_11"),
        "stud_6": Ikb(f"{places['stud_6']}", callback_data="map_12"),
        "stud_9": Ikb(f"{places['stud_9']}", callback_data="map_13"),
        "stud_10": Ikb(f"{places['stud_10']}", callback_data="map_14"),
        "stud_11": Ikb(f"{places['stud_11']}", callback_data="map_15"),
        "stud_15": Ikb(f"{places['stud_15']}", callback_data="map_16"),
        "stud_16": Ikb(f"{places['stud_16']}", callback_data="map_17"),
        "sport": Ikb(f"{places['sport']}", callback_data="map_18"),
        "lab": Ikb(f"{places['lab']}", callback_data="map_19"),
        "ran": Ikb(f"{places['ran']}", callback_data="map_21"),
        "prof_1": Ikb(f"{places['prof_1']}", callback_data="map_22"),
        "prof_2": Ikb(f"{places['prof_2']}", callback_data="map_23"),
        "teach_house": Ikb(f"{places['teach_house']}", callback_data="map_24"),
        "abit": Ikb(f"{places['abit']}", callback_data="map_25"),
        "ipm": Ikb(f"{places['ipm']}", callback_data="map_26"),
    },
    "shedule": {
        "tomorrow": Ikb("Расписание на завтра", callback_data="schedule_nextd"),
        # btn_28 = Ikb("", callback_data="schedule_nextnextd")
        "week": Ikb("Расписание на неделю", callback_data="schedule_all")
        # btn_30 = Ikb("", callback_data="")
        # btn_31 = Ikb("", callback_data="")
        # btn_32 = Ikb("", callback_data="")
        # btn_33 = Ikb("", callback_data="")
    },
    "admin": {"send": Ikb("Отправить ✅", callback_data="sendMessage")},
}

# РЕГИСТРАЦИЯ
reg_1 = types.InlineKeyboardButton("Начнём!", callback_data="reg_start")
reg_2 = types.InlineKeyboardButton("Отправить данные 📥", callback_data="reg_link")

# МЕНЮ
btn_1 = types.InlineKeyboardButton("Расписание 🗓️", callback_data="menu_schedule")
btn_2 = types.InlineKeyboardButton("Маршруты 🗺️", callback_data="menu_routes")
btn_3 = types.InlineKeyboardButton("Напоминания 🛎️", callback_data="menu_remember")
btn_4 = types.InlineKeyboardButton("Найти в Политехе 🔍", callback_data="menu_find")
btn_5 = types.InlineKeyboardButton("Настройки ⚙", callback_data="settings")

btn_6 = types.InlineKeyboardButton("", callback_data="")
btn_7 = types.InlineKeyboardButton("", callback_data="")
btn_8 = types.InlineKeyboardButton("", callback_data="")
btn_9 = types.InlineKeyboardButton("", callback_data="")

# -----------------------------------------------------------------------------------------

# НАВИГАЦИЯ
btn_10 = types.InlineKeyboardButton("Подтвердить ✅", callback_data="nav_enter")
btn_11 = types.InlineKeyboardButton("Отменить ❌", callback_data="nav_cancel")
btn_12 = types.InlineKeyboardButton("Добавить 🔽", callback_data="nav_add")
btn_13 = types.InlineKeyboardButton("Сохранить ✅", callback_data="nav_save")
btn_14 = types.InlineKeyboardButton("Обновить 🔄", callback_data="nav_update")
btn_15 = types.InlineKeyboardButton("Изменить 🔄", callback_data="nav_edit")

btn_16 = types.InlineKeyboardButton("Вперёд ▶", callback_data="nav_forward_stud")
btn_17 = types.InlineKeyboardButton("Назад ◀", callback_data="nav_back_stud")
btn_18 = types.InlineKeyboardButton("Вперёд ▶", callback_data="nav_forward_teacher")
btn_35 = types.InlineKeyboardButton("Назад ◀", callback_data="nav_back_teacher")

# -----------------------------------------------------------------------------------------

# НАСТРОЙКИ
btn_19 = types.InlineKeyboardButton("Изменить имя 🗣️", callback_data="settings_name")
btn_20 = types.InlineKeyboardButton(
    "Изменить номер группы 🎒", callback_data="settings_group"
)
btn_21 = types.InlineKeyboardButton("Служба поддержки 📢", callback_data="settings_help")
btn_22 = types.InlineKeyboardButton("О боте ℹ", callback_data="settings_about")

btn_23 = types.InlineKeyboardButton(
    "Предложить идею ❗", url="https://forms.gle/DWPkHUrd3JGEhd8j8"
)
btn_24 = types.InlineKeyboardButton(
    "Настроить заново ♻", callback_data="settings_restart"
)
btn_25 = types.InlineKeyboardButton("", callback_data="")
btn_26 = types.InlineKeyboardButton("", callback_data="")

# -----------------------------------------------------------------------------------------

# МАРШРУТЫ
map_1 = types.InlineKeyboardButton(f"{places['main']} 🏛️", callback_data="map_1")
map_2 = types.InlineKeyboardButton(f"{places['chem']}", callback_data="map_2")
map_3 = types.InlineKeyboardButton(f"{places['mech']}", callback_data="map_3")
map_4 = types.InlineKeyboardButton(f"{places['hydro_1']}", callback_data="map_4")
map_5 = types.InlineKeyboardButton(f"{places['hydro_2']}", callback_data="map_5")
map_6 = types.InlineKeyboardButton(f"{places['nik']}", callback_data="map_6")
map_7 = types.InlineKeyboardButton(f"{places['stud_1']}", callback_data="map_7")
map_8 = types.InlineKeyboardButton(f"{places['stud_2']}", callback_data="map_8")
map_9 = types.InlineKeyboardButton(f"{places['stud_3']}", callback_data="map_9")
map_10 = types.InlineKeyboardButton(f"{places['stud_4']}", callback_data="map_10")
map_11 = types.InlineKeyboardButton(f"{places['stud_5']}", callback_data="map_11")
map_12 = types.InlineKeyboardButton(f"{places['stud_6']}", callback_data="map_12")
map_13 = types.InlineKeyboardButton(f"{places['stud_9']}", callback_data="map_13")
map_14 = types.InlineKeyboardButton(f"{places['stud_10']}", callback_data="map_14")
map_15 = types.InlineKeyboardButton(f"{places['stud_11']}", callback_data="map_15")
map_16 = types.InlineKeyboardButton(f"{places['stud_15']}", callback_data="map_16")
map_17 = types.InlineKeyboardButton(f"{places['stud_16']}", callback_data="map_17")
map_18 = types.InlineKeyboardButton(f"{places['sport']}", callback_data="map_18")
map_19 = types.InlineKeyboardButton(f"{places['lab']}", callback_data="map_19")
map_20 = types.InlineKeyboardButton(f"{places['hydro_3']}", callback_data="map_20")
map_21 = types.InlineKeyboardButton(f"{places['ran']}", callback_data="map_21")
map_22 = types.InlineKeyboardButton(f"{places['prof_1']}", callback_data="map_22")
map_23 = types.InlineKeyboardButton(f"{places['prof_2']}", callback_data="map_23")
map_24 = types.InlineKeyboardButton(f"{places['teach_house']}", callback_data="map_24")
map_25 = types.InlineKeyboardButton(f"{places['abit']}", callback_data="map_25")
map_26 = types.InlineKeyboardButton(f"{places['ipm']}", callback_data="map_26")

# -----------------------------------------------------------------------------------------
#
# РАСПИСАНИЕ
btn_27 = types.InlineKeyboardButton(
    "Расписание на завтра", callback_data="schedule_nextd"
)
btn_28 = types.InlineKeyboardButton("", callback_data="schedule_nextnextd")
btn_29 = types.InlineKeyboardButton(
    "Расписание на неделю", callback_data="schedule_all"
)

btn_30 = types.InlineKeyboardButton("", callback_data="")
btn_31 = types.InlineKeyboardButton("", callback_data="")
btn_32 = types.InlineKeyboardButton("", callback_data="")
btn_33 = types.InlineKeyboardButton("", callback_data="")

# -----------------------------------------------------------------------------------------

# АДМИН
btn_34 = types.InlineKeyboardButton("Отправить ✅", callback_data="sendMessage")
