from config import path, plugins,kitty_name, slash
import os
import importlib

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''

#  this one get last user message ans analyze it


#def remove_stupid_space(x):
#    return x.replace(" ", "")

# main plugins (you can add your own. Then I'll be offended by you)
# in this list, the smaller the index, the more important plugin is

class Parser:
    def __init__(self, history):
        self.main_plugs = ['echo.py', 'congratulations.py', 'help_me.py']
        self.history = history

    def pop_last(self, msg):
        isd = 0
        # parsing main plugins firstly:
        for pl in self.main_plugs:
            pth = "plugins"
            plugin = __import__(pth, fromlist=[ pl])

            plugin = getattr(plugin, pl[:pl.index('.py')])

            ans = plugin.answer(msg[1])

            if ans != None:
                isd = 1
                self.history.send_msg(ans, user=kitty_name)
            

        # parsing other plugins:
        if isd == 0:
            for pl in list(set(plugins) - set(self.main_plugs)):
                pth = "plugins"
                plugin = __import__(pth, fromlist=[ pl])
                print(pl)
                print(plugin)

                plugin = getattr(plugin, pl[:pl.index('.py')])
                print(plugin)

                ans = plugin.answer(msg[1])

                if ans != None:
                    isd = 1
                    self.history.send_msg(ans, user=kitty_name)

            # if kitty can't answer:
            if isd == 0:
                pth = "plugins"
                plugin = __import__(pth, fromlist=[ 'standart_output'])

                plugin = getattr(plugin, 'standart_output')

                ans = plugin.answer(msg[1])

                self.history.send_msg(ans, user=kitty_name)

        


