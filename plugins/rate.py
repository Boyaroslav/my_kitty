import requests
from bs4 import BeautifulSoup

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
need beautifulsoup4 module
'''

info = "узнай курсы валют прямо из my_kitty! 'курс {валюта} к {валюта2}'"

def parse_rate(main, your):
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

    LANGUAGE = "en-US,en;q=0.5"
    sess = requests.session()
    sess.headers['USER-AGENT'] = USER_AGENT
    sess.headers['LANGUAGE'] = LANGUAGE

    stupid_string = "not found"

    stupid_string_2 = "not found"

    money = "not found"
    try:
        get =  sess.get(f"https://www.google.com/search?q=курс+{main}+к{your}").content

        soup = BeautifulSoup(get, 'lxml')

        stupid_string = soup.find("span", attrs={'class':'vLqKYe'}).text

        stupid_string_2 = soup.find("span", attrs={'class':"MWvIVe"}).text
    
        money = soup.find("span",  attrs={'class':'DFlfde SwHCTb'}).text

    except:
        pass

    return f"1 {stupid_string} = {money} {stupid_string_2}"

def answer(msg, *args):
    msg = msg.split()

    need = ['курс', 'rate']


    



    if msg[0] not in need:
        return None

    main_currency = msg[1]

    if len(msg) > 2:
        your_currency = msg[2]

    else:
        your_currency = "рубль"

    return parse_rate(main_currency, your_currency)



