from sys import argv, path
from random import choice

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''

#  working, but (при очистке остается 1 сообщение, и при попытке выхода появляется системная информаия(pygame))

need = ["clear", "очистить", "удали историю"]

get = ''.join(argv)
get = get[get.index(".py") + 3:]

isd = 0

for i in need:
    if i == get:
        isd = 1
if not isd:
    quit()
        


import sys 
import os

p = str(__file__)

ind = -1

for i in range(2):
    while (p[ind] != "/"):
        ind -= 1
    ind -= 1
ind += 1




sys.path.append(p[:ind])

for i in need:
    if get == i:
        from window import *
        print("очистка...")
        window.clear_chat_history()
        
        quit()
