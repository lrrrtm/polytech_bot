import requests
from PIL import Image
from config import *
from bs4 import BeautifulSoup



def getCat(tID):
    link2 = ""
    while True:
        link = requests.get(catLink).text
        if "jpg" in link:
            link2 = link.split("\/")
            break
    link2 = str(link.split("\/")[4])
    link2 = link2[0:link2.find("\"")]
    r = requests.get(catLinkGet.format(link2))

    with open(f"{mainSource}/cats/{tID}.jpg", 'wb') as f:
        f.write(r.content)
        f.close()

    bot.send_photo(tID, open(f"{mainSource}/cats/{tID}.jpg",'rb'))