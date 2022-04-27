from datetime import datetime

def answer(msg, **args):
    now = datetime.now()
    if msg == "год":
        return now.year
    
    elif msg == "месяц":
        return now.month
    elif msg == "день":
        return now.day
    elif msg == "час":
        return now.hour
    elif msg == "минута":
        return now.minute
    elif msg == "секунда":
        return now.second
    elif msg == "дата":
        return f"{now.year}:{now.month}:{now.day}"
    elif msg == "время":
        return f"{now.hour}:{now.minute}:{now.second}"
