from random import choice


'''
github - https://github.com/bulochkasyablokom
'''


def answer(msg, *args):
    coin = choice(["орел", "решка"])

    need = ["подбрось монетку", "орел или решка", "монетка", "орёл или решка"]

    for i in need:
        if i == msg.lower() or i in msg.lower():
            if coin == "орел":
                return choice([coin.capitalize(), f"Выпал {coin}."])
            elif coin == "решка":
                return choice([coin.capitalize(), f"Выпала {coin}."])
