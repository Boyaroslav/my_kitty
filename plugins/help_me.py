from sys import argv
'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''
def answer(msg):

    need = ["помощь", "помоги", "help", "что делать"]

    hlp = "Привет! \\n Это голосовой помощник! \\n Вот фразы, которые ты можешь задать 'из коробки':\\n" + \
        "help : то, что ты сейчас видишь, \\n" + \
        "echo/say/скажи : вывести фразу на экран \\n" + \
        "Поздороваться любыми словами - получишь милость в ответ ;)" 



    for i in need:
        if msg.lstrip() == i:
            return hlp
