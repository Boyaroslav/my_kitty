import chat_history
from config import path, plugins,kitty_name
import os

'''
Bobyler Yaroslav 2022
github - https://github.com/Boyaroslav
'''

#  this one get last user message ans analyze it
def remove_stupid_space(x):
    return x.replace(" ", "")
def pop_last(msg):
    isd = 0
    for pl in plugins:
        ans = os.popen(f'python3 {path}/plugins/{remove_stupid_space(pl)} "{msg[1]}"').read()
        
        if ans != "":
            ans = ans.split("\\n")
            print(ans)
            # deleting \n in the end
            ans[-1] = ans[-1][:-1]
            for i in ans:
                chat_history.send_msg(i, user=kitty_name)
            isd = 1
            break
        else:
            continue
    print("isd", isd)
    if isd == 0:
        ans = os.popen(f'python3 {path}/plugins/standart_output.py').read()
        chat_history.send_msg(ans[:-1], user=kitty_name)
        print("hui", ans)

