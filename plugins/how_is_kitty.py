
from sys import argv
from random import choice

'''
Bobyler Yaroslav 2022
github - https://github.com/Boyaroslav
'''


answers = ["хорошо", "fine", "нормально", "у меня все хорошо ;3", "отлично! Спасибо, что интересуешься"]

need = ["как дела", "как ты", "how are you", "все хорошо?", "все в порядке?", "всё хорошо?", "всё в порядке?"]


get = ''.join(argv)
get = get[get.index(".py") + 3:]


for i in need:
    if i in get.lower():
        print(choice(answers))
        quit()
