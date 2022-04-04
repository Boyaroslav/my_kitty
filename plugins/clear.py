from random import choice
from os import name as os_name

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''



# DONT WORK

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

    from ...my_kitty import window


    for i in need:
        if msg.lower() == i:
            window.clear_chat_history()

            
    return None
            