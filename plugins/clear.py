from random import choice
from os import name as os_name

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''


def answer(msg):
    need = ["clear", "очистить", "удали историю"]

    isd = 0

    for i in need:
        if i == msg.lower():
            isd = 1
    if not isd:
        return None
            
    slash = "/"
    if os_name == "nt":
        slash = "\\"

    import sys 

    p = str(__file__)

    ind = -1

    for i in range(2):
        while (p[ind] != slash):
            ind -= 1
        ind -= 1
    ind += 1




    sys.path.append(p[:ind])

    for i in need:
        if msg.lower() == i:
            return "очистка..."
            return window.history.clear_chat_history
    return None
            