'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''
def answer(msg, *args):

    need = ["помощь", "помоги", "help", "что делать"]

    hlp = ["Привет! ",  "Это голосовой помощник!", "Вот фразы, которые ты можешь задать 'из коробки':", 
        "help : то, что ты сейчас видишь, ",
        "echo/say/скажи : вывести фразу на экран",
        "Поздороваться любыми словами - получишь милость в ответ ;)" ,
        "погода {город} узнать погоду",
        "курс  {валюта} узнать курс",
        "смайлик - рандомный смайлик",
        "1 или 2 или 3 - выбор между 1, 2 и 3",
        "set theme тема.txt - установить тему из папки themes",
        "reboot - ну вы поняли",
        "можешь также испытать меня на прочность :)"]



    for i in need:
        if msg.lstrip() == i:
            return hlp
