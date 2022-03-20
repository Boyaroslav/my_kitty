from sys import argv
from random import choice

'''
Bobyler Yaroslav 2022
github - https://github.com/Boyaroslav
'''


answers = ["Рада тебя видеть!", "Здравствуй...", "Я по вам соскучилась", "Привет"]

need = ["привет", "здравствуй", "hi", "hello", "good morning", "добрый вечер", "добрый день", "здорова"]

get = ''.join(argv)
get = get[get.index(".py") + 3:]


for i in need:
    if i in get.lower():
        print(choice(answers))
        quit()
