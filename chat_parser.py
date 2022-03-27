import chat_history
from config import path, plugins,kitty_name
import os

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''

#  this one get last user message ans analyze it


#def remove_stupid_space(x):
#    return x.replace(" ", "")

# main plugins (you can add your own. Then I'll be offended by you)
# in this list, the smaller the index, the more important plugin is
main_plugs = ['bawdry.py', 'echo.py', 'congratulations.py', 'help_me.py']


def pop_last(msg):
    isd = 0
    # parsing main plugins firstly:
    for pl in main_plugs:
        ans = os.popen(f'python3 {path}/plugins/{pl} "{msg[1]}"').read() 
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
    if isd:
        return None
    # parsing other plugins:
    for pl in plugins:
        ans = os.popen(f'python3 {path}/plugins/{pl} "{msg[1]}"').read()       
        if ans != "":
            ans = ans.split("\\n")
            print(ans)
            # deleting \n in the end
            ans[-1] = ans[-1][:-1]
            for i in ans:
                print(i)
                if "kitty_exit" in i:
                    import window
                    window.exit()
                chat_history.send_msg(i, user=kitty_name)
            isd = 1
            break
        else:
            continue
    print("isd", isd)
    # if kitty can't answer:
    if isd == 0:
        ans = os.popen(f'python3 {path}/plugins/standart_output.py').read()
        chat_history.send_msg(ans[:-1], user=kitty_name)
        print("hui", ans)
    


