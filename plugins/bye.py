from sys import argv
from random import choice

'''
Bobyler Yaroslav 2022
github - https://github.com/Boyaroslav
'''


answers = ["пока(", "прощай...", "пока", "удачи.", "bye-bye", "goodbye", "чао :("]

need = ["пока", "мне пора", "goodbye", "bye", "exit", "quit"]


get = ''.join(argv)

get = get[get.index(".py") + 3:]


for i in need:
    if i in get.lower():
        print(choice(answers))
        print("kitty_exit")
        quit()
