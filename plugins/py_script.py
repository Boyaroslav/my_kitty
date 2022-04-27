from subprocess import run
import os
'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''
def answer(arg, *args):
    print(arg.split()[0])
    if arg.split()[0] == "python":
        buf = open("buffer.py", "w+")
        buf.writelines(' '.join(arg.split()[1:]))
        buf.close()
        x = os.popen("python3 buffer.py").read()
        os.system("rm -rf buffer.py")

        return x