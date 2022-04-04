from sys import argv
'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''
def answer(msg):

    need = ["помощь", "помоги", "help", "что делать"]

    hlp = ["Привет! ",  "Это голосовой помощник!", "Вот фразы, которые ты можешь задать 'из коробки':", 
        "help : то, что ты сейчас видишь, ",
        "echo/say/скажи : вывести фразу на экран",
        "Поздороваться любыми словами - получишь милость в ответ ;)" ]



    for i in need:
        if msg.lstrip() == i:
            return hlp
