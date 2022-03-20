import chat_history
from config import path, plugins,kitty_name
import os

#  this one get last user message ans analyze it
def remove_stupid_space(x):
    return x.replace(" ", "")
def pop_last(msg):
    isd = 0
    for pl in plugins:
        print(f'python3 {path}/plugins/{remove_stupid_space(pl)} "{msg[1]}"')
        ans = os.popen(f'python3 {path}/plugins/{remove_stupid_space(pl)} "{msg[1]}"').read()
        print(ans)
        if ans != "":
            chat_history.send_msg(ans[:-1], user=kitty_name)
            isd = 1
            break
        else:
            continue
    print("isd", isd)
    if isd == 0:
        ans = os.popen(f'python3 {path}/plugins/standart_output.py').read()
        chat_history.send_msg(ans[:-1], user=kitty_name)
        print("hui", ans)

