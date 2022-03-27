import config
from chat_parser import pop_last

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''


name = config.kitty_name



# you can change start message ^ ^
global history

history = [
    [name, "Привет! Рада Тебя видеть!"]
]


def send_msg(msg, user="you"):
    global history
    history.append([user, msg])
    if user == "you":
        pop_last(history[-1])

    

def clear_chat_history():
    global history
    del history[0]


def print_history():
    global history
    print(history)


