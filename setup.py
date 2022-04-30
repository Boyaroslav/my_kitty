#  use it to create .desktop file and configure my_kitty
# works on Linux only

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''

import config
import os
deskt = open(os.path.expanduser('~') + "/.local/share/applications/my_kitty.desktop", "w+")

file = ["[Desktop Entry]\n", "Name = my_kitty\n", "Version=3.6.4\n", f"Icon = {config.kitty_picture}\n",
        f"Exec = python3 {config.path}main.pyw\n", "Terminal=false\n", "Type = Application\n"]

deskt.writelines(file)

deskt.close()

# now you can start my_kitty from your apps bar
