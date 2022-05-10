
'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''

info = "Поздороваться любыми словами - получишь милость в ответ ;)"

def answer(msg, *args):
    from random import choice

    answers = ["Рада тебя видеть!", "Здравствуй...", "Я по вам соскучилась", "Привет"]

    need = ["привет", "здравствуй", "hi", "hello", "good morning", "добрый вечер", "добрый день", "здорова"]

    

    for i in need:
        if i in msg:
            return choice(answers)
            
