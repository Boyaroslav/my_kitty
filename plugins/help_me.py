import threading
import queue

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''

def get_help():
    import sys
    hlp = []
    sys.path.append("..")
    from config import plugins as ps
    pl = ps.copy()
    pl
    pl.remove("help_me.py")
    for i in pl:
        pl_inf = __import__('plugins', fromlist=[i])

        pl_inf = getattr(pl_inf, i[:i.index('.py')])
        try:
            hlp.append(str(i + " : " + pl_inf.info))
        except:
            hlp.append(str(i + " : ОТСУТСТВУЕТ ИНФОРМАЦИЯ"))
    return hlp

info = "help : то, что ты сейчас видишь"

def answer(msg, *args):
    hlp = get_help()
    print(hlp)

    need = ["помощь", "помоги", "help", "что делать"]

    #hlp = ["Привет! ",  "Это голосовой помощник!", "Вот фразы, которые ты можешь задать 'из коробки':", 
    #    "help : то, что ты сейчас видишь, ",
    #    "echo/say/скажи : вывести фразу на экран",
    #    "Поздороваться любыми словами - получишь милость в ответ ;)" ,
    #    "погода {город} узнать погоду",
    #    "курс  {валюта} узнать курс",
    #    "смайлик - рандомный смайлик",
    #    "1 или 2 или 3 - выбор между 1, 2 и 3",
    #    "set theme тема.txt - установить тему из папки themes",
    #    "reboot - ну вы поняли",
    #    "sys info - информация о системе",
    #    'темы/плагины - ваши плагины и темы',
    #    "можешь также испытать меня на прочность :)"]



    for i in need:
        if msg.lstrip() == i:
            return hlp
            quit()
