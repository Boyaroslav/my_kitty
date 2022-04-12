import time
from os import name as os_name
from config import path


def timer(sleep_time, string):
    time.sleep(sleep_time)
    print("done!")
    #import sys 
    # = str(__file__)

    #ind = -1

    #for i in range(2):
    #    while (p[ind] != "/"):
    #        ind -= 1
    #    ind -= 1
    #ind += 1
    #sys.path.append(p[:ind])
    from subprocess import run
    syst = f'python3 {path}notification.py'
    run(['python3',  f'{path}notification.py',  f"Таймер {string} истёк!!!"])

    quit()
    #from  notification import Notify
    #x = Notify("Таймер истёк!!!")
    #x.start()

def answer(msg, *args):
    import threading

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
        "секунды":1,
        "минуты":60,
        "часа":360,

        "minut": 60,
        "secod": 1,
        "millisecond": 0.001,
        "hour": 360 
    }
    un = 1
    name = f"{un} секунд"

    for i in units:
        if unit == i:
            un = units[i]
            name = i
    

    #time.sleep(count * un)





    sleep_time = un * count
    name = f'{count} {name}'
    
    thread = threading.Thread(target=timer, args=(sleep_time, name,))
    thread.start()

    return "Таймер поставлен"
    

