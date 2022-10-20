import aiohttp
import ujson
from datetime import datetime
import logging


async def get_shedule(
    gid: str,
    is_teacher: bool = False,
    is_tomorrow: bool = False,
) -> None | str:
    if is_teacher:
        # мне пока что похуй на учителей (извините) если что сами добавите
        # schedule_url = "https://ruz.spbstu.ru/teachers/{gid}"
        return None
    else:
        schedule_url: str = f"https://ruz.spbstu.ru/api/v1/ruz/scheduler/{gid}"

    async with aiohttp.ClientSession() as session:
        async with session.get(schedule_url) as res:
            schedule_json = ujson.loads(await res.text())
            logging.debug(schedule_json)
            if not schedule_json["days"]:
                return "Радуйся политехник, на эту неделю занатия не поставлены!"

            weekday = datetime.now().weekday()

            if is_tomorrow and not schedule_json["days"][weekday + 1]:
                return "Радуйся политехник, завтра у тебя нет пар!"

            try:
                schedule = "\n".join(
                    [
                        f"🔸`{a['time_start']}-{a['time_end']}`\n"
                        f"🔸_{a['subject']}_\n"
                        f"🔸*{a['typeObj']['name']}*\n"
                        f"🔸*{a['auditories'][0]['building']['name']}, ауд. {a['auditories'][0]['name']}*\n"
                        f"🔸*{'Неизвестно' if a['teachers'] == None else a['teachers'][0]['full_name']}*\n"
                        for a in schedule_json["days"][weekday + is_tomorrow]["lessons"]
                    ]
                )
                return schedule
            except TypeError or KeyError:
                return "Извини!!! Сервер политеха вернул какую то хуйню вместо расписания которую я не смог распарсить!!!!(((((!"
