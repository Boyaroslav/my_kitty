

'''
Bobylev Yaroslav 2022
analog of echo script
'''




def answer(msg, *args):
    g = msg.split()

    if "скажи" == g[0]:
        return ' '.join(g[1:])

    elif "say" == g[0]:
        return ' '.join(g[1:])

    elif "echo" == g[0]:
        return ' '.join(g[1:])

    else:
        return None