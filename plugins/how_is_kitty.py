
from random import choice

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''
def answer(msg, *args):

    answers = ["хорошо", "fine", "нормально", "у меня все хорошо ;3", "отлично! Спасибо, что интересуешься"]

    need = ["как дела", "как ты", "how are you", "все хорошо?", "все в порядке?", "всё хорошо?", "всё в порядке?"]



    for i in need:
        if i in msg.lower():
            return choice(answers)

