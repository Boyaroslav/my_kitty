
from random import choice


'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''
def answer(arg):

    need = ["хуй", "пизд", "хер", "дроч", "хуё", "хуе", "дерьмо", "гавно", "блять", "блядь"]
    answers = ["фу...", "как некультурно!", "я обиделась.", "какая гадость!", "безобразие!"]



    for i in need:
        if i in arg.lower():
            return choice(answers)
    
    return None

