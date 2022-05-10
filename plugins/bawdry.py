
from random import choice


'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''

info = "Будет ругать вас за брань"


def answer(arg, *args):

    need = ["хуй", "пизд", "хер", "дроч", "хуё", "хуе", "дерьмо", "гавно", "блять", "блядь", "сука", "еблан"]
    answers = ["фу...", "как некультурно!", "я обиделась.", "какая гадость!", "безобразие!"]



    for i in need:
        if i in arg.lower():
            return choice(answers)
    
    return None

