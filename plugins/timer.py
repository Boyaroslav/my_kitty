import time
from os import name as os_name




def answer(msg, *args):
    msg = msg.split()
    if msg[0] not in ["timer", "таймер"]:
        return None



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




    from .. import config
    sleep_time = unit[units] * count
    with timer_tick(sleep_time):
        print("timer hui")
        return window.notify.draw_not("Таймер на", count, un, "звонит!", config.kitty_name)
        return "Таймер поставлен"
    

