from config import path, plugins,kitty_name, slash, maxlen_message
import os
import sys

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
        self.main_plugs = ['echo.py', 'congratulations.py', 'help_me.py', 'clear.py', 'bye.py']
        self.history = history
        self.requested = []

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

                if type(ans) == type(self.pop_last):
                    self.history.send_msg(ans, user=kitty_name)
                elif type(ans) == list:
                    for i in ans:
                        while i:
                            if len(i) <= maxlen_message:
                                self.history.send_msg(i, user=kitty_name)
                                ans = ''
                                break
                            else:
                                self.history.send_msg(i[:len(i) % (maxlen_message + 1)], user=kitty_name)
                                i = i[len(i) % (maxlen_message + 1):]
               

                else:
                    while ans:
                        if len(ans) <= maxlen_message:
                            self.history.send_msg(ans, user=kitty_name)
                            ans = ''
                            break
                        else:
                            self.history.send_msg(ans[:len(ans) % (maxlen_message)], user=kitty_name)
                            ans = ans[maxlen_message:]
                break


            

        # parsing other plugins:
        if isd == 0:
            for pl in list(set(plugins) - set(self.main_plugs)):
                pth = "plugins"
                plugin = __import__(pth, fromlist=[ pl])


                plugin = getattr(plugin, pl[:pl.index('.py')])
    
                ans = plugin.answer(msg[1])

                if ans != None:
                    isd = 1
                    if type(ans) == list:
                        for i in ans:
                            while i:
                                if len(i) <= maxlen_message:
                                    self.history.send_msg(i, user=kitty_name)
                                    ans = ''
                                    break
                                else:
                                    self.history.send_msg(i[:len(i) % (maxlen_message + 1)], user=kitty_name)
                                    i = i[len(i) % (maxlen_message + 1):]


                    else:
                        while ans:
                            if len(ans) <= maxlen_message:
                                self.history.send_msg(ans, user=kitty_name)
                                ans = ''
                                break
                            else:
                                self.history.send_msg(ans[:len(ans) % (maxlen_message)], user=kitty_name)
                                ans = ans[maxlen_message:]
                    break

            # if kitty can't answer:
            if isd == 0:
                pth = "plugins"
                plugin = __import__(pth, fromlist=[ 'standart_output'])

                plugin = getattr(plugin, 'standart_output')

                ans = plugin.answer(msg[1], self.requested)

                self.history.send_msg(ans, user=kitty_name)
        self.requested.append(plugin.__name__)




    def clear_requested(self):
        del self.requested[:]
        


