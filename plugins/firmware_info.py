# я ебнуося
'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''

info = "зачем то даю инфу о биосе. Введите 'биос'"

def answer(msg, **args):
    if msg in ["биос", "версия биос", "версия биоса", "bios", "bios version"]:
        return open("/sys/class/dmi/id/bios_version").read()