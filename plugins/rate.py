from sys import argv
import requests
from bs4 import BeautifulSoup

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
need beautifulsoup4 module
'''

need = ['курс', 'rate']


USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

LANGUAGE = "en-US,en;q=0.5"


get = ''.join(argv)
get = get[get.index(".py") + 3:]
g = get.split()


if g[0] not in need:
    quit()

main_currency = g[1]

if len(g) > 2:
    your_currency = g[2]

else:
    your_currency = "рубль"




def parse_rate(main, your):
    sess = requests.session()
    sess.headers['USER-AGENT'] = USER_AGENT
    sess.headers['LANGUAGE'] = LANGUAGE
    try:
        get =  sess.get(f"https://www.google.com/search?q=курс+{main}+к{your}").content

        soup = BeautifulSoup(get, 'lxml')

        stupid_string = soup.find("span", attrs={'class':'vLqKYe'}).text

        stupid_string_2 = soup.find("span", attrs={'class':"MWvIVe"}).text
    
        money = soup.find("span",  attrs={'class':'DFlfde SwHCTb'}).text

    except:
        stupid_string = "error"
        stupid_string_2 = "error"
        money = "error"

    return f"1 {stupid_string} = {money} {stupid_string_2}"

print(parse_rate(main_currency, your_currency))



