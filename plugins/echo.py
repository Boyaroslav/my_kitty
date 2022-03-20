from sys import argv

'''
Bobylev Yaroslav 2022
analog of echo script
'''



get = ''.join(argv)
get = get[get.index(".py") + 3:]
g = get.split()


if "скажи" == g[0]:
    print(' '.join(g[1:]))
    quit()
elif "say" == g[0]:
    print(' '.join(g[1:]))
    quit()
elif "echo" == g[0]:
    print(' '.join(g[1:]))
    quit()