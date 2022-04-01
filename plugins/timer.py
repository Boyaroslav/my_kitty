import time
from os import name as os_name


def answer(msg):
    if msg[0] not in ["timer", "таймер"]:
        return None

    return "Таймер поставлен!"

    count = int(msg[1])

    unit = msg[2]

    units = {
        'минут': 60,
        'секунд': 1,
        'милисекунд': 0.001,
        "час": 360,

        "minut": 60,
        "secod": 1,
        "millisecond": 0.001,
        "hour": 360 
    }

    if unit not in units:
        un = 1
    else:
        un = units[unit]

    #time.sleep(count * un)

    import sys 


    p = str(__file__)

    ind = -1

    for i in range(2):
        while (p[ind] != slash):
            ind -= 1
        ind -= 1
    ind += 1




    sys.path.append(p[:ind])


    from window import notify
    from config import kitty_name
    window.notify.draw_not("Таймер на", count, un, "звонит!", kitty_name)

