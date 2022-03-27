from sys import argv
import requests
from bs4 import BeautifulSoup

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
need beautifulsoup4 module
'''

need = ["погода", "какая сейчас погода", "what is the weather"]


get = ''.join(argv)
get = get[get.index(".py") + 3:]
g = get.split()

country, city = None, None


USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

LANGUAGE = "en-US,en;q=0.5"


def parse_weather(country, city):
    if country:
        search = f"{country}+{city}"
    else:
        search = city

    sess = requests.session()
    sess.headers['USER-AGENT'] = USER_AGENT
    sess.headers['LANGUAGE'] = LANGUAGE
    try:
        get =  sess.get(f"https://www.google.com/search?q=weather+{search}").content

        soup = BeautifulSoup(get, 'lxml')
    
        s_f = soup.find("span",  attrs={'class':'wob_t q8U8x'}).text

    except:
        s_f = "error :("

    return str("сейчас в " + city + " " + s_f + " градусов")


for i in need:
    if i in g:
        g = g[g.index(i) + 1:]
        if len(g) == 1:
            city = g[-1]
        else:
            country, city = g[-2], g[-1]
        print(parse_weather(country, city))