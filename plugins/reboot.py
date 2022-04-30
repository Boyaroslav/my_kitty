
import pygame


def rbt(x):
    import os
    ans = str("python3 " + x + "main.pyw")
    os.system(ans)
    
def answer(msg, *args):
    if msg in ["reboot", "restart", "перезапуск", "перезапустить", "перезагрузка"]:
        import sys
        import threading
        p = str(__file__)

        ind = -1

        for i in range(2):
            while (p[ind] != "/"):
                ind -= 1
            ind -= 1
        ind += 2
        reb_thread = threading.Thread(target=rbt, args=(str(p[:ind]),))
        reb_thread.start()
        from pygame import quit
        return pygame.quit()
        
