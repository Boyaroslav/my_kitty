# NEED PYWAL BEING INSTALLED!!!
# https://github.com/dylanaraps/pywal
import os

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''
info = "установите pywal, чтобы я работал. Я меняю тему в соответствии с картинкой. 'wal {путь}'"

def change(pth):
    try:
        os.system(f"wal -s -t -i {pth}")
    except:
        return "У вас не установлен wal"
    print(os.path.expanduser('~') + "/.cache/wal/colors")
    if os.path.exists(os.path.expanduser('~') + "/.cache/wal/colors"):
        cache = open(os.path.expanduser('~') + "/.cache/wal/colors").readlines()
        # 0 - borders
        # 1 - BG
        # 2 - text
        # 3 - 
        from . import change_theme
        change_theme.change_config(cache)
        return "Отлично! Перезагрузите меня :("
    else:
        return "Wrong path"


def answer(msg, **arg):
    msg = msg.split()
    if msg[0] == 'wal':
        if msg[1:]:
            
            return change(*msg[1:])
        return "Введите wal 'путь до изображения'"