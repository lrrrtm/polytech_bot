import logging
from datetime import datetime

import aiohttp
import ujson


async def get_shedule(
    gid: str,
    target_date: datetime = datetime.now(),
    is_teacher: bool = False,
) -> None | str:
    if is_teacher:
        # мне пока что похуй на учителей (извините) если что сами добавите
        # schedule_url = "https://ruz.spbstu.ru/teachers/{gid}"
        return None
    else:
        schedule_url: str = f"https://ruz.spbstu.ru/api/v1/ruz/scheduler/{gid}"

    async with aiohttp.ClientSession() as session:
        async with session.get(
            schedule_url, params={"date": str(target_date.date())}
        ) as res:
            schedule_json = ujson.loads(await res.text())
            logging.debug(schedule_json)
            if not schedule_json["days"]:
                return "Радуйся политехник, на эту неделю занатия не поставлены!"

            weekday = target_date.weekday()

            if weekday == 6:
                return "Воскресенье брат"

            try:
                schedule = f"Расписание на {str(target_date.date())}\n\n" + "\n".join(
                    [
                        f"🔸`{a['time_start']}-{a['time_end']}`\n"
                        f"🔸_{a['subject']}_\n"
                        f"🔸*{a['typeObj']['name']}*\n"
                        f"🔸*{a['auditories'][0]['building']['name']}, ауд. {a['auditories'][0]['name']}*\n"
                        f"🔸*{'Неизвестно' if not a['teachers'] else a['teachers'][0]['full_name']}*\n"
                        for a in schedule_json["days"][weekday]["lessons"]
                    ],
                )
                return schedule
            except TypeError or KeyError as e:
                logging.error(e)
                return "Извини!!! Сервер политеха вернул какую то хуйню вместо расписания которую я не смог распарсить!!!!(((((!"
