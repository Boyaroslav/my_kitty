import config
from chat_parser import pop_last


name = config.kitty_name


def send_msg(msg, user="you"):
    history.append([user, msg])
    if user == "you":
        pop_last(history[-1])


# you can change start message ^ ^

history = [
    [name, "Привет! Рада Тебя видеть!"]
]