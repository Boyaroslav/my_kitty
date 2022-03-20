from sys import argv
from random import choice

answers = ["Рада тебя видеть!", "Здравствуй...", "Я по вам соскучилась", "Привет"]

need = ["привет", "здравствуй", "hi", "hello", "good morning", "добрый вечер", "добрый день", "здорова"]

get = ''.join(argv)
get = get[get.index(".py") + 3:]



if get.lower() in need:
    print(choice(answers))
