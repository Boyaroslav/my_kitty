'''
Bobyler Yaroslav 2022
github - https://github.com/Boyaroslav
'''

info = "Вычислю за вас любой пример"

def answer(msg, *args):
    try:
        return str(eval(msg))
    except:
        pass