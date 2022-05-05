#  use it to create .desktop file and configure my_kitty
# works on Linux only

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''

import config
import os
from subprocess import Popen, PIPE
try:
    deskt = open("/usr/bin/my_kitty", "w+")
    os.system("chmod +x /usr/bin/my_kitty")
    
    
except:
    deskt = open(os.path.expanduser('~') + "/.local/bin/my_kitty", "w+")
    os.system("chmod +x ~/.local/bin/my_kitty")
    #deskt = open(os.path.expanduser('~'), "/.local/bin/my_kitty.sh")
try:
    deskt2 = open("/usr/share/applications/my_kitty.desktop", "w+")
    
except:
    deskt2 = open(os.path.expanduser('~') + "/.local/share/applications/my_kitty.desktop", "w+")

file = ["[Desktop Entry]\n", "Name = my_kitty\n", "Version=3.7\n", f"Icon = {config.kitty_picture}\n",
        f"Exec = python3 {config.path}main.pyw\n", "Terminal=false\n", "Type = Application\n"]

deskt2.writelines(file)
print("file my_kitty.desktop created!")
deskt2.close()

deskt.write(f"python3 {config.path}main.pyw")
deskt.close()
print("file my_kitty.sh created")

#p = Popen(['sudo', '-S', "echo",  '"python3',  f'{config.path}main.pyw"',  '>', '/usr/bin/my_kitty.sh'], stdin=PIPE, stderr=PIPE,universal_newlines=True)
#sudo_prompt = p.communicate(input())[1]



print("done")

# now you can start my_kitty from your apps bar
