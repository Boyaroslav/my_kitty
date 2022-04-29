from random import choice

'''
Bobyler Yaroslav 2022
github - https://github.com/Boyaroslav
'''
def answer(msg, *args):


    answers = ["пока(", "прощай...", "пока", "удачи.", "bye-bye", "goodbye", "чао :("]

    need = ["пока", "мне пора", "goodbye", "bye", "exit", "quit"]


    for i in need:
        if i in msg.lower():
            print(choice(answers))
            return quit()
