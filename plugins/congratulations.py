from sys import argv
from random import choice

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''


answers = ["Рада тебя видеть!", "Здравствуй...", "Я по вам соскучилась", "Привет"]

need = ["привет", "здравствуй", "hi", "hello", "good morning", "добрый вечер", "добрый день", "здорова"]

get = ''.join(argv)
get = get[get.index(".py") + 3:].lower()

for i in need:
    if i in get:
        print(choice(answers))
        quit()
