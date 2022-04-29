# я ебнуося

def answer(msg, **args):
    if msg in ["биос", "версия биос", "версия биоса", "bios", "bios version"]:
        return open("/sys/class/dmi/id/bios_version").read()