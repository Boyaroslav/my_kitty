from sys import argv
from random import choice


'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''


need = ["хуй", "пизд", "хер", "дроч", "хуё", "хуе", "дерьмо", "гавно", "блять", "блядь"]
answers = ["фу...", "как некультурно!", "я обиделась.", "какая гадость!", "безобразие!"]

get = ''.join(argv)
get = get[get.index(".py") + 3:]


for i in need:
    if i in get.lower():
        print(choice(answers))
        quit()
