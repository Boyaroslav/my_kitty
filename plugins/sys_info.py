'''
Bobylev Yaroslav
https://github.com/Boyaroslav
'''

info = "neofetch/информация о системе. Даю информацию об ос"

def answer(msg, *args):
    if msg not in ["system information", "информация о системе", "sys info", "neofetch", "система", "моя система", "my system"]:
        return None
    import os
    ans = []
    if os.name == "nt":
        return ["Windows"]

    try:
        HOSTNAME = open("/proc/sys/kernel/hostname").read()
        ans.append("Hostname : " + HOSTNAME)
        x = open("/etc/os-release").readlines()
        keys = {"PRETTY_NAME":'name', "VERSION":'version'}

        for i in x:
            for j in keys:

                if j == i[:i.index('=')]:

                    ans.append(f"{keys[j]} : {i[i.index(str(j)) + 2 + len(j):-2]}")
        DE = os.popen("echo $XDG_CURRENT_DESKTOP").read()
        if ':' in DE:
            DE = DE[DE.index(':') + 1::]
        else:
            pass
        ans.append("DE : " + DE)
        
        MODEL = open("/sys/devices/virtual/dmi/id/product_name", "r").read()
        
        ans.append("MODEL NAME : " + MODEL[:-1])
        
        CPU = open("/proc/cpuinfo").readlines()
        cpu = "not found"
        for i in CPU:
            print(i)
            if "model name" in i:
                cpu = i[i.index(":") + 1::]
                break
        ans.append("CPU : " + cpu)
        
    except:
       ans = ["Not found"]

    return ans
         
