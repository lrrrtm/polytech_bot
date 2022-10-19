from telebot.types import InlineKeyboardButton as Ikb
from config import places

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
    },
    "routes": {
        "main": Ikb(f"{places['main']['fullname']} 🏛️", callback_data="map_1"),
        "chem": Ikb(f"{places['chem']['fullname']}", callback_data="map_2"),
        "mech": Ikb(f"{places['mech']['fullname']}", callback_data="map_3"),
        "hydro_1": Ikb(f"{places['hydro_1']['fullname']}", callback_data="map_4"),
        "hydro_2": Ikb(f"{places['hydro_2']['fullname']}", callback_data="map_5"),
        "hydro_3": Ikb(f"{places['hydro_3']['fullname']}", callback_data="map_20"),
        "nik": Ikb(f"{places['nik']['fullname']}", callback_data="map_6"),
        "stud_1": Ikb(f"{places['stud_1']['fullname']}", callback_data="map_7"),
        "stud_2": Ikb(f"{places['stud_2']['fullname']}", callback_data="map_8"),
        "stud_3": Ikb(f"{places['stud_3']['fullname']}", callback_data="map_9"),
        "stud_4": Ikb(f"{places['stud_4']['fullname']}", callback_data="map_10"),
        "stud_5": Ikb(f"{places['stud_5']['fullname']}", callback_data="map_11"),
        "stud_6": Ikb(f"{places['stud_6']['fullname']}", callback_data="map_12"),
        "stud_9": Ikb(f"{places['stud_9']['fullname']}", callback_data="map_13"),
        "stud_10": Ikb(f"{places['stud_10']['fullname']}", callback_data="map_14"),
        "stud_11": Ikb(f"{places['stud_11']['fullname']}", callback_data="map_15"),
        "stud_15": Ikb(f"{places['stud_15']['fullname']}", callback_data="map_16"),
        "stud_16": Ikb(f"{places['stud_16']['fullname']}", callback_data="map_17"),
        "sport": Ikb(f"{places['sport']['fullname']}", callback_data="map_18"),
        "lab": Ikb(f"{places['lab']['fullname']}", callback_data="map_19"),
        "ran": Ikb(f"{places['ran']['fullname']}", callback_data="map_21"),
        "prof_1": Ikb(f"{places['prof_1']['fullname']}", callback_data="map_22"),
        "prof_2": Ikb(f"{places['prof_2']['fullname']}", callback_data="map_23"),
        "teach_house": Ikb(
            f"{places['teach_house']['fullname']}", callback_data="map_24"
        ),
        "abit": Ikb(f"{places['abit']['fullname']}", callback_data="map_25"),
        "ipm": Ikb(f"{places['ipm']['fullname']}", callback_data="map_26"),
    },
    "shedule": {
        "tomorrow": Ikb("Расписание на завтра", callback_data="schedule_nextd"),
        "after_tomorrow": Ikb("", callback_data="schedule_nextnextd"),
        "week": Ikb("Расписание на неделю", callback_data="schedule_all"),
    },
    "admin": {"send": Ikb("Отправить ✅", callback_data="sendMessage")},
}