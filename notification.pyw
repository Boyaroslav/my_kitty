import pygame
from config import notify_size, button_color1, text_font, text_font_size, chat_color, kitty_picture
from sys import argv


'''
Bobylev Yaroslav 2022
Github - https://github.com/Boyaroslav
'''
class Notify:
    def __init__(self, msg):
        #msg = ''.join(msg)
        #msg = msg[msg.index(".py") + 3:]
        print(msg)
        pygame.init()
        pygame.font.init()
        
        self.notify_root = pygame.display.set_mode(notify_size)

        self.clock = pygame.time.Clock()

        self.msg = msg

        fnt  = pygame.font.SysFont(text_font, text_font_size)

        self.text = fnt.render(msg, True, chat_color)
        pygame.display.set_caption("Уведомление my_kitty")
        icon = pygame.image.load(kitty_picture)
        pygame.display.set_icon(icon)



    def start(self):
    

        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    quit()
            self.notify_root.fill(button_color1)
            self.notify_root.blit(self.text, (notify_size[0] // 4  - 10, notify_size[1] // 2 - 10))
            
            pygame.display.update()
            self.clock.tick(30)


N = Notify(str(argv[1]))

N.start()