from random import choice


'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''

def answer(msg, *args):
    msg = msg.split()
    emoji = ["(·^·)", "*\(≖‿≖*\)", "(⌐■_■)", "<(^_^)>", "(0 3 0)", "(/◡_◡) /O",
    "(*^=^)", "	\(`0´)/", "	= _ =", "	(o ____ 0)", "L(° O °L)", "(^_^)", "( ꒡()꒡)",
    "\(°^°)/", "	(-⊙_⊙)", "\_(-_-)_/", "=O_O="]
    if msg != "":
        if msg[0] in ["смайлик", "emoji", "смайл", "smile"]:
            ans = str(choice(emoji))
            return ans