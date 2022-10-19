import aiohttp
import ujson
from datetime import datetime


async def get_shedule(
    gid: str,
    is_teacher: bool = False,
    session: None | aiohttp.ClientSession = None,
) -> None | list[dict]:

    if not session:
        session = aiohttp.ClientSession()

    if is_teacher:
        # мне пока что похуй на учителей (извините) если что сами добавите
        # schedule_url = "https://ruz.spbstu.ru/teachers/{gid}"
        return None
    else:
        schedule_url: str = f"https://ruz.spbstu.ru/api/v1/ruz/scheduler/{gid}"

    async with session.get(schedule_url) as res:
        schedule_json = ujson.loads(await res.text())
        hrs = "\n".join(
            [
                f"_{a['time_start']}-{a['time_end']} {a['subject']}_\n"
                f"*{a['typeObj']['name']}*\n"
                f"*{a['auditories'][0]['building']['name']}, ауд {a['auditories'][0]['name']}*\n"
                f"*{a['teachers'][0]['full_name']}*\n"
                for a in schedule_json["days"][datetime.now().weekday()]["lessons"]
            ]
        )

        return hrs
