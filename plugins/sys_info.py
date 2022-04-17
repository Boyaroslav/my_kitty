'''
Bobylev Yaroslav
https://github.com/Boyaroslav
'''

def answer(msg, *args):
    if msg not in ["system information", "информация о системе", "sys info", "neofetch", "система", "моя система", "my system"]:
        return None
    import os
    ans = []
    if os.name == "nt":
        return "Windows"

    try:
        x = open("/etc/os-release").readlines()
        keys = {"PRETTY_NAME":'name', "VERSION":'version'}

        for i in x:
            for j in keys:

                if j == i[:i.index('=')]:

                    ans.append(f"{keys[j]} : {i[i.index(str(j)) + 1 + len(j)::]}")
        
    except:
       ans = ["Not found"]

    return ans
         
