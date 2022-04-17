'''

Bobylev Yaroslav 2022
https://github.com/Boyaroslav
'''

import os

def answer(msg, *args):
    
    need_plugs = ["плагины", "какие у меня плагины", "список плагинов", "plugins list", "покажи плагины", "plugins"]

    need_theme = ["темы", "themes", "какие у меня темы", "список тем", "themes list", "покажи темы"]

    for i in need_plugs:
        if msg.rstrip("?") == i:


            plugs_len_inline = 3

            import sys 
            p = str(__file__)

            ind = -1
            if "/" in p:
                slash = "/"

            elif "\\" in p:
                slash = "\\"
            for i in range(1):
                while (p[ind] != slash):
                    ind -= 1
                ind -= 1
            ind += 1

            plugs = os.listdir(p[:ind])
           
            if "__pycache__" in plugs:
                plugs.remove("__pycache__")
            plugs.remove("__init__.py")
            ans = []

            for j in range(len(plugs) // plugs_len_inline):
                ans.append(';\t'.join(plugs[:plugs_len_inline]))
                print(ans[-1])
                del plugs[:plugs_len_inline]
            print(ans)
           
            return ans
    for i in need_theme:
        if msg.rstrip("?") == i:

            theme_len_inline = 3

            import sys
            p = str(__file__)

            ind = -1
            
            if "/" in p:
                slash = "/"

            elif "\\" in p:
                slash = "\\"


            for i in range(2):
                while (p[ind] != slash):
                    ind -= 1
                ind -= 1
            ind += 1
            


            theme = os.listdir(p[:ind] + slash + "themes")

            ans = []
            

            for j in range(len(theme) // theme_len_inline):
                ans.append(';\t'.join(theme[:theme_len_inline]))
                del theme[:theme_len_inline]
            return ans
    return None          
