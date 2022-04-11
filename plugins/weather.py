import requests
from bs4 import BeautifulSoup

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
need beautifulsoup4 module
'''

def parse_weather(country, city):
    if country:
        search = f"{country}+{city}"
    else:
        search = city
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

    LANGUAGE = "en-US,en;q=0.5"

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

def answer(msg, *args):

    need = ["погода", "какая сейчас погода", "what is the weather"]


    country, city = None, None


    
    msg = msg.split()

    for i in need:
        if i in msg:
            if len(msg) == 1:
                city = msg[-1]
            else:
                country, city = msg[-2], msg[-1]
            return str(parse_weather(country, city))