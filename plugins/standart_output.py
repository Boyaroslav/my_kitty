from random import choice

#  just to print emoji
from . import emoji 


'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''

def answer(msg, history):
    if len(history) > 2:
        if history.count('plugins.weather') > len(history) // 2:
            return "Извини, мой любимый метеоролог, не поняла тебя ^-^"

        elif history.count('plugins.rate') > len(history) // 2:
            a =  ''.join(["Не могу ответить на твоё послание.", " Но я слышала, что те, кто мониторят курс имеют успех и красивых детей *_*"])
            return a

        elif history.count('plugins.emoji') > len(history) // 2:
            a = str(''.join(["Не могу ответить. Но я знаю, что вы любите смайлики, а потому ",  emoji.answer('smile')]))
            print(a)
            return a
        
        elif history.count('plugins.bawdry') > len(history) // 2:
            return "Не могу ответить тебе. Да так тебе и надо, хам >:["

        elif history.count('plugins.standart_output') > len(history) // 2:
            return choice(['Не поняла. Мы слишком часто не понимаем друг друга...', "Процент нашего недопонимания крайне высок. Что я делаю не так?",
            "Повтори пожалуйста. Надеюсь ты к этому привык", "Мне кажется, что вы мне не по зубам("])

        elif history[-2] == 'plugins.standart_output':
            return "Я опять вас не поняла ;3"



    answer = ["Извини, повтори ещё раз", "Я не поняла. Повтори пожалуйста", "Ой, я запуталась. Прости, ты не мог бы повторить?"]

    return choice(answer)
